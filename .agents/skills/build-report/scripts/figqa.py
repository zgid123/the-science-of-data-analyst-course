"""Layout check of a rendered matplotlib figure: the faults a reader sees and a colour check cannot.

    issues = figqa.check(fig, min_pt=6.5)     # after drawing, before or after saving
    figqa.report(fig, "out.png")               # prints one WARN line per finding and returns the findings

Findings, each with the text involved:
- overlap: two labels cover each other;
- cut off: a label runs past the edge of the figure;
- crossed: a label without a background plate lies across a line (an arrow, a lifeline, a gridline);
- overflow: text sits in a box but runs past the box's edge;
- covered: a shape drawn above a label hides part of it (a badge, a box, a marker);
- small: text below `min_pt` points at its printed size (6 pt in a report, 10 pt on a slide). A report figure prints
  as wide as build_docx places it (printed_width: the portrait text width, or a landscape page when that prints it
  at least 8 % larger), so a canvas wider than that shrinks, and its text with it;
- empty: a margin with nothing in it wider than 18 % of the figure (shrink the canvas or fill it).
c4kit.Canvas.save, diagrams and charts.save call it; render_figures prints the findings of every figure.
"""

from __future__ import annotations

import matplotlib
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.text import Text
from matplotlib.transforms import Bbox

TOL = 1.5          # pixels of overlap ignored (anti-aliasing, touching edges)
CM = 1 / 2.54


def printed_width(w: float, h: float) -> float:
    """Width in inches at which build_docx prints a w × h inch figure: the portrait text width (16 cm, at most 19 cm
    tall), or a landscape page (24.7 × 15 cm) when that prints it at least 8 % larger."""
    ratio = w / h
    port = min(16.0 * CM, 19.0 * CM * ratio)
    land = min(24.7 * CM, 15.0 * CM * ratio)
    return land if land >= port * 1.08 else port


def _texts(fig, renderer):
    out = []
    for t in fig.findobj(Text):
        if not t.get_visible() or not t.get_text().strip() or (t.get_alpha() == 0):
            continue
        if t.axes is not None and not t.axes.get_visible():
            continue
        try:
            bb = t.get_window_extent(renderer)
        except (RuntimeError, ValueError):
            continue
        if bb.width < 1 or bb.height < 1:
            continue
        out.append((t, bb))
    return out


def _shrink(bb, d):
    return Bbox.from_extents(bb.x0 + d, bb.y0 + d, bb.x1 - d, bb.y1 - d)


def _label(t):
    s = " ".join(t.get_text().split())
    return s if len(s) <= 40 else s[:37] + "…"


def check(fig, min_pt: float = 6.0, empty: float = 0.18, page: bool = True) -> list[str]:
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    fb = fig.bbox
    fw, fh = fig.get_size_inches()
    scale = min(1.0, printed_width(fw, fh) / fw) if page else 1.0
    issues = []
    guides, hidden = _guides(fig)
    texts = [(t, b) for t, b in _texts(fig, r) if id(t) not in hidden]
    legend_texts = {id(t) for lg in fig.findobj(matplotlib.legend.Legend) for t in lg.get_texts()}

    # overlap, cut off and small text
    tiny = []
    for i, (a, ba) in enumerate(texts):
        if ba.x0 < fb.x0 - TOL or ba.y0 < fb.y0 - TOL or ba.x1 > fb.x1 + TOL or ba.y1 > fb.y1 + TOL:
            issues.append(f"cut off: '{_label(a)}' runs past the edge of the figure")
        printed = a.get_fontsize() * scale
        if printed < min_pt - 0.01:
            tiny.append((printed, _label(a)))
        for b, bb in texts[i + 1:]:
            x0, y0 = max(ba.x0, bb.x0), max(ba.y0, bb.y0)
            x1, y1 = min(ba.x1, bb.x1), min(ba.y1, bb.y1)
            if x1 - x0 > TOL and y1 - y0 > TOL:
                small = min(ba.width * ba.height, bb.width * bb.height)
                if (x1 - x0) * (y1 - y0) > 0.08 * small:
                    issues.append(f"overlap: '{_label(a)}' and '{_label(b)}'")

    if tiny:
        low, example = min(tiny)
        issues.append(f"small: {len(tiny)} label(s) print below {min_pt} pt, the smallest at {low:.1f} pt "
                      f"('{example}'); enlarge the text or narrow the canvas"
                      + (f" (it prints at {scale:.0%} of its size)" if scale < 0.99 else ""))

    # labels without a plate crossing lines
    filled = [(p, p.get_window_extent(r)) for p in fig.findobj(matplotlib.patches.Patch)
              if p.get_visible() and p.get_fill() and p.get_facecolor()[3] > 0.5 and p is not fig.patch
              and not (p.axes is not None and p is p.axes.patch)]
    lines = [ln for ln in fig.findobj(Line2D) if ln.get_visible() and len(ln.get_xydata()) > 1
             and ln.get_linewidth() > 0 and ln.get_linestyle() not in ("None", "", " ")]
    for t, bb in texts:
        if t.get_bbox_patch() is not None or id(t) in legend_texts:
            continue
        inner = _shrink(bb, 2)
        if inner.width <= 0 or inner.height <= 0:
            continue
        cx, cy = (bb.x0 + bb.x1) / 2, (bb.y0 + bb.y1) / 2
        covers = [p for p, b in filled if b.x0 <= cx <= b.x1 and b.y0 <= cy <= b.y1]
        for ln in lines:
            if id(ln) in guides or ln.get_gid() == "guide":
                continue
            if any(p.get_zorder() > ln.get_zorder() and p.axes is ln.axes for p in covers):
                continue                               # the line runs under a filled box the text sits on
            path = ln.get_transform().transform_path(ln.get_path())
            if path.intersects_bbox(inner, filled=False):
                issues.append(f"crossed: '{_label(t)}' lies across a line; move it or give it a plate")
                break

    # labels hidden under a shape drawn above them
    for t, bb in texts:
        for p, b in filled:
            if p.axes is not t.axes or p.get_zorder() <= t.get_zorder() or p is t.get_bbox_patch():
                continue
            x0, y0, x1, y1 = max(bb.x0, b.x0), max(bb.y0, b.y0), min(bb.x1, b.x1), min(bb.y1, b.y1)
            if x1 - x0 > 2 and y1 - y0 > 2 and (x1 - x0) * (y1 - y0) > 0.04 * bb.width * bb.height:
                issues.append(f"covered: '{_label(t)}' is partly hidden under a shape drawn above it")
                break

    # text running past the box it sits in
    boxes = [p for p in fig.findobj(lambda a: isinstance(a, (FancyBboxPatch, Rectangle)))
             if p.get_visible() and p.get_facecolor()[3] > 0 and p.get_fill()]
    boxes = [(p, p.get_window_extent(r)) for p in boxes]
    boxes = [(p, b) for p, b in boxes if b.width < fb.width * 0.9 and b.height < fb.height * 0.9]
    for t, bb in texts:
        if t.get_bbox_patch() is not None or id(t) in legend_texts:
            continue
        cx, cy = (bb.x0 + bb.x1) / 2, (bb.y0 + bb.y1) / 2
        holders = [(p, b) for p, b in boxes if b.x0 <= cx <= b.x1 and b.y0 <= cy <= b.y1
                   and p.get_zorder() <= t.get_zorder() and b.width * b.height > bb.width * bb.height * 0.6]
        if not holders:
            continue
        p, b = min(holders, key=lambda pb: pb[1].width * pb[1].height)
        if bb.x0 < b.x0 - TOL or bb.x1 > b.x1 + TOL or bb.y0 < b.y0 - TOL or bb.y1 > b.y1 + TOL:
            issues.append(f"overflow: '{_label(t)}' runs past the edge of its box")

    # empty margins
    drawn = [bb for _, bb in texts]
    for a in fig.findobj(lambda a: isinstance(a, (matplotlib.patches.Patch, Line2D, matplotlib.image.AxesImage,
                                                  matplotlib.collections.Collection))):
        if not a.get_visible() or a is fig.patch or (a.axes is not None and a is a.axes.patch):
            continue
        if isinstance(a, matplotlib.patches.Patch) and a.get_facecolor()[3] == 0 and a.get_edgecolor()[3] == 0:
            continue
        try:
            b = a.get_window_extent(r)
        except (RuntimeError, ValueError, TypeError):
            continue
        if b.width > 0 and b.height > 0 and b.width < fb.width * 1.01 and b.height < fb.height * 1.01:
            drawn.append(b)
    if drawn:
        u = Bbox.union(drawn)
        for side, gap, total in (("left", u.x0 - fb.x0, fb.width), ("right", fb.x1 - u.x1, fb.width),
                                 ("top", fb.y1 - u.y1, fb.height), ("bottom", u.y0 - fb.y0, fb.height)):
            if gap > empty * total:
                issues.append(f"empty: {gap / fig.dpi:.2f} in with nothing at the {side} "
                              f"({gap / total:.0%} of the figure); shrink the canvas")
    return sorted(set(issues))


def _guides(fig):
    """Gridlines and tick marks (recessive guides that labels may cross), and tick labels outside the view, which
    matplotlib keeps but does not draw."""
    lines, hidden = set(), set()
    for ax in fig.axes:
        for axis, k in ((ax.xaxis, 0), (ax.yaxis, 1)):
            lo, hi = sorted(axis.get_view_interval())
            for tick in axis.get_major_ticks() + axis.get_minor_ticks():
                lines.update({id(tick.gridline), id(tick.tick1line), id(tick.tick2line)})
                if not lo - 1e-9 <= tick.get_loc() <= hi + 1e-9:
                    hidden.update({id(tick.label1), id(tick.label2)})
    return lines, hidden


LOG: list[str] = []          # every finding reported in this process (render_figures counts them per task)


def report(fig, path=None, min_pt: float = 6.0, page: bool = True) -> list[str]:
    issues = check(fig, min_pt=min_pt, page=page)
    for i in issues:
        print(f"WARN  figure {path or ''}: {i}")
    LOG.extend(f"{path}: {i}" for i in issues)
    return issues
