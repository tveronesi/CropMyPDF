# CropMyPDF

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/tveronesi/CropMyPDF)
[![License](https://img.shields.io/badge/license-unknown-lightgrey.svg)](https://github.com/tveronesi/CropMyPDF)
[![Built for e-readers](https://img.shields.io/badge/built%20for-e--readers-orange.svg)](https://github.com/tveronesi/CropMyPDF)

> **From cluttered PDF to clean, e-reader-friendly reading in seconds.**

**CropMyPDF** is a lightweight graphical tool that removes unnecessary margins from PDF files so they are far more comfortable to read on **Kindle**, **Kobo**, **reMarkable**, and other e-ink devices.

[⭐ Why it matters](#-why-cropmypdf) · [✨ Features](#-features) · [👀 Before / After](#-before--after) · [📚 Featured use cases](#-featured-use-cases) · [🚀 How to use](#-how-to-use) · [📣 Call to action](#-call-to-action)

---

## Why CropMyPDF

PDFs are often designed for paper, not for e-readers. That usually means:

- huge white margins
- tiny content area on small screens
- constant zooming and panning
- slower, less pleasant reading

**CropMyPDF fixes that workflow in a simple, visual way.**

Instead of living with wasted space, you crop the page to the content area you actually want to read.

---

## ✨ Features

- **Visual preview** before cropping
- **Mouse-based selection** to choose the exact area to keep
- **Keeps the cover intact** by leaving the first page untouched
- **Exports a new cropped PDF** next to the original file
- **Fast, simple workflow** with minimal friction
- **Ideal for e-ink readers** and small screens

---

## 👀 Before / After

### Before
A PDF with wide margins wastes most of the screen on blank space.

### After
The same PDF becomes much more readable because the content takes center stage.

**Result:**
- more text visible at once
- less zooming
- less scrolling
- more comfortable reading on e-readers

> **In short:** same PDF, better experience.

> **Screenshot tip:** add a side-by-side image here showing a full-margin page vs the cropped version.

---

## 📚 Featured use cases

### Built for readers who want more page, less paper
CropMyPDF is especially useful when you want to:

- read **papers, manuals, guides, and reports** on a Kindle or Kobo
- make documents more comfortable on a **reMarkable** or other e-ink tablet
- reduce distractions caused by empty margins
- turn dense PDFs into a more focused reading experience
- avoid editing PDFs manually with complex software

### Strong real-world examples
- **Academic papers**: fit more content per page and reduce constant zooming
- **Technical manuals**: make diagrams and instructions easier to follow on small screens
- **Scanned books and notes**: remove wasted whitespace and improve legibility
- **Work reports and documentation**: turn static PDFs into something actually pleasant to read on the go

**It is built for one job:** make PDFs feel made for reading, not just for printing.

---

## 🚀 How to use

```bash
git clone https://github.com/abianchi91/CropMyPDF.git
cd CropMyPDF
pip install -r requirements.txt
python -m cropmypdf
```

You can also run it directly:

```bash
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

## 📣 Call to action

If you like cleaner reading, faster navigation, and a better PDF experience on e-ink devices, **CropMyPDF is the simplest way to get there**.

**Try it, crop a PDF, and read the difference immediately.**

---

## Short promo copy

**CropMyPDF** is a lightweight graphical tool that removes unnecessary PDF margins and makes documents easier to read on Kindle, Kobo, reMarkable, and other e-readers. Preview the page, choose the area to keep with your mouse, and export a cleaner PDF in seconds.
