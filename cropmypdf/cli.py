"""Command line interface for CropMyPDF (GUI + agent-friendly JSON commands)."""
import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

VERSION = "0.2.0"

# Known agent skill folders. Each one gets <root>/cropmypdf/SKILL.md
SKILL_TARGETS = {
    "claude": Path.home() / ".claude" / "skills",
    "copilot": Path.home() / ".copilot" / "skills",
    "agents": Path.home() / ".agents" / "skills",
}


def _emit(obj, code: int = 0) -> int:
    print(json.dumps(obj, ensure_ascii=False))
    return code


def _skill_source() -> Path:
    return Path(__file__).parent / "skill" / "SKILL.md"


def install_skill(targets: List[str], directory: Optional[str], force: bool) -> int:
    src = _skill_source()
    if not src.is_file():
        return _emit({"error": "Embedded SKILL.md not found: %s" % src}, 1)
    roots = []
    if directory:
        roots.append(Path(directory).expanduser())
    else:
        names = list(SKILL_TARGETS) if "all" in targets else targets
        roots.extend(SKILL_TARGETS[n] for n in names)
    installed, skipped = [], []
    for root in roots:
        dest = root / "cropmypdf" / "SKILL.md"
        if dest.exists() and not force:
            skipped.append(str(dest))
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        installed.append(str(dest))
    return _emit({"installed": installed, "skipped_existing": skipped})


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cropmypdf", description="Crop PDF margins for e-readers.")
    p.add_argument("--version", action="store_true", help="print version and exit")
    sub = p.add_subparsers(dest="command")

    sub.add_parser("gui", help="open the graphical cropper (default)")

    c = sub.add_parser("crop", help="crop a PDF without GUI")
    c.add_argument("input")
    c.add_argument("-o", "--output")
    g = c.add_mutually_exclusive_group(required=True)
    g.add_argument("--auto", action="store_true", help="auto-detect content area")
    g.add_argument("--margins", nargs=4, type=float, metavar=("L", "T", "R", "B"),
                   help="fractions to remove from each side")
    g.add_argument("--bbox", nargs=4, type=float, metavar=("X0", "Y0", "X1", "Y1"),
                   help="fractional box to keep")
    c.add_argument("--start", type=int, help="first page (1-based)")
    c.add_argument("--end", type=int, help="last page (1-based)")
    c.add_argument("--no-cover", action="store_true", help="also crop the first page")

    d = sub.add_parser("detect", help="print the suggested crop box")
    d.add_argument("input")
    d.add_argument("--start", type=int)
    d.add_argument("--end", type=int)
    d.add_argument("--no-cover", action="store_true")

    s = sub.add_parser("install-skill", help="install the embedded AI agent skill")
    s.add_argument("--target", nargs="+", default=["all"],
                   choices=["all"] + list(SKILL_TARGETS), help="agent(s) to install for")
    s.add_argument("--dir", help="custom skills directory (overrides --target)")
    s.add_argument("--force", action="store_true", help="overwrite existing skill")
    return p


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.version:
        print(VERSION)
        return 0
    cmd = args.command or "gui"
    try:
        if cmd == "gui":
            from .pdf_crop import PDFCropTool
            PDFCropTool()
            return 0
        if cmd == "install-skill":
            return install_skill(args.target, args.dir, args.force)
        from . import core
        if cmd == "detect":
            bbox = core.detect_content_bbox(
                args.input, args.start, args.end, skip_cover=not args.no_cover)
            return _emit({"input": args.input, "bbox": [round(v, 4) for v in bbox]})
        if cmd == "crop":
            result = core.crop_pdf(
                args.input,
                output_path=args.output,
                bbox=tuple(args.bbox) if args.bbox else None,
                margins=tuple(args.margins) if args.margins else None,
                auto=args.auto,
                start_page=args.start,
                end_page=args.end,
                include_cover=not args.no_cover,
            )
            return _emit(result)
    except Exception as exc:  # report as JSON for agents
        return _emit({"error": str(exc)}, 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
