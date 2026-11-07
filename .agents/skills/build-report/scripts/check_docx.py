"""Post-check a built Word document against its markdown sources and the delivery rules.

Usage: python .claude/skills/build-report/scripts/check_docx.py --task TASK --lang CODE [--docx PATH]
       (the document defaults to <build>/<out> of the task's language in tasks.toml)

ERROR  content parity with the sources: numbered headings (number and text, in order), figure and table caption
       counts, image count, table count; every table caption directly above its table, every figure caption
       directly below its image, every caption registered with a SEQ field for the lists of figures and tables.
ERROR  layout: an image or a table wider (or an image taller) than the text area of its page; a table without a
       repeating header row; an empty heading.
ERROR  front matter and numbering: the contents, figure and table list fields; updateFields on open; a PAGE field
       in the footers; the title page without header; the first body page numbered 1 (arabic) after roman front
       matter; the short title and the author in every running header. A compact task ([TASK.layout] compact =
       true) has no contents, lists or roman pages, and those three checks are skipped for it.
ERROR  delivery: markdown or pandoc leftovers in the text (**, ![, ](, {width, $$, [^, | :--, ```); an em dash;
       an ordered list numbered other than (1), (2); a citation [n] beyond the reference list; core properties
       (title, author, language) different from tasks.toml and the language pack.
WARN   for a target language, the pack's conventions applied to the Word text (decimal style, glossary,
       untranslated lines), which catches anything the build introduced;
       placeholders still to fill ([Course name], [Group], TODO, …; the reference list is skipped, since APA keeps
       bracketed descriptions such as [Computer software]); three or more empty paragraphs in a row.
Exit code 1 when any ERROR is found. Word computes page numbers only when it opens the file, so page-level layout
(widows, blank pages) is not checked here; the build's keep-with-next and landscape rules cover it.
"""

import argparse
import re
import sys
import zipfile

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from lxml import etree

from common import ROOT, language_packs, load_config, load_report, resolve, source_language, tasks, shown
import glossary
from lang_rules import Rules
from table_layout import LONG_WORD_PT, count_lines, text_pt, unbroken, word_widths

EMU_PER_TWIP = 635
MAX_CELL_LINES = 20            # a table cell taller than this means its column is squeezed
TOLERANCE = 1.01
LEFTOVERS = ["**", "![", "](", "{width", "$$", "[^", "| :--", "|---", "```", "<!--"]
PLACEHOLDER = re.compile(r"\[(?!\d)[^\]\[]{2,40}\]|\bTODO\b|\bTBD\b|\bXXX\b|\?\?\?")
CITATION = re.compile(r"\[(\d+(?:\s*[,;–-]\s*\d+)*)\]")


def text_of(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def style_of(el):
    ps = el.find(qn("w:pPr") + "/" + qn("w:pStyle"))
    return ps.get(qn("w:val")) if ps is not None else ""


def norm(s):
    s = re.sub(r"[*_`]", "", s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s.replace("—", "–")).strip()


def sections_of(body):
    """(elements, sectPr) per Word section, in order."""
    out, cur = [], []
    for el in body:
        if el.tag == qn("w:sectPr"):
            out.append((cur, el))
            continue
        cur.append(el)
        sp = el.find(qn("w:pPr") + "/" + qn("w:sectPr")) if el.tag == qn("w:p") else None
        if sp is not None:
            out.append((cur, sp))
            cur = []
    return out


def text_area(sect):
    size, mar = sect.find(qn("w:pgSz")), sect.find(qn("w:pgMar"))
    w = int(size.get(qn("w:w"))) - int(mar.get(qn("w:left"))) - int(mar.get(qn("w:right")))
    h = int(size.get(qn("w:h"))) - int(mar.get(qn("w:top"))) - int(mar.get(qn("w:bottom")))
    return w * EMU_PER_TWIP, h * EMU_PER_TWIP


def instr_texts(el):
    return " ".join(i.text or "" for i in el.iter(qn("w:instrText")))


def title_page_height(doc):
    """Estimated height in points of everything before the first heading (the title page), with the line model of
    estimate_pages.py: lines at their font size, spacing before and after, images at their printed height, table rows
    at their column widths. Capitals and table cells are counted wide, so the estimate errs on the tall side."""
    from estimate_pages import line_count
    from docx.text.paragraph import Paragraph
    h = 0.0
    width = doc.sections[0].page_width - doc.sections[0].left_margin - doc.sections[0].right_margin
    width_pt = width / 12700.0
    for el in doc.element.body:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            if p.style.name.startswith("Heading") or p.style.name == "Front Heading":
                break
            pf = p.paragraph_format
            h += (pf.space_before.pt if pf.space_before is not None else 0)
            h += (pf.space_after.pt if pf.space_after is not None else 0)
            h += max((int(e.get("cy")) for e in el.iter(qn("wp:extent"))), default=0) / 12700.0
            size = next((r.font.size.pt for r in p.runs if r.font.size), 12.0)
            wide = 0.6 if p.text.isupper() else 0.5
            h += line_count(p.text, size, width_pt, wide) * size * 1.3
        elif el.tag == qn("w:tbl"):
            grid = [int(g.get(qn("w:w"))) / 20.0 for g in el.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
            for row in Table(el, doc).rows:
                tallest = 0.0
                for cell, w in zip(row.cells, grid):
                    size = next((r.font.size.pt for cp in cell.paragraphs for r in cp.runs if r.font.size), 12.0)
                    n = sum(line_count(cp.text, size, max(w - 12, 20), 0.5) for cp in cell.paragraphs)
                    tallest = max(tallest, n * size * 1.3 + 4)
                h += tallest
    return h


def table_fit(t):
    """Findings for a table whose columns do not suit their text: a word broken across lines, or a squeezed cell."""
    grid = [int(g.get(qn("w:w"))) / 20.0 for g in t._tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol"))]
    label, found = t.rows[0].cells[0].text[:30], []
    for i, row in enumerate(t.rows):
        for j, (cell, w) in enumerate(zip(row.cells, grid)):
            inner, size = w - 8.0, next((r.font.size.pt for p in cell.paragraphs for r in p.runs if r.font.size), 9.5)
            mono = frozenset(x for p in cell.paragraphs for r in p.runs
                             if r.style is not None and r.style.name == "Verbatim Char" for x in r.text.split())
            for word in (part for w in cell.text.split() for part in unbroken(w)):
                if inner < text_pt(word, size, i == 0, any(word in m for m in mono)) <= LONG_WORD_PT:
                    found.append(f"table '{label}': column {j + 1} ({w:.0f} pt) breaks the word '{word}'")
            n = count_lines(word_widths(cell.text, size, i == 0, mono), inner, size)
            if n > MAX_CELL_LINES:
                found.append(f"table '{label}': row {i + 1}, column {j + 1} ({w:.0f} pt) wraps to {n} lines")
    return found


def check(doc_path, rep, task, cfg, pack, n_refs, rules=None):
    errors, warns = [], []
    doc = Document(str(doc_path))
    body = doc.element.body
    paras = list(body.iter(qn("w:p")))
    code_styles = {"SourceCode"}

    # ---- content parity: numbered headings of the main parts (appendix subheadings restart at 1 and are skipped)
    def main_part(seq):
        """Numbered (level, number, text) items up to the first unnumbered H1 that follows the numbered parts."""
        out, started = [], False
        for level, text in seq:
            num = re.match(r"^(\d+(?:\.\d+)*)\.\s", text)
            if level == 1 and not num and started:
                break
            started |= level == 1 and bool(num)
            if started and num and level <= 3:
                out.append((level, num.group(1), norm(text)))
        return out

    md_heads = main_part([(h.level, h.text) for h in rep.headings])
    dx_seq = []
    for p in paras:
        st = style_of(p)
        if st in ("Heading1", "Heading2", "Heading3"):
            if not text_of(p).strip():
                errors.append("empty heading paragraph")
            dx_seq.append((int(st[-1]), text_of(p)))
    dx_heads = main_part(dx_seq)
    if [(lv, n) for lv, n, _ in dx_heads] != [(lv, n) for lv, n, _ in md_heads]:
        diff = next(((a, b) for a, b in zip(md_heads, dx_heads) if a[:2] != b[:2]), None)
        errors.append(f"numbered headings differ from the sources: {len(dx_heads)} in Word, {len(md_heads)} in "
                      f"markdown; first difference {diff}")
    else:
        for (_, n, a), (_, _, b) in zip(md_heads, dx_heads):
            if a != b:
                errors.append(f"heading {n} text differs: markdown '{a[:50]}' vs Word '{b[:50]}'")

    md_figs = sum(c.kind == "figure" for c in rep.captions)
    md_tabs = sum(c.kind == "table" for c in rep.captions)
    figs = [p for p in paras if style_of(p) == "ImageCaption"]
    tabs = [p for p in paras if style_of(p) == "TableCaption"]
    if (len(figs), len(tabs)) != (md_figs, md_tabs):
        errors.append(f"captions: Word has {len(figs)} figure and {len(tabs)} table captions, "
                      f"markdown has {md_figs} and {md_tabs}")
    for p in figs:
        prev = p.getprevious()
        if prev is None or prev.find(".//" + qn("w:drawing")) is None:
            errors.append(f"figure caption not directly below its image: '{text_of(p)[:50]}'")
        if "SEQ Figure" not in instr_texts(p):
            errors.append(f"figure caption without SEQ field (missing from the list of figures): '{text_of(p)[:50]}'")
    for p in tabs:
        nxt = p.getnext()
        if nxt is None or nxt.tag != qn("w:tbl"):
            errors.append(f"table caption not directly above its table: '{text_of(p)[:50]}'")
        if "SEQ Table" not in instr_texts(p):
            errors.append(f"table caption without SEQ field (missing from the list of tables): '{text_of(p)[:50]}'")

    md_images = sum(len(re.findall(r"^!\[", p.read_text(encoding="utf-8"), re.M)) for p in rep.files)
    md_tables = sum(len(re.findall(r"^\|[^\n]*\n\|\s*:?-{3,}", p.read_text(encoding="utf-8"), re.M)) for p in rep.files)
    n_images = len(doc.inline_shapes)
    n_tables = len(list(body.iter(qn("w:tbl"))))
    if n_images != md_images:
        errors.append(f"images: Word has {n_images}, markdown has {md_images}")
    if n_tables != md_tables:
        errors.append(f"tables: Word has {n_tables}, markdown has {md_tables}")

    # ---- layout: images and tables fit their section's text area
    secs = sections_of(body)
    for i, (els, sect) in enumerate(secs):
        w, h = text_area(sect)
        for el in els:
            for ext in el.iter(qn("wp:extent")):
                cx, cy = int(ext.get("cx")), int(ext.get("cy"))
                if cx > w * TOLERANCE or cy > h * TOLERANCE:
                    errors.append(f"image in Word section {i + 1} is {cx / 360000:.1f} × {cy / 360000:.1f} cm, "
                                  f"text area {w / 360000:.1f} × {h / 360000:.1f} cm")
            tbls = [el] if el.tag == qn("w:tbl") else []
            for t in tbls:
                tw = t.find(qn("w:tblPr") + "/" + qn("w:tblW"))
                if tw is not None and tw.get(qn("w:type")) == "dxa" and int(tw.get(qn("w:w"))) * EMU_PER_TWIP > w * TOLERANCE:
                    errors.append(f"table '{text_of(t)[:40]}' in Word section {i + 1} is wider than its text area")
                first_row = t.find(qn("w:tr"))
                title_table = i == 0
                if not title_table and (first_row is None or first_row.find(qn("w:trPr") + "/" + qn("w:tblHeader")) is None):
                    errors.append(f"table '{text_of(t)[:40]}' has no repeating header row")
                if not title_table:
                    errors.extend(table_fit(Table(t, doc)))

    # ---- front matter, fields and numbering
    instrs = instr_texts(body)
    compact = task.get("layout", {}).get("compact", False)    # a short document without contents, lists or roman pages
    captions = {name: sum(1 for p in body.iter(qn("w:p")) if style_of(p) == style)
                for name, style in (("Figure", "ImageCaption"), ("Table", "TableCaption"))}
    for need, what in () if compact else (('TOC \\o "1-3"', "table of contents"),):
        if need not in instrs:
            errors.append(f"{what} field ({need}) is missing")
    for name, count in captions.items():
        need, what = f'TOC \\h \\z \\c "{name}"', f"list of {name.lower()}s"
        if not compact and count and need not in instrs:
            errors.append(f"{what} field ({need}) is missing")
        if not count and need in instrs:
            errors.append(f"{what} is in the document but the report has no {name.lower()} captions: an empty page")
    upd = doc.settings.element.find(qn("w:updateFields"))
    if upd is None or upd.get(qn("w:val")) not in ("true", "1"):
        errors.append("settings: updateFields is not set, so Word will not fill in the contents on opening")
    else:
        # Schema order (CT_Settings): Word tolerates a misplaced element, Google Docs, Pages and LibreOffice do not
        names = [c.tag.split("}")[1] for c in doc.settings.element if isinstance(c.tag, str)]
        early = {"zoom", "embedSystemFonts", "proofState", "stylePaneFormatFilter", "doNotTrackMoves",
                 "defaultTabStop", "characterSpacingControl", "savePreviewPicture"}
        if any(n in early for n in names[names.index("updateFields") + 1:]):
            errors.append("settings: updateFields is out of schema order, so strict readers (Google Docs, Pages, "
                          "LibreOffice) reject the file")
    if any(m.get(qn("w:gutter")) is None for m in doc.element.body.iter(qn("w:pgMar"))):
        errors.append("a section's page margins lack the required w:gutter attribute, so strict readers reject the file")
    sections = doc.sections
    s0 = sections[0]
    text_h = (s0.page_height - s0.top_margin - s0.bottom_margin) / 12700.0
    title_h = title_page_height(doc)
    if title_h > text_h:
        errors.append(f"the title page is estimated at {title_h:.0f} pt, more than its {text_h:.0f} pt text area, so "
                      "it runs onto a second page: shorten the title or the names table, or reduce the fixed spacing")
    if sections[0].header.paragraphs and "".join(p.text for p in sections[0].header.paragraphs).strip():
        errors.append("the title page has a running header")
    numfmts = [(s._sectPr.find(qn("w:pgNumType"))) for s in sections]
    starts = [(i, n.get(qn("w:fmt")), n.get(qn("w:start"))) for i, n in enumerate(numfmts) if n is not None]
    if not any(f == "decimal" and s == "1" for _, f, s in starts):
        errors.append("no section restarts arabic page numbering at 1 (the first body page)")
    if not compact and not any(f == "lowerRoman" for _, f, _ in starts):
        errors.append("front matter is not numbered with roman numerals")
    for i, s in enumerate(sections[1:], start=2):
        if s.header.is_linked_to_previous:
            continue
        head = " ".join(p.text for p in s.header.paragraphs)
        for need in (cfg["short_title"], cfg.get("author", task.get("author", ""))):
            if need and need not in head:
                errors.append(f"running header of Word section {i} lacks '{need}'")
        if "PAGE" not in " ".join(instr_texts(p._p) for p in s.footer.paragraphs):
            errors.append(f"footer of Word section {i} has no PAGE field")

    # ---- delivery: leftovers, house style, citations, metadata, placeholders
    empties, in_refs = 0, False
    for p in paras:
        txt = text_of(p)
        st = style_of(p)
        if st == "Heading1":
            in_refs = txt.strip() in pack["references"]      # APA keeps bracketed descriptions such as [Software]
        if st not in code_styles:
            for bad in LEFTOVERS:
                if bad in txt:
                    errors.append(f"markdown leftover '{bad}' in: '{txt[:60]}'")
        if "—" in txt:
            errors.append(f"em dash in: '{txt[:60]}'")
        for m in CITATION.finditer(txt):
            for part in re.split(r"\s*[,;]\s*", m.group(1)):
                nums = [int(x) for x in re.split(r"\s*[–-]\s*", part)]
                if n_refs and any(k > n_refs for k in nums) and 0 not in nums:
                    errors.append(f"citation [{m.group(1)}] beyond the {n_refs} references: '{txt[:50]}'")
        if rules and not in_refs and st not in code_styles and txt.strip():
            lang_err, lang_warn = rules.check(txt, heading=st.startswith("Heading"))
            warns += [f"{pack['code']} convention: {x}" for x in lang_err + lang_warn]
        for m in PLACEHOLDER.finditer("" if in_refs or st in code_styles else txt):   # code keeps its brackets
            if CITATION.fullmatch(m.group(0)) is None:
                warns.append(f"placeholder to fill: '{m.group(0)}'")
        has_content = txt.strip() or p.find(".//" + qn("w:drawing")) is not None \
            or p.find(qn("w:pPr") + "/" + qn("w:sectPr")) is not None or p.find(".//" + qn("w:br")) is not None \
            or p.find(".//" + qn("m:oMath")) is not None                 # a display formula is content
        empties = 0 if has_content else empties + 1
        if empties == 3:
            warns.append(f"three or more empty paragraphs in a row before: '{text_of(p.getnext())[:40] if p.getnext() is not None else ''}'")

    with zipfile.ZipFile(doc_path) as z:
        if "word/numbering.xml" in z.namelist():
            numbering = etree.fromstring(z.read("word/numbering.xml"))
            used = {n.get(qn("w:val")) for n in body.iter(qn("w:numId"))}
            abstract_of = {n.get(qn("w:numId")): n.find(qn("w:abstractNumId")).get(qn("w:val"))
                           for n in numbering.iter(qn("w:num"))}
            used_abs = {abstract_of.get(u) for u in used}
            for a in numbering.iter(qn("w:abstractNum")):
                if a.get(qn("w:abstractNumId")) not in used_abs:
                    continue
                lvl = a.find(qn("w:lvl"))
                fmt = lvl.find(qn("w:numFmt")) if lvl is not None else None
                txt = lvl.find(qn("w:lvlText")) if lvl is not None else None
                if fmt is not None and fmt.get(qn("w:val")) == "decimal" and txt is not None \
                        and not txt.get(qn("w:val"), "").startswith("("):
                    errors.append(f"ordered list numbered '{txt.get(qn('w:val'))}' instead of '(%1)'")

    cp = doc.core_properties
    want = {"title": cfg["title"], "author": cfg.get("author", task.get("author", "")), "language": pack["locale"]}
    for k, v in want.items():
        if (getattr(cp, k) or "") != v:
            errors.append(f"core property {k} is '{getattr(cp, k)}', expected '{v}'")
    unique_warns = list(dict.fromkeys(warns))
    return errors, unique_warns, dict(headings=len(dx_heads), figures=len(figs), tables=len(tabs), images=n_images,
                                      sections=len(sections))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", required=True)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--docx", help="document to check (default: from tasks.toml)")
    args = ap.parse_args()
    config = load_config()
    name = resolve(args.task, config)[0]
    task = tasks(config)[name]
    packs = language_packs()
    pack, cfg = packs[args.lang], task[args.lang]
    doc_path = ROOT / (args.docx or f"{task['build']}/{cfg['out']}")
    if not doc_path.exists():
        print(f"ERROR {shown(doc_path)} does not exist (build it first)")
        return 1
    rep = load_report(ROOT / task["report"], pack, packs)
    n_refs = 0
    if rep.references_file:
        n_refs = len(re.findall(r"^\[\d+\]\s", rep.references_file.read_text(encoding="utf-8"), re.M))
    rules = Rules(pack, packs[source_language(packs)], glossary.for_task(pack, task)) if "translation" in pack else None
    errors, warns, stats = check(doc_path, rep, task, cfg, pack, n_refs, rules)
    print(f"===== {args.lang.upper()} {shown(doc_path)}: {stats['headings']} numbered headings, "
          f"{stats['figures']} figures, {stats['tables']} tables, {stats['images']} images, {stats['sections']} Word "
          f"sections: {len(errors)} errors, {len(warns)} warnings")
    for e in errors:
        print("  ERROR " + e)
    for w in warns:
        print("  WARN  " + w)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
