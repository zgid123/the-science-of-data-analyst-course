"""Inline-SVG charts for report.html: palette, drawing primitives and one function per chart.

Each chart function takes the parsed results JSON and returns a <figure> with the SVG, hover tooltips
(data-tip) and a table view. Palette roles follow the dataviz reference instance; the outcome pair was
validated with validate_palette.js (logs/08_palette_check.log).
"""

from __future__ import annotations

import html

from common import OUTCOMES

# Palette roles (dataviz reference instance; outcome pair validated with validate_palette.js, light mode)
OUTCOME_COLOR = {"Withdrawn": "#c23a3a", "Fail": "#ec7b70", "Pass": "#5598e7", "Distinction": "#184f95"}
OUTCOME_INK = {"Withdrawn": "#ffffff", "Fail": "#1d2433", "Pass": "#1d2433", "Distinction": "#ffffff"}
SERIES_1 = "#2a78d6"
INK, INK2, MUTED = "#1d2433", "#5b6475", "#7a8394"  # page ink tokens (design-notes.md)
GRID, BASE, SURFACE = "#e6e9ef", "#b9c0cc", "#ffffff"
FONT = 'font-family="system-ui,-apple-system,Segoe UI,sans-serif"'


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def fmt(n: float, digits: int = 0) -> str:
    return f"{n:,.{digits}f}"


def tip(*lines: str) -> str:
    return esc(" | ".join(lines))


def rounded_bar(x: float, y: float, w: float, h: float, r: float = 4) -> str:
    """Horizontal bar: square at the baseline (left), rounded data end (right)."""
    if w <= 0:
        return ""
    r = min(r, w, h / 2)
    return (f"M{x:.1f},{y:.1f}h{w - r:.1f}a{r},{r} 0 0 1 {r},{r}v{h - 2 * r:.1f}"
            f"a{r},{r} 0 0 1 -{r},{r}h-{w - r:.1f}z")


def legend(items: list[tuple[str, str]]) -> str:
    keys = "".join(
        f'<span class="key"><span class="swatch" style="background:{c}"></span>{esc(n)}</span>' for n, c in items)
    return f'<div class="legend" aria-hidden="true">{keys}</div>'


def table(headers: list[str], rows: list[list], caption: str) -> str:
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<details class="tableview"><summary>{esc(caption)}</summary><div class="scroll">'
            f"<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div></details>")


def figure(title: str, subtitle: str, svg: str, extra: str = "") -> str:
    return (f'<figure class="chart"><figcaption><strong>{esc(title)}</strong>'
            f'<span class="sub">{esc(subtitle)}</span></figcaption>{svg}{extra}</figure>')


# ---------------------------------------------------------------- charts, sections 1-4 (results/segments.json, columns.json)


def outcome_by_module(seg: dict) -> str:
    rows = [dict(r) for r in seg["final_result_by_module"]]
    total = {o: sum(r[o] for r in rows) for o in OUTCOMES}
    rows = sorted(rows, key=lambda r: r["Withdrawn"] / sum(r[o] for o in OUTCOMES))
    rows.append({"code_module": "All", **total})
    W, left, right, bar, gap_y = 760, 64, 12, 22, 14
    plot = W - left - right
    H = 30 + len(rows) * (bar + gap_y) + 26
    out = []
    for i, r in enumerate(rows):
        n = sum(r[o] for o in OUTCOMES)
        y = 24 + i * (bar + gap_y)
        weight = "600" if r["code_module"] == "All" else "400"
        out.append(f'<text x="{left - 10}" y="{y + bar / 2 + 4}" text-anchor="end" fill="{INK2}" font-size="13" '
                   f'font-weight="{weight}">{esc(r["code_module"])}</text>')
        x = left
        for k, o in enumerate(OUTCOMES):
            share = r[o] / n
            w = share * plot
            w_draw = max(0.0, w - (2 if k < len(OUTCOMES) - 1 else 0))  # 2px surface gap between segments
            t = tip(f"{r['code_module']} · {o}", f"{share:.1%} ({fmt(r[o])} of {fmt(n)} enrolments)")
            shape = (f'<path d="{rounded_bar(x, y, w_draw, bar)}"' if k == len(OUTCOMES) - 1
                     else f'<rect x="{x:.1f}" y="{y}" width="{w_draw:.1f}" height="{bar}"')
            out.append(f'{shape} fill="{OUTCOME_COLOR[o]}" class="mark" data-tip="{t}" tabindex="0"/>')
            if w_draw > 44:
                out.append(f'<text x="{x + w_draw / 2:.1f}" y="{y + bar / 2 + 4}" text-anchor="middle" font-size="11.5" '
                           f'fill="{OUTCOME_INK[o]}" pointer-events="none">{share:.0%}</text>')
            x += w
    axis_y = 24 + len(rows) * (bar + gap_y) - gap_y + 6
    for p in (0, 25, 50, 75, 100):
        xx = left + p / 100 * plot
        anchor = "end" if p == 100 else "start" if p == 0 else "middle"
        out.append(f'<text x="{xx:.1f}" y="{axis_y + 14}" text-anchor="{anchor}" font-size="11" fill="{MUTED}">{p}%</text>')
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Outcome mix by module, 100 percent stacked bars" '
           f'{FONT}>{"".join(out)}</svg>')
    tbl = table(["Module", "Enrolments"] + [f"{o} %" for o in OUTCOMES] + OUTCOMES,
                [[r["code_module"], fmt(sum(r[o] for o in OUTCOMES))]
                 + [f"{r[o] / sum(r[x] for x in OUTCOMES):.1%}" for o in OUTCOMES] + [fmt(r[o]) for o in OUTCOMES]
                 for r in rows], "Table view: outcome counts and shares by module")
    return figure("Withdrawal ranges from 12% to 45% across modules",
                  "Share of enrolments by final result, modules ordered by withdrawal rate; all 32,593 enrolments.",
                  legend([(o, OUTCOME_COLOR[o]) for o in OUTCOMES]) + svg, tbl)


def weekly_clicks(seg: dict) -> str:
    data = {o: {} for o in OUTCOMES}
    for r in seg["weekly_clicks_by_final_result"]:
        data[r["final_result"]][r["week"]] = r["clicks_per_enrolment"]
    weeks = sorted({w for d in data.values() for w in d})
    W, H, left, right, top, bottom = 760, 300, 52, 16, 14, 34
    pw, ph = W - left - right, H - top - bottom
    ymax = max(v for d in data.values() for v in d.values())
    ystep = 25 if ymax <= 150 else 50
    ytop = ystep * -(-ymax // ystep)
    wx = lambda w: left + (w - weeks[0]) / (weeks[-1] - weeks[0]) * pw
    vy = lambda v: top + ph - v / ytop * ph
    out = []
    for v in range(0, int(ytop) + 1, ystep):
        out.append(f'<line x1="{left}" x2="{W - right}" y1="{vy(v):.1f}" y2="{vy(v):.1f}" stroke="{GRID if v else BASE}" stroke-width="1"/>')
        out.append(f'<text x="{left - 8}" y="{vy(v) + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{v}</text>')
    for w in range(0, weeks[-1] + 1, 5):
        out.append(f'<text x="{wx(w):.1f}" y="{H - 14}" text-anchor="middle" font-size="11" fill="{MUTED}">{w}</text>')
    out.append(f'<text x="{W - right}" y="{H - 1}" text-anchor="end" font-size="11" fill="{MUTED}">week of presentation (week 0 = days 0–6)</text>')
    out.append(f'<line x1="{wx(0):.1f}" x2="{wx(0):.1f}" y1="{top}" y2="{top + ph}" stroke="{BASE}" stroke-width="1"/>'
               f'<text x="{wx(0) + 5:.1f}" y="{top + 10}" font-size="11" fill="{INK2}">presentation starts</text>')
    for o in OUTCOMES:
        pts = " ".join(f"{wx(w):.1f},{vy(data[o].get(w, 0)):.1f}" for w in weeks)
        out.append(f'<polyline points="{pts}" fill="none" stroke="{OUTCOME_COLOR[o]}" stroke-width="2" '
                   'stroke-linejoin="round" stroke-linecap="round"/>')
    # hover columns: one tooltip per week listing every series
    colw = pw / (len(weeks) - 1)
    for w in weeks:
        lines = [f"week {w}"] + [f"{o}: {data[o].get(w, 0):.1f} clicks" for o in OUTCOMES]
        out.append(f'<rect x="{wx(w) - colw / 2:.1f}" y="{top}" width="{colw:.1f}" height="{ph}" fill="transparent" '
                   f'class="mark col" data-tip="{tip(*lines)}" data-x="{wx(w):.1f}" tabindex="-1"/>')
    out.append(f'<line class="crosshair" x1="0" x2="0" y1="{top}" y2="{top + ph}" stroke="{MUTED}" stroke-width="1" visibility="hidden"/>')
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Average clicks per enrolment per week by final result" '
           f'{FONT}>{"".join(out)}</svg>')
    tbl = table(["Week"] + OUTCOMES, [[w] + [f"{data[o].get(w, 0):.1f}" for o in OUTCOMES] for w in weeks],
                "Table view: clicks per enrolment by week and outcome")
    return figure("Engagement separates by outcome from the first week",
                  "Average VLE clicks per enrolment per week; every enrolment in the outcome group counts, "
                  "including weeks after withdrawal (which contribute 0).",
                  legend([(o, OUTCOME_COLOR[o]) for o in OUTCOMES]) + svg, tbl)


def clicks_range(seg: dict) -> str:
    rows = {r["final_result"]: r for r in seg["clicks_by_final_result"]}
    W, left, right, rowh = 760, 96, 60, 40
    H = 24 + len(OUTCOMES) * rowh + 24
    xmax = 4000
    sx = lambda v: left + v / xmax * (W - left - right)
    out = []
    for v in range(0, xmax + 1, 1000):
        out.append(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="14" y2="{H - 26}" stroke="{GRID if v else BASE}" stroke-width="1"/>'
                   f'<text x="{sx(v):.1f}" y="{H - 10}" text-anchor="middle" font-size="11" fill="{MUTED}">{f"{v // 1000}K" if v else "0"}</text>')
    for i, o in enumerate(OUTCOMES):
        r = rows[o]
        y = 30 + i * rowh
        t = tip(o, f"median {fmt(r['median_clicks'])} clicks", f"middle 50%: {fmt(r['p25'])}–{fmt(r['p75'])}",
                f"{fmt(r['zero_click'])} of {fmt(r['enrolments'])} with no clicks")
        out.append(f'<text x="{left - 12}" y="{y + 4}" text-anchor="end" font-size="13" fill="{INK2}">{o}</text>'
                   f'<line x1="{sx(r["p25"]):.1f}" x2="{sx(r["p75"]):.1f}" y1="{y}" y2="{y}" stroke="{OUTCOME_COLOR[o]}" '
                   'stroke-width="6" stroke-linecap="round" opacity="0.55"/>'
                   f'<circle cx="{sx(r["median_clicks"]):.1f}" cy="{y}" r="5.5" fill="{OUTCOME_COLOR[o]}" stroke="{SURFACE}" stroke-width="2"/>'
                   f'<text x="{sx(r["p75"]) + 10:.1f}" y="{y + 4}" font-size="12" fill="{INK}">{fmt(r["median_clicks"])}</text>'
                   f'<rect x="{left}" y="{y - rowh / 2}" width="{W - left - right}" height="{rowh}" fill="transparent" '
                   f'class="mark" data-tip="{t}" tabindex="0"/>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Total clicks per enrolment by final result" {FONT}>{"".join(out)}</svg>'
    tbl = table(["Final result", "Enrolments", "Median clicks", "25th pct", "75th pct", "No clicks"],
                [[o, fmt(rows[o]["enrolments"]), fmt(rows[o]["median_clicks"]), fmt(rows[o]["p25"]), fmt(rows[o]["p75"]),
                  fmt(rows[o]["zero_click"])] for o in OUTCOMES], "Table view: clicks per enrolment by outcome")
    return figure("Median total clicks rise from 89 (Withdrawn) to 1,896 (Distinction)",
                  "Total VLE clicks per enrolment over the whole presentation: dot = median, bar = middle 50%. "
                  "Totals include exposure: withdrawn students are enrolled for less time.", svg, tbl)


def hbars(rows: list[tuple[str, float, str]], title: str, subtitle: str, fmt_v, ref: tuple[float, str] | None,
          tbl: str, label_w: int = 190, xmax: float | None = None) -> str:
    W, right, bar, gap_y = 760, 70, 16, 8
    H = 14 + len(rows) * (bar + gap_y) + 22
    xmax = xmax or max(v for _, v, _ in rows)
    sx = lambda v: label_w + v / xmax * (W - label_w - right)
    out = []
    for i, (name, v, t) in enumerate(rows):
        y = 10 + i * (bar + gap_y)
        out.append(f'<text x="{label_w - 10}" y="{y + bar / 2 + 4}" text-anchor="end" font-size="12" fill="{INK2}">{esc(name)}</text>'
                   f'<path d="{rounded_bar(label_w, y, sx(v) - label_w, bar)}" fill="{SERIES_1}" class="mark" data-tip="{esc(t)}" tabindex="0"/>'
                   f'<text x="{sx(v) + 6:.1f}" y="{y + bar / 2 + 4}" font-size="11.5" fill="{INK}">{fmt_v(v)}</text>')
    if ref:
        out.append(f'<line x1="{sx(ref[0]):.1f}" x2="{sx(ref[0]):.1f}" y1="4" y2="{H - 18}" stroke="{INK2}" stroke-width="1"/>'
                   f'<text x="{sx(ref[0]) + 4:.1f}" y="{H - 6}" font-size="11" fill="{INK2}">{esc(ref[1])}</text>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}" {FONT}>{"".join(out)}</svg>'
    return figure(title, subtitle, svg, tbl)


def duplicates(seg: dict) -> str:
    rows = sorted(seg["duplicate_rows_by_presentation"], key=lambda r: -r["share"])
    total_dup = sum(r["duplicate_rows"] for r in rows)
    total = sum(r["rows"] for r in rows)
    data = [(f'{r["code_module"]} {r["code_presentation"]}', r["share"] * 100,
             f'{r["code_module"]} {r["code_presentation"]} | {r["share"]:.2%} of rows | {fmt(r["duplicate_rows"])} of {fmt(r["rows"])}')
            for r in rows]
    tbl = table(["Presentation", "Click-log rows", "Exact duplicate rows", "Share"],
                [[f'{r["code_module"]} {r["code_presentation"]}', fmt(r["rows"]), fmt(r["duplicate_rows"]), f'{r["share"]:.2%}']
                 for r in rows], "Table view: duplicate click-log rows by presentation")
    return hbars(data, "Exact duplicate click rows occur in every presentation",
                 f"Share of studentVle rows that repeat another row exactly (same student, site, day and clicks); "
                 f"{fmt(total_dup)} of {fmt(total)} rows overall.",
                 lambda v: f"{v:.1f}%", (total_dup / total * 100, f"overall {total_dup / total:.2%}"), tbl, label_w=110)


def missingness(cols: list[dict]) -> str:
    rows = sorted([c for c in cols if c["missing"]], key=lambda c: -c["missing_rate"])
    data = [(f'{c["table"]}.{c["column"]}', c["missing_rate"] * 100,
             f'{c["table"]}.{c["column"]} | {c["missing_rate"]:.2%} missing | {fmt(c["missing"])} of {fmt(c["rows"])} rows')
            for c in rows]
    tbl = table(["Column", "Missing", "Rows", "Rate", "Completeness"],
                [[f'{c["table"]}.{c["column"]}', fmt(c["missing"]), fmt(c["rows"]), f'{c["missing_rate"]:.2%}', c["completeness"]]
                 for c in rows], "Table view: missing values by column")
    return hbars(data, f"{len(rows)} of {len(cols)} columns have missing values; three are missing by design",
                 "Share of rows with an empty value. vle.week_from, vle.week_to and date_unregistration are missing by design "
                 "(week plan only for some sites; unregistration only for students who left).",
                 lambda v: f"{v:.2f}%" if v < 1 else f"{v:.1f}%", None, tbl, label_w=260, xmax=100)


# ---------------------------------------------------------------- charts, section 5 (results/descriptive.json)


def imd_gradient(desc: dict) -> str:
    rows = {r["value"]: r for r in desc["outcome_by_dimension"]["imd_band"]["rows"]}
    bands = ["0-10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "60-70%", "70-80%", "80-90%", "90-100%", "(missing)"]
    W, H, left, right, top, bottom = 760, 280, 48, 16, 14, 46
    pw, ph = W - left - right, H - top - bottom
    step = pw / len(bands)
    bx = lambda i: left + step * (i + 0.5)
    vy = lambda v: top + ph - v / 0.8 * ph
    out = []
    for v in (0, 0.2, 0.4, 0.6, 0.8):
        out.append(f'<line x1="{left}" x2="{W - right}" y1="{vy(v):.1f}" y2="{vy(v):.1f}" stroke="{GRID if v else BASE}" stroke-width="1"/>'
                   f'<text x="{left - 8}" y="{vy(v) + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{v:.0%}</text>')
    for i, b in enumerate(bands):
        r = rows[b]["success"]
        c = MUTED if b == "(missing)" else SERIES_1
        t = tip(f"imd_band {b}", f"success {r['rate']:.1%}", f"95% interval {r['lo']:.1%}–{r['hi']:.1%}", f"{fmt(r['n'])} enrolments")
        out.append(f'<line x1="{bx(i):.1f}" x2="{bx(i):.1f}" y1="{vy(r["lo"]):.1f}" y2="{vy(r["hi"]):.1f}" stroke="{c}" stroke-width="2" stroke-linecap="round"/>'
                   f'<circle cx="{bx(i):.1f}" cy="{vy(r["rate"]):.1f}" r="5" fill="{c}" stroke="{SURFACE}" stroke-width="2"/>'
                   f'<text x="{bx(i):.1f}" y="{vy(r["hi"]) - 8:.1f}" text-anchor="middle" font-size="11" fill="{INK}">{r["rate"]:.0%}</text>'
                   f'<text x="{bx(i):.1f}" y="{H - 28}" text-anchor="middle" font-size="11" fill="{INK2}">{esc(b.replace("-", "–"))}</text>'
                   f'<rect x="{bx(i) - step / 2:.1f}" y="{top}" width="{step:.1f}" height="{ph}" fill="transparent" class="mark" data-tip="{t}" tabindex="0"/>')
    out.append(f'<text x="{left}" y="{H - 8}" font-size="11" fill="{MUTED}">deprivation decile (0–10% = most deprived areas)</text>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Success rate by IMD band" {FONT}>{"".join(out)}</svg>'
    tbl = table(["imd_band", "Enrolments", "Success", "95% interval", "Withdrawn"],
                [[b, fmt(rows[b]["n"]), f'{rows[b]["success"]["rate"]:.1%}',
                  f'{rows[b]["success"]["lo"]:.1%}–{rows[b]["success"]["hi"]:.1%}', f'{rows[b]["withdrawn"]["rate"]:.1%}'] for b in bands],
                "Table view: success rate by deprivation band")
    return figure("Success rises from 35% in the most deprived decile to 58% in the least deprived",
                  "Share of enrolments ending in Pass or Distinction, with Wilson 95% intervals. The missing band (grey) "
                  "is concentrated in North Region and Ireland.", svg, tbl)


def gender_simpson(desc: dict) -> str:
    s = desc["simpson"]["female_vs_male:withdrawn"]
    rows = s["per_module"]
    W, left, right, rowh = 760, 150, 70, 30
    H = 20 + len(rows) * rowh + 40
    lo, hi = -10, 10
    sx = lambda v: left + (v - lo) / (hi - lo) * (W - left - right)
    out = []
    for v in range(lo, hi + 1, 5):
        out.append(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="12" y2="{H - 36}" stroke="{BASE if v == 0 else GRID}" stroke-width="1"/>'
                   f'<text x="{sx(v):.1f}" y="{H - 22}" text-anchor="middle" font-size="11" fill="{MUTED}">{v:+d}</text>')
    for i, r in enumerate(rows):
        y = 18 + i * rowh
        g = r["gap_pp"]
        x0, x1 = (sx(0), sx(g)) if g >= 0 else (sx(g), sx(0))
        share = s["group1_share_by_module"][r["module"]]
        t = tip(r["module"], f"women minus men: {g:+.1f} points", f"women {share:.0%} of the module",
                f"{fmt(r['n1'])} women, {fmt(r['n2'])} men")
        out.append(f'<text x="{left - 10}" y="{y + 13}" text-anchor="end" font-size="12" fill="{INK2}">{r["module"]} ({share:.0%} women)</text>'
                   f'<rect x="{x0:.1f}" y="{y + 3}" width="{max(x1 - x0, 1):.1f}" height="16" rx="3" fill="{SERIES_1}"/>'
                   f'<text x="{(sx(g) + 6) if g >= 0 else (sx(g) - 6):.1f}" y="{y + 15}" text-anchor="{"start" if g >= 0 else "end"}" font-size="11.5" fill="{INK}">{g:+.1f}</text>'
                   f'<rect x="{left}" y="{y}" width="{W - left - right}" height="{rowh}" fill="transparent" class="mark" data-tip="{t}" tabindex="0"/>')
    for v, name, dash in ((s["crude_gap_pp"], "crude", "4 3"), (s["module_standardised_gap_pp"], "within modules", "")):
        out.append(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="10" y2="{H - 36}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="{dash}"/>'
                   f'<text x="{sx(v):.1f}" y="{H - 6}" text-anchor="middle" font-size="11" fill="{INK}">{name} {v:+.1f}</text>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Gender gap in withdrawal by module" {FONT}>{"".join(out)}</svg>'
    tbl = table(["Module", "Women share", "Women", "Men", "Gap (points)"],
                [[r["module"], f'{s["group1_share_by_module"][r["module"]]:.0%}', fmt(r["n1"]), fmt(r["n2"]), f'{r["gap_pp"]:+.2f}'] for r in rows]
                + [["Crude (all)", "", "", "", f'{s["crude_gap_pp"]:+.2f}'], ["Module-standardised", "", "", "", f'{s["module_standardised_gap_pp"]:+.2f}']],
                "Table view: withdrawal gap, women minus men, by module")
    return figure("Women withdraw less overall, but more within 6 of 7 modules",
                  "Withdrawal rate of women minus men, percentage points. Dashed line: crude gap; solid line: gap "
                  "standardised to module size. Women are concentrated in BBB and GGG, where withdrawal is low.", svg, tbl)


def first_assessment(desc: dict) -> str:
    rows = desc["assessments"]["first_assessment_by_outcome"]
    data = [(r["final_result"], r["first_not_submitted"] * 100,
             f'{r["final_result"]} | {r["first_not_submitted"]:.1%} never submitted the first TMA/CMA | '
             f'median first score {r["median_first_score"]:.0f} | {fmt(r["n"])} enrolments') for r in rows]
    tbl = table(["Final result", "Enrolments", "First assessment not submitted", "Median first score"],
                [[r["final_result"], fmt(r["n"]), f'{r["first_not_submitted"]:.1%}', f'{r["median_first_score"]:.0f}'] for r in rows],
                "Table view: first assessment by outcome")
    return hbars(data, "More than half of withdrawn students never submitted the first assessment",
                 "Share of enrolments with no submission for the earliest-due TMA or CMA of their presentation. Includes "
                 "students who had already left, so part of the Withdrawn share is a consequence, not a warning.",
                 lambda v: f"{v:.1f}%", None, tbl, label_w=110, xmax=100)


def survival_curves(desc: dict) -> str:
    curves = {k: {int(d): v for d, v in c.items()} for k, c in desc["survival"]["weekly_curves"].items()}
    modules = [k for k in curves if k != "All"]
    days = sorted(curves["All"])
    W, H, left, right, top, bottom = 760, 300, 48, 90, 14, 34
    pw, ph = W - left - right, H - top - bottom
    ymin = 0.6
    dx = lambda d: left + d / days[-1] * pw
    vy = lambda v: top + (1 - v) / (1 - ymin) * ph
    out = []
    for v in (0.6, 0.7, 0.8, 0.9, 1.0):
        out.append(f'<line x1="{left}" x2="{left + pw}" y1="{vy(v):.1f}" y2="{vy(v):.1f}" stroke="{GRID}" stroke-width="1"/>'
                   f'<text x="{left - 8}" y="{vy(v) + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{v:.0%}</text>')
    for d in range(0, days[-1] + 1, 28):
        out.append(f'<text x="{dx(d):.1f}" y="{H - 14}" text-anchor="middle" font-size="11" fill="{MUTED}">{d}</text>')
    out.append(f'<text x="{left + pw}" y="{H - 1}" text-anchor="end" font-size="11" fill="{MUTED}">day of presentation</text>')
    labels = []
    for k in modules + ["All"]:
        c, w = (SERIES_1, 2.5) if k == "All" else (BASE, 1.5)
        pts = " ".join(f"{dx(d):.1f},{vy(curves[k][d]):.1f}" for d in days)
        out.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linejoin="round"/>')
        labels.append([vy(curves[k][days[-1]]), k, curves[k][days[-1]]])
    labels.sort()
    for i in range(1, len(labels)):  # keep end labels at least 12px apart
        labels[i][0] = max(labels[i][0], labels[i - 1][0] + 12)
    for y, k, v in labels:
        out.append(f'<text x="{left + pw + 6}" y="{y + 4:.1f}" font-size="11" fill="{INK if k == "All" else INK2}" '
                   f'font-weight="{600 if k == "All" else 400}">{k} {v:.0%}</text>')
    colw = pw / (len(days) - 1)
    for d in days:
        t = tip(f"day {d}", *[f"{k}: {curves[k][d]:.1%} still enrolled" for k in ["All"] + modules])
        out.append(f'<rect x="{dx(d) - colw / 2:.1f}" y="{top}" width="{colw:.1f}" height="{ph}" fill="transparent" '
                   f'class="mark col" data-tip="{t}" data-x="{dx(d):.1f}" tabindex="-1"/>')
    out.append(f'<line class="crosshair" x1="0" x2="0" y1="{top}" y2="{top + ph}" stroke="{MUTED}" stroke-width="1" visibility="hidden"/>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Kaplan-Meier retention by module" {FONT}>{"".join(out)}</svg>'
    sa = desc["survival"]["survival_at"]
    cols = ["28", "60", "120", "180", "269"]
    tbl = table(["Module"] + [f"day {c}" for c in cols], [[k] + [f"{sa[k][c]:.1%}" for c in cols] for k in ["All"] + modules],
                "Table view: share still enrolled (Kaplan–Meier)")
    return figure("A quarter of students enrolled on day 0 withdraw before the end, steadily over time",
                  "Kaplan–Meier share still enrolled, from day 0; blue = all modules, grey = each module (end value labelled). "
                  "Pass and Fail are censored at the presentation end.", svg, tbl)


def yoy_withdrawal(desc: dict) -> str:
    rows = sorted(desc["temporal"]["year_on_year"], key=lambda r: -r["withdrawal_change_pp"])
    data = [(f'{r["module"]} {r["semester"]}', r["withdrawal_change_pp"],
             f'{r["module"]} {r["semester"]} | withdrawal {r["withdrawal_change_pp"]:+.1f} points | success {r["success_change_pp"]:+.1f} points')
            for r in rows]
    tbl = table(["Module and semester", "Withdrawal change (points)", "Success change (points)"],
                [[f'{r["module"]} {r["semester"]}', f'{r["withdrawal_change_pp"]:+.2f}', f'{r["success_change_pp"]:+.2f}'] for r in rows],
                "Table view: change from 2013 to 2014")
    return hbars(data, "Withdrawal rose from 2013 to 2014 in every module observed in both years",
                 "Change in withdrawal rate from the 2013 to the 2014 presentation of the same module and semester, percentage points.",
                 lambda v: f"+{v:.1f}", None, tbl, label_w=110)


# ---------------------------------------------------------------- charts, sections 5.2 and 5.6 (descriptive.json, multivariate.json)

CLUSTER_COLOR = ["#2a78d6", "#eb6834", "#1baf7a"]  # categorical slots 1-3, validated (logs/08_palette_check.log)
CLUSTER_NAME = {1: "low activity", 2: "middle activity", 3: "high activity"}


def trajectory_clusters(multi: dict) -> str:
    t = multi["trajectories"]
    cl = t["clusters"]
    weeks = len(cl[0]["centre_weekly_clicks"])
    W, H, left, right, top, bottom = 760, 290, 48, 150, 14, 34
    pw, ph = W - left - right, H - top - bottom
    ymax = max(max(c["centre_weekly_clicks"]) for c in cl)
    ytop = 25 * -(-ymax // 25)
    wx = lambda w: left + w / (weeks - 1) * pw
    vy = lambda v: top + ph - v / ytop * ph
    out = []
    for v in range(0, int(ytop) + 1, 25):
        out.append(f'<line x1="{left}" x2="{left + pw}" y1="{vy(v):.1f}" y2="{vy(v):.1f}" stroke="{GRID if v else BASE}" stroke-width="1"/>'
                   f'<text x="{left - 8}" y="{vy(v) + 4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{v}</text>')
    for w in range(0, weeks, 5):
        out.append(f'<text x="{wx(w):.1f}" y="{H - 14}" text-anchor="middle" font-size="11" fill="{MUTED}">{w}</text>')
    out.append(f'<text x="{left + pw}" y="{H - 1}" text-anchor="end" font-size="11" fill="{MUTED}">week of presentation</text>')
    for c, color in zip(cl, CLUSTER_COLOR):
        pts = " ".join(f"{wx(w):.1f},{vy(v):.1f}" for w, v in enumerate(c["centre_weekly_clicks"]))
        out.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>')
    for i, c in enumerate(sorted(cl, key=lambda c: -c["cluster"])):  # fixed slots, most active first
        y = top + 14 + 58 * i
        color = CLUSTER_COLOR[c["cluster"] - 1]
        out.append(f'<rect x="{left + pw + 8}" y="{y - 9}" width="10" height="10" rx="2" fill="{color}"/>'
                   f'<text x="{left + pw + 24}" y="{y:.1f}" font-size="11.5" fill="{INK}">{CLUSTER_NAME[c["cluster"]]}</text>'
                   f'<text x="{left + pw + 24}" y="{y + 15:.1f}" font-size="11" fill="{INK2}">{c["share"]:.0%} of enrolments</text>'
                   f'<text x="{left + pw + 24}" y="{y + 29:.1f}" font-size="11" fill="{INK2}">{c["success"]["rate"]:.0%} succeed</text>')
    colw = pw / (weeks - 1)
    for w in range(weeks):
        tt = tip(f"week {w}", *[f"{CLUSTER_NAME[c['cluster']]}: {c['centre_weekly_clicks'][w]:.1f} clicks" for c in cl])
        out.append(f'<rect x="{wx(w) - colw / 2:.1f}" y="{top}" width="{colw:.1f}" height="{ph}" fill="transparent" '
                   f'class="mark col" data-tip="{tt}" data-x="{wx(w):.1f}" tabindex="-1"/>')
    out.append(f'<line class="crosshair" x1="0" x2="0" y1="{top}" y2="{top + ph}" stroke="{MUTED}" stroke-width="1" visibility="hidden"/>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Weekly click trajectories by cluster" {FONT}>{"".join(out)}</svg>'
    tbl = table(["Cluster", "Enrolments", "Withdrawn", "Fail", "Pass", "Distinction", "Success (95% interval)"],
                [[CLUSTER_NAME[c["cluster"]], fmt(c["n"])] + [fmt(c["outcomes"][o]) for o in OUTCOMES]
                 + [f'{c["success"]["rate"]:.1%} ({c["success"]["lo"]:.1%}–{c["success"]["hi"]:.1%})'] for c in cl],
                "Table view: trajectory clusters by outcome")
    return figure(f"Three engagement trajectories, from fading out to sustained (k = {t['k_selected']})",
                  f"Typical weekly clicks of each cluster (back-transformed centre of k-means on log clicks, weeks 0–37). Silhouette {t['by_k'][str(t['k_selected'])]['silhouette']:.2f}: "
                  "the clusters cut a continuum rather than separate distinct groups.",
                  legend([(CLUSTER_NAME[c["cluster"]], col) for c, col in zip(cl, CLUSTER_COLOR)]) + svg, tbl)


SIGNAL_LABEL = {"n_submitted": "assessments submitted", "active_days": "active days", "clicks_total": "total clicks",
                "active_days_early": "active days, days 0–27", "mean_score": "mean score", "clicks_early": "clicks, days 0–27",
                "clicks_prestart": "clicks before day 0", "first_score": "first assessment score", "n_late": "late submissions",
                "first_days_late": "first assessment, days late", "edu_ord": "prior education (ordered)",
                "imd_ord": "IMD band (ordered)", "studied_credits": "studied credits",
                "num_of_prev_attempts": "previous attempts", "age_ord": "age band (ordered)",
                "date_registration": "registration day"}


def signal_ranking(desc: dict) -> str:
    rows = desc["signal_ranking"]["rows"]
    W, left, right, rowh = 760, 210, 150, 22
    H = 16 + len(rows) * rowh + 30
    sx = lambda v: left + (v + 1) / 2 * (W - left - right)
    out = []
    for v in (-1, -0.5, 0, 0.5, 1):
        out.append(f'<line x1="{sx(v):.1f}" x2="{sx(v):.1f}" y1="8" y2="{H - 26}" stroke="{BASE if v == 0 else GRID}" stroke-width="1"/>'
                   f'<text x="{sx(v):.1f}" y="{H - 12}" text-anchor="middle" font-size="11" fill="{MUTED}">{v:+.1f}</text>')
    for i, r in enumerate(rows):
        y = 18 + i * rowh
        whole = r["measured_over"] == "whole presentation"
        c = MUTED if whole else SERIES_1
        d = r["cliffs_delta"]
        tt = tip(SIGNAL_LABEL[r["measure"]], f"Cliff's delta {d:+.2f} (within modules {r['median_within_module']:+.2f})",
                 f"measured over: {r['measured_over']}", f"{fmt(r['n'])} enrolments")
        out.append(f'<text x="{left - 10}" y="{y + 4}" text-anchor="end" font-size="12" fill="{INK2}">{esc(SIGNAL_LABEL[r["measure"]])}</text>'
                   f'<line x1="{sx(0):.1f}" x2="{sx(d):.1f}" y1="{y}" y2="{y}" stroke="{c}" stroke-width="2"/>'
                   f'<circle cx="{sx(d):.1f}" cy="{y}" r="5" fill="{c}" stroke="{SURFACE}" stroke-width="2"/>'
                   f'<text x="{W - right + 10}" y="{y + 4}" font-size="11.5" fill="{INK}">{d:+.2f}{"  (whole presentation)" if whole else ""}</text>'
                   f'<rect x="{left}" y="{y - rowh / 2}" width="{W - left - right}" height="{rowh}" fill="transparent" class="mark" data-tip="{tt}" tabindex="0"/>')
    svg = f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Measures ranked by Cliff\'s delta" {FONT}>{"".join(out)}</svg>'
    tbl = table(["Measure", "Cliff's delta", "Median within module", "Measured over", "Enrolments"],
                [[SIGNAL_LABEL[r["measure"]], f'{r["cliffs_delta"]:+.3f}', f'{r["median_within_module"]:+.3f}', r["measured_over"], fmt(r["n"])]
                 for r in rows], "Table view: separation of success by measure")
    return figure("Early activity separates success most among measures known by day 27",
                  "Cliff's delta, successful minus unsuccessful enrolments (+1 = every successful enrolment ranks higher). "
                  "Grey: measured over the whole presentation, so partly a consequence of the outcome.",
                  legend([("known before or early in the presentation", SERIES_1), ("measured over the whole presentation", MUTED)]) + svg, tbl)
