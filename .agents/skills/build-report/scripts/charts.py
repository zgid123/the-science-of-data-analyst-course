"""Charts for report figures and slides: one call per chart form, drawn with matplotlib in the shared palette.

Usage in a report figure builder (figures/taskN/…, called with the build language):

    import charts as ch
    fig, ax = ch.figure(6.5, 3.0, lang=lang)             # inches; report type sizes; numbers in the language's style
    ch.bars(ax, ["Model A", "Model B"], {"One step": [0.28, 0.30], "Loop": [0.52, 0.63]}, ref=0.22,
            ref_label="No cleaning")
    ch.save(fig, out)                                     # 300 dpi, then the layout check (figqa)

On a slide, inside slidekit.chart(s, name, x, y, w, h, draw): `ax = ch.axes(fig)` and the same calls; slidekit sets
the slide type sizes and the language.

Forms and the job each does (pick by the data's job, then the form):

| Job | Form |
| :---- | :---- |
| compare magnitudes across categories | bars (grouped for 2–4 series), dots (many categories, or a gap) |
| parts of a whole | stacked (100 % bars, labelled segments) |
| change over an ordered x | lines (end labels), slope (two points in time) |
| relation of two measures | scatter (up to three groups) |
| a matrix of values | heatmap (sequential or diverging ramp, values in the cells) |
| overlap of sets | venn (two or three sets, counts per region) |
| a distribution | hist |
| one headline number | not a chart: a stat tile (slidekit.bignum) or a sentence |

House rules every form follows: one value axis (two measures of different scale make two charts); series colours in
the palette's fixed order, never cycled, and at most six series; a legend for two or more series and none for one;
direct value labels where they are few, so the reader needs no gridline; recessive axes; values and labels in ink,
never in the series colour; thin marks with rounded data ends and a white gap between neighbours.
"""

from __future__ import annotations

import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch, Patch, Rectangle  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

import palette as P  # noqa: E402

CONTEXTS = {             # type sizes (pt) and mark sizes per medium
    "report": dict(base=8.5, small=7.5, value=7.5, lw=1.6, marker=5.0, dpi=300),
    "slide": dict(base=12, small=12, value=12, lw=2.4, marker=8.0, dpi=400),
}
STATE = {"context": "report", "lang": "en"}
PLATE = dict(boxstyle="round,pad=0.12", fc=P.SURFACE, ec="none")      # behind a label that sits on a guide line


def use(context: str | None = None, lang: str | None = None):
    """Set the medium (report or slide) and the language whose number style labels follow."""
    if context:
        STATE["context"] = context
    if lang:
        STATE["lang"] = lang
    c = CONTEXTS[STATE["context"]]
    plt.rcParams.update({"font.family": ["Arial", "Helvetica", "DejaVu Sans"], "font.size": c["base"],
                         "axes.edgecolor": P.GRID, "axes.labelcolor": P.MUTED, "text.color": P.INK,
                         "xtick.color": P.MUTED, "ytick.color": P.MUTED, "axes.titlesize": c["base"],
                         "legend.fontsize": c["small"], "svg.fonttype": "none"})


def size(role="base"):
    return CONTEXTS[STATE["context"]][role]


# ----------------------------------------------------------------------------- numbers
def num(v, digits: int | None = None, pct: bool = False, sign: bool = False) -> str:
    """A number in the language's style: 0.75 / 1,250 in English, 0,75 / 1.250 in Vietnamese; pct adds "%" (the
    value is already a percentage), sign adds "+" to positive values."""
    if digits is None:
        digits = 0 if float(v).is_integer() and abs(v) >= 1 else (1 if abs(v) >= 10 else 2)
    s = f"{v:+,.{digits}f}" if sign else f"{v:,.{digits}f}"
    if STATE["lang"] != "en":
        s = s.replace(",", "\0").replace(".", ",").replace("\0", ".")
    return s + ("%" if pct else "")


# ----------------------------------------------------------------------------- figure and axes
def figure(w: float, h: float, lang: str | None = None, context: str = "report"):
    """A figure of w × h inches with one axes, in the report's (or a slide's) type sizes."""
    use(context, lang)
    fig = plt.figure(figsize=(w, h), dpi=size("dpi"))
    fig.patch.set_facecolor(P.SURFACE)
    return fig, axes(fig)


def axes(fig, rect=None):
    """One axes in `fig` with room for a legend row above and tick labels below (rect in figure fractions)."""
    w, h = fig.get_size_inches()
    top = 0.42 / h                                      # a legend row
    bottom = 0.42 / h
    left = 0.1 / w
    ax = fig.add_axes(rect or [left, bottom, 1 - left - 0.1 / w, 1 - top - bottom])
    ax._kit = rect is None                              # fit() sizes this plot area to its content
    style(ax)
    return ax


def style(ax, grid: str | None = None, left: bool = False):
    """Recessive axes: no frame but a light baseline, muted ticks without marks, an optional light grid."""
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(side == "left" and left)
    for side in ("bottom", "left"):
        ax.spines[side].set_color(P.GRID)
    ax.tick_params(length=0, colors=P.MUTED, labelsize=size("small"), pad=4)
    if grid:
        ax.grid(axis=grid, color=P.GRID, lw=0.6)
        ax.set_axisbelow(True)
    ax.set_facecolor("none")


def ticks(axis, pct=False):
    """Tick labels in the language's number style, every label with the same number of decimals."""
    def fmt(v, _):
        locs = [x for x in axis.get_majorticklocs()]
        d = 0
        for x in locs:
            while d < 3 and abs(round(x, d) - x) > 1e-9:
                d += 1
        return num(v, d, pct)
    axis.set_major_formatter(matplotlib.ticker.FuncFormatter(fmt))


def legend(ax, items, kind="patch", loc="above", ncol=None):
    """A one-row legend above the plot, left-aligned: items are (label, colour) or (label, colour, linestyle)."""
    handles = []
    for it in items:
        label, color = it[0], it[1]
        if kind == "line":
            handles.append(Line2D([], [], color=color, lw=size("lw"), ls=it[2] if len(it) > 2 else "-", label=label))
        else:
            handles.append(Patch(fc=color, ec="none", label=label))
    if loc == "above":
        return ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.02), ncol=ncol or len(handles),
                         frameon=False, handlelength=1.4 if kind == "line" else 0.9, handleheight=0.9,
                         columnspacing=1.4, borderaxespad=0, fontsize=size("small"))
    return ax.legend(handles=handles, loc=loc, frameon=False, fontsize=size("small"))


def _colors(names, colors):
    if colors is None:
        return dict(zip(names, P.series(len(names))))
    if isinstance(colors, dict):
        return {n: colors.get(n, P.OTHER) for n in names}
    return dict(zip(names, colors))


def _bar(ax, x, base, width, value, color, horizontal, radius_pt=3.0):
    """One bar from `base` to `value` with its data end rounded and its baseline end square."""
    fig = ax.figure
    bb = ax.get_position()
    fw, fh = fig.get_size_inches()
    x0, x1 = ax.get_xlim()
    y0, y1 = ax.get_ylim()
    ux = (x1 - x0) / (bb.width * fw * 72)              # data units per point, x
    uy = (y1 - y0) / (bb.height * fh * 72)             # data units per point, y
    if horizontal:
        length, thick, ul, ut = value - base, width, ux, uy
    else:
        length, thick, ul, ut = value - base, width, uy, ux
    r_pt = min(radius_pt, abs(length) / ul / 2, thick / ut / 2) if length else 0
    ext = r_pt * ul * (1 if length >= 0 else -1)        # extend past the baseline by the radius, then clip it off
    if horizontal:
        xy, w, h = (min(base - ext, value), x - width / 2), abs(length) + abs(ext), width
        clip = Rectangle((min(base, value), x - width / 2), abs(length), width, transform=ax.transData)
    else:
        xy, w, h = (x - width / 2, min(base - ext, value)), width, abs(length) + abs(ext)
        clip = Rectangle((x - width / 2, min(base, value)), width, abs(length), transform=ax.transData)
    p = FancyBboxPatch(xy, w, h, boxstyle=f"round,pad=0,rounding_size={r_pt * ut}", mutation_aspect=ul / ut,
                       fc=color, ec="none", lw=0, zorder=3)
    ax.add_patch(p)
    p.set_clip_path(clip)
    if not hasattr(ax, "_kit_bars"):
        ax._kit_bars = []
    ax._kit_bars.append((p, (x, base, width, value, color, horizontal, radius_pt)))
    return p


# ----------------------------------------------------------------------------- forms
def bars(ax, categories, series: dict, *, horizontal=False, ref=None, ref_label=None, labels="all", digits=None,
         pct=False, colors=None, limit=None, show_legend=True, group_gap=0.28):
    """Grouped bars: one group per category, one bar per series (2–4 series read best; one series takes slot 1 and
    no legend). `ref` draws a dashed reference line (a baseline value) labelled `ref_label`; labels = "all", "max"
    (the largest bar of each group) or "none"; `limit` fixes the value axis maximum."""
    names = list(series)
    cols = _colors(names, colors)
    n, k = len(categories), len(names)
    width = (1 - group_gap) / k
    gap = 0.03 if k > 1 else 0                         # a white gap between neighbouring bars
    top = max(max(v) for v in series.values())
    top = max(top, ref or 0)
    lo = min(0, min(min(v) for v in series.values()))
    vmax = limit or top * 1.16
    pos = list(range(n))
    if horizontal:
        ax.set_ylim(n - 0.5, -0.5)
        ax.set_xlim(lo, vmax)
        ax.set_yticks(pos, categories)
        ax.set_xticks([])
        ax.spines["bottom"].set_visible(False)
    else:
        ax.set_xlim(-0.5, n - 0.5)
        ax.set_ylim(lo, vmax)
        ax.set_xticks(pos, categories)
        ax.set_yticks([])
    for j, name in enumerate(names):
        for i, v in enumerate(series[name]):
            c = i - (1 - group_gap) / 2 + width * (j + 0.5)
            _bar(ax, c, 0, width - gap, v, cols[name], horizontal)
            show = labels == "all" or (labels == "max" and v == max(series[m][i] for m in names))
            if show:
                txt = num(v, digits, pct)
                bold = labels == "max" or (k > 1 and v == max(series[m][i] for m in names))
                if horizontal:
                    ax.annotate(txt, (v, c), xytext=(3, 0), textcoords="offset points", ha="left", va="center",
                                fontsize=size("value"), color=P.INK, fontweight="bold" if bold else "normal")
                else:
                    ax.annotate(txt, (c, v), xytext=(0, 2.5), textcoords="offset points", ha="center",
                                va="bottom", fontsize=size("value"), color=P.INK,
                                fontweight="bold" if bold else "normal")
    items = [(nm, cols[nm]) for nm in names] if k > 1 else []
    if ref is not None:
        (ax.axvline if horizontal else ax.axhline)(ref, color=P.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=4)
        if ref_label:
            items.append((ref_label, P.MUTED, (0, (3, 2))))
    if show_legend and items:
        _mixed_legend(ax, items)
    return ax


def _mixed_legend(ax, items):
    handles = []
    for it in items:
        if len(it) > 2:
            handles.append(Line2D([], [], color=it[1], lw=1.2, ls=it[2], label=it[0]))
        else:
            handles.append(Patch(fc=it[1], ec="none", label=it[0]))
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.02), ncol=len(handles), frameon=False,
              handlelength=1.4, handleheight=0.9, columnspacing=1.4, borderaxespad=0, fontsize=size("small"))


def stacked(ax, categories, parts: dict, *, percent=True, horizontal=True, labels=True, min_label=0.07, digits=0,
            colors=None, show_legend=True):
    """100 % stacked bars (percent=True) or absolute stacks: parts maps a part name to its value per category.
    Segment labels sit inside segments that are wide enough (`min_label` of the whole), in ink or white by fill."""
    names = list(parts)
    cols = _colors(names, colors)
    n = len(categories)
    totals = [sum(parts[p][i] for p in names) for i in range(n)]
    vmax = 100 if percent else max(totals) * 1.05
    pos = list(range(n))
    if horizontal:
        ax.set_ylim(n - 0.5, -0.5)
        ax.set_xlim(0, vmax)
        ax.set_yticks(pos, categories)
        ax.set_xticks([])
        ax.spines["bottom"].set_visible(False)
    else:
        ax.set_xlim(-0.5, n - 0.5)
        ax.set_ylim(0, vmax)
        ax.set_xticks(pos, categories)
        ax.set_yticks([])
    for i in range(n):
        acc = 0.0
        for nm in names:
            v = parts[nm][i] / totals[i] * 100 if percent else parts[nm][i]
            if horizontal:
                ax.barh(i, v, left=acc, height=0.62, color=cols[nm], edgecolor=P.SURFACE, lw=1.2, zorder=3)
                cx, cy = acc + v / 2, i
            else:
                ax.bar(i, v, bottom=acc, width=0.62, color=cols[nm], edgecolor=P.SURFACE, lw=1.2, zorder=3)
                cx, cy = i, acc + v / 2
            if labels and v >= min_label * vmax:
                ax.text(cx, cy, num(v, digits, pct=percent), ha="center", va="center", fontsize=size("value"),
                        color=P.text_on(cols[nm]), zorder=4)
            acc += v
    if show_legend and len(names) > 1:
        legend(ax, [(nm, cols[nm]) for nm in names])
    return ax


def dots(ax, categories, series: dict, *, ref=None, ref_label=None, connect=True, digits=None, pct=False,
         colors=None, labels=True, show_legend=True, limit=None):
    """A dot plot with categories down the side: one dot per series; two series joined by a line show the gap
    (a dumbbell). Suits many categories and small differences that bars would hide."""
    names = list(series)
    cols = _colors(names, colors)
    n = len(categories)
    vals = [v for s in series.values() for v in s]
    lo, hi = min(vals + ([ref] if ref is not None else [])), max(vals + ([ref] if ref is not None else []))
    pad = (hi - lo) * 0.12 or 1
    ax.set_xlim(limit[0] if limit else lo - pad, limit[1] if limit else hi + pad)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_yticks(range(n), categories)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    for i in range(n):
        row = [series[nm][i] for nm in names]
        ax.axhline(i, color=P.GRID, lw=0.6, zorder=1, gid="guide")
        if connect and len(names) > 1:
            ax.plot([min(row), max(row)], [i, i], color=P.MUTED, lw=size("lw") * 0.9, zorder=2,
                    solid_capstyle="round")
        for nm in names:
            v = series[nm][i]
            ax.plot(v, i, "o", ms=size("marker") * 1.3, color=cols[nm], mec=P.SURFACE, mew=1.2, zorder=3)
        if labels:
            for nm in names:
                v = series[nm][i]
                right = v == max(row)
                ax.annotate(num(v, digits, pct), (v, i), xytext=(7 if right else -7, 0), textcoords="offset points",
                            ha="left" if right else "right", va="center", fontsize=size("value"), color=P.INK,
                            bbox=PLATE)
    if ref is not None:
        ax.axvline(ref, color=P.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    if show_legend:
        items = [(nm, cols[nm]) for nm in names] if len(names) > 1 else []
        if ref is not None and ref_label:
            items.append((ref_label, P.MUTED, (0, (3, 2))))
        if items:
            _mixed_legend(ax, items)
    return ax


def _spread(ax, ys, gap_pt):
    """Move label y positions (data units) apart to at least gap_pt points, keeping their order and mean."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    disp = [ax.transData.transform((0, ys[i]))[1] for i in order]
    gap = gap_pt * ax.figure.dpi / 72
    for _ in range(50):
        moved = False
        for a in range(1, len(disp)):
            if disp[a] - disp[a - 1] < gap:
                push = (gap - (disp[a] - disp[a - 1])) / 2
                disp[a - 1] -= push
                disp[a] += push
                moved = True
        if not moved:
            break
    out = list(ys)
    inv = ax.transData.inverted()
    for k, i in enumerate(order):
        out[i] = inv.transform((0, disp[k]))[1]
    return out


def lines(ax, x, series: dict, *, end_labels=True, markers=True, digits=None, pct=False, colors=None,
          highlight=None, xlabel=None, ylabel=None, grid=True, show_legend=None):
    """Lines over an ordered x, each labelled at its end with its name and last value (no legend needed); with
    `highlight`, the named series keep their colour and the rest turn grey for context."""
    names = list(series)
    cols = _colors(names, colors)
    if highlight:
        keep = {highlight} if isinstance(highlight, str) else set(highlight)
        cols = {nm: (cols[nm] if nm in keep else P.OTHER) for nm in names}
    xs = list(range(len(x))) if isinstance(x[0], str) else list(x)
    for nm in names:
        z = 3 if not highlight or cols[nm] != P.OTHER else 2
        ax.plot(xs, series[nm], color=cols[nm], lw=size("lw"), zorder=z, solid_capstyle="round",
                marker="o" if markers else None, ms=size("marker"), mec=P.SURFACE, mew=1.0)
    if isinstance(x[0], str):
        ax.set_xticks(xs, x)
    style(ax, grid="y" if grid else None)
    ticks(ax.yaxis, pct)
    if not isinstance(x[0], str):
        ticks(ax.xaxis)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=size("small"))
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=size("small"))
    if end_labels:
        span = xs[-1] - xs[0]
        ax.set_xlim(xs[0] - span * 0.04, xs[-1] + span * 0.04)
        ax.figure.canvas.draw()
        ends = _spread(ax, [series[nm][-1] for nm in names], size("value") * 1.3)
        for nm, y in zip(names, ends):
            ax.annotate(f"{nm} {num(series[nm][-1], digits, pct)}", (xs[-1], y), xytext=(8, 0),
                        textcoords="offset points", ha="left", va="center", fontsize=size("value"),
                        color=P.INK, annotation_clip=False, bbox=PLATE)
    elif show_legend is not False and len(names) > 1:
        legend(ax, [(nm, cols[nm]) for nm in names], kind="line")
    return ax


def slope(ax, left: str, right: str, series: dict, *, digits=None, pct=False, colors=None, highlight=None):
    """Two points in time per series joined by a line, labelled on both sides: before and after at a glance."""
    names = list(series)
    cols = _colors(names, colors)
    if highlight:
        keep = {highlight} if isinstance(highlight, str) else set(highlight)
        cols = {nm: (cols[nm] if nm in keep else P.OTHER) for nm in names}
    vals = [v for a, b in series.values() for v in (a, b)]
    pad = (max(vals) - min(vals)) * 0.08 or 1
    ax.set_ylim(min(vals) - pad, max(vals) + pad)
    ax.set_xlim(-0.05, 1.05)
    for side in ("bottom", "left", "right", "top"):
        ax.spines[side].set_visible(False)
    ax.set_xticks([0, 1], [left, right])
    ax.set_yticks([])
    ax.xaxis.tick_top()
    for xv in (0, 1):
        ax.axvline(xv, color=P.GRID, lw=0.8, zorder=1)
    for nm in names:
        a, b = series[nm]
        ax.plot([0, 1], [a, b], color=cols[nm], lw=size("lw"), marker="o", ms=size("marker"), mec=P.SURFACE,
                zorder=3)
    ax.figure.canvas.draw()
    ys_l = _spread(ax, [series[nm][0] for nm in names], size("value") * 1.3)
    ys_r = _spread(ax, [series[nm][1] for nm in names], size("value") * 1.3)
    for nm, yl, yr in zip(names, ys_l, ys_r):
        a, b = series[nm]
        ax.text(-0.04, yl, f"{nm} {num(a, digits, pct)}", ha="right", va="center", fontsize=size("value"),
                color=P.INK)
        ax.text(1.04, yr, num(b, digits, pct), ha="left", va="center", fontsize=size("value"), color=P.INK,
                fontweight="bold")
    return ax


def scatter(ax, groups: dict, *, xlabel=None, ylabel=None, labels=None, colors=None, digits=None, show_legend=True):
    """Points of up to three groups ({name: [(x, y), …]}); `labels` maps (x, y) to a short name shown beside it.
    Any two points can sit side by side, so only the first three palette slots are used (they stay apart for every
    reader); more groups go to small multiples."""
    names = list(groups)
    if len(names) > 3:
        raise ValueError("scatter: at most three groups; use small multiples for more")
    cols = _colors(names, colors)
    for nm in names:
        xs, ys = zip(*groups[nm])
        ax.scatter(xs, ys, s=(size("marker") * 1.4) ** 2, color=cols[nm], edgecolor=P.SURFACE, lw=1.0, zorder=3)
    style(ax, grid="both", left=True)
    for (x, y), text in (labels or {}).items():
        ax.annotate(text, (x, y), xytext=(5, 4), textcoords="offset points", fontsize=size("value"), color=P.INK)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=size("small"))
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=size("small"))
    ticks(ax.xaxis)
    ticks(ax.yaxis)
    if show_legend and len(names) > 1:
        legend(ax, [(nm, cols[nm]) for nm in names])
    return ax


def heatmap(ax, rows, cols, values, *, ramp="sequential", center=None, digits=None, pct=False, hue=P.BLUE,
            labels=True, vmin=None, vmax=None):
    """A matrix of values as coloured cells with the value written in each (ink or white by the cell's fill).
    ramp="sequential" for magnitude (one hue, light to dark), "diverging" for values around `center`."""
    flat = [v for r in values for v in r if v is not None]
    lo, hi = vmin if vmin is not None else min(flat), vmax if vmax is not None else max(flat)
    if ramp == "diverging":
        c = center if center is not None else 0
        span = max(hi - c, c - lo) or 1
        lo, hi = c - span, c + span
        colors = P.diverging(9)
    else:
        colors = P.sequential(7, hue)
    cm = P.cmap(colors)
    for i, r in enumerate(values):
        for j, v in enumerate(r):
            if v is None:
                fill = P.SOFT
            else:
                fill = matplotlib.colors.to_hex(cm((v - lo) / ((hi - lo) or 1)))
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fc=fill, ec=P.SURFACE, lw=1.5, zorder=2))
            if labels and v is not None:
                ax.text(j, i, num(v, digits, pct), ha="center", va="center", fontsize=size("value"),
                        color=P.text_on(fill), zorder=3)
    ax.set_xlim(-0.5, len(cols) - 0.5)
    ax.set_ylim(len(rows) - 0.5, -0.5)
    ax.set_xticks(range(len(cols)), cols)
    ax.set_yticks(range(len(rows)), rows)
    ax.xaxis.tick_top()
    for side in ("bottom", "left", "right", "top"):
        ax.spines[side].set_visible(False)
    ax.set_aspect("auto")
    return ax


def venn(ax, sets: list[str], counts: dict, *, colors=None, digits=None):
    """Two or three overlapping sets with a count in each region. counts keys name the sets a region belongs to:
    for sets ["A", "B", "C"], "A" is A only, "AB" is A and B but not C, "ABC" is all three (letters by position)."""
    k = len(sets)
    if k not in (2, 3):
        raise ValueError("venn: two or three sets")
    cols = colors or P.series(k)
    if k == 2:
        centers = [(-0.5, 0), (0.5, 0)]
        spots = {"A": (-0.85, 0), "B": (0.85, 0), "AB": (0, 0)}
        name_at = [(-0.5, 1.12, "center"), (0.5, 1.12, "center")]
    else:
        centers = [(0, 0.55), (-0.55, -0.4), (0.55, -0.4)]
        spots = {"A": (0, 1.05), "B": (-0.95, -0.7), "C": (0.95, -0.7), "AB": (-0.55, 0.3), "AC": (0.55, 0.3),
                 "BC": (0, -0.75), "ABC": (0, 0)}
        name_at = [(0, 1.72, "center"), (-1.25, -1.5, "center"), (1.25, -1.5, "center")]
    for (cx, cy), c in zip(centers, cols):
        ax.add_patch(Circle((cx, cy), 1.0, fc=c, alpha=0.16, ec="none", zorder=1))
        ax.add_patch(Circle((cx, cy), 1.0, fc="none", ec=c, lw=1.6, zorder=2))
    for key, (x, y) in spots.items():
        if key in counts:
            ax.text(x, y, num(counts[key], digits), ha="center", va="center", fontsize=size("base") + 1,
                    color=P.INK, fontweight="bold" if len(key) == k else "normal", zorder=3)
    for (x, y, ha), name, c in zip(name_at, sets, cols):
        ax.text(x, y, name, ha=ha, va="center", fontsize=size("base"), color=P.INK, fontweight="bold", zorder=3)
    ax.set_xlim(-2.1, 2.1)
    ax.set_ylim(-1.9 if k == 3 else -1.4, 2.0 if k == 3 else 1.4)
    ax.set_aspect("equal")
    ax.axis("off")
    return ax


def hist(ax, values, *, bins=12, color=P.BLUE, ref=None, ref_label=None, xlabel=None, digits=None):
    """A histogram of one distribution, with an optional dashed reference (a mean, a threshold)."""
    ax.hist(values, bins=bins, color=color, edgecolor=P.SURFACE, lw=1.0, zorder=3)
    style(ax, grid="y")
    ticks(ax.xaxis)
    ticks(ax.yaxis)
    if ref is not None:
        ax.axvline(ref, color=P.INK, lw=1.0, ls=(0, (4, 3)), zorder=4)
        if ref_label:
            ax.set_ylim(0, ax.get_ylim()[1] * 1.14)
            ax.annotate(ref_label, (ref, 1), xycoords=("data", "axes fraction"), xytext=(4, -1),
                        textcoords="offset points", ha="left", va="top", fontsize=size("value"), color=P.INK,
                        bbox=PLATE, zorder=5)
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=size("small"))
    return ax


def callout(ax, xy, text, xytext, *, color=P.INK):
    """A short note joined to a point of the chart by a thin leader (an annotation that explains one mark)."""
    ax.annotate(text, xy, xytext=xytext, textcoords="data", fontsize=size("value"), color=color, ha="left",
                va="center", arrowprops=dict(arrowstyle="-", color=P.MUTED, lw=0.8, shrinkA=2, shrinkB=3),
                bbox=dict(boxstyle="round,pad=0.25", fc=P.SURFACE, ec=P.LINE, lw=0.6), zorder=6)


# ----------------------------------------------------------------------------- output
def fit(fig, pad=0.06):
    """Size the plot area of a one-chart figure so that everything it draws (tick labels, legend, value and end
    labels) fits inside the figure with `pad` inches to spare, and nothing more; the figure keeps its size, so text
    keeps its printed size. Rounded bars are redrawn for the new shape."""
    axs = [a for a in fig.axes if a.get_label() != "icon"]
    if len(axs) != 1 or not getattr(axs[0], "_kit", False):
        return
    ax = axs[0]
    w, h = fig.get_size_inches()
    for _ in range(4):
        fig.canvas.draw()
        tb = ax.get_tightbbox(fig.canvas.get_renderer())
        pos = ax.get_position()
        x0, y0 = tb.x0 / fig.dpi / w, tb.y0 / fig.dpi / h
        x1, y1 = tb.x1 / fig.dpi / w, tb.y1 / fig.dpi / h
        nx0 = pos.x0 + (pad / w - x0)
        nx1 = pos.x1 + ((1 - pad / w) - x1)
        ny0 = pos.y0 + (pad / h - y0)
        ny1 = pos.y1 + ((1 - pad / h) - y1)
        if max(abs(nx0 - pos.x0), abs(nx1 - pos.x1), abs(ny0 - pos.y0), abs(ny1 - pos.y1)) < 0.002:
            break
        ax.set_position([nx0, ny0, max(nx1 - nx0, 0.05), max(ny1 - ny0, 0.05)])
    for patch, spec in getattr(ax, "_kit_bars", []):
        patch.remove()
    specs = [spec for _, spec in getattr(ax, "_kit_bars", [])]
    ax._kit_bars = []
    for spec in specs:
        _bar(ax, *spec)


def save(fig, path, check=True):
    """Fit the plot area, write the figure at the medium's resolution and run the layout check; returns its
    findings."""
    fit(fig)
    fig._figqa_done = check
    fig.savefig(path, dpi=size("dpi"), facecolor=P.SURFACE)
    issues = []
    if check:
        import figqa
        report = STATE["context"] == "report"
        issues = figqa.report(fig, path, min_pt=6.0 if report else 10, page=report)

    plt.close(fig)
    return issues
