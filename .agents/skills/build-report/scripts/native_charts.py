"""Native PowerPoint charts: editable in PowerPoint (right-click, Edit Data), styled like the kit's image charts.

    import native_charts as nc
    nc.bars(slide, x, y, w, h, ["Model A", "Model B"], {"Baseline": [0.28, 0.30], "Method": [0.52, 0.63]},
            ref=0.22, ref_label="No cleaning", lang="vi")
    nc.stacked(slide, x, y, w, h, categories, {"Correct": [...], "Wrong": [...]})
    nc.lines(slide, x, y, w, h, x_labels, {"Selector": [...], "Upper bound": [...]})
    nc.scatter(slide, x, y, w, h, {"Open": [(7, 52), (13, 58)], "Closed": [(100, 72)]})
    nc.doughnut(slide, x, y, w, h, {"Correct": 62, "Wrong join": 18, "Other": 20})

When to use which: a native chart keeps its data inside the deck, so a presenter can change a number in PowerPoint
and the chart follows; it renders with PowerPoint's own engine, which some viewers (quick-look previews, older
PDF exports) draw softer than an image. An image chart (charts.py through slidekit.chart) looks the same in every
viewer and supports every form (heatmap, Venn, slope, dot plot). Choose native for figures the presenter may edit or
re-use, images where the exact look matters most.

Conventions shared with charts.py: palette series in fixed order (at most six), value labels written by the kit in
the build language (0,52 in Vietnamese, whatever the viewer's locale), no gridlines, a hidden value axis when every
bar carries its label, a legend above the plot for two or more series, Arial at the slide's sizes. The plot area is
fixed inside the frame (manual layout), so a reference value can be drawn exactly as a dashed native line.
"""

from __future__ import annotations

from lxml import etree
from pptx.chart.data import CategoryChartData, XyChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

import palette as P

I = lambda v: Emu(int(round(v * 914400)))               # noqa: E731
RGB = lambda c: RGBColor.from_string(c.lstrip("#").upper())   # noqa: E731
SIZES = {"label": 12, "axis": 12, "legend": 12}
PLOT = {"x": 0.02, "y": 0.14, "w": 0.96, "h": 0.74}     # plot area inside the frame, as fractions


def num(v, digits=None, lang="en", pct=False):
    """A number in the language's style (the same rule as charts.num)."""
    if digits is None:
        digits = 0 if float(v).is_integer() and abs(v) >= 1 else (1 if abs(v) >= 10 else 2)
    s = f"{v:,.{digits}f}"
    if lang != "en":
        s = s.replace(",", "\0").replace(".", ",").replace("\0", ".")
    return s + ("%" if pct else "")


def _font(font, size, color=P.INK, bold=False):
    font.name = "Arial"
    font.size = Pt(size)
    font.bold = bold
    font.color.rgb = RGB(color)


def _layout(chart, plot=None):
    """Fix the plot area inside the frame, so positions on the chart are known."""
    plot = plot or PLOT
    pa = chart._chartSpace.find(qn("c:chart")).find(qn("c:plotArea"))
    old = pa.find(qn("c:layout"))
    if old is not None:
        pa.remove(old)
    layout = etree.SubElement(pa, qn("c:layout"))
    pa.remove(layout)
    pa.insert(0, layout)
    ml = etree.SubElement(layout, qn("c:manualLayout"))
    for tag, val in (("c:layoutTarget", "inner"), ("c:xMode", "edge"), ("c:yMode", "edge"), ("c:x", plot["x"]),
                     ("c:y", plot["y"]), ("c:w", plot["w"]), ("c:h", plot["h"])):
        etree.SubElement(ml, qn(tag)).set("val", str(val))


def _legend(chart, show, size=None):
    chart.has_legend = show
    if show:
        chart.legend.position = XL_LEGEND_POSITION.TOP
        chart.legend.include_in_layout = False
        _font(chart.legend.font, size or SIZES["legend"])


def _clean_axis(axis, visible=True, size=None, gridlines=False):
    axis.has_major_gridlines = gridlines
    axis.has_minor_gridlines = False
    axis.visible = visible
    if visible:
        _font(axis.tick_labels.font, size or SIZES["axis"], P.MUTED)
        axis.format.line.color.rgb = RGB(P.GRID)


def _colors(names, colors):
    if colors is None:
        return P.series(len(names))
    if isinstance(colors, dict):
        return [colors.get(n, P.OTHER) for n in names]
    return list(colors)


def _labels(series, values, digits, lang, pct, size, color=P.INK, bold_max=None, position=None):
    """Write each point's label text in the build language (PowerPoint would format by the viewer's locale)."""
    for k, v in enumerate(values):
        if v is None:
            continue
        dl = series.points[k].data_label
        tf = dl.text_frame
        tf.text = num(v, digits, lang, pct)
        _font(tf.paragraphs[0].runs[0].font, size, color, bold=bold_max is not None and v == bold_max[k])
        if position is not None:
            dl.position = position


def _frame_to_plot(x, y, w, h, plot=None):
    plot = plot or PLOT
    return x + w * plot["x"], y + h * plot["y"], w * plot["w"], h * plot["h"]


def bars(slide, x, y, w, h, categories, series: dict, *, horizontal=False, ref=None, ref_label=None, labels=True,
         digits=None, pct=False, colors=None, limit=None, lang="en", gap=60, overlap=-8):
    """Clustered columns (or bars with horizontal=True): one group per category, one bar per series. `ref` draws a
    dashed native line at that value with `ref_label` in the legend row; `limit` fixes the value axis maximum."""
    names = list(series)
    data = CategoryChartData()
    data.categories = categories
    for n in names:
        data.add_series(n, series[n])
    kind = XL_CHART_TYPE.BAR_CLUSTERED if horizontal else XL_CHART_TYPE.COLUMN_CLUSTERED
    frame = slide.shapes.add_chart(kind, I(x), I(y), I(w), I(h), data)
    chart = frame.chart
    _layout(chart)
    plot = chart.plots[0]
    plot.gap_width, plot.overlap = gap, overlap if len(names) > 1 else 0
    plot.vary_by_categories = False
    top = max(max(v for v in s if v is not None) for s in series.values())
    vmax = limit or (max(top, ref or 0) * 1.15)
    va = chart.value_axis
    va.minimum_scale, va.maximum_scale = 0, vmax
    _clean_axis(va, visible=not labels)
    _clean_axis(chart.category_axis)
    if horizontal:
        chart.category_axis.reverse_order = True
    maxes = [max(series[n][i] for n in names) for i in range(len(categories))] if len(names) > 1 else None
    for s, c, n in zip(plot.series, _colors(names, colors), names):
        s.format.fill.solid()
        s.format.fill.fore_color.rgb = RGB(c)
        s.format.line.fill.background()
        if labels:
            _labels(s, series[n], digits, lang, pct, SIZES["label"], bold_max=maxes,
                    position=XL_LABEL_POSITION.OUTSIDE_END)
    _legend(chart, len(names) > 1 or ref_label is not None)
    if ref is not None:
        px, py, pw, ph = _frame_to_plot(x, y, w, h)
        if horizontal:
            rx = px + pw * ref / vmax
            ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(rx), I(py), I(rx), I(py + ph))
        else:
            ry = py + ph * (1 - ref / vmax)
            ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(px), I(ry), I(px + pw), I(ry))
        ln.line.color.rgb = RGB(P.MUTED)
        ln.line.width = Pt(1.5)
        ln.line.dash_style = MSO_LINE_DASH_STYLE.DASH
        if ref_label:
            _ref_key(slide, x, y, w, ref_label, len(names))
    return frame


def _ref_key(slide, x, y, w, label, n_series):
    """A dashed key with the reference label at the right end of the legend row."""
    from scene import text_width
    tw = text_width(label, SIZES["legend"]) + 0.1
    kx = x + w - tw - 0.55
    ky = y + 0.18
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, I(kx), I(ky), I(kx + 0.4), I(ky))
    ln.line.color.rgb = RGB(P.MUTED)
    ln.line.width = Pt(1.5)
    ln.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    box = slide.shapes.add_textbox(I(kx + 0.48), I(ky - 0.13), I(tw), I(0.26))
    tf = box.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.text = label
    _font(tf.paragraphs[0].runs[0].font, SIZES["legend"], P.INK)


def stacked(slide, x, y, w, h, categories, parts: dict, *, percent=True, horizontal=True, labels=True, digits=0,
            colors=None, lang="en", min_label=0.07):
    """100 % (percent=True) or absolute stacked bars; segment labels in white or ink by the fill, shown when the
    segment is at least `min_label` of the whole."""
    names = list(parts)
    totals = [sum(parts[n][i] for n in names) for i in range(len(categories))]
    vals = {n: [parts[n][i] / totals[i] * 100 if percent else parts[n][i] for i in range(len(categories))]
            for n in names}
    data = CategoryChartData()
    data.categories = categories
    for n in names:
        data.add_series(n, vals[n])
    kind = (XL_CHART_TYPE.BAR_STACKED_100 if horizontal else XL_CHART_TYPE.COLUMN_STACKED_100) if percent else \
        (XL_CHART_TYPE.BAR_STACKED if horizontal else XL_CHART_TYPE.COLUMN_STACKED)
    frame = slide.shapes.add_chart(kind, I(x), I(y), I(w), I(h), data)
    chart = frame.chart
    _layout(chart)
    plot = chart.plots[0]
    plot.gap_width, plot.overlap = 50, 100
    _clean_axis(chart.value_axis, visible=False)
    _clean_axis(chart.category_axis)
    if horizontal:
        chart.category_axis.reverse_order = True
    vmax = 100 if percent else max(totals)
    for s, c, n in zip(plot.series, _colors(names, colors), names):
        s.format.fill.solid()
        s.format.fill.fore_color.rgb = RGB(c)
        s.format.line.color.rgb = RGB(P.SURFACE)
        s.format.line.width = Pt(1.5)
        if labels:
            shown = [v if v >= min_label * vmax else None for v in vals[n]]
            _labels(s, shown, digits, lang, percent, SIZES["label"], P.text_on(c),
                    position=XL_LABEL_POSITION.CENTER)
    _legend(chart, len(names) > 1)
    return frame


def lines(slide, x, y, w, h, x_labels, series: dict, *, digits=None, pct=False, colors=None, lang="en",
          end_labels=True, markers=True):
    """Lines over ordered categories; with end_labels the last point of each line carries its value."""
    names = list(series)
    data = CategoryChartData()
    data.categories = [str(v) for v in x_labels]
    for n in names:
        data.add_series(n, series[n])
    frame = slide.shapes.add_chart(XL_CHART_TYPE.LINE_MARKERS if markers else XL_CHART_TYPE.LINE, I(x), I(y),
                                   I(w), I(h), data)
    chart = frame.chart
    _layout(chart, dict(PLOT, w=0.86))
    _clean_axis(chart.value_axis, gridlines=True)
    chart.value_axis.major_gridlines.format.line.color.rgb = RGB(P.GRID)
    _clean_axis(chart.category_axis)
    for s, c, n in zip(chart.plots[0].series, _colors(names, colors), names):
        s.format.line.color.rgb = RGB(c)
        s.format.line.width = Pt(2.5)
        s.smooth = False
        if markers:
            s.marker.format.fill.solid()
            s.marker.format.fill.fore_color.rgb = RGB(c)
            s.marker.format.line.color.rgb = RGB(P.SURFACE)
            s.marker.size = 7
        if end_labels:
            last = [None] * (len(series[n]) - 1) + [series[n][-1]]
            _labels(s, last, digits, lang, pct, SIZES["label"], position=XL_LABEL_POSITION.RIGHT)
    _legend(chart, len(names) > 1)
    return frame


def scatter(slide, x, y, w, h, groups: dict, *, colors=None, marker=9):
    """Points of up to three groups ({name: [(x, y), …]}), as with charts.scatter."""
    if len(groups) > 3:
        raise ValueError("scatter: at most three groups; use small multiples for more")
    data = XyChartData()
    for n, pts in groups.items():
        s = data.add_series(n)
        for px, py in pts:
            s.add_data_point(px, py)
    frame = slide.shapes.add_chart(XL_CHART_TYPE.XY_SCATTER, I(x), I(y), I(w), I(h), data)
    chart = frame.chart
    _layout(chart)
    _clean_axis(chart.value_axis, gridlines=True)
    _clean_axis(chart.category_axis)
    chart.value_axis.major_gridlines.format.line.color.rgb = RGB(P.GRID)
    for s, c in zip(chart.plots[0].series, _colors(list(groups), colors)):
        s.format.line.fill.background()
        s.marker.style = 8                             # circle
        s.marker.size = marker
        s.marker.format.fill.solid()
        s.marker.format.fill.fore_color.rgb = RGB(c)
        s.marker.format.line.color.rgb = RGB(P.SURFACE)
    _legend(chart, len(groups) > 1)
    return frame


def doughnut(slide, x, y, w, h, parts: dict, *, colors=None, lang="en", digits=0, hole=55, centre=None):
    """Shares of one whole as a ring, each segment labelled with its percentage; `centre` writes a headline in the
    hole (e.g. the total). Use it for two to five parts; more parts read better as stacked bars."""
    names = list(parts)
    total = sum(parts.values())
    data = CategoryChartData()
    data.categories = names
    data.add_series("share", [parts[n] for n in names])
    frame = slide.shapes.add_chart(XL_CHART_TYPE.DOUGHNUT, I(x), I(y), I(w), I(h), data)
    chart = frame.chart
    _layout(chart, {"x": 0.25, "y": 0.04, "w": 0.5, "h": 0.92})
    hs = chart._chartSpace.find(".//" + qn("c:holeSize"))
    if hs is not None:
        hs.set("val", str(hole))
    plot = chart.plots[0]
    plot.vary_by_categories = True
    s = plot.series[0]
    cols = _colors(names, colors)
    for k, c in enumerate(cols):
        pt = s.points[k]
        pt.format.fill.solid()
        pt.format.fill.fore_color.rgb = RGB(c)
        pt.format.line.color.rgb = RGB(P.SURFACE)
    _labels(s, [parts[n] / total * 100 for n in names], digits, lang, True, SIZES["label"], P.SURFACE)
    for k, c in enumerate(cols):
        s.points[k].data_label.text_frame.paragraphs[0].runs[0].font.color.rgb = RGB(P.text_on(c))
    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.RIGHT
    chart.legend.include_in_layout = False
    _font(chart.legend.font, SIZES["legend"])
    if centre:
        box = slide.shapes.add_textbox(I(x + w * 0.35), I(y + h * 0.4), I(w * 0.3), I(h * 0.2))
        tf = box.text_frame
        tf.text = centre
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        _font(p.runs[0].font, 20, P.NAVY, bold=True)
    return frame
