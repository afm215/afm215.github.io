# scripts/

Utility scripts for the Academic Pages template.

## `make-og-image.py`

Generates the default Open Graph / social preview image at
`images/og-image.png` (1200x630 PNG) used by `_includes/seo.html` when a page
does not define its own header image.

```
python3 scripts/make-og-image.py
```

Requirements:

- Python 3 with [Pillow](https://python-pillow.org) (`pip install Pillow`)
- A TrueType font; defaults to DejaVu Sans (`/usr/share/fonts/truetype/dejavu`),
  override with the `FONT_DIR` environment variable
- The site favicon at `images/favicon-512x512.png` (already in the template);
  it is composited as the card logo

The output is byte-reproducible for a given Pillow/font version and is committed
to the repo, so the build itself does not need Pillow.

## `make-thesis-roadmap.py` / `make-hpc-illustration.py`

Matplotlib generators for hand-laid-out figures committed under
`images/research/`:

- `make-thesis-roadmap.py` → `thesis_roadmap.{png,svg}` (manuscript roadmap on `/thesis/`)
- `make-hpc-illustration.py` → `hpc_tooling_teaser.{png,svg}` and
  `sparse_indexing_teaser.{png,svg}` (portfolio teasers for the HPC experimentation tooling
  and sparse matrix optimization projects)

```
python scripts/make-thesis-roadmap.py
python scripts/make-hpc-illustration.py
```

Requirements: Python 3 with `matplotlib` and `numpy`. Fonts fall back to DejaVu Sans
if Segoe UI is unavailable, so output may differ slightly across platforms.
