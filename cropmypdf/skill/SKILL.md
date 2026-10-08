---
name: cropmypdf
description: Crop PDF margins to make PDFs comfortable on e-readers (Kindle, Kobo, reMarkable) and small screens. Use when the user wants to trim white margins, auto-crop a PDF, crop a page range, or prepare a PDF for e-ink reading. Runs the local `cropmypdf` CLI and returns JSON.
---

# CropMyPDF skill

Use the `cropmypdf` command-line tool (installed with the Python package) to crop PDFs
without opening a GUI. Every command prints a single JSON object on stdout.

## Prerequisite

```bash
cropmypdf --version || pip install cropmypdf
```

## Commands

### 1. Auto-crop (best default)
Detects the content area across all pages and removes the surrounding white margins.

```bash
cropmypdf crop input.pdf --auto
```

Output: `input_cropped.pdf` next to the original (override with `-o out.pdf`).

### 2. Manual crop by margins to REMOVE (fractions of the page, 0-1)

```bash
cropmypdf crop input.pdf --margins 0.08 0.05 0.08 0.05   # left top right bottom
```

### 3. Manual crop by box to KEEP (x0 y0 x1 y1, fractions from top-left)

```bash
cropmypdf crop input.pdf --bbox 0.1 0.06 0.9 0.94
```

### 4. Inspect without writing anything

```bash
cropmypdf detect input.pdf
```

Returns the suggested box, e.g. `{"bbox": [0.11, 0.07, 0.89, 0.93]}`.

### Useful options

| Option | Meaning |
|---|---|
| `-o, --output PATH` | Output file (default `<name>_cropped.pdf`) |
| `--start N` / `--end N` | 1-based page range; pages outside are dropped |
| `--no-cover` | Crop page 1 too (by default the cover is kept untouched) |

### Interactive GUI (only if the user wants to pick the area with the mouse)

```bash
cropmypdf gui
```

## Recommended workflow

1. Run `cropmypdf detect file.pdf` and show the user the suggested box if they care about precision.
2. Run `cropmypdf crop file.pdf --auto` (or with the adjusted `--bbox`).
3. Report the `output` path and `pages_written` from the JSON.
4. Never overwrite the original file; always write to a new path.

## Errors

On failure the command exits non-zero and prints `{"error": "..."}`. Typical causes: file not found,
invalid box (values must satisfy 0 <= x0 < x1 <= 1), or missing dependencies (`pip install cropmypdf`).
