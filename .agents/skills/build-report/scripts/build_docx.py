"""Build one Word document (.docx) from the markdown section files of a report folder.

Usage (normally called by report.py with the task's settings from tasks.toml):
    python .claude/skills/build-report/scripts/build_docx.py --src taskN/report --lang en \
        --out build/taskN/Report_EN.docx --title "..." --short-title "..." --author "..." [--subject "..."] [--portrait]
        [--compact]

--portrait keeps every page in portrait: wide tables take the portrait text width in a smaller font and wide
figures scale to it, so the document has only the title, front-matter and body sections. Use it for copies that
are edited in Google Docs, where copying content that spans an orientation change between documents has been
observed to stop the document from saving (tasks.toml: google_docs = true builds this copy next to the Word file).

--compact builds a short document such as a proposal (tasks.toml: [taskN.layout] compact = true): parts and front
pages follow one another without page breaks, there is no contents page and no list of figures or tables, and the
page after the title page is numbered 1 in arabic numerals. Every page stays portrait, as with --portrait, so no page
breaks surround rotated tables or figures. The title page, captions, tables and headers stay as usual.

Pipeline:
    1. Create a styled reference.docx (fonts, spacing, captions, tables, A4 page setup, document language).
    2. Pandoc converts the ordered markdown sections of the language into content (text, lists, tables, images,
       footnotes); the filter report_format.lua turns em dashes into en dashes and numbers ordered lists (1), (2) ….
    3. A python-docx pass adds what only Word's layout engine offers: title page, contents / figure / table
       lists as fields, roman and arabic page numbering, headers and footers, landscape pages for wide
       diagrams and wide tables, table styling with repeating header rows, captions kept with their object,
       document language and metadata.

Interface texts (contents headings, caption words) come from the language pack of --lang (languages/*.toml or a
report-language-<code>.toml contributed by another skill). Word refreshes the contents and lists on opening.
"""

from __future__ import annotations

import argparse
import copy
import re
import subprocess
import sys
from pathlib import Path

import pypandoc
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Emu, Inches, Pt, RGBColor
from docx.table import Table
from docx.text.paragraph import Paragraph

from common import ROOT, language_packs, section_files, shown

HERE = Path(__file__).resolve().parent
CACHE = ROOT / "build" / ".cache"

# ----------------------------------------------------------------------------- configuration
BODY_FONT = "Times New Roman"
MONO_FONT = "Courier New"
NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY = RGBColor(0x59, 0x5F, 0x69)

PAGE_W, PAGE_H = Cm(21.0), Cm(29.7)            # A4
MARGIN = dict(top=Cm(2.0), bottom=Cm(2.0), left=Cm(3.0), right=Cm(2.0))
TEXT_W_PORTRAIT = PAGE_W - MARGIN["left"] - MARGIN["right"]        # 16.0 cm
TEXT_W_LANDSCAPE = PAGE_H - MARGIN["left"] - MARGIN["right"]       # 24.7 cm
TEXT_H_LANDSCAPE = PAGE_W - MARGIN["top"] - MARGIN["bottom"]       # 17.0 cm

TEXT_H_PORTRAIT = PAGE_H - MARGIN["top"] - MARGIN["bottom"]       # 25.7 cm
LINE_SPACING = 1.3             # running text (body paragraphs, lists, quotes)
LANDSCAPE_GAIN = 1.08          # rotate a figure only when landscape prints it at least 8% larger
LANDSCAPE_TABLE_CHARS = 80     # text-heavy tables (mean characters per body cell) also go on a landscape page
SHORT_CELL = 24                # a column whose body cells are all this short keeps each cell on one line
FIT_SLACK = 0.15               # a table that fits takes its natural width plus up to 15% of air, centred
LANDSCAPE_PAGES = True         # False (--portrait): wide content stays on portrait pages, no orientation changes
COMPACT = False                # True (--compact): no page breaks before parts, no contents or lists, arabic from page 1

def labels_for(code: str, src: Path, meta: dict) -> dict:
    """Interface texts of the language pack plus the document metadata (title, short title, author, subject)."""
    packs = language_packs()
    if code not in packs:
        raise SystemExit(f"no language pack for '{code}'; known: {', '.join(packs)}")
    pack = packs[code]
    return dict(files=lambda: section_files(src, pack, packs), lang=pack["locale"], contents=pack["contents"],
                lof=pack["lof"], lot=pack["lot"], hint=pack["hint"], fig_prefix=tuple(pack["figure"][:1]),
                table_prefix=tuple(pack["table"][:1]), layout=pack.get("docx", {}), **meta)

# ----------------------------------------------------------------------------- small XML helpers
# Word validates the order of child elements; these lists follow the WordprocessingML schema.
ORDER = {
    "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl", "numPr",
            "suppressLineNumbers", "pBdr", "shd", "tabs", "suppressAutoHyphens", "kinsoku", "wordWrap",
            "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd", "snapToGrid",
            "spacing", "ind", "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection",
            "textAlignment", "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"],
    "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize", "tblStyleColBandSize", "tblW",
              "jc", "tblCellSpacing", "tblInd", "tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook",
              "tblCaption", "tblDescription"],
    "trPr": ["cnfStyle", "divId", "gridBefore", "gridAfter", "wBefore", "wAfter", "cantSplit", "trHeight",
             "tblHeader", "tblCellSpacing", "jc", "hidden"],
    "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap", "tcMar",
             "textDirection", "tcFitText", "vAlign", "hideMark"],
    "sectPr": ["headerReference", "footerReference", "footnotePr", "endnotePr", "type", "pgSz", "pgMar", "paperSrc",
               "pgBorders", "lnNumType", "pgNumType", "cols", "formProt", "vAlign", "noEndnote", "titlePg",
               "textDirection", "bidi", "rtlGutter", "docGrid", "printerSettings", "sectPrChange"],
}


def local(el):
    return el.tag.split("}")[1]


def put(parent, child, replace=True):
    """Insert child into parent at its schema position, replacing an existing element of the same kind."""
    order = ORDER[local(parent)]
    name = local(child)
    if replace:
        for old in parent.findall(child.tag):
            parent.remove(old)
    idx = order.index(name)
    for existing in parent:
        if local(existing) in order and order.index(local(existing)) > idx:
            existing.addprevious(child)
            return child
    parent.append(child)
    return child


def el_(tag, **attrs):
    e = OxmlElement(f"w:{tag}")
    for k, v in attrs.items():
        e.set(qn(f"w:{k}"), str(v))
    return e

def set_style_font(style, size=None, bold=None, italic=None, color=None, font=BODY_FONT):
    style.font.name = font
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), font)
    for attr in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        rfonts.attrib.pop(qn(attr), None)
    if size is not None:
        style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic
    if color is not None:
        style.font.color.rgb = color


def set_spacing(style, before=0, after=6, line=1.15, align=None, keep_next=None, page_break=None, indent_left=None):
    pf = style.paragraph_format
    pf.space_before, pf.space_after, pf.line_spacing = Pt(before), Pt(after), line
    if align is not None:
        pf.alignment = align
    if keep_next is not None:
        pf.keep_with_next = keep_next
    if page_break is not None:
        pf.page_break_before = page_break
    if indent_left is not None:
        pf.left_indent = indent_left


def add_border(ppr, side="left", color="1F3864", size=18, space=8):
    pbdr = ppr.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = put(ppr, el_("pBdr"))
    pbdr.append(el_(side, val="single", sz=size, space=space, color=color))


def shade(el_pr, fill):
    put(el_pr, el_("shd", val="clear", color="auto", fill=fill))


def add_field(paragraph, instr, placeholder=""):
    """Insert a complex Word field (TOC, PAGE, SEQ, ...) that Word computes when fields are updated.

    The placeholder is the cached result shown until Word updates the field; a list of strings is written
    as one line each, so a pre-filled list reads correctly even before the update.
    """
    def run_with(*children):
        r = OxmlElement("w:r")
        for child in children:
            r.append(child)
        paragraph._p.append(r)
        return r

    begin = el_("fldChar", fldCharType="begin", dirty="true")
    run_with(begin)
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = f" {instr} "
    run_with(it)
    run_with(el_("fldChar", fldCharType="separate"))
    lines = placeholder if isinstance(placeholder, list) else [placeholder]
    for i, line in enumerate(lines):
        t = OxmlElement("w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = line
        run_with(t, el_("br")) if i < len(lines) - 1 else run_with(t)
    run_with(el_("fldChar", fldCharType="end"))


def page_break_paragraph():
    p = OxmlElement("w:p")
    r = OxmlElement("w:r")
    br = OxmlElement("w:br")
    br.set(qn("w:type"), "page")
    r.append(br)
    p.append(r)
    return p


def section_break_paragraph(sect_pr):
    """A paragraph whose properties end a section; the given sectPr describes the section that ends here."""
    p = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    ppr.append(sect_pr)
    p.append(ppr)
    return p


def make_sect_pr(base, landscape=False):
    sp = copy.deepcopy(base)
    for tag in ("w:headerReference", "w:footerReference", "w:titlePg", "w:pgNumType"):
        for el in sp.findall(qn(tag)):
            sp.remove(el)
    w, h = (PAGE_H, PAGE_W) if landscape else (PAGE_W, PAGE_H)
    pgsz = el_("pgSz", w=w.twips, h=h.twips)
    if landscape:
        pgsz.set(qn("w:orient"), "landscape")
    put(sp, pgsz)
    put(sp, el_("type", val="nextPage"))
    return sp


def text_of(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def style_of(el):
    ps = el.find(qn("w:pPr") + "/" + qn("w:pStyle")) if el.tag == qn("w:p") else None
    return ps.get(qn("w:val")) if ps is not None else ""


def has_drawing(el):
    return el.tag == qn("w:p") and el.find(".//" + qn("w:drawing")) is not None


# ----------------------------------------------------------------------------- 1. reference document
def build_reference(path: Path, pandoc: str, lang: str, layout: dict | None = None):
    """Styled reference document; layout (from the language pack's [docx] table) may set body_size, line_spacing."""
    layout = layout or {}
    body_size, line = layout.get("body_size", 12), layout.get("line_spacing", LINE_SPACING)
    data = subprocess.run([pandoc, "--print-default-data-file", "reference.docx"],
                          check=True, capture_output=True).stdout
    path.write_bytes(data)
    doc = Document(str(path))
    st = doc.styles

    def new_style(name, base="Normal"):
        """Return the paragraph style, creating it when the reference document lacks it."""
        if name in [x.name for x in st]:
            return st[name]
        s = st.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        s.base_style = st[base]
        return s

    for name, base in (("Source Code", "Normal"), ("Captioned Figure", "Normal"), ("Figure", "Normal"),
                       ("Image Caption", "Normal"), ("Table Caption", "Normal"), ("Block Text", "Body Text"),
                       ("Footnote Text", "Normal"), ("Compact", "Body Text"), ("First Paragraph", "Body Text")):
        new_style(name, base)

    # Page setup used by pandoc for the output document
    sec = doc.sections[0]
    sec.page_width, sec.page_height = PAGE_W, PAGE_H
    sec.top_margin, sec.bottom_margin = MARGIN["top"], MARGIN["bottom"]
    sec.left_margin, sec.right_margin = MARGIN["left"], MARGIN["right"]
    sec.header_distance = sec.footer_distance = Cm(1.25)

    # Language for spelling and hyphenation, set on the document defaults
    rpr_default = doc.styles.element.find(qn("w:docDefaults") + "/" + qn("w:rPrDefault") + "/" + qn("w:rPr"))
    lang_el = rpr_default.find(qn("w:lang"))
    if lang_el is None:
        lang_el = OxmlElement("w:lang")
        rpr_default.append(lang_el)
    lang_el.set(qn("w:val"), lang)
    lang_el.set(qn("w:eastAsia"), lang)

    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        set_style_font(st[name], size=body_size)
    for name in ("Body Text", "First Paragraph"):
        set_spacing(st[name], before=0, after=6, line=line, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    set_spacing(st["Compact"], before=0, after=3, line=line, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    heads = {"Heading 1": (16, 18 if COMPACT else 0, 12, not COMPACT), "Heading 2": (14, 18, 6, False),
             "Heading 3": (12.5, 14, 4, False), "Heading 4": (12, 10, 4, False)}
    for name, (size, before, after, brk) in heads.items():
        set_style_font(st[name], size=size, bold=True, italic=False, color=NAVY)
        set_spacing(st[name], before=before, after=after, line=1.1, align=WD_ALIGN_PARAGRAPH.LEFT,
                    keep_next=True, page_break=brk)
    add_border(st["Heading 1"].element.get_or_add_pPr(), side="bottom", size=8, space=4)

    set_style_font(st["Block Text"], size=body_size, italic=True, color=RGBColor(0x26, 0x2B, 0x33))
    set_spacing(st["Block Text"], before=6, after=10, line=line, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
                indent_left=Cm(1.0))
    add_border(st["Block Text"].element.get_or_add_pPr(), side="left", size=18, space=10)

    set_style_font(st["Source Code"], size=9.5, font=MONO_FONT)
    set_spacing(st["Source Code"], before=4, after=8, line=1.0, align=WD_ALIGN_PARAGRAPH.LEFT, indent_left=Cm(0.4))
    shade(st["Source Code"].element.get_or_add_pPr(), "F2F4F7")

    for name in ("Captioned Figure", "Figure"):
        set_spacing(st[name], before=6, after=2, line=1.0, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)
    set_style_font(st["Image Caption"], size=10.5, italic=True, color=GREY)
    set_spacing(st["Image Caption"], before=2, after=12, line=1.1, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_style_font(st["Table Caption"], size=10.5, bold=True, italic=False, color=NAVY)
    set_spacing(st["Table Caption"], before=10, after=4, line=1.1, align=WD_ALIGN_PARAGRAPH.CENTER, keep_next=True)

    set_style_font(st["Footnote Text"], size=9.5)
    set_spacing(st["Footnote Text"], before=0, after=2, line=1.0, align=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # Styles added for table cells, front-matter headings and the running header
    tt = new_style("Table Text")
    set_style_font(tt, size=9.5)
    set_spacing(tt, before=1, after=1, line=1.05, align=WD_ALIGN_PARAGRAPH.LEFT)
    th = new_style("Table Header", "Table Text")
    set_style_font(th, size=9.5, bold=True, color=NAVY)
    th.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fh = new_style("Front Heading")
    set_style_font(fh, size=16, bold=True, color=NAVY)
    set_spacing(fh, before=0, after=12, line=1.1, align=WD_ALIGN_PARAGRAPH.LEFT, keep_next=True,
                page_break=not COMPACT)
    add_border(fh.element.get_or_add_pPr(), side="bottom", size=8, space=4)
    hd = new_style("Running Header")
    set_style_font(hd, size=9, italic=True, color=GREY)
    set_spacing(hd, before=0, after=0, line=1.0, align=WD_ALIGN_PARAGRAPH.LEFT)
    # Predefined Word list styles: entry text, then a dot leader to the page number at the right margin
    for i, (size, indent) in enumerate([(12, 0), (11.5, 0.6), (11, 1.2)], start=1):
        toc = new_style(f"TOC {i}")
        set_style_font(toc, size=size, bold=(i == 1))
        set_spacing(toc, before=4 if i == 1 else 0, after=2, line=1.15, indent_left=Cm(indent))
        toc.paragraph_format.tab_stops.add_tab_stop(TEXT_W_PORTRAIT, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    tof = new_style("Table of Figures")
    set_style_font(tof, size=11.5)
    set_spacing(tof, before=0, after=3, line=1.15)
    tof.paragraph_format.tab_stops.add_tab_stop(TEXT_W_PORTRAIT, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    doc.save(str(path))


# ----------------------------------------------------------------------------- 3. Word layout pass
def format_title_page(doc, body, first_h1):
    """Everything before the first Heading 1 is the title page: centred, sized, borderless."""
    els = []
    for el in list(body):
        if el is first_h1:
            break
        els.append(el)
    paras = [e for e in els if e.tag == qn("w:p")]
    texts = {id(p): text_of(p) for p in paras}
    tbl = next((e for e in els if e.tag == qn("w:tbl")), None)
    before_tbl = [p for p in paras if tbl is None or els.index(p) < els.index(tbl)]
    title_p = next((p for p in reversed(before_tbl) if texts[id(p)].isupper()), None)
    for el in els:
        if el.tag == qn("w:p"):
            p = Paragraph(el, doc)
            if style_of(el) == "ImageCaption":
                el.getparent().remove(el)          # the logo needs no caption
                continue
            pf = p.paragraph_format
            pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
            pf.space_after = Pt(4)
            pf.first_line_indent = None
            if has_drawing(el):
                for sh in p._p.iter(qn("wp:extent")):
                    ratio = int(sh.get("cy")) / int(sh.get("cx"))
                    sh.set("cx", str(int(Inches(1.6))))
                    sh.set("cy", str(int(Inches(1.6) * ratio)))
                for ext in p._p.iter(qn("a:ext")):
                    ratio = int(ext.get("cy")) / int(ext.get("cx"))
                    ext.set("cx", str(int(Inches(1.6))))
                    ext.set("cy", str(int(Inches(1.6) * ratio)))
                pf.space_before, pf.space_after = Pt(24), Pt(24)
            for r in p.runs:
                r.font.size = Pt(13)
                r.font.color.rgb = NAVY
            if el is title_p:
                # fixed spacing is a fallback for viewers that ignore vertical justification (about 7 cm in total,
                # well within one page); Word's justified section spreads the remaining space evenly
                pf.space_before, pf.space_after = Pt(48), Pt(48)
                for r in p.runs:
                    r.font.size = Pt(22)
                    r.font.bold = True
        elif el.tag == qn("w:tbl"):
            t = Table(el, doc)
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            borders = el_("tblBorders")
            for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
                borders.append(el_(side, val="nil"))
            put(el.find(qn("w:tblPr")), borders)
            for row in t.rows:
                for cell in row.cells:
                    cell.width = Cm(7.5)
                    for cp in cell.paragraphs:
                        cp.style = doc.styles["Table Text"]
                        for r in cp.runs:
                            r.font.size = Pt(12)
    # Institution lines before the logo form one block, so vertical justification keeps them together
    text_paras = [e for e in els if e.tag == qn("w:p") and e.getparent() is not None]
    logo_i = next((i for i, e in enumerate(text_paras) if has_drawing(e)), None)
    if logo_i and logo_i > 1:
        head = text_paras[0]
        for extra in text_paras[1:logo_i]:
            br = OxmlElement("w:r")
            br.append(OxmlElement("w:br"))
            head.append(br)
            for r in list(extra.findall(qn("w:r"))):
                head.append(r)
            extra.getparent().remove(extra)
    real = [e for e in els if e.tag in (qn("w:p"), qn("w:tbl")) and e.getparent() is not None]
    Paragraph(real[-1], doc).paragraph_format.space_before = Pt(48)   # place and date, below the names
    return real[-1]


def collect_entries(body):
    """Headings (levels 1-3), figure captions and table captions in document order, as (style, text) pairs."""
    heads, figs, tabs = [], [], []
    for p in body.iter(qn("w:p")):
        st = style_of(p)
        if st in ("Heading1", "Heading2", "Heading3"):
            heads.append((f"TOC {st[-1]}", text_of(p)))
        elif st == "ImageCaption":
            figs.append(("Table of Figures", text_of(p)))
        elif st == "TableCaption":
            tabs.append(("Table of Figures", text_of(p)))
    return heads, figs, tabs


def list_field(doc, instr, entries, hint):
    """A TOC-type field whose cached result is one paragraph per entry, styled with the predefined list styles
    (text, tab, page number at the right margin with a dot leader). Word fills in page numbers on update."""
    entries = entries or [("Table of Figures", hint)]
    paras = []
    for k, (style, label) in enumerate(entries):
        p = OxmlElement("w:p")
        par = Paragraph(p, doc)
        par.style = doc.styles[style]
        if k == 0:
            for child in (el_("fldChar", fldCharType="begin", dirty="true"), None,
                          el_("fldChar", fldCharType="separate")):
                r = OxmlElement("w:r")
                if child is None:
                    child = OxmlElement("w:instrText")
                    child.set(qn("xml:space"), "preserve")
                    child.text = f" {instr} "
                r.append(child)
                p.append(r)
        par.add_run(label)
        par.add_run("\t")
        paras.append(p)
    r = OxmlElement("w:r")
    r.append(el_("fldChar", fldCharType="end"))
    paras[-1].append(r)
    return paras


def convert_front_headings(doc, body):
    """Level-1 headings before Part 1 (abbreviations, terms) become front-matter headings: same look as the
    contents page, outside the table of contents. Returns the first body heading ("1. ...")."""
    body_start = None
    for el in body:
        if style_of(el) == "Heading1":
            if re.match(r"^\d+\.", text_of(el)):
                body_start = el
                break
            Paragraph(el, doc).style = doc.styles["Front Heading"]
    return body_start


def front_block(doc, heading, instr, entries, hint):
    h = OxmlElement("w:p")
    hp = Paragraph(h, doc)
    hp.style = doc.styles["Front Heading"]
    hp.add_run(heading)
    return [h] + list_field(doc, instr, entries, hint)


def insert_front_matter(doc, anchor, body_start, base_sect, labels):
    """Front matter in reading order: contents right after the title page; the report's own front pages
    (abbreviations, terms) follow; the lists of figures and tables close the front matter before Part 1.
    Returns the section properties that end the front matter (in a compact build, the title page's own)."""
    heads, figs, tabs = collect_entries(anchor.getparent())
    # The title page is its own section, vertically justified so its blocks spread over the whole page;
    # its section properties sit on the last title-page paragraph (place and date), so no empty line follows it.
    title_sect = make_sect_pr(base_sect)
    put(title_sect, el_("vAlign", val="both"))
    put(anchor.get_or_add_pPr() if hasattr(anchor, "get_or_add_pPr") else anchor.find(qn("w:pPr")), title_sect)
    if COMPACT:                     # a short document: no contents or lists; the body follows the title page directly
        return title_sect
    for el in reversed(front_block(doc, labels["contents"], 'TOC \\o "1-3" \\h \\z \\u', heads, labels["hint"])):
        anchor.addnext(el)
    # \c collects paragraphs holding a SEQ field of that name; unlike \t "Style,level" it does not depend on
    # the locale's list separator (";" on Vietnamese-region systems) or on style names
    tail = (front_block(doc, labels["lof"], 'TOC \\h \\z \\c "Figure"', figs, labels["hint"])
            + front_block(doc, labels["lot"], 'TOC \\h \\z \\c "Table"', tabs, labels["hint"]))
    fm_end = make_sect_pr(base_sect)
    tail.append(section_break_paragraph(fm_end))                       # ends the front-matter section
    target = body_start
    while target.getprevious() is not None and target.getprevious().tag == qn("w:bookmarkStart"):
        target = target.getprevious()                                  # keep Part 1's bookmark with its heading
    for el in tail:
        target.addprevious(el)
    return fm_end


def cell_texts(t):
    return [[c.text for c in row.cells] for row in t.rows]


def is_landscape_table(t):
    """Tables whose readable minimum does not fit a portrait page, and text-heavy tables, get a landscape page."""
    rows = cell_texts(t)
    body_cells = [c for r in rows[1:] for c in r]
    mean = sum(len(c) for c in body_cells) / max(1, len(body_cells))
    return mean >= LANDSCAPE_TABLE_CHARS or sum(column_limits(rows, 8.5)[0]) > TEXT_W_PORTRAIT


def column_limits(rows, font_pt):
    """(minimum, natural) width in EMU of every column.

    Minimum: the longest word fits on one line, the header wraps to at most about three lines, and a short
    column (numbers, years, names: every body cell up to SHORT_CELL characters) keeps each cell on one line;
    a long label column fits within about three lines (capped at 4 cm). Natural: every cell on one line, with
    the header on up to two lines.
    """
    char = Cm(font_pt * 0.5 / 72 * 2.54)            # average character width (about half an em)
    pad = Cm(0.35)                                  # cell margins
    mins, nats = [], []
    for j in range(len(rows[0])):
        head, body = rows[0][j], [r[j] for r in rows[1:]] or [""]
        word = max((len(w) for c in [head] + body for w in c.split()), default=1) * 1.1
        longest = max(len(c) for c in body)
        short = longest if longest <= SHORT_CELL else 0
        label = min(longest / 3, Cm(4.0) / char)
        m = max(word, len(head) / 3, short, label) * char + pad
        mins.append(m)
        nats.append(max(m, (max(longest, len(head) / 2)) * char + pad))
    return mins, nats


def column_widths(rows, total, font_pt):
    """Column widths in EMU, sized to the content.

    A table whose natural width fits takes that width (plus up to FIT_SLACK of air) and is centred, so short
    columns stay narrow. A wider table gives every column its minimum and the remaining width to the columns
    whose text still wraps, in proportion to how much text they hold; when even the minimums do not fit, the
    soft part of each minimum shrinks first, down to the longest word, and a table denser still narrows every
    column alike.
    """
    char = Cm(font_pt * 0.5 / 72 * 2.54)
    pad = Cm(0.35)
    mins, nats = column_limits(rows, font_pt)
    if sum(nats) <= total:
        scale = min(1 + FIT_SLACK, total / sum(nats))
        return [int(n * scale) for n in nats]
    word = [max((len(w) for c in [r[j] for r in rows] for w in c.split()), default=1) * 1.1 * char + pad
            for j in range(len(rows[0]))]
    if sum(mins) > total:
        soft = sum(m - w for m, w in zip(mins, word))
        over = sum(mins) - total
        mins = [m - (m - w) * min(1.0, over / soft) if soft else m for m, w in zip(mins, word)]
    if sum(mins) > total:                           # dense tables: every column narrows alike, words may break
        mins = [m * total / sum(mins) for m in mins]
    room = max(0, total - sum(mins))
    need = []
    for j, m in enumerate(mins):
        body = [r[j] for r in rows[1:]] or [""]
        need.append(max(0.0, sum(len(c) for c in body) / len(body) * char - (m - pad)))
    if sum(need) == 0:
        need = [n - m for n, m in zip(nats, mins)] if sum(nats) > sum(mins) else [1.0] * len(mins)
    return [int(m + room * n / sum(need)) for m, n in zip(mins, need)]


def style_tables(doc, body, title_tables):
    for el in body.iter(qn("w:tbl")):
        if el in title_tables:
            continue
        t = Table(el, doc)
        wide = is_landscape_table(t)
        landscape = wide and LANDSCAPE_PAGES
        total = TEXT_W_LANDSCAPE if landscape else TEXT_W_PORTRAIT
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        tblpr = el.find(qn("w:tblPr"))
        for old in tblpr.findall(qn("w:tblStyle")) + tblpr.findall(qn("w:tblLook")):
            tblpr.remove(old)
        borders = el_("tblBorders")
        for side, sz, color in (("top", 12, "1F3864"), ("left", 4, "B7C0CC"), ("bottom", 12, "1F3864"),
                                ("right", 4, "B7C0CC"), ("insideH", 4, "B7C0CC"), ("insideV", 4, "B7C0CC")):
            borders.append(el_(side, val="single", sz=sz, color=color))
        size = 9 if landscape else (8.5 if wide else 9.5)
        widths = column_widths(cell_texts(t), total, size)
        put(tblpr, el_("tblW", w=int(sum(widths) / 635), type="dxa"))
        put(tblpr, borders)
        put(tblpr, el_("tblLayout", type="fixed"))
        mar = el_("tblCellMar")
        for side, v in (("top", 40), ("left", 80), ("bottom", 40), ("right", 80)):
            mar.append(el_(side, w=v, type="dxa"))
        put(tblpr, mar)

        rows = t.rows
        grid = el.find(qn("w:tblGrid"))
        if grid is not None:
            for gc, wdt in zip(grid.findall(qn("w:gridCol")), widths):
                gc.set(qn("w:w"), str(int(wdt / 635)))
        for i, row in enumerate(rows):
            trpr = row._tr.get_or_add_trPr()
            put(trpr, el_("cantSplit"))
            if i == 0:
                put(trpr, el_("tblHeader"))            # repeat header row on every page
            for j, cell in enumerate(row.cells):
                cell.width = widths[j]
                tcpr = cell._tc.get_or_add_tcPr()
                for old in tcpr.findall(qn("w:shd")):
                    tcpr.remove(old)
                put(tcpr, el_("vAlign", val="top"))
                if i == 0:
                    shade(tcpr, "DCE3EC")
                elif i % 2 == 0:
                    shade(tcpr, "F5F7FA")
                for cp in cell.paragraphs:
                    cp.style = doc.styles["Table Header" if i == 0 else "Table Text"]
                    # headers centred, body left-aligned, overriding column alignment from the markdown
                    cp.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else WD_ALIGN_PARAGRAPH.LEFT
                    for r in cp.runs:
                        r.font.size = Pt(size)


def mark_captions(doc, body, labels):
    """Prepare captions for Word's figure and table lists, and keep each caption with its object.

    Bold 'Table x.y.' paragraphs above a table become Table Caption. Every figure and table caption then
    receives a hidden SEQ field (\\h hides its result), which is how Word's own captions register with
    TOC \\c lists; the visible caption text with its hierarchical number stays as written.
    """
    pat = re.compile(r"^(%s)\s+[A-Z0-9]+(\.\d+)*\." % "|".join(labels["table_prefix"]))
    counts = {"Figure": 0, "Table": 0}
    for el in list(body.iter(qn("w:p"))):
        nxt = el.getnext()
        seq = None
        if pat.match(text_of(el)) and nxt is not None and nxt.tag == qn("w:tbl"):
            p = Paragraph(el, doc)
            p.style = doc.styles["Table Caption"]
            for r in p.runs:
                r.font.bold = None
            seq = "Table"
        elif style_of(el) == "ImageCaption":
            seq = "Figure"
        if seq:
            add_field(Paragraph(el, doc), f"SEQ {seq} \\h", "")
            counts[seq] += 1
        if has_drawing(el):
            Paragraph(el, doc).paragraph_format.keep_with_next = True
    return counts


def size_image(par_el, max_w, max_h):
    ext = par_el.find(".//" + qn("wp:extent"))
    cx, cy = int(ext.get("cx")), int(ext.get("cy"))
    ratio = cx / cy
    w = min(int(max_w), int(max_h * ratio))
    h = int(w / ratio)
    ext.set("cx", str(w))
    ext.set("cy", str(h))
    for a in par_el.iter(qn("a:ext")):
        a.set("cx", str(w))
        a.set("cy", str(h))
    return ratio


def image_ratio(par_el):
    ext = par_el.find(".//" + qn("wp:extent"))
    return int(ext.get("cx")) / int(ext.get("cy"))


def lines_estimate(el, width_cm):
    chars_per_line = width_cm * 4.3   # ~12 pt Times New Roman
    return max(1, int(len(text_of(el)) / chars_per_line) + 1)


def landscape_groups(doc, body, labels, start_after):
    """Find wide figures and wide tables, together with the paragraph that introduces them."""
    fig_ref = re.compile(r"(%s)\s+\d+\.\d+" % "|".join(labels["fig_prefix"]))
    groups = []
    started = start_after is None
    for el in list(body):
        if not started:
            started = el is start_after
            continue
        if has_drawing(el):
            ratio = image_ratio(el)
            cap = el.getnext()
            end = cap if cap is not None and style_of(cap) == "ImageCaption" else el
            prev = el.getprevious()
            intro = prev if (prev is not None and style_of(prev) in ("BodyText", "FirstParagraph")
                             and fig_ref.search(text_of(prev))) else None
            # Compare the printed width in each orientation, leaving room for the introduction and the caption
            intro_cm = 0.62 * lines_estimate(intro, TEXT_W_LANDSCAPE / 360000) if intro is not None else 0
            land_h = TEXT_H_LANDSCAPE - Cm(2.0) - Cm(intro_cm)
            land_w = min(TEXT_W_LANDSCAPE, land_h * ratio)
            port_w = min(TEXT_W_PORTRAIT, Cm(19) * ratio)
            if LANDSCAPE_PAGES and land_w >= port_w * LANDSCAPE_GAIN:
                size_image(el, TEXT_W_LANDSCAPE, land_h)
                groups.append((intro if intro is not None else el, end))
            else:
                size_image(el, TEXT_W_PORTRAIT, Cm(19))
        elif LANDSCAPE_PAGES and el.tag == qn("w:tbl") and is_landscape_table(Table(el, doc)):
            prev = el.getprevious()
            start = prev if prev is not None and style_of(prev) == "TableCaption" else el
            groups.append((start, el))
    return groups


def only_bookmarks_between(a, b):
    el = a.getnext()
    while el is not None and el is not b:
        if el.tag not in (qn("w:bookmarkStart"), qn("w:bookmarkEnd")):
            return False
        el = el.getnext()
    return el is b


def apply_landscape(groups, base_sect):
    """Wrap each group in its own landscape section; adjacent groups share one section with page breaks."""
    merged = []
    for start, end in groups:
        if merged and only_bookmarks_between(merged[-1][-1][1], start):
            merged[-1].append((start, end))
        else:
            merged.append([(start, end)])
    for run in merged:
        first_start, last_end = run[0][0], run[-1][1]
        first_start.addprevious(section_break_paragraph(make_sect_pr(base_sect)))   # ends the portrait part
        for start, _ in run[1:]:
            start.addprevious(page_break_paragraph())
        last_end.addnext(section_break_paragraph(make_sect_pr(base_sect, landscape=True)))


def setup_headers_and_numbering(doc, labels, fm_end):
    """Title page without header or footer; front matter numbered i, ii, iii; Part 1 starts again at 1
    (in a compact build there is no separate front matter, so the page after the title page is 1)."""
    secs = doc.sections
    width = TEXT_W_PORTRAIT
    body_idx = next(i for i, sec in enumerate(secs) if sec._sectPr is fm_end) + 1
    for i, s in enumerate(secs):
        landscape = s.orientation == WD_ORIENT.LANDSCAPE
        if i == 0:                                   # title page: no header, no footer
            s.header.is_linked_to_previous = False
            s.footer.is_linked_to_previous = False
            continue
        if i == body_idx:                            # the first body section (directly after the title page when compact)
            put(s._sectPr, el_("pgNumType", fmt="decimal", start=1))
        elif i == 1:
            put(s._sectPr, el_("pgNumType", fmt="lowerRoman", start=1))
        elif i < body_idx:
            put(s._sectPr, el_("pgNumType", fmt="lowerRoman"))
        if i == 1 or landscape or (i > 1 and secs[i - 1].orientation == WD_ORIENT.LANDSCAPE):
            # a new header per orientation change so the right-aligned tab matches the page width
            s.header.is_linked_to_previous = False
            s.footer.is_linked_to_previous = False
            w = TEXT_W_LANDSCAPE if landscape else width
            hp = s.header.paragraphs[0]
            hp.style = doc.styles["Running Header"]
            hp.paragraph_format.tab_stops.add_tab_stop(w, WD_TAB_ALIGNMENT.RIGHT)
            hp.add_run(labels["short_title"] + "\t" + labels["author"])
            add_border(hp._p.get_or_add_pPr(), side="bottom", color="B7C0CC", size=4, space=4)
            fp = s.footer.paragraphs[0]
            fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_field(fp, "PAGE", "1")
            for r in fp.runs:
                r.font.size = Pt(10)


def finalize_settings(doc, labels):
    settings = doc.settings.element
    for old in settings.findall(qn("w:updateFields")):
        settings.remove(old)
    upd = el_("updateFields", val="true")
    # updateFields belongs right after the zoom/view block; placing it first among optional settings is accepted
    zoom = settings.find(qn("w:zoom"))
    (zoom.addnext(upd) if zoom is not None else settings.insert(0, upd))
    cp = doc.core_properties
    cp.title, cp.author, cp.language = labels["title"], labels["author"], labels["lang"]
    cp.subject = labels.get("subject") or ""


SVG_EXT = "{96DAC541-7B7A-43D3-8B79-37D633B846F1}"      # Office's extension for an SVG beside its PNG fallback
SVG_NS = "http://schemas.microsoft.com/office/drawing/2016/SVG/main"


def attach_svg(doc, src: Path) -> int:
    """Give every figure whose PNG has an SVG twin in <src>/assets/figures the SVG as well, the way Word itself
    stores an SVG picture: the PNG stays as the fallback for older readers, Word 2016+ draws the vector version
    (sharp at any zoom, text selectable) and Word 365 can turn it into editable shapes (Convert to Shape)."""
    import hashlib
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    from docx.opc.packuri import PackURI
    from docx.opc.part import Part
    from lxml import etree
    twins = {}
    for png in (src / "assets" / "figures").glob("*.png"):
        svg = png.with_suffix(".svg")
        if svg.exists():
            twins[hashlib.sha1(png.read_bytes()).hexdigest()] = svg
    done = {}
    for rel in list(doc.part.rels.values()):
        if rel.reltype != RT.IMAGE or rel.is_external:
            continue
        svg = twins.get(hashlib.sha1(rel.target_part.blob).hexdigest())
        if svg is None:
            continue
        part = Part(PackURI(f"/word/media/{svg.stem}-{rel.rId}.svg"), "image/svg+xml", svg.read_bytes(),
                    doc.part.package)
        done[rel.rId] = doc.part.relate_to(part, RT.IMAGE)
    for blip in doc.element.body.iter(qn("a:blip")):
        rid = blip.get(qn("r:embed"))
        if rid in done and blip.find(qn("a:extLst")) is None:
            ext_lst = etree.SubElement(blip, qn("a:extLst"))
            ext = etree.SubElement(ext_lst, qn("a:ext"))
            ext.set("uri", SVG_EXT)
            svg_blip = etree.SubElement(ext, f"{{{SVG_NS}}}svgBlip", nsmap={"asvg": SVG_NS})
            svg_blip.set(qn("r:embed"), done[rid])
    return len(done)


def build(lang: str, pandoc: str, src: Path, out: Path, meta: dict):
    labels = labels_for(lang, src, meta)
    cache = CACHE
    cache.mkdir(parents=True, exist_ok=True)
    ref = cache / f"reference-{lang}.docx"
    layout = {**(labels.get("layout") or {}), **meta.get("task_layout", {})}   # the task's [layout] overrides the pack
    build_reference(ref, pandoc, labels["lang"], layout)
    raw = cache / f"pandoc-{lang}.docx"
    files = [p.name for p in labels["files"]()]
    # report_format.lua enforces the house style in the output: "—" → "–", ordered lists numbered (1), (2) …
    subprocess.run([pandoc, *files, "--from", "markdown", "--to", "docx", "--reference-doc", str(ref),
                    "--lua-filter", str(HERE / "report_format.lua"), "--metadata", f"figure_lang={meta.get('figure_lang', lang)}",
                    "--resource-path", ".", "-o", str(raw)], cwd=src, check=True)

    doc = Document(str(raw))
    body = doc.element.body
    base_sect = body.find(qn("w:sectPr"))
    for tag in ("w:headerReference", "w:footerReference", "w:titlePg"):
        for el in base_sect.findall(qn(tag)):
            base_sect.remove(el)

    first_h1 = next(el for el in body if style_of(el) == "Heading1")
    title_tables = [el for el in body if el.tag == qn("w:tbl") and el.getnext() is not None
                    and list(body).index(el) < list(body).index(first_h1)]
    title_end = format_title_page(doc, body, first_h1)
    body_start = convert_front_headings(doc, body)
    style_tables(doc, body, title_tables)
    counts = mark_captions(doc, body, labels)
    groups = landscape_groups(doc, body, labels, start_after=title_end)
    apply_landscape(groups, base_sect)
    fm_end = insert_front_matter(doc, title_end, body_start, base_sect, labels)
    setup_headers_and_numbering(doc, labels, fm_end)
    finalize_settings(doc, labels)
    n_svg = attach_svg(doc, src) if meta.get("vector") else 0

    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out))
    raw.unlink()
    n_land = sum(1 for s in doc.sections if s.orientation == WD_ORIENT.LANDSCAPE)
    print(f"[{lang}] {len(files)} sections → {shown(out)}  "
          f"({len(doc.sections)} Word sections, {n_land} landscape, {len(doc.inline_shapes)} images, "
          f"{counts['Figure']} figure and {counts['Table']} table captions listed"
          + (f", {n_svg} figures as SVG with PNG fallback" if meta.get("vector") else "") + ")")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", required=True, help="folder of markdown sections, relative to the project root")
    ap.add_argument("--lang", required=True, help="language pack code (en, vi, ...)")
    ap.add_argument("--out", required=True, help="output .docx path, relative to the project root")
    ap.add_argument("--title", required=True, help="document title (title metadata)")
    ap.add_argument("--short-title", required=True, help="running header title")
    ap.add_argument("--author", required=True, help="author shown in the header and metadata")
    ap.add_argument("--subject", default="", help="subject metadata")
    ap.add_argument("--figure-lang", default=None,
                    help="use figure.<code>.png where it exists (default: the build language; the source language, e.g. en, keeps the original figures)")
    ap.add_argument("--portrait", action="store_true",
                    help="keep every page in portrait (no landscape sections), e.g. for editing in Google Docs")
    ap.add_argument("--body-size", type=float, help="body font size in pt (default: the pack's [docx] body_size or 12)")
    ap.add_argument("--line-spacing", type=float, help="line spacing of running text (default: the pack's or 1.3)")
    ap.add_argument("--vector", action="store_true",
                    help="figures with an SVG twin go in as SVG with their PNG as fallback (sharp at any zoom)")
    ap.add_argument("--compact", action="store_true",
                    help="short document: no page breaks before parts, no contents or lists, arabic numbering from 1")
    args = ap.parse_args()
    global LANDSCAPE_PAGES, COMPACT
    COMPACT = args.compact
    LANDSCAPE_PAGES = not (args.portrait or args.compact)   # a short document stays portrait: no breaks around rotated pages
    meta = dict(title=args.title, short_title=args.short_title, author=args.author, subject=args.subject,
                vector=args.vector and not args.portrait,
                figure_lang=args.figure_lang or args.lang,
                task_layout={k: v for k, v in (("body_size", args.body_size), ("line_spacing", args.line_spacing)) if v})
    build(args.lang, pypandoc.get_pandoc_path(), (ROOT / args.src).resolve(), (ROOT / args.out).resolve(), meta)


if __name__ == "__main__":
    sys.exit(main())
