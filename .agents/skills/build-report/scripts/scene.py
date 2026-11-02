"""One drawing, two outputs: a Scene describes a diagram once in inches, and renders it either as an image
(matplotlib: a report figure or a picture on a slide) or as native PowerPoint shapes that stay editable and whose
text the slide checks and translators see.

    sc = Scene(6.3, 2.0, medium="report")       # medium sets the type sizes: report (print) or slide
    sc.rect(0.1, 0.1, 2, 0.8, fill=P.tint(P.BLUE), edge=P.BLUE, r=0.08)
    h = sc.text(0.2, 0.2, "Measured text wraps to its width", w=1.8, role="text")
    sc.line([(2.1, 0.5), (3.0, 0.5)], head=True)
    sc.icon("database", 3.1, 0.3, 0.4)
    sc.save("figure.png")                       # an image, checked by figqa
    sc.to_slide(slide, x=0.3, y=1.4)            # the same drawing as native shapes on a slide

Coordinates run from the top-left corner. Text is wrapped by its measured width (Arial) and drawn with explicit
line breaks in both outputs, so both have the same lines. `Scene.check()` runs the layout check (figqa) on the
image twin; to_slide() runs it too, so a native diagram is checked like an image one. diagrams.py builds every
diagram type as a Scene.
"""

from __future__ import annotations

import math

import palette as P

TYPE = {                 # point sizes per medium and role
    "report": {"name": 9.5, "text": 8.0, "small": 7.5, "badge": 7.5, "min": 6.0},
    "slide": {"name": 16.0, "text": 14.0, "small": 12.0, "badge": 11.0, "min": 10.0},
}
LS = 1.22                # line height in em


def wrap_lines(text: str, w: float, pt: float, bold: bool = False) -> list[str]:
    """Lines of text wrapped to w inches at pt points by measured Arial width (a character estimate without Arial)."""
    if not text:
        return []
    try:
        import slide_measure
        return slide_measure.wrap(text, pt, bold, w / slide_measure.WRAP_GUARD)
    except (FileNotFoundError, OSError, ImportError):
        import textwrap
        chars = max(6, int(w * 72 / (pt * 0.52)))
        return [ln for p in text.split("\n") for ln in (textwrap.wrap(p, chars, break_long_words=False) or [""])]


def text_width(text: str, pt: float, bold: bool = False) -> float:
    """Printed width in inches of one line."""
    try:
        import slide_measure
        return slide_measure.width(text, pt, bold)
    except (FileNotFoundError, OSError, ImportError):
        return len(text) * pt * 0.52 / 72


class Scene:
    def __init__(self, w: float, h: float, medium: str = "report"):
        self.w, self.h, self.medium = w, h, medium
        self.items: list[tuple] = []
        self.T = TYPE[medium]

    # ------------------------------------------------------------------ type and measuring
    def pt(self, role):
        return self.T[role] if isinstance(role, str) else role

    def lines(self, text, w, role="text", bold=False):
        return wrap_lines(text, w, self.pt(role), bold)

    def text_h(self, text, w, role="text", bold=False):
        """Height in inches of `text` wrapped to w at the role's size."""
        n = len(self.lines(text, w, role, bold))
        return n * self.pt(role) * LS / 72              # PowerPoint's exact spacing gives every line LS em

    def width_of(self, text, role="text", bold=False):
        return text_width(text, self.pt(role), bold)

    # ------------------------------------------------------------------ primitives
    def rect(self, x, y, w, h, fill=None, edge=None, r=0.0, lw=1.0, dashed=False, z=1):
        """A rectangle (rounded with radius r inches); fill or edge None leaves it out."""
        self.items.append(("rect", z, dict(x=x, y=y, w=w, h=h, fill=fill, edge=edge, r=r, lw=lw, dashed=dashed)))

    def ellipse(self, cx, cy, w, h, fill=None, edge=None, lw=1.0, alpha=1.0, z=1):
        self.items.append(("ellipse", z, dict(cx=cx, cy=cy, w=w, h=h, fill=fill, edge=edge, lw=lw, alpha=alpha)))

    def poly(self, pts, fill=None, edge=None, lw=1.0, z=1):
        """A closed polygon through pts (a diamond, a chevron, a tab)."""
        self.items.append(("poly", z, dict(pts=list(pts), fill=fill, edge=edge, lw=lw)))

    def line(self, pts, color=P.CONNECTOR, lw=1.2, dashed=False, head=False, tail=False, z=2):
        """A polyline through pts; head draws an arrowhead at the last point, tail at the first."""
        self.items.append(("line", z, dict(pts=list(pts), color=color, lw=lw, dashed=dashed, head=head, tail=tail)))

    def curve(self, p0, p1, bend=0.25, color=P.CONNECTOR, lw=1.2, dashed=False, head=True, z=2):
        """A circular arc from p0 to p1 bowing to the left of the direction by `bend` × the chord length."""
        (x0, y0), (x1, y1) = p0, p1
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        dx, dy = x1 - x0, y1 - y0
        cx, cy = mx + dy * bend, my - dx * bend
        pts = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1,
                (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1) for t in [k / 24 for k in range(25)]]
        self.line(pts, color, lw, dashed, head=head, z=z)

    def text(self, x, y, text, w, role="text", bold=False, color=P.INK, align="left", plate=None, italic=False,
             z=5):
        """Text wrapped to w inches with its top at y; align left (x is the left edge), center (x is the centre) or
        right (x is the right edge). `plate` is a fill drawn behind the text (it hides lines under it). Returns the
        height."""
        pt = self.pt(role)
        lines = wrap_lines(text, w, pt, bold)
        if not lines:
            return 0.0
        self.items.append(("text", z, dict(x=x, y=y, w=w, lines=lines, pt=pt, bold=bold, color=color, align=align,
                                           plate=plate, italic=italic)))
        return len(lines) * pt * LS / 72

    def icon(self, name, x, y, size, color=P.BLUE, bg=P.SURFACE, z=6):
        self.items.append(("icon", z, dict(name=name, x=x, y=y, size=size, color=color, bg=bg)))

    def badge(self, cx, cy, n, color=P.NAVY, r=None, z=8):
        """A numbered disc."""
        r = r or self.pt("badge") * 0.92 / 72
        self.ellipse(cx, cy, 2 * r, 2 * r, fill=color, edge=P.SURFACE, lw=1.0, z=z)
        self.items.append(("label", z + 1, dict(cx=cx, cy=cy, s=str(n), pt=self.pt("badge"), color=P.SURFACE,
                                                bold=True)))

    def image(self, path, x, y, w, h, z=0):
        self.items.append(("image", z, dict(path=str(path), x=x, y=y, w=w, h=h)))

    def _sorted(self):
        return [it for _, it in sorted(enumerate(self.items), key=lambda kv: (kv[1][1], kv[0]))]

    # ------------------------------------------------------------------ image output
    def figure(self):
        """The drawing as a matplotlib figure (inches, y down)."""
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle
        plt.rcParams["font.family"] = ["Arial", "Helvetica", "DejaVu Sans"]
        fig = plt.figure(figsize=(self.w, self.h))
        fig.patch.set_facecolor("white")
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, self.w)
        ax.set_ylim(self.h, 0)
        ax.axis("off")
        for kind, z, a in self._sorted():
            if kind == "rect":
                ls = (0, (4, 2.5)) if a["dashed"] else "-"
                if a["r"]:
                    p = FancyBboxPatch((a["x"], a["y"]), a["w"], a["h"],
                                       boxstyle=f"round,pad=0,rounding_size={min(a['r'], a['w'] / 2, a['h'] / 2)}",
                                       fc=a["fill"] or "none", ec=a["edge"] or "none", lw=a["lw"], ls=ls, zorder=z)
                else:
                    p = Rectangle((a["x"], a["y"]), a["w"], a["h"], fc=a["fill"] or "none", ec=a["edge"] or "none",
                                  lw=a["lw"], ls=ls, zorder=z)
                ax.add_patch(p)
            elif kind == "ellipse":
                ax.add_patch(Ellipse((a["cx"], a["cy"]), a["w"], a["h"], fc=a["fill"] or "none",
                                     ec=a["edge"] or "none", lw=a["lw"], alpha=a["alpha"] if a["fill"] else 1,
                                     zorder=z))
                if a["fill"] and a["alpha"] < 1 and a["edge"]:
                    ax.add_patch(Ellipse((a["cx"], a["cy"]), a["w"], a["h"], fc="none", ec=a["edge"], lw=a["lw"],
                                         zorder=z))
            elif kind == "poly":
                ax.add_patch(Polygon(a["pts"], closed=True, fc=a["fill"] or "none", ec=a["edge"] or "none",
                                     lw=a["lw"], zorder=z, joinstyle="miter"))
            elif kind == "line":
                pts = a["pts"]
                ls = (0, (4, 2.5)) if a["dashed"] else "-"
                xs, ys = zip(*pts)
                ax.plot(xs, ys, color=a["color"], lw=a["lw"], ls=ls, zorder=z, solid_capstyle="butt",
                        solid_joinstyle="miter")
                for flag, (p0, p1) in ((a["head"], (pts[-2], pts[-1])), (a["tail"], (pts[1], pts[0]))):
                    if flag:
                        ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=10, color=a["color"],
                                                     lw=0.01, zorder=z, shrinkA=0, shrinkB=0))
            elif kind == "text":
                ha = a["align"]
                bbox = dict(boxstyle="round,pad=0.16", fc=a["plate"], ec="none") if a["plate"] else None
                ax.text(a["x"], a["y"], "\n".join(a["lines"]), fontsize=a["pt"], color=a["color"], ha=ha,
                        va="top", fontweight="bold" if a["bold"] else "normal", linespacing=LS,
                        style="italic" if a["italic"] else "normal", zorder=z, bbox=bbox)
            elif kind == "label":
                ax.text(a["cx"], a["cy"], a["s"], fontsize=a["pt"], color=a["color"], ha="center", va="center",
                        fontweight="bold" if a["bold"] else "normal", zorder=z,
                        bbox=dict(boxstyle="circle,pad=0.05", fc="none", ec="none"))
            elif kind == "icon":
                import icons
                icons.draw_icon(fig, a["name"], a["x"], a["y"], a["size"], a["color"], a["bg"],
                                zorder=10 + z).set_label("icon")
            elif kind == "image":
                import matplotlib.image as mpimg
                ax.imshow(mpimg.imread(a["path"]), extent=(a["x"], a["x"] + a["w"], a["y"] + a["h"], a["y"]),
                          zorder=z)
                ax.set_xlim(0, self.w)
                ax.set_ylim(self.h, 0)
        return fig

    def check(self, min_pt=None):
        """Layout findings of the drawing (figqa), at its own size."""
        import matplotlib.pyplot as plt
        import figqa
        fig = self.figure()
        issues = figqa.check(fig, min_pt=min_pt or self.T["min"], page=self.medium == "report")
        plt.close(fig)
        return issues

    def save(self, path, check=True, dpi=300):
        """Write the drawing as a PNG (or SVG by the file name) and run the layout check; returns the findings."""
        import matplotlib.pyplot as plt
        import figqa
        fig = self.figure()
        fig._figqa_done = check
        fig.savefig(path, dpi=dpi, facecolor="white")
        issues = figqa.report(fig, path, min_pt=self.T["min"], page=self.medium == "report") if check else []
        plt.close(fig)
        return issues

    # ------------------------------------------------------------------ native slide output
    def to_slide(self, slide, x=0.0, y=0.0, check=True, cache=None, name=None):
        """Draw the scene as native PowerPoint shapes with its top-left corner at (x, y) inches on `slide`, in one
        group (named `name`) so it moves and scales as a whole and ungroups for editing; icons and images become
        pictures. Returns the layout findings (printed as WARN lines)."""
        from pptx.dml.color import RGBColor
        from pptx.enum.dml import MSO_LINE_DASH_STYLE
        from pptx.enum.shapes import MSO_SHAPE
        from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
        from pptx.oxml.ns import qn
        from pptx.util import Emu, Inches, Pt
        from lxml import etree

        I = lambda v: Emu(int(round(v * 914400)))                       # noqa: E731
        from matplotlib.colors import to_hex
        rgb = lambda c: RGBColor.from_string(to_hex(c)[1:].upper())      # noqa: E731  (hex or a colour name)
        group = slide.shapes.add_group_shape()                          # the diagram moves and scales as one
        group.name = name or "diagram"
        sh = group.shapes

        def style_line(shape_line, color, lw, dashed):
            if color is None:
                shape_line.fill.background()
                return
            shape_line.color.rgb = rgb(color)
            shape_line.width = Pt(lw)
            if dashed:
                shape_line.dash_style = MSO_LINE_DASH_STYLE.DASH

        for kind, z, a in self._sorted():
            if kind == "rect":
                shape = sh.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if a["r"] else MSO_SHAPE.RECTANGLE,
                                     I(x + a["x"]), I(y + a["y"]), I(a["w"]), I(a["h"]))
                if a["r"]:
                    shape.adjustments[0] = min(0.5, a["r"] / max(min(a["w"], a["h"]), 1e-6))
                if a["fill"]:
                    shape.fill.solid()
                    shape.fill.fore_color.rgb = rgb(a["fill"])
                else:
                    shape.fill.background()
                style_line(shape.line, a["edge"], a["lw"], a["dashed"])
                shape.shadow.inherit = False
            elif kind == "ellipse":
                shape = sh.add_shape(MSO_SHAPE.OVAL, I(x + a["cx"] - a["w"] / 2), I(y + a["cy"] - a["h"] / 2),
                                     I(a["w"]), I(a["h"]))
                if a["fill"]:
                    shape.fill.solid()
                    shape.fill.fore_color.rgb = rgb(a["fill"])
                    if a["alpha"] < 1:
                        clr = shape.fill._xPr.find(qn("a:solidFill"))[0]
                        etree.SubElement(clr, qn("a:alpha")).set("val", str(int(a["alpha"] * 100000)))
                else:
                    shape.fill.background()
                style_line(shape.line, a["edge"], a["lw"], False)
                shape.shadow.inherit = False
            elif kind == "poly":
                pts = [(x + px, y + py) for px, py in a["pts"]]
                fb = sh.build_freeform(I(pts[0][0]), I(pts[0][1]), scale=1.0)
                fb.add_line_segments([(I(px), I(py)) for px, py in pts[1:]], close=True)
                shape = fb.convert_to_shape()
                if a["fill"]:
                    shape.fill.solid()
                    shape.fill.fore_color.rgb = rgb(a["fill"])
                else:
                    shape.fill.background()
                style_line(shape.line, a["edge"], a["lw"], False)
                shape.shadow.inherit = False
            elif kind == "line":
                pts = [(x + px, y + py) for px, py in a["pts"]]
                fb = sh.build_freeform(I(pts[0][0]), I(pts[0][1]), scale=1.0)
                fb.add_line_segments([(I(px), I(py)) for px, py in pts[1:]], close=False)
                shape = fb.convert_to_shape()
                shape.fill.background()
                style_line(shape.line, a["color"], a["lw"], a["dashed"])
                ln = shape.line._get_or_add_ln()
                for flag, tag in ((a["head"], "a:tailEnd"), (a["tail"], "a:headEnd")):
                    if flag:
                        end = etree.SubElement(ln, qn(tag))
                        end.set("type", "triangle")
                        end.set("w", "med")
                        end.set("len", "med")
                shape.shadow.inherit = False
            elif kind in ("text", "label"):
                if kind == "label":
                    w = text_width(a["s"], a["pt"], True) + 0.1
                    lines, left, top, width = [a["s"]], a["cx"] - w / 2, a["cy"] - a["pt"] * 0.62 / 72, w
                    align, plate = "center", None
                else:
                    lines, top = a["lines"], a["y"]
                    width = max(text_width(ln, a["pt"], a["bold"]) for ln in lines) + 0.04
                    if not a["plate"]:                         # room to spare; a plate stays tight to its text
                        width = max(width, a["w"])
                    left = {"left": a["x"], "center": a["x"] - width / 2, "right": a["x"] - width}[a["align"]]
                    align, plate = a["align"], a["plate"]
                height = len(lines) * a["pt"] * LS / 72
                pad = 0.03 if plate else 0.0
                box = sh.add_textbox(I(x + left - pad), I(y + top - pad), I(width + 2 * pad), I(height + 2 * pad))
                tf = box.text_frame
                tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = I(pad)
                tf.word_wrap = False
                tf.vertical_anchor = MSO_ANCHOR.TOP
                if plate:
                    box.fill.solid()
                    box.fill.fore_color.rgb = rgb(plate)
                p = tf.paragraphs[0]
                p.alignment = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}[align]
                p.line_spacing = Pt(a["pt"] * LS)
                for k, ln in enumerate(lines):
                    if k:
                        p.add_line_break()
                    r = p.add_run()
                    r.text = ln
                    r.font.size = Pt(a["pt"])
                    r.font.name = "Arial"
                    r.font.bold = a["bold"]
                    r.font.italic = a.get("italic", False)
                    r.font.color.rgb = rgb(a["color"])
            elif kind == "icon":
                import icons
                from pathlib import Path
                folder = Path(cache) if cache else Path(__file__).resolve().parents[4] / "build" / ".cache" / "icons"
                folder.mkdir(parents=True, exist_ok=True)
                f = folder / f"{a['name']}-{to_hex(a['color'])[1:]}-{to_hex(a['bg'])[1:]}.png"
                if not f.exists():
                    icons.icon_png(a["name"], a["color"], f, size_in=1.0, dpi=300, bg=a["bg"])
                sh.add_picture(str(f), I(x + a["x"]), I(y + a["y"]), I(a["size"]), I(a["size"]))
            elif kind == "image":
                sh.add_picture(a["path"], I(x + a["x"]), I(y + a["y"]), I(a["w"]), I(a["h"]))
        issues = self.check() if check else []
        for i in issues:
            print(f"WARN  native scene {self.w:.1f}x{self.h:.1f} in: {i}")
        return issues


def bend_points(p0, p1, n=24, bend=0.25):
    """Points of the arc used by Scene.curve (for placing labels on it)."""
    (x0, y0), (x1, y1) = p0, p1
    cx, cy = (x0 + x1) / 2 + (y1 - y0) * bend, (y0 + y1) / 2 - (x1 - x0) * bend
    return [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1, (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1)
            for t in [k / n for k in range(n + 1)]]


def edge_point(c, hw, hh, toward):
    """Where the line from the centre c of a hw × hh half-size box toward a point leaves the box."""
    dx, dy = toward[0] - c[0], toward[1] - c[1]
    if dx == 0 and dy == 0:
        return c
    t = min(hw / abs(dx) if dx else math.inf, hh / abs(dy) if dy else math.inf)
    return (c[0] + dx * t, c[1] + dy * t)
