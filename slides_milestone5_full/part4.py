"""Plan slides 70–94 of the full Milestone 5 deck: AQ2 findings, AQ3/AQ4 results of the Level 2 test, answers by question,
decision support D1–D3, limitations and future work, the pilot, generative AI, conclusions, take-home and thank you.

Numbers come from the Milestone 5 report: Sections 11.3–14 and Appendices XII–XVI (Tables A.30, A.33–A.43).
Chart images are cached under the names m5-full-p4-*.
"""

from slides_milestone5_full.common import *   # noqa: F401,F403
from matplotlib.patches import Rectangle


# ----------------------------------------------------------------------------- helpers
def head_line(s, x, y, w, line, color=NAVY):
    """A bold heading line at HEAD size; returns the y below it."""
    hh = lh(line, w, HEAD, True)
    text(s, I(x), I(y), I(w), I(hh), line, size=HEAD, color=color, bold=True, spacing=1.0)
    return y + hh + 0.05


def stack(s, x, y, w, items, bottom, gap=0.2):
    """Cards (head, paras, color, fill, line) stacked from y to bottom: the largest kit size that fits, the free
    height shared over the cards; returns the bottom."""
    room_ = bottom - y - gap * (len(items) - 1)
    pt = next((p for p in (PT["lead"], PT["body"], BODY)
               if sum(card_h(it[0], it[1], w, pt=p, hp=max(HEAD, p)) for it in items) <= room_), BODY)
    hs = [card_h(it[0], it[1], w, pt=pt, hp=max(HEAD, pt)) for it in items]
    kit.room("stack", sum(hs), room_)
    extra = max(0.0, (room_ - sum(hs)) / len(items))
    for it, h in zip(items, hs):
        head, paras = it[0], it[1]
        color = it[2] if len(it) > 2 else NAVY
        fill = it[3] if len(it) > 3 else SOFT
        line = it[4] if len(it) > 4 else LINE
        card(s, x, y, w, head, paras, color=color, h=h + extra, fill=fill, line=line, pt=pt, hp=max(HEAD, pt),
             line_w=2.0 if line not in (LINE,) else 1.0)
        y += h + extra + gap
    return y - gap


def flow3(s, y, bottom, items, gap=0.5):
    """Three cards (head, paras, color, fill, line) across the content width, of one height down to `bottom`,
    linked by arrows; the largest kit size that fits."""
    xs, cw = cols(3, gap)
    pt = next((p for p in (PT["lead"], PT["body"], BODY)
               if max(card_h(it[0], it[1], cw, pt=p, hp=max(HEAD, p)) for it in items) <= bottom - y), BODY)
    kit.room("flow3", max(card_h(it[0], it[1], cw, pt=pt, hp=max(HEAD, pt)) for it in items), bottom - y)
    for k, (x, it) in enumerate(zip(xs, items)):
        head, paras = it[0], it[1]
        color, fill, line = (list(it[2:5]) + [NAVY, SOFT, LINE][len(it) - 2:])[:3]
        card(s, x, y, cw, head, paras, color=color, h=bottom - y, fill=fill, line=line, pt=pt, hp=max(HEAD, pt),
             line_w=2.0 if line != LINE else 1.0)
        if k < 2:
            ay = y + (bottom - y) / 2
            arrow(s, x + cw + 0.06, ay, x + cw + gap - 0.06, ay)
    return bottom


def owner(s, y, who, kind, color=NAVY):
    """The decision owner line: who decides and how reversible the decision is; returns the y below it."""
    paras = [[(T("Decided by: "), color, True), (who + "; ", INK, False), (kind, color, True)]]
    return rich(s, X0, y, CWI, paras, pt=PT["body"]) + 0.05


def colour_cells(shape, rows, col, colours, bold=True):
    """Fill one column's body cells with a colour per row and white bold text."""
    tbl = shape.table
    for i, c in enumerate(colours, 1):
        cell = tbl.cell(i, col)
        cell.fill.solid()
        cell.fill.fore_color.rgb = c
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                r.font.color.rgb, r.font.bold = WHITE, bold


# ----------------------------------------------------------------------------- 70 AQ2 set-up
def s70(prs):
    s = kit.base(prs, kicker(70), T("AQ2: How We Tested the Signs"), notes(70))
    y = lead(s, T("We compared each early sign within its own module run, adjusted for the other signs, on 2013 and "
                  "again, unchanged, on 2014."))
    key70 = T("Key: AQ2 = the diagnostic question (which early signs go with later non-completion); TMA = "
              "tutor-marked assignment; CMA = computer-marked assessment; run = one offering of a module.")
    ky = bottom_key(s, key70)
    bottom = ky - 0.15
    lw, rw, rx = kit.split(0.56)
    groups = [(T("Task signs: "), T("runs with a task due by day 27 (9,960 and 12,585 enrolments)"),
               [(T("Missed task"), T("a TMA or CMA due by day 27, not submitted by then")),
                (T("Late TMA"), T("a TMA due by day 27, submitted after its deadline"))]),
              (T("Click signs: "), T("every run (11,811 and 15,724 enrolments)"),
               [(T("No click in the last 7 days"), T("no platform click on days 21–27")),
                (T("Activity below the run median"), T("clicks on days 0–27 below the median of the same run")),
                (T("No click before the start"), T("no click before day 0, the start of the run"))])]
    chip_w, row_h, gap_r = 2.95, 0.5, 0.1
    heads = [[[(h, AGENT_INK if k == 0 else kit.BLUE, True), (p, INK, False)]] for k, (h, p, _) in enumerate(groups)]
    need = [0.15 + rich_h(hd, lw - 0.36, BODY) + 0.05 + len(g[2]) * (row_h + gap_r) + 0.05
            for hd, g in zip(heads, groups)]
    kit.room("aq2 sign groups", sum(need) + 0.2, bottom - y)
    free = max(0.0, bottom - y - 0.2 - sum(need))
    gy = y
    for k, ((h, p, rows), hd, nd) in enumerate(zip(groups, heads, need)):
        n_rows = len(rows)
        gh = nd + free * n_rows / 5
        rh = row_h + (gh - nd) / n_rows
        rect(s, I(X0), I(gy), I(lw), I(gh), fill=SOFT, line=LINE, radius=True)
        ty = rich(s, X0 + 0.18, gy + 0.15, lw - 0.36, hd, pt=BODY) + 0.05
        for name, body in rows:
            chip(s, X0 + 0.18, ty + (rh - row_h) / 2, chip_w, row_h, name,
                 fill=ACC_FILL if k == 0 else kit.REF_FILL, line_color=WARM if k == 0 else kit.BLUE,
                 color=AGENT_INK if k == 0 else NAVY, size=BODY, bold=True)
            bh = lh(body, lw - chip_w - 0.55, BODY)
            text(s, I(X0 + chip_w + 0.35), I(ty + (rh - bh) / 2), I(lw - chip_w - 0.55), I(bh), body, size=BODY,
                 color=INK, spacing=1.0)
            ty += rh + gap_r
        gy += gh + 0.2
    items = [(T("Population"), [T("Registered at day 27: 11,811 enrolments in the 9 runs of 2013 (44.4% did not "
                                  "complete) and 15,724 in the 13 runs of 2014 (44.0%), module CCC included.")]),
             (T("Model and result"), [T("Logistic regression with a fixed effect for each run, background terms and "
                                        "sign × module terms. Result: a risk difference in percentage points, each "
                                        "sign adjusted for the other four; an association, not an effect.")]),
             (T("Criterion, fixed in Milestone 4"), [T("At least 5 points, a 95% interval excluding 0, and the same "
                                                      "direction in at least two-thirds of the modules; p-values take "
                                                      "no part.")], AGENT_INK, ACC_FILL, WARM)]
    stack(s, rx, y, rw, items, bottom, gap=0.15)
    src(s, "Source: Milestone 5 report, Section 11.3, Section 9, Table 9.1, and Appendix XIII.")


# ----------------------------------------------------------------------------- 71 AQ2 five signs (built deck, slide 22)
def s71(prs):
    s = kit.base(prs, kicker(71), T("AQ2: Five Early Signs"), notes(71))
    y = lead(s, T("All five early signs, inactivity included, go with later non-completion within module run, by "
                  "similar amounts in 2013 and 2014."))
    lw, rw, rx = kit.split(0.5 if kit.LANG == "en" else 0.57)
    head22 = T("Extra later non-completion with each sign at day 27")
    hh22 = lh(head22, lw, HEAD, True)
    text(s, I(X0), I(y), I(lw), I(hh22), head22, size=HEAD, color=NAVY, bold=True, spacing=1.0)
    ky = bottom_key(s, T("Key: dot = risk difference; whisker = 95% interval; dashed line = the 5-point criterion; "
                         "TMA = tutor-marked assignment. Task signs on runs with a task due by day 27; click signs on "
                         "all runs."), X0, lw)
    chart(s, "m5-full-p4-aq2-signs", X0, y + hh22 + 0.05, lw, ky - y - hh22 - 0.15, aq2_dots)
    paras = [
        tb("The five signs: ", "the rule's three parts (Missed task, Late TMA, No click in the last 7 days, that is "
                               "days 21–27) and two activity signs tested only here: Activity below the run median "
                               "(clicks on days 0–27) and No click before the start (day 0)."),
        tb("Risk difference: ", "the extra percentage points of later non-completion among enrolments with the sign "
                                "against those without, within module run, adjusted for the other signs."),
        tb("Population: ", "registered at day 27; 11,811 enrolments in 2013 (44.4% non-completion) and 15,724 in "
                           "2014 (44.0%); task signs on 9,960 and 12,585."),
        tb("Criterion: ", "at least 5 points, an interval excluding 0, and the same direction (more non-completion "
                          "with the sign) in two-thirds of modules."),
        [(T("These are associations, not causes."), AGENT_INK, True)]]
    kit.room("aq2 text", y + rich_h(paras, rw), END)
    rich(s, rx, y, rw, paras, pt=fit_pt(paras, rw, END - y))
    src(s, "Source: Milestone 5 report, Sections 9 and 11.3, Table 9.1 and Appendices VIII and XIII, "
           "Figure A.3 and Table A.33.")


# ----------------------------------------------------------------------------- 72 AQ2 by module
MODS = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
SIGNS = ["Missed task", "Late TMA", "No click in the last 7 days", "Activity below the run median",
         "No click before the start"]
# Table A.34: mutually adjusted risk difference by module (estimate, low, high); None = not defined or not run.
A34 = {2013: [[(48.1, 28.7, 67.5), (45.3, 40.4, 50.1), None, (35.4, 30.5, 40.2), None, (40.2, 34.0, 46.3), None],
              [(20.5, 6.3, 34.7), (21.8, 16.0, 27.5), None, (15.6, 4.4, 26.9), None, (22.3, 16.0, 28.7), None],
              [(7.4, -5.2, 20.1), (8.9, 4.7, 13.1), None, (22.0, 12.7, 31.3), (27.5, 18.2, 36.8), (13.9, 8.2, 19.5),
               (3.8, -3.5, 11.2)],
              [(8.3, -0.8, 17.3), (10.8, 7.3, 14.4), None, (13.7, 10.0, 17.4), (15.8, 9.3, 22.3), (16.1, 12.6, 19.5),
               (10.9, 3.5, 18.3)],
              [(9.4, -8.6, 27.5), (7.6, 3.9, 11.3), None, (12.9, 6.5, 19.3), (17.6, 9.7, 25.6), (11.2, 5.2, 17.2),
               (5.0, -1.6, 11.6)]],
       2014: [[(39.4, 20.9, 57.8), (53.4, 47.9, 58.8), (34.5, 29.4, 39.6), (36.6, 30.5, 42.7), None,
               (33.0, 26.9, 39.2), None],
              [(-1.2, -14.4, 12.1), (25.4, 18.7, 32.2), None, (19.5, 11.0, 28.0), None, (22.5, 12.7, 32.3), None],
              [(12.7, -0.1, 25.5), (11.1, 6.9, 15.4), (16.0, 11.6, 20.3), (14.2, 7.1, 21.3), (19.0, 12.3, 25.6),
               (20.1, 12.1, 28.2), (16.0, 10.6, 21.4)],
              [(7.1, -2.9, 17.2), (9.2, 5.5, 12.8), (14.2, 10.7, 17.6), (17.7, 13.7, 21.7), (18.5, 13.6, 23.5),
               (17.9, 14.4, 21.4), (12.1, 6.6, 17.5)],
              [(8.1, -10.4, 26.7), (1.2, -2.4, 4.9), (11.0, 5.9, 16.0), (5.6, -1.4, 12.6), (22.9, 16.8, 29.0),
               (8.9, 3.7, 14.2), (7.7, 2.7, 12.7)]]}


def module_heat(fig):
    ax = charts.axes(fig)
    colors = pal.sequential(7, pal.BLUE)
    cm = pal.cmap(colors)
    rows, labels = [], []
    for yr in (2013, 2014):
        rows.append(None)
        labels.append(str(yr))
        for k, sg in enumerate(SIGNS):
            rows.append(A34[yr][k])
            labels.append(T(sg))
    for i, row in enumerate(rows):
        if row is None:
            continue
        for j, cell in enumerate(row):
            if cell is None:
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fc=pal.SOFT, ec="white", lw=1.5, zorder=2))
                ax.text(j, i, "–", ha="center", va="center", fontsize=charts.size("value"), color=C_MUTED, zorder=3)
                continue
            v, lo, hi = cell
            fill = charts.matplotlib.colors.to_hex(cm(max(0.0, min(1.0, v / 50))))
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fc=fill, ec="white", lw=1.5, zorder=2))
            inc0 = lo <= 0
            ax.text(j, i, fmt(v, 1), ha="center", va="center", fontsize=charts.size("value"),
                    color=pal.text_on(fill), fontstyle="italic" if inc0 else "normal", zorder=4)
            if inc0:
                exc = v < 0
                ax.add_patch(Rectangle((j - 0.44, i - 0.42), 0.88, 0.84, fc="none",
                                       ec=f"#{kit.C_RED}" if exc else C_INK, lw=2.0 if exc else 1.0,
                                       ls="-" if exc else (0, (3, 2)), zorder=3))
    ax.set_xlim(-0.5, len(MODS) - 0.5)
    ax.set_ylim(len(rows) - 0.5, -0.5)
    ax.set_xticks(range(len(MODS)), MODS)
    ax.xaxis.tick_top()
    ax.set_yticks(range(len(rows)), labels)
    for t, r in zip(ax.get_yticklabels(), rows):
        if r is None:
            t.set_fontweight("bold")
            t.set_color(C_INK)
    for side in ("bottom", "left", "right", "top"):
        ax.spines[side].set_visible(False)


def s72(prs):
    s = kit.base(prs, kicker(72), T("AQ2: Consistent Across Modules"), notes(72))
    y = lead(s, T("Each sign points the same way in every module in 2013 and in 29 of 30 module estimates in 2014, but "
                  "its size varies between modules."))
    lw, rw, rx = kit.split(0.58)
    y2 = head_line(s, X0, y, lw, T("Risk difference by module, points, adjusted for the other signs"))
    ky = bottom_key(s, T("Key: darker cell = larger risk difference; – = sign not defined (no task due by day 27) or "
                         "module not run; italic with dashed frame = 95% interval includes 0; red frame = the one "
                         "estimate in the opposite direction. AAA–GGG = the seven anonymised modules of the Open University "
                         "Learning Analytics Dataset."), X0, lw)
    chart(s, "m5-full-p4-aq2-modules", X0, y2, lw, ky - y2 - 0.1, module_heat)
    items = [(T("Direction holds"), [T("2013: every sign keeps its direction in every module where it is defined (4 "
                                       "of 4 for the task signs, 6 of 6 for the click signs). 2014: 29 of 30 module "
                                       "estimates.")]),
             (T("One wide exception"), [T("A late TMA (tutor-marked assignment) in AAA 2014: −1.2 points on 348 "
                                          "enrolments, interval −14.4 to 12.1, which includes 0. No CCC student had "
                                          "a late TMA by day 27.")], MINUS),
             (T("Size varies"), [T("No click in the last 7 days goes with 27.5 points in EEE but 3.8 in GGG (2013). "
                                   "Intervals that include 0 lie mostly in the small module AAA: no evidence there, "
                                   "not evidence of no information. Consistency means the same direction, not the "
                                   "same size.")], AGENT_INK, ACC_FILL, WARM)]
    stack(s, rx, y, rw, items, END, gap=0.18)
    src(s, "Source: Milestone 5 report, Section 11.3 and Appendix XIII, Table A.34.")


# ----------------------------------------------------------------------------- 73 AQ2 sensitivity runs
# Table A.35 (2013): primary analysis, then the six variants, per sign (missed, late, inactive, below median, pre-start).
A35 = [("Primary analysis", [40.8, 20.2, 14.5, 13.4, 10.6]),
       ("De-duplicated clicks", [40.9, 20.4, 14.7, 13.0, 10.6]),
       ("Late CMAs counted as late", [40.6, 15.2, 14.4, 13.5, 10.6]),
       ("Flagged enrolments removed", [40.8, 20.2, 14.4, 13.4, 10.6]),
       ("Runs with no task due removed", [40.8, 20.2, 14.2, 13.4, 10.4]),
       ("Low activity at half the median", [40.6, 21.6, 13.6, 14.7, 11.3]),
       ("One sign effect for all modules", [40.8, 21.0, 11.5, 13.4, 9.6])]


def sens_dots(fig):
    ax = charts.axes(fig)
    n = len(SIGNS)
    ax.set_ylim(n - 0.5, -0.7)
    ax.set_xlim(0, 46)
    ax.axvline(5, color=C_MUTED, lw=1.2, ls=(0, (4, 3)), zorder=1)
    for i in range(n):
        vals = [row[1][i] for row in A35[1:]]
        ax.plot([min(vals + [A35[0][1][i]]), max(vals + [A35[0][1][i]])], [i, i], color=f"#{kit.C_GRID}", lw=6,
                solid_capstyle="round", zorder=1)
        for k, v in enumerate(vals):
            ax.plot(v, i + (k - 2.5) * 0.06, "o", ms=7, color=C_GREY, mec="white", mew=0.8, zorder=2)
        p = A35[0][1][i]
        ax.plot(p, i, "o", ms=11, color=C_ACC, mec="white", mew=1.2, zorder=3)
        ax.annotate(fmt(p, 1), (max(vals + [p]), i), xytext=(9, 0), textcoords="offset points", ha="left",
                    va="center", fontsize=charts.size("value"), color=C_INK, fontweight="bold")
    ax.annotate(T("15.2: late CMAs counted"), (15.2, 1), xytext=(0, -20), textcoords="offset points", ha="center",
                va="center", fontsize=charts.size("small"), color=C_INK,
                arrowprops=dict(arrowstyle="-", color=C_MUTED, lw=0.8))
    ax.set_yticks(range(n), [T(sg) for sg in SIGNS])
    ax.set_xticks([0, 10, 20, 30, 40])
    charts.ticks(ax.xaxis)
    ax.grid(axis="x", color=f"#{kit.C_GRID}", lw=0.6)
    ax.set_axisbelow(True)
    ax.set_xlabel(T("Risk difference in 2013, percentage points"), fontsize=charts.size("small"), color=C_MUTED)
    handles = [Line2D([], [], color=C_ACC, marker="o", lw=0, ms=9, label=T("Primary analysis")),
               Line2D([], [], color=C_GREY, marker="o", lw=0, ms=7, label=T("Six sensitivity runs")),
               Line2D([], [], color=C_MUTED, lw=1.2, ls=(0, (3, 2)), label=T("5-point criterion"))]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.02), ncol=2, frameon=False, handlelength=1.6,
              columnspacing=1.2, borderaxespad=0, fontsize=charts.size("small"))


def s73(prs):
    s = kit.base(prs, kicker(73), T("AQ2: Sensitivity Runs"), notes(73))
    y = lead(s, T("Six sensitivity runs in each year change no verdict: every sign stays above 5 points with an "
                  "interval excluding 0."))
    lw, rw, rx = kit.split(0.57)
    y2 = head_line(s, X0, y, lw, T("Each sign under the primary analysis and six sensitivity runs, 2013"))
    ky = bottom_key(s, T("Key: sensitivity run = the same model with one analysis choice changed: de-duplicated clicks; "
                         "late CMAs (computer-marked assessments) counted as late, beside late TMAs (tutor-marked assignments); flagged enrolments removed; the 2 "
                         "runs with no task due removed; low activity cut at half the run median; one sign effect for "
                         "all modules. The grey band spans all seven estimates."), X0, lw)
    chart(s, "m5-full-p4-aq2-sensitivity", X0, y2, lw, ky - y2 - 0.1, sens_dots)
    items = [(T("Largest shift"), [T("Counting late CMAs lowers the late sign from 20.2 to 15.2 points, because by day "
                                     "27 a late CMA occurs only in DDD 2013B, in 85.65% of its enrolments.")]),
             (T("2014 agrees"), [T("The same six runs leave every 2014 verdict unchanged: the smallest estimate under "
                                   "any of them is 6.9 points, with a lowest interval bound of 4.3.")]),
             (T("All 22 runs pooled"), [T("On 27,535 enrolments registered at day 27, the five signs go with 39.8, "
                                          "20.6, 14.7, 14.0 and 9.4 points and meet the criterion in every module.")])]
    stack(s, rx, y, rw, items, END, gap=0.18)
    src(s, "Source: Milestone 5 report, Appendix XIII, Table A.35 and the sections on sensitivity runs and on the "
           "comparison of the two years.")


# ----------------------------------------------------------------------------- 74 AQ2 activity gradient
A36 = [("No click", 5.6, 3.0), ("Under ½\nmedian", 2.6, 1.7), ("½ median\nto median", -3.7, 1.8),
       ("Median\nto 2×", 1.9, 1.5), ("2× median\nor more", -2.6, 1.8)]


def residual_bars(fig):
    ax = charts.axes(fig)
    n = len(A36)
    ax.set_xlim(-0.6, n - 0.4)
    ax.set_ylim(-6.5, 8.0)
    ax.axhline(0, color=C_MUTED, lw=1.0, zorder=1)
    for i, (lab, v, band) in enumerate(A36):
        ax.add_patch(Rectangle((i - 0.42, -band), 0.84, 2 * band, fc=f"#{kit.C_GRID}", ec="none", zorder=1))
        ax.bar(i, v, 0.46, color=C_ACC, zorder=3)
        ax.annotate(fmt(v, 1, sign=True), (i, v), xytext=(0, 3 if v > 0 else -3), textcoords="offset points",
                    ha="center", va="bottom" if v > 0 else "top", fontsize=charts.size("value"), color=C_INK,
                    fontweight="bold")
    ax.set_xticks(range(n), [T(r[0]) for r in A36])
    ax.set_yticks([-6, -3, 0, 3, 6])
    ax.yaxis.set_major_formatter(charts.matplotlib.ticker.FuncFormatter(lambda v, _: fmt(v, 0, sign=v != 0)))
    ax.set_ylabel(T("Observed minus predicted, points"), fontsize=charts.size("small"), color=C_MUTED)
    ax.set_xlabel(T("Clicks on days 0–27, against the run median"), fontsize=charts.size("small"), color=C_MUTED)
    handles = [Patch(fc=C_ACC, label=T("Residual")),
               Patch(fc=f"#{kit.C_GRID}", label=T("±2 standard-error band"))]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0, 1.02), ncol=2, frameon=False, handlelength=1.4,
              columnspacing=1.2, borderaxespad=0, fontsize=charts.size("small"))


def s74(prs):
    s = kit.base(prs, kicker(74), T("AQ2: Activity Works as a Gradient"), notes(74))
    y = lead(s, T("The yes-or-no click signs miss a graded activity pattern; with clicks as a continuous measure, the "
                  "below-median sign falls below the criterion in 2014 while the other four still meet it."))
    lw, rw, rx = kit.split(0.47)
    msg = [[(T("Chosen after seeing the residuals, "), WHITE, True),
            (T("so the added run qualifies the verdict; the planned estimates remain the primary result. Design "
               "consequence: the AQ3 model (the predictive question) uses continuous click measures."), WHITE, False)]]
    mh = rich_h(msg, CWI - 0.6) + 0.2
    yb = END - mh
    y2 = head_line(s, X0, y, lw, T("Model error by activity level, 2013"))
    k74 = T("Key: residual = observed minus predicted non-completion; all five levels lie outside their band. "
            "11,811 enrolments.")
    kh = lh(k74, lw, PT["small"])
    chart(s, "m5-full-p4-aq2-residuals", X0, y2, lw, yb - 0.2 - kh - 0.05 - y2, residual_bars)
    key(s, yb - 0.2 - kh, k74, X0, lw)
    y3 = head_line(s, rx, y, rw, T("Risk difference, planned → with clicks as a continuous adjustment, points"))
    rows = [[T("Sign"), "2013", "2014"],
            [T("Missed task"), num("40.8 → 37.3"), num("39.3 → 35.6")],
            [T("Late TMA"), num("20.2 → 19.5"), num("20.3 → 19.5")],
            [T("No click in the last 7 days"), num("14.5 → 9.3"), num("15.8 → 10.7")],
            [T("Activity below the run median"), num("13.4 → 5.8"), T("14.6 → 5.9: same direction in 4 of 7 modules, "
                                                                 "criterion not met")],
            [T("No click before the start"), num("10.6 → 8.9"), num("8.7 → 6.5")]]
    widths = [I(rw * f) for f in (0.4, 0.22)]
    widths.append(I(rw) - sum(widths))
    k74b = T("Key: continuous adjustment = log(1 + clicks on days 0–27) added to the model; TMA = tutor-marked "
             "assignment.")
    kbh = lh(k74b, rw, PT["small"])
    size = BODY if y3 + table_h(rows, widths, BODY) <= yb - 0.3 - kbh else PT["small"]
    shape = table(s, I(rx), I(y3), I(rw), rows, widths, size=size)
    cell = shape.table.cell(4, 2)
    cell.fill.solid()
    cell.fill.fore_color.rgb = BAD_FILL
    for r in cell.text_frame.paragraphs[0].runs:
        r.font.color.rgb, r.font.bold = MINUS, True
    th = stretch_table(shape, yb - 0.2 - kbh - 0.08 - y3)
    key(s, y3 + th + 0.08, k74b, rx, rw)
    rect(s, MX, I(yb), CW, I(mh), fill=NAVY, radius=True)
    rich(s, X0 + 0.3, yb + 0.1, CWI - 0.6, msg, color=WHITE)
    src(s, "Source: Milestone 5 report, Section 11.3 and Appendix XIII, Table A.36 and the section on sensitivity runs "
           "and model checks.")


# ----------------------------------------------------------------------------- 75 AQ2 meaning
def s75(prs):
    s = kit.base(prs, kicker(75), T("AQ2: What the Signs Mean for the List"), notes(75))
    y = lead(s, T("The signs give each name on a contact list a factual reason staff can check and show that the "
                  "early-sign rule needs its activity part, but they do not show that contact would help."))
    msg = [[(T("Confidence: moderate. "), WHITE, True),
            (T("Two years agree, but the click signs rest on a known misfit, and unrecorded reasons could explain the "
               "associations."), WHITE, False)]]
    mh = rich_h(msg, CWI - 0.6) + 0.2
    yb = END - mh
    xs, tw = cols(3, 0.25)
    tiles = [(T("40.8 points"), T("The strongest sign, a missed task, in 2013 (39.3 in 2014)."), WARM),
             (T("19.6%"), T("of 2013 non-completers (Fail or Withdrawn) had missed a task by week 4; 14.7% in 2014."),
              NAVY),
             (T("6 of 22 runs"), T("had no task due by day 27, while the click signs are defined in every run."),
              NAVY)]
    th = max(kit.num_h(40) + 0.05 + lh(b, tw - 0.3, BODY) for _, b, _ in tiles) + 0.25
    for x, (v, b, c) in zip(xs, tiles):
        rect(s, I(x), I(y), I(tw), I(th), fill=SOFT, line=LINE, radius=True)
        text(s, I(x), I(y + 0.1), I(tw), I(kit.num_h(40)), v, size=40, color=c, bold=True, align=PP_ALIGN.CENTER,
             spacing=1.0)
        text(s, I(x + 0.15), I(y + 0.1 + kit.num_h(40) + 0.05), I(tw - 0.3), I(lh(b, tw - 0.3, BODY)), b, size=BODY,
             color=INK, align=PP_ALIGN.CENTER, spacing=1.0)
    cy = y + th + 0.2
    xc, cw = cols(2, 0.25)
    can = [T("Give each listed name a factual reason that a member of staff checks against the record."),
           T("Show that each part of the early-sign rule (missed task, late tutor-marked assignment, no click in the "
             "last 7 days) carries "
             "information on its own, inactivity included."),
           T("Suggest, as a hypothesis, where early support could go.")]
    cannot = [T("Show a cause: a student who stops clicking may already have decided to leave."),
              T("Show that contacting a flagged student helps."),
              T("Justify treating a group differently: the missed-task sign holds in each of the 15 groups of 2013, as "
                "a description.")]
    h = yb - 0.2 - cy
    pt = next((p for p in (PT["lead"], PT["body"], BODY)
               if max(card_h(T("The signs can"), can, cw, p, max(HEAD, p)),
                      card_h(T("The signs cannot"), cannot, cw, p, max(HEAD, p))) <= h), BODY)
    kit.room("aq2 can cards", max(card_h(T("The signs can"), can, cw, pt), card_h(T("The signs cannot"), cannot, cw,
                                                                                   pt)), h)
    card(s, xc[0], cy, cw, T("The signs can"), can, color=OUT_INK, h=h, fill=OUT_FILL, line=PLUS, pt=pt,
         hp=max(HEAD, pt), line_w=2.0)
    card(s, xc[1], cy, cw, T("The signs cannot"), cannot, color=MINUS, h=h, fill=BAD_FILL, line=MINUS, pt=pt,
         hp=max(HEAD, pt), line_w=2.0)
    rect(s, MX, I(yb), CW, I(mh), fill=NAVY, radius=True)
    rich(s, X0 + 0.3, yb + 0.1, CWI - 0.6, msg, color=WHITE)
    src(s, "Source: Milestone 5 report, Sections 11.2 and 11.3, Appendix XII, Table A.31, and Appendix XIII, Table "
           "A.33 and the sections on groups of students and on what AQ2 means for the project.")


# ----------------------------------------------------------------------------- 76 AQ3 and AQ4: the ranked list
def s76(prs):
    s = kit.base(prs, kicker(76), T("AQ3 and AQ4: The Ranked List"), notes(76))
    y = lead(s, T("A model built on 2013 ranks the 2014 students slightly better than the early-sign rule, and its "
                  "list gives a reason beside each name; it is a rank, not a probability."))
    neither = [[(T("Neither answer says "), AGENT_INK, True),
                (T("who should make contact or whether contact helps, and the order of risk is not shown to match "
                   "the need for help."), INK, False)]]
    nh = rich_h(neither, CWI - 0.36, PT["body"]) + 0.25
    ny = END - nh
    rect(s, MX, I(ny), CW, I(nh), fill=ACC_FILL, line=WARM, radius=True, line_w=2.0)
    rich(s, X0 + 0.18, ny + 0.12, CWI - 0.36, neither, pt=PT["body"])
    items = [(T("AQ3 – Predictive: Answered"),
              [tb("Both cut-offs: ", "lists of 5 per 20 hold 38.6% of later non-completers at day 13 and 41.5% at "
                                     "day 27, so waiting two more weeks adds little."),
               tb("Model and rule: ", "they share most names; each list holds 903 students the other does not, and "
                                      "of the students only the model picks, 59.7% do not complete; of those only the rule picks, 50.6%."),
               tb("Probability: ", "the predicted risks match the observed rates (calibration) in only 5 of the 13 "
                                  "runs, so staff see ranks and reasons.")]),
             (T("AQ4 – Prescriptive: Partial"),
              [tb("Order: ", "per 20 students (the size of one tutor group), the top-ranked student is a later non-completer 92.4% of the "
                             "time, the fifth 57.6%, the sixth 55.2%; from the seventh on, 47.3% or less, close to the base rate of "
                             "44.0% (2014 non-completion at day 27)."),
               tb("Reasons: ", "for 80.7% of listed students the main reason is behaviour (low activity, a missed "
                               "task or a late submission)."),
               tb("Fairness: ", "the fairness check (a group reached over 10 points less well than other students) found none "
                                "of the three groups fixed in advance disadvantaged (students with a declared "
                                "disability; in the most deprived band; with no deprivation band recorded).")])]
    xs, cw = cols(2, 0.3)
    room = ny - 0.2 - y
    pt = min(fit_pt(b, cw - 0.36, room - lh(a, cw - 0.36, HEAD, True) - 0.45) for a, b in items)
    kit.room("aq34 cards", max(card_h(a, b, cw, pt=pt) for a, b in items), room)
    for k, (x, (a, b)) in enumerate(zip(xs, items)):
        card(s, x, y, cw, a, b, h=room, pt=pt, fill=ACC_FILL if k == 0 else SOFT, line=WARM if k == 0 else LINE,
             line_w=1.5 if k == 0 else 1.0)
    src(s, "Source: Milestone 5 report, Sections 10 and 11.4, and Appendix XIV, Table A.37.")


# ----------------------------------------------------------------------------- 77 answers by question
def s77(prs):
    s = kit.base(prs, kicker(77), T("Answers by Question"), notes(77))
    y = lead(s, T("We can describe the size and timing of non-completion, name its early signs and rank students "
                  "slightly better than the rule; we cannot say whether contact helps."))
    rows = [[T("Question"), T("Evidence and method"), T("Main finding"), T("Confidence"),
             T("Implication for decision")],
            [T("AQ1, descriptive"), T("22 runs, day 14: 28,061 enrolments; rates under two denominators"),
             T("45.3% did not complete; runs 24.9–58.3%; under 20% of non-completers missed a task by week 4"),
             T("High for OULAD 2013–2014; KPI proxy"), T("D2 hypothesis; tasks alone come too late")],
            [T("AQ2, diagnostic"), T("Day 27: 11,811 and 15,724; logistic, run fixed effects"),
             T("Five signs consistent in both years; missed task 40.8 and 39.3 points"),
             T("Moderate; association"), T("D1 reasons; contact to test")],
            [T("AQ3, predictive"), T("Train 2013: 11,811; test 2014: 15,724; penalised logistic, gate S1"),
             T("S1 met: 0.725 vs 0.704; 41.5% of non-completers on lists of 5 per 20"),
             T("Moderate; ranks only, calibration fails in 8 of 13 runs"), T("D1 order; the rule as fallback")],
            [T("AQ4, prescriptive ranking"), T("AQ3 scores, 2014: 15,724; top-k per run; FR1"),
             T("1st contact 92.4%, 7th 47.3% non-completers; FR1: none flagged"), T("Moderate; no contact data"),
             T("D1 list of up to about 6 per 20, not a contact plan")]]
    fr = (0.15, 0.21, 0.27, 0.16)
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    k77 = T("Key: orange = answered on data; blue = answered for the ranking, contact part without data. D1 = whom "
            "to contact; D2 = where "
            "support time goes; S1 = the gate a model must pass to replace the early-sign rule; FR1 = the fairness "
            "review rule; KPI = key performance indicator; OULAD = Open University Learning Analytics Dataset.")
    kh = lh(k77, CWI, PT["small"])
    room = END - kh - 0.1 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    colour_cells(shape, rows, 0, [WARM, WARM, WARM, kit.BLUE])
    th = stretch_table(shape, room)
    key(s, y + th + 0.1, k77)
    src(s, "Source: Milestone 5 report, Section 11.5, Table 11.3, and Appendix XIV, Tables A.38 and A.39.")


# ----------------------------------------------------------------------------- 78–80 decision support
def s78(prs):
    s = kit.base(prs, kicker(78), T("Decision D1: Whom to Contact"), notes(78))
    y = lead(s, T("For whom to contact, the AQ3 model ranks the list with the signs shown as reasons, and the "
                  "early-sign rule, which holds 97% of the model's hits, is its fallback."))
    y = owner(s, y, T("course lecturers, lecturer-advisors and the support office, at each review point"),
              T("a reversible decision"))
    k78 = T("Key: early-sign rule = a task due but not submitted, a late TMA (tutor-marked assignment) or no click in "
            "the last 7 days; S1 = the gate the AQ3 model (predictive question) must pass to replace the rule's "
            "order, met on the 2014 test; FR1 = the fairness review rule; AQ2–AQ4 = the diagnostic, predictive and "
            "ranking questions.")
    note78 = [tb("Why ranking matters: ", "the rule flags 28.8% of the 27,535 enrolments registered at day 27 across "
                                          "the 22 runs, more than a list of 5 per 20 students (25%) can hold, so the "
                                          "list is ordered by the number of signs.")]
    kh = lh(k78, CWI, PT["small"])
    ky = END - kh
    items = [(T("Evidence now"),
              [tb("AQ2: ", "a missed task goes with 40.8 more points of non-completion (37.7–43.9) in 2013, and each "
                           "part of the rule carries information on its own."),
               tb("AQ3, AQ4: ", "model lists of 5 per 20 hold 41.5% of later non-completers (rule 40.3%, random "
                                "25.1%); gate S1 met; FR1 flags no group.")]),
             (T("Decision option"),
              [T("Build the pilot's week-3 and week-5 lists from the AQ3 ranking, at most about 6 per 20 students, "
                 "shown as ranks with behavioural reasons."),
               T("A member of staff checks every name; the early-sign rule, ordered by its number of signs, is the "
                 "fallback.")],
              AGENT_INK, ACC_FILL, WARM),
             (T("Check before adoption"),
              [T("The model's order still holds on the university's own records, recounted before the pilot."),
               T("Contact raises completion against usual support: a randomised pilot, with the contact person and "
                 "the offer left open.")])]
    xs3, cw3 = cols(3, 0.5)
    hnat = max(card_h(it[0], it[1], cw3, BODY) for it in items) + 0.1
    flow3(s, y, y + hnat, items)
    by = y + hnat + 0.2
    bh = ky - 0.12 - by
    nw = 3.0
    npt = PT["lead"] if rich_h(note78, CWI - nw - 0.5, PT["lead"]) + 0.15 <= bh else PT["body"]
    kit.room("d1 number box", max(kit.num_h(PT["number"]), rich_h(note78, CWI - nw - 0.5, npt)) + 0.15, bh)
    rect(s, MX, I(by), CW, I(bh), fill=SOFT, line=LINE, radius=True)
    text(s, I(X0), I(by), I(nw), I(bh), T("28.8%"), size=PT["number"], color=WARM, bold=True, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    nt = rich_h(note78, CWI - nw - 0.5, npt)
    rich(s, X0 + nw + 0.2, by + (bh - nt) / 2 + 0.04, CWI - nw - 0.5, note78, pt=npt)
    key(s, ky, k78)
    src(s, "Source: Milestone 5 report, Section 11.5, Appendices VIII and IX, and Appendix XIV, Table A.40.")


def d2_bars(fig):
    ax = charts.axes(fig)
    cats = ["AAA", "EEE", "GGG", "BBB", "FFF", "DDD", T("October start"), T("February start")]
    vals = [AQ1_2013[m] for m in ["AAA", "EEE", "GGG", "BBB", "FFF", "DDD"]] + [(42.4, 41.3, 43.5),
                                                                              (51.6, 50.1, 53.1)]
    n = len(cats)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xlim(0, 68)
    for i, (v, lo, hi) in enumerate(vals):
        col = C_ACC if v >= 50 else C_GREY
        ax.barh(i + (0.25 if i >= 6 else 0), v, 0.62, color=col, zorder=3)
        ax.plot([lo, hi], [i + (0.25 if i >= 6 else 0)] * 2, color=C_INK, lw=1.0, zorder=4)
        ax.annotate(fmt(v, 1) + "%", (hi, i + (0.25 if i >= 6 else 0)), xytext=(4, 0), textcoords="offset points",
                    ha="left", va="center", fontsize=charts.size("value"), color=C_INK)
    ax.set_yticks([i + (0.25 if i >= 6 else 0) for i in range(n)], cats)
    ax.set_ylim(n - 0.25, -0.5)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)


def s79(prs):
    s = kit.base(prs, kicker(79), T("Decision D2: Where Support Time Goes"), notes(79))
    y = lead(s, T("Support time could go first where non-completion and early signs are highest, as a hypothesis to "
                  "check on the university's own records."))
    y = owner(s, y, T("the program manager, for the time of the support office and the lecturer-advisors"),
              T("each semester"))
    lw = 3.9
    k79 = T("Key: bar = non-completion among students registered at day 14, 2013 (modules AAA–GGG of the Open "
            "University Learning Analytics Dataset, then all runs by start month); line = 95% Wilson interval; orange "
            "= above 50%. AQ1, AQ2 = the descriptive and diagnostic questions.")
    kh = lh(k79, lw, PT["small"])
    y2 = head_line(s, X0, y, lw, T("Where losses concentrate, 2013"))
    chart(s, "m5-full-p4-d2-modules", X0, y2, lw, END - kh - 0.08 - y2, d2_bars)
    key(s, END - kh, k79, X0, lw)
    rx = X0 + lw + 0.35
    xs, cw = cols(3, 0.5, rx, XR - rx)
    items = [(T("Evidence now"),
              [tb("AQ1: ", "non-completion from 24.9% to 57.5% between the runs of 2013; February runs 51.6% against "
                           "October runs 42.4%."),
               tb("AQ2: ", "no click on days 21–27 in 54.8% of GGG 2013J but 7.6% of DDD 2013B.")]),
             (T("Decision option, a hypothesis"),
              [T("Place early support time first in the courses and intakes with the highest non-completion and the "
                 "highest share of early signs, measured on the university's own records."),
               [(T("Caution: "), MINUS, True), (T("high risk marks where losses concentrate, not where support helps "
                                                  "most."), INK, False)]],
              AGENT_INK, ACC_FILL, WARM),
             (T("Check before adoption"),
              [T("The pattern repeats in the university's courses over several semesters."),
               T("The baseline is recounted under the add-drop rule: only students still registered at day 14 "
                 "count.")])]
    pt = next((p for p in (PT["body"], BODY) if max(card_h(a, b, cw, p) for a, b, *_ in items) <= END - y), BODY)
    kit.room("d2 cards", max(card_h(a, b, cw, pt) for a, b, *_ in items), END - y)
    for k, (x, it) in enumerate(zip(xs, items)):
        c, f, ln = (it[2], it[3], it[4]) if len(it) > 2 else (NAVY, SOFT, LINE)
        card(s, x, y, cw, it[0], it[1], color=c, h=END - y, fill=f, line=ln, pt=pt, line_w=2.0 if ln != LINE else 1.0)
        if k < 2:
            arrow(s, x + cw + 0.06, y + (END - y) / 2, x + cw + 0.44, y + (END - y) / 2)
    src(s, "Source: Milestone 5 report, Section 11.5, Appendix XII, Table A.30, and Appendix XIV, Table A.40. Run "
           "codes: B = February start, J = October start.")


def s80(prs):
    s = kit.base(prs, kicker(80), T("Decision D3: Whether to Extend"), notes(80))
    y = lead(s, T("For extending the approach, the project offers a measurement method, a gate and a fairness audit, "
                  "not a verdict; extension waits for a pilot result."))
    y = owner(s, y, T("leadership with the legal and data office, on the pilot's results"),
              T("close to a one-way door"), color=MINUS)
    msg = T("Even a negative pilot result shows, at small scale, which part of the path fails.")
    mh = lh(msg, CWI - 0.6, PT["lead"], True) + 0.3
    k80 = T("Key: D3 = whether to extend the approach to all courses and link data routinely; S1 = the gate to "
            "replace the early-sign rule; FR1 = the fairness review rule; AQ1 = the descriptive question; AI = "
            "artificial intelligence.")
    kh = lh(k80, CWI, PT["small"])
    yb = END - mh
    ky = yb - 0.15 - kh
    bottom = ky - 0.15
    xs, cw = cols(3, 0.5)
    ev = [T("The denominator alone can move a completion rate by up to 13.6 points."),
          T("AQ3 meets its gate and AQ4 its fairness rule on OULAD, which is not the university."),
          T("No evidence on the effect of contact exists.")]
    pt = next((p for p in (PT["lead"], PT["body"]) if card_h(T("Evidence now"), ev, cw, p, max(HEAD, p))
               <= bottom - y), BODY)
    card(s, xs[0], y, cw, T("Evidence now"), ev, h=bottom - y, pt=pt, hp=max(HEAD, pt))
    cols_ = [(T("What the project offers"), AGENT_INK, "agent",
              [(T("A measure"), T("one completion rule (the AQ1 method)")),
               (T("A gate"), T("S1, fixed in advance")), (T("An audit"), T("fairness by rule FR1"))]),
             (T("Extend only if all three hold"), MINUS, "bad",
              [(T("1. A completion gain"), T("against comparison courses")),
               (T("2. Legal approval"), T("Vietnam's rules on high-risk AI")),
               (T("3. Staff capacity"), T("confirmed for the lists"))])]
    for k, (head, c, st, nodes_) in enumerate(cols_):
        x = xs[k + 1]
        ty = head_line(s, x, y, cw, head, color=c) + 0.05
        nh = (bottom - ty - 2 * 0.12) / 3
        kit.room("d3 nodes", max(node_h(a, [b], cw, body_pt=BODY) for a, b in nodes_), nh)
        for a, b in nodes_:
            node(s, x, ty, cw, nh, a, [b], st, body_pt=BODY)
            ty += nh + 0.12
    for k in range(2):
        ay = y + (bottom - y) / 2
        arrow(s, xs[k] + cw + 0.06, ay, xs[k + 1] - 0.06, ay)
    key(s, ky, k80)
    closing_box(s, yb, msg, h=mh)
    src(s, "Source: Milestone 5 report, Section 11.5, Appendix XII and Appendix XIV, Table A.40.")


# ----------------------------------------------------------------------------- 81–83 limitations
KIND_COL = {"No evidence found": MINUS, "No data to test": kit.BLUE, "Measurement": kit.VIOLET,
            "Scope": kit.TEAL, "Scope and causal": kit.TEAL}


def s81(prs):
    s = kit.base(prs, kicker(81), T("Kinds of Limit"), notes(81))
    y = lead(s, T("We keep three kinds of limit apart, because each calls for a different next step."))
    kinds = [(T("No evidence found"), T("A comparison was made and showed no clear difference: for example, the year "
                                        "difference over all enrolments in the six shared modules, −0.2 points (−1.4 "
                                        "to 0.9)."), T("no claim; reported as uncertain"), MINUS),
             (T("No data to test"), T("OULAD and every screened dataset lack the data: contacts and their outcomes, "
                                      "delivery mode, year of study, attendance, staff capacity."),
              T("collect in the randomised pilot"), kit.BLUE),
             (T("Measurement"), T("The AQ3 risks hold as ranks, not probabilities (calibration fails in 8 of 13 "
                                  "runs)."),
              T("ranks and reasons only; a later review point"), kit.VIOLET)]
    conds = [(T("Scope"), T("UK distance-learning modules of 2013–2014; instructional conditions change what predicts "
                            "success.")),
             (T("Confounding"), T("The effect of contact cannot be known from these data.")),
             (T("Ethics"), T("A flag must not become a label: predictive analysis can carry bias and stereotyping."))]
    xs, cw = cols(3, 0.3)
    k81 = T("Key: OULAD = Open University Learning Analytics Dataset, our open stand-in for the university's records.")
    kh = lh(k81, CWI, PT["small"])
    ch = max(card_h(a, [b], cw, BODY) for a, b in conds)
    cy = END - kh - 0.1 - ch
    hy = cy - 0.4
    nh = max(node_h(T("Next step: ") + n, None, cw, head_pt=BODY) for _, _, n, _ in kinds) + 0.05
    ny = hy - 0.25 - nh
    bb = ny - 0.4
    bh = bb - y
    pt = next((p for p in (PT["lead"], PT["body"], BODY)
               if max(0.15 + lh(a, cw - 0.4, HEAD, True) + 0.05 + rich_h([b], cw - 0.4, p) for a, b, _, _ in kinds)
               <= bh), BODY)
    kit.room("limit kinds", max(0.15 + lh(a, cw - 0.4, HEAD, True) + 0.05 + rich_h([b], cw - 0.4, pt)
                                for a, b, _, _ in kinds), bh)
    for x, (a, b, nxt, c) in zip(xs, kinds):
        rect(s, I(x), I(y), I(cw), I(bh), fill=SOFT, line=c, radius=True, line_w=2.0)
        ty = head_line(s, x + 0.2, y + 0.15, cw - 0.4, a, color=c)
        rich(s, x + 0.2, ty, cw - 0.4, [b], pt=pt)
        arrow(s, x + cw / 2, bb + 0.05, x + cw / 2, ny - 0.05, color=c)
        node(s, x, ny, cw, nh, T("Next step: ") + nxt, None, "white", head_pt=BODY)
    head_line(s, X0, hy, CWI, T("Three conditions on every answer"))
    for x, (a, b) in zip(xs, conds):
        card(s, x, cy, cw, a, [b], h=ch, pt=BODY)
    key(s, END - kh, k81)
    src(s, "Source: Milestone 5 report, Section 12 and Appendix XV, Table A.41.")


def s82(prs):
    s = kit.base(prs, kicker(82), T("Limitation Log"), notes(82))
    y = lead(s, T("Each limit is logged with its kind and its handling, so a reader knows where each answer can and "
                  "cannot be used."))
    log = [(T("Year difference over all enrolments in shared modules; small-module click signs (intervals include 0)"),
            "No evidence found", T("No claim; reported as uncertain")),
           (T("Contact and its outcome; delivery mode, year of study, attendance; staff capacity"), "No data to test",
            T("Randomised pilot")),
           (T("Several-modules sign before 2014; approved leave and transfer"), "No data to test",
            T("Described on 2014; university recount")),
           (T("AQ3 probabilities (calibration fails in 8 of 13 runs); active non-completers rarely listed"),
            "Measurement", T("Ranks and reasons only; a later review point")),
           (T("2014 runs described before the AQ3 test"), "Scope", T("Design fixed on 2013; tuning recorded")),
           (T("Binary click signs; below-median sign weak in 2014 once adjusted; KPI proxy and denominator"),
            "Measurement", T("Continuous click measures in AQ3; one add-drop rule")),
           (T("UK distance learning of 2013–2014; observational design"), "Scope and causal",
            T("Re-check on the university's records; options as hypotheses"))]
    rows = [[T("Limitation"), T("Kind"), T("Handling")]] + [[a, T(b), c] for a, b, c in log]
    fr = (0.5, 0.17)
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    k82 = T("Key: kind colours: red = no evidence found; blue = no data to test; violet = measurement; teal = scope, "
            "or scope and causal. Several-modules sign = tasks missed in more "
            "than one module at once; KPI = key performance indicator; add-drop rule = only students still registered at "
            "day 14 count; AQ3, AQ4 = the predictive and ranking questions.")
    kh = lh(k82, CWI, PT["small"])
    room = END - kh - 0.1 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    colour_cells(shape, rows, 1, [KIND_COL[b] for _, b, _ in log])
    for i in range(1, len(rows)):
        for r in shape.table.cell(i, 0).text_frame.paragraphs[0].runs:
            r.font.bold, r.font.color.rgb = False, INK
    th = stretch_table(shape, room)
    key(s, y + th + 0.1, k82)
    src(s, "Source: Milestone 5 report, Section 12, Table 12.1, and Appendix XV, Table A.41.")


def s83(prs):
    s = kit.base(prs, kicker(83), T("Measurement and Model Limits"), notes(83))
    y = lead(s, T("Several design values are assumptions and several estimates are lenient, so the sizes of the "
                  "estimates matter more than the verdicts."))
    rows = [[T("Limit"), T("What it means"), T("What it affects")],
            [T("KPI proxy"), T("Completion of a module run stands for course completion; approved leave or transfer "
                               "counts as withdrawal."), T("The baseline completion rate")],
            [T("Denominator"), T("Who counts as enrolled moves a run's rate by up to 13.6 points."),
             T("Every year comparison")],
            [T("Capacity assumed"), T("3 or 5 contacts per 20 students; runs stand in for each lecturer-advisor's "
                                      "groups."), T("List lengths of D1 and AQ4")],
            [T("Lenient criterion"), T("5 points at a base rate near 44%."), T("AQ2 verdicts: sizes separate the "
                                                                              "signs")],
            [T("Runs held fixed"), T("Intervals treat the runs as fixed; module estimates span 3.8 to 27.5 points."),
             T("How far a later run may differ")],
            [T("Run length"), T("A module run lasts 234 to 269 days, longer than a semester."),
             T("The meaning of “week 4” at the university")],
            [T("No minimum gain"), T("Gate S1 sets no minimum size of gain."),
             T("The pass: 82 more non-completers on 3,955 list places")],
            [T("Fairness trade-off"), T("Fairness criteria cannot all hold when base rates differ."),
             T("One criterion: equal recall at capacity")]]
    fr = (0.17, 0.48)
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    k83 = T("Key: KPI = key performance indicator; D1 = whom to contact; AQ2 = the diagnostic question; AQ4 = the "
            "ranking question; S1 = the gate a model must pass to replace the early-sign rule.")
    kh = lh(k83, CWI, PT["small"])
    room = END - kh - 0.1 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    th = stretch_table(shape, room)
    key(s, y + th + 0.1, k83)
    src(s, "Source: Milestone 5 report, Section 12, Appendix XII, Appendix XIII, Table A.34, and Appendix XV, sections "
           "on measurement and on model and analysis limits.")


# ----------------------------------------------------------------------------- 84–87 future work and the pilot
def s84(prs):
    s = kit.base(prs, kicker(84), T("Future Work in Order"), notes(84))
    y = lead(s, T("One step can run on OULAD as it stands; four need the university, and the last, a randomised "
                  "pilot, alone can show whether contact helps."))
    steps = [(T("1. Later review point"),
              T("Does a list after the second assessed task reach the non-completers who still look active at week "
                "4?"), T("OULAD views extended to the later cut-off, design fixed first"), T("The AQ3 protocol"),
              "white"),
             (T("2. Model check at the university"),
              T("Do the ranking, its small gain over the rule and its fairness hold for the university's courses? "
                "Calibration per course."), T("The university's records of step 3"), T("Step 3"), "ref"),
             (T("3. Transfer to the university"),
              T("Baseline completion under the add-drop rule; the rule on the university's task calendar; AQ1 and AQ2 "
                "re-checked."), T("Two years of the university's records"), T("Data access approved"), "ref"),
             (T("4. Risk classification and consent"),
              T("Is the list a high-risk use, and what human control does it need? Do students accept "
                "activity-based contact?"), T("Legal review; consultation with students"), T("Step 3"), "ref"),
             (T("5. Randomised pilot"),
              T("Does contact raise completion? Which contact and offer work? KPI 1 contact part and KPI 2."),
              T("Contact record: time, person, offer, outcome"), T("Steps 3 and 4"), "agent")]
    k84 = T("Key: AQ1–AQ4 = the descriptive, diagnostic, predictive and ranking questions; AQ3 protocol = the "
            "frozen protocol of the Level 2 prototype; add-drop rule = only students still registered at day 14 count; OULAD = Open University Learning "
            "Analytics Dataset; KPI 1 = early-sign contact rate; KPI 2 = follow-up rate.")
    kh = lh(k84, CWI, PT["small"])
    xs, sw = cols(5, 0.28)
    by = y + 0.45
    top_rise = 0.15                                  # each step sits higher than the one before (a staircase)
    bottom = END - kh - 0.12

    def step_need(k, pt):
        h_, a, d, dep, _ = steps[k]
        sy = by + (4 - k) * top_rise
        return sy + 0.12 + lh(h_, sw - 0.24, HEAD, True) + 0.05 + rich_h(
            [a, T("Data: ") + d, T("Depends on: ") + dep], sw - 0.24, pt)
    pt = BODY if all(step_need(k, BODY) <= bottom - 0.08 for k in range(5)) else PT["small"]
    for k, (h_, a, d, dep, st) in enumerate(steps):
        sy = by + (4 - k) * top_rise
        fill, line_c, hc, _ = kit.NODE_STYLES[st]
        rect(s, I(xs[k]), I(sy), I(sw), I(bottom - sy), fill=fill, line=line_c, radius=True, line_w=1.5)
        ty = head_line(s, xs[k] + 0.12, sy + 0.12, sw - 0.24, h_, color=hc)
        paras = [a, [(T("Data: "), hc, True), (d, INK, False)], [(T("Depends on: "), hc, True), (dep, INK, False)]]
        kit.room("future step", ty + rich_h(paras, sw - 0.24, pt), bottom)
        rich(s, xs[k] + 0.12, ty, sw - 0.24, paras, pt=pt)
        if k < 4:
            ay = by + (4 - k) * top_rise + 0.35
            arrow(s, xs[k] + sw + 0.03, ay, xs[k + 1] + 0.0 - 0.03, ay - top_rise)
    for x1, x2, lab, c in [(xs[0], xs[0] + sw, T("On OULAD now"), NAVY), (xs[1], xs[4] + sw, T("At the university"),
                                                                       kit.BLUE)]:
        rect(s, I(x1), I(y + 0.12), I(x2 - x1), I(0.03), fill=c)
        rect(s, I(x1), I(y + 0.04), I(0.03), I(0.1), fill=c)
        rect(s, I(x2 - 0.03), I(y + 0.04), I(0.03), I(0.1), fill=c)
        text(s, I(x1), I(y + 0.17), I(x2 - x1), I(0.25), lab, size=PT["small"], color=c, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
    key(s, END - kh, k84)
    src(s, "Source: Milestone 5 report, Section 12.1 and Appendix XV, Table A.42.")


def s85(prs):
    s = kit.base(prs, kicker(85), T("Next at the University: Recount and Replace Assumptions"), notes(85))
    y = lead(s, T("At the university, the baseline is recounted under the add-drop rule, the early-sign rule is checked "
                  "on its task calendar, and every assumed value is replaced by its records."))
    lw, rw, rx = kit.split(0.46)
    k85 = T("Key: add-drop rule = only students still registered at day 14 count; FR1 = the fairness review rule; "
            "AQ1, AQ2 = the descriptive and diagnostic questions.")
    kh = lh(k85, CWI, PT["small"])
    bottom = END - kh - 0.12
    items = [(T("Step 3: transfer to the university"),
              [T("Recount baseline completion under the add-drop rule: the denominator alone moves a rate by more "
                 "than ten points."),
               T("Check the early-sign rule on the university's task calendar."),
               T("Re-check the AQ1 and AQ2 results.")]),
             (T("Data needed"), [T("Two years of the university's enrolment, task and platform records, with access "
                                   "approved by the legal and data office.")]),
             (T("Not imputed or simulated"), [T("Contacts, attendance and year of study: invented values would turn "
                                                "assumptions into apparent evidence.")], MINUS)]
    stack(s, X0, y, lw, items, bottom, gap=0.18)
    vals = [T("Baseline completion rate"), T("Capacity figures"), T("One-week data delay"),
            T("List lengths: 3 or 5 per 20"), T("Ten-point fairness gap of FR1")]
    y2 = head_line(s, rx, y, rw, T("Five assumed values to replace"))
    acc = [[(T("Acceptance of activity-based contact "), AGENT_INK, True),
            (T("was voiced only by simulated students, so real students in Vietnam must be asked."), INK, False)]]
    ah = rich_h(acc, rw - 0.36, PT["body"]) + 0.3
    ay = bottom - ah
    rect(s, I(rx), I(ay), I(rw), I(ah), fill=ACC_FILL, line=WARM, radius=True, line_w=2.0)
    rich(s, rx + 0.18, ay + 0.15, rw - 0.36, acc, pt=PT["body"])
    cw_ = 3.2
    ch_ = 0.5
    gap = (ay - 0.3 - y2 - 5 * ch_) / 4
    kit.room("assumed values", 5 * ch_ + 4 * 0.12, ay - 0.3 - y2)
    cy = y2
    for v in vals:
        chip(s, rx, cy, cw_, ch_, v, fill=WHITE, line_color=GREY, size=BODY)
        cy += ch_ + gap
    mid = y2 + (ay - 0.3 - y2) / 2
    tx = rx + cw_ + 0.5
    nw = XR - tx
    for k in range(5):
        cyk = y2 + k * (ch_ + gap) + ch_ / 2
        arrow(s, rx + cw_ + 0.05, cyk, tx - 0.05, mid)
    nh = node_h(T("The university's records"), [T("its own counts replace each value")], nw)
    node(s, tx, mid - nh / 2 - 0.1, nw, nh + 0.2, T("The university's records"),
         [T("its own counts replace each value")], "ref")
    key(s, END - kh, k85)
    src(s, "Source: Milestone 5 report, Section 12.1 and Appendix XV, Table A.42 and the text after it.")


def s86(prs):
    s = kit.base(prs, kicker(86), T("Risk Classification and Human Control"), notes(86))
    y = lead(s, T("A contact list built from a model is likely a high-risk use of AI in education under Vietnamese "
                  "law, so it needs a risk classification first, and staff keep the final say."))
    xs, cw = cols(2, 0.3)
    laws = [(T("Law on Artificial Intelligence, No. 134/2025/QH15"),
             [T("Applies from 1 March 2026: human control and the ability to intervene over every decision of an AI "
                "system.")]),
            (T("Decision 33/2026/QĐ-TTg"),
             [T("Lists among high-risk uses in education AI systems that automatically assess or rank learners, and "
                "those that monitor or analyse learner behaviour.")])]
    lh_ = max(card_h(a, b, cw, PT["body"]) for a, b in laws)
    for x, (a, b) in zip(xs, laws):
        card(s, x, y, cw, a, b, h=lh_, pt=PT["body"])
    fy = y + lh_ + 0.45
    nodes = [(T("Step 3: transfer"), [T("records recounted")], "ref"),
             (T("Step 4: risk classification"), [T("legal review and consultation with students, before any "
                                                   "contact")], "agent"),
             (T("Step 5: pilot"), [T("staff keep the final say on every contact")], "out")]
    xn, nw = cols(3, 0.6)
    nh = max(node_h(a, b, nw, body_pt=BODY) for a, b, _ in nodes) + 0.15
    for k, (x, (a, b, st)) in enumerate(zip(xn, nodes)):
        node(s, x, fy, nw, nh, a, b, st, body_pt=BODY)
        if k < 2:
            arrow(s, x + nw + 0.05, fy + nh / 2, x + nw + 0.55, fy + nh / 2)
    arrow(s, xs[0] + cw / 2, y + lh_ + 0.05, xn[1] + nw * 0.3, fy - 0.05)
    arrow(s, xs[1] + cw / 2, y + lh_ + 0.05, xn[1] + nw * 0.7, fy - 0.05)
    k86 = T("Key: AI = artificial intelligence. Arrows from the two legal texts point to the step they require.")
    kh = lh(k86, CWI, PT["small"])
    by = fy + nh + 0.3
    bottom = END - kh - 0.1
    lower = [(T("Personal data"), [T("A declared disability is health information, so the pilot needs the student's "
                                     "consent to use it.")]),
             (T("Ethics"), [T("Predictive analysis carries a potential for bias and stereotyping, so a flag leads to "
                              "support, expires with the run and never becomes a label.")], MINUS)]
    pt = next((p for p in (PT["lead"], PT["body"], BODY) if max(card_h(a, b, cw, p, max(HEAD, p))
                                                                for a, b, *_ in lower) <= bottom - by), BODY)
    kit.room("law lower cards", max(card_h(a, b, cw, pt) for a, b, *_ in lower), bottom - by)
    for x, it in zip(xs, lower):
        card(s, x, by, cw, it[0], it[1], color=it[2] if len(it) > 2 else NAVY, h=bottom - by, pt=pt,
             hp=max(HEAD, pt))
    key(s, END - kh, k86)
    src(s, "Source: Milestone 5 report, Sections 12 and 12.1, Appendix VI and Appendix XV.")


def s87(prs):
    s = kit.base(prs, kicker(87), T("The Randomised Pilot"), notes(87))
    y = lead(s, T("Only a randomised pilot among flagged students can separate the effect of contact from the reasons "
                  "students are flagged, and its contacts are logged before any model is retrained."))
    # the randomisation diagram
    dh = 2.45
    x0, w0 = X0, 2.6
    node(s, x0, y + 0.5, w0, dh - 1.0, T("Flagged students"), [T("in the pilot courses; time zero at the eligibility "
                                                                  "cut-off")], "white", body_pt=BODY)
    x1, w1 = x0 + w0 + 0.5, 1.9
    node(s, x1, y + 0.75, w1, dh - 1.5, T("Random assignment"), None, "system")
    arrow(s, x0 + w0 + 0.05, y + dh / 2, x1 - 0.05, y + dh / 2)
    x2, w2 = x1 + w1 + 0.55, 2.3
    bh = (dh - 0.25) / 2
    node(s, x2, y, w2, bh, T("Contact"), [T("person and offer logged")], "agent", body_pt=BODY)
    node(s, x2, y + bh + 0.25, w2, bh, T("Usual support"), [T("no extra contact")], "white", body_pt=BODY)
    arrow(s, x1 + w1 + 0.05, y + dh / 2, x2 - 0.05, y + bh / 2)
    arrow(s, x1 + w1 + 0.05, y + dh / 2, x2 - 0.05, y + bh + 0.25 + bh / 2)
    x3, w3 = x2 + w2 + 0.55, 2.0
    node(s, x3, y + 0.5, w3, dh - 1.0, T("Outcome logged"), [T("time, person, offer, outcome")], "white",
         body_pt=BODY)
    arrow(s, x2 + w2 + 0.05, y + bh / 2, x3 - 0.05, y + dh / 2)
    arrow(s, x2 + w2 + 0.05, y + bh + 0.25 + bh / 2, x3 - 0.05, y + dh / 2)
    x4 = x3 + w3 + 0.5
    node(s, x4, y + 0.5, XR - x4, dh - 1.0, T("Completion compared"), [T("contact against usual support")], "out",
         body_pt=BODY)
    arrow(s, x3 + w3 + 0.05, y + dh / 2, x4 - 0.05, y + dh / 2)
    k87 = T("Key: KPI 1 = early-sign contact rate; KPI 2 = follow-up rate (the two secondary key performance "
            "indicators); steps 3 and 4 = the transfer to the university and the risk classification.")
    kh = lh(k87, CWI, PT["small"])
    cy = y + dh + 0.35
    bottom = END - kh - 0.1
    xs, cw = cols(4, 0.22)
    items = [(T("Why random"), [T("Only random assignment separates the effect of contact from the reasons a student "
                                  "was flagged.")]),
             (T("What it answers"), [T("Whether contact raises completion; which contact and offer work; the contact "
                                       "part of KPI 1 and KPI 2.")]),
             (T("One rule"), [T("Contacts logged with their outcomes before any model is retrained, or a model would "
                                "learn its own influence.")], AGENT_INK, ACC_FILL, WARM),
             (T("Timing"), [T("Steps 3 and 4 complete before contact begins in Semester 2 of 2026–2027.")])]
    pt = next((p for p in (PT["lead"], PT["body"], BODY) if max(card_h(a, b, cw, p, max(HEAD, p))
                                                                for a, b, *_ in items) <= bottom - cy), BODY)
    kit.room("pilot cards", max(card_h(a, b, cw, pt) for a, b, *_ in items), bottom - cy)
    for x, it in zip(xs, items):
        c, f, ln = (it[2], it[3], it[4]) if len(it) > 2 else (NAVY, SOFT, LINE)
        card(s, x, cy, cw, it[0], it[1], color=c, h=bottom - cy, fill=f, line=ln, pt=pt, hp=max(HEAD, pt),
             line_w=2.0 if ln != LINE else 1.0)
    key(s, END - kh, k87)
    src(s, "Source: Milestone 5 report, Section 12.1 and Appendix XV, Table A.42 and the text after it.")


# ----------------------------------------------------------------------------- 88–90 generative AI
def s88(prs):
    s = kit.base(prs, kicker(88), T("Generative AI: Roles and One Rule"), notes(88))
    y = lead(s, T("AI proposed and challenged, and we verified; it was never a source of data, statistics, licence "
                  "information or results."))
    guide = [[(T("Guidance followed: "), NAVY, True),
              (T("UNESCO (United Nations Educational, Scientific and Cultural Organization) holds that generative AI "
                 "cannot be trusted to be accurate and that its information should never be accepted at face value."),
               INK, False)]]
    gh = rich_h(guide, CWI - 0.36, PT["body"]) + 0.3
    gy = END - gh
    lw, gap = 3.6, 0.9
    roles = [T("Simulated stakeholder"), T("Research and code assistant"), T("Critic"), T("Writing partner")]
    checks = [T("Quotes against transcripts"), T("Literature against saved copies with verbatim quotations"),
              T("Code against fixtures (small inputs with known answers) and independent recounts"),
              T("Critics confined to the brief and the data")]
    top = y + 0.42
    avail = gy - 0.3 - top
    chip_h = min(0.95, (avail - 3 * 0.2) / 4)
    step = (avail - chip_h) / 3
    text(s, I(X0), I(y), I(lw), I(0.3), T("AI proposed"), size=HEAD, color=AGENT_INK, bold=True, spacing=1.0)
    for k, r in enumerate(roles):
        chip(s, X0, top + k * step, lw, chip_h, r, fill=ACC_FILL, line_color=WARM, color=AGENT_INK, size=PT["body"],
             bold=True)
    rx, rw = X0 + lw + gap, 5.0
    ay = top + 1.5 * step + chip_h / 2
    arrow(s, X0 + lw + 0.1, ay, rx - 0.1, ay)
    text(s, I(rx), I(y), I(rw), I(0.3), T("We verified with"), size=HEAD, color=NAVY, bold=True, spacing=1.0)
    for k, c in enumerate(checks):
        chip(s, rx, top + k * step, rw, chip_h, c, fill=WHITE, line_color=NAVY, size=BODY)
    fx = rx + rw + 0.3
    rule = [T("AI is never a source of data, statistics, licence information or results; every fact it offered was "
              "checked against a saved source, the data files or code we ran."),
            [(T("No AI produced a metric value, threshold or result."), AGENT_INK, True)]]
    rh = top + 3 * step + chip_h - y
    pt = next((p for p in (PT["lead"], PT["body"], BODY) if card_h(T("One rule"), rule, XR - fx, p, max(HEAD, p))
               <= rh), BODY)
    kit.room("one rule", card_h(T("One rule"), rule, XR - fx, pt), rh)
    card(s, fx, y, XR - fx, T("One rule"), rule, h=rh, pt=pt, hp=max(HEAD, pt), line=NAVY, line_w=2.0)
    rect(s, MX, I(gy), CW, I(gh), fill=SOFT, line=LINE, radius=True)
    rich(s, X0 + 0.18, gy + 0.15, CWI - 0.36, guide, pt=PT["body"])
    src(s, "Source: Milestone 5 report, Sections 13, 13.1 and 13.2, and Appendix XVI.")


def s89(prs):
    s = kit.base(prs, kicker(89), T("AI Decision Log"), notes(89))
    y = lead(s, T("Each milestone records what AI was used for, how we checked its output and what we decided."))
    rows = [[T("Milestone"), T("AI used for"), T("Our check"), T("Our decision")],
            [T("1 Problem"), T("Simulated stakeholders and a reviewer: 12 critiques"),
             T("Each quote checked against its transcript; 9 accepted, 2 in part, 1 rejected"),
             T("Cut-offs moved to the end of weeks 2 and 4; the interviews count as simulated")],
            [T("2 Data"), T("Requirement critic and selection reviewer: 22 critiques"),
             T("No dataset fact without the official source"),
             T("Gates require a dated withdrawal and dated tasks")],
            [T("3 Preparation"), T("Code assistant and a separate leakage auditor: 8 findings"),
             T("Fixture tests; 13 of 13 numbers equal to an independent recount"), T("All eight findings acted on")],
            [T("4 Method"), T("Three isolated reviewers: 24 critiques"),
             T("Each checked against design facts and arithmetic"),
             T("Switching rule with a margin fixed in advance; gate S1 fixed on all 13 test runs")],
            [T("5 Evidence"), T("Evidence extraction, AQ1 and AQ2 code, drafting and review"),
             T("369 statements checked against 32 sources, 0 errors; 2014 associations re-estimated by separate code, "
               "35 of 35 agree"),
             T("66 critiques: 42 accepted, 14 in part, none rejected, 10 handled in finishing")]]
    fr = (0.14, 0.27, 0.31)
    widths = [int(CW * f) for f in fr]
    widths.append(CW - sum(widths))
    k89 = T("Key: S1 = the gate a model must pass to replace the early-sign rule; AQ1, AQ2 = the descriptive and "
            "diagnostic questions; fixture = a small input with a known answer; no AI produced a metric value, "
            "threshold or result.")
    kh = lh(k89, CWI, PT["small"])
    room = END - kh - 0.1 - y
    size = PT["body"] if table_h(rows, widths, PT["body"]) <= room else BODY
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    th = stretch_table(shape, room)
    key(s, y + th + 0.1, k89)
    src(s, "Source: Milestone 5 report, Section 13.1 and Appendix XVI, Table A.43.")


def s90(prs):
    s = kit.base(prs, kicker(90), T("What AI Changed, and What We Rejected"), notes(90))
    y = lead(s, T("AI helped most when it had to argue from the data, and the decisions stayed ours."))
    k90 = T("Key: leakage check = a test that information from after the cut-off does not enter the predictors; "
            "AQ2 = the diagnostic question; AQ3, AQ4 = the predictive and ranking questions; OULAD = Open University "
            "Learning Analytics Dataset.")
    kh = lh(k90, CWI, PT["small"])
    bottom = END - kh - 0.12
    xs, cw = cols(3, 0.25)
    items = [(T("Where it helped"), [T("The Milestone 3 auditor found tasks due before registration counted as "
                                       "missed, and a leakage check that could not fail, that is, one that would pass "
                                       "even with leakage."),
                                     T("The Milestone 4 reviewer found that the 2013 runs hold 6 modules, not 7, "
                                       "which made the AQ2 criterion a share of modules.")], OUT_INK, OUT_FILL, PLUS),
             (T("What we rejected"), [T("Removing early identification from the Business Goal."),
                                      T("An imbalance argument for precision–recall curves: non-completion is "
                                        "44–46%."),
                                      T("Looking at the outcomes of repeat test students, which would break the "
                                        "independent test.")], MINUS, BAD_FILL, MINUS),
             (T("Decisions that stayed ours"), [T("Keep the 2014 runs out of every AQ3 choice."),
                                                T("One early-sign rule for OULAD and the pilot."),
                                                T("Run the AQ3 model once on 2014, as frozen on 2013."),
                                                T("State every association as an association."),
                                                T("Every result in the report comes from code we reran and "
                                                  "checked.")])]
    pt = next((p for p in (PT["lead"], PT["body"], BODY) if max(card_h(a, b, cw, p, max(HEAD, p))
                                                                for a, b, *_ in items) <= bottom - y), BODY)
    kit.room("ai columns", max(card_h(a, b, cw, pt) for a, b, *_ in items), bottom - y)
    for x, it in zip(xs, items):
        c, f, ln = (it[2], it[3], it[4]) if len(it) > 2 else (NAVY, SOFT, NAVY)
        card(s, x, y, cw, it[0], it[1], color=c, h=bottom - y, fill=f, line=ln, pt=pt, hp=max(HEAD, pt),
             line_w=2.0)
    key(s, END - kh, k90)
    src(s, "Source: Milestone 5 report, Section 13.2 and Appendix XVI.")


# ----------------------------------------------------------------------------- 91–94 conclusions and close
def s91(prs):
    s = kit.base(prs, kicker(91), T("Conclusions, Firmest First"), notes(91))
    y = lead(s, T("On OULAD, an early list cannot rest on missed tasks alone, and the early signs can serve as reasons "
                  "that staff check beside each name."))
    tiers = [(T("1. High confidence, OULAD 2013–2014"), PLUS, OUT_FILL,
              T("45.3% of the enrolments registered at day 14 did not complete; runs varied from 24.9% to 58.3%; the "
                "year comparison depends on the add-drop rule; most non-completers first missed a task after "
                "week 4.")),
             (T("2. Moderate confidence"), WARM, ACC_FILL,
              T("All five early signs go with later non-completion in both years, a missed task by 40.8 and 39.3 "
                "points, in the same direction across modules, with one wide exception. These are associations.")),
             (T("3. Moderate confidence, ranks only"), NAVY, SOFT,
              T("A penalised logistic model built on 2013 ranks the 2014 students slightly better than the rule and "
                "passes gate S1; lists of 5 per 20 hold 41.5% of later non-completers, no fairness group flagged."))]
    lab_w = 3.3
    key91 = T("Key: tiers run from the firmest finding at the top; the label of each tier is its confidence level. "
              "OULAD = Open University Learning Analytics Dataset; add-drop rule = only students still registered at "
              "day 14 count; S1 = the gate a model must pass to replace the early-sign rule.")
    kh = lh(key91, CWI, PT["small"])
    bottom = END - kh - 0.15

    def tier_h(pt):
        return [max(rich_h([b], CWI - 2 * k * 0.45 - lab_w - 0.5, pt), lh(h_, lab_w - 0.3, HEAD, True)) + 0.3
                for k, (h_, _, _, b) in enumerate(tiers)]
    pt = next((p for p in (PT["lead"], PT["body"], BODY) if sum(tier_h(p)) + 0.5 <= bottom - y), BODY)
    bhs = tier_h(pt)
    kit.room("conclusion tiers", sum(bhs) + 0.5, bottom - y)
    extra = (bottom - y - sum(bhs) - 0.5) / 3
    for k, ((head, c, fill, body), bh) in enumerate(zip(tiers, bhs)):
        inset = k * 0.45
        x, w = X0 + inset, CWI - 2 * inset
        bh += extra
        rect(s, I(x), I(y), I(w), I(bh), fill=fill, line=c, radius=True, line_w=2.0)
        text(s, I(x + 0.18), I(y), I(lab_w - 0.3), I(bh), head, size=HEAD, color=c if c != GREY else INK,
             bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        bt = rich_h([body], w - lab_w - 0.2, pt)
        rich(s, x + lab_w, y + (bh - bt) / 2 + 0.03, w - lab_w - 0.2, [body], pt=pt)
        y += bh + 0.25
    key(s, END - kh, key91)
    src(s, "Source: Milestone 5 report, Sections 11.2, 11.3, 11.4 and 14.")


def s92(prs):
    s = kit.base(prs, kicker(92), T("What We Cannot Conclude, and Open Problems"), notes(92))
    y = lead(s, T("Three claims stay out of reach of these data, and each maps to an open problem with a planned "
                  "answer."))
    rows = [[T("We cannot conclude that…"), T("Because"), T("Open problem and planned answer")],
            [T("the signs cause non-completion"), T("A regression capturing associations is descriptive, not causal."),
             T("Treat the signs as reasons to check, never as causes.")],
            [T("a model's risk is a reliable probability for each run"),
             T("Calibration fails in 8 of the 13 test runs, so the model holds as a rank, not a probability."),
             T("Show ranks and reasons; check calibration per course on the university's records.")],
            [T("contacting a listed student raises completion"),
             T("No data record contact, and questions of effectiveness need a randomised experiment."),
             T("A randomised pilot with contacts and outcomes logged.")]]
    widths = [int(CW * f) for f in (0.3, 0.36)]
    widths.append(CW - sum(widths))
    scope = [[(T("Over all three: "), WHITE, True),
              (T("every result describes UK distance-learning modules of 2013–2014 and is recounted on the "
                 "university's records, after a risk classification of the list."), WHITE, False)]]
    mh = rich_h(scope, CWI - 0.6, PT["lead"]) + 0.25
    k92 = T("Key: orange column = the planned answer; calibration = whether predicted risks match the observed "
            "rates.")
    kh = lh(k92, CWI, PT["small"])
    yb = END - mh
    room = yb - 0.2 - kh - 0.1 - y
    size = PT["lead"] if table_h(rows, widths, PT["lead"]) <= room else PT["body"]
    shape = table(s, MX, I(y), CW, rows, widths, size=size)
    for i in range(1, 4):
        c = shape.table.cell(i, 2)
        c.fill.solid()
        c.fill.fore_color.rgb = ACC_FILL
        for r in c.text_frame.paragraphs[0].runs:
            r.font.color.rgb, r.font.bold = AGENT_INK, True
    th = stretch_table(shape, room)
    key(s, y + th + 0.1, k92)
    rect(s, MX, I(yb), CW, I(mh), fill=NAVY, radius=True)
    rich(s, X0 + 0.3, yb + 0.12, CWI - 0.6, scope, pt=PT["lead"], color=WHITE)
    src(s, "Source: Milestone 5 report, Sections 12, 12.1 and 14.")


def s93(prs):
    s = kit.base(prs, kicker(93), T("Take-home"), notes(93))
    y = lead(s, T("Three things to take home: what to watch, how long a list should be, and what to prove first."))
    lines = [(T("Watch for inactivity, not only missed tasks."),
              T("Fewer than one in five future non-completers had missed a task by week 4; inactivity shows "
                "earlier."), WARM, ACC_FILL),
             (T("Size the list to the people who will call."),
              T("5 to 6 names per 20 students, each with the reason it is there."), NAVY, SOFT),
             (T("Read scores as ranks; pilot before scaling."),
              T("Risks are not reliable probabilities; only a randomised pilot shows whether contact helps."),
              NAVY, SOFT)]
    take = T("Take-home: watch for inactivity, size the list to capacity, and prove that contact works before scaling.")
    mh = lh(take, CWI - 0.6, PT["lead"], True) + 0.35
    yb = END - mh
    hp = 26
    num_w = 0.9
    hs = [max(lh(a, CWI - num_w - 0.5, hp, True) + 0.08 + lh(b, CWI - num_w - 0.5, PT["lead"]), 0.9) + 0.3
          for a, b, _, _ in lines]
    gap = 0.2
    extra = max(0.0, (yb - 0.25 - y - sum(hs) - 2 * gap) / 3)
    kit.room("take-home lines", sum(hs) + 2 * gap, yb - 0.25 - y)
    for k, ((a, b, c, f), h) in enumerate(zip(lines, hs)):
        h += extra
        rect(s, I(X0), I(y), I(CWI), I(h), fill=f, line=c if k == 0 else LINE, radius=True,
             line_w=2.0 if k == 0 else 1.0)
        text(s, I(X0 + 0.15), I(y), I(num_w), I(h), str(k + 1), size=PT["number"], color=c, bold=True,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        inner = lh(a, CWI - num_w - 0.5, hp, True) + 0.08 + lh(b, CWI - num_w - 0.5, PT["lead"])
        ty = y + (h - inner) / 2
        text(s, I(X0 + num_w + 0.3), I(ty), I(CWI - num_w - 0.5), I(lh(a, CWI - num_w - 0.5, hp, True)), a,
             size=hp, color=AGENT_INK if k == 0 else NAVY, bold=True, spacing=1.0)
        text(s, I(X0 + num_w + 0.3), I(ty + lh(a, CWI - num_w - 0.5, hp, True) + 0.08), I(CWI - num_w - 0.5),
             I(lh(b, CWI - num_w - 0.5, PT["lead"])), b, size=PT["lead"], color=INK, spacing=1.0)
        y += h + gap
    closing_box(s, yb, take, h=mh)
    src(s, "Source: Milestone 5 report, Sections 11.2, 11.4, 11.5 and 14, and Appendix XII, Table A.31.")


def s94(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, fill=NAVY)
    text(s, 0, I(1.7), W, I(0.9), T("Thank you. Questions?"), size=PT["cover"], color=WHITE, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    text(s, I(1.0), I(2.75), W - I(2.0), I(0.45), T("Early Identification of Disengaging Students in Online Courses – "
                                                    "team N04"), size=PT["lead"], color=WHITE,
         align=PP_ALIGN.CENTER, spacing=1.0)
    msg = T("Take-home: watch for inactivity, size the list to capacity, and prove that contact works before scaling.")
    mh = lh(msg, 10.5, PT["lead"] + 4, True) + 0.4
    rect(s, I(1.3), I(3.65), W - I(2.6), I(mh), fill=pal_rgb(pal.shade(pal.NAVY, 0.25)), radius=True)
    text(s, I(1.6), I(3.65), W - I(3.2), I(mh), msg, size=PT["lead"] + 4, color=WHITE, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    text(s, I(1.0), I(6.3), W - I(2.0), I(0.35), T("Data: Open University Learning Analytics Dataset (Kuzilek, Hlosta "
                                                   "and Zdrahal), CC BY 4.0."), size=PT["small"],
         color=pal_rgb("#C9D3E3"), align=PP_ALIGN.CENTER, spacing=1.0)
    s.notes_slide.notes_text_frame.text = notes(94)
    src(s, "Source: Milestone 5 report, Sections 5 and 7.2, and Appendix XVI.")


SLIDES = {70: s70, 71: s71, 72: s72, 73: s73, 74: s74, 75: s75, 76: s76, 77: s77, 78: s78, 79: s79, 80: s80,
          81: s81, 82: s82, 83: s83, 84: s84, 85: s85, 86: s86, 87: s87, 88: s88, 89: s89, 90: s90, 91: s91,
          92: s92, 93: s93, 94: s94}
