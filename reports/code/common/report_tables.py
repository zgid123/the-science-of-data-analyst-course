"""Build the Markdown tables of the four reports from the result tables.

    python common/report_tables.py        prints every table (run through common/run_step.py: logs/report_tables.md)

The reports (`aq-*/README.md`) hold these tables as printed here. `common/check_reports.py` imports the same
functions and fails when a row of a report differs from the row built from the result tables, so a report cannot
state a table value the result tables do not hold. Percentages are rounded half up on the decimal value.
"""

from __future__ import annotations

import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import polars as pl

ROOT = Path(__file__).resolve().parents[1]
MINUS = "−"


def rnd(x: float, digits: int = 1) -> str:
    """Half-up rounding on the decimal value, with a true minus sign."""
    q = Decimal(repr(round(float(x), 9))).quantize(Decimal(10) ** -digits, rounding=ROUND_HALF_UP)
    s = f"{q:.{digits}f}"
    if q == 0:
        s = s.lstrip("-")
    return s.replace("-", MINUS)


def pct(x: float, digits: int = 1) -> str:
    return rnd(x * 100, digits) + "%"


def signed(x: float, digits: int = 1, scale: float = 100.0) -> str:
    s = rnd(x * scale, digits)
    return s if s.startswith(MINUS) else "+" + s


def ci(lo: float, hi: float, digits: int = 1, scale: float = 100.0, sign: bool = False) -> str:
    f = (lambda v: signed(v, digits, scale)) if sign else (lambda v: rnd(v * scale, digits))
    return f"{f(lo)} to {f(hi)}"


def table(header: list[str], rows: list[list[str]]) -> list[str]:
    return ["| " + " | ".join(header) + " |", "| " + " | ".join(":----" for _ in header) + " |", *["| " + " | ".join(r) + " |" for r in rows]]


def csv(rel: str) -> pl.DataFrame:
    return pl.read_csv(ROOT / rel)


# =====================================================================================================================
# AQ1
# =====================================================================================================================
def aq1_tables() -> dict[str, list[str]]:
    out = {}
    rt = csv("aq-1/results/rates_all.csv")
    lab = {"pooled": "All runs", "year": "Year", "start_month": "Start month", "module": "Module"}
    names = {"B": "February (B)", "J": "October (J)", "all runs": "22 runs"}
    rows = []
    for r in rt.filter(pl.col("level").is_in(list(lab))).iter_rows(named=True):
        g = str(r["group"])
        rows.append([lab[r["level"]], names.get(g, g), f"{r['enrolments']:,}", f"{r['events']:,}", pct(r["rate"]), ci(r["ci_low"], r["ci_high"])])
    out["AQ1 Table 1. Non-completion rate (Fail or Withdrawn) of enrolments registered at day 14, with Wilson 95% intervals"] = table(
        ["Level", "Group", "Enrolments", "Non-completers", "Rate", "95% interval"], rows)

    yc = csv("aq-1/results/year_comparison_all.csv")
    den = {"registered at day 14 (KPI population)": "Registered at day 14", "all enrolments": "All enrolments"}
    rows = []
    for r in yc.filter(pl.col("level") == "overall").iter_rows(named=True):
        method = "pooled" if r["method"].startswith("pooled") else "weighted over the pairs"
        rows.append([den[r["denominator"]], r["scope"].replace(" x ", " × "), method, f"{r['n_2013']:,}", pct(r["rate_2013"]), f"{r['n_2014']:,}", pct(r["rate_2014"]),
                     f"{signed(r['difference_2014_minus_2013'])} ({ci(r['ci_low'], r['ci_high'], sign=True)})"])
    out["AQ1 Table 2. Non-completion in 2014 minus 2013, percentage points with 95% interval, under two denominators"] = table(
        ["Denominator", "Runs compared", "Method", "2013 enrolments", "2013 rate", "2014 enrolments", "2014 rate", "2014 − 2013 (95% interval)"], rows)

    def both_den(level: str, scope: str) -> list[str]:
        cells = []
        for d in den:
            r = yc.filter((pl.col("level") == level) & (pl.col("scope") == scope) & (pl.col("denominator") == d) & pl.col("method").str.starts_with("pooled")).row(0, named=True)
            cells += [f"{r['n_2013']:,} / {r['n_2014']:,}", f"{pct(r['rate_2013'])} / {pct(r['rate_2014'])}",
                      f"{signed(r['difference_2014_minus_2013'])} ({ci(r['ci_low'], r['ci_high'], sign=True)})"]
        return cells

    rows = [[m, *both_den("module", m)] for m in yc.filter(pl.col("level") == "module")["scope"].unique(maintain_order=True).to_list()]
    for sm, name in (("B", "February runs, modules run in both years"), ("J", "October runs, modules run in both years")):
        rows.append([name, *both_den("start month, modules run in both years", sm)])
    for sm, name in (("B", "February runs, all modules"), ("J", "October runs, all modules")):
        rows.append([name, *both_den("start month, all modules", sm)])
    out["AQ1 Table 3. The year difference by module and by start month (2013 / 2014)"] = table(
        ["Group", "Registered at day 14: enrolments", "Rate", "2014 − 2013 (95% interval)", "All enrolments: enrolments", "Rate", "2014 − 2013 (95% interval)"], rows)

    nr = csv("aq-1/results/not_registered_d14_by_year_all.csv")
    rows = [[r["scope"].replace(" x ", " × "), f"{r['not_registered_2013']:,} of {r['enrolments_2013']:,} ({pct(r['share_not_registered_2013'])})",
             f"{r['not_registered_2014']:,} of {r['enrolments_2014']:,} ({pct(r['share_not_registered_2014'])})",
             f"{signed(r['difference_2014_minus_2013'])} ({ci(r['ci_low'], r['ci_high'], sign=True)})",
             f"{pct(r['non_completion_among_not_registered_2013'])} / {pct(r['non_completion_among_not_registered_2014'])}"] for r in nr.iter_rows(named=True)]
    out["AQ1 Table 4. Enrolments not registered at day 14, by year"] = table(
        ["Runs compared", "2013", "2014", "2014 − 2013 (95% interval)", "Of these, Fail or Withdrawn (2013 / 2014)"], rows)

    sh = csv("aq-1/results/outcome_shares_all.csv").filter(pl.col("level").is_in(["pooled", "module"]))
    rows = []
    for g in sh["group"].unique(maintain_order=True).to_list():
        t = sh.filter(pl.col("group") == g)
        v = {r["final_result"]: r for r in t.iter_rows(named=True)}
        rows.append(["All runs" if g == "all runs" else g, f"{v['Pass']['enrolments']:,}", *[pct(v[k]["rate"]) for k in ("Distinction", "Pass", "Fail", "Withdrawn")]])
    out["AQ1 Table 5. Outcome shares by module, KPI population"] = table(["Module", "Enrolments", "Distinction", "Pass", "Fail", "Withdrawn"], rows)

    dp = csv("aq-1/results/denominators_pooled_all.csv")
    rows = [[r["denominator"], f"{r['enrolments']:,}", f"{r['non_completers']:,}", pct(r["rate"])] for r in dp.iter_rows(named=True)]
    out["AQ1 Table 6. The same rate under three denominators"] = table(["Denominator", "Enrolments", "Non-completers", "Rate"], rows)

    fm = csv("aq-1/results/first_missed_task_by_outcome_all.csv")
    order = ["Non-completers (Fail or Withdrawn)", "Fail", "Withdrawn", "Completers (Pass or Distinction)"]
    rows = []
    for g in order:
        r = fm.filter(pl.col("group") == g).row(0, named=True)
        rows.append([g if g not in ("Fail", "Withdrawn") else f"– {g}", f"{r['enrolments']:,}", pct(r["share_ever_missed"]), rnd(r["median_first_missed_week"], 0),
                     *[pct(r[f"share_missed_by_week_{w}"]) for w in (4, 8, 12, 20)]])
    out["AQ1 Table 7. First assessed task (TMA or CMA) due while enrolled and not submitted, KPI population"] = table(
        ["Final result", "Enrolments", "Ever missed a task", "Median week of the first miss", "Missed by week 4", "By week 8", "By week 12", "By week 20"], rows)

    w4 = csv("aq-1/results/first_missed_by_week4_all.csv").filter(pl.col("group").str.starts_with("Non-completers"))
    rows = []
    for pop in ("all runs", "runs with a task due by day 27"):
        for yr in ("both years", "2013", "2014"):
            r = w4.filter((pl.col("population") == pop) & (pl.col("year").cast(pl.Utf8) == yr)).row(0, named=True)
            rows.append([pop.capitalize(), yr.capitalize() if yr == "both years" else yr, str(r["runs"]), f"{r['enrolments']:,}", f"{r['missed_by_week_4']:,}",
                         pct(r["share"]), ci(r["ci_low"], r["ci_high"])])
    out["AQ1 Table 8. Non-completers with a missed task by the end of week 4"] = table(
        ["Runs", "Year", "Number of runs", "Non-completers", "Missed a task by week 4", "Share", "95% interval"], rows)

    bm = csv("aq-1/results/first_missed_task_by_module_all.csv")
    cal = csv("aq-1/results/task_calendar_by_run_all.csv").with_columns(pl.col("run").str.slice(0, 3).alias("code_module")).group_by("code_module").agg(
        (pl.col("tasks_due_by_day27") > 0).sum().alias("with"), pl.len().alias("runs"))
    rows = []
    for r in bm.iter_rows(named=True):
        c = cal.filter(pl.col("code_module") == r["code_module"]).row(0, named=True)
        w4m = "no task due by day 27" if c["with"] == 0 else pct(r["share_missed_by_week_4"])
        rows.append([r["code_module"], f"{c['with']} of {c['runs']}", f"{r['non_completers']:,}", pct(r["share_ever_missed"]), rnd(r["median_first_missed_week"], 1).replace(".0", ""),
                     w4m, pct(r["share_missed_by_week_8"])])
    out["AQ1 Table 9. Non-completers by module: when the first missed task appears"] = table(
        ["Module", "Runs with a task due by day 27", "Non-completers", "Ever missed a task", "Median week of the first miss", "Missed by week 4", "Missed by week 8"], rows)

    au = csv("aq-1/results/rates_by_audit_group_all.csv")
    pick = [("gender", "F", "Gender", "Female"), ("gender", "M", "Gender", "Male"), ("disability", "N", "Disability", "Not declared"), ("disability", "Y", "Disability", "Declared"),
            ("imd_band", "0-10%", "Deprivation band", "0–10% (most deprived)"), ("imd_band", "40-50%", "Deprivation band", "40–50%"),
            ("imd_band", "90-100%", "Deprivation band", "90–100% (least deprived)"), ("imd_band", "Missing", "Deprivation band", "Missing"),
            ("age_band", "0-35", "Age band", "0–35"), ("age_band", "35-55", "Age band", "35–55"), ("age_band", "55<=", "Age band", "55 or over")]
    rows = []
    for a, g, la, lg in pick:
        r = au.filter((pl.col("attribute") == a) & (pl.col("group") == g)).row(0, named=True)
        rows.append([la, lg, f"{r['enrolments']:,}", pct(r["rate"]), ci(r["ci_low"], r["ci_high"])])
    out["AQ1 Table 10. Non-completion by audit attribute, KPI population"] = table(["Attribute", "Group", "Enrolments", "Rate", "95% interval"], rows)
    return out


# =====================================================================================================================
# AQ2
# =====================================================================================================================
SIGN_SHORT = {"sign_task_missed": "Task missed", "sign_tma_late": "TMA late", "sign_inactive_last7": "Inactive last 7 days",
              "sign_low_activity": "Low activity", "sign_no_pre_activity": "No pre-start activity",
              "sign_low_activity_q25": "Low activity", "sign_low_activity_median": "Low activity", "sign_low_activity_dedup": "Low activity",
              "sign_any_task_late": "TMA late"}
SIGN_LONG = {"sign_task_missed": "Task due and not submitted", "sign_tma_late": "TMA submitted late", "sign_inactive_last7": "No platform activity in the last 7 days",
             "sign_low_activity": "Clicks below half the run median", "sign_no_pre_activity": "No activity before the start"}
SIGN_ORDER = ["sign_task_missed", "sign_tma_late", "sign_low_activity", "sign_inactive_last7", "sign_no_pre_activity"]
VERDICT = {"consistent association": "Consistent", "weak or inconsistent": "Weak or inconsistent"}


def aq2_tables() -> dict[str, list[str]]:
    out = {}
    for yr in ("2013", "2014"):
        a, orr = csv(f"aq-2/results/associations_{yr}.csv"), csv(f"aq-2/results/odds_ratios_{yr}.csv")
        rows = []
        for s in SIGN_ORDER:
            r, o = a.filter(pl.col("sign") == s).row(0, named=True), orr.filter(pl.col("term") == s).row(0, named=True)
            rows.append([SIGN_LONG[s], f"{r['n_support']:,}", f"{r['with_sign']:,} ({pct(r['share_with_sign'])})", f"{pct(r['rate_with_sign'])} / {pct(r['rate_without_sign'])}",
                         f"{signed(r['unadjusted_rd'])} ({ci(r['unadj_ci_low'], r['unadj_ci_high'])})", f"**{signed(r['adjusted_rd'])}** ({ci(r['adj_ci_low'], r['adj_ci_high'])})",
                         f"{rnd(o['odds_ratio'], 1)} ({rnd(o['or_ci_low'], 1)} to {rnd(o['or_ci_high'], 1)})"])
        runs = "9 runs of 2013" if yr == "2013" else "13 runs of 2014"
        out[f"AQ2 Table {'1' if yr == '2013' else '1b'}. Risk difference in non-completion per sign, {runs}, enrolments registered at day 27"] = table(
            ["Sign at day 27", "n (rows averaged over)", "Students with the sign", "Non-completion with / without", "Unadjusted difference (95% interval)",
             "Adjusted difference (95% interval)", "Odds ratio (95% interval)"], rows)

        bm, ver, sup = csv(f"aq-2/results/associations_by_module_{yr}.csv"), a, csv(f"aq-2/results/sign_support_{yr}.csv")
        mods = sorted(sup["code_module"].unique().to_list())
        rows = []
        for s in SIGN_ORDER:
            cells = []
            for m in mods:
                t = bm.filter((pl.col("sign") == s) & (pl.col("code_module") == m))
                if t.height:
                    r = t.row(0, named=True)
                    txt = f"{signed(r['adjusted_rd'], 0)} ({ci(r['adj_ci_low'], r['adj_ci_high'], 0)}; n = {r['enrolments']:,})"
                    cells.append(txt if r["interval_excludes_0"] else f"*{txt}*")
                else:
                    h = sup.filter((pl.col("sign") == s) & (pl.col("code_module") == m))["handling"][0]
                    cells.append("not defined" if "not defined" in h else h)
            v = ver.filter(pl.col("sign") == s).row(0, named=True)
            rows.append([SIGN_SHORT[s], *cells, f"{v['modules_same_direction']} of {v['modules_defined']}", f"{v['modules_same_direction_interval_excludes_0']} of {v['modules_defined']}"])
        out[f"AQ2 Table {'2' if yr == '2013' else '2b'}. Adjusted risk difference by module, {yr} runs (percentage points, 95% interval, n)"] = table(
            ["Sign", *mods, "Same direction (point estimate)", "Same direction, interval excludes 0"], rows)

    rep = csv("aq-2/results/replication.csv")
    rows = []
    for s in SIGN_ORDER:
        r = rep.filter(pl.col("sign") == s).row(0, named=True)
        rows.append([SIGN_SHORT[s], f"{signed(r['adjusted_rd'])} ({ci(r['adj_ci_low'], r['adj_ci_high'])}), n = {r['n_support']:,}",
                     f"{signed(r['adjusted_rd_2014'])} ({ci(r['adj_ci_low_2014'], r['adj_ci_high_2014'])}), n = {r['n_support_2014']:,}",
                     f"{signed(r['change_2014_minus_2013'])} ({ci(r['change_ci_low'], r['change_ci_high'], sign=True)})",
                     f"{VERDICT[r['verdict']]} / {VERDICT[r['verdict_2014']]}", f"{VERDICT[r['verdict_strict']]} / {VERDICT[r['verdict_strict_2014']]}"])
    out["AQ2 Table 3. Adjusted risk difference per sign, estimation and replication"] = table(
        ["Sign", "2013 runs", "2014 runs", "Change 2014 − 2013 (95% interval)", "Level 1 criterion (2013 / 2014)", "Counting only modules whose interval excludes 0 (2013 / 2014)"], rows)

    ss = csv("aq-2/results/replication_sensitivity.csv")
    vname = {"main": "Main model", "clicks de-duplicated (low-activity sign from de-duplicated clicks)": "Low activity from de-duplicated clicks",
             "late CMAs also count as late": "Late CMAs also count as late", "without flagged enrolments": "Without flagged enrolments",
             "only runs with a task due by day 27": "Only the runs with a task due by day 27",
             "low activity = below a quarter of the run median": "Low activity = below a quarter of the run median",
             "low activity = below the run median": "Low activity = below the run median (the Milestone 5 cut)",
             "post hoc: + log(1 + clicks on days 0-27)": "Post hoc: plus log(1 + clicks on days 0–27)",
             "post hoc: low activity = below the run median, + log(1 + clicks on days 0-27)": "Post hoc: low activity = below the run median, plus log(1 + clicks)"}
    for yr, suf in (("2013", ""), ("2014", "_2014")):
        rows = []
        for v in ss["variant"].unique(maintain_order=True).to_list():
            t = ss.filter(pl.col("variant") == v)
            cells = []
            for s in SIGN_ORDER:
                r = [x for x in t.iter_rows(named=True) if SIGN_SHORT[x["sign"]] == SIGN_SHORT[s]][0]
                txt = f"{rnd(r['adjusted_rd' + suf] * 100)} (n = {r['n' + suf]:,})"
                cells.append(txt if r["verdict" + suf] == "consistent association" else f"**{txt}: criterion not met**")
            rows.append([vname[v], *cells])
        out[f"AQ2 Table {'4' if yr == '2013' else '4b'}. Sensitivity of the adjusted risk differences, {yr} runs (percentage points; n = rows averaged over)"] = table(
            ["Variant", *[SIGN_SHORT[s] for s in SIGN_ORDER]], rows)

    rows = []
    post = ss.filter(pl.col("status") == "post hoc")
    for v in post["variant"].unique(maintain_order=True).to_list():
        for r in post.filter(pl.col("variant") == v).iter_rows(named=True):
            name = SIGN_SHORT[r["sign"]] + (" (below the run median)" if r["sign"] == "sign_low_activity_median" else " (below half the run median)" if r["sign"] == "sign_low_activity" else "")
            rows.append(["Half the run median (primary)" if "below the run median" not in v else "Run median", name,
                         f"{signed(r['adjusted_rd'])} ({ci(r['adj_ci_low'], r['adj_ci_high'])})", f"{r['modules_same_direction']} of {r['modules_defined']}", VERDICT[r["verdict"]],
                         f"{signed(r['adjusted_rd_2014'])} ({ci(r['adj_ci_low_2014'], r['adj_ci_high_2014'])})", f"{r['modules_same_direction_2014']} of {r['modules_defined_2014']}", VERDICT[r["verdict_2014"]]])
    out["AQ2 Table 6. Each sign against the Level 1 criterion when clicks on days 0–27 enter as a continuous adjustment (post hoc)"] = table(
        ["Low-activity cut in the model", "Sign", "2013: adjusted difference (95% interval)", "2013: modules, same direction", "2013: criterion",
         "2014: adjusted difference (95% interval)", "2014: modules, same direction", "2014: criterion"], rows)

    r13, r14 = csv("aq-2/results/binned_residuals_activity5_2013.csv"), csv("aq-2/results/binned_residuals_activity5_2014.csv")
    lv = {"1 no click on days 0-27": "No click", "2 below half the run median": "Below half the run median", "3 half the median to the median": "Half the median to the median",
          "4 median to twice the median": "Median to twice the median", "5 twice the median or more": "Twice the median or more"}
    mm = {"main model (low activity = below half the run median)": "Main model", "post hoc: main model + log(1 + clicks on days 0-27)": "Post hoc: plus log(1 + clicks)"}
    rows = []
    for mname, mlab in mm.items():
        for k, lab in lv.items():
            cells = [mlab, lab]
            for d in (r13, r14):
                r = d.filter((pl.col("model") == mname) & (pl.col("activity_level5") == k)).row(0, named=True)
                res = f"{signed(r['residual'])} (±{rnd(r['two_se'] * 100)})"
                cells += [f"{r['enrolments']:,}", f"{pct(r['observed'])} / {pct(r['predicted'])}", f"**{res}**" if r["outside_2se"] else res]
            rows.append(cells)
    out["AQ2 Table 5. Binned residuals by activity level on days 0–27: observed minus predicted non-completion (percentage points; band = ±2 standard errors; bold = outside the band)"] = table(
        ["Model", "Activity level", "2013: enrolments", "2013: observed / predicted", "2013: residual (band)", "2014: enrolments", "2014: observed / predicted", "2014: residual (band)"], rows)

    rows = []
    glab = {("gender", "F"): "Women", ("gender", "M"): "Men", ("disability", "N"): "No declared disability", ("disability", "Y"): "Declared disability",
            ("imd_group", "0-30% (most deprived)"): "Deprivation 0–30% (most deprived)", ("imd_group", "30-70%"): "Deprivation 30–70%",
            ("imd_group", "70-100% (least deprived)"): "Deprivation 70–100% (least deprived)", ("imd_group", "Missing"): "Deprivation band missing"}
    sub = csv("aq-2/results/subgroups_2013.csv")
    for (a, g), lab in glab.items():
        cells = [lab]
        for s in SIGN_ORDER:
            r = sub.filter((pl.col("attribute") == a) & (pl.col("group") == g) & (pl.col("sign") == s)).row(0, named=True)
            cells.append(f"{rnd(r['adjusted_rd'] * 100)} (n = {r['n']:,})")
        rows.append(cells)
    out["AQ2 Table 7. Adjusted risk difference by student group, 2013 runs (percentage points; n = rows of the group averaged over)"] = table(
        ["Group", *[SIGN_SHORT[s] for s in SIGN_ORDER]], rows)
    return out


# =====================================================================================================================
# AQ3
# =====================================================================================================================
def aq3_tables() -> dict[str, list[str]]:
    out = {}
    s1 = csv("aq-3/results/s1_gate.csv").row(0, named=True)
    tp = csv("aq-3/results/test_pooled.csv").filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
    sec = csv("aq-3/results/secondary.csv").filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
    ctx = csv("aq-3/results/test_context_vs_rule.csv")
    f3 = lambda v: rnd(v, 3)  # noqa: E731
    s3 = lambda v: signed(v, 3, 1.0)  # noqa: E731

    def diff_to_m1(name: str) -> str:
        if name == "B2_rule":
            return f"{s3(-s1['difference'])} ({s3(-s1['boot_ci_high'])} to {s3(-s1['boot_ci_low'])})"
        t = ctx.filter((pl.col("ranking_a") == name) & (pl.col("ranking_b") == "M1"))
        if t.height:
            r = t.row(0, named=True)
            return f"{s3(r['difference'])} ({s3(r['boot_ci_low'])} to {s3(r['boot_ci_high'])})"
        r = ctx.filter((pl.col("ranking_a") == "M1") & (pl.col("ranking_b") == name)).row(0, named=True)
        return f"{s3(-r['difference'])} ({s3(-r['boot_ci_high'])} to {s3(-r['boot_ci_low'])})"

    labels = [("B3", "B3 background-only logistic model"), ("B2_rule", "B2 early-sign rule, ranked"), ("M1", "**M1 penalised logistic regression, primary set (chosen)**"),
              ("M2", "M2 penalised logistic regression, extended set"), ("M3", "M3 gradient-boosted trees, primary set"), ("M4", "M4 gradient-boosted trees, extended set")]
    rand = tp["random_list_normalised_recall"][0]
    rows = [["Random list (expected)", f3(rand), "1.00", "0.500", "–"]]
    for name, lab in labels:
        t, s = tp.filter(pl.col("ranking") == name).row(0, named=True), sec.filter(pl.col("ranking") == name).row(0, named=True)
        b = "**" if name == "M1" else ""
        rows.append([lab, f"{b}{f3(t['pooled_normalised_recall'])}{b}", f"{b}{rnd(s['lift'], 2)}{b}", f"{b}{f3(s['roc_auc_within_run'])}{b}", "–" if name == "M1" else diff_to_m1(name)])
    out["AQ3 Table 2. All rankings on the test runs, day 27, 5 per 20"] = table(
        ["Ranking", "Pooled normalised recall", "Lift over the base rate", "ROC-AUC within run", "Difference to M1 (95% interval)"], rows)

    e = csv("aq-3/results/errors_by_slice.csv")
    pick = [("activity_level", "none", "No clicks since the start"), ("activity_level", "low", "Low activity (below half the run median)"), ("activity_level", "normal", "Normal activity"),
            ("attempts", "first attempt", "First attempt at the module"), ("attempts", "repeat attempt", "Repeat attempt"),
            ("registration", "registered after the start", "Registered after the start"), ("final_result", "Fail", "Final result Fail"), ("final_result", "Withdrawn", "Final result Withdrawn")]
    rows = []
    for sl, g, lab in pick:
        r = e.filter((pl.col("slice") == sl) & (pl.col("group") == g)).row(0, named=True)
        rows.append([lab, f"{r['enrolments']:,}", f"{r['non_completers']:,}", pct(r["model_recall"]), pct(r["rule_recall"])])
    out["AQ3 Table 3. Recall by activity level and history, day 27, 5 per 20 (share of the group's non-completers who are listed)"] = table(
        ["Group at day 27", "Enrolments", "Non-completers", "Model recall", "Rule recall"], rows)

    cal = csv("aq-3/results/calibration.csv").filter((pl.col("cutoff") == 27) & (pl.col("model") == "M1")).row(0, named=True)
    cr, fc = csv("aq-3/results/calibration_by_run.csv"), csv("aq-4/results/fairness_calibration.csv")
    rows = [["All 13 test runs (S3)", s3(cal["citl"]), f3(cal["slope"]), pct(cal["mean_predicted"]), pct(cal["observed_rate"])]]
    for run, lab in (("CCC-2014B", "CCC-2014B (module absent from training)"), ("CCC-2014J", "CCC-2014J")):
        r = cr.filter(pl.col("run") == run).row(0, named=True)
        rows.append([lab, s3(r["citl"]), f3(r["slope"]), pct(r["mean_predicted"]), pct(r["observed_rate"])])
    outside = cr.filter(pl.col("citl").abs() > 0.2)["run"].to_list()
    rows.append(["Runs outside ±0.2", f"{len(outside)} of {cr.height} ({', '.join(outside)})", "", "", ""])
    for g in ("Declared disability", "Deprivation band 0–10%"):
        r = fc.filter(pl.col("group") == g).row(0, named=True)
        rows.append([g, s3(r["citl"]), f3(r["slope"]), pct(r["mean_predicted"]), pct(r["observed_rate"])])
    out["AQ3 Table 4. Calibration of the frozen M1 at day 27 (no recalibration on any 2014 row)"] = table(
        ["Scope", "Calibration-in-the-large (target 0)", "Slope (target 1)", "Mean predicted", "Observed"], rows)

    sens = csv("aq-3/results/sensitivity.csv")
    names = ["Main: all runs, day 27, 5 per 20", "Paired runs (module and start month also ran in 2013)", "Unpaired runs (CCC-B, CCC-J, EEE-B, GGG-B)", "Module CCC only",
             "Without module CCC", "Without test enrolments of students seen in 2013", "Without Withdrawn enrolments lacking a withdrawal day", "Rule variant that also counts late CMAs",
             "Labels-available: February runs, trained on 2013 February runs only", "Same February runs, model trained on all 2013 runs", "Day 27, 3 per 20", "Day 13, 5 per 20", "Day 13, 3 per 20"]
    assert sens.height == len(names)
    rows = [[n, str(r["runs"]), f3(r["model_nr"]), f3(r["rule_nr"]), f"{s3(r['difference'])} ({s3(r['boot_ci_low'])} to {s3(r['boot_ci_high'])})", f"{r['wins']} / {r['ties']} / {r['losses']}"]
            for n, r in zip(names, sens.iter_rows(named=True))]
    out["AQ3 Table 5. Sensitivity of the model-minus-rule difference (none of these can change the S1 verdict)"] = table(
        ["Variant", "Runs", "Model", "Rule", "Difference (95% interval)", "Wins / ties / losses"], rows)

    mc = csv("aq-3/results/model_choice.csv")
    rows = [[r["config"], f3(r["pooled_normalised_recall"]), s3(r["gain_vs_M1"]) if r["config"] != "M1" else "–", f"{r['folds_with_gain_vs_M1']} of 9" if r["config"] != "M1" else "–",
             "chosen" if r["chosen"] else ""] for r in mc.iter_rows(named=True)]
    out["AQ3 Table 6. Model choice on the 9 development folds of 2013 (day 27, 5 per 20)"] = table(
        ["Configuration", "Pooled normalised recall", "Gain over M1", "Folds with a gain over M1", "Choice"], rows)
    return out


# =====================================================================================================================
# AQ4
# =====================================================================================================================
def aq4_tables() -> dict[str, list[str]]:
    out = {}
    q = csv("aq-4/results/list_quality_pooled.csv")
    rl = {"model": "Model", "rule": "Rule", "random (expected)": "Random (expected)"}
    rows = []
    for (cut, per20), lab in (((27, 5), "Day 27, 5 per 20 (main)"), ((27, 3), "Day 27, 3 per 20"), ((13, 5), "Day 13, 5 per 20"), ((13, 3), "Day 13, 3 per 20")):
        for i, rk in enumerate(("model", "rule", "random (expected)")):
            if rk.startswith("random") and cut == 13:
                continue
            r = q.filter((pl.col("cutoff") == cut) & (pl.col("per20") == per20) & (pl.col("ranking") == rk)).row(0, named=True)
            rows.append([lab if i == 0 else "", f"{r['list_places']:,}" if i == 0 else "", rl[rk], f"{float(r['non_completers_on_list']):,.0f}", pct(r["recall"]), pct(r["attainable_recall"]),
                         rnd(r["normalised_recall"], 3), pct(r["precision"]), rnd(r["lift"], 2)])
    out["AQ4 Table 1. List quality on the 13 test runs of 2014"] = table(
        ["Cut-off and capacity", "List places", "Ranking", "Non-completers listed", "Recall", "Ceiling of recall", "Normalised recall", "Precision", "Lift"], rows)

    t = csv("aq-4/results/tiers.csv").filter(pl.col("ranking") == "model")
    rows = []
    for key, lab in (("tier 1 (top 3 per 20)", "Tier 1 (top 3 per 20)"), ("tier 2 (next 2 per 20)", "Tier 2 (next 2 per 20)"), ("not listed", "Not listed")):
        r = t.filter(pl.col("tier") == key).row(0, named=True)
        rows.append([lab, f"{r['enrolments']:,}", f"{pct(r['non_completion_rate'])} ({r['non_completers']:,})", f"{r['withdrawn']:,}", f"{r['fail']:,}"])
    out["AQ4 Table 2. Non-completion by tier of the model list, day 27"] = table(["Tier", "Enrolments", "Did not complete", "Withdrawn", "Failed"], rows)

    rf = csv("aq-4/results/reason_frequency.csv")
    lab = {"active_days_0c": "Few active days since the start", "tasks_missed_c": "Task due and not submitted", "highest_education": "Lower prior education",
           "tma_late_c": "TMA submitted late", "num_of_prev_attempts": "Previous attempt at the module"}
    rows, rest_n, rest_share = [], 0, 0.0
    for r in rf.iter_rows(named=True):
        if r["first_reason_column"] in lab:
            rows.append([lab[r["first_reason_column"]], f"{r['listed_students']:,}", pct(r["share_of_list"]), pct(r["non_completion_rate"])])
        else:
            rest_n += r["listed_students"]; rest_share += r["share_of_list"]
    rows.append(["Other reasons together", f"{rest_n:,}", pct(rest_share), "–"])
    out["AQ4 Table 3. First reason of the listed students, day 27, 5 per 20"] = table(["First reason", "Listed students", "Share of the list", "Did not complete"], rows)

    f = csv("aq-4/results/fairness_confirmatory.csv").filter(pl.col("ranking") == "model")
    glab = {"Age 55 or over": "Age 55 or over (below 400 enrolments)"}
    rows = []
    for r in f.iter_rows(named=True):
        conf = bool(r["confirmatory"])
        status = ("Flagged" if r["flagged"] else "Not flagged") if conf else "Insufficient data, not cleared"
        rows.append([glab.get(r["group"], r["group"]), f"{r['test_enrolments']:,}", f"{r['group_non_completers']:,}", pct(r["recall_group"]), pct(r["recall_others"]),
                     f"{signed(r['gap'])} points ({ci(r['boot_ci95_low'], r['boot_ci95_high'], sign=True)})", rnd(r["p_holm"], 2) if conf else "–", status])
    out["AQ4 Table 4. Confirmatory check FR1, model list, day 27, 5 per 20 (5,000 two-level bootstrap replicates)"] = table(
        ["Group", "Test enrolments", "Non-completers", "Recall of the group", "Recall of the others", "Gap (95% interval)", "Holm-adjusted p", "Status"], rows)

    d, fc = csv("aq-4/results/fairness_descriptive.csv"), csv("aq-4/results/fairness_calibration.csv")
    pick = [("gender", "F", "Female", "Female"), ("gender", "M", "Male", "Male"), ("disability", "N", "No declared disability", None), ("disability", "Y", "Declared disability", "Declared disability"),
            ("imd_band", "0-10%", "Deprivation band 0–10%", "Deprivation band 0–10%"), ("imd_band", "90-100%", "Deprivation band 90–100%", None),
            ("imd_band", "Missing", "Deprivation band missing", "Deprivation band missing"), ("age_band", "0-35", "Age 0–35", None), ("age_band", "35-55", "Age 35–55", None)]
    rows = []
    for a, g, lab_, calg in pick:
        r = d.filter((pl.col("attribute") == a) & (pl.col("group") == g)).row(0, named=True)
        c = signed(fc.filter(pl.col("group") == calg)["citl"][0], 2, 1.0) if calg else "–"
        rows.append([lab_, pct(r["base_rate"]), pct(r["model_selection_rate"]), pct(r["model_recall"]), pct(r["model_precision"]), c])
    out["AQ4 Table 5. Descriptive checks by group, model list, day 27, 5 per 20"] = table(
        ["Group", "Non-completion rate", "Share listed", "Recall", "Precision", "Calibration-in-the-large"], rows)
    return out


ALL = {"aq-1": aq1_tables, "aq-2": aq2_tables, "aq-3": aq3_tables, "aq-4": aq4_tables}

if __name__ == "__main__":
    n = 0
    for aq, fn in ALL.items():
        print(f"\n## {aq}\n")
        for title, lines in fn().items():
            print(f"**{title}**\n\n" + "\n".join(lines) + "\n")
            n += 1
    print(f"{n} report tables built from the result tables")
    sys.exit(0)
