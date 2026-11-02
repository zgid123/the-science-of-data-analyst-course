"""Render an approximate PNG preview of every slide of a .pptx deck, without PowerPoint or LibreOffice.

Usage: python .claude/skills/build-report/scripts/preview_slides.py DECK.pptx [--out DIR] [--slides 3,7-9]
Output: DIR/slide-NN.png (default DIR: build/.cache/slide-preview/<deck name>/), plus contact.png with all slides.

The preview draws what layout review needs: filled and outlined shapes, connectors, pictures, column charts, tables, and text wrapped with
the font's metrics (Arial by default), aligned and anchored as in the deck. It is a layout aid for spotting
overlaps, overflow and crowded slides; exact rendering stays with the presentation program.
"""

import argparse
import re

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE, MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from check_slides import FONT_DIRS
from common import ROOT
from slide_measure import walk

SCALE = 96 / 914400            # pixels per EMU at 96 dpi
PT = 96 / 72                   # pixels per point
_fonts = {}



def text_runs(p):
    """A paragraph's text runs including fields (a slide number is an a:fld), each readable as a run."""
    from pptx.oxml.ns import qn
    from pptx.text.text import _Run
    return [_Run(el, p) for el in p._p if el.tag in (qn("a:r"), qn("a:fld"))]

def font(bold, size_pt, mono=False):
    key = (bold, size_pt, mono)
    if key not in _fonts:
        name = ("Courier New Bold.ttf" if bold else "Courier New.ttf") if mono else ("Arial Bold.ttf" if bold else "Arial.ttf")
        for d in FONT_DIRS:
            try:
                _fonts[key] = ImageFont.truetype(f"{d}/{name}", max(1, int(size_pt * PT)))
                break
            except OSError:
                continue
        else:
            _fonts[key] = ImageFont.load_default()
    return _fonts[key]


def rgb(fill_or_color, default=None):
    try:
        return "#" + str(fill_or_color.fore_color.rgb if hasattr(fill_or_color, "fore_color") else fill_or_color.rgb)
    except (AttributeError, TypeError, ValueError):
        return default


def draw_text(draw, frame, box, default_size=18):
    """Wrap and draw a text frame inside box = (x0, y0, x1, y1), honouring alignment, anchor and margins."""
    x0, y0, x1, y1 = box
    m = lambda v, d: (d if v is None else v) * SCALE          # noqa: E731  (a margin of 0 is a real 0)
    ml, mr = m(frame.margin_left, 91440), m(frame.margin_right, 91440)
    mt, mb = m(frame.margin_top, 45720), m(frame.margin_bottom, 45720)
    width = max(1, x1 - x0 - ml - mr)
    lines, paragraphs = [], frame.paragraphs
    nowrap = frame.word_wrap is False
    for i, p in enumerate(paragraphs):
        runs = [r for r in text_runs(p) if r.text]
        size = max((r.font.size.pt for r in runs if r.font.size), default=default_size)
        spacing = p.line_spacing if isinstance(p.line_spacing, float) else (
            p.line_spacing.pt / size if p.line_spacing is not None and size else 1.0)
        step = size * PT * (1.2 if spacing == 1.0 else 1.0) * spacing   # exact spacing already holds the leading
        line, line_w = [], 0.0
        breaks = {id(r._r) for r in runs if r._r.getprevious() is not None
                  and r._r.getprevious().tag.endswith("}br")}          # a run after a line break starts a line
        for r in runs or [None]:
            if r is None:
                break
            if id(r._r) in breaks and line:
                lines.append((line, line_w, step, p.alignment))
                line, line_w = [], 0.0
            f = font(bool(r.font.bold), r.font.size.pt if r.font.size else size, r.font.name == "Courier New")
            color = rgb(r.font.color, "#000000") if r.font.color and r.font.color.type is not None else "#000000"
            for word in re.split(r"(\s+)", r.text):
                if not word:
                    continue
                w = f.getlength(word)
                if not nowrap and line_w + w > width and line and word.strip():
                    lines.append((line, line_w, step, p.alignment))
                    line, line_w = [], 0.0
                    if not word.strip():
                        continue
                line.append((word, f, color))
                line_w += w
        lines.append((line, line_w, step, p.alignment))
        if i < len(paragraphs) - 1 and p.space_after is not None:
            lines.append(([], 0, p.space_after.pt * PT, None))
    total = sum(h for *_, h, _ in lines)
    anchor = frame.vertical_anchor
    y = y0 + mt if anchor in (None, MSO_ANCHOR.TOP) else (
        (y0 + y1 - total) / 2 if anchor == MSO_ANCHOR.MIDDLE else y1 - mb - total)
    for line, line_w, h, align in lines:
        x = x0 + ml + (width - line_w if align == PP_ALIGN.RIGHT else (width - line_w) / 2 if align == PP_ALIGN.CENTER else 0)
        for word, f, color in line:
            draw.text((x, y + h * 0.1), word, font=f, fill=color)
            x += f.getlength(word)
        y += h
    if total > (y1 - y0) + 6:
        draw.rectangle(box, outline="#FF00FF", width=2)          # overflow marker


def draw_path(draw, shape, box, color):
    """A freeform's path (moveTo / lnTo points in its own coordinates) scaled to its box."""
    import math
    from pptx.oxml.ns import qn
    for path in shape._element.iter(qn("a:path")):
        pw, ph = int(path.get("w", 1)) or 1, int(path.get("h", 1)) or 1
        pts = [(box[0] + int(pt.get("x")) / pw * (box[2] - box[0]), box[1] + int(pt.get("y")) / ph * (box[3] - box[1]))
               for pt in path.iter(qn("a:pt"))]
        if len(pts) > 1:
            width = max(1, round(shape.line.width.pt * 1.4)) if shape.line.width else 2
            if path.find(qn("a:close")) is not None:            # a closed shape (a diamond, a tab): fill it
                fill = rgb(shape.fill) if shape.fill.type == 1 else None
                draw.polygon(pts, fill=fill, outline=color if shape.line.fill.type == 1 else None)
                continue
            draw.line(pts, fill=color, width=width)
            if "tailEnd" in shape.line._get_or_add_ln().xml:
                (x1, y1), (x2, y2) = pts[-2], pts[-1]
                a = math.atan2(y2 - y1, x2 - x1)
                draw.polygon([(x2, y2), (x2 - 9 * math.cos(a - 0.45), y2 - 9 * math.sin(a - 0.45)),
                              (x2 - 9 * math.cos(a + 0.45), y2 - 9 * math.sin(a + 0.45))], fill=color)


def chart_image(chart, w_px, h_px):
    """A native chart drawn with the kit's chart forms from its own data and series colours, for review."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import charts as ch
    from pptx.enum.chart import XL_CHART_TYPE as K
    try:
        plot = chart.plots[0]
        kind = chart.chart_type
        dpi = 100
        fig = plt.figure(figsize=(max(w_px, 10) / dpi, max(h_px, 10) / dpi), dpi=dpi)
        ch.use("slide")
        ax = ch.axes(fig)
        def col(s):
            try:
                return "#" + str(s.format.fill.fore_color.rgb)
            except (AttributeError, TypeError):
                return None
        cats = [str(c) for c in plot.categories] if kind != K.XY_SCATTER else []
        series = {s.name: [v if v is not None else 0 for v in s.values] for s in plot.series}
        colors = [col(s) for s in plot.series]
        colors = colors if all(colors) else None
        if kind in (K.COLUMN_CLUSTERED, K.BAR_CLUSTERED):
            ch.bars(ax, cats, series, horizontal=kind == K.BAR_CLUSTERED, colors=colors)
        elif kind in (K.BAR_STACKED_100, K.COLUMN_STACKED_100, K.BAR_STACKED, K.COLUMN_STACKED):
            ch.stacked(ax, cats, series, horizontal=kind in (K.BAR_STACKED_100, K.BAR_STACKED), colors=colors,
                       percent=kind in (K.BAR_STACKED_100, K.COLUMN_STACKED_100))
        elif kind in (K.LINE, K.LINE_MARKERS):
            lc = [("#" + str(s.format.line.color.rgb)) for s in plot.series]
            ch.lines(ax, cats, series, colors=lc)
        elif kind == K.DOUGHNUT:
            s = plot.series[0]
            fills = []
            for k in range(len(cats)):
                try:
                    fills.append("#" + str(s.points[k].format.fill.fore_color.rgb))
                except (AttributeError, TypeError):
                    fills.append(None)
            ax.pie(list(s.values), colors=fills if all(fills) else None, wedgeprops=dict(width=0.45, edgecolor="white"),
                   startangle=90, counterclock=False)
            ax.set_aspect("equal")
        else:
            plt.close(fig)
            return None
        ch.fit(fig)
        from io import BytesIO
        buf = BytesIO()
        fig.savefig(buf, dpi=dpi, transparent=True)
        plt.close(fig)
        buf.seek(0)
        return Image.open(buf).convert("RGBA").resize((max(1, w_px), max(1, h_px)))
    except Exception as e:                                     # a preview must not stop on an unusual chart
        print(f"preview: chart not drawn ({e})")
        return None


def render(slide, size):
    img = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(img)
    for shape in walk(slide.shapes):
        box = (shape.left * SCALE, shape.top * SCALE, (shape.left + shape.width) * SCALE, (shape.top + shape.height) * SCALE)
        if hasattr(shape, "begin_x"):                               # connector: a line, with an arrowhead if set
            x1, y1, x2, y2 = (v * SCALE for v in (shape.begin_x, shape.begin_y, shape.end_x, shape.end_y))
            color = rgb(shape.line.color, "#6B727C")
            draw.line((x1, y1, x2, y2), fill=color, width=2)
            if "tailEnd" in shape.line._get_or_add_ln().xml:
                import math
                a = math.atan2(y2 - y1, x2 - x1)
                draw.polygon([(x2, y2), (x2 - 9 * math.cos(a - 0.45), y2 - 9 * math.sin(a - 0.45)),
                              (x2 - 9 * math.cos(a + 0.45), y2 - 9 * math.sin(a + 0.45))], fill=color)
            continue
        if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
            from io import BytesIO
            pic = Image.open(BytesIO(shape.image.blob)).convert("RGBA").resize((max(1, int(box[2] - box[0])), max(1, int(box[3] - box[1]))))
            img.paste(pic, (int(box[0]), int(box[1])), pic)          # transparent pixels keep what lies below
            continue
        if getattr(shape, "has_chart", False) and shape.has_chart:   # a native chart, drawn with charts.py
            pic = chart_image(shape.chart, int(box[2] - box[0]), int(box[3] - box[1]))
            if pic is not None:
                img.paste(pic, (int(box[0]), int(box[1])), pic)
            continue
        if shape.has_table:
            tbl, y = shape.table, box[1]
            for row in tbl.rows:
                x, h = box[0], row.height * SCALE
                for col, cell in zip(tbl.columns, row.cells):
                    w = col.width * SCALE
                    draw.rectangle((x, y, x + w, y + h), fill=rgb(cell.fill, "#FFFFFF"), outline="#D5DAE1")
                    draw_text(draw, cell.text_frame, (x, y, x + w, y + h), 14)
                    x += w
                y += h
            continue
        fill = rgb(shape.fill) if getattr(shape, "fill", None) is not None and shape.fill.type == 1 else None
        line = rgb(shape.line.color) if getattr(shape, "line", None) is not None and shape.line.fill.type == 1 else None
        if shape.shape_type == MSO_SHAPE_TYPE.FREEFORM:            # a path: trace its points, arrowhead if set
            draw_path(draw, shape, box, line or "#6B727C")
            if shape.has_text_frame and shape.text_frame.text.strip():
                draw_text(draw, shape.text_frame, box)
            continue
        kind = getattr(shape, "auto_shape_type", None) if shape.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE else None
        if fill or line:
            if kind == MSO_SHAPE.OVAL:
                draw.ellipse(box, fill=fill, outline=line, width=1)
            elif kind == MSO_SHAPE.RECTANGLE:
                draw.rectangle(box, fill=fill, outline=line, width=1)
            else:
                draw.rounded_rectangle(box, radius=8, fill=fill, outline=line, width=1)
        if shape.has_text_frame and shape.text_frame.text.strip():
            draw_text(draw, shape.text_frame, box)
    return img


def parse_range(spec, n):
    if not spec:
        return list(range(1, n + 1))
    out = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    return [i for i in out if 1 <= i <= n]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("--out")
    ap.add_argument("--slides", help="slide numbers, e.g. 3,7-9 (default: all)")
    args = ap.parse_args()
    deck = ROOT / args.deck
    prs = Presentation(str(deck))
    out = ROOT / (args.out or f"build/.cache/slide-preview/{deck.stem}")
    out.mkdir(parents=True, exist_ok=True)
    size = (int(prs.slide_width * SCALE), int(prs.slide_height * SCALE))
    pages = []
    for n in parse_range(args.slides, len(prs.slides)):
        img = render(prs.slides[n - 1], size)
        img.save(out / f"slide-{n:02d}.png")
        pages.append(img)
    cols = 3
    thumb = (size[0] // 3, size[1] // 3)
    sheet = Image.new("RGB", (thumb[0] * cols + 10 * (cols + 1), (thumb[1] + 10) * ((len(pages) + cols - 1) // cols) + 10), "#888888")
    for i, img in enumerate(pages):
        sheet.paste(img.resize(thumb), (10 + (i % cols) * (thumb[0] + 10), 10 + (i // cols) * (thumb[1] + 10)))
    sheet.save(out / "contact.png")
    shown = out.relative_to(ROOT) if out.is_relative_to(ROOT) else out      # an --out folder may lie outside the project
    print(f"{len(pages)} slides → {shown}/ (slide-NN.png, contact.png)")


if __name__ == "__main__":
    main()
