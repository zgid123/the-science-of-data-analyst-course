"""Slide-deck kit of the build-report skill: theme, type scale, layout blocks, diagrams, charts and translation.

A deck is a Python script in the project root that draws its slides with this kit and builds one .pptx per language
(see slides.md in the skill for the workflow and the design rules). Typical start of a deck script:

    import sys
    sys.path.insert(0, ".claude/skills/build-report/scripts")
    import slidekit as kit
    from slidekit import T, D, I, PT, lead, node, flow_row, chart, ...

    def s_example(prs):
        s = kit.base(prs, K["p1"], T("Short Topic Title"), T("(~50 seconds) Speaker notes ..."))
        y = lead(s, T("One sentence that states what the slide shows"))
        flow_row(s, y, 1.5, [(T("Step"), T("what happens"), "agent"), ...])

    kit.use_strings("slides_taskN_vi")          # Vietnamese strings, keyed by the English text
    kit.build_deck(lang, SLIDES, OUT[lang], FOOTER_EN, cache=..., before=kickers)

Layers, all lengths in inches unless a name says EMU:
  theme        colours (NAVY, INK, GREY, LINE, SOFT, WHITE, PLUS, MINUS, BLUE, WARM, VIOLET and fills), the 16:9 page
               (W, H, MX, TOP, BOTTOM, CW, END) and one fixed type scale PT; text never shrinks to fit
  primitives   text, rect, base (kicker, title, rule, footer, slide number, optional presenter), table, points,
               number_fields, arial_theme, title_size
  measuring    lh / line_h, list_height, list_h, node_h, num_h, room (reports content that does not fit);
               slide_measure.tighten() shrinks every text box to its text after a slide is built
  blocks       lead, note, foot, table_at, cards / cards_at, panel_list, panels, side_cards, split, bignum
  diagrams     node (styled boxes: soft, agent, system, input, out, bad, ref, white, violet), chip, flow_row, arrow,
               path (elbow arrows), label, link, brace_label, picture, formula (mathtext rendered once)
  charts       chart() renders a matplotlib drawing at 400 dpi at its exact size on the slide; clean_axes, HEX,
               chart colours C_*; D() writes numbers with the language's decimal mark
  strings      T() returns the English text or its form in the deck's VI module; MISSING collects keys without one
  deck         build_deck() builds, tightens, numbers and saves one language and reports missing strings

Command line (run from the project root):
  python .claude/skills/build-report/scripts/slidekit.py strings DECK.py [--all] [--out FILE.json]
        English strings of a deck that its Vietnamese module lacks (or all of them), for the translator
  python .claude/skills/build-report/scripts/slidekit.py text DECK.pptx [--out FILE.md]
        every slide's text, table cells and speaker notes in order, for the reviewer's first reading pass
  python .claude/skills/build-report/scripts/slidekit.py sync DECK.py [--write [--prune]]
        after English edits: missing and unused VI keys, and the old key each changed English string replaces
  python .claude/skills/build-report/scripts/slidekit.py diff A.pptx B.pptx
        compare two built decks part by part (proves that a refactor of a deck script changes nothing)
  python .claude/skills/build-report/scripts/slidekit.py prompt translate|review DECK.py --task T
        --voice group|solo --scratch DIR [--log FILE] [--focus TEXT]
        the translator's or reviewer's prompt, filled from the deck, the task and the language pack
"""

import argparse
import hashlib
import importlib
import importlib.util
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from lxml import etree
from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

from slide_measure import Para, font_path, tighten, walk
from slide_measure import text_height as paras_height

import palette as pal
from common import CONFIG, PYTHON, ROOT, shown                      # the project root and interpreter (common.py)
I = Inches
EMU = 914400

# ----------------------------------------------------------------------------- theme
FONT = "Arial"
TITLE_FONT = font_path(True)
# Colours come from palette.py, shared with report figures and charts, so a role looks the same on a slide and on
# the page. RGBColor values for shapes, bare hex strings (C_*) for matplotlib (HEX(C_BLUE) adds the "#").
NAVY = pal.rgb(pal.NAVY)
INK = pal.rgb(pal.INK)
GREY = pal.rgb(pal.MUTED)
LINE = pal.rgb("#D5DAE1")
SOFT = pal.rgb(pal.SOFT)
TINT = pal.rgb("#EAF0F8")
WHITE = pal.rgb(pal.SURFACE)
PLUS = pal.rgb(pal.GOOD)                        # strength, correct, output
MINUS = pal.rgb(pal.CRITICAL)                   # limitation, error
BLUE = pal.rgb(pal.BLUE)                        # systems, baselines (series slot 1)
WARM = pal.rgb(pal.ORANGE)                      # agents, the method under study (series slot 2)
TEAL = pal.rgb(pal.TEAL)
VIOLET = pal.rgb(pal.VIOLET)
GOLD = pal.rgb(pal.GOLD)
MAGENTA = pal.rgb(pal.MAGENTA)
AGENT_FILL = pal.rgb(pal.tint(pal.ORANGE))
AGENT_INK = pal.rgb(pal.shade(pal.ORANGE, 0.4))
OUT_FILL = pal.rgb(pal.tint(pal.GOOD))
OUT_INK = pal.rgb(pal.shade(pal.GOOD, 0.3))
BAD_FILL = pal.rgb(pal.tint(pal.CRITICAL))
INPUT = pal.rgb(pal.EXTERNAL)
REF_FILL = pal.rgb(pal.tint(pal.BLUE))
VIOLET_FILL = pal.rgb(pal.tint(pal.VIOLET))
HEX = lambda c: f"#{c}"
C_BLUE, C_WARM, C_GREYBAR, C_VIOLET, C_GREEN, C_RED = (c[1:] for c in (pal.BLUE, pal.ORANGE, pal.OTHER, pal.VIOLET,
                                                                       pal.GOOD, pal.CRITICAL))
C_TEAL, C_GOLD, C_MAGENTA = pal.TEAL[1:], pal.GOLD[1:], pal.MAGENTA[1:]
C_INK, C_MUTED, C_GRID = pal.INK[1:], pal.MUTED[1:], pal.GRID[1:]

W, H = Inches(13.333), Inches(7.5)
MX = Inches(0.3)                                # side margin, kept small so figures can be large
TOP = Inches(1.1)                               # content starts below the compact title band
BOTTOM = Inches(7.12)                           # content ends above the footer
CW = W - 2 * MX                                 # content width (EMU)
CH = BOTTOM - TOP                               # content height (EMU)
END = 6.95                                      # bottom of the content area (inches)

# One type scale (pt) on every slide. Roles: the title slide (cover), slide titles (title), the lead line under a
# title (lead), card and panel heads (head), body text, list items and table cells (body), captions, sources and
# diagram bodies (small), large statistics (number), section labels (kicker) and the footer (footer).
PT = {"cover": 36, "title": 26, "lead": 18, "head": 18, "body": 16, "small": 12, "number": 48, "kicker": 11,
      "footer": 9}

# ----------------------------------------------------------------------------- state of the deck being built
LANG = "en"
FOOTER = ""
CACHE = ROOT / "build" / ".cache" / "slides"
MISSING = []
_VI = {"module": None, "override": None}


def use_strings(module):
    """Name the module whose dict VI maps each English string to its Vietnamese form (e.g. "slides_taskN_vi")."""
    _VI["module"] = module


def T(en):
    """The text of the language being built: the English string, or its form from the deck's VI module."""
    if LANG == "en":
        return en
    table = _VI["override"]
    if table is None:
        table = importlib.import_module(_VI["module"]).VI if _VI["module"] else {}
    vi = table.get(en)
    if vi is None:
        MISSING.append(en)
        return en
    return vi


def D(v, digits=2):
    """A number written with the decimal mark of the language being built."""
    s = f"{v:.{digits}f}"
    return s if LANG == "en" else s.replace(".", ",")


# ----------------------------------------------------------------------------- primitives
def text(slide, x, y, w, h, runs, size=18, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
         spacing=1.1):
    """Add a text box (EMU). `runs` is a string, or a list of paragraphs; a paragraph is a string or a list of
    (text, color, bold) runs."""
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(0.05)
    tf.margin_top = tf.margin_bottom = Inches(0.02)
    for i, para in enumerate(runs if isinstance(runs, list) else [runs]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = spacing
        p.space_after = Pt(size * 0.45)
        for t, c, b in (para if isinstance(para, list) else [(para, color, bold)]):
            r = p.add_run()
            r.text = t
            r.font.name, r.font.size, r.font.bold = FONT, Pt(size), b
            r.font.color.rgb = c
    return box


def rect(slide, x, y, w, h, fill=None, line=None, radius=False, line_w=1.0):
    """A rectangle (EMU), rounded when `radius`; no fill or outline when the colour is None."""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, x, y, w, h)
    if radius:
        shape.adjustments[0] = 0.06
    if fill is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(line_w)
    shape.shadow.inherit = False
    return shape


def title_size(title, width, start=28, minimum=20):
    """Largest font size (pt) at which the title fits on one line, measured with Arial Bold metrics."""
    for pt in range(start, minimum - 1, -1):
        if ImageFont.truetype(TITLE_FONT, pt * 10).getlength(title) / 720 * 914400 <= width * 0.97:
            return pt
    return minimum


def base(prs, kicker, title, notes, presenter=None):
    """Content slide: small section label, short topic title, accent rule, footer, slide number and speaker notes;
    with `presenter`, the presenter's name is right-aligned on the kicker line. A deck built without a footer
    (footer_en "" or None) puts the slide number at the right end of the kicker line instead, and can lower END."""
    s = prs.slides.add_slide(prs.slide_layouts[6])
    number = len(prs.slides)
    text(s, MX, Inches(0.14), Inches(9), Inches(0.28), kicker.upper(), size=PT["kicker"], color=GREY, bold=True)
    text(s, MX, Inches(0.36), CW, Inches(0.55), title, size=PT["title"] or title_size(title, CW, start=26), color=NAVY,
         bold=True, spacing=1.0)
    rect(s, MX, Inches(0.94), Inches(0.8), Inches(0.04), fill=NAVY)
    if FOOTER:
        text(s, MX, H - Inches(0.33), Inches(9), Inches(0.28), FOOTER, size=PT["footer"], color=GREY)
        num = text(s, W - MX - Inches(1), H - Inches(0.33), Inches(1), Inches(0.28), str(number), size=PT["footer"],
                   color=GREY, align=PP_ALIGN.RIGHT)
    else:                                       # no footer: the number sits at the right end of the kicker line
        num = text(s, W - MX - Inches(1), Inches(0.14), Inches(1), Inches(0.28), str(number), size=PT["kicker"],
                   color=GREY, bold=True, align=PP_ALIGN.RIGHT)
    num.name = "Slide Number"
    s.notes_slide.notes_text_frame.text = notes
    if presenter:
        text(s, W - MX - I(5), I(0.14), I(5), I(0.28), T("Presenter: ") + presenter, size=PT["kicker"], color=GREY,
             bold=True, align=PP_ALIGN.RIGHT)
    return s


def number_fields(prs):
    """Turn each slide's page number into PowerPoint's slide-number field, so it follows any reordering."""
    import uuid
    for slide in prs.slides:
        for shape in walk(slide.shapes):
            if shape.name != "Slide Number" or not shape.has_text_frame:
                continue
            for p in shape.text_frame.paragraphs:
                for r in list(p._p.findall(qn("a:r"))):
                    fld = r.makeelement(qn("a:fld"), {"id": "{%s}" % str(uuid.uuid4()).upper(), "type": "slidenum"})
                    for child in list(r):
                        fld.append(child)                   # keeps the run's font, size, colour and cached number
                    r.addprevious(fld)
                    p._p.remove(r)


def arial_theme(path):
    """Set the theme fonts to Arial, so text that inherits them (speaker notes, chart labels) matches the slides."""
    tmp = path.with_suffix(".tmp")
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.startswith("ppt/theme/") and item.filename.endswith(".xml"):
                data = re.sub(rb'(<a:latin typeface=")[^"]*(")', rb"\1Arial\2", data)
            zout.writestr(item, data)
    shutil.move(tmp, path)


def points(slide, x, y, w, h, heading, items, color, size=None, marker="•"):
    """A bold heading and a bulleted list (EMU) at PT["body"]."""
    size = size or PT["body"]
    paras = [[(heading, color, True)]] + [[(f"{marker}  ", color, True), (t, INK, False)] for t in items]
    text(slide, x, y, w, h, paras, size=size, spacing=1.05)


def _table(slide, x, y, w, rows, col_w, size=14, row_h=Inches(0.42)):
    shape = slide.shapes.add_table(len(rows), len(rows[0]), x, y, w, row_h * len(rows))
    tbl = shape.table
    for j, cw in enumerate(col_w):
        tbl.columns[j].width = cw
    for i, row in enumerate(rows):
        tbl.rows[i].height = row_h if i else Inches(0.55)
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.margin_left = cell.margin_right = Inches(0.12)
            cell.margin_top = cell.margin_bottom = Inches(0.06)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.fill.solid()
            cell.fill.fore_color.rgb = NAVY if i == 0 else (SOFT if i % 2 == 0 else WHITE)
            p = cell.text_frame.paragraphs[0]
            cell.text_frame.word_wrap = True
            r = p.add_run()
            r.text = val
            r.font.name, r.font.size = FONT, Pt(size)
            r.font.bold = i == 0 or j == 0
            r.font.color.rgb = WHITE if i == 0 else (NAVY if j == 0 else INK)
    return shape


def table(slide, x, y, w, rows, col_w, size=None, row_h=None):
    """A table (EMU) with a navy header row and a bold first column; every row is as tall as its wrapped cells
    need, at least `row_h`."""
    size = size or PT["body"]
    shape = _table(slide, x, y, w, rows, col_w, size=size, row_h=row_h or Inches(0.42))
    tbl, total = shape.table, 0
    for i, row in enumerate(rows):
        need = max(line_h(v, cw / EMU - 0.24, size, i == 0 or j == 0) for j, (v, cw) in enumerate(zip(row, col_w)))
        hgt = max(need + 0.16, (row_h / EMU if row_h and i else 0.55 if not i else 0))
        tbl.rows[i].height = Inches(hgt)
        total += hgt
    shape.height = Inches(total)
    room("table", y / EMU + total, BOTTOM / EMU)
    return shape


def link(s, x1, y1, x2, y2, head=True, color=GREY):
    """A straight connector (EMU), with an arrowhead at its end unless `head` is False."""
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x1, y1, x2, y2)
    c.line.color.rgb, c.line.width = color, Pt(1.75)
    if head:
        etree.SubElement(c.line._get_or_add_ln(), qn("a:tailEnd"), type="triangle", w="med", len="med")
    return c


# ----------------------------------------------------------------------------- measuring
def para_h(paras, w):
    """Height of the paragraphs wrapped to width w (inches)."""
    return paras_height(paras, w)


def line_h(text_, w, pt, bold=False):
    """Height in inches of one text box's paragraph at `pt`, wrapped to width w (inches)."""
    return para_h([Para(text_, pt, bold)], w)


def lh(line, w, pt=None, bold=False):
    """Height in inches of a paragraph wrapped to width w (inches), PT["body"] by default."""
    return line_h(line, w, pt or PT["body"], bold)


def bullets_height(items, w, pt=None, spacing=1.1):
    """Height in inches of a bulleted list as text() lays it out (one paragraph per item, space after each)."""
    pt = pt or PT["body"]
    return sum(para_h([Para("•  " + t, pt, spacing=spacing)], w) + pt * 0.45 / 72 for t in items)


def list_height(head, items, w):
    """Height in inches of points(): a bold heading and a bulleted list at PT["body"]."""
    pt = PT["body"]
    return para_h([Para(head, pt, True, spacing=1.05)], w) + pt * 0.45 / 72 + bullets_height(items, w, pt, 1.05)


def num_h(pt):
    """Height of one line of a large number."""
    return pt * 1.25 / 72


def room(where, need, have):
    """Report content that does not fit its area at the fixed type scale (the slide then needs a new layout)."""
    if need > have + 0.01:
        print(f"  ! {LANG} {where}: needs {need:.2f} in, has {have:.2f} in", file=sys.stderr)


# ----------------------------------------------------------------------------- blocks
def lead(s, line, y=None):
    """A one-sentence lead under the title (PT["lead"]); returns the y (inches) below it."""
    y = y if y is not None else TOP / EMU + 0.15
    hgt = lh(line, CW / EMU, PT["lead"])
    text(s, MX, I(y), CW, I(hgt), line, size=PT["lead"], color=INK, spacing=1.0)
    return y + hgt + 0.2


def note(s, line, y, x=None, w=None, color=GREY):
    """A source or caveat line at PT["small"] at y (inches); returns the y below it."""
    x = x if x is not None else MX / EMU
    w = w if w is not None else CW / EMU
    hgt = lh(line, w, PT["small"])
    text(s, I(x), I(y), I(w), I(hgt), line, size=PT["small"], color=color, spacing=1.0)
    return y + hgt


def foot(s, line):
    """A source line placed at the bottom of the content area."""
    note(s, line, END - lh(line, CW / EMU, PT["small"]))


def table_at(s, rows, fracs, y, x=None, w=None, size=None):
    """A table with column shares `fracs` at (x, y) inches; returns its bottom (inches)."""
    size = size or PT["body"]
    x = I(x) if x is not None else MX
    w = I(w) if w is not None else CW
    widths = [int(w * f) for f in fracs]
    widths[-1] = w - sum(widths[:-1])
    shape = table(s, x, I(y), w, rows, widths, size=size)
    return y + shape.height / EMU


def cards(s, items, cols, y0=None, height=None, number=True, color=NAVY, size=None, head_size=None, icons=None):
    """A grid of rounded cards (EMU); each item is (heading, body). Numbered cards show a large index first. Every
    card takes the height of the tallest, and the grid is centred vertically in the available area; returns its
    bottom (EMU). `icons` (icons.py names, one per card) adds an icon in the card colour: at the right end of the
    number row on numbered cards, otherwise before the heading."""
    bs, hs = size or PT["body"], head_size or PT["head"]
    isz = CARD_ICON
    y0 = (y0 if y0 is not None else TOP + Inches(0.2)) / EMU
    height = (height if height is not None else CH - Inches(0.3)) / EMU
    rows = (len(items) + cols - 1) // cols
    gap = 0.25
    cw = (CW / EMU - (cols - 1) * gap) / cols
    inner = cw - 0.6
    nh = num_h(PT["number"]) if number else 0
    hw = inner - (isz + 0.15 if icons and not number else 0)        # heading width beside an inline icon
    head_h = lambda head: max(line_h(head, hw, hs, True), isz if icons and not number else 0)
    tallest = max(0.3 + nh + head_h(head) + 0.15 + line_h(body, inner, bs) + 0.3 for head, body in items)
    room("cards", rows * tallest + (rows - 1) * gap, height)
    top = y0 + (height - (rows * tallest + (rows - 1) * gap)) / 2
    for i, (head, body) in enumerate(items):
        x, y = MX / EMU + (i % cols) * (cw + gap), top + (i // cols) * (tallest + gap)
        rect(s, Inches(x), Inches(y), Inches(cw), Inches(tallest), fill=SOFT, line=LINE, radius=True)
        ty = y + 0.3
        if number:
            text(s, Inches(x + 0.3), Inches(y + 0.2), Inches(1.2), Inches(nh), str(i + 1), size=PT["number"],
                 color=color, bold=True, spacing=1.0)
            ty += nh
        hx = x + 0.3
        if icons and icons[i]:
            if number:
                icon(s, icons[i], x + cw - 0.3 - isz, y + 0.2 + (nh - isz) / 2, isz, color=color, bg=SOFT)
            else:
                lh1 = line_h("A", hw, hs, True)
                icon(s, icons[i], hx, ty + (lh1 - isz) / 2, isz, color=color, bg=SOFT)
                hx += isz + 0.15
        hh = line_h(head, hw, hs, True)
        text(s, Inches(hx), Inches(ty), Inches(hw), Inches(hh), head, size=hs, color=color, bold=True,
             spacing=1.0)
        hh = head_h(head)
        text(s, Inches(x + 0.3), Inches(ty + hh + 0.15), Inches(inner), Inches(line_h(body, inner, bs)), body, size=bs,
             color=INK, spacing=1.0)
    return Inches(top + rows * tallest + (rows - 1) * gap)


def cards_at(s, items, cols, y, number=False, color=NAVY, bottom=None, icons=None):
    """A grid of cards from y (inches) down to `bottom`; returns its bottom (inches)."""
    bottom = bottom or END
    return cards(s, items, cols, y0=I(y), height=I(bottom - y), number=number, color=color, icons=icons) / EMU


def panel_list(s, x, y, w, h, head, items, color=NAVY):
    """A soft panel with a bold heading and bullets (PT["body"]) at (x, y, w, h) inches."""
    rect(s, I(x), I(y), I(w), I(h), fill=SOFT, line=LINE, radius=True)
    points(s, I(x + 0.25), I(y + 0.2), I(w - 0.5), I(h - 0.4), head, items, color)


def list_h(head, items, w):
    """Height of panel_list's content for inner width w (inches), with its padding."""
    return list_height(head, items, w - 0.5) + 0.45


def panels(s, y0, left, right, y1=None, split=0.5):
    """Two side-by-side bullet panels (heading, items, colour) of one shared height, centred between y0 and y1."""
    y1 = y1 or END
    gap = 0.3
    lw = (CW / EMU - gap) * split
    rw = CW / EMU - gap - lw
    ph = max(list_h(left[0], left[1], lw), list_h(right[0], right[1], rw))
    room("panels", ph, y1 - y0)
    y = y0 + max(0.0, (y1 - y0 - ph) / 2)
    panel_list(s, MX / EMU, y, lw, ph, *left)
    panel_list(s, MX / EMU + lw + gap, y, rw, ph, *right)
    return y + ph


def side_cards(s, x, y, w, items, bottom=None, gap=0.25):
    """Stacked cards (head, body, colour) in a side column, centred between y and bottom; returns their bottom."""
    bottom = bottom or END
    hh = [lh(a, w - 0.5, PT["head"], True) + 0.1 + lh(b, w - 0.5) + 0.4 for a, b, _ in items]
    yy = y + max(0, (bottom - y - sum(hh) - gap * (len(items) - 1)) / 2)
    for (a, b, c), hgt in zip(items, hh):
        rect(s, I(x), I(yy), I(w), I(hgt), fill=SOFT, line=LINE, radius=True)
        ah = lh(a, w - 0.5, PT["head"], True)
        text(s, I(x + 0.25), I(yy + 0.2), I(w - 0.5), I(ah), a, size=PT["head"], color=c, bold=True, spacing=1.0)
        text(s, I(x + 0.25), I(yy + 0.3 + ah), I(w - 0.5), I(lh(b, w - 0.5)), b, size=PT["body"], color=INK,
             spacing=1.0)
        yy += hgt + gap
    return yy - gap


def split(frac, gap=0.35):
    """Left width, right width and right x (inches) of a two-column layout, the left taking `frac` of the width."""
    lw = (CW / EMU - gap) * frac
    return lw, CW / EMU - gap - lw, MX / EMU + lw + gap


def bignum(s, x, y, w, value, line, color=NAVY):
    """A large number with its label under it, centred in width w (inches); returns the height used."""
    vh = num_h(PT["number"])
    text(s, I(x), I(y), I(w), I(vh), value, size=PT["number"], color=color, bold=True, align=PP_ALIGN.CENTER,
         spacing=1.0)
    hgt = lh(line, w - 0.3)
    text(s, I(x + 0.15), I(y + vh + 0.05), I(w - 0.3), I(hgt), line, size=PT["body"], color=INK,
         align=PP_ALIGN.CENTER, spacing=1.0)
    return vh + 0.05 + hgt


# ----------------------------------------------------------------------------- diagrams
NODE_STYLES = {"soft": (SOFT, LINE, NAVY, INK), "agent": (AGENT_FILL, WARM, AGENT_INK, INK),
               "system": (BLUE, None, WHITE, WHITE), "input": (INPUT, None, WHITE, WHITE),
               "out": (OUT_FILL, PLUS, OUT_INK, INK), "bad": (BAD_FILL, MINUS, MINUS, INK),
               "ref": (REF_FILL, BLUE, NAVY, INK), "white": (WHITE, LINE, NAVY, INK),
               "violet": (VIOLET_FILL, VIOLET, VIOLET, INK)}


ICON_SIZE = 0.42                                # an icon at the top of a node, in inches
CARD_ICON = 0.36                                # an icon beside a card heading, in inches


def node(s, x, y, w, h, head, body=None, style="soft", head_pt=None, body_pt=None, align=PP_ALIGN.CENTER,
         icon=None):
    """A diagram box with a bold heading and optional body lines, centred, in one of NODE_STYLES: soft (neutral),
    agent (an LLM step), system (a tool or engine), input, out (a result), bad (an error), ref (a reference),
    white, violet. `icon` (an icons.py name) sits at the top in the heading's colour and the text below it."""
    fill, line, hc, bc = NODE_STYLES[style]
    head_pt, body_pt = head_pt or PT["body"], body_pt or PT["small"] + 2
    rect(s, I(x), I(y), I(w), I(h), fill=fill, line=line, radius=True, line_w=1.5)
    body = [] if body is None else (body if isinstance(body, list) else [body])
    paras = ([[(head, hc, True)]] if head else []) + [[(b, bc, False)] for b in body]
    ty = y
    if icon:
        text_h = node_h(head, body, w, head_pt, body_pt) - 0.3
        top = y + max(0.12, (h - ICON_SIZE - 0.08 - text_h) / 2)
        globals()["icon"](s, icon, x + (w - ICON_SIZE) / 2, top, ICON_SIZE, color=hc, bg=fill)
        ty = top + ICON_SIZE + 0.04
        h = h - (ty - y)
    box = text(s, I(x + 0.1), I(ty), I(w - 0.2), I(h), paras, size=body_pt, align=align,
               anchor=MSO_ANCHOR.TOP if icon else MSO_ANCHOR.MIDDLE, spacing=1.0)
    for k, p in enumerate(box.text_frame.paragraphs):
        for r in p.runs:
            r.font.size = Pt(head_pt if (head and k == 0) else body_pt)
        p.space_after = Pt(3)
    return box


def node_h(head, body, w, head_pt=None, body_pt=None):
    """Height a node needs for its text at width w (inches)."""
    head_pt, body_pt = head_pt or PT["body"], body_pt or PT["small"] + 2
    body = [] if body is None else (body if isinstance(body, list) else [body])
    inner = w - 0.3
    return (0.3 + (lh(head, inner, head_pt, True) + 0.05 if head else 0) +
            sum(lh(b, inner, body_pt) + 0.05 for b in body))


def arrow(s, x1, y1, x2, y2, color=GREY):
    """A straight arrow between two points (inches)."""
    link(s, I(x1), I(y1), I(x2), I(y2), color=color)


def path(s, pts, color=GREY):
    """An elbow arrow through the points (inches), with its head at the last point."""
    for k in range(len(pts) - 1):
        (x1, y1), (x2, y2) = pts[k], pts[k + 1]
        link(s, I(x1), I(y1), I(x2), I(y2), head=k == len(pts) - 2, color=color)


def label(s, x, y, w, line, color=INK, size=None, align=PP_ALIGN.CENTER, bold=False, fill=WHITE):
    """A small label on a white plate (for arrows), centred vertically on y; returns its height."""
    size = size or PT["small"]
    hgt = lh(line, w - 0.1, size, bold) + 0.06
    if fill is not None:
        rect(s, I(x), I(y - hgt / 2), I(w), I(hgt), fill=fill)
    text(s, I(x), I(y - hgt / 2), I(w), I(hgt), line, size=size, color=color, bold=bold, align=align,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    return hgt


def chip(s, x, y, w, h, line, fill=WHITE, line_color=LINE, color=INK, size=None, bold=False):
    """A small rounded tile holding one value or name."""
    rect(s, I(x), I(y), I(w), I(h), fill=fill, line=line_color, radius=True, line_w=1.25)
    text(s, I(x), I(y), I(w), I(h), line, size=size or PT["small"], color=color, bold=bold, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)


def flow_row(s, y, h, items, gap=0.42, x0=None, width=None):
    """Nodes (head, body, style) or (head, body, style, icon) across a width, linked by arrows; returns the bottom
    (inches)."""
    x0 = x0 if x0 is not None else MX / EMU
    width = width if width is not None else CW / EMU
    n = len(items)
    w = (width - (n - 1) * gap) / n
    for k, item in enumerate(items):
        head, body, style = item[:3]
        x = x0 + k * (w + gap)
        node(s, x, y, w, h, head, body, style, icon=item[3] if len(item) > 3 else None)
        if k + 1 < n:
            arrow(s, x + w + 0.04, y + h / 2, x + w + gap - 0.04, y + h / 2)
    return y + h


def brace_label(s, x1, x2, y, line, color=GREY):
    """A thin bracket from x1 to x2 at y (inches) with a small label centred under it."""
    rect(s, I(x1), I(y), I(x2 - x1), I(0.025), fill=color)
    rect(s, I(x1), I(y - 0.08), I(0.025), I(0.1), fill=color)
    rect(s, I(x2 - 0.025), I(y - 0.08), I(0.025), I(0.1), fill=color)
    hgt = line_h(line, x2 - x1 + 1.0, PT["small"])
    text(s, I(x1 - 0.5), I(y + 0.05), I(x2 - x1 + 1.0), I(hgt), line, size=PT["small"], color=color,
         align=PP_ALIGN.CENTER, spacing=1.0)


def picture(s, file, x, y, max_w, max_h):
    """An image as large as the box (inches) allows, centred in it; returns (left, top, width, height)."""
    with Image.open(file) as im:
        ratio = im.width / im.height
    w = min(max_w, max_h * ratio)
    hgt = w / ratio
    left, top = x + (max_w - w) / 2, y + (max_h - hgt) / 2
    s.shapes.add_picture(str(file), I(left), I(top), I(w), I(hgt))
    return left, top, w, hgt


def equation(tex, size=22):
    """Render a mathtext formula to a transparent PNG once; returns (path, width in, height in) at natural size."""
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / f"eq_{hashlib.md5(f'{tex}|{size}'.encode()).hexdigest()[:12]}.png"
    if not p.exists():
        fig = plt.figure(figsize=(0.01, 0.01))
        fig.text(0, 0, f"${tex}$", fontsize=size, color="#2B2F36")
        fig.savefig(p, dpi=300, transparent=True, bbox_inches="tight", pad_inches=0.04)
        plt.close(fig)
    with Image.open(p) as im:
        return p, im.width / 300, im.height / 300


def formula(s, tex, x, y, w=None, size=22, align="left"):
    """Place a formula at (x, y) inches at natural size (centred in w when align is "center"); returns its height.
    One formula per line, so each fits the slide."""
    p, fw, fh = equation(tex, size)
    if w and fw > w:
        fh, fw = fh * w / fw, w
    dx = (w - fw) / 2 if (w and align == "center") else 0
    s.shapes.add_picture(str(p), I(x + dx), I(y), I(fw), I(fh))
    return fh


# ----------------------------------------------------------------------------- charts
def chart(s, name, x, y, w, h, draw):
    """Render `draw(fig)` with matplotlib at exactly w × h inches and 400 dpi, and place it at (x, y) inches without
    scaling, so it stays sharp in every viewer. Text uses Arial at the deck's sizes; labels pass through T() and
    numbers through D(), so each language gets its own PNG (CACHE/<name>-<lang>.png)."""
    import charts
    charts.use("slide", LANG)                   # charts.py forms (charts.axes(fig), charts.bars …) in slide sizes
    plt.rcParams.update({"font.family": "Arial", "font.size": PT["small"]})
    fig = plt.figure(figsize=(w, h), dpi=400)
    draw(fig)
    charts.fit(fig)                             # only plot areas made by charts.axes() are fitted
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / f"{name}-{LANG}.png"
    fig.savefig(p, dpi=400, transparent=True)
    plt.close(fig)
    s.shapes.add_picture(str(p), I(x), I(y), I(w), I(h))


def icon(s, name, x, y, size, color=BLUE, bg=WHITE):
    """An icon (icons.py) as a size × size inch picture at (x, y) inches; colours are RGBColor or hex. On a filled
    shape, pass the fill as `bg` so the icon's cut-outs match it."""
    import icons
    hexc = lambda c: c if isinstance(c, str) else f"#{c}"
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / f"icon-{name}-{hexc(color)[1:]}-{hexc(bg)[1:]}.png"
    if not p.exists():
        icons.icon_png(name, hexc(color), p, size_in=1.0, dpi=300, bg=hexc(bg))
    s.shapes.add_picture(str(p), I(x), I(y), I(size), I(size))


def clean_axes(ax, grid="y"):
    """Recessive axes: no top, right or left spine, a light baseline, muted ticks, an optional light grid."""
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(HEX(C_GRID))
    ax.tick_params(length=0, colors=HEX(C_MUTED), labelsize=PT["small"])
    if grid:
        ax.grid(axis=grid, color=HEX(C_GRID), lw=0.8)
        ax.set_axisbelow(True)


# ----------------------------------------------------------------------------- deck
def build_deck(lang, slides, out, footer_en, cache=None, before=None):
    """Build one language of a deck: every slide function in order, then tighten each text box to its text, turn the
    page numbers into fields, save to `out`, set the theme fonts to Arial and list English strings that the deck's
    VI module lacks. `before()` runs after the language is set (e.g. to fill the kicker labels)."""
    global LANG, FOOTER, CACHE
    LANG = lang
    if cache is not None:
        CACHE = Path(cache)
    MISSING.clear()
    FOOTER = T(footer_en) if footer_en else ""
    if before:
        before()
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    for make in slides:
        make(prs)
    for slide in prs.slides:
        tighten(slide)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    number_fields(prs)
    prs.save(str(out))
    arial_theme(out)
    print(f"[{lang}] {len(prs.slides)} slides → {out}")
    if MISSING:
        print(f"[{lang}] {len(dict.fromkeys(MISSING))} strings without a Vietnamese form:")
        for m in dict.fromkeys(MISSING):
            print("   ", m[:110])
    return prs


# ----------------------------------------------------------------------------- command line
def _load_deck(script):
    path = Path(script).resolve()
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _deck_strings(deck_path, everything):
    """English strings of a deck in slide order: those its VI module lacks, or all of them; returns (strings, deck,
    the slidekit module the deck uses)."""
    import tempfile
    import slidekit as kit                      # the module the deck imports, not this __main__ copy
    deck = _load_deck(deck_path)
    if everything:
        kit._VI["override"] = {}
    import contextlib
    import io
    with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
        deck.OUT = {"en": Path(tmp) / "en.pptx", "vi": Path(tmp) / "vi.pptx"}
        deck.build("vi")
    strings = list(dict.fromkeys(kit.MISSING))
    kit._VI["override"] = None
    return strings, deck, kit


def cmd_strings(args):
    """English strings of a deck that its Vietnamese module lacks (all of them with --all), in slide order."""
    strings, _, _ = _deck_strings(args.deck, args.all)
    if args.out:
        Path(args.out).write_text(json.dumps(strings, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"{len(strings)} strings → {args.out}")
    else:
        print(json.dumps(strings, ensure_ascii=False, indent=1))


def _vi_module_path(kit):
    """File of the deck's VI module (the one named by use_strings)."""
    return Path(importlib.import_module(kit._VI["module"]).__file__)


def write_vi_module(path, table, docstring):
    """Write a VI module in the canonical form: docstring, then one key line and one value line per entry."""
    lines = [f'"""{docstring}"""', "", "VI = {"]
    for k, v in table.items():
        lines += [f"    {k!r}:", f"        {v!r},"]
    lines.append("}")
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_sync(args):
    """Compare a deck's English strings with the keys of its VI module: missing keys, unused keys, and for each
    English string that changed, the old key it most resembles. --write renames those keys (the values stay and
    need a review against the new English) and, with --prune, drops keys that no slide uses."""
    import ast
    import difflib
    english, _, kit = _deck_strings(args.deck, True)
    path = _vi_module_path(kit)
    table = dict(importlib.import_module(kit._VI["module"]).VI)
    missing = [e for e in english if e not in table]
    unused = [k for k in table if k not in set(english)]
    def similar(a, b):
        """Same string reworded: close in characters and sharing at least half of the shorter one's words; a
        short label (three words or fewer) must match much more closely, since short strings look alike."""
        ratio = difflib.SequenceMatcher(None, a, b).ratio()
        wa, wb = set(a.lower().split()), set(b.lower().split())
        shared = len(wa & wb) / max(1, min(len(wa), len(wb)))
        short = min(len(wa), len(wb)) <= 3
        return ratio >= (max(args.threshold, 0.8) if short else args.threshold) and shared >= 0.5, ratio

    pairs, free = [], list(unused)
    for m in missing:
        best = max(free, key=lambda u: similar(m, u)[1], default=None)
        if best is not None and similar(m, best)[0]:
            pairs.append((best, m))
            free.remove(best)
    print(f"{path.name}: {len(english)} English strings, {len(table)} keys; {len(missing)} missing, "
          f"{len(unused)} unused, {len(pairs)} renamed English strings")
    for old, new in pairs:
        print(f"  RENAME  {old[:70]!r}\n      →   {new[:70]!r}")
    for m in [m for m in missing if m not in {n for _, n in pairs}]:
        print(f"  MISSING {m[:90]!r}")
    for u in free:
        print(f"  UNUSED  {u[:90]!r}")
    if args.write and (pairs or (args.prune and free)):
        renames = dict(pairs)
        out = {}
        for k, v in table.items():
            if k in renames:
                out[renames[k]] = v
            elif not (args.prune and k in free):
                out[k] = v
        doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf-8"))) or "Vietnamese strings of a deck."
        write_vi_module(path, out, doc)
        print(f"wrote {path}: {len(pairs)} keys renamed" + (f", {len(free)} dropped" if args.prune else "") +
              "; review each renamed value against its new English")


def _parts(pptx):
    import hashlib as _h
    z = zipfile.ZipFile(pptx)
    out = {}
    for n in z.namelist():
        d = z.read(n)
        if n.endswith(".xml") or n.endswith(".rels"):
            d = re.sub(rb'id="\{[0-9A-F-]+\}"', b'id="{X}"', d)      # slide-number fields get a fresh id each build
        out[n] = _h.md5(d).hexdigest()
    return out


def cmd_diff(args):
    """Compare two built decks part by part (slides, notes, media), ignoring the ids of slide-number fields; exit 1
    when any part differs. Use it to prove that a refactor of a deck script changes nothing."""
    a, b = _parts(args.a), _parts(args.b)
    diff = [n for n in sorted(set(a) | set(b)) if a.get(n) != b.get(n)]
    print(f"{len(a)} parts, {len(diff)} differ")
    for n in diff:
        print("  ", n)
    sys.exit(1 if diff else 0)


def cmd_prompt(args):
    """Print the translator's or the reviewer's prompt for a deck, filled from the deck, the task and the language
    pack (templates/prompts/deck-translate.md, deck-review.md). It writes the files the prompt names into the scratch
    folder: the strings still to translate, or the built deck's text for the reviewer's first pass."""
    import tomllib
    skill = Path(__file__).resolve().parents[1]
    pack = tomllib.loads((skill / "languages" / args.lang / "pack.toml").read_text(encoding="utf-8"))
    tasks = tomllib.loads(CONFIG.read_text(encoding="utf-8")) if CONFIG.exists() else {}
    scratch = Path(args.scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    strings, deck, kit = _deck_strings(args.deck, False)
    title = getattr(deck, "DECK_TITLE", None) or Path(args.deck).stem      # a deck names itself in DECK_TITLE
    fields = dict(python=(f"./{Path(PYTHON).relative_to(ROOT)}" if Path(PYTHON).is_relative_to(ROOT) else PYTHON),
                  skill=shown(skill),
                  lang=args.lang, LANG=args.lang.upper(), lang_name=pack.get("name_en", pack.get("name", args.lang)), task=args.task,
                  deck=args.deck, deck_title=title, root=ROOT, scratch=scratch, suffix=pack.get("suffix", ""),
                  vi_module=shown(_vi_module_path(kit)), report=tasks.get(args.task, {}).get("report", ""),
                  voice_line=pack.get("slides", {}).get(f"voice_{args.voice}", ""), review_log=args.log or "",
                  log_title=args.log_title, focus=(f"\n**Focus of this review:** {args.focus}\n" if args.focus else ""),
                  strings_file="", text_file="")
    if args.kind == "translate":
        f = scratch / "strings.json"
        f.write_text(json.dumps(strings, ensure_ascii=False, indent=1), encoding="utf-8")
        fields["strings_file"] = f
    else:
        deck.OUT = {"en": scratch / f"Slides_EN.pptx", args.lang: scratch / f"Slides_{args.lang.upper()}.pptx"}
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):       # the prompt is the only output
            deck.build(args.lang)
        f = scratch / "deck_text.md"
        f.write_text(deck_text(deck.OUT[args.lang]), encoding="utf-8")
        fields["text_file"] = f
    if args.kind == "review":                                 # term drift, measured, goes to the reviewer as evidence
        import glossary
        from common import language_packs
        lp = language_packs()[args.lang]
        rows = glossary.load(lp, glossary.names_of(tasks.get(args.task, {}), args.lang))
        source, target = glossary.deliverable_text(lp, None, str(_vi_module_path(kit)))
        drift = glossary.coverage(rows, source, target)
        if drift:
            lines = "".join(f"\n- '{d['row']['en']}': {d['en']}× in the English, the glossary form '{d['row']['vi']}' "
                            f"{d['vi']}× in the translation" for d in drift)
            fields["focus"] += ("\n**Term drift measured by `glossary.py coverage`** (each concept likely travels under "
                                f"several names; give it the glossary's one term everywhere):{lines}\n")
    template = (skill / "templates" / "prompts" / f"deck-{args.kind}.md").read_text(encoding="utf-8")
    print(template.format(**fields))


def deck_text(pptx, notes=True):
    """Every slide's text, table rows and (unless notes=False) speaker notes in order, as plain text. Without the
    notes it is what a reader of the deck sees, the input of the slide-only reading pass (slides.md section 2)."""
    out = []
    for n, slide in enumerate(Presentation(str(pptx)).slides, 1):
        out.append(f"\n=== Slide {n}")
        for sh in walk(slide.shapes):
            if sh.has_text_frame:
                out += [p.text for p in sh.text_frame.paragraphs if p.text.strip()]
            if sh.has_table:
                out += [" | ".join(c.text for c in r.cells) for r in sh.table.rows]
        if notes:
            out.append("[Notes] " + (slide.notes_slide.notes_text_frame.text if slide.has_notes_slide else ""))
    return "\n".join(out)


def cmd_text(args):
    txt = deck_text(args.pptx, notes=not args.slides_only)
    if args.out:
        Path(args.out).write_text(txt, encoding="utf-8")
        print(f"{args.pptx} → {args.out}")
    else:
        print(txt)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("strings", help="English strings a deck's Vietnamese module lacks (or all with --all)")
    p.add_argument("deck", help="deck script, e.g. build_slides_taskN.py")
    p.add_argument("--all", action="store_true", help="every English string, also those already translated")
    p.add_argument("--out", help="JSON file to write (default: print)")
    p.set_defaults(func=cmd_strings)
    p = sub.add_parser("text", help="slide text and notes of a built deck, for review")
    p.add_argument("pptx")
    p.add_argument("--slides-only", action="store_true", help="leave out the notes: what a reader of the deck sees")
    p.add_argument("--out", help="file to write (default: print)")
    p.set_defaults(func=cmd_text)
    p = sub.add_parser("sync", help="missing, unused and renamed keys of a deck's VI module after English edits")
    p.add_argument("deck")
    p.add_argument("--write", action="store_true", help="rename keys whose English changed (values kept for review)")
    p.add_argument("--prune", action="store_true", help="with --write: drop keys that no slide uses")
    p.add_argument("--threshold", type=float, default=0.6, help="similarity that pairs an old key with new English")
    p.set_defaults(func=cmd_sync)
    p = sub.add_parser("diff", help="compare two built decks part by part (exit 1 when they differ)")
    p.add_argument("a")
    p.add_argument("b")
    p.set_defaults(func=cmd_diff)
    p = sub.add_parser("prompt", help="the translator's or reviewer's prompt for a deck, filled from deck, task, pack")
    p.add_argument("kind", choices=["translate", "review"])
    p.add_argument("deck")
    p.add_argument("--task", required=True)
    p.add_argument("--voice", choices=["group", "solo"], required=True, help="who speaks in the notes")
    p.add_argument("--scratch", required=True, help="folder for the strings or deck text the prompt names")
    p.add_argument("--lang", default="vi")
    p.add_argument("--log", help="review log to append to (review prompts)")
    p.add_argument("--log-title", default="Native review", help="heading of the reviewer's log section")
    p.add_argument("--focus", help="one paragraph on what this review concentrates on")
    p.set_defaults(func=cmd_prompt)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
