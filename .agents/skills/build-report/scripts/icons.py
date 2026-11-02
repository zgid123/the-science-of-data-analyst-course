"""Pictograms drawn in code: one colour, flat, licence-free, recoloured by role, sharp at any size.

Usage:
    from icons import ICONS, draw_icon, icon_png
    draw_icon(fig, "database", left, top, size, color)   # on any matplotlib figure, inches from the top-left corner
    icon_png("lock", "#2A6FBB", "lock.png")              # a transparent PNG (slides, documents)
    Canvas.icon(...), Canvas.box(..., icon="server")     # in c4kit; slidekit.icon(...) on a slide

Each icon is drawn in a unit square (0..1, y up) with solid shapes in the icon colour and cut-outs in the
background colour, so it reads on white and on a light tint; on a solid fill, draw it in white with the fill as its
background. Use an icon beside a word, never instead of it: the word carries the meaning, the icon makes the
element quick to find and the page inviting. `python icons.py OUT.png` draws the whole set as a contact sheet.
"""

from __future__ import annotations

import math
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle, Wedge, Arc  # noqa: E402

from palette import BLUE, INK, SURFACE  # noqa: E402


class Pen:
    """Draws one icon on a unit-square axes: fill shapes in `fg`, cut-outs in `bg`, strokes in unit widths."""

    def __init__(self, ax, fg, bg, size_in):
        self.ax, self.fg, self.bg, self.pt = ax, fg, bg, size_in * 72

    def _c(self, cut):
        return self.bg if cut else self.fg

    def rect(self, x, y, w, h, r=0.0, cut=False):
        if r:
            p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=self._c(cut), ec="none")
        else:
            p = Rectangle((x, y), w, h, fc=self._c(cut), ec="none")
        self.ax.add_patch(p)

    def circle(self, x, y, r, cut=False):
        self.ax.add_patch(Circle((x, y), r, fc=self._c(cut), ec="none"))

    def ellipse(self, x, y, w, h, cut=False):
        self.ax.add_patch(Ellipse((x, y), w, h, fc=self._c(cut), ec="none"))

    def poly(self, pts, cut=False):
        self.ax.add_patch(Polygon(pts, closed=True, fc=self._c(cut), ec="none"))

    def wedge(self, x, y, r, a0, a1, width=None, cut=False):
        self.ax.add_patch(Wedge((x, y), r, a0, a1, width=width, fc=self._c(cut), ec="none"))

    def ring(self, x, y, r, w, cut=False):
        self.ax.add_patch(Circle((x, y), r - w / 2, fc="none", ec=self._c(cut), lw=w * self.pt))

    def arc(self, x, y, d, a0, a1, w, cut=False):
        self.ax.add_patch(Arc((x, y), d, d, theta1=a0, theta2=a1, ec=self._c(cut), lw=w * self.pt, capstyle="round"))

    def line(self, pts, w, cut=False, cap="round"):
        xs, ys = zip(*pts)
        self.ax.add_line(Line2D(xs, ys, color=self._c(cut), lw=w * self.pt, solid_capstyle=cap,
                                solid_joinstyle="round"))


# ----------------------------------------------------------------------------- the set
def _user(p, x=0.5, s=1.0, cut=False):
    p.circle(x, 0.5 + 0.22 * s, 0.17 * s, cut)
    p.wedge(x, 0.5 - 0.38 * s, 0.34 * s, 0, 180, cut=cut)


def user(p):
    _user(p)


def users(p):
    _user(p, 0.64, 0.82)
    p.circle(0.40, 0.68, 0.19, cut=True)
    p.wedge(0.40, 0.08, 0.36, 0, 180, cut=True)
    _user(p, 0.38, 0.86)


def agent(p):                                                   # an LLM agent: a robot head
    p.line([(0.5, 0.80), (0.5, 0.90)], 0.06)
    p.circle(0.5, 0.92, 0.05)
    p.rect(0.18, 0.28, 0.64, 0.50, r=0.12)
    p.rect(0.30, 0.44, 0.40, 0.20, r=0.08, cut=True)
    p.circle(0.40, 0.54, 0.05)
    p.circle(0.60, 0.54, 0.05)
    p.rect(0.08, 0.42, 0.06, 0.20, r=0.02)
    p.rect(0.86, 0.42, 0.06, 0.20, r=0.02)
    p.rect(0.34, 0.12, 0.32, 0.12, r=0.03)


def server(p):
    for y in (0.66, 0.40, 0.14):
        p.rect(0.14, y, 0.72, 0.22, r=0.05)
        p.circle(0.27, y + 0.11, 0.035, cut=True)
        p.line([(0.48, y + 0.11), (0.74, y + 0.11)], 0.035, cut=True)


def database(p):
    p.rect(0.18, 0.18, 0.64, 0.62)
    p.ellipse(0.5, 0.18, 0.64, 0.22)
    p.ellipse(0.5, 0.80, 0.64, 0.22)
    p.ellipse(0.5, 0.80, 0.50, 0.11, cut=True)
    for y in (0.40, 0.60):
        p.arc(0.5, y + 0.11, 0.66, 200, 340, 0.035, cut=True)


def document(p):
    p.poly([(0.20, 0.08), (0.80, 0.08), (0.80, 0.68), (0.58, 0.92), (0.20, 0.92)])
    p.poly([(0.58, 0.92), (0.58, 0.68), (0.80, 0.68)], cut=True)
    for y in (0.56, 0.42, 0.28):
        p.line([(0.32, y), (0.68, y)], 0.05, cut=True)


def folder(p):
    p.poly([(0.08, 0.16), (0.08, 0.80), (0.38, 0.80), (0.46, 0.70), (0.92, 0.70), (0.92, 0.16)])
    p.rect(0.08, 0.16, 0.84, 0.46, r=0.04)
    p.line([(0.12, 0.62), (0.88, 0.62)], 0.03, cut=True)


def table(p):
    p.rect(0.10, 0.16, 0.80, 0.68, r=0.05)
    p.rect(0.15, 0.21, 0.70, 0.46, cut=True)
    for y in (0.36, 0.52):
        p.line([(0.15, y), (0.85, y)], 0.04)
    for x in (0.38, 0.62):
        p.line([(x, 0.21), (x, 0.67)], 0.04)


def lock(p):
    p.arc(0.5, 0.60, 0.40, 0, 180, 0.09)
    p.line([(0.30, 0.60), (0.30, 0.48)], 0.09, cap="butt")
    p.line([(0.70, 0.60), (0.70, 0.48)], 0.09, cap="butt")
    p.rect(0.18, 0.08, 0.64, 0.46, r=0.07)
    p.circle(0.5, 0.36, 0.07, cut=True)
    p.rect(0.47, 0.17, 0.06, 0.18, cut=True)


def key(p):
    p.ring(0.30, 0.62, 0.20, 0.10)
    p.line([(0.44, 0.48), (0.86, 0.06)], 0.10, cap="butt")
    p.line([(0.70, 0.22), (0.80, 0.32)], 0.09, cap="butt")
    p.line([(0.60, 0.32), (0.67, 0.39)], 0.09, cap="butt")


def shield(p):
    pts = [(0.5, 0.94), (0.86, 0.80), (0.86, 0.50)]
    pts += [(0.5 + 0.36 * math.cos(math.radians(a)), 0.50 + 0.44 * math.sin(math.radians(a))) for a in range(0, -181, -15)]
    pts += [(0.14, 0.50), (0.14, 0.80)]
    p.poly(pts)
    p.line([(0.33, 0.50), (0.46, 0.37), (0.68, 0.63)], 0.08, cut=True)


def cloud(p):
    p.circle(0.34, 0.44, 0.18)
    p.circle(0.56, 0.56, 0.24)
    p.circle(0.74, 0.42, 0.16)
    p.rect(0.16, 0.26, 0.74, 0.18, r=0.09)


def gear(p):
    pts = []
    for k in range(32):
        a = k * math.pi / 16
        r = 0.42 if (k % 4) in (0, 1) else 0.32
        pts.append((0.5 + r * math.cos(a + math.pi / 32), 0.5 + r * math.sin(a + math.pi / 32)))
    p.poly(pts)
    p.circle(0.5, 0.5, 0.13, cut=True)


def chart(p):
    p.line([(0.10, 0.10), (0.90, 0.10)], 0.05)
    for x, h in ((0.18, 0.30), (0.42, 0.55), (0.66, 0.78)):
        p.rect(x, 0.16, 0.16, h, r=0.03)


def trend(p):
    p.line([(0.10, 0.10), (0.90, 0.10)], 0.05)
    p.line([(0.12, 0.30), (0.38, 0.52), (0.58, 0.40), (0.86, 0.78)], 0.08)
    p.poly([(0.92, 0.88), (0.74, 0.84), (0.90, 0.68)])


def search(p):
    p.ring(0.42, 0.58, 0.28, 0.10)
    p.line([(0.62, 0.38), (0.88, 0.12)], 0.12)


def mail(p):
    p.rect(0.08, 0.20, 0.84, 0.60, r=0.06)
    p.line([(0.14, 0.72), (0.5, 0.44), (0.86, 0.72)], 0.06, cut=True)


def phone(p):
    p.rect(0.28, 0.06, 0.44, 0.88, r=0.08)
    p.rect(0.33, 0.20, 0.34, 0.62, cut=True)
    p.circle(0.5, 0.13, 0.035, cut=True)


def laptop(p):
    p.rect(0.18, 0.32, 0.64, 0.50, r=0.05)
    p.rect(0.23, 0.37, 0.54, 0.40, cut=True)
    p.poly([(0.06, 0.18), (0.94, 0.18), (0.86, 0.30), (0.14, 0.30)])


def globe(p):
    p.circle(0.5, 0.5, 0.43)
    p.circle(0.5, 0.5, 0.35, cut=True)
    p.ax.add_patch(Ellipse((0.5, 0.5), 0.34, 0.74, fc="none", ec=p.fg, lw=0.07 * p.pt))
    p.line([(0.5, 0.14), (0.5, 0.86)], 0.07, cap="butt")
    p.line([(0.14, 0.5), (0.86, 0.5)], 0.07, cap="butt")
    p.arc(0.5, 1.02, 1.0, 232, 308, 0.06)
    p.arc(0.5, -0.02, 1.0, 52, 128, 0.06)


def clock(p):
    p.circle(0.5, 0.5, 0.42)
    p.circle(0.5, 0.5, 0.33, cut=True)
    p.line([(0.5, 0.5), (0.5, 0.74)], 0.07)
    p.line([(0.5, 0.5), (0.66, 0.40)], 0.07)


def calendar(p):
    p.rect(0.12, 0.10, 0.76, 0.72, r=0.06)
    p.rect(0.17, 0.15, 0.66, 0.48, cut=True)
    p.line([(0.32, 0.76), (0.32, 0.92)], 0.07)
    p.line([(0.68, 0.76), (0.68, 0.92)], 0.07)
    for k in range(6):
        p.rect(0.24 + (k % 3) * 0.19, 0.42 - (k // 3) * 0.19, 0.11, 0.11, r=0.02)


def check(p):
    p.circle(0.5, 0.5, 0.42)
    p.line([(0.30, 0.50), (0.44, 0.36), (0.71, 0.64)], 0.09, cut=True)


def cross(p):
    p.circle(0.5, 0.5, 0.42)
    p.line([(0.34, 0.34), (0.66, 0.66)], 0.09, cut=True)
    p.line([(0.34, 0.66), (0.66, 0.34)], 0.09, cut=True)


def warning(p):
    p.poly([(0.5, 0.92), (0.94, 0.12), (0.06, 0.12)])
    p.line([(0.5, 0.64), (0.5, 0.38)], 0.09, cut=True)
    p.circle(0.5, 0.24, 0.05, cut=True)


def info(p):
    p.circle(0.5, 0.5, 0.42)
    p.line([(0.5, 0.26), (0.5, 0.52)], 0.09, cut=True)
    p.circle(0.5, 0.68, 0.055, cut=True)


def bolt(p):
    p.poly([(0.58, 0.94), (0.22, 0.44), (0.46, 0.44), (0.40, 0.06), (0.78, 0.58), (0.54, 0.58)])


def cpu(p):                                                     # a model or a chip
    for k in range(3):
        o = 0.32 + k * 0.18
        for a, b in (((o, 0.06), (o, 0.18)), ((o, 0.82), (o, 0.94)), ((0.06, o), (0.18, o)), ((0.82, o), (0.94, o))):
            p.line([a, b], 0.06, cap="butt")
    p.rect(0.18, 0.18, 0.64, 0.64, r=0.08)
    p.rect(0.33, 0.33, 0.34, 0.34, r=0.04, cut=True)


def card(p):
    p.rect(0.06, 0.20, 0.88, 0.60, r=0.07)
    p.rect(0.06, 0.58, 0.88, 0.10, cut=True)
    p.rect(0.14, 0.30, 0.18, 0.14, r=0.02, cut=True)


def coin(p):                                                    # money: two coins
    p.circle(0.64, 0.62, 0.30)
    p.circle(0.40, 0.40, 0.36, cut=True)
    p.circle(0.40, 0.40, 0.31)
    p.ring(0.40, 0.40, 0.23, 0.04, cut=True)


def camera(p):
    p.rect(0.08, 0.20, 0.84, 0.56, r=0.08)
    p.rect(0.32, 0.72, 0.30, 0.12, r=0.03)
    p.circle(0.5, 0.48, 0.20, cut=True)
    p.circle(0.5, 0.48, 0.12)


def face(p):                                                    # biometrics: a face in a scan frame
    for (x, y), (dx, dy) in (((0.08, 0.92), (1, -1)), ((0.92, 0.92), (-1, -1)), ((0.08, 0.08), (1, 1)),
                             ((0.92, 0.08), (-1, 1))):
        p.line([(x, y + dy * 0.18), (x, y), (x + dx * 0.18, y)], 0.06)
    p.ellipse(0.5, 0.5, 0.48, 0.60)
    p.circle(0.41, 0.56, 0.04, cut=True)
    p.circle(0.59, 0.56, 0.04, cut=True)
    p.arc(0.5, 0.44, 0.22, 200, 340, 0.04, cut=True)


def eye(p):
    p.poly([(0.06, 0.5)] + [(0.5 + 0.44 * math.cos(math.radians(a)), 0.5 + 0.30 * math.sin(math.radians(a)))
                            for a in range(165, 15, -10)] + [(0.94, 0.5)]
           + [(0.5 + 0.44 * math.cos(math.radians(a)), 0.5 + 0.30 * math.sin(math.radians(a))) for a in range(-15, -166, -10)])
    p.circle(0.5, 0.5, 0.17, cut=True)
    p.circle(0.5, 0.5, 0.09)


def code(p):
    p.line([(0.32, 0.72), (0.12, 0.5), (0.32, 0.28)], 0.08)
    p.line([(0.68, 0.72), (0.88, 0.5), (0.68, 0.28)], 0.08)
    p.line([(0.56, 0.80), (0.44, 0.20)], 0.07)


def flag(p):
    p.line([(0.22, 0.06), (0.22, 0.92)], 0.07)
    p.poly([(0.25, 0.90), (0.84, 0.76), (0.25, 0.54)])


def star(p):
    pts = []
    for k in range(10):
        r = 0.44 if k % 2 == 0 else 0.19
        a = math.pi / 2 + k * math.pi / 5
        pts.append((0.5 + r * math.cos(a), 0.47 + r * math.sin(a)))
    p.poly(pts)


def play(p):
    p.circle(0.5, 0.5, 0.42)
    p.poly([(0.40, 0.30), (0.40, 0.70), (0.72, 0.5)], cut=True)


def film(p):
    p.rect(0.12, 0.08, 0.76, 0.84, r=0.05)
    p.rect(0.30, 0.16, 0.40, 0.68, cut=True)
    for k in range(4):
        y = 0.16 + k * 0.19
        p.rect(0.16, y, 0.09, 0.09, cut=True)
        p.rect(0.75, y, 0.09, 0.09, cut=True)


def bell(p):
    p.poly([(0.16, 0.26), (0.84, 0.26), (0.74, 0.40), (0.72, 0.62)]
           + [(0.5 + 0.22 * math.cos(math.radians(a)), 0.62 + 0.22 * math.sin(math.radians(a))) for a in range(0, 181, 15)]
           + [(0.28, 0.62), (0.26, 0.40)])
    p.circle(0.5, 0.17, 0.08)


def network(p):
    pts = [(0.5, 0.80), (0.18, 0.24), (0.82, 0.24)]
    for a in range(3):
        p.line([pts[a], pts[(a + 1) % 3]], 0.05)
    for x, y in pts:
        p.circle(x, y, 0.13)


def arrows(p):                                                  # exchange / sync
    p.line([(0.14, 0.64), (0.78, 0.64)], 0.08, cap="butt")
    p.poly([(0.92, 0.64), (0.72, 0.80), (0.72, 0.48)])
    p.line([(0.86, 0.34), (0.22, 0.34)], 0.08, cap="butt")
    p.poly([(0.08, 0.34), (0.28, 0.50), (0.28, 0.18)])


def upload(p):
    p.line([(0.5, 0.26), (0.5, 0.70)], 0.10, cap="butt")
    p.poly([(0.5, 0.92), (0.26, 0.64), (0.74, 0.64)])
    p.line([(0.14, 0.24), (0.14, 0.10), (0.86, 0.10), (0.86, 0.24)], 0.07)


def download(p):
    p.line([(0.5, 0.88), (0.5, 0.44)], 0.10, cap="butt")
    p.poly([(0.5, 0.22), (0.26, 0.50), (0.74, 0.50)])
    p.line([(0.14, 0.24), (0.14, 0.10), (0.86, 0.10), (0.86, 0.24)], 0.07)


def filter_(p):
    p.poly([(0.08, 0.86), (0.92, 0.86), (0.58, 0.46), (0.58, 0.10), (0.42, 0.20), (0.42, 0.46)])


def layers(p):
    for k, y in enumerate((0.20, 0.38, 0.56)):
        p.poly([(0.5, y + 0.30), (0.92, y + 0.12), (0.5, y - 0.06), (0.08, y + 0.12)], cut=k % 2 == 1)
        if k % 2 == 1:
            p.poly([(0.5, y + 0.24), (0.84, y + 0.12), (0.5, y), (0.16, y + 0.12)])


def book(p):
    p.poly([(0.08, 0.18), (0.08, 0.84), (0.46, 0.76), (0.46, 0.10)])
    p.poly([(0.92, 0.18), (0.92, 0.84), (0.54, 0.76), (0.54, 0.10)])


ICONS = {
    "user": user, "users": users, "agent": agent, "server": server, "database": database, "document": document,
    "folder": folder, "table": table, "lock": lock, "key": key, "shield": shield, "cloud": cloud, "gear": gear,
    "chart": chart, "trend": trend, "search": search, "mail": mail, "phone": phone, "laptop": laptop,
    "globe": globe, "clock": clock, "calendar": calendar, "check": check, "cross": cross, "warning": warning,
    "info": info, "bolt": bolt, "cpu": cpu, "card": card, "coin": coin, "camera": camera, "face": face, "eye": eye,
    "code": code, "flag": flag, "star": star, "play": play, "film": film, "bell": bell, "network": network,
    "arrows": arrows, "upload": upload, "download": download, "filter": filter_, "layers": layers, "book": book,
}


# ----------------------------------------------------------------------------- placing
def draw_icon(fig, name, left, top, size, color=BLUE, bg=SURFACE, zorder=10):
    """Draw icon `name` on `fig` in a size × size inch square whose top-left corner is (left, top) inches from the
    figure's top-left corner; `bg` is the colour of the cut-outs (the colour behind the icon)."""
    if name not in ICONS:
        raise KeyError(f"unknown icon '{name}'; known: {', '.join(sorted(ICONS))}")
    fw, fh = fig.get_size_inches()
    ax = fig.add_axes([left / fw, 1 - (top + size) / fh, size / fw, size / fh], zorder=zorder)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.patch.set_alpha(0)
    ICONS[name](Pen(ax, color, bg, size))
    return ax


def icon_png(name, color, path, size_in=0.5, dpi=400, bg=SURFACE):
    """A transparent PNG of one icon (cut-outs in `bg`), size_in inches square at `dpi`."""
    fig = plt.figure(figsize=(size_in, size_in), dpi=dpi)
    fig.patch.set_alpha(0)
    draw_icon(fig, name, 0, 0, size_in, color, bg)
    fig.savefig(path, dpi=dpi, transparent=True)
    plt.close(fig)
    return path


def contact_sheet(path, cols=8, size=0.6, gap=0.5):
    """Every icon with its name, in the default colour and white on a fill, for review."""
    from palette import ORANGE
    names = sorted(ICONS)
    rows = math.ceil(len(names) / cols)
    cw, ch = size * 2 + gap * 1.2, size + 0.55
    fig = plt.figure(figsize=(cols * cw + 0.4, rows * ch + 0.4))
    fig.patch.set_facecolor(SURFACE)
    for k, n in enumerate(names):
        x, y = 0.3 + (k % cols) * cw, 0.2 + (k // cols) * ch
        draw_icon(fig, n, x, y, size, BLUE)
        bg = fig.add_axes([(x + size + 0.1) / fig.get_figwidth(), 1 - (y + size) / fig.get_figheight(),
                           size / fig.get_figwidth(), size / fig.get_figheight()])
        bg.axis("off")
        bg.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0,rounding_size=0.15", fc=ORANGE, ec="none",
                                    transform=bg.transAxes))
        draw_icon(fig, n, x + size + 0.1 + size * 0.15, y + size * 0.15, size * 0.7, SURFACE, ORANGE, zorder=11)
        fig.text((x + size + 0.05) / fig.get_figwidth(), 1 - (y + size + 0.2) / fig.get_figheight(), n,
                 ha="center", va="center", fontsize=8, color=INK, family="Arial")
    fig.savefig(path, dpi=200, facecolor=SURFACE)
    plt.close(fig)


if __name__ == "__main__":
    contact_sheet(sys.argv[1] if len(sys.argv) > 1 else "icons.png")
