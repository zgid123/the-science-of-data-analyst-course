"""Full Milestone 5 deck, plan slides 47–69: modeling strategy, evaluation design, experimental status, how the
findings are read, the Final Project Traceability Matrix and the AQ1 findings.

Numbers come from the Milestone 5 report (Sections 8–11.2 and Appendices VIII–XII); charts reuse the data of the
built deck (build_slides_milestone5_30.py) where it already holds them.
"""

from slides_milestone5_full.common import *   # noqa: F401,F403

DESIGNED = pal_rgb(pal.tint(pal.BLUE))            # light blue: a design element (method slides)
LINKED = pal_rgb("#E6E8EC")                       # light grey: a link that holds evidence


def head(s, x, y, w, line, color=NAVY, pt=HEAD):
    """A bold heading line at (x, y); returns the y below it."""
    h = lh(line, w, pt, True)
    text(s, I(x), I(y), I(w), I(h), line, size=pt, color=color, bold=True, spacing=1.0)
    return y + h


def fill_cell(cell, rgb, color=None, bold=None):
    cell.fill.solid()
    cell.fill.fore_color.rgb = rgb
    for p in cell.text_frame.paragraphs:
        for r in p.runs:
            if color is not None:
                r.font.color.rgb = color
            if bold is not None:
                r.font.bold = bold


def fitted_table(s, y, rows, fracs, bottom, x=None, w=None, sizes=(PT["body"], BODY)):
    """A kit table at the largest size that fits above `bottom`, stretched to it; returns the shape."""
    x = X0 if x is None else x
    w = CWI if w is None else w
    widths = [int(I(w) * f) for f in fracs[:-1]]
    widths.append(I(w) - sum(widths))
    size = next((pt for pt in sizes if table_h(rows, widths, pt) <= bottom - y), sizes[-1])
    kit.room("table", y + table_h(rows, widths, size), bottom)
    shape = table(s, I(x), I(y), I(w), rows, widths, size=size)
    stretch_table(shape, bottom - y)
    return shape


def spread(s, x, y, w, paras, pt, bottom):
    """Paragraphs spread evenly from y down to bottom (the free height goes into the gaps between them)."""
    hs = [rich_h([p], w, pt) for p in paras]
    gap = max(0.0, (bottom - y - sum(hs)) / (len(paras) - 1)) if len(paras) > 1 else 0
    for p, h in zip(paras, hs):
        rich(s, x, y, w, [p], pt=pt)
        y += h + gap


def spread_card(s, x, y, w, h, head_line, paras, color=NAVY, fill=SOFT, line=LINE, sizes=(PT["lead"], PT["body"], BODY)):
    """A card whose paragraphs take the largest kit size that fits and spread evenly to its bottom edge."""
    rect(s, I(x), I(y), I(w), I(h), fill=fill, line=line, radius=True)
    ty = y + 0.18
    if head_line:
        ty = head(s, x + 0.2, ty, w - 0.4, head_line, color=color) + 0.12
    room = y + h - 0.2 - ty
    pt = next((p for p in sizes if rich_h(paras, w - 0.4, p) + 0.08 * (len(paras) - 1) <= room), sizes[-1])
    kit.room("card text", rich_h(paras, w - 0.4, pt), room)
    gap_room = y + h - 0.2
    spread(s, x + 0.2, ty, w - 0.4, paras, pt, min(gap_room, ty + rich_h(paras, w - 0.4, pt) + 0.35 * (len(paras) - 1)))


def red_from(cell, word):
    """Set the cell's text from `word` onwards in bold red (a GAP or N.A. mark), the part before it unchanged."""
    p = cell.text_frame.paragraphs[0]
    r = p.runs[0]
    full = r.text
    k = full.index(word)
    if k == 0:
        r.font.bold, r.font.color.rgb = True, MINUS
        return
    r.text = full[:k]
    r2 = p.add_run()
    r2.text = full[k:]
    r2.font.name, r2.font.size = r.font.name, r.font.size
    r2.font.bold, r2.font.color.rgb = True, MINUS


def stack_cards(s, x, y, w, items, bottom=END, gap=0.2):
    """Cards (head, body, colour) stacked from y to bottom at the largest kit size that fits; the free height is
    shared by the cards."""
    def hs(pt):
        return [card_h(a, [b], w, pt=pt, hp=HEAD) for a, b, _ in items]
    # card_h measures generously (about one spare line per card), so a size is taken when it fits within 10%;
    # check_slides then measures every box with the font's metrics.
    pt = next((p for p in (PT["body"], BODY) if sum(hs(p)) + gap * (len(items) - 1) <= (bottom - y) * 1.1), BODY)
    h = hs(pt)
    room = bottom - y - gap * (len(items) - 1)
    kit.room("side cards", sum(h), room * 1.1)
    if sum(h) > room:                               # share the cards' measured slack out evenly
        h = [x * room / sum(h) for x in h]
    extra = max(0.0, (room - sum(h)) / len(items))
    for (a, b, c), hh in zip(items, h):
        card(s, x, y, w, a, [b], color=c, h=hh + extra, pt=pt, hp=HEAD)
        y += hh + extra + gap


# ----------------------------------------------------------------------------- 8 Modeling
def s47(prs):
    s = kit.base(prs, kicker(47), T("From Questions to Technical Tasks"), notes(47))
    y = lead(s, T("Each question's purpose fixes its technical task and how its result may be read."))
    rows = [("AQ1", T("Descriptive"), T("Aggregation and rate comparison"),
             T("States what happened, with its denominator and 95% interval.")),
            ("AQ2", T("Diagnostic"), T("Association within module run"),
             T("An association, never a cause: a regression that captures associations describes.")),
            ("AQ3", T("Predictive"), T("Binary classification at day 13 and day 27"),
             T("Judged on runs the model has not seen: explaining data well does not mean predicting well.")),
            ("AQ4", T("Prescriptive"), T("Ranking under a fixed capacity"),
             T("A decision option for staff, untested until a pilot."))]
    key47 = T("Key: AQ1–AQ4 = the four analytical questions; the level under each names its analytics type. "
              "Capacity = 3 or 5 contacts per 20 students. Reading rules after Shmueli (2010): explanatory power "
              "does not imply predictive power.")
    msg = T("Designed at Level 1 (the compulsory level: method and evaluation design) in Milestone 4; AQ1 and AQ2 "
            "then ran on 2013 and 2014, and AQ3 and AQ4 ran once as the Level 2 prototype.")
    mh = lh(msg, CWI - 0.6, PT["lead"], True) + 0.3
    ky = END - mh - 0.2 - lh(key47, CWI, PT["small"])
    closing_box(s, END - mh, msg, h=mh)
    key(s, ky, key47)
    wq, wt = 2.2, 4.0
    gap = 0.45
    xt = X0 + wq + gap
    xr = xt + wt + gap
    wr = XR - xr
    for x, w, lab in [(X0, wq, T("Question")), (xt, wt, T("Technical task")), (xr, wr, T("How its result may be read"))]:
        head(s, x, y, w, lab)
    y += 0.4
    rg = 0.18
    rh = (ky - 0.2 - y - 3 * rg) / 4
    kit.room("task rows", 4 * 0.65 + 3 * rg, ky - 0.2 - y)
    for i, (q, lvl, task, read) in enumerate(rows):
        yy = y + i * (rh + rg)
        node(s, X0, yy, wq, rh, q, lvl, style="system")
        arrow(s, X0 + wq + 0.05, yy + rh / 2, xt - 0.05, yy + rh / 2)
        node(s, xt, yy, wt, rh, task, None, style="soft", head_pt=PT["body"])
        arrow(s, xt + wt + 0.05, yy + rh / 2, xr - 0.05, yy + rh / 2)
        node(s, xr, yy, wr, rh, None, read, style="agent", body_pt=PT["body"])
    src(s, "Source: Milestone 5 report, Section 8 and Appendix VIII, Table A.22.")


def selection_slide(s, n, cols_, key_line, note_line=None):
    """The Method Selection Matrix transposed: one column per question, one row per attribute."""
    y = lead(s, T(PLAN_LEADS[n]))
    labels = [T("Analytics type and task"), T("Baseline"), T("Candidate methods"), T("Primary proposal"),
              T("Rationale")]
    rows = [[""] + [c[0] for c in cols_]] + [[lab] + [c[1][i] for c in cols_] for i, lab in enumerate(labels)]
    ky = bottom_key(s, key_line)
    bottom = ky - 0.15
    if note_line:
        nh = lh(note_line, CWI, PT["body"], True)
        ny = ky - 0.12 - nh
        text(s, I(X0), I(ny), I(CWI), I(nh), note_line, size=PT["body"], color=AGENT_INK, bold=True, spacing=1.0)
        bottom = ny - 0.15
    shape = fitted_table(s, y, rows, [0.2, 0.4, 0.4], bottom)
    for j in (1, 2):
        fill_cell(shape.table.cell(4, j), ACC_FILL)
    fill_cell(shape.table.cell(4, 0), WARM, color=WHITE)


PLAN_LEADS = {
    48: "AQ1 needs no model, only grouped rates with intervals, and AQ2 needs a within-run association model that "
        "makes no causal claim.",
    49: "AQ3 proposes an interpretable penalised logistic model that must beat the early-sign rule, and AQ4 a top-k "
        "list per run with the signs behind each name.",
}


def s48(prs):
    s = kit.base(prs, kicker(48), T("Method Selection: AQ1 and AQ2"), notes(48))
    cols_ = [(T("AQ1 – Descriptive"),
              [T("Descriptive: aggregation and rate comparison."),
               T("Pooled rate; rate over all enrolments; rate without enrolments flagged for an unknown withdrawal or "
                 "registration day."),
               T("Grouped rates with 95% intervals."),
               T("Grouped rates with Wilson intervals; cumulative first missed week by outcome; year difference with "
                 "a Newcombe interval."),
               T("A descriptive question needs no model; the denominator decides the rate.")]),
             (T("AQ2 – Diagnostic"),
              [T("Diagnostic: association within module run."),
               T("Unadjusted rate difference per sign."),
               T("Logistic regression with run fixed effects and sign × module terms; mixed-effects logistic "
                 "regression."),
               T("The fixed-effects logistic regression, robust standard errors; effects as average risk differences, "
                 "odds ratios beside them."),
               T("Every run is observed, so fixed effects suit; 6 modules are too few for a random effect; no causal "
                 "claim.")])]
    key48 = T("Key: AQ1 = descriptive question (outcome shares and timing); AQ2 = diagnostic question (early signs, "
              "association only). Wilson / Newcombe interval = 95% interval of a rate / of a difference of two rates. "
              "Run fixed effects = a term per module run, so students are compared only within their run. Risk "
              "difference = extra percentage points of later non-completion with a sign. Orange row = primary "
              "proposal.")
    selection_slide(s, 48, cols_, key48)
    src(s, "Source: Milestone 5 report, Section 8.1, Table 8.1, and Appendix VIII.")


def s49(prs):
    s = kit.base(prs, kicker(49), T("Method Selection: AQ3 and AQ4"), notes(49))
    cols_ = [(T("AQ3 – Predictive (proposal, run in Level 2)"),
              [T("Predictive: binary classification at day 13 and day 27."),
               T("Early-sign rule ranked by its number of signs; background-only logistic model; random list."),
               T("Penalised logistic regression; gradient-boosted trees; discrete-time survival as an extension."),
               T("Penalised logistic regression on the 19 primary predictors (23 parameters), unless a challenger wins "
                 "by a margin fixed in advance."),
               T("Interpretable reasons for staff; about 230 non-completers per parameter; classes close in size; "
                 "transfer to a later run.")]),
             (T("AQ4 – Prescriptive (proposal, run in Level 2)"),
              [T("Prescriptive: ranking under a fixed capacity."),
               T("Random list; rule-ranked list of the same length."),
               T("Top-k per run from the AQ3 scores; risk tiers from capacity."),
               T("Top-k per run, with the signs behind each name."),
               T("Capacity is fixed; no contact data, so no ranking by expected benefit; a member of staff "
                 "decides.")])]
    key49 = T("Key: AQ3 = predictive question (model against the early-sign rule); AQ4 = prescriptive question "
              "(ranking under capacity). Early-sign rule = flags a task due and not submitted, a tutor-marked "
              "assignment submitted late, or no click in the 7 days before the cut-off. Penalised = coefficients "
              "shrunk to avoid overfitting. Top-k = the k highest-ranked students of a run; capacity = 3 or 5 "
              "contacts per 20 students. Orange row = primary proposal.")
    selection_slide(s, 49, cols_, key49)
    src(s, "Source: Milestone 5 report, Section 8.1, Table 8.1, and Appendix VIII.")


def s50(prs):
    s = kit.base(prs, kicker(50), T("Eight Criteria and the Tie-break"), notes(50))
    y = lead(s, T("Every candidate is judged on the course's eight criteria, and ties go to the simpler, more "
                  "interpretable method, because decisions about people call for it."))
    crit = [(T("Fit to the question"), T("Does it directly give the output the question needs?")),
            (T("Fit to the data"), T("Do size, feature types and time structure suit it?")),
            (T("Assumptions"), T("What does it require, and do the data roughly meet it?")),
            (T("Interpretability"), T("How much of its logic must the users understand?")),
            (T("Complexity against the baseline"), T("What does a more complex method add?")),
            (T("Robustness and reproducibility"), T("Can it be rerun stably and kept free of leakage?")),
            (T("Ethics and fairness"), T("Could its errors harm a group; does it use a sensitive attribute?")),
            (T("Actionability"), T("Does its output support the decision it serves?"))]
    lw = 7.6
    y0 = head(s, X0, y, lw, T("The eight course criteria")) + 0.12
    xs, cw = cols(2, 0.2, X0, lw)
    rg = 0.12
    rh = (END - y0 - 3 * rg) / 4
    tw = cw - 0.7
    need = max(lh(a, tw, PT["body"], True) + 0.04 + lh(b, tw, BODY) for a, b in crit) + 0.06
    kit.room("criteria tiles", need, rh)
    for k, (a, b) in enumerate(crit):
        r, c = divmod(k, 2)
        x, yy = xs[c], y0 + r * (rh + rg)
        rect(s, I(x), I(yy), I(cw), I(rh), fill=SOFT, line=LINE, radius=True)
        th = lh(a, tw, PT["body"], True) + 0.04 + lh(b, tw, BODY)
        ty = yy + (rh - th) / 2
        text(s, I(x + 0.12), I(ty - 0.06), I(0.45), I(0.45), str(k + 1), size=PT["head"] + 4, color=WARM, bold=True,
             spacing=1.0)
        ty = head(s, x + 0.58, ty, tw, a, pt=PT["body"])
        rich(s, x + 0.58, ty + 0.04, tw, [b], pt=BODY)
    rx = X0 + lw + 0.5
    rw = XR - rx
    arrow(s, X0 + lw + 0.08, y0 + 2 * rh, rx - 0.08, y0 + 2 * rh)
    ties = [tb("Start from a rule: ", "a simple heuristic often delivers much of the gain."),
            tb("Prefer the simpler: ", "when many models reach about the same error, choose the simpler one."),
            tb("Count the upkeep: ", "complexity is costly to maintain."),
            tb("Interpretable by design: ", "for high-stakes decisions about people, prefer a model interpretable "
                                            "by design to a black box explained afterwards.")]
    msg = T("For AQ3, the predictive question: penalised logistic regression first; boosted trees only as "
            "challenger.")
    mh = rich_h([msg], rw - 0.4, PT["body"]) + 0.3
    yb = END - mh
    rect(s, I(rx), I(yb), I(rw), I(mh), fill=NAVY, radius=True)
    text(s, I(rx + 0.2), I(yb), I(rw - 0.4), I(mh), msg, size=PT["body"], color=WHITE, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    spread_card(s, rx, y, rw, yb - 0.2 - y, T("When candidates tie"), ties,
                sizes=(PT["body"], BODY))
    src(s, "Source: Milestone 5 report, Section 8.1 and Appendix VIII.")


def ranking_chart(fig):
    ax = charts.axes(fig)
    cats = [T("Day 13 (end of week 2)"), T("Day 27 (end of week 4)")]
    vals = [20.2, 28.8]
    ax.set_xlim(0, 36)
    ax.set_ylim(1.6, -0.75)
    for i, v in enumerate(vals):
        ax.barh(i, v, height=0.5, color=C_ACC if i == 1 else C_GREY, zorder=3)
        ax.annotate(f"{charts.num(v, 1)}%", (v, i), xytext=(5, 0), textcoords="offset points", ha="left",
                    va="center", fontsize=charts.size("value"), color=C_INK, fontweight="bold")
    for x, lab, ha, dx in [(15, T("List of 3 per 20: 15%"), "right", -5), (25, T("List of 5 per 20: 25%"), "left", 5)]:
        ax.axvline(x, color=C_INK, lw=1.3, ls=(0, (4, 3)), zorder=4)
        ax.annotate(lab, (x, -0.5), xytext=(dx, 0), textcoords="offset points", ha=ha, va="center",
                    fontsize=charts.size("small"), color=C_INK)
    ax.set_yticks(range(2), cats)
    ax.set_xticks([0, 10, 20, 30])
    charts.ticks(ax.xaxis, pct=True)
    ax.set_xlabel(T("Share of enrolments flagged by the early-sign rule, 22 runs"), fontsize=charts.size("small"),
                  color=C_MUTED)


def s51(prs):
    s = kit.base(prs, kicker(51), T("Why a Ranking, Not a Threshold"), notes(51))
    y = lead(s, T("The early-sign rule flags more students than staff can contact, so the list must be ranked to fit "
                  "capacity."))
    lw, rw, rx = kit.split(0.55)
    y1 = head(s, X0, y, lw, T("The rule flags more students than a list can hold"))
    ky = bottom_key(s, T("Key: bar = share of the enrolments registered at the cut-off that the early-sign rule flags "
                         "(a task due and not submitted, a tutor-marked assignment submitted late, or no click in the 7 "
                         "days before the cut-off). Dashed lines = list lengths at 3 or 5 contacts per 20 students, "
                         "scenario values."), X0, lw)
    chart(s, "m5-full-p3-ranking", X0, y1 + 0.1, lw, ky - y1 - 0.2, ranking_chart)
    side = [(T("Staff need an order"), T("The rule names more students than a list of 15% or 25% of a run can hold, "
                                         "so someone must decide who comes first."), NAVY),
            (T("Risk, not benefit"), T("No data record a contact or its outcome, so the list cannot rank by the expected "
                                       "benefit of a contact."), WARM),
            (T("A person decides"), T("The list orders by risk and shows its reasons; a member of staff decides. Risk "
                                      "as need stays untested until a randomised pilot."), NAVY)]
    stack_cards(s, rx, y, rw, side)
    src(s, "Source: Milestone 5 report, Section 8 and Appendices VIII and IX.")


# ----------------------------------------------------------------------------- 9 Evaluation
def s52(prs):
    s = kit.base(prs, kicker(52), T("Judging a List by Capacity"), notes(52))
    y = lead(s, T("A list is judged by how many later non-completers it reaches against the most a list of its length "
                  "could reach."))
    lw = 5.6
    nc = {0, 1, 2, 4, 6, 9, 12, 15, 18}             # 9 later non-completers, 4 of them in the list (the first row)
    sz, gx, gy = 0.5, 0.95, 0.6
    lines = [tb("Recall ", "= 4 of 9 non-completers."),
             tb("Normalised recall ", "= 4 of 5, the most a list of 5 can reach."),
             [(T("Key: orange figure = later non-completer; navy box = on the list. Illustration, not data."), KEY,
               False)]]
    gy0 = y + 0.58
    gy = max(gy, (END - y - 0.06 - rich_h(lines, lw - 0.4) - 0.02 - 0.58 - 0.12) / 4)
    yk = gy0 + 4 * gy + 0.02 - (gy - sz) + 0.12
    ph = yk - y + rich_h(lines, lw - 0.4) + 0.06
    rect(s, I(X0), I(y), I(lw), I(max(ph, END - y)), fill=SOFT, line=LINE, radius=True)
    text(s, I(X0 + 0.2), I(y + 0.12), I(lw - 0.4), I(0.3), T("Worked example: 20 students, a list of 5"), size=HEAD,
         color=NAVY, bold=True, spacing=1.0)
    x0 = X0 + (lw - 4 * gx - sz) / 2
    for k in range(20):
        r, c = divmod(k, 5)
        icon(s, "user", x0 + c * gx, gy0 + r * gy, sz, color=WARM if k in nc else GREY, bg=SOFT)
    box = rect(s, I(x0 - 0.12), I(gy0 - 0.06), I(4 * gx + sz + 0.24), I(sz + 0.12), line=NAVY, line_w=2.25)
    box.fill.background()
    rich(s, X0 + 0.2, yk, lw - 0.4, lines)
    kit.room("worked example", y + ph, END)
    rx, rw = X0 + lw + 0.35, CWI - lw - 0.35
    defs = [
        tb("Capacity k: ", "3 or 5 contacts per 20 students, that is 15% or 25% of a run; the main operating point is "
                           "5 per 20 at day 27."),
        tb("Recall at capacity: ", "the share of a run's non-completers who are on its list."),
        tb("Normalised recall: ", "recall divided by the most a list of length k can reach, k non-completers "
                                  "(5 in the example, hence 4 of 5); across the training runs this ceiling is 46% "
                                  "to 100% of a run's non-completers."),
        tb("Why not \"precision of at least 50%\" (Milestone 1): ", "precision is the share of the list who do not "
                                                                     "complete; with non-completion near 45%, a random "
                                                                     "list already reaches about 45%."),
        tb("What else is judged: ", "whether later non-completers are ranked first, whether predicted risks match "
                                    "the observed rates (calibration), and whether the list helps the decision.")]
    pt15 = fit_pt(defs, rw, END - y)
    kit.room("list metrics", y + rich_h(defs, rw, pt15), END)
    spread(s, rx, y, rw, defs, pt15, END)
    src(s, "Source: Milestone 5 report, Section 9 and Appendices III (Table A.8) and IX.")


def s53(prs):
    s = kit.base(prs, kicker(53), T("Evaluation Plan"), notes(53))
    y = lead(s, T("Each question has a primary metric, a baseline, a validation and a success criterion fixed before "
                  "any code ran."))
    rows = [[T("Question"), T("Primary metric"), T("Baseline"), T("Validation"), T("Success criterion")],
            [T("AQ1 – Descriptive"), T("Non-completion rates and outcome shares with 95% intervals"),
             T("Pooled rate; rate over all enrolments; rate without flagged enrolments"),
             T("Two independent aggregation paths: prepared views and raw tables"),
             T("Both paths agree to the enrolment; every rate carries its denominator and interval")],
            [T("AQ2 – Diagnostic"), T("Average risk difference of each sign within module run, 95% interval"),
             T("Unadjusted rate difference"),
             T("9 runs of 2013; sensitivity runs; replication on the 13 runs of 2014"),
             T("At least 5 points, interval excluding 0, same direction in at least two-thirds of modules")],
            [T("AQ3 – Predictive"), T("Pooled normalised recall at capacity (day 27, 5 per 20)"),
             T("Rule-ranked list; background-only model; random list"),
             T("Leave-one-run-out folds in 2013; one logged test on all 13 runs of 2014"),
             T("Gate S1: the model's list must beat the rule's list")],
            [T("AQ4 – Prescriptive"), T("Normalised recall at capacity"), T("Random list; rule-ranked list"),
             T("As AQ3, a list per test run"),
             T("Gate S1 met by the list, and fairness rule FR1 passed or its flags reviewed")]]
    ky = bottom_key(s, T("Key: AQ1–AQ4 = the four analytical questions. Normalised recall = recall divided by the most a "
                         "list of its length can reach. Rule-ranked list = the early-sign rule's flags ordered by their "
                         "number of signs. S1 = the single gate of the predictive model; FR1 = the fairness review rule. "
                         "Orange column = the success criterion, fixed in Milestone 4."))
    shape = fitted_table(s, y, rows, [0.14, 0.22, 0.2, 0.22, 0.22], ky - 0.15)
    fill_cell(shape.table.cell(0, 4), WARM)
    for i in range(1, 5):
        fill_cell(shape.table.cell(i, 4), ACC_FILL)
    src(s, "Source: Milestone 5 report, Section 9, Table 9.1, and Section 9.1.")


def aq2_rule(fig):
    ax = charts.axes(fig)
    items = [("A", 12, 8, 16, True, T("Consistent")), ("B", 3, 1, 5, False, T("Below 5 points")),
             ("C", 7, -2, 16, False, T("Interval includes 0"))]
    ax.set_xlim(-5, 26)
    ax.set_ylim(2.6, -0.7)
    ax.axvspan(-5, 5, color="#EEF0F3", zorder=0)
    ax.axvline(0, color=C_MUTED, lw=1.2, zorder=1)
    ax.axvline(5, color=C_INK, lw=1.3, ls=(0, (4, 3)), zorder=1)
    ax.annotate(T("5-point criterion"), (5, -0.5), xytext=(4, 0), textcoords="offset points", ha="left",
                va="center", fontsize=charts.size("small"), color=C_INK)
    for i, (lab, v, lo, hi, ok, verdict) in enumerate(items):
        col = C_ACC if ok else C_GREY
        ax.plot([lo, hi], [i, i], color=col, lw=2.6, zorder=2)
        for e in (lo, hi):
            ax.plot([e, e], [i - 0.1, i + 0.1], color=col, lw=2.2, zorder=2)
        ax.plot(v, i, "o", ms=12, color=col, mec="white", mew=1.4, zorder=3)
        ax.annotate(verdict, (hi, i), xytext=(8, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=charts.size("value"), color=C_ACC if ok else C_INK,
                    fontweight="bold" if ok else "normal")
    ax.set_yticks(range(3), [T("Sign A"), T("Sign B"), T("Sign C")])
    ax.set_xticks([-5, 0, 5, 10, 15, 20, 25])
    ax.set_xlabel(T("Adjusted risk difference, percentage points"), fontsize=charts.size("small"), color=C_MUTED)


def s54(prs):
    s = kit.base(prs, kicker(54), T("The AQ2 Success Criterion"), notes(54))
    y = lead(s, T("A sign counts as a consistent association only when its adjusted difference is at least 5 points, "
                  "its interval excludes 0 and its direction holds in two-thirds of modules."))
    lw, rw, rx = kit.split(0.48)
    conds = [T("Risk difference, adjusted for the other signs, of at least 5 percentage points."),
             T("95% interval of the risk difference excluding 0."),
             T("Same direction in at least two-thirds of the modules where the sign is defined.")]
    whys = [tb("Why 5 points: ", "the smallest gap worth staff attention, a convention fixed in Milestone 4. It is "
                                 "lenient at a base rate near 44%, so the size of each estimate distinguishes the "
                                 "signs."),
            tb("Why no p-values: ", "a p-value does not measure the size of an effect; p-values are reported but take "
                                    "no part in the verdict.")]
    y1 = head(s, X0, y, lw, T("All three conditions must hold")) + 0.1
    pt_w = fit_pt(whys, lw, 2.3)
    wh = rich_h(whys, lw, pt_w)
    yw = END - wh
    rich(s, X0, yw, lw, whys, pt=pt_w)
    gap = 0.15
    ch = (yw - 0.25 - y1 - 2 * gap) / 3
    kit.room("conditions", max(lh(c, lw - 0.85, PT["body"]) for c in conds) + 0.1, ch)
    for k, c in enumerate(conds):
        yy = y1 + k * (ch + gap)
        rect(s, I(X0), I(yy), I(lw), I(ch), fill=SOFT, line=LINE, radius=True)
        text(s, I(X0 + 0.15), I(yy), I(0.5), I(ch), str(k + 1), size=PT["head"] + 6, color=WARM, bold=True,
             anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        text(s, I(X0 + 0.7), I(yy), I(lw - 0.85), I(ch), c, size=PT["body"], color=INK, anchor=MSO_ANCHOR.MIDDLE,
             spacing=1.0)
    y2 = head(s, rx, y, rw, T("How the criterion sorts three signs (illustration, not data)"))
    ky = bottom_key(s, T("Key: dot = adjusted risk difference of an invented sign; whisker = its 95% interval; dashed "
                         "line = the 5-point criterion; grey band = below 5 points. Risk difference = extra percentage "
                         "points of later non-completion with the sign, within module run. AQ2 = the diagnostic "
                         "question on early signs."), rx, rw)
    chart(s, "m5-full-p3-aq2-rule", rx, y2 + 0.1, rw, ky - y2 - 0.2, aq2_rule)
    src(s, "Source: Milestone 5 report, Sections 9 and 9.1, Table 9.1, and Appendix IX.")


def s55(prs):
    s = kit.base(prs, kicker(55), T("Validation Design"), notes(55))
    y = lead(s, T("Development and model choice stay inside 2013, and the 13 runs of 2014 are scored once by a model "
                  "frozen in advance."))
    steps = [(T("2013: 9 runs"), T("leave-one-run-out folds"), "soft", "calendar"),
             (T("Freeze 1"), T("question, splits, metrics, baselines"), "ref", "lock"),
             (T("Model choice"), T("challenger rule on the folds"), "soft", "filter"),
             (T("Freeze 2"), T("final model; test access recorded"), "ref", "lock"),
             (T("2014: 13 runs"), T("scored once: 15,724 enrolments at day 27"), "agent", "check")]
    key55 = T("Key: AQ3 = the predictive question. Fold = one 2013 run held out while the model learns from the other "
              "8. Paired run = a 2014 run whose module and start month also ran in 2013. Normalised recall = recall "
              "divided by the most a list of its length can reach.")
    ky = bottom_key(s, key55)
    items = [(T("Inside each fold"), [T("Every learned step (filling, scaling, tuning) is refitted; students who also "
                                        "appear in the held-out run are removed from its training data."),
                                      T("Fold results only choose between candidates; they are never reported as "
                                        "performance.")]),
             (T("Challenger rule"), [T("Trees or the extended set replace the primary model only with a gain of at least "
                                       "0.03 in pooled normalised recall (about 89 more non-completers listed) and a gain "
                                       "in 7 of 9 folds, fixed before any fold result.")]),
             (T("Test populations"), [T("9 paired runs (10,801 enrolments) test a later run of a known module; 4 "
                                        "unpaired runs (4,923) test transfer; both also reported apart. The 1,586 test "
                                        "enrolments of students seen in 2013 stay in, and are removed in a sensitivity "
                                        "analysis.")])]
    xs, cw = cols(3, 0.25)
    ch_need = max(card_h(a, b, cw, pt=BODY) for a, b in items)
    fh = 1.7
    free = ky - 0.15 - y - fh - 0.3
    pt55 = PT["body"] if max(card_h(a, b, cw, pt=PT["body"]) for a, b in items) <= free else BODY
    kit.room("validation cards", ch_need, free)
    fh = max(fh, ky - 0.15 - y - 0.3 - max(card_h(a, b, cw, pt=pt55) for a, b in items) - 0.6)
    kit.flow_row(s, y, fh, steps, gap=0.35)
    yc = y + fh + 0.3
    for x, (a, b) in zip(xs, items):
        card(s, x, yc, cw, a, b, h=ky - 0.15 - yc, pt=pt55)
    src(s, "Source: Milestone 5 report, Section 9.1 and Appendix IX.")


def s56(prs):
    s = kit.base(prs, kicker(56), T("Gate S1 and the Calibration Condition"), notes(56))
    y = lead(s, T("One gate decides whether a model replaces the rule's order, and probabilities are shown only if "
                  "calibration holds."))
    key56 = T("Key: S1–S3 = the success criteria of the predictive model (AQ3), fixed in Milestone 4. Normalised recall "
              "= recall divided by the most a list of its length can reach. Rule-ranked list = the early-sign rule's "
              "flags ordered by their number of signs.")
    ky = bottom_key(s, key56)
    items = [(T("S2: precision at capacity"), [T("The share of the list who do not complete. Reported, not a gate: recall, precision and "
                                                 "lift at capacity re-express the same listed non-completers, so S1 "
                                                 "alone decides.")]),
             (T("S3: calibration"), [T("Probabilities are shown only if calibration-in-the-large lies between −0.2 and "
                                       "0.2 and the slope between 0.8 and 1.2; otherwise staff see ranks and reasons "
                                       "only. Never recalibrated on 2014.")])]
    xs, cw = cols(2, 0.25)
    chh = max(card_h(a, b, cw, pt=PT["body"]) for a, b in items)
    yc = ky - 0.15 - chh
    for x, (a, b) in zip(xs, items):
        card(s, x, yc, cw, a, b, h=chh, pt=PT["body"])
    top, bot = y, yc - 0.3
    w1, w2, w3 = 3.0, 5.2, 3.2
    gap = (CWI - w1 - w2 - w3) / 2
    x1, x2 = X0, X0 + w1 + gap
    x3 = x2 + w2 + gap
    node(s, x1, top, w1, bot - top, T("Model list against rule-ranked list"),
         [T("All 13 test runs of 2014"), T("Day 27, 5 contacts per 20 students")], style="soft")
    gate = [T("Pooled normalised recall above the rule list's."),
            T("95% paired two-level bootstrap interval of the difference above 0."),
            T("One-sided sign-flip test over the 13 per-run differences: p below 0.05.")]
    node(s, x2, top, w2, bot - top, T("Gate S1: all three must hold"), gate, style="system", body_pt=PT["body"])
    arrow(s, x1 + w1 + 0.05, (top + bot) / 2, x2 - 0.05, (top + bot) / 2)
    eh = (bot - top - 0.3) / 2
    node(s, x3, top, w3, eh, T("Pass: the model's order"), T("reported with the number of extra non-completers "
                                                              "listed"), style="out")
    node(s, x3, top + eh + 0.3, w3, eh, T("Fail: the rule's order stays"), T("an acceptable outcome"), style="bad")
    path(s, [(x2 + w2 + 0.05, (top + bot) / 2), (x2 + w2 + gap / 2, (top + bot) / 2),
             (x2 + w2 + gap / 2, top + eh / 2), (x3 - 0.05, top + eh / 2)])
    path(s, [(x2 + w2 + gap / 2, (top + bot) / 2), (x2 + w2 + gap / 2, top + eh * 1.5 + 0.3),
             (x3 - 0.05, top + eh * 1.5 + 0.3)])
    src(s, "Source: Milestone 5 report, Section 9.1 and Appendix IX, Table A.23.")


def s57(prs):
    s = kit.base(prs, kicker(57), T("Fairness and Rule FR1"), notes(57))
    y = lead(s, T("The list is audited for equal recall across groups, and a clear gap sends the group to human review, "
                  "not to an automatic verdict."))
    lw = 6.3
    fair = [
        T("Group attributes stay out of the predictors and serve only the audit, because bias cannot be audited "
          "without group membership."),
        tb("Criterion: ", "equal recall at capacity, so a struggling student has the same chance of being listed "
                          "whatever the group."),
        tb("Rule FR1 (fairness review rule): ", "flag a group for human review when its recall is more than 10 points "
                                                "below the other students' and the Holm-adjusted (corrected for "
                                                "several tests) one-sided interval of the gap lies below 0."),
        tb("No flag ", "means no evidence of a gap at that precision, not proof that the list is fair."),
        tb("A flag ", "calls for review of why the gap arises, not rejection of the model.")]
    pt17 = fit_pt(fair, lw, END - y)
    rich(s, X0, y, lw, fair, pt=pt17)
    rx, rw = X0 + lw + 0.4, CWI - lw - 0.4
    y1 = head(s, rx, y, rw, T("Confirmatory groups in the 2014 test at day 27 (enrolments)"))
    xs, cw = cols(3, 0.2, rx, rw)
    for x, (v, lab) in zip(xs, [("1,488", T("declared disability")), ("1,486", T("most deprived band (0–10%)")),
                                ("610", T("missing deprivation band"))]):
        rect(s, I(x), I(y1 + 0.12), I(cw), I(1.4), fill=SOFT, line=LINE, radius=True)
        text(s, I(x), I(y1 + 0.2), I(cw), I(0.5), v, size=PT["cover"] - 4, color=NAVY, bold=True,
             align=PP_ALIGN.CENTER, spacing=1.0)
        rich(s, x + 0.1, y1 + 0.74, cw - 0.2, [lab], align=PP_ALIGN.CENTER)
    yk = key(s, y1 + 1.62, T("Confirmatory: fixed in advance, each with at least 400 test enrolments. Aged 55 or over: "
                            "118, too few; the gap is reported as \"insufficient data, not cleared\". Deprivation band "
                            "= band of the Index of Multiple Deprivation of the student's home area."), rx, rw)
    key17 = T("Key: the bar is the largest recall gap, in percentage points, allowed before human review. Recall at "
              "capacity = share of a group's non-completers who make the list. No recall values exist yet.")
    by_low = END - lh(key17, rw, PT["small"]) - 1.2
    by = max(yk + 0.2, yk + 0.2 + (by_low - yk - 0.2) / 2)
    head(s, rx, by, rw, T("FR1 threshold"))
    scale = (rw - 0.4) / 30
    bx = rx + 0.2
    rect(s, I(bx), I(by + 0.42), I(10 * scale), I(0.3), fill=WARM)
    rect(s, I(bx), I(by + 0.85), I(30 * scale), I(0.02), fill=GREY)
    for p in (0, 10, 20, 30):
        rect(s, I(bx + p * scale - 0.01), I(by + 0.8), I(0.02), I(0.1), fill=GREY)
        text(s, I(bx + p * scale - 0.5), I(by + 0.92), I(1.0), I(0.25), str(p), size=PT["small"], color=KEY,
             align=PP_ALIGN.CENTER, spacing=1.0)
    text(s, I(bx + 10 * scale + 0.15), I(by + 0.42), I(rw - 10 * scale - 0.4), I(0.3),
         T("10 points"), size=PT["small"] + 2, color=AGENT_INK, bold=True, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    yk2 = bottom_key(s, key17, rx, rw)
    kit.room("fairness column", by + 1.2, yk2)
    src(s, "Source: Milestone 5 report, Section 9.2 and Appendix IX, Table A.24.")


def s58(prs):
    s = kit.base(prs, kicker(58), T("Leakage and Interpretability in the Evaluation"), notes(58))
    y = lead(s, T("No 2014 outcome enters any AQ3 choice, and each listed student's reasons come from the same model "
                  "that ranks the student."))
    xs, cw = cols(2, 0.35)
    ky = bottom_key(s, T("Key: AQ3 = the predictive question (model against the early-sign rule). Leakage = information "
                         "that would not exist at the moment of use. Fold = one 2013 run held out in development. Model "
                         "card and datasheet = standard documents of a model's and a dataset's use and limits."))
    bottom = ky - 0.15
    leak = [tb("1. Choices fixed on 2013. ", "Predictors, candidates, selection rule and gate were fixed in Milestone 4 "
                                            "on the 2013 runs alone."),
            tb("2. Refit inside each fold. ", "Filling, scaling and tuning are redone, so no held-out run informs its "
                                             "own prediction."),
            tb("3. Folds only choose. ", "Fold results are never reported as performance, because a score that guided "
                                        "a choice flatters the chosen model.")]
    spread_card(s, xs[0], y, cw, bottom - y, T("Leakage controls of the evaluation"), leak,
                sizes=(PT["body"], BODY))
    rx = xs[1]
    y1 = head(s, rx, y, cw, T("What a lecturer would see (illustration, not data)"))
    rh = 1.3
    rect(s, I(rx), I(y1 + 0.12), I(cw), I(rh), fill=WHITE, line=NAVY, radius=True, line_w=1.5)
    circ = s.shapes.add_shape(9, I(rx + 0.2), I(y1 + 0.12 + (rh - 0.6) / 2), I(0.6), I(0.6))
    circ.fill.solid()
    circ.fill.fore_color.rgb = NAVY
    circ.line.fill.background()
    text(s, I(rx + 0.2), I(y1 + 0.12 + (rh - 0.6) / 2), I(0.6), I(0.6), "1", size=PT["head"], color=WHITE, bold=True,
         align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    text(s, I(rx + 0.95), I(y1 + 0.2), I(cw - 1.1), I(0.3), T("Student, rank 1 of the run's list"), size=PT["body"],
         color=NAVY, bold=True, spacing=1.0)
    chips_ = [T("Task due, not submitted"), T("No click, days 21–27"), T("Clicks below run median")]
    cxs, ccw = cols(3, 0.1, rx + 0.95, cw - 1.1)
    for x, c in zip(cxs, chips_):
        chip(s, x, y1 + 0.62, ccw, 0.6, c, fill=ACC_FILL, line_color=WARM, size=PT["small"])
    interp = [tb("Reasons shown are reasons used: ", "each name's signs come from the same model that ranks the "
                                                     "student."),
              tb("No coefficient is read as a cause: ", "a sign that raises a rank is a reason to look, not an "
                                                        "explanation."),
              tb("Documented: ", "a model card for the model and a datasheet for its data.")]
    yi = y1 + 0.12 + rh + 0.25
    spread_card(s, rx, yi, cw, bottom - yi, None, interp, sizes=(PT["body"], BODY))
    src(s, "Source: Milestone 5 report, Section 9.2 and Appendix IX.")


# ----------------------------------------------------------------------------- 10 Experimental status
def s59(prs):
    s = kit.base(prs, kicker(59), T("What We Ran: Level 2 for AQ3 and AQ4"), notes(59))
    y = lead(s, T("Every question now has real results: AQ1 and AQ2 on both years, and AQ3 and AQ4 by one test of a "
                  "model frozen on 2013 and scored once on the 13 runs of 2014."))
    xs, cw = cols(4)
    labels = [("AQ1", T("Answered"), T("descriptive"), True), ("AQ2", T("Answered"), T("diagnostic"), True),
              ("AQ3", T("Answered"), T("predictive"), True), ("AQ4", T("Partial"), T("prescriptive"), False)]
    for x, (q, st, lvl, done) in zip(xs, labels):       # two lines per tile: question and level, then the status
        rect(s, I(x), I(y), I(cw), I(0.78), fill=WARM if done else ACC_FILL, line=WARM, radius=True, line_w=2.0)
        ink = WHITE if done else AGENT_INK
        text(s, I(x + 0.15), I(y + 0.05), I(cw - 0.3), I(0.3), q + " · " + lvl, size=PT["small"] + 2, color=ink,
             spacing=1.0)
        text(s, I(x + 0.15), I(y + 0.34), I(cw - 0.3), I(0.4), st, size=PT["head"], color=ink, bold=True,
             spacing=1.0)
    y += 0.86
    y = key(s, y, T("Key: filled orange = Answered; light orange = Partial, the ranking is answered while the contact "
                    "part has no data. Level 2 = the brief's optional level: running "
                    "the model test fixed in Milestone 4. Penalised logistic model = a regression that shrinks weak "
                    "signs.")) + 0.15
    gate = [[(T("Gate S1 (model replaces rule) met: "), AGENT_INK, True),
             (T("normalised recall 72.5% (= last column: each list is shorter than its run's non-completers) vs "
                "70.4% for the rule, ahead in 11 of 13 runs; the model ranks, the rule is the fallback."), INK, False)]]
    gh = rich_h(gate, CWI - 0.36, PT["body"]) + 0.2
    gy = END - gh
    rect(s, MX, I(gy), CW, I(gh), fill=ACC_FILL, line=WARM, radius=True, line_w=1.5)
    rich(s, X0 + 0.18, gy + 0.1, CWI - 0.36, gate, pt=PT["body"])
    y = head(s, X0, y, CWI, T("Lists of 5 per 20 students, day 27, 13 test runs of 2014"))
    rows = [[T("List"), T("Non-completers listed"), T("Share of all non-completers"), T("Share of list not completing")],
            [T("Penalised logistic model (primary)"), num("2,868"), num("41.5%"), num("72.5%")],
            [T("Early-sign rule, ranked by number of signs"), num("2,786"), num("40.3%"), num("70.4%")],
            [T("Model using background only"), num("2,244"), num("32.5%"), num("56.7%")],
            [T("Random list (expected)"), num("1,738"), num("25.1%"), num("43.9%")]]
    shape = fitted_table(s, y + 0.08, rows, [0.4, 0.2, 0.2, 0.2], gy - 0.2, sizes=(PT["body"], BODY, PT["small"]))
    for j in range(4):
        fill_cell(shape.table.cell(1, j), ACC_FILL, AGENT_INK, True)
    src(s, "Source: Milestone 5 report, Sections 3 and 10, Tables 3.1 and 10.1.")


def s60(prs):
    s = kit.base(prs, kicker(60), T("What the Frozen Protocol Fixed, and How It Ran"), notes(60))
    y = lead(s, T("The protocol left no modeling choice open: three baselines and four configurations were fixed on "
                  "2013, and the 2014 outcomes were opened once."))
    lw = 8.0
    ky = bottom_key(s, T("Key: B = baseline; M = model configuration. Primary set = the 19 primary predictors; extended "
                         "set = the primary set plus 10 further predictors. Early-sign rule = flags a missed task, a late "
                         "tutor-marked assignment or no click in the 7 days before the cut-off. Orange row = B2, the "
                         "benchmark the contact decision needs; bold M1 = the model chosen. Ties go to the simpler one."),
                    X0, lw)
    rows = [[T("ID"), T("Role"), T("Method"), T("Predictors")],
            ["B1", T("Baseline"), T("Random list"), "–"],
            ["B2", T("Baseline"), T("Early-sign rule, ranked by its number of signs"),
             T("Rule columns")],
            ["B3", T("Baseline"), T("Background-only logistic model"),
             T("Module, start month, attempts, credits, education, registration lead")],
            ["M1", T("Primary"), T("Penalised logistic regression"), T("Primary set")],
            ["M2", T("Challenger"), T("Penalised logistic regression"), T("Extended set")],
            ["M3", T("Challenger"), T("Gradient-boosted trees"), T("Primary set")],
            ["M4", T("Challenger"), T("Gradient-boosted trees"), T("Extended set")]]
    shape = fitted_table(s, y, rows, [0.08, 0.17, 0.37, 0.38] if kit.LANG == "en" else [0.07, 0.22, 0.31, 0.40], ky - 0.15, w=lw, sizes=(PT["body"], BODY, PT["small"]))
    for j in range(4):
        fill_cell(shape.table.cell(2, j), ACC_FILL)
        fill_cell(shape.table.cell(4, j), WHITE, AGENT_INK, True)
    rx = X0 + lw + 0.35
    rw = XR - rx
    steps = [T("Reproduce the input; check hashes"), T("Fit the baselines"), T("Fit the candidates"),
             T("Apply the split and folds"), T("Evaluate all; report unfavourable results"),
             T("Error and subgroup analysis"), T("Compare with the Level 1 proposal"), T("Record the experiment log")]
    y1 = head(s, rx, y, rw, T("Eight steps"))
    msg = T("One logged test: 2014 outcomes opened once, after the models were frozen with a hash.")
    mh = lh(msg, rw - 0.4, PT["body"], True) + 0.3
    yb = END - mh
    rect(s, I(rx), I(yb), I(rw), I(mh), fill=NAVY, radius=True)
    text(s, I(rx + 0.2), I(yb), I(rw - 0.4), I(mh), msg, size=PT["body"], color=WHITE, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
    gap = 0.08
    sh = (yb - 0.2 - y1 - 0.08 - 7 * gap) / 8
    kit.room("protocol steps", max(lh(st, rw - 0.55, BODY) for st in steps) + 0.06, sh)
    for k, st in enumerate(steps):
        yy = y1 + 0.08 + k * (sh + gap)
        rect(s, I(rx), I(yy), I(rw), I(sh), fill=SOFT, line=LINE, radius=True)
        text(s, I(rx + 0.08), I(yy), I(0.4), I(sh), str(k + 1), size=PT["body"], color=WARM, bold=True,
             anchor=MSO_ANCHOR.MIDDLE, spacing=1.0)
        text(s, I(rx + 0.45), I(yy), I(rw - 0.55), I(sh), st, size=BODY, color=INK, anchor=MSO_ANCHOR.MIDDLE,
             spacing=1.0)
    src(s, "Source: Milestone 5 report, Section 10 and Appendix X, Table A.25.")


# ----------------------------------------------------------------------------- 11 Findings
def s61(prs):
    s = kit.base(prs, kicker(61), T("How We Read the Findings"), notes(61))
    y = lead(s, T("A number means different things at different analytics levels, so every finding carries its level "
                  "and confidence."))
    conf = [(T("High"), T("two independent computations verify the counts on the stated population, not for the "
                          "university's courses."), WARM),
            (T("Moderate"), T("estimates keep their direction under the checks but rest on observational data or a "
                              "model with a known weakness."), NAVY),
            (T("Not applicable"), T("the contact part of AQ4 has no data to test; it waits for a randomised pilot."), GREY)]
    xs, cw = cols(3, 0.2)
    paras = [[[(T("Confidence ") + a.lower() + ": ", AGENT_INK if c == WARM else c, True), (b, INK, False)]]
             for a, b, c in conf]
    bh = max(rich_h(q, cw - 0.4, BODY) for q in paras) + 0.25
    yb = END - bh
    for x, q, (_, _, c) in zip(xs, paras, conf):
        rect(s, I(x), I(yb), I(cw), I(bh), fill=SOFT, line=c, radius=True, line_w=2.0)
        rich(s, x + 0.2, yb + 0.12, cw - 0.4, q, pt=BODY)
    rows = [[T("Question"), T("Evidence reached"), T("What the answer states"), T("What it does not state")],
            [T("AQ1 – Descriptive"), T("Results on 2013, 2014 and the 22 runs pooled"),
             T("Outcome shares and first missed week, with denominator and 95% interval"),
             T("Why a module or run has a higher rate; any rate for the university's own courses")],
            [T("AQ2 – Diagnostic"), T("Results on 2013, replicated on 2014"),
             T("Which signs go with later non-completion within module runs, by how many points"),
             T("That a sign causes non-completion, or that removing it would raise completion")],
            [T("AQ3 – Predictive"), T("Single test, 13 runs of 2014"),
             T("How well the model ranks students against the rule"),
             T("A reliable probability for each run")],
            [T("AQ4 – Prescriptive"), T("Ranking from the AQ3 scores"),
             T("Who ranks first on a list, with a reason per name"),
             T("Whom contact helps, or which contact works")]]
    k61 = T("Key: AQ1–AQ4 = the four analytical questions; every finding is an effect size with its 95% interval "
            "and population; orange column = what the answer does not state.")
    kh = lh(k61, CWI, PT["small"])
    key(s, yb - 0.2 - kh, k61)
    shape = fitted_table(s, y, rows, [0.17, 0.23, 0.31, 0.29], yb - 0.3 - kh)
    fill_cell(shape.table.cell(0, 3), WARM)
    for i in range(1, 5):
        fill_cell(shape.table.cell(i, 3), ACC_FILL)
    src(s, "Source: Milestone 5 report, Section 11 and Appendix XI, Table A.26.")


def s62(prs):
    s = kit.base(prs, kicker(62), T("Traceability Matrix: From Goal to Data"), notes(62))
    y = lead(s, T("Each question traces in one row from the goal and its KPI to the data we actually had, with GAP "
                  "where OULAD lacks a variable."))
    goals = [tb("All rows share one Business Goal: ", "improve successful course completion by identifying students "
                                                      "who stop taking part early enough to support them within the "
                                                      "semester. "),
             tb("SMART Goal: ", "raise completion after the add-drop period in the pilot courses by five percentage "
                                "points (assumed 70% to 75%) by the end of 2027–2028.")]
    goals = [goals[0] + goals[1]]
    k1 = T("Key: AQ1–AQ4 = the four analytical questions. KPI = key performance indicator; primary KPI = completion rate of enrolments after the add-drop "
           "period; KPI 1 = early-sign contact rate; KPI 2 = follow-up rate. GAP (red) = a link without data in "
           "OULAD (Open University Learning Analytics Dataset). SMART = specific, measurable, achievable, relevant, "
           "time-bound.")
    ky = bottom_key(s, k1)
    gh = card_h(None, goals, CWI, pt=BODY)
    card(s, X0, y, CWI, None, goals, h=gh, pt=BODY)
    y += gh + 0.2
    rows = [[T("Question"), T("Goal and KPI"), T("Final question, short"), T("Level"), T("Required data"),
             T("Actual dataset and variables")],
            ["AQ1", T("Primary KPI"), T("Outcome shares; first missed week"), T("Descriptive"),
             T("Dated result, tasks"), T("22 runs, day 14: 28,061; GAP: delivery mode, year of study")],
            ["AQ2", T("Primary KPI; KPI 1"), T("Signs by week 4, within module"), T("Diagnostic"),
             T("Signs, weeks 1–4"), T("Day 27: 11,811 (2013) and 15,724 (2014); GAP: attendance")],
            ["AQ3", T("KPI 1 (the rule to beat)"), T("Weeks 2 and 4 against the rule"), T("Predictive"),
             T("Enrolment at cut-off"), T("19 predictors; 2014 test")],
            ["AQ4", T("KPIs 1–2: GAP"), T("Ranked list per group of 20 students"), T("Prescriptive"),
             T("Capacity; contacts"), T("GAP: contacts")]]
    shape = fitted_table(s, y, rows, [0.1, 0.16, 0.2, 0.12, 0.15, 0.27], ky - 0.15)
    tbl = shape.table
    for i in range(1, 5):
        for j in range(1, 6):
            if "GAP" in rows[i][j]:
                fill_cell(tbl.cell(i, j), WHITE)
                red_from(tbl.cell(i, j), "GAP")
            else:
                fill_cell(tbl.cell(i, j), LINKED)
    src(s, "Source: Milestone 5 report, Sections 2.1 and 11.1, Table 11.1, and Appendix XI, Table A.27.")


def s63(prs):
    s = kit.base(prs, kicker(63), T("Traceability Matrix: From Method to Decision"), notes(63))
    y = lead(s, T("Every link from method to decision now holds evidence: AQ1–AQ3 are answered, AQ4 for its "
                  "ranking."))
    k1 = T("Key: AQ1–AQ4 = the four analytical questions. Grey = the link holds evidence. "
           "TMA, CMA = tutor- and computer-marked tasks. S1 = the gate a model must pass to replace the rule; FR1 = the "
           "fairness review rule. Decisions: D1 whom to contact, D2 where to place support time, D3 whether to "
           "extend. Status: Answered = real results answer all of the question; Partial = the core is answered while "
           "a named part waits for data; no question is dropped.")
    ky = bottom_key(s, k1)
    rows = [[T("Question"), T("Preparation"), T("Method and rationale"), T("Evaluation / result"), T("Decision"),
             T("Status")],
            ["AQ1", T("Day-14 rule; TMA, CMA"), T("Grouped rates; no model needed"), T("Paths agree; 45.3%"),
             "D2, D3", T("Answered")],
            ["AQ2", T("Dated by day 27"), T("Logistic, run effects"), T("5 of 5 signs, both years"), "D2; D1",
             T("Answered")],
            ["AQ3", T("Refit per fold"), T("Penalised logistic; reasons"), T("S1 met: 0.725 vs 0.704"), "D1",
             T("Answered")],
            ["AQ4", T("3 or 5 per 20"), T("Top-k with reasons"), T("FR1: 0 of 3 flagged"), "D1", T("Partial")]]
    shape = fitted_table(s, y, rows, [0.11, 0.19, 0.23, 0.2, 0.12, 0.15], ky - 0.15,
                         sizes=(PT["lead"], PT["body"], BODY))
    tbl = shape.table
    for i in range(1, 5):
        for j in range(1, 5):
            fill_cell(tbl.cell(i, j), LINKED)
        fill_cell(tbl.cell(i, 5), WARM if i < 4 else ACC_FILL, color=WHITE if i < 4 else AGENT_INK, bold=True)
    src(s, "Source: Milestone 5 report, Section 11.1, Table 11.2, and Appendix XI, Tables A.27 and A.28.")


# AQ1 outcome shares, students registered at day 14 (Appendix XII, Table A.29): Distinction, Pass, Fail, Withdrawn.
OUT_SHARES = [("2013", "12,076", (8.9, 45.4, 26.7, 18.9)), ("2014", "15,985", (12.2, 42.9, 23.8, 21.2)),
              ("22 runs", "28,061", (10.8, 44.0, 25.0, 20.2))]


def outcome_shares(fig):
    ax = charts.axes(fig)
    names = [T("Distinction"), T("Pass"), T("Fail"), T("Withdrawn")]
    cols_ = ["#C9CED5", C_GREY, C_ACC, f"#{AGENT_INK}"]
    n = len(OUT_SHARES)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xlim(0, 100)
    for i, (_, _, vals) in enumerate(OUT_SHARES):
        acc = 0.0
        for v, c in zip(vals, cols_):
            ax.barh(i, v, left=acc, height=0.6, color=c, edgecolor="white", lw=1.2, zorder=3)
            ax.text(acc + v / 2, i, f"{charts.num(v, 1)}%", ha="center", va="center", fontsize=charts.size("value"),
                    color="white" if c in (C_ACC, f"#{AGENT_INK}") else C_INK, zorder=4)
            acc += v
    ax.set_yticks(range(n), [f"{T(a)}\n(n = {num(b)})" for a, b, _ in OUT_SHARES])
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.legend(handles=[Patch(fc=c, label=nm) for nm, c in zip(names, cols_)], loc="lower left",
              bbox_to_anchor=(0, 1.02), ncol=4, frameon=False, handlelength=1.4, columnspacing=1.2, borderaxespad=0,
              fontsize=charts.size("small"))


def s64(prs):
    s = kit.base(prs, kicker(64), T("AQ1: How Many Do Not Complete"), notes(64))
    y = lead(s, T("Close to half of the enrolments still registered at day 14 do not complete, a quarter by failing and "
                  "a fifth by withdrawing, and the two years agree."))
    lw, rw, rx = kit.split(0.4)
    bh = 1.85
    rect(s, I(X0), I(y), I(lw), I(bh), fill=SOFT, line=LINE, radius=True)
    bignum(s, X0, y + 0.1, lw, T("45.3%"), T("(44.7–45.8) of the 28,061 enrolments still registered at day 14, over 22 runs, did not complete: 12,700."),
           color=WARM)
    facts = [tb("2013: ", "45.7% (44.8–46.6) of 12,076."),
             tb("2014: ", "44.9% (44.2–45.7) of 15,985."),
             tb("Success criterion met: ", "two independent counts, from the prepared and the raw "
                                           "data, agree exactly."),
             tb("Confidence: ", "high for OULAD 2013–2014; validity for the university's courses remains open.")]
    ky = bottom_key(s, T("Key: AQ1 = descriptive question (outcome shares and timing). Day 14 = end of the add-drop "
                         "period. Non-completion = Fail or Withdrawn. Intervals = 95% confidence intervals. OULAD = Open "
                         "University Learning Analytics Dataset."), X0, lw)
    room = ky - 0.15 - (y + bh + 0.2)
    pt = fit_pt(facts, lw, room)
    kit.room("aq1 facts", rich_h(facts, lw, pt), room)
    rich(s, X0, y + bh + 0.2, lw, facts, pt=pt)
    y1 = head(s, rx, y, rw, T("Final outcome, enrolments registered at day 14 (%)"))
    chart(s, "m5-full-p3-outcomes", rx, y1 + 0.1, rw, END - y1 - 0.1, outcome_shares)
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Table A.29.")


def s65(prs):
    s = kit.base(prs, kicker(65), T("AQ1: Modules, Runs and Start Months"), notes(65))
    y = lead(s, T("Non-completion ranges from about a quarter to over half between modules and runs, and February runs "
                  "lose more students than October runs in both years."))
    lw, rw, rx = kit.split(0.58)
    y1 = head(s, X0, y, lw, T("Non-completion per module, students registered at day 14"))
    ky = bottom_key(s, T("Key: bar = rate in %; whisker = 95% Wilson interval; CCC ran only in 2014. AAA–GGG = "
                         "anonymised module codes of OULAD (Open University Learning Analytics Dataset)."), X0, lw)
    chart(s, "m5-full-p3-aq1-modules", X0, y1 + 0.1, lw, ky - y1 - 0.2, aq1_modules)
    facts = [tb("Modules, both years: ", "lowest AAA, 26.3% of 720; highest CCC, 54.3% (2014 only)."),
             tb("Runs, all 22: ", "from 24.9% (AAA 2013J) to 58.3% (CCC 2014B)."),
             tb("Start month: ", "February 51.6% against October 42.4% in 2013; 49.6% against 41.6% in 2014."),
             tb("How students leave: ", "in GGG 2013, 4.3% withdrew and 31.7% failed; in CCC, 33.1% withdrew and 21.3% "
                                        "failed."),
             [(T("So: a hypothesis for decision D2, where support time would go first, to be checked on the "
                 "university's records."), AGENT_INK, True)]]
    kx = T("Key: AQ1 = descriptive question. Run = one offering of a module, named by year and start month (B = "
           "February, J = October).")
    ky2 = bottom_key(s, kx, rx, rw)
    pt = fit_pt(facts, rw, ky2 - 0.15 - y)
    kit.room("aq1 module facts", rich_h(facts, rw, pt), ky2 - 0.15 - y)
    rich(s, rx, y, rw, facts, pt=pt)
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Figure A.2 and Table A.30.")


# Table A.29: (label, failed, withdrawn, total non-completion, n)
DENOM = [("2013\nday 14", 26.7, 18.9, 45.7, "12,076"), ("2013\nall", 24.0, 27.5, 51.4, "13,529"),
         ("2014\nday 14", 23.8, 21.2, 44.9, "15,985"), ("2014\nall", 20.0, 33.8, 53.8, "19,064")]


def denom_bars(fig):
    ax = charts.axes(fig)
    xs = [0, 1, 2.5, 3.5]
    ax.set_xlim(-0.6, 4.1)
    ax.set_ylim(0, 64)
    for x, (lab, f, w, tot, n) in zip(xs, DENOM):
        ax.bar(x, f, 0.7, color=C_GREY, edgecolor="white", lw=1.2, zorder=3)
        ax.bar(x, w, 0.7, bottom=f, color=C_ACC, edgecolor="white", lw=1.2, zorder=3)
        ax.text(x, f / 2, f"{charts.num(f, 1)}%", ha="center", va="center", fontsize=charts.size("value"),
                color=C_INK, zorder=4)
        ax.text(x, f + w / 2, f"{charts.num(w, 1)}%", ha="center", va="center", fontsize=charts.size("value"),
                color="white", zorder=4)
        ax.annotate(f"{charts.num(tot, 1)}%", (x, tot), xytext=(0, 3), textcoords="offset points", ha="center",
                    va="bottom", fontsize=charts.size("value"), color=C_INK, fontweight="bold")
    ax.set_xticks(xs, [f"{T(a.split(chr(10))[0])}\n{T(a.split(chr(10))[1])}\n(n = {num(d[4])})"
                       for a, d in zip([d[0] for d in DENOM], DENOM)])
    ax.set_yticks([])
    ax.spines["bottom"].set_color(f"#{kit.C_GRID}")
    ax.legend(handles=[Patch(fc=C_GREY, label=T("Fail")), Patch(fc=C_ACC, label=T("Withdrawn"))], loc="lower left",
              bbox_to_anchor=(0, 1.02), ncol=2, frameon=False, handlelength=1.4, columnspacing=1.2, borderaxespad=0,
              fontsize=charts.size("small"))


def s66(prs):
    s = kit.base(prs, kicker(66), T("AQ1: The Denominator Matters"), notes(66))
    y = lead(s, T("Counting all enrolments instead of those registered at day 14 lifts non-completion above half, "
                  "almost entirely through early withdrawals."))
    lw, rw, rx = kit.split(0.48)
    y1 = head(s, X0, y, lw, T("Non-completion under two denominators, %"))
    ky = bottom_key(s, T("Key: day 14 = enrolments still registered at the end of the add-drop period (the KPI "
                         "population); all = every enrolment, including those who left before day 14. Bar = Fail plus "
                         "Withdrawn; bold = non-completion. KPI = key performance indicator."), X0, lw)
    chart(s, "m5-full-p3-denominator", X0, y1 + 0.1, lw, ky - y1 - 0.2, denom_bars)
    side = [(T("The failed share barely moves"), T("The extra non-completers are early withdrawals."), NAVY),
            (T("One run: 13.6 points"), T("BBB 2014J: 36.2% of 1,791 at day 14; 49.7% of all 2,292."), NAVY),
            (T("Flagged records change nothing"), T("Without unknown withdrawal or registration days: 45.6% (2013) and "
                                                    "44.6% (2014) at day 14."), NAVY),
            (T("So"), T("Every rate must name its denominator; the KPI fixes the add-drop rule."), WARM)]
    stack_cards(s, rx, y, rw, side, gap=0.18)
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Tables A.29 and A.32.")


def s67(prs):
    s = kit.base(prs, kicker(67), T("AQ1: The Year Comparison Depends on the Add-drop Rule"), notes(67))
    y = lead(s, T("Over all enrolments 2014 looks worse than 2013, but among students registered at day 14 it is no "
                  "worse, because more 2014 students left before day 14."))
    lw, rw, rx = kit.split(0.6)
    y1 = head(s, X0, y, lw, T("Change in non-completion from 2013 to 2014"))
    ky = bottom_key(s, T("Key: dot = 2014 minus 2013 in points; whisker = 95% Newcombe interval, and one that crosses 0 "
                         "shows no clear difference. Grey = over all enrolments; orange = registered at day 14 (the KPI "
                         "rule). KPI = key performance indicator (completion after add-drop)."), X0, lw)
    chart(s, "m5-full-p3-year-diff", X0, y1 + 0.1, lw, ky - y1 - 0.2, year_diff)
    side = [(T("The rise comes from CCC"), T("Over all enrolments the +2.3 points come from module CCC, which ran only "
                                             "in 2014 (non-completion 62.2% of its enrolments); the six shared modules show −0.2."),
             NAVY),
            (T("Why the years flip"), T("16.2% of 2014 enrolments against 10.7% of 2013 were not registered at day 14, "
                                        "so more 2014 non-completers left before the KPI counts them."), NAVY),
            (T("So"), T("No general rise among the students the KPI counts; a yearly figure must state its add-drop "
                        "rule."), WARM)]
    stack_cards(s, rx, y, rw, side)
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Table A.32.")


GROUPS = [("Declared disability", 55.0, 54.9), ("No declared disability", 44.7, 43.9),
          ("Most deprived band (0–10%)", 61.2, 53.8), ("Least deprived band (90–100%)", 35.2, 36.0)]


def group_bars(fig):
    ax = charts.axes(fig)
    charts.bars(ax, [T(g[0]) for g in GROUPS], {"2013": [g[1] for g in GROUPS], "2014": [g[2] for g in GROUPS]},
                horizontal=True, pct=True, digits=1, limit=75, colors=[C_GREY, C_ACC])


def s68(prs):
    s = kit.base(prs, kicker(68), T("AQ1: Non-completion by Group of Students"), notes(68))
    y = lead(s, T("Non-completion is higher for students with a declared disability and rises with deprivation, which "
                  "is why these groups anchor the fairness audit."))
    lw, rw, rx = kit.split(0.58)
    y1 = head(s, X0, y, lw, T("Non-completion by group, students registered at day 14 (%)"))
    ky = bottom_key(s, T("Key: bar length = non-completion (Fail or Withdrawn) in the group. Groups: declared "
                         "disability 1,157 (2013) and 1,519 (2014); most deprived band 1,196 and 1,512; least deprived "
                         "band 969 and 1,299. Deprivation band = Index of Multiple Deprivation band of the student's home "
                         "area."), X0, lw)
    chart(s, "m5-full-p3-groups", X0, y1 + 0.1, lw, ky - y1 - 0.2, group_bars)
    side = [(T("Described, not explained"), T("The rates are not adjusted for any other difference, so they say nothing "
                                              "about why the groups differ."), NAVY),
            (T("Too few to compare"), T("Students aged 55 or over: 76 in 2013 and 122 in 2014, too uncertain for any "
                                        "comparison."), NAVY),
            (T("So"), T("These are the groups where a list could fail students most: the confirmatory groups of the "
                        "fairness audit (") + ref(57) + ").", WARM)]
    stack_cards(s, rx, y, rw, side)
    src(s, "Source: Milestone 5 report, Sections 9.2 and 11.2, and Appendix XII.")


MISSED_W = {"2013": [19.6, 37.4, 78.1], "2014": [14.7, 33.4, 72.7]}


def missed_steps(fig):
    ax = charts.axes(fig)
    charts.bars(ax, [T("By week 4 (day 27)"), T("By week 8"), T("During the run")], MISSED_W, horizontal=True,
                pct=True, digits=1, limit=100, colors=[C_GREY, C_ACC])


def s69(prs):
    s = kit.base(prs, kicker(69), T("AQ1: When Non-completers First Miss a Task"), notes(69))
    y = lead(s, T("Most non-completers miss a task at some point, but under one in five has missed one by week 4, when "
                  "the list is made."))
    lw, rw, rx = kit.split(0.55)
    y1 = head(s, X0, y, lw, T("Non-completers who had missed a task (TMA or CMA), %"))
    ky = bottom_key(s, T("Key: population = non-completers registered at day 14, 5,515 in 2013 and 7,185 in 2014. TMA = "
                         "tutor-marked assignment; CMA = computer-marked assessment; missed = fell due with no "
                         "submission. Week 4 ends on day 27. OULAD = Open University Learning Analytics Dataset."), X0, lw)
    chart(s, "m5-full-p3-missed", X0, y1 + 0.1, lw, ky - y1 - 0.2, missed_steps)
    side = [(T("Completers rarely miss early"), T("Under 1% by week 4; 21.9% (2013) and 19.4% (2014) during the run."),
             NAVY),
            (T("Late for most"), T("The median non-completer first misses a task in week 9 in both years; six of the 22 "
                                   "runs had no task due by day 27."), NAVY),
            (T("So"), T("A rule on tasks alone comes too late, which is why the early-sign rule also counts "
                        "inactivity. Confidence: high for OULAD."), WARM)]
    stack_cards(s, rx, y, rw, side)
    src(s, "Source: Milestone 5 report, Section 11.2 and Appendix XII, Table A.31.")


SLIDES = {47: s47, 48: s48, 49: s49, 50: s50, 51: s51, 52: s52, 53: s53, 54: s54, 55: s55, 56: s56, 57: s57,
          58: s58, 59: s59, 60: s60, 61: s61, 62: s62, 63: s63, 64: s64, 65: s65, 66: s66, 67: s67, 68: s68, 69: s69}
