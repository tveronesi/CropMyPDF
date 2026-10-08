"""Headless (no GUI) API for CropMyPDF.

All box coordinates are *fractions* of the page (0.0 - 1.0), measured from the
top-left corner, so one crop box can be applied to pages of any size.
"""
import os
from typing import Dict, Optional, Sequence, Tuple

import fitz  # PyMuPDF
import numpy as np

BBox = Tuple[float, float, float, float]  # x0, y0, x1, y1 (fractions)


def _page_indices(total: int, start_page: Optional[int], end_page: Optional[int]):
    start = (start_page - 1) if start_page else 0
    end = (end_page - 1) if end_page else total - 1
    start = max(0, start)
    end = min(total - 1, end)
    return list(range(start, end + 1))


def detect_content_bbox(
    pdf_path: str,
    start_page: Optional[int] = None,
    end_page: Optional[int] = None,
    skip_cover: bool = True,
    dpi: int = 50,
    threshold: int = 245,
    padding: float = 0.01,
) -> BBox:
    """Detect the union of the non-white content area across pages.

    Returns a fractional bounding box (x0, y0, x1, y1).
    """
    doc = fitz.open(pdf_path)
    try:
        indices = _page_indices(len(doc), start_page, end_page)
        if skip_cover and 0 in indices and len(indices) > 1:
            indices.remove(0)
        x0, y0, x1, y1 = 1.0, 1.0, 0.0, 0.0
        found = False
        for i in indices:
            pix = doc[i].get_pixmap(dpi=dpi, colorspace=fitz.csGRAY, alpha=False)
            arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
            mask = arr < threshold
            if not mask.any():
                continue
            rows = np.where(mask.any(axis=1))[0]
            cols = np.where(mask.any(axis=0))[0]
            x0 = min(x0, cols[0] / pix.width)
            x1 = max(x1, (cols[-1] + 1) / pix.width)
            y0 = min(y0, rows[0] / pix.height)
            y1 = max(y1, (rows[-1] + 1) / pix.height)
            found = True
        if not found:
            return (0.0, 0.0, 1.0, 1.0)
        return (
            max(0.0, x0 - padding),
            max(0.0, y0 - padding),
            min(1.0, x1 + padding),
            min(1.0, y1 + padding),
        )
    finally:
        doc.close()


def crop_pdf(
    input_path: str,
    output_path: Optional[str] = None,
    bbox: Optional[BBox] = None,
    margins: Optional[Sequence[float]] = None,
    auto: bool = False,
    start_page: Optional[int] = None,
    end_page: Optional[int] = None,
    include_cover: bool = True,
) -> Dict:
    """Crop a PDF and save it. Returns a dict describing the result.

    Choose ONE of: ``bbox`` (x0,y0,x1,y1 fractions to keep), ``margins``
    (left,top,right,bottom fractions to remove) or ``auto=True``.
    ``start_page`` / ``end_page`` are 1-based. Pages outside the range are
    dropped (the cover is kept when ``include_cover`` is true).
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(input_path)
    chosen = sum([bbox is not None, margins is not None, bool(auto)])
    if chosen != 1:
        raise ValueError("Provide exactly one of: bbox, margins, auto")

    if auto:
        bbox = detect_content_bbox(
            input_path, start_page, end_page, skip_cover=include_cover
        )
    elif margins is not None:
        left, top, right, bottom = margins
        bbox = (left, top, 1.0 - right, 1.0 - bottom)

    x0, y0, x1, y1 = bbox
    if not (0.0 <= x0 < x1 <= 1.0 and 0.0 <= y0 < y1 <= 1.0):
        raise ValueError("Invalid crop box: %r" % (bbox,))

    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = base + "_cropped.pdf"

    doc = fitz.open(input_path)
    new_pdf = fitz.open()
    pages_written = 0
    try:
        for page in doc:
            if page.number == 0 and include_cover:
                new_pdf.insert_pdf(doc, from_page=0, to_page=0)
                pages_written += 1
                continue
            if start_page is not None and page.number < start_page - 1:
                continue
            if end_page is not None and page.number > end_page - 1:
                continue
            pw, ph = page.rect.width, page.rect.height
            page.set_cropbox(fitz.Rect(x0 * pw, y0 * ph, x1 * pw, y1 * ph))
            new_pdf.insert_pdf(doc, from_page=page.number, to_page=page.number)
            pages_written += 1
        new_pdf.save(output_path)
    finally:
        new_pdf.close()
        doc.close()

    return {
        "input": os.path.abspath(input_path),
        "output": os.path.abspath(output_path),
        "pages_written": pages_written,
        "bbox": [round(v, 4) for v in (x0, y0, x1, y1)],
    }
