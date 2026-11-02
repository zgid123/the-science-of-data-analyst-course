"""Small code-first diagram toolkit for C4-style figures, rendered with matplotlib.

Coordinates are in inches on a canvas of size (width, height). Every element is
placed with (x, y, w, h), where (x, y) is the TOP-LEFT corner measured from the
top-left of the canvas, so specs read like a page layout.

Colours come from palette.py (ROLES, LIGHT, INK, MUTED), so a role looks the same in every figure, chart and slide.
Text wraps by its measured width in Arial. Boxes take an icon (icons.py). Canvas.trim() cuts the empty space under
the drawing, and Canvas.save() runs the layout check (figqa.py) and prints what a reader would trip over. Ready-made
diagram types built on the canvas (sequence, timeline, state machine, process, cycle, matrix, layers, comparison,
annotated screenshot) are in diagrams.py.
"""

from __future__ import annotations

import textwrap
from dataclasses import dataclass

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, FancyBboxPatch, Rectangle  # noqa: E402

import palette  # noqa: E402

FONT = "Arial"
plt.rcParams["font.family"] = [FONT, "Helvetica", "DejaVu Sans"]

# Role-based palette shared by every figure (palette.py): (fill, text colour), and light tones (fill, text, edge).
ROLES = palette.ROLES
LIGHT = palette.LIGHT

LEGEND_LABELS = {
    "person": "Person",
    "system": "Software system in scope",
    "external": "External system",
    "warehouse": "Data Warehouse",
    "lake": "Data Lake",
    "agent": "Agent / serving",
    "ingest": "Ingestion",
    "review": "Quality & review",
    "store": "Supporting store",
    "critical": "Error / rejection",
}

INK = palette.INK
MUTED = palette.MUTED
CONNECTOR = palette.CONNECTOR


@dataclass
class Node:
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

    def anchor(self, side: str, t: float = 0.5):
        """Point on a side; t runs 0..1 along that side (left->right / top->bottom)."""
        if side == "n":
            return (self.x + self.w * t, self.y)
        if side == "s":
            return (self.x + self.w * t, self.y + self.h)
        if side == "w":
            return (self.x, self.y + self.h * t)
        if side == "e":
            return (self.x + self.w, self.y + self.h * t)
        raise ValueError(side)


def wrap(text: str, width_in: float, fs: float, bold: bool = False) -> str:
    """Wrap text to width_in inches at fs points by its measured width in Arial (a character estimate when Arial is
    not installed); words are never split, so a name like "attribute_history" stays whole."""
    try:
        import slide_measure
        return "\n".join(slide_measure.wrap(text, fs, bold, width_in / slide_measure.WRAP_GUARD))
    except (FileNotFoundError, OSError, ImportError):
        chars = max(8, int(width_in * 72 / (fs * 0.52)))
        return "\n".join(textwrap.fill(p, chars, break_long_words=False, break_on_hyphens=False)
                         for p in text.split("\n"))


class Canvas:
    def __init__(self, width: float, height: float, title: str | None = None, subtitle: str | None = None):
        self.W, self.H = width, height
        self.fig = plt.figure(figsize=(width, height))
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(height, 0)  # y grows downward
        self.ax.axis("off")
        self.fig.patch.set_facecolor("white")
        self.used_roles: list[str] = []
        if title:
            self.ax.text(0.3, 0.32, title, fontsize=13, fontweight="bold", color=INK, va="top")
        if subtitle:
            self.ax.text(0.3, 0.62, subtitle, fontsize=9.5, color=MUTED, va="top")

    # ------------------------------------------------------------------ helpers
    def _note_role(self, role):
        if role not in self.used_roles:
            self.used_roles.append(role)

    def _label_block(self, node, name, tech, desc, color, name_fs=10, desc_fs=8, top_pad=None):
        parts = []
        cx = node.cx
        y = node.y + (top_pad if top_pad is not None else 0.14)
        self.ax.text(cx, y, wrap(name, node.w - 0.15, name_fs, True), ha="center", va="top",
                     fontsize=name_fs, fontweight="bold", color=color, linespacing=1.15)
        n_lines = wrap(name, node.w - 0.15, name_fs, True).count("\n") + 1
        y += n_lines * name_fs * 1.25 / 72 + 0.04
        if tech:
            t = wrap(f"[{tech}]", node.w - 0.15, desc_fs - 0.5)
            self.ax.text(cx, y, t, ha="center", va="top", fontsize=desc_fs - 0.5, color=color,
                         style="italic", alpha=0.92, linespacing=1.1)
            y += (t.count("\n") + 1) * (desc_fs - 0.5) * 1.2 / 72 + 0.06
        if desc:
            d = wrap(desc, node.w - 0.2, desc_fs)
            self.ax.text(cx, y, d, ha="center", va="top", fontsize=desc_fs, color=color, linespacing=1.2)
        return parts

    # ------------------------------------------------------------------ shapes
    def box(self, x, y, w, h, name, tech=None, desc=None, role="system", light=False, dashed=False,
            name_fs=10, desc_fs=8, icon=None):
        """A C4 box; `icon` (an icons.py name) sits on top of a narrow or tall box with the text under it, and on the
        left of a wide, short box with the text beside it."""
        node = Node(x, y, w, h)
        if light:
            fill, txt, edge = LIGHT[role]
        else:
            fill, txt = ROLES[role]
            edge = fill
        self._note_role(role)
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.08",
                                         fc=fill, ec=edge, lw=1.3, ls="--" if dashed else "-", zorder=3))
        text_node, top_pad = node, None
        if icon:
            color = edge if light else txt
            if w >= 1.6 and h <= 1.0:                    # wide and short: the icon on the left, text beside it
                s = min(0.42, h * 0.5)
                self.icon(icon, x + 0.12, y + (h - s) / 2, s, color=color, bg=fill)
                text_node = Node(x + s + 0.12, y, w - s - 0.16, h)
            else:                                        # narrow or tall: the icon on top, text under it
                s = min(0.34, w * 0.3)
                self.icon(icon, x + (w - s) / 2, y + 0.12, s, color=color, bg=fill)
                top_pad = 0.12 + s + 0.06
        self._label_block(text_node, name, tech, desc, txt, name_fs, desc_fs, top_pad=top_pad)
        return node

    def icon(self, name, x, y, size, color=None, bg="white"):
        """An icon (icons.py) in a size × size inch square with its top-left corner at (x, y)."""
        import icons
        icons.draw_icon(self.fig, name, x, y, size, color or palette.BLUE, bg).set_label("icon")

    def person(self, x, y, w, h, name, desc=None, role="person", desc_fs=8):
        fill, txt = ROLES[role]
        self._note_role(role)
        r = min(0.24, h * 0.22)
        body_top = y + r * 1.55
        self.ax.add_patch(FancyBboxPatch((x, body_top), w, h - (body_top - y),
                                         boxstyle="round,pad=0,rounding_size=0.22", fc=fill, ec=fill, zorder=3))
        self.ax.add_patch(Circle((x + w / 2, y + r), r, fc=fill, ec="white", lw=1.5, zorder=4))
        body = Node(x, body_top, w, h - (body_top - y))
        self._label_block(body, name, None, desc, txt, 10, desc_fs, top_pad=0.12)
        return Node(x, y, w, h)

    def database(self, x, y, w, h, name, tech=None, desc=None, role="warehouse", light=False,
                 name_fs=10, desc_fs=8):
        if light:
            fill, txt, edge = LIGHT[role]
        else:
            fill, txt = ROLES[role]
            edge = fill
        self._note_role(role)
        e = min(0.28, h * 0.22)  # ellipse height
        self.ax.add_patch(Rectangle((x, y + e / 2), w, h - e, fc=fill, ec="none", zorder=3))
        self.ax.add_patch(Ellipse((x + w / 2, y + h - e / 2), w, e, fc=fill, ec=edge, lw=1.3, zorder=3))
        self.ax.plot([x, x], [y + e / 2, y + h - e / 2], color=edge, lw=1.3, zorder=3)
        self.ax.plot([x + w, x + w], [y + e / 2, y + h - e / 2], color=edge, lw=1.3, zorder=3)
        top_edge = "white" if not light else edge
        self.ax.add_patch(Ellipse((x + w / 2, y + e / 2), w, e, fc=fill, ec=top_edge, lw=1.3, zorder=4))
        node = Node(x, y + e, w, h - e)
        self._label_block(node, name, tech, desc, txt, name_fs, desc_fs, top_pad=0.06)
        return Node(x, y, w, h)

    def boundary(self, x, y, w, h, label, sublabel=None, color="#6E7781", fill=None):
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                         fc=fill or "none", ec=color, lw=1.2, ls=(0, (5, 3)), zorder=1))
        self.ax.text(x + 0.14, y + h - 0.1, label, ha="left", va="bottom", fontsize=9.5,
                     fontweight="bold", color=color, zorder=2)
        if sublabel:
            self.ax.text(x + 0.14, y + h - 0.1 - 0.02, "", fontsize=1)
            self.ax.text(x + w - 0.14, y + h - 0.1, sublabel, ha="right", va="bottom", fontsize=8,
                         style="italic", color=color, zorder=2)
        return Node(x, y, w, h)

    def lane(self, x, y, w, h, header, fill="#F4F6F9", header_fill="#3B4452"):
        self.ax.add_patch(Rectangle((x, y), w, h, fc=fill, ec="none", zorder=0))
        self.ax.add_patch(Rectangle((x, y), w, 0.42, fc=header_fill, ec="none", zorder=1))
        self.ax.text(x + w / 2, y + 0.21, header, ha="center", va="center", fontsize=10,
                     fontweight="bold", color="white", zorder=2)
        return Node(x, y, w, h)

    def band(self, x, y, w, h, label, fill="#EEF1F5", color=MUTED):
        """A horizontal background band with a label on its left edge."""
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                                         fc=fill, ec="none", zorder=0))
        self.ax.text(x + 0.12, y + h / 2, label, ha="left", va="center", rotation=90,
                     fontsize=8.5, fontweight="bold", color=color, zorder=1)
        return Node(x, y, w, h)

    def uml_class(self, x, y, w, name, fields, stereotype=None, role="warehouse", fs=8, row_h=0.2):
        fill, txt, edge = LIGHT[role]
        self._note_role(role)
        head_h = 0.34 + (0.16 if stereotype else 0)
        h = head_h + row_h * len(fields) + 0.1
        self.ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.05",
                                         fc="white", ec=edge, lw=1.3, zorder=3))
        self.ax.add_patch(FancyBboxPatch((x, y), w, head_h, boxstyle="round,pad=0,rounding_size=0.05",
                                         fc=fill, ec=edge, lw=1.3, zorder=3))
        ty = y + 0.08
        if stereotype:
            self.ax.text(x + w / 2, ty, f"«{stereotype}»", ha="center", va="top", fontsize=fs - 0.5,
                         color=txt, style="italic", zorder=4)
            ty += 0.16
        self.ax.text(x + w / 2, ty, name, ha="center", va="top", fontsize=fs + 1.5, fontweight="bold",
                     color=txt, zorder=4)
        fy = y + head_h + 0.06
        for f in fields:
            weight = "bold" if f.startswith("PK ") else "normal"
            self.ax.text(x + 0.1, fy, f, ha="left", va="top", fontsize=fs, color=INK,
                         fontweight=weight, family="monospace" if False else None, zorder=4)
            fy += row_h
        return Node(x, y, w, h)

    def note(self, x, y, w, text, fs=8, color=MUTED):
        self.ax.text(x, y, wrap(text, w, fs), ha="left", va="top", fontsize=fs, color=color,
                     style="italic", linespacing=1.25)

    # ------------------------------------------------------------------ arrows
    def arrow(self, a: Node, b: Node, label=None, sides=None, via=None, ts=(0.5, 0.5), dashed=True,
              both=False, color="#4A5260", label_at=0.5, label_dx=0.0, label_dy=0.0, fs=7.5, lw=1.2,
              label_w=1.8, head=True, ends=None):
        """Connect two nodes. sides=('e','w') forces anchor sides; via adds waypoints.

        Without sides, the connector picks an orthogonal straight path when the boxes overlap
        on one axis, and an L-shaped path otherwise.
        """
        if sides:
            p0 = a.anchor(sides[0], ts[0])
            p1 = b.anchor(sides[1], ts[1])
            pts = [p0] + list(via or []) + [p1]
            if not via:
                # make an orthogonal elbow when anchors are not aligned
                if sides[0] in "ns" and sides[1] in "ns" and abs(p0[0] - p1[0]) > 1e-6:
                    my = (p0[1] + p1[1]) / 2
                    pts = [p0, (p0[0], my), (p1[0], my), p1]
                elif sides[0] in "ew" and sides[1] in "ew" and abs(p0[1] - p1[1]) > 1e-6:
                    mx = (p0[0] + p1[0]) / 2
                    pts = [p0, (mx, p0[1]), (mx, p1[1]), p1]
                elif sides[0] in "ew" and sides[1] in "ns":
                    pts = [p0, (p1[0], p0[1]), p1]
                elif sides[0] in "ns" and sides[1] in "ew":
                    pts = [p0, (p0[0], p1[1]), p1]
        else:
            ox0, ox1 = max(a.x, b.x), min(a.x + a.w, b.x + b.w)
            oy0, oy1 = max(a.y, b.y), min(a.y + a.h, b.y + b.h)
            if ox1 - ox0 > 0.25:  # vertical connection
                mx = (ox0 + ox1) / 2
                if a.cy < b.cy:
                    pts = [(mx, a.y + a.h), (mx, b.y)]
                else:
                    pts = [(mx, a.y), (mx, b.y + b.h)]
            elif oy1 - oy0 > 0.2:  # horizontal connection
                my = (oy0 + oy1) / 2
                if a.cx < b.cx:
                    pts = [(a.x + a.w, my), (b.x, my)]
                else:
                    pts = [(a.x, my), (b.x + b.w, my)]
            else:  # L-shape: leave horizontally, enter vertically
                p0 = a.anchor("e" if b.cx > a.cx else "w")
                p1 = b.anchor("n" if b.cy > a.cy else "s")
                pts = [p0, (p1[0], p0[1]), p1]

        ls = (0, (4, 2.5)) if dashed else "-"
        xs, ys = zip(*pts)
        self.ax.plot(xs[:-1] + (xs[-1],), ys[:-1] + (ys[-1],), color=color, lw=lw, ls=ls, zorder=2,
                     solid_capstyle="butt")
        if head:
            self.ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>",
                                              mutation_scale=11, color=color, lw=0.01, zorder=2,
                                              shrinkA=0, shrinkB=0))
        if ends:
            # multiplicity labels just beside each endpoint (UML associations)
            for (px, py), (qx, qy), txt in ((pts[0], pts[1], ends[0]), (pts[-1], pts[-2], ends[1])):
                if not txt:
                    continue
                dx, dy = qx - px, qy - py
                n = max((dx * dx + dy * dy) ** 0.5, 1e-6)
                ox, oy = px + dx / n * 0.14, py + dy / n * 0.14
                ox, oy = (ox + 0.08, oy - 0.08) if abs(dx) < abs(dy) else (ox, oy - 0.1)
                self.ax.text(ox, oy, txt, fontsize=8, color=INK, ha="left", va="center", zorder=5)
        if both:
            self.ax.add_patch(FancyArrowPatch(pts[1], pts[0], arrowstyle="-|>", mutation_scale=11,
                                              color=color, lw=0.01, zorder=2, shrinkA=0, shrinkB=0))
        if label:
            # place on the longest segment
            segs = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
            (sx, sy), (ex, ey) = max(segs, key=lambda s: abs(s[0][0] - s[1][0]) + abs(s[0][1] - s[1][1]))
            lx = sx + (ex - sx) * label_at + label_dx
            ly = sy + (ey - sy) * label_at + label_dy
            va = "center"
            if abs(sy - ey) < 1e-6 and abs(ex - sx) < 0.9 and label_dy == 0:
                # short horizontal connector: lift the label so the arrowhead stays visible
                ly -= 0.07
                va = "bottom"
            self.ax.text(lx, ly, wrap(label, label_w, fs), ha="center", va=va, fontsize=fs,
                         color=INK, zorder=5, linespacing=1.15,
                         bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#C9CED6", lw=0.6))

    # ------------------------------------------------------------------ legend & save
    def legend(self, y=None, roles=None, extra=None):
        """Colour swatches for the roles used, then line styles; wraps to a second row when needed."""
        roles = self.used_roles if roles is None else roles
        y = y if y is not None else self.H - 0.35
        items = [("role", r, LEGEND_LABELS[r]) for r in roles] + [("line", k, lab) for k, lab in (extra or [])]
        x = 0.3
        for kind, key, label in items:
            width = (0.34 if kind == "role" else 0.5) + len(label) * 0.066 + 0.3
            if x + width > self.W - 0.2:
                x, y = 0.3, y + 0.3
            if kind == "role":
                fill = ROLES[key][0]
                self.ax.add_patch(FancyBboxPatch((x, y - 0.09), 0.26, 0.18, boxstyle="round,pad=0,rounding_size=0.03",
                                                 fc=fill, ec=fill, zorder=3))
                self.ax.text(x + 0.34, y, label, va="center", fontsize=8, color=INK)
            else:
                ls = (0, (4, 2.5)) if key == "dashed" else "-"
                color, lw = ("#1A8C8C", 1.8) if key == "teal" else ("#4A5260", 1.2)
                self.ax.plot([x, x + 0.4], [y, y], color=color, lw=lw, ls=ls)
                self.ax.text(x + 0.5, y, label, va="center", fontsize=8, color=INK)
            x += width

    def trim(self, pad=0.15):
        """Cut the empty space under the drawing: the canvas ends `pad` inches below its lowest element, so the
        figure takes no more room on the page than it needs."""
        self.fig.canvas.draw()
        r = self.fig.canvas.get_renderer()
        bottom = 0.0
        inv = self.ax.transData.inverted()
        for a in self.ax.get_children():
            if not a.get_visible() or a is self.ax.patch or a in self.ax.spines.values():
                continue
            try:
                bb = a.get_window_extent(r)
            except (RuntimeError, ValueError, TypeError, AttributeError):
                continue
            if bb.width <= 0 or bb.height <= 0 or bb.height >= self.fig.bbox.height * 0.999:
                continue
            bottom = max(bottom, inv.transform((bb.x0, bb.y0))[1])
        new_h = min(self.H, bottom + pad)
        if new_h < self.H - 0.05:
            old_h = self.H
            insets = []                                   # icon axes, kept at their place in inches
            for a in self.fig.axes:
                if a is not self.ax:
                    q = a.get_position()
                    insets.append((a, q.x0 * self.W, (1 - q.y1) * old_h, q.width * self.W, q.height * old_h))
            self.H = new_h
            self.fig.set_size_inches(self.W, new_h)
            self.ax.set_position([0, 0, 1, 1])
            self.ax.set_ylim(new_h, 0)
            for a, left, top, w, h in insets:
                a.set_position([left / self.W, 1 - (top + h) / new_h, w / self.W, h / new_h])
        return self

    def save(self, path, check=True, min_pt=6.0):
        """Write the figure at 300 dpi and run the layout check (figqa); returns the findings it printed."""
        self.fig._figqa_done = check
        self.fig.savefig(path, dpi=300, facecolor="white")
        issues = []
        if check:
            import figqa
            issues = figqa.report(self.fig, path, min_pt=min_pt)

        plt.close(self.fig)
        return issues
