# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf>=1.26"]
# ///
"""Render PDF pages to PNG for side-by-side visual review against the Markdown.

Also prints, per page, what to look at (tables, boxes, code, images, links)
and the first and last words of the page's body text outside tables, so the
matching Markdown section can be found with a quick search.

Usage:
  uv run render_pages.py input.pdf --out DIR [--pages 1,3-5] [--dpi 80]
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf

import pdf_layout as L


def parse_pages(spec: str | None, n: int) -> list[int]:
    if not spec:
        return list(range(1, n + 1))
    pages: list[int] = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            pages += range(int(a), int(b) + 1)
        else:
            pages.append(int(part))
    return [p for p in pages if 1 <= p <= n]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--pages", help="e.g. 1,3-5 (default: all)")
    ap.add_argument("--dpi", type=int, default=80, help="80 is enough to read body text; raise for small print")
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    layout = L.analyse(doc)
    a.out.mkdir(parents=True, exist_ok=True)
    for pno in parse_pages(a.pages, doc.page_count):
        page = doc[pno - 1]
        path = a.out / f"page-{pno:03d}.png"
        page.get_pixmap(dpi=a.dpi).save(path)
        grids = layout.grids.get(pno - 1, [])
        skip = layout.running.get(pno - 1, []) + [g.bbox for g in grids]
        words = [w[4] for w in page.get_text("words", sort=True) if not L.in_any(pymupdf.Rect(w[:4]), skip)]
        head, tail = " ".join(words[:8]), " ".join(words[-8:])
        n_tab = sum(not g.is_box for g in grids)
        n_box = sum(g.is_box for g in grids)
        extras = [f"{n_tab} tables", f"{n_box} boxes"]
        if layout.code.get(pno - 1):
            extras.append(f"{len(layout.code[pno - 1])} code blocks")
        if (n_img := len([i for i in page.get_image_info() if i["bbox"][2] - i["bbox"][0] >= 20])):
            extras.append(f"{n_img} images")
        if (n_lnk := len(L.page_links(page))):
            extras.append(f"{n_lnk} links")
        print(f"{path}  [{', '.join(extras)}]\n    starts: {head!r}\n    ends:   {tail!r}")

if __name__ == "__main__":
    main()
