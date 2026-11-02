"""Content-driven layout for slide decks: measure text, size each box to it, then place boxes by arithmetic.

All lengths are in inches. The rules the decks follow:

  • Size from content. A box is as wide as its longest line (capped by a maximum, beyond which the text wraps)
    and as tall as its wrapped lines, plus fixed padding. Text is measured with the deck's font (Arial metrics).
  • Peers share an axis. Boxes in a flow row are centred on one horizontal axis, so the arrows between them are
    straight; boxes in a column are centred on one vertical axis.
  • Peers of a grid share a size. Cards that are read as a set (statistics, timeline steps) take the width of
    their column and the height of the tallest, so their edges line up.
  • Space is shared out evenly. A row either spreads across its span with equal gaps, or sits centred with a fixed
    gap; a group is centred in the area it is given, horizontally and vertically.
  • Parents follow children. A group box spans exactly the boxes it groups; a parent is centred over its children;
    a label sits at the midpoint of the gap it names.

Used by slidekit.py; tighten() runs over every slide after it is built. Arial is looked up in the font folders that
check_slides.py and preview_slides.py use, so all three measure text alike.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

from PIL import ImageFont

FONT_DIRS = ["/System/Library/Fonts/Supplemental", "/Library/Fonts", "/usr/share/fonts/truetype/msttcorefonts",
             "C:/Windows/Fonts"]

EMU = 914400
LINE = 1.2                    # PowerPoint line height in em for single spacing
FRAME = 0.12                  # text-frame margins plus a small slack, so PowerPoint never wraps earlier than measured
_FONTS: dict = {}


def walk(shapes):
    """Every shape of a slide, with the shapes inside groups instead of the groups (a native diagram is drawn as
    one group). The kit's groups map child coordinates one to one, so child positions are slide positions."""
    for sh in shapes:
        if sh.shape_type == 6:                          # MSO_SHAPE_TYPE.GROUP
            yield from walk(sh.shapes)
        else:
            yield sh


def font_path(bold: bool = False) -> str:
    """Path of Arial (Bold) in the first font folder that holds it."""
    name = "Arial Bold.ttf" if bold else "Arial.ttf"
    for d in FONT_DIRS:
        if os.path.exists(f"{d}/{name}"):
            return f"{d}/{name}"
    raise FileNotFoundError(f"{name} not found in {FONT_DIRS}")


def font(pt: float, bold: bool = False):
    key = (round(pt * 10), bold)
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(font_path(bold), key[0])
    return _FONTS[key]


def width(text: str, pt: float, bold: bool = False) -> float:
    """Printed width of one line, in inches."""
    return font(pt, bold).getlength(text) / 720


WRAP_GUARD = 0.97              # metric drift between this measurement, the checker and PowerPoint


def wrap(text: str, pt: float, bold: bool, max_w: float) -> list[str]:
    """Greedy word wrap to `max_w` inches; explicit newlines are kept. A line counts as full at WRAP_GUARD of the
    width, so a line that only just fits in this measurement is wrapped here as PowerPoint may wrap it."""
    out = []
    max_w *= WRAP_GUARD
    for para in text.split("\n"):
        line = ""
        for word in para.split():
            trial = f"{line} {word}".strip()
            if line and width(trial, pt, bold) > max_w:
                out.append(line)
                line = word
            else:
                line = trial
        out.append(line)
    return out


@dataclass
class Para:
    text: str
    pt: float
    bold: bool = False
    color: object = None
    spacing: float = 1.0


@dataclass
class Box:
    x: float
    y: float
    w: float
    h: float

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def cy(self):
        return self.y + self.h / 2

    @property
    def right(self):
        return self.x + self.w

    @property
    def bottom(self):
        return self.y + self.h

    def mid(self, side):
        return {"n": (self.cx, self.y), "s": (self.cx, self.bottom), "w": (self.x, self.cy), "e": (self.right, self.cy)}[side]

    def emu(self):
        return [int(v * EMU) for v in (self.x, self.y, self.w, self.h)]


def measure(paras: list[Para], max_w: float, pad_x: float = 0.2, pad_y: float = 0.16, min_w: float = 0.0,
            gap: float = 0.06) -> tuple[float, float]:
    """(width, height) of a box holding the paragraphs, wrapped within `max_w`; `gap` separates a heading from its body."""
    inner = max_w - 2 * pad_x - FRAME
    widest, h, prev = 0.0, 0.0, None
    for p in paras:
        if not p.text:
            continue
        lines = wrap(p.text, p.pt, p.bold, inner)
        widest = max(widest, max(width(line, p.pt, p.bold) for line in lines))
        h += len(lines) * p.pt * LINE * p.spacing / 72 + (gap if prev is not None and prev != p.bold else 0)
        prev = p.bold
    return max(min_w, min(max_w, widest + 2 * pad_x + FRAME)), h + 2 * pad_y


def text_height(paras: list[Para], inner_w: float, gap: float = 0.06) -> float:
    """Height of the paragraphs wrapped to an inner width (no padding)."""
    h = 0.0
    for k, p in enumerate(paras):
        if p.text:
            h += len(wrap(p.text, p.pt, p.bold, inner_w - FRAME)) * p.pt * LINE * p.spacing / 72 + (gap if k else 0)
    return h


def row(sizes, left: float, right: float, cy: float, gap: float | None = None) -> list[Box]:
    """Boxes of the given (w, h) on one horizontal axis `cy`.

    gap=None spreads them across [left, right] with equal gaps (edge boxes touch the ends);
    a number places them with that gap, centred between left and right."""
    total = sum(w for w, _ in sizes)
    n = len(sizes)
    if gap is None:
        gap = (right - left - total) / (n - 1) if n > 1 else 0
        x = left if n > 1 else (left + right - total) / 2
    else:
        x = (left + right - total - gap * (n - 1)) / 2
    boxes = []
    for w, h in sizes:
        boxes.append(Box(x, cy - h / 2, w, h))
        x += w + gap
    return boxes


def column(sizes, top: float, bottom: float, cx: float, gap: float | None = None) -> list[Box]:
    """Boxes of the given (w, h) on one vertical axis `cx`, spread or centred like row()."""
    total = sum(h for _, h in sizes)
    n = len(sizes)
    if gap is None:
        gap = (bottom - top - total) / (n - 1) if n > 1 else 0
        y = top if n > 1 else (top + bottom - total) / 2
    else:
        y = (top + bottom - total - gap * (n - 1)) / 2
    boxes = []
    for w, h in sizes:
        boxes.append(Box(cx - w / 2, y, w, h))
        y += h + gap
    return boxes


def centred(length: float, start: float, end: float) -> float:
    """Start coordinate that centres `length` in [start, end]."""
    return start + (end - start - length) / 2


def above(target: Box, size, gap: float) -> Box:
    w, h = size
    return Box(target.cx - w / 2, target.y - gap - h, w, h)


def below(target: Box, size, gap: float) -> Box:
    w, h = size
    return Box(target.cx - w / 2, target.bottom + gap, w, h)


def separate(boxes: list[Box], min_gap: float, left: float, right: float) -> list[Box]:
    """Shift boxes of one row apart so neighbours keep `min_gap`, keeping the row's centre and its bounds."""
    boxes = sorted(boxes, key=lambda b: b.cx)
    for _ in range(3):
        for a, b in zip(boxes, boxes[1:]):
            overlap = a.right + min_gap - b.x
            if overlap > 0:
                a.x -= overlap / 2
                b.x += overlap / 2
        if boxes[0].x < left:
            d = left - boxes[0].x
            for b in boxes:
                b.x += d
        if boxes[-1].right > right:
            d = boxes[-1].right - right
            for b in boxes:
                b.x -= d
    return boxes


def hull(boxes: list[Box], pad: float = 0.0) -> Box:
    """The box that just contains the given boxes."""
    x0, y0 = min(b.x for b in boxes) - pad, min(b.y for b in boxes) - pad
    x1, y1 = max(b.right for b in boxes) + pad, max(b.bottom for b in boxes) + pad
    return Box(x0, y0, x1 - x0, y1 - y0)


def shift(boxes: list[Box], dx: float = 0.0, dy: float = 0.0) -> list[Box]:
    for b in boxes:
        b.x += dx
        b.y += dy
    return boxes


def tighten(slide, slack: float = 0.08, slack_ratio: float = 0.02) -> int:
    """Shrink every text box of a slide to the text it holds, keeping the text where it was.

    A text box keeps its alignment point: centred text keeps its centre, right-aligned text its right edge, left-aligned
    text its left edge; middle-anchored text keeps its vertical centre, bottom-anchored text its bottom edge. Lines are
    measured with the same wrapping PowerPoint applies at the box's current width, so no line breaks move. Returns the
    number of boxes resized."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
    changed = 0
    for sh in slide.shapes:                         # grouped diagrams (scene.py) are already sized exactly
        if sh.shape_type != MSO_SHAPE_TYPE.TEXT_BOX or not sh.text_frame.text.strip():
            continue
        tf = sh.text_frame
        ml = (tf.margin_left if tf.margin_left is not None else 91440) / EMU
        mr = (tf.margin_right if tf.margin_right is not None else 91440) / EMU
        mt = (tf.margin_top if tf.margin_top is not None else 45720) / EMU
        mb = (tf.margin_bottom if tf.margin_bottom is not None else 45720) / EMU
        avail = sh.width / EMU - ml - mr
        widest, height = 0.0, 0.0
        paras = tf.paragraphs
        for k, p in enumerate(paras):
            runs = [r for r in p.runs if r.text]
            pt = max((r.font.size.pt for r in runs if r.font.size), default=18)
            bold = any(r.font.bold for r in runs)
            txt = "".join(r.text for r in runs)
            if not txt:
                lines = [""]
            elif "\n" not in txt and width(txt, pt, bold) <= avail:
                lines = [txt]           # one line, measured as written (repeated spaces included)
            else:
                lines = wrap(txt, pt, bold, avail)
            widest = max([widest] + [width(line, pt, bold) for line in lines])
            spacing = p.line_spacing if isinstance(p.line_spacing, float) else 1.0
            height += len(lines) * pt * LINE * spacing / 72
            if p.space_before is not None and k:
                height += p.space_before.pt / 72
            if p.space_after is not None and k < len(paras) - 1:
                height += p.space_after.pt / 72
        new_w = min(sh.width / EMU, widest * (1 + slack_ratio) + ml + mr + slack)   # a guard against metric drift
        if height + mt + mb + 0.02 > sh.height / EMU:
            new_w = sh.width / EMU      # the measured text is taller than its box: narrowing would add a wrapped line
        new_h = min(sh.height / EMU, height + mt + mb + 0.02)
        x, y, w, h = sh.left / EMU, sh.top / EMU, sh.width / EMU, sh.height / EMU
        align = paras[0].alignment
        if align == PP_ALIGN.CENTER:
            x = x + (w - new_w) / 2
        elif align == PP_ALIGN.RIGHT:
            x = x + w - new_w
        anchor = tf.vertical_anchor
        if anchor == MSO_ANCHOR.MIDDLE:
            y = y + (h - new_h) / 2
        elif anchor == MSO_ANCHOR.BOTTOM:
            y = y + h - new_h
        sh.left, sh.top, sh.width, sh.height = (int(v * EMU) for v in (x, y, new_w, new_h))
        changed += 1
    return changed
