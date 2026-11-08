# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "pymupdf>=1.26",
#   # pymupdf4llm 2.0 on PyPI is an empty placeholder wheel; stay on 1.x.
#   "pymupdf4llm>=1.27,<2",
# ]
# ///
"""Convert a text-based PDF to Markdown, preserving content as-is.

Pipeline (all deterministic):
  1. Analyse layout (pdf_layout.py): running headers/footers, ruled tables,
     single-cell callout boxes, page-break table continuations, monospace
     code blocks, paragraph starts, heading sizes.
  2. In an in-memory copy of the PDF, redact running lines and replace every
     table/box, code block and image with a placeholder token.
  3. Run pymupdf4llm (classic rule-based path) for the text flow.
  4. Swap tokens for Markdown tables / blockquotes / fenced code / image links.
  5. Normalise: join wrapped lines using the PDF's paragraph starts, tidy
     lists and headings, fix link labels, restore real hyphens; keep constant
     running header/footer lines once.

Usage:
  uv run convert.py input.pdf [-o output.md] [--assets-dir DIR]
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import pymupdf
import pymupdf4llm

import pdf_layout as L

# The GNN "layout" path ignores hdr_info; the classic path is fully rule-based.
pymupdf4llm.use_layout(False)

PH = "ZZ{}{:04d}ZZ"  # ZZGRID0007ZZ / ZZIMG0002ZZ / ZZCODE0001ZZ
PH_RE = re.compile(r"[ \t#*_>~`-]*(?:<mark>)?ZZ(GRID|IMG|CODE)(\d{4})ZZ(?:</mark>)?[*_~` \t]*")
MIN_IMAGE_PT = 20  # ignore decorative specks smaller than this


# ------------------------------------------------------------ block render


def md_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def render_table(rows: list[list[str]], n_cols: int) -> str:
    rows = [r + [""] * (n_cols - len(r)) for r in rows] or [[""] * n_cols]
    out = ["| " + " | ".join(md_cell(c) for c in rows[0]) + " |", "|" + "---|" * n_cols]
    out += ["| " + " | ".join(md_cell(c) for c in r) + " |" for r in rows[1:]]
    return "\n".join(out)


def render_box(paragraphs: list[str]) -> str:
    lines = ["> " + re.sub(r"^[•▪◦‣●]\s*", "- ", p) for p in paragraphs]
    return "\n>\n".join(lines) if lines else ">"


def build_blocks(layout: L.DocLayout) -> dict[tuple[str, int], str]:
    """Placeholder key -> markdown block. Table continuations map to ''."""
    blocks: dict[tuple[str, int], str] = {}
    tables = iter(L.merged_tables(layout))
    gid = cid = 0
    for pno in sorted(layout.grids):
        for gi, g in enumerate(layout.grids[pno]):
            if g.is_box:
                blocks[("GRID", gid)] = render_box(g.rows[0][0].paragraphs)
            elif (pno, gi) in layout.continues:
                blocks[("GRID", gid)] = ""
            else:
                t = next(tables)
                blocks[("GRID", gid)] = render_table(t["rows"], t["n_cols"])
            g.placeholder = gid  # type: ignore[attr-defined]
            gid += 1
        for c in layout.code.get(pno, []):
            blocks[("CODE", cid)] = "```\n" + "\n".join(c.lines) + "\n```"
            c.placeholder = cid  # type: ignore[attr-defined]
            cid += 1
    return blocks


def extract_images(doc: pymupdf.Document, layout: L.DocLayout, assets: Path, link_dir: str, stem: str) -> dict:
    """Save every placed raster image; return {page: [(rect, id, markdown)]}.

    The embedded bytes are written unchanged when possible (as-is); images
    with a soft mask (transparency) are rendered from the page instead.
    Images inside a table/box are skipped here (verify.py reports them).
    """
    out: dict[int, list] = {}
    n = 0
    for pno, page in enumerate(doc):
        grids = [g.bbox for g in layout.grids.get(pno, [])]
        k = 0
        for info in page.get_image_info(xrefs=True):
            r = pymupdf.Rect(info["bbox"]) & page.rect
            if r.width < MIN_IMAGE_PT or r.height < MIN_IMAGE_PT or L.in_any(r, grids):
                continue
            k += 1
            xref = info.get("xref", 0)
            data = doc.extract_image(xref) if xref else None
            if data and not data.get("smask"):
                name, blob = f"{stem}-p{pno + 1}-{k}.{data['ext']}", data["image"]
            else:
                name, blob = f"{stem}-p{pno + 1}-{k}.png", page.get_pixmap(clip=r, dpi=200).tobytes("png")
            assets.mkdir(parents=True, exist_ok=True)
            (assets / name).write_bytes(blob)
            out.setdefault(pno, []).append((r, n, f"![]({link_dir}/{name})"))
            n += 1
    return out


def redacted_copy(doc: pymupdf.Document, layout: L.DocLayout, images: dict) -> pymupdf.Document:
    """Copy of the PDF with running lines removed and grids/code/images replaced by tokens.

    Grid borders/shading are removed too; otherwise pymupdf4llm reads them as
    strikethrough/highlight around the token or renders them as images.
    """
    red = pymupdf.open()
    red.insert_pdf(doc)
    for pno, page in enumerate(red):

        def token(rect, kind, i):
            size = max(2.0, min(8.0, rect.width / 8))
            page.add_redact_annot(rect, text=PH.format(kind, i), fontsize=size, align=0, fill=False)

        for r in layout.running.get(pno, []):
            page.add_redact_annot(r + (-1, -1, 1, 1))
        for g in layout.grids.get(pno, []):
            token(g.bbox + (-1, -1, 1, 1), "GRID", g.placeholder)
        for c in layout.code.get(pno, []):
            token(c.rect + (-1, -1, 1, 1), "CODE", c.placeholder)
        for r, i, _ in images.get(pno, []):
            token(r, "IMG", i)
        page.apply_redactions(
            images=pymupdf.PDF_REDACT_IMAGE_REMOVE, graphics=pymupdf.PDF_REDACT_LINE_ART_REMOVE_IF_COVERED
        )
    return red


def rule_anchors(doc: pymupdf.Document, layout: L.DocLayout) -> list[str]:
    """For each horizontal rule, the squeezed tail of the PDF text line just above it."""
    anchors = []
    for pno in sorted(layout.rules):
        lines = [
            ln for b in doc[pno].get_text("dict")["blocks"] for ln in b.get("lines", [])
            if not L.in_any(pymupdf.Rect(ln["bbox"]), layout.running.get(pno, []))
        ]
        for r in layout.rules[pno]:
            above = [ln for ln in lines if ln["bbox"][3] <= r.y0 + 1 and L.squeeze("".join(s["text"] for s in ln["spans"]))]
            if above:
                ln = max(above, key=lambda l: l["bbox"][3])
                anchors.append(L.squeeze("".join(s["text"] for s in ln["spans"]))[-30:])
            else:
                anchors.append("")
    return anchors


def insert_rules(md: str, anchors: list[str]) -> str:
    """Insert "---" after the Markdown line holding each anchor (in document order).

    Placement is done here rather than through pymupdf4llm, whose reading
    order for a bare line is unreliable.
    """
    lines = md.split("\n")
    start = 0
    for anchor in anchors:
        if not anchor:
            lines.insert(0, "---")
            continue
        buf, owner = "", []
        for i in range(start, len(lines)):
            sq = L.squeeze(lines[i])
            buf += sq
            owner += [i] * len(sq)
        k = buf.find(anchor)
        if k < 0:
            continue  # verify.py reports the missing rule
        i = owner[k + len(anchor) - 1]
        lines[i + 1 : i + 1] = ["", "---", ""]
        start = i + 3
    return "\n".join(lines)


# ------------------------------------------------------------ text repairs


def restore_hyphens(md: str, pairs: list[tuple[str, str]]) -> str:
    """pymupdf4llm drops the hyphen when joining "event-" + newline + "level".

    In PDFs that mark soft wraps with a trailing space, such a hyphen is part
    of the text (a compound word), so put it back - once per recorded break.
    """
    for a, b in pairs:
        md = re.sub(rf"(?<![\w-]){re.escape(a)}{re.escape(b)}(?![\w])", f"{a}-{b}", md, count=1)
    return md


def fix_link_labels(md: str, links: list[tuple[pymupdf.Rect, str, str]]) -> str:
    """pymupdf4llm links a whole span; narrow the label to the PDF's linked text.

    "[UCI – Student Performance: https://x](https://x)" becomes
    "UCI – Student Performance: [https://x](https://x)" when only the URL is
    the link area in the PDF.
    """
    for _, uri, vis in links:
        if not vis:
            continue

        def narrow(m: re.Match) -> str:
            label = m.group(1)
            if label == vis or vis not in label:
                return m.group(0)
            return label.replace(vis, f"[{vis}]({uri})", 1)

        md = re.sub(r"\[([^\]]+)\]\(" + re.escape(uri) + r"\)", narrow, md)
    return md


# ------------------------------------------------------------ normalisation

LIST_RE = re.compile(r"^(\s*)([-*+]|\d{1,3}[.)])\s+(.*)$")
CHECKBOX_RE = re.compile(r"^\s*(?:[-*+]\s+)?([☐☑☒□▢])\s*")
CHECKBOX_MD = {"☐": "[ ]", "□": "[ ]", "▢": "[ ]", "☑": "[x]", "☒": "[x]"}  # GitHub task-list items
STRUCT_RE = re.compile(r"^\s*(#{1,6} |>|\||!\[|```)")
SPLIT_HEADING_END = ("→", "-", "–", "—", ",", ":", "&", "/", "và", "and", "of", "the")


def plain_heading(line: str) -> str:
    m = re.match(r"^(#{1,6}) (.+)$", line)
    if not m:
        return line
    text = re.sub(r"\*\*|__", "", m.group(2))
    text = re.sub(r"^_(.+)_$", r"\1", text)
    return f"{m.group(1)} {re.sub(r' {2,}', ' ', text).strip()}"


def is_para_start(lines: list[str], i: int, starts: set[str]) -> bool:
    """Does lines[i] begin a paragraph in the PDF? (prefix match on squeezed text)"""
    buf = ""
    for line in lines[i:]:
        if not line.strip() or STRUCT_RE.match(line):
            break
        buf += L.squeeze(line)
        if len(buf) >= L.KEY_LEN:
            break
    if not buf:
        return True
    key = buf[: L.KEY_LEN]
    return key in starts or any(k.startswith(key) or key.startswith(k) for k in starts if len(k) < L.KEY_LEN)


def escape_lead(content: str) -> str:
    """Escape text that Markdown would read as a nested block marker.

    "- 1) Check docs" must stay a bullet whose text starts with "1)", not a
    bullet containing an ordered list; same for "- - x", "- # x", "- > x".
    """
    content = re.sub(r"^(\d{1,9})([.)])(?=\s)", r"\1\\\2", content)
    return re.sub(r"^([-+*#>])(?=\s)", r"\\\1", content)


def join(prev: str, line: str) -> str:
    if prev.rstrip().endswith("**") and line.lstrip().startswith("**") and prev.count("**") % 2 == 0:
        return re.sub(r"\*\*\s*$", "", prev) + " " + re.sub(r"^\s*\*\*", "", line)
    return prev.rstrip() + " " + line.strip()


def normalise(md: str, starts: set[str]) -> str:
    """Line-level cleanup of pymupdf4llm output. Fenced code is never touched."""
    src = [l.rstrip() for l in md.splitlines()]
    out: list[str] = []
    in_fence = False
    last_kind = None  # kind of the last non-blank emitted line: para/list/struct
    for i, line in enumerate(src):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            last_kind = "struct"
            continue
        if in_fence:
            out.append(line)
            continue
        if not line.strip():
            out.append("")
            continue
        line = plain_heading(line)
        line = CHECKBOX_RE.sub(lambda m: f"- {CHECKBOX_MD[m.group(1)]} ", line)
        h = re.match(r"^(#{1,6}) (.+)$", line)
        if h:
            # merge a heading pymupdf4llm split over two wrapped lines
            j = len(out) - 1
            while j >= 0 and out[j] == "":
                j -= 1
            pm = re.match(r"^(#{1,6}) (.+)$", out[j]) if j >= 0 else None
            if pm and pm.group(1) == h.group(1) and (pm.group(2).endswith(SPLIT_HEADING_END) or h.group(2)[:1].islower()):
                out[j] = f"{pm.group(1)} {pm.group(2)} {h.group(2)}"
                del out[j + 1 :]
                continue
            out += ["", line, ""]
            last_kind = "struct"
            continue
        if STRUCT_RE.match(line):
            out.append(line)
            last_kind = "struct"
            continue
        m = LIST_RE.match(line)
        if m:
            out.append(f"{m.group(1)}{m.group(2)} {escape_lead(m.group(3))}")
            last_kind = "list"
            continue
        # plain text: continuation of the previous paragraph/list item unless
        # the PDF starts a new paragraph here
        if last_kind in ("para", "list") and not is_para_start(src, i, starts):
            j = len(out) - 1
            while out[j] == "":
                j -= 1
            out[j] = join(out[j], line)
            del out[j + 1 :]
            continue
        if out and out[-1] != "":
            out.append("")
        out.append(line.strip())
        last_kind = "para"
    out = tidy_lists(out)
    md = "\n".join(out)
    md = re.sub(r"(\*\*|__)\s+([.,;:!?)\]])", r"\1\2", md)  # "**bold** ." -> "**bold**."
    md = re.sub(r"<u>(\[[^\]]*\]\([^)]*\))</u>", r"\1", md)  # underline = link styling
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def mark_checkboxes(md: str, keys: dict[str, str]) -> str:
    """Turn a list item into a task item when its PDF line started with a checkbox glyph that pymupdf4llm read as a
    bullet (□ ▢); fenced code is never touched."""
    out, in_fence = [], False
    for line in md.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else re.match(r"^(\s*)[-*+]\s+(?!\[[ xX]\]\s)(.+)$", line)
        if m and keys:
            mark = keys.get(L.squeeze(m.group(2))[:L.KEY_LEN])
            if mark:
                line = f"{m.group(1)}- {mark} {m.group(2)}"
        out.append(line)
    return "\n".join(out)


def tidy_lists(lines: list[str]) -> list[str]:
    """Consistent list markup: no stray indentation, tight items."""
    out: list[str] = []
    run: list[int] = []  # indices in out of the current list's items

    def flush():
        # pymupdf4llm's indentation is not reliable (it shifts across page
        # breaks), so lists are flattened; nesting is restored in review.
        for k in run:
            m = LIST_RE.match(out[k])
            out[k] = f"{m.group(2)} {m.group(3)}"
        run.clear()

    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and LIST_RE.match(line):
            if run and all(x == "" for x in out[run[-1] + 1 :]):
                del out[run[-1] + 1 :]  # blank lines between items -> tight list
            elif run:
                flush()
            out.append(line)
            run.append(len(out) - 1)
            continue
        if line.strip() and run:
            flush()
            if out[-1] != "":
                out.append("")
        out.append(line)
    if run:
        flush()
    return out


# ------------------------------------------------------------------ driver


def convert(pdf: Path, out: Path, assets: Path) -> dict:
    doc = pymupdf.open(pdf)
    out.parent.mkdir(parents=True, exist_ok=True)
    if not any(p.get_text().strip() for p in doc):
        sys.exit(f"{pdf}: no extractable text (scanned PDF?) - OCR it first; see SKILL.md")
    layout = L.analyse(doc)
    blocks = build_blocks(layout)
    headers = L.HeadingLevels(doc, layout)
    link_dir = Path(os.path.relpath(assets.resolve(), out.parent.resolve())).as_posix()
    images = extract_images(doc, layout, assets, link_dir, pdf.stem)
    blocks.update({("IMG", i): link for lst in images.values() for _, i, link in lst})
    red = redacted_copy(doc, layout, images)

    md = pymupdf4llm.to_markdown(
        red,
        hdr_info=headers,
        filename=pdf.stem,
        table_strategy=None,  # tables come from our grid detector
        ignore_graphics=True,  # table borders/shading are not figures
        ignore_images=True,  # images were extracted and tokenised above
        ignore_code=True,  # code blocks were extracted and tokenised above
        show_progress=False,
    )

    used: set = set()

    def sub(m: re.Match) -> str:
        key = (m.group(1), int(m.group(2)))
        used.add(key)
        block = blocks.get(key, "")
        return f"\n\n{block}\n\n" if block else "\n\n"

    md = PH_RE.sub(sub, md)
    missing = sorted(f"{k}{i}" for k, i in set(blocks) - used)
    md = restore_hyphens(md, layout.hyphen_breaks)
    md = fix_link_labels(md, [lk for page in doc for lk in L.page_links(page)])
    md = normalise(md, layout.para_starts)
    md = mark_checkboxes(md, layout.checkbox_starts)
    md = re.sub(r"\n{3,}", "\n\n", insert_rules(md, rule_anchors(doc, layout)))
    heads, foots = layout.running_kept
    if heads:
        md = "\n\n".join(heads) + "\n\n" + md
    if foots:
        md = md.rstrip("\n") + "\n\n" + "\n\n".join(foots) + "\n"
    out.write_text(md, encoding="utf-8")

    return {
        "pages": doc.page_count,
        "tables": len(L.merged_tables(layout)),
        "boxes": sum(g.is_box for gs in layout.grids.values() for g in gs),
        "code_blocks": sum(len(v) for v in layout.code.values()),
        "images": sum(len(v) for v in images.values()),
        "running_lines_removed": sum(len(v) for v in layout.running.values()),
        "running_lines_kept_once": heads + foots,
        "body_font_size": headers.body,
        "heading_sizes": {f"h{v}": k for k, v in headers.levels.items()},
        "missing_placeholders": missing,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="output .md (default: next to the PDF)")
    ap.add_argument("--assets-dir", type=Path, help="image folder (default: <stem>_assets next to output)")
    a = ap.parse_args()
    out = a.out or a.pdf.with_suffix(".md")
    assets = a.assets_dir or out.parent / f"{out.stem}_assets"
    stats = convert(a.pdf, out, assets)
    print(f"wrote {out}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    if stats["missing_placeholders"]:
        print("WARNING: some placeholders were not found in the text flow; "
              "their content is missing - check verify.py output", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
