"""Page budget of a built report: how long its main content is, where the pages go, and what a move would buy.

Usage: python .claude/skills/build-report/scripts/page_budget.py DOCX [--budget PAGES] [--blocks] [--optimistic]
       python .claude/skills/build-report/scripts/page_budget.py --task TASK [--budget PAGES]   (every built language;
       make pages TASK=taskN BUDGET=10)

The main content runs from the first numbered level-1 heading ("1. …") to the reference list ("References" or "Tài
liệu tham khảo"), as briefs count it (front matter and appendices excluded). For each part it prints:

- optimistic: the continuous-flow estimate of estimate_pages.py (heights summed as if text flowed without gaps);
- laid out: the pessimistic layout of paginate.py, page by page under the builder's rules (sections, unsplittable
  table rows with repeated headers, figures, keep-with-next, widows and orphans), with wider characters and word-wrap
  loss; a part's length includes the space it leaves empty before a page break;
- flow: the same pessimistic measures without page breaks, so laid out minus flow is the space lost to layout;
- tables: the share of the flow that is tables.

The totals say how far the main content sits from --budget and how much of that distance moving text, moving tables
or closing layout gaps could cover; the last line gives how full the last main-text page is, so a planned cut can be
checked against the page it would actually save. Plan with the pessimistic figure; the real length lies between the
two columns.

--blocks lists every heading of levels 1–3 and every table of the main content with its pessimistic length (with
--optimistic, the continuous-flow lengths), for weighing which block a move would take.

Before proposing a move, map each candidate block to the brief's required report structure and task tables: only
detail beyond what the brief requires, or content stated twice, is a candidate; size alone never is.
"""

import argparse
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import paginate  # noqa: E402
from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.table import Table  # noqa: E402
from docx.text.paragraph import Paragraph  # noqa: E402
from estimate_pages import TEXT_H_PT, TEXT_W_PT, font_size, line_count  # noqa: E402

REFERENCES = ("References", "Tài liệu")


def is_part(name):
    return name[:2].rstrip(".").isdigit()


def optimistic_parts(path, char_width=0.45, blocks=False):
    """[(label, pages)] with the continuous-flow line model of estimate_pages.py."""
    doc = Document(path)
    body_size = font_size(next((p for p in doc.paragraphs if p.style.name == "Body Text"), doc.paragraphs[0]), 12)
    spacing = doc.styles["Body Text"].paragraph_format.line_spacing or 1.3
    out, name, h = [], None, 0.0
    for el in doc.element.body:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            style = p.style.name
            split = style.startswith("Heading 1") or style == "Front Heading"
            if blocks and style[:9] in ("Heading 2", "Heading 3"):
                split = True
            if blocks and paginate.CAPTION.match(p.text.strip()) and name is not None:
                out.append((name, h / TEXT_H_PT))
                name, h = "  [table] " + p.text.strip()[:37], 0.0
                continue
            if split:
                if name is not None:
                    out.append((name, h / TEXT_H_PT))
                name, h = p.text.strip()[:45], 0.0
            if name is None:
                continue
            extents = el.findall(".//" + qn("wp:extent"))
            if extents:
                h += max(int(e.get("cy")) for e in extents) / 12700.0 + 12
            size = font_size(p, body_size)
            n = line_count(p.text, size, TEXT_W_PT, char_width)
            if n:
                after = p.paragraph_format.space_after.pt if p.paragraph_format.space_after is not None else 6
                h += n * size * (1.1 if style.startswith("Heading") else spacing) * 1.15 + after
                h += 16 if style.startswith("Heading") else 0
        elif el.tag == qn("w:tbl") and name is not None:
            grid = [int(g.get(qn("w:w"))) / 20.0 for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
            for row in Table(el, doc).rows:
                tallest = 0.0
                for cell, w in zip(row.cells, grid):
                    size = next((r.font.size.pt for cp in cell.paragraphs for r in cp.runs if r.font.size), 9.5)
                    n = sum(line_count(cp.text, size, max(w - 10, 20), char_width) for cp in cell.paragraphs)
                    tallest = max(tallest, n * size * 1.05 * 1.15 + 4)
                h += tallest
            h += 12
            if blocks:
                out.append((name, h / TEXT_H_PT))
                name, h = name.replace("  [table] ", "  (text after) "), 0.0
    out.append((name, h / TEXT_H_PT))
    return out


def flow_heights(path, m):
    """Pessimistic heights per level-1 part without page breaks, split into text and tables (in pages)."""
    blocks, geo = paginate.blocks_of(Document(path), m)
    page_h = geo[0][1]
    out, name = {}, None
    for b in blocks:
        if b["kind"] == "p" and (b["style"].startswith("Heading 1") or b["style"] in ("Front Heading", "Title")):
            name = b["text"][:45]
            out[name] = {"text": 0.0, "tables": 0.0}
        if name is None:
            continue
        if b["kind"] == "p":
            out[name]["text"] += (b["before"] + b["n"] * b["line_h"] + b["after"]
                                  + (b["image"] + 6 if b["image"] else 0)) / page_h
        else:
            out[name]["tables"] += (sum(b["rows"]) + b["after"]) / page_h
    return out


def last_page_fill(path, m):
    """How full the last page of the main content is, just before the reference list starts a new page."""
    fills = []
    orig = paginate.Layout.new_page

    def logged(self):
        fills.append((self.page, self.y / self.h if self.h else 0.0))
        orig(self)
    paginate.Layout.new_page = logged
    try:
        parts, _ = paginate.paginate(path, m)
    finally:
        paginate.Layout.new_page = orig
    ref = next((s for n, s, e in parts if n.startswith(REFERENCES)), None)
    if ref is None:
        return None
    before = [f for p, f in fills if p == int(ref) - 1]
    return before[-1] if before else None


def blocks_report(path, optimistic):
    if optimistic:
        rows = optimistic_parts(path, blocks=True)
        start = next(i for i, (n, _) in enumerate(rows) if is_part(n))
        end = next(i for i, (n, _) in enumerate(rows) if n.startswith(REFERENCES))
        for n, p in rows[start:end]:
            if p >= 0.01:
                print(f"{n:50} {p:5.2f}")
        print(f"main content: {sum(p for _, p in rows[start:end]):.1f} pages (optimistic, continuous flow)")
        return
    rows, _ = paginate.paginate(path, paginate.PESSIMISTIC, split_blocks=True)
    start = next(i for i, (n, s, e) in enumerate(rows) if is_part(n))
    end = next(i for i, (n, s, e) in enumerate(rows) if n.startswith(REFERENCES))
    for n, s, e in rows[start:end]:
        if e - s >= 0.01:
            print(f"{n:50} {e - s:5.2f}")
    print(f"main content: {rows[end][1] - rows[start][1]:.1f} pages (pessimistic layout; --optimistic for the "
          f"continuous flow)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", nargs="?")
    ap.add_argument("--task", help="a task of tasks.toml: measure every built document in its build folder")
    ap.add_argument("--budget", type=float, default=None, help="page budget of the main content (from the brief)")
    ap.add_argument("--blocks", action="store_true", help="list every heading and table of the main content")
    ap.add_argument("--optimistic", action="store_true", help="with --blocks: continuous-flow lengths")
    a = ap.parse_args()
    if a.task:
        from common import ROOT, load_config, tasks
        found = tasks(load_config())
        names = list(found) if a.task == "all" else [a.task]
        for name in names:
            build = ROOT / found[name]["build"]
            for docx in sorted(build.glob("*.docx")):
                print(f"===== {name}: {docx.name}")
                sys.argv = [sys.argv[0], str(docx)] + (["--budget", str(a.budget)] if a.budget is not None else [])
                main()
        return 0
    if not a.docx:
        ap.error("give a DOCX or --task")
    if a.blocks:
        blocks_report(a.docx, a.optimistic)
        return 0
    opt = dict(optimistic_parts(a.docx))
    laid, _ = paginate.paginate(a.docx, paginate.PESSIMISTIC)
    flow = flow_heights(a.docx, paginate.PESSIMISTIC)
    print(f"{'part':45} {'optimistic':>10} {'laid out':>8} {'flow':>6} {'gap':>5} {'tables':>6}")
    tot = dict(opt=0.0, laid=0.0, flow=0.0, tables=0.0)
    for n, s, e in laid:
        o = opt.get(n, float("nan"))
        f = flow.get(n, {"text": 0.0, "tables": 0.0})
        fl = f["text"] + f["tables"]
        mark = is_part(n)
        print(f"{n:45} {o:10.1f} {e - s:8.2f} {fl:6.2f} {e - s - fl:5.2f} {f['tables']:6.2f}" if mark
              else f"{n:45} {o:10.1f} {e - s:8.2f}")
        if mark:
            tot["opt"] += o
            tot["laid"] += e - s
            tot["flow"] += fl
            tot["tables"] += f["tables"]
    print(f"{'main content':45} {tot['opt']:10.1f} {tot['laid']:8.2f} {tot['flow']:6.2f} "
          f"{tot['laid'] - tot['flow']:5.2f} {tot['tables']:6.2f}")
    print(f"main content: optimistic {tot['opt']:.1f} pages, pessimistic {tot['laid']:.1f} pages (plan with this); "
          f"text {tot['flow'] - tot['tables']:.1f}, tables {tot['tables']:.1f}, layout gaps "
          f"{tot['laid'] - tot['flow']:.1f}")
    fill = last_page_fill(a.docx, paginate.PESSIMISTIC)
    if fill is not None:
        print(f"last main-text page {fill:.0%} full: a cut saves a page only if it removes more than "
              f"{fill:.2f} of a page")
    if a.budget is not None:
        print(f"budget {a.budget:g} pages: {tot['laid'] - a.budget:+.1f} pages (pessimistic), "
              f"{tot['opt'] - a.budget:+.1f} (optimistic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
