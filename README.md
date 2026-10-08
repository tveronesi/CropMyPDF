# CropMyPDF

**CropMyPDF** is a simple graphical tool that helps you remove unnecessary margins from PDF files, making them easier to read on devices like **Kindle**, **Kobo**, **reMarkable** and other e-ink readers.

> Turn cluttered PDFs into clean, e-reader-friendly pages in a few clicks.

---

## Why CropMyPDF?

PDFs often waste precious screen space with large white margins, headers, and footers. On e-readers and small screens this means:

- more zooming
- more panning
- slower reading
- less comfortable reading experience

**CropMyPDF solves this by letting you visually crop the page area you want to keep and export a cleaner version immediately.**

---

## Features

- **Visual preview** of the page before cropping
- **Mouse-based selection** to choose the exact area to keep
- **Keeps the cover intact** by leaving the first page untouched
- **Exports a new cropped PDF** next to the original file
- **Fast and simple workflow** designed for non-technical users
- **Perfect for e-ink devices** and small screens

---

## Concrete use cases

### For Kindle / Kobo / reMarkable readers
Read academic papers, manuals, comics, guides, and documents without wasting screen space on margins.

### For students and researchers
Make lecture notes, papers, and reports more readable and easier to annotate on tablets and e-readers.

### For professionals
Clean up exported reports, contracts, and documentation before sharing them with clients or reading them on the go.

### For anyone tired of zooming
Reduce the need to constantly pinch, pan, and re-center PDF pages on mobile devices.

---

## What makes it appealing?

- **Instant visual feedback** before saving
- **One job, done well**: crop PDFs quickly and cleanly
- **Ideal for e-ink workflows** where every pixel matters
- **Lightweight Python app** with a straightforward setup

---

## Example scenarios

- A 300-page research paper with wide margins becomes much more comfortable to read on a Kindle.
- A reMarkable user can focus on the content instead of blank space.
- A scanned handbook can be trimmed to maximize readability on a Kobo.
- A PDF manual can be made more usable on a phone during travel.

---

## Installation

```bash
git clone https://github.com/abianchi91/CropMyPDF.git
cd CropMyPDF
pip install -r requirements.txt
```

## Usage

```bash
# run as module
python -m cropmypdf

# or run directly
python cropmypdf/pdf_crop.py
```

---

## Requirements

- Python 3.8 or higher
- tkinter (usually comes with Python)
- PyMuPDF (`fitz`)
- Pillow
- NumPy

---

## Suggested tagline ideas

- **CropMyPDF — Read PDFs the way they should have been made for e-readers**
- **From cluttered PDF to clean reading experience**
- **Trim margins. Gain space. Read better.**
- **The fast way to make PDFs Kindle-ready**

---

## Short promo copy

**CropMyPDF** is a lightweight graphical tool that removes unnecessary PDF margins and makes documents easier to read on Kindle, Kobo, reMarkable, and other e-readers. Preview the page, choose the area to keep with your mouse, and export a cleaner PDF in seconds.
