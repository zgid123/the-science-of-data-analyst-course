"""Consistency checks of the T08 AQ1/AQ2 analysis against the numbers Milestones 3 and 4 already report.

Recounts the 2013 populations from the prepared views (2013 filter pushed to the reader, asserted), compares them
with the published figures of Milestone 3 (fig_outcome_by_run.csv, rule_rates.csv, capacity_by_run.parquet,
validation summary) and Milestone 4 (Table A.6, Table A.7, Section 3.2, Section 4.3), checks the interval and
average-risk-difference code against statsmodels, and scans the results for 2014 rows. Figures that would need a 2014
row are listed as "not checkable" with the reason, never computed.

Usage (from the repository root): venv/bin/python reports/milestone-5/code/aq_checks.py
Prints one line per check; exits 1 if any check fails.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import polars as pl
import statsmodels.api as sm
from statsmodels.stats.proportion import confint_proportions_2indep, proportion_confint

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aq_analysis as A  # noqa: E402  (same folder; reuses the 2013-only loaders and interval functions)

RESULTS: list[tuple[str, str, str, str]] = []


def check(name: str, expected, observed, note: str = "", tol: float = 0.0) -> None:
    if isinstance(expected, (int, float)) and isinstance(observed, (int, float)):
        ok = abs(expected - observed) <= tol
    else:
        ok = expected == observed
    RESULTS.append(("PASS" if ok else "FAIL", name, f"expected {expected}, observed {observed}", note))


def info(name: str, text: str) -> None:
    RESULTS.append(("INFO", name, text, ""))


def main() -> int:
    enr = A.load_view("enrolment")
    f13 = A.load_view("features_d13")
    f27 = A.load_view("features_d27")
    cap = A.load_view("capacity_by_run")
    res = json.loads((A.RES / "aq_results.json").read_text())

    # ---- 2013 enrolment counts per run and overall against Milestone 3 fig_outcome_by_run.csv -------------------
    pub = pl.read_csv(A.META / "fig_outcome_by_run.csv").filter(pl.col("code_presentation").str.starts_with("2013"))
    own = enr.group_by("code_module", "code_presentation", "final_result").len().pivot(
        on="final_result", index=["code_module", "code_presentation"], values="len")
    j = pub.join(own, on=["code_module", "code_presentation"], suffix="_own")
    for x in j.sort("code_module", "code_presentation").iter_rows(named=True):
        exp = tuple(x[o] for o in A.OUTCOMES)
        obs = tuple(x[f"{o}_own"] for o in A.OUTCOMES)
        check(f"M3 fig_outcome_by_run {x['code_module']} {x['code_presentation']} (Pass, Distinction, Fail, Withdrawn)",
              exp, obs)
    check("2013 enrolments, all runs (sum of M3 published 2013 counts)", int(pub.select(pl.sum_horizontal(A.OUTCOMES)).sum().item()),
          enr.height)
    check("2013 non-completers, all enrolments (M3 published Fail + Withdrawn)",
          int(pub["Fail"].sum() + pub["Withdrawn"].sum()), int(enr["non_completion"].sum()))
    check("AQ1 all-enrolment population in aq_results.json", enr.height, res["aq1"]["all_enrolments"]["n"])
    check("AQ1 day-14 population in aq_results.json", int(enr["enrolled_d14"].sum()), res["aq1"]["day14_registered"]["n"])

    # ---- run sizes at the cut-offs against rule_rates.csv and capacity_by_run --------------------------------------
    rr = pl.read_csv(A.META / "rule_rates.csv").filter(pl.col("split") == "train")
    for c, f in [(13, f13), (27, f27)]:
        own_n = f.group_by("code_module", "code_presentation").agg(
            pl.len().alias("n"), pl.col("rule_missed").mean().alias("rule_missed"),
            pl.col("rule_tma_late").mean().alias("rule_tma_late"),
            pl.col("inactive_last7").mean().alias("inactive_last7"),
            pl.col("early_sign_rule").mean().alias("early_sign_rule"))
        jj = rr.filter(pl.col("cutoff_day") == c).join(own_n, on=["code_module", "code_presentation"], suffix="_own")
        jj = jj.join(cap.filter(pl.col("cutoff_day") == c).select("code_module", "code_presentation",
                                                                   pl.col("enrolled").alias("cap_n")),
                     on=["code_module", "code_presentation"])
        for x in jj.sort("code_module", "code_presentation").iter_rows(named=True):
            check(f"day {c} run size {x['code_module']} {x['code_presentation']} (rule_rates.csv, capacity_by_run)",
                  (x["enrolled"], x["cap_n"]), (x["n"], x["n"]))
            obs = tuple(round(x[k + "_own"], 4) for k in ["early_sign_rule", "rule_missed", "rule_tma_late",
                                                          "inactive_last7"])
            exp = tuple(round(x[k], 4) for k in ["early_sign_rule", "rule_missed", "rule_tma_late", "inactive_last7"])
            check(f"day {c} rule shares {x['code_module']} {x['code_presentation']} (rule, missed, TMA late, inactive)",
                  exp, obs)
        check(f"day {c} 2013 run sizes against enrolment.enrolled_d{c}",
              int(enr[f"enrolled_d{c}"].sum()), f.height)

    # ---- Milestone 4 Table A.6 ---------------------------------------------------------------------------------------
    check("M4 Table A.6: training enrolments day 13", 12080, f13.height)
    check("M4 Table A.6: training non-completers day 13", 5519, int(f13["non_completion"].sum()))
    check("M4 Table A.6: training non-completion day 13 (45.7%)", 45.7, round(100 * f13["non_completion"].mean(), 1))
    check("M4 Table A.6: training enrolments day 27", 11811, f27.height)
    check("M4 Table A.6: training non-completers day 27", 5245, int(f27["non_completion"].sum()))
    check("M4 Table A.6 and Section 4.3: training non-completion day 27 (44.4%)", 44.4,
          round(100 * f27["non_completion"].mean(), 1))
    check("AQ2 population in aq_results.json (11,811 / 5,245)", (11811, 5245),
          (res["aq2"]["population"]["n"], res["aq2"]["population"]["non_completers"]))
    for c, f, exp in [(13, f13, (370, 92)), (27, f27, (369, 91))]:
        g = f.group_by("code_module", "code_presentation").agg(pl.len().alias("n"),
                                                               pl.col("non_completion").sum().alias("nc")).sort("n")
        check(f"M4 Section 3.2 / Table A.6: smallest training run day {c} (enrolments, non-completers)", exp,
              (g["n"][0], g["nc"][0]), note=f"run {g['code_module'][0]} {g['code_presentation'][0]}")
        k = cap.filter(pl.col("cutoff_day") == c).select("code_module", "code_presentation", "list_tutor_5")
        kk = g.join(k, on=["code_module", "code_presentation"]).with_columns(
            pl.min_horizontal("list_tutor_5", "nc").alias("attain"))
        check(f"M4 Table A.6: most non-completers a 5-per-20 list can hold, day {c}", 3032 if c == 13 else 2976,
              int(kk["attain"].sum()))
        if c == 27:
            share = (kk["attain"] / kk["nc"])
            check("M4 Section 4.3 (C13): a 5-per-20 list at day 27 holds 46% to 100% of a run's non-completers",
                  (46, 100), (round(100 * share.min()), round(100 * share.max())))
    lo13, lo27 = 100 * f27["non_completion"].mean(), 100 * f13["non_completion"].mean()
    check("M4 Section 3.2: '44-46% of students do not complete' (training runs, day 27 and day 13)", True,
          44 <= min(lo13, lo27) and max(lo13, lo27) <= 46, note=f"{lo13:.1f}% at day 27, {lo27:.1f}% at day 13")

    # ---- Milestone 4 Table A.7 (day 27, training) --------------------------------------------------------------------
    def grp(expr):
        d = f27.filter(expr)
        return (d.height, int(d["non_completion"].sum()))
    check("M4 Table A.7: female", (5697, 2488), grp(pl.col("gender") == "F"))
    check("M4 Table A.7: male", (6114, 2757), grp(pl.col("gender") == "M"))
    check("M4 Table A.7: declared disability", (1123, 602), grp(pl.col("disability") == "Y"))
    check("M4 Table A.7: deprivation band 0-10%", (1163, 699), grp(pl.col("imd_band") == "0-10%"))
    check("M4 Table A.7: deprivation band missing", (418, 118), grp(pl.col("imd_band") == "Missing"))
    check("M4 Table A.7: age 55 or over", (75, 18), grp(pl.col("age_band") == "55<="))

    # ---- AQ1 headline: day-14 rate against the day-13 figure ---------------------------------------------------------
    d14 = res["aq1"]["day14_registered"]
    info("AQ1 day-14 non-completion against the M4 day-13 figure",
         f"day 14: {d14['non_completers']}/{d14['n']} = {100 * d14['non_completion'][0]:.2f}%; day 13 (Table A.6): "
         f"5,519/12,080 = 45.69%. Both round to 45.7%; the populations differ by a net 4 enrolments and 4 non-completers "
         f"because 'enrolled at day d' changes between day 13 and day 14 (late registrations, unregistrations on day 14).")
    fl = enr.filter(pl.col("withdrawal_day_missing") | pl.col("registration_missing"))
    info("Flagged enrolments (M3: 138 over 22 runs = 93 without a withdrawal day + 45 without a registration day)",
         f"2013 share: {fl.height} ({int(enr['withdrawal_day_missing'].sum())} without a withdrawal day, "
         f"{int(enr['registration_missing'].sum())} without a registration day); "
         f"{int(fl['enrolled_d14'].sum())} of them in the day-14 population, "
         f"{f27.filter(pl.col('eval_withdrawal_day_unknown') | pl.col('registration_missing')).height} at day 27. "
         f"Consistent with M3 DQ04 (87 of the 93 in October 2014 runs). The remaining 117 lie in 2014 runs and are not read.")
    info("Not checkable on 2013 alone (needs 2014 rows)",
         "32,593 enrolments and 28,061 in the day-14 population over 22 runs (AQ1 card), 54.7% completion in the "
         "day-14 population over 22 runs (M3 validation), 28.8% rule rate over 27,535 enrolments at day 27 (M4 "
         "Section 4.1). Partial check: 2013 holds 13,529 enrolments (12,076 at day 14); the published 2014 outcome "
         "counts add 19,064 enrolments, total 32,593 (next check).")
    pub_all = pl.read_csv(A.META / "fig_outcome_by_run.csv")
    check("M3 fig_outcome_by_run total over 22 runs equals the AQ1 card's 32,593", 32593,
          int(pub_all.select(pl.sum_horizontal(A.OUTCOMES)).sum().item()))

    # ---- interval and estimator code against statsmodels ------------------------------------------------------------
    for x, n in [(5515, 12076), (92, 370), (19, 76)]:
        p, lo, hi = A.wilson(x, n)
        slo, shi = proportion_confint(x, n, alpha=0.05, method="wilson")
        check(f"Wilson interval {x}/{n} against statsmodels", (round(slo, 10), round(shi, 10)),
              (round(lo, 10), round(hi, 10)))
    for a, n1, c, n0 in [(1156, 1285, 3489, 8675), (367, 577, 4229, 9383)]:
        d, lo, hi = A.newcombe(a, n1, c, n0)
        slo, shi = confint_proportions_2indep(a, n1, c, n0, method="newcomb", compare="diff")
        check(f"Newcombe interval {a}/{n1} - {c}/{n0} against statsmodels", (round(slo, 8), round(shi, 8)),
              (round(lo, 8), round(hi, 8)))
    f = A.build_signs(f27)
    m = A.Fit(f, list(A.SIGNS), interactions=False)  # common-effect model: get_margeff averages over all rows
    me = m.res.get_margeff(at="overall", method="dydx", dummy=True)
    for s in ["inactive_last7", "low_relative_activity", "no_pre_start_activity"]:  # defined on all rows
        j_ = m.idx[s] - 1  # get_margeff drops the constant
        est, lo, hi, se = m.ame(s, np.arange(f.height))
        check(f"Average risk difference of {s} (model without sign x module terms) against statsmodels get_margeff",
              (round(float(me.margeff[j_]), 8), round(float(me.margeff_se[j_]), 6)), (round(est, 8), round(se, 6)))

    # ---- no 2014 row in any result ----------------------------------------------------------------------------------
    for p in sorted(A.RES.glob("aq*_*.csv")):
        txt = p.read_text()
        check(f"no 2014 run in {p.name}", False, "2014B" in txt or "2014J" in txt)
    yc = pl.read_csv(A.COMPARE / "aq1_year_comparison_published.csv")
    check("2014 rows of aq1_year_comparison_published.csv all labelled as published in Milestone 3", True,
          bool(yc.filter(pl.col("year") == 2014)["source"].str.starts_with("published in Milestone 3").all()))

    width = max(len(r[1]) for r in RESULTS)
    for st, name, txt, note in RESULTS:
        print(f"{st:4}  {name:<{width}}  {txt}" + (f"  [{note}]" if note else ""))
    nfail = sum(r[0] == "FAIL" for r in RESULTS)
    npass = sum(r[0] == "PASS" for r in RESULTS)
    print(f"SUMMARY: {npass} PASS, {nfail} FAIL, {sum(r[0] == 'INFO' for r in RESULTS)} INFO")
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
