"""AQ1 (descriptive) and AQ2 (diagnostic) on the module runs of one scope, following the Milestone 4 plan.

Scopes (`--scope`): `2013` (default; the 9 runs of 2013, results/2013/), `2014` (the 13 runs of 2014, results/2014/) and
`all` (all 22 runs, results/all_runs/). The 2013 scope is the analysis as first run; its text below applies to it.
The 2014 and all-run scopes repeat every AQ1 and AQ2 step on their runs (AQ1 for 2014 and the 22-run baselines;
AQ2 replicated on 2014 as Change Log C14 plans; Change Log C15), with the same assertion that no row outside the
scope enters.

Plan items (Milestone 4 report): Section 3.2 (methods), Section 4.1 Tables 4.1 and 4.2 (Evaluation Design Cards of
AQ1 and AQ2), Section 4.3, Section 4.4 and Appendices II-IV. In the 2013 scope AQ2 is estimated on the 2013 runs
(Change Log C14) and no 2014 row of any prepared view is read. The only 2014
information used is the per-run outcome counts that Milestone 3 published in
`data/metadata/fig_outcome_by_run.csv` (AQ1 year comparison, labelled "published in Milestone 3").

Every view is scanned lazily with a 2013 filter pushed down to the Parquet/CSV reader, and `assert_2013` is called on
every frame before any column is used, so no 2014 row enters any computation.

Usage (from the package folder): python src/analysis/aq_analysis.py [--scope 2013|2014|all]  (run_all.sh steps 08, 12, 13)
Writes the results folder of the scope (results/2013/, results/2014/ or results/all_runs/): aq1_*.csv, aq2_*.csv,
aq_results.json and aq_summary.md; the 2013 scope also writes results/compare/aq1_year_*_published.csv.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import polars as pl
import statsmodels.api as sm

HERE = Path(__file__).resolve().parent              # src/analysis
ROOT = HERE.parents[1]                               # the package folder
DATA = ROOT / "data"                                 # prepared data built by the Milestone 3 pipeline (src/)
PROC, META = DATA / "processed", DATA / "metadata"
RAW = DATA / "raw"
RES = ROOT / "results" / "2013"                      # results of the selected scope (set_scope)
COMPARE = ROOT / "results" / "compare"               # comparisons between the years

Z = 1.959963984540054                                # 97.5% quantile of the standard normal
RUNS_2013 = {"2013B", "2013J"}
SCOPES = {
    "2013": dict(name="2013", presentations={"2013B", "2013J"}, years={2013}, splits={"train"},
                 label="all 9 runs of 2013", runs_text="runs of 2013", out="2013"),
    "2014": dict(name="2014", presentations={"2014B", "2014J"}, years={2014}, splits={"test"},
                 label="all 13 runs of 2014", runs_text="runs of 2014", out="2014"),
    "all": dict(name="all", presentations={"2013B", "2013J", "2014B", "2014J"}, years={2013, 2014},
                splits={"train", "test"}, label="all 22 runs", runs_text="runs of 2013 and 2014", out="all_runs"),
}
SC = SCOPES["2013"]


def set_scope(name: str) -> None:
    """Select the runs every loader keeps and the folder every result is written to."""
    global SC, RES
    SC = SCOPES[name]
    RES = ROOT / "results" / SC["out"]
OUTCOMES = ["Pass", "Distinction", "Fail", "Withdrawn"]
MIN_EVENTS_SUBGROUP_MODEL = 100                      # Section 4.4: about 100 non-completers per group


# ---------------------------------------------------------------------------------------------------------------
# 2013-only loading
# ---------------------------------------------------------------------------------------------------------------
def assert_2013(df: pl.DataFrame, label: str) -> pl.DataFrame:
    """Stop if any row of a frame belongs to a 2014 run."""
    pres = set(df["code_presentation"].unique().to_list())
    assert pres <= RUNS_2013, f"{label}: non-2013 presentations {pres - RUNS_2013}"
    if "year" in df.columns:
        assert (df["year"] == 2013).all(), f"{label}: year != 2013"
    if "split" in df.columns:
        assert (df["split"] == "train").all(), f"{label}: split != train"
    return df


def assert_scope(df: pl.DataFrame, label: str) -> pl.DataFrame:
    """Stop if any row of a frame lies outside the runs of the selected scope."""
    pres = set(df["code_presentation"].unique().to_list())
    assert pres <= SC["presentations"], f"{label}: presentations {pres - SC['presentations']} outside scope {SC['name']}"
    if "year" in df.columns:
        assert df["year"].is_in(list(SC["years"])).all(), f"{label}: year outside scope {SC['name']}"
    if "split" in df.columns:
        assert df["split"].is_in(list(SC["splits"])).all(), f"{label}: split outside scope {SC['name']}"
    return df


def load_view(name: str) -> pl.DataFrame:
    """Scan a prepared view with the scope filter pushed down to the reader, then assert it."""
    lf = pl.scan_parquet(PROC / f"{name}.parquet")
    lf = lf.filter(pl.col("code_presentation").is_in(sorted(SC["presentations"])))
    return assert_scope(lf.collect(), name)


def load_raw(name: str) -> pl.DataFrame:
    """Scan a raw OULAD table with the scope filter pushed down to the CSV reader (second aggregation path)."""
    lf = pl.scan_csv(RAW / f"{name}.csv", null_values=["", "?"], infer_schema_length=0)
    lf = lf.filter(pl.col("code_presentation").is_in(sorted(SC["presentations"])))
    return assert_scope(lf.collect(), f"raw {name}")


# ---------------------------------------------------------------------------------------------------------------
# Intervals
# ---------------------------------------------------------------------------------------------------------------
def wilson(x: int, n: int) -> tuple[float, float, float]:
    """Proportion with its 95% Wilson score interval."""
    if n == 0:
        return (math.nan, math.nan, math.nan)
    p = x / n
    den = 1 + Z * Z / n
    mid = (p + Z * Z / (2 * n)) / den
    half = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return p, mid - half, mid + half


def newcombe(x1: int, n1: int, x2: int, n2: int) -> tuple[float, float, float]:
    """Difference p1 - p2 with the 95% Newcombe hybrid score interval (method 10, Wilson limits)."""
    p1, l1, u1 = wilson(x1, n1)
    p2, l2, u2 = wilson(x2, n2)
    d = p1 - p2
    return d, d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2), d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)


def woolf_or(a: int, b: int, c: int, d: int) -> tuple[float, float, float]:
    """Odds ratio a*d/(b*c) of a 2x2 table (a = sign & event) with its 95% Woolf interval."""
    if min(a, b, c, d) == 0:
        return (math.nan, math.nan, math.nan)
    lor = math.log(a * d / (b * c))
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return math.exp(lor), math.exp(lor - Z * se), math.exp(lor + Z * se)


def r(v, k=4):
    # + 0.0 turns a rounded -0.0 (floating-point noise around zero) into 0.0, so reruns give identical files
    return None if v is None or (isinstance(v, float) and math.isnan(v)) else round(float(v), k) + 0.0


# ---------------------------------------------------------------------------------------------------------------
# AQ1
# ---------------------------------------------------------------------------------------------------------------
def rate_rows(df: pl.DataFrame, level: str, keys: list[str], denominator: str) -> list[dict]:
    """Completion, non-completion and the four outcome shares per group, each with Wilson interval."""
    rows = []
    groups = df.group_by(keys, maintain_order=False).agg(
        pl.len().alias("n"),
        pl.col("completed").sum().alias("completion"),
        pl.col("non_completion").sum().alias("non_completion"),
        *[(pl.col("final_result") == o).sum().alias(o) for o in OUTCOMES],
    ).sort(keys) if keys else df.select(
        pl.len().alias("n"),
        pl.col("completed").sum().alias("completion"),
        pl.col("non_completion").sum().alias("non_completion"),
        *[(pl.col("final_result") == o).sum().alias(o) for o in OUTCOMES],
    )
    for g in groups.iter_rows(named=True):
        label = " ".join(str(g[k]) for k in keys) if keys else SC["label"]
        for m in ["completion", "non_completion", *OUTCOMES]:
            p, lo, hi = wilson(g[m], g["n"])
            rows.append(dict(level=level, group=label, denominator=denominator, measure=m, events=g[m],
                             n=g["n"], rate=r(p), ci_low=r(lo), ci_high=r(hi)))
    return rows


def aq1(enr: pl.DataFrame, f27: pl.DataFrame, out: dict) -> None:
    enr = enr.with_columns(
        pl.col("start_month").replace({"B": "B (February)", "J": "J (October)"}),
        pl.col("code_presentation").str.slice(4, 1).alias("start_month_code"),
        (pl.col("code_module") + " " + pl.col("code_presentation")).alias("run"),
        (pl.col("withdrawal_day_missing") | pl.col("registration_missing")).alias("flagged"),
    )
    pops = {
        "day14_registered": enr.filter(pl.col("enrolled_d14")),
        "all_enrolments": enr,
        "day14_registered_excl_flagged": enr.filter(pl.col("enrolled_d14") & ~pl.col("flagged")),
    }
    # --- primary metric: rates per level and denominator ----------------------------------------------------
    rows = []
    for den, d in pops.items():
        rows += rate_rows(d, "overall", [], den)
        rows += rate_rows(d, "module", ["code_module"], den)
        rows += rate_rows(d, "run", ["code_module", "code_presentation"], den)
        rows += rate_rows(d, "start_month", ["start_month"], den)
    rates = pl.DataFrame(rows)
    rates.write_csv(RES / "aq1_rates.csv")

    # --- error analysis: runs whose rate moves by more than its interval between the two denominators --------
    shift = []
    for lvl in ["overall", "module", "run", "start_month"]:
        a = rates.filter((pl.col("level") == lvl) & (pl.col("denominator") == "day14_registered"))
        b = rates.filter((pl.col("level") == lvl) & (pl.col("denominator") == "all_enrolments"))
        j = a.join(b, on=["level", "group", "measure"], suffix="_all")
        for x in j.iter_rows(named=True):
            moved = not (x["ci_low"] <= x["rate_all"] <= x["ci_high"])
            shift.append(dict(level=lvl, group=x["group"], measure=x["measure"],
                              n_day14=x["n"], rate_day14=x["rate"], ci_low_day14=x["ci_low"],
                              ci_high_day14=x["ci_high"], n_all=x["n_all"], rate_all=x["rate_all"],
                              shift_pp=r(100 * (x["rate_all"] - x["rate"]), 2),
                              outside_day14_interval=moved))
    shift = pl.DataFrame(shift)
    shift.write_csv(RES / "aq1_denominator_shift.csv")

    ydiff = []
    if SC["name"] == "2013":  # 2013 scope only; the computed comparison of both years is aq_year_compare.py
        # --- year comparison: 2013 computed against 2014 published in Milestone 3 (all enrolments only) ----------
        pub = pl.read_csv(META / "fig_outcome_by_run.csv").with_columns(
            pl.col("code_presentation").str.slice(0, 4).alias("year"),
            pl.col("code_presentation").str.slice(4, 1).alias("start_month_code"),
        )
        pub = pub.with_columns(
            pl.sum_horizontal(OUTCOMES).alias("n"),
            (pl.col("Pass") + pl.col("Distinction")).alias("completion"),
            (pl.col("Fail") + pl.col("Withdrawn")).alias("non_completion"),
        )
        yr = []
        for lvl, keys in [("year", ["year"]), ("module_year", ["code_module", "year"]),
                          ("start_month_year", ["start_month_code", "year"])]:
            g = pub.group_by(keys).agg(pl.col(["n", "completion", "non_completion", *OUTCOMES]).sum()).sort(keys)
            for x in g.iter_rows(named=True):
                src = ("computed from 2013 rows; equals the Milestone 3 published counts (logs/11_aq_checks.log)"
                       if x["year"] == "2013" else "published in Milestone 3 (fig_outcome_by_run.csv); not recomputed")
                for m in ["completion", "non_completion", *OUTCOMES]:
                    p, lo, hi = wilson(x[m], x["n"])
                    yr.append(dict(level=lvl, group=" ".join(str(x[k]) for k in keys), year=x["year"],
                                   denominator="all_enrolments", measure=m, events=x[m], n=x["n"], rate=r(p),
                                   ci_low=r(lo), ci_high=r(hi), source=src))
        year_tab = pl.DataFrame(yr)
        # 2013 rows must equal the 2013 computation exactly
        own = rates.filter((pl.col("denominator") == "all_enrolments") & (pl.col("level") == "overall"))
        pub13 = year_tab.filter((pl.col("level") == "year") & (pl.col("year") == "2013"))
        for m in ["completion", "non_completion", *OUTCOMES]:
            a = own.filter(pl.col("measure") == m)["events"][0]
            b = pub13.filter(pl.col("measure") == m)["events"][0]
            assert a == b, f"2013 {m}: computed {a} != published {b}"
        # difference 2014 - 2013 in non-completion (all enrolments), Newcombe interval
        ydiff = []
        for lvl in ["year", "module_year", "start_month_year"]:
            t = year_tab.filter((pl.col("level") == lvl) & (pl.col("measure") == "non_completion"))
            t = t.with_columns(pl.col("group").str.replace(r" ?20\d\d$", "").alias("unit"))
            for unit in t["unit"].unique().sort().to_list():
                s = t.filter(pl.col("unit") == unit)
                if s.height != 2:
                    continue  # module CCC: 2014 only
                a = s.filter(pl.col("year") == "2013").row(0, named=True)
                b = s.filter(pl.col("year") == "2014").row(0, named=True)
                d, lo, hi = newcombe(b["events"], b["n"], a["events"], a["n"])
                ydiff.append(dict(level=lvl, unit=unit or "all runs", measure="non_completion",
                                  rate_2013=a["rate"], n_2013=a["n"], rate_2014_published=b["rate"], n_2014=b["n"],
                                  diff_pp_2014_minus_2013=r(100 * d, 2), ci_low_pp=r(100 * lo, 2),
                                  ci_high_pp=r(100 * hi, 2)))
        COMPARE.mkdir(parents=True, exist_ok=True)
        year_tab.write_csv(COMPARE / "aq1_year_comparison_published.csv")
        pl.DataFrame(ydiff).write_csv(COMPARE / "aq1_year_difference_published.csv")

    # --- secondary metric: cumulative share with a first missed task by week, by outcome ----------------------
    cum = []
    max_week = int(enr["first_missed_week"].max())
    for den in ["day14_registered", "all_enrolments"]:
        d = pops[den].with_columns(
            pl.when(pl.col("completed")).then(pl.lit("Completed")).otherwise(pl.lit("Not completed"))
            .alias("completion_group"))
        for gcol in ["final_result", "completion_group"]:
            for gval in sorted(d[gcol].unique().to_list()):
                s = d.filter(pl.col(gcol) == gval)
                for w in range(1, max_week + 1):
                    x = int((s["first_missed_week"] <= w).sum())
                    p, lo, hi = wilson(x, s.height)
                    cum.append(dict(denominator=den, group=gval, week=w, events=x, n=s.height,
                                    cum_share=r(p), ci_low=r(lo), ci_high=r(hi)))
    pl.DataFrame(cum).write_csv(RES / "aq1_first_missed_week_cumulative.csv")

    fm = []
    for den in ["day14_registered", "all_enrolments"]:
        d = pops[den]
        for gval in ["all", *OUTCOMES, "Completed", "Not completed"]:
            if gval == "all":
                s = d
            elif gval == "Completed":
                s = d.filter(pl.col("completed"))
            elif gval == "Not completed":
                s = d.filter(pl.col("non_completion"))
            else:
                s = d.filter(pl.col("final_result") == gval)
            miss = s["first_missed_week"].drop_nulls()
            p_any, lo_any, hi_any = wilson(miss.len(), s.height)
            p4, lo4, hi4 = wilson(int((s["first_missed_week"] <= 4).sum()), s.height)
            fm.append(dict(denominator=den, group=gval, n=s.height, with_missed_task=miss.len(),
                           share_any=r(p_any), ci_low_any=r(lo_any), ci_high_any=r(hi_any),
                           share_by_week4=r(p4), ci_low_week4=r(lo4), ci_high_week4=r(hi4),
                           week_q1=r(miss.quantile(0.25, "lower"), 1) if miss.len() else None,
                           week_median=r(miss.quantile(0.5, "lower"), 1) if miss.len() else None,
                           week_q3=r(miss.quantile(0.75, "lower"), 1) if miss.len() else None))
    fm = pl.DataFrame(fm)
    fm.write_csv(RES / "aq1_first_missed_week_summary.csv")

    # --- error analysis: runs with no task due by day 27 -------------------------------------------------------
    due = f27.group_by("code_module", "code_presentation").agg(
        pl.len().alias("enrolled_d27"), pl.col("tasks_due_c").max().alias("max_tasks_due_by_d27"))
    first_due = load_view("assessment_due").group_by("code_module", "code_presentation").agg(
        pl.col("due_day").min().alias("first_task_due_day"))
    kpi = pops["day14_registered"].group_by("code_module", "code_presentation").agg(
        pl.len().alias("n_day14"),
        pl.col("first_missed_week").drop_nulls().len().alias("with_missed_task"),
        pl.col("first_missed_week").min().alias("earliest_first_missed_week"),
        pl.col("first_missed_week").median().alias("median_first_missed_week"),
        (pl.col("first_missed_week") <= 4).sum().alias("missed_by_week4"),
    )
    nt = due.join(first_due, on=["code_module", "code_presentation"]).join(
        kpi, on=["code_module", "code_presentation"]).with_columns(
        (pl.col("max_tasks_due_by_d27") == 0).alias("no_task_due_by_d27")).sort("code_module", "code_presentation")
    nt.write_csv(RES / "aq1_runs_task_due.csv")

    # --- subgroup description (gender, disability, deprivation band, age band) --------------------------------
    sub = []
    for den in ["day14_registered", "all_enrolments"]:
        for col in ["gender", "disability", "imd_band", "age_band"]:
            for x in rate_rows(pops[den], col, [col], den):
                if x["measure"] in ("completion", "non_completion"):
                    sub.append(x)
    pl.DataFrame(sub).write_csv(RES / "aq1_subgroup_rates.csv")

    # --- validation: two independent aggregation paths (prepared view and raw tables) -------------------------
    info = load_raw("studentInfo")
    reg = load_raw("studentRegistration").with_columns(
        pl.col("date_registration").cast(pl.Int64), pl.col("date_unregistration").cast(pl.Int64))
    raw = info.join(reg, on=["code_module", "code_presentation", "id_student"], how="left")
    assert raw.height == info.height
    raw = raw.with_columns(
        ((pl.col("date_registration").is_null() | (pl.col("date_registration") <= 14))
         & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > 14))).alias("d14"))
    val = []
    for den, rawd, prepd in [("all_enrolments", raw, pops["all_enrolments"]),
                             ("day14_registered", raw.filter(pl.col("d14")), pops["day14_registered"])]:
        a = rawd.group_by("code_module", "code_presentation", "final_result").len("raw")
        b = prepd.group_by("code_module", "code_presentation", "final_result").len("prepared")
        j = a.join(b, on=["code_module", "code_presentation", "final_result"], how="full", coalesce=True)
        j = j.fill_null(0).with_columns(pl.lit(den).alias("denominator"),
                                        (pl.col("raw") == pl.col("prepared")).alias("agree"))
        val.append(j.sort("code_module", "code_presentation", "final_result"))
    # first missed week: enrolment view against a recount from assessment_due
    ad = load_view("assessment_due")
    recount = ad.filter((pl.col("status") == "not_submitted") & pl.col("due_while_enrolled")).group_by(
        "code_module", "code_presentation", "id_student").agg(pl.col("due_week").min().alias("recount"))
    fmw = enr.select("code_module", "code_presentation", "id_student", "first_missed_week").join(
        recount, on=["code_module", "code_presentation", "id_student"], how="left")
    fmw_agree = int(((fmw["first_missed_week"] == fmw["recount"]) | (
        fmw["first_missed_week"].is_null() & fmw["recount"].is_null())).sum())
    valid = pl.concat(val)
    valid.write_csv(RES / "aq1_validation_two_paths.csv")
    assert valid["agree"].all(), "AQ1: the two aggregation paths disagree"
    assert fmw_agree == enr.height, "AQ1: first_missed_week does not match its recount"

    # --- key numbers -------------------------------------------------------------------------------------------
    def pick(lvl, den, m, grp=None):
        t = rates.filter((pl.col("level") == lvl) & (pl.col("denominator") == den) & (pl.col("measure") == m))
        if grp is not None:
            t = t.filter(pl.col("group") == grp)
        return t

    o = {}
    for den in pops:
        ov = pick("overall", den, "non_completion").row(0, named=True)
        oc = pick("overall", den, "completion").row(0, named=True)
        mods = pick("module", den, "non_completion").sort("rate")
        runs = pick("run", den, "non_completion").sort("rate")
        o[den] = dict(
            n=ov["n"], non_completers=ov["events"], non_completion=[ov["rate"], ov["ci_low"], ov["ci_high"]],
            completion=[oc["rate"], oc["ci_low"], oc["ci_high"]],
            module_low=mods.row(0, named=True), module_high=mods.row(-1, named=True),
            run_low=runs.row(0, named=True), run_high=runs.row(-1, named=True),
            shares={m: pick("overall", den, m).select("rate", "ci_low", "ci_high").row(0) for m in OUTCOMES})
    if ydiff:
        o["year_difference"] = ydiff[[x["level"] for x in ydiff].index("year")]
    o["runs_outside_interval_between_denominators"] = shift.filter(
        (pl.col("level") == "run") & (pl.col("measure") == "non_completion") & pl.col("outside_day14_interval")
    )["group"].to_list()
    o["first_missed_week"] = fm.filter(pl.col("denominator") == "day14_registered").to_dicts()
    o["runs_no_task_due_by_d27"] = nt.filter(pl.col("no_task_due_by_d27")).select(
        pl.col("code_module") + " " + pl.col("code_presentation")).to_series().to_list()
    o["validation"] = dict(cells=valid.height, all_agree=bool(valid["agree"].all()),
                           first_missed_week_agree=f"{fmw_agree}/{enr.height}")
    out["aq1"] = o


# ---------------------------------------------------------------------------------------------------------------
# AQ2
# ---------------------------------------------------------------------------------------------------------------
SIGNS = {
    "missed_task": "a task (TMA or CMA) due by day 27 not submitted by day 27",
    "late_tma": "a TMA due by day 27 submitted late by day 27",
    "inactive_last7": "no click on days 21-27",
    "low_relative_activity": "clicks on days 0-27 below the run median",
    "no_pre_start_activity": "no click before day 0",
}
TASK_SIGNS = {"missed_task", "late_tma"}


def build_signs(f: pl.DataFrame, variant: str = "primary") -> pl.DataFrame:
    """Binary signs at day 27; variants are the sensitivity runs of the AQ2 card."""
    f = f.with_columns(
        (pl.col("code_module") + " " + pl.col("code_presentation")).alias("run"),
        pl.col("tasks_due_c").max().over("code_module", "code_presentation").alias("run_tasks_due"),
    )
    if variant == "dedup_clicks":
        med = pl.col("clicks_0c_dedup").median().over("code_module", "code_presentation")
        ratio = (pl.col("clicks_0c_dedup") + 1) / (med + 1)
    else:
        ratio = pl.col("activity_ratio_run")
    thr = 0.5 if variant == "below_half_median" else 1.0
    late = (pl.col("tasks_late_c") >= 1) if variant == "late_tma_or_cma" else (pl.col("tma_late_c") >= 1)
    return f.with_columns(
        (pl.col("tasks_missed_c") >= 1).cast(pl.Int8).alias("missed_task"),
        late.cast(pl.Int8).alias("late_tma"),
        pl.col("inactive_last7").cast(pl.Int8).alias("inactive_last7"),
        (ratio < thr).cast(pl.Int8).alias("low_relative_activity"),
        (pl.col("clicks_pre") == 0).cast(pl.Int8).alias("no_pre_start_activity"),
        pl.col("non_completion").cast(pl.Int8).alias("y"),
        (pl.col("run_tasks_due") >= 1).alias("task_run"),
    )


def defined_mask(f: pl.DataFrame, s: str) -> np.ndarray:
    return f["task_run"].to_numpy() if s in TASK_SIGNS else np.ones(f.height, bool)


class Fit:
    """Logistic regression of non-completion with run fixed effects, background adjustment, signs and
    sign x module terms coded as deviations from the average module (Appendix III). Robust (HC1) covariance,
    no clustering (Section 3.2)."""

    def __init__(self, f: pl.DataFrame, signs: list[str], interactions: bool = True):
        self.f, self.signs, self.interactions = f, signs, interactions
        runs = sorted(f["run"].unique().to_list())
        cols, names = [np.ones(f.height)], ["const"]
        for rn in runs[1:]:
            cols.append((f["run"] == rn).to_numpy().astype(float))
            names.append(f"run[{rn}]")
        cols.append(f["num_of_prev_attempts"].to_numpy().astype(float))
        names.append("num_of_prev_attempts")
        cols.append(f["studied_credits"].to_numpy().astype(float) / 30.0)
        names.append("studied_credits_per30")
        self.mods: dict[str, list[str]] = {}
        mod = f["code_module"].to_numpy()
        for s in signs:
            sv = f[s].to_numpy().astype(float)
            cols.append(sv)
            names.append(s)
            dm = defined_mask(f, s)
            # modules where the sign is defined and varies; a module where it never occurs (in 2014, no CCC
            # enrolment has a late TMA by day 27) gets no module term, so its rows take the average-module effect
            ms = sorted(m for m in set(mod[dm]) if len(set(sv[dm & (mod == m)])) > 1)
            self.mods[s] = ms
            if interactions and len(ms) > 1:
                ref = ms[-1]
                for m in ms[:-1]:
                    z = (mod == m).astype(float) - (mod == ref).astype(float)
                    cols.append(sv * z)
                    names.append(f"{s}:dev[{m}]")
        self.X = np.column_stack(cols)
        self.names = names
        self.idx = {n: i for i, n in enumerate(names)}
        self.y = f["y"].to_numpy().astype(float)
        res = sm.Logit(self.y, self.X).fit(method="newton", maxiter=100, disp=0, cov_type="HC1")
        self.converged = bool(res.mle_retvals["converged"])
        self.b, self.V, self.res = np.asarray(res.params), np.asarray(res.cov_params()), res
        self.mod = mod

    def _set(self, rows: np.ndarray, s: str, val: float) -> np.ndarray:
        X = self.X[rows].copy()
        X[:, self.idx[s]] = val
        if self.interactions:
            for m in self.mods[s][:-1]:
                j = self.idx[f"{s}:dev[{m}]"]
                ref = self.mods[s][-1]
                z = (self.mod[rows] == m).astype(float) - (self.mod[rows] == ref).astype(float)
                X[:, j] = val * z
        return X

    def ame(self, s: str, rows: np.ndarray) -> tuple[float, float, float, float]:
        """Average risk difference (sign on minus sign off) over `rows`, delta-method robust interval."""
        X1, X0 = self._set(rows, s, 1.0), self._set(rows, s, 0.0)
        p1, p0 = 1 / (1 + np.exp(-X1 @ self.b)), 1 / (1 + np.exp(-X0 @ self.b))
        est = float(np.mean(p1 - p0))
        g = (X1 * (p1 * (1 - p1))[:, None] - X0 * (p0 * (1 - p0))[:, None]).mean(axis=0)
        se = float(np.sqrt(g @ self.V @ g))
        return est, est - Z * se, est + Z * se, se

    def log_or(self, s: str, module: str | None = None) -> tuple[float, float]:
        """Log odds ratio of a sign at the average module (module=None) or in one module, with its SE."""
        g = np.zeros(len(self.b))
        g[self.idx[s]] = 1.0
        if module is not None and self.interactions and len(self.mods[s]) > 1:
            ms = self.mods[s]
            if module == ms[-1]:
                for m in ms[:-1]:
                    g[self.idx[f"{s}:dev[{m}]"]] = -1.0
            else:
                g[self.idx[f"{s}:dev[{module}]"]] = 1.0
        return float(g @ self.b), float(np.sqrt(g @ self.V @ g))

    def predict(self) -> np.ndarray:
        return 1 / (1 + np.exp(-self.X @ self.b))


def or_ci(lo: float, se: float) -> tuple[float, float, float]:
    return math.exp(lo), math.exp(lo - Z * se), math.exp(lo + Z * se)


def crude(f: pl.DataFrame, s: str) -> dict:
    d = f.filter(pl.Series(defined_mask(f, s)))
    a = int(((d[s] == 1) & (d["y"] == 1)).sum())
    n1 = int((d[s] == 1).sum())
    c = int(((d[s] == 0) & (d["y"] == 1)).sum())
    n0 = int((d[s] == 0).sum())
    rd, lo, hi = newcombe(a, n1, c, n0)
    o, olo, ohi = woolf_or(a, n1 - a, c, n0 - c)
    return dict(n=d.height, n_with=n1, nc_with=a, rate_with=r(a / n1 if n1 else math.nan),
                n_without=n0, nc_without=c, rate_without=r(c / n0 if n0 else math.nan),
                rd_unadj_pp=r(100 * rd, 2), rd_unadj_ci_low=r(100 * lo, 2), rd_unadj_ci_high=r(100 * hi, 2),
                or_unadj=r(o, 3), or_unadj_ci_low=r(olo, 3), or_unadj_ci_high=r(ohi, 3))


def verdict(ame_pp: float, lo_pp: float, same: int, defined: int) -> str:
    """Success criterion of Table 4.2."""
    ok = ame_pp >= 5 and lo_pp > 0 and same >= math.ceil(2 * defined / 3)
    return "consistent association" if ok else "weak or inconsistent"


def aq2(f27raw: pl.DataFrame, out: dict) -> None:
    signs = list(SIGNS)
    f = build_signs(f27raw)
    assert (f["missed_task"] == f["rule_missed"].cast(pl.Int8)).all()
    assert (f["late_tma"] == f["rule_tma_late"].cast(pl.Int8)).all()
    # task signs cannot occur in runs with no task due by day 27
    assert int(f.filter(~pl.col("task_run"))[["missed_task", "late_tma"]].sum().sum_horizontal()[0]) == 0

    # sign prevalence per run (with the late-CMA count used by the rule variant)
    prev = f.group_by("code_module", "code_presentation").agg(
        pl.len().alias("n"), pl.col("y").sum().alias("non_completers"),
        pl.col("run_tasks_due").first().alias("max_tasks_due_by_d27"),
        *[pl.col(s).mean().round(4).alias(f"share_{s}") for s in signs],
        (pl.col("cma_late_c") >= 1).mean().round(4).alias("share_late_cma"),
        pl.col("early_sign_rule").mean().round(4).alias("share_early_sign_rule"),
    ).sort("code_module", "code_presentation")
    prev.write_csv(RES / "aq2_sign_rates_by_run.csv")

    main = Fit(f, signs, interactions=True)
    assert main.converged
    coef = pl.DataFrame(dict(term=main.names, coef=main.b, robust_se=np.sqrt(np.diag(main.V)),
                             z=main.b / np.sqrt(np.diag(main.V)),
                             p_value=np.asarray(main.res.pvalues))).with_columns(
        pl.col("coef").exp().alias("odds_ratio"))
    coef.write_csv(RES / "aq2_model_coefficients.csv")

    # --- primary table: unadjusted and adjusted side by side -------------------------------------------------
    n_task_runs = f.filter(pl.col("task_run"))["run"].n_unique()
    rows = []
    for s in signs:
        mask = defined_mask(f, s)
        rows_idx = np.where(mask)[0]
        c = crude(f, s)
        single = Fit(f, [s], interactions=True)
        se_ame = single.ame(s, rows_idx)
        mu = main.ame(s, rows_idx)
        lo_, se_ = main.log_or(s)
        orr = or_ci(lo_, se_)
        slo, sse = single.log_or(s)
        sor = or_ci(slo, sse)
        mods = main.mods[s]
        mod_ame = {m: main.ame(s, np.where(mask & (main.mod == m))[0])[0] for m in mods}
        same = sum(1 for m in mods if math.copysign(1, mod_ame[m]) == math.copysign(1, mu[0]))
        p_main = float(main.res.pvalues[main.idx[s]])
        rows.append(dict(sign=s, definition=SIGNS[s],
                         population="enrolments registered at day 27 in "
                         + (f"the {n_task_runs} {SC['runs_text']} with a task due by day 27" if s in TASK_SIGNS else SC["label"]),
                         **c,
                         rd_adj_single_pp=r(100 * se_ame[0], 2), rd_adj_single_ci_low=r(100 * se_ame[1], 2),
                         rd_adj_single_ci_high=r(100 * se_ame[2], 2),
                         or_adj_single=r(sor[0], 3), or_adj_single_ci_low=r(sor[1], 3),
                         or_adj_single_ci_high=r(sor[2], 3),
                         rd_adj_mutual_pp=r(100 * mu[0], 2), rd_adj_mutual_ci_low=r(100 * mu[1], 2),
                         rd_adj_mutual_ci_high=r(100 * mu[2], 2),
                         or_adj_mutual=r(orr[0], 3), or_adj_mutual_ci_low=r(orr[1], 3),
                         or_adj_mutual_ci_high=r(orr[2], 3), p_value_mutual=float(f"{p_main:.3g}"),
                         modules_defined=len(mods), modules_same_direction=same,
                         verdict=verdict(100 * mu[0], 100 * mu[1], same, len(mods))))
    assoc = pl.DataFrame(rows)
    assoc.write_csv(RES / "aq2_associations.csv")

    # --- secondary: module-specific risk differences from the sign x module terms ---------------------------
    mrows = []
    for s in signs:
        mask = defined_mask(f, s)
        for m in main.mods[s]:
            sel = mask & (main.mod == m)
            d = f.filter(pl.Series(sel))
            c = crude(d.with_columns(pl.lit(True).alias("task_run")), s)
            a = main.ame(s, np.where(sel)[0])
            lo_, se_ = main.log_or(s, m)
            o = or_ci(lo_, se_)
            mrows.append(dict(sign=s, module=m, n=c["n"], n_with=c["n_with"], rate_with=c["rate_with"],
                              rate_without=c["rate_without"], rd_unadj_pp=c["rd_unadj_pp"],
                              rd_unadj_ci_low=c["rd_unadj_ci_low"], rd_unadj_ci_high=c["rd_unadj_ci_high"],
                              rd_adj_mutual_pp=r(100 * a[0], 2), rd_adj_mutual_ci_low=r(100 * a[1], 2),
                              rd_adj_mutual_ci_high=r(100 * a[2], 2), or_adj_mutual=r(o[0], 3),
                              or_adj_mutual_ci_low=r(o[1], 3), or_adj_mutual_ci_high=r(o[2], 3)))
    pl.DataFrame(mrows).write_csv(RES / "aq2_module_effects.csv")

    # --- error analysis: binned residuals by run, activity level and predicted risk -----------------------------
    p = main.predict()
    fr = f.with_columns(pl.Series("p", p))
    act = (pl.when(pl.col("clicks_0c") == 0).then(pl.lit("1 no clicks days 0-27"))
           .when(pl.col("activity_ratio_run") < 0.5).then(pl.lit("2 below half the run median"))
           .when(pl.col("activity_ratio_run") < 1).then(pl.lit("3 half to the run median"))
           .when(pl.col("activity_ratio_run") < 2).then(pl.lit("4 median to twice the median"))
           .otherwise(pl.lit("5 twice the run median or more")))
    fr = fr.with_columns(act.alias("activity_level"),
                         (pl.col("p").rank("ordinal") * 10 / pl.len()).ceil().cast(pl.Int64).alias("risk_decile"))
    br = []
    for by in ["run", "activity_level", "risk_decile"]:
        g = fr.group_by(by).agg(pl.len().alias("n"), pl.col("y").mean().alias("observed"),
                                pl.col("p").mean().alias("predicted"),
                                (pl.col("p") * (1 - pl.col("p"))).sum().alias("v")).sort(by)
        for x in g.iter_rows(named=True):
            se = math.sqrt(x["v"]) / x["n"]
            res_ = x["observed"] - x["predicted"]
            br.append(dict(binned_by=by, bin=str(x[by]), n=x["n"], observed=r(x["observed"]),
                           predicted=r(x["predicted"]), residual_pp=r(100 * res_, 2),
                           band_2se_pp=r(200 * se, 2), outside_band=abs(res_) > 2 * se))
    br = pl.DataFrame(br)
    br.write_csv(RES / "aq2_binned_residuals.csv")

    # --- error analysis: correlation among the signs and click measures (Pearson; phi for two binary signs) -----
    cm = f.with_columns(pl.col("clicks_0c").log1p().alias("log_clicks_0_27"),
                        pl.col("active_days_0c").cast(pl.Float64).alias("active_days_0_27"),
                        pl.col("activity_ratio_run").log().alias("log_activity_ratio"))
    vars_ = [*signs, "log_clicks_0_27", "active_days_0_27", "log_activity_ratio"]
    M = np.column_stack([cm[v].cast(pl.Float64).to_numpy() for v in vars_])
    C = np.corrcoef(M, rowvar=False)
    corr = pl.DataFrame({"variable": vars_, **{v: np.round(C[:, i], 3) for i, v in enumerate(vars_)}})
    corr.write_csv(RES / "aq2_sign_correlation.csv")

    # --- sensitivity runs ---------------------------------------------------------------------------------------
    flagged = (pl.col("eval_withdrawal_day_unknown") | pl.col("registration_missing"))
    variants = [
        ("primary", "plan", f27raw, "primary"),
        ("dedup_clicks", "plan (card AQ2: de-duplicated clicks)", f27raw, "dedup_clicks"),
        ("late_tma_or_cma", "plan (card AQ2: rule variant that also counts late CMAs)", f27raw, "late_tma_or_cma"),
        ("excl_flagged", "plan (card AQ2: without the flagged enrolments)", f27raw.filter(~flagged), "primary"),
        ("drop_no_task_runs", "plan (card AQ2: dropping runs with no task due)",
         f27raw.filter(pl.col("tasks_due_c").max().over("code_module", "code_presentation") >= 1), "primary"),
        ("below_half_median", "added (threshold of the relative-activity sign)", f27raw, "below_half_median"),
        ("no_interactions", "added (common sign effect across modules)", f27raw, "primary"),
    ]
    sens = []
    for name, origin, data, var in variants:
        d = build_signs(data, var)
        m = Fit(d, signs, interactions=(name != "no_interactions"))
        for s in signs:
            mask = defined_mask(d, s)
            a = m.ame(s, np.where(mask)[0])
            lo_, se_ = m.log_or(s)
            o = or_ci(lo_, se_)
            c = crude(d, s)
            sens.append(dict(variant=name, origin=origin, sign=s, n=c["n"], n_non_completers=int(d["y"].sum()),
                             n_with=c["n_with"], converged=m.converged,
                             rd_unadj_pp=c["rd_unadj_pp"], rd_adj_mutual_pp=r(100 * a[0], 2),
                             rd_adj_mutual_ci_low=r(100 * a[1], 2), rd_adj_mutual_ci_high=r(100 * a[2], 2),
                             or_adj_mutual=r(o[0], 3), or_adj_mutual_ci_low=r(o[1], 3),
                             or_adj_mutual_ci_high=r(o[2], 3)))
    sens = pl.DataFrame(sens)
    sens.write_csv(RES / "aq2_sensitivity.csv")

    # --- subgroup description: gender, disability, deprivation band (described, not adjusted away) ------------
    sub = []
    for col in ["gender", "disability", "imd_band"]:
        for gval in sorted(f[col].unique().to_list()):
            d = f.filter(pl.col(col) == gval)
            nc = int(d["y"].sum())
            enough = nc >= MIN_EVENTS_SUBGROUP_MODEL and (d.height - nc) >= MIN_EVENTS_SUBGROUP_MODEL
            m = None
            if enough:
                try:
                    import warnings
                    from statsmodels.tools.sm_exceptions import ConvergenceWarning
                    with warnings.catch_warnings():   # a non-converged refit is caught below and reported crude
                        warnings.simplefilter("ignore", ConvergenceWarning)
                        m = Fit(d, signs, interactions=False)
                    if not m.converged:
                        m = None
                except Exception:  # noqa: BLE001 - separation in a small group: report crude only
                    m = None
            p_, lo_, hi_ = wilson(nc, d.height)
            for s in signs:
                c = crude(d, s)
                row = dict(attribute=col, group=gval, n=d.height, non_completers=nc, nc_rate=r(p_),
                           nc_ci_low=r(lo_), nc_ci_high=r(hi_), sign=s, n_sign_defined=c["n"],
                           n_with=c["n_with"], rate_with=c["rate_with"], rate_without=c["rate_without"],
                           rd_unadj_pp=c["rd_unadj_pp"], rd_unadj_ci_low=c["rd_unadj_ci_low"],
                           rd_unadj_ci_high=c["rd_unadj_ci_high"], rd_adj_mutual_pp=None,
                           rd_adj_mutual_ci_low=None, rd_adj_mutual_ci_high=None,
                           adjusted_note="adjusted model fitted (run fixed effects, background, all signs; no "
                                         "sign x module terms)" if m is not None else
                           f"crude only: fewer than {MIN_EVENTS_SUBGROUP_MODEL} non-completers or completers, or no convergence")
                if m is not None and c["n_with"] > 0:
                    a = m.ame(s, np.where(defined_mask(d, s))[0])
                    row.update(rd_adj_mutual_pp=r(100 * a[0], 2), rd_adj_mutual_ci_low=r(100 * a[1], 2),
                               rd_adj_mutual_ci_high=r(100 * a[2], 2))
                sub.append(row)
    pl.DataFrame(sub).write_csv(RES / "aq2_subgroups.csv")

    out["aq2"] = dict(
        population=dict(n=f.height, non_completers=int(f["y"].sum()), non_completion=r(f["y"].mean()),
                        n_task_runs=int(f["task_run"].sum()),
                        task_runs=sorted(f.filter(pl.col("task_run"))["run"].unique().to_list()),
                        runs=sorted(f["run"].unique().to_list())),
        model=dict(n_params=len(main.b), converged=main.converged, covariance="HC1 robust, no clustering",
                   pseudo_r2=r(main.res.prsquared)),
        associations=assoc.select("sign", "n", "n_with", "rate_with", "rate_without", "rd_unadj_pp",
                                  "rd_unadj_ci_low", "rd_unadj_ci_high", "rd_adj_single_pp",
                                  "rd_adj_mutual_pp", "rd_adj_mutual_ci_low", "rd_adj_mutual_ci_high",
                                  "or_adj_mutual", "or_adj_mutual_ci_low", "or_adj_mutual_ci_high",
                                  "modules_defined", "modules_same_direction", "verdict").to_dicts(),
        binned_residual_bins_outside_2se=br.filter(pl.col("outside_band")).select("binned_by", "bin",
                                                                                   "residual_pp").to_dicts(),
    )


# ---------------------------------------------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------------------------------------------
def md_table(df: pl.DataFrame) -> str:
    cols = df.columns
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join([":----"] * len(cols)) + " |"]
    for row in df.iter_rows():
        lines.append("| " + " | ".join("" if v is None else str(v) for v in row) + " |")
    return "\n".join(lines)


def pct(rate, lo, hi) -> str:
    return f"{100 * rate:.1f}% ({100 * lo:.1f}–{100 * hi:.1f})"


def summary() -> None:
    rates = pl.read_csv(RES / "aq1_rates.csv")
    parts = ["# AQ1 and AQ2 results on the 9 module runs of 2013\n" if SC["name"] == "2013"
             else f"# AQ1 and AQ2 results on {SC['label']}\n",
             f"Written by `src/analysis/aq_analysis.py --scope {SC['name']}`. Rates carry 95% Wilson score intervals; differences of two rates "
             "carry 95% Newcombe hybrid score intervals; model estimates carry 95% intervals from HC1 robust "
             "standard errors (delta method for risk differences). Methods and deviations: `results/README.md`.\n"]

    def rate_tab(level, den):
        t = rates.filter((pl.col("level") == level) & (pl.col("denominator") == den))
        t = t.filter(pl.col("measure").is_in(["non_completion", "Pass", "Distinction", "Fail", "Withdrawn"]))
        t = t.with_columns(pl.struct("rate", "ci_low", "ci_high").map_elements(
            lambda x: pct(x["rate"], x["ci_low"], x["ci_high"]), return_dtype=pl.String).alias("v"))
        w = t.pivot(on="measure", index=["group", "n"], values="v", aggregate_function="first")
        nc = t.filter(pl.col("measure") == "non_completion").select("group", pl.col("events").alias("non_completers"))
        return w.join(nc, on="group").select("group", "n", "non_completers", "non_completion", "Pass",
                                             "Distinction", "Fail", "Withdrawn")

    parts.append("## AQ1. Outcome shares\n")
    for den, txt in [("day14_registered", "enrolments still registered at day 14 (KPI population)"),
                     ("all_enrolments", "all enrolments")]:
        for lvl in ["overall", "module", "run", "start_month"]:
            words = {"overall": "All runs", "module": "By module", "run": "By run", "start_month": "By start month"}[lvl]
            parts.append(f"**{words}, {txt}.** Non-completion and the four outcome shares"
                         f"{'' if lvl == 'overall' else ' by ' + lvl.replace('_', ' ')} (`aq1_rates.csv`).\n")
            parts.append(md_table(rate_tab(lvl, den)) + "\n")
    t = rates.filter((pl.col("level") == "overall") & pl.col("measure").is_in(["completion", "non_completion"]))
    parts.append("**Denominator baselines.** Pooled completion and non-completion under the three denominators "
                 "the AQ1 card names: day-14 population, all enrolments, day-14 population without the flagged "
                 "enrolments (`aq1_rates.csv`).\n")
    parts.append(md_table(t.select("denominator", "measure", "events", "n", "rate", "ci_low", "ci_high")) + "\n")
    sh = pl.read_csv(RES / "aq1_denominator_shift.csv").filter(pl.col("measure") == "non_completion")
    parts.append("**Denominator shift.** Non-completion under the day-14 and all-enrolment denominators and whether "
                 "the all-enrolment rate falls outside the day-14 interval (`aq1_denominator_shift.csv`).\n")
    parts.append(md_table(sh.select("level", "group", "n_day14", "rate_day14", "ci_low_day14", "ci_high_day14",
                                    "n_all", "rate_all", "shift_pp", "outside_day14_interval")) + "\n")
    if SC["name"] == "2013":
        yd = pl.read_csv(COMPARE / "aq1_year_difference_published.csv")
        parts.append("**Year comparison.** Non-completion over all enrolments in 2013 (computed) and 2014 (published in "
                     "Milestone 3, not recomputed), with the 2014 − 2013 difference (`../compare/aq1_year_difference_published.csv`; the comparison computed from both years is in `../compare/`).\n")
        parts.append(md_table(yd) + "\n")
    fm = pl.read_csv(RES / "aq1_first_missed_week_summary.csv")
    parts.append("**First missed task.** Share of enrolments with a missed assessed task, share by week 4 and the "
                 "quartiles of the week of the first missed task, by outcome (`aq1_first_missed_week_summary.csv`).\n")
    parts.append(md_table(fm) + "\n")
    cum = pl.read_csv(RES / "aq1_first_missed_week_cumulative.csv").filter(
        (pl.col("denominator") == "day14_registered") & pl.col("week").is_in([2, 4, 6, 8, 12, 16, 20, 26, 30, 34]))
    parts.append("**Cumulative first missed task.** Cumulative share of the day-14 population with a first missed "
                 "task by selected weeks, by outcome (`aq1_first_missed_week_cumulative.csv`, all weeks).\n")
    parts.append(md_table(cum.pivot(on="week", index="group", values="cum_share", aggregate_function="first")) + "\n")
    parts.append("**Runs and tasks due.** Tasks due by day 27, first due day and missed-task timing per run "
                 "(`aq1_runs_task_due.csv`).\n")
    parts.append(md_table(pl.read_csv(RES / "aq1_runs_task_due.csv")) + "\n")
    sg = pl.read_csv(RES / "aq1_subgroup_rates.csv").filter(
        (pl.col("denominator") == "day14_registered") & (pl.col("measure") == "non_completion"))
    parts.append("**Subgroups (description only).** Non-completion in the day-14 population by gender, disability, "
                 "deprivation band and age band (`aq1_subgroup_rates.csv`).\n")
    parts.append(md_table(sg.select("level", "group", "events", "n", "rate", "ci_low", "ci_high")) + "\n")

    parts.append("## AQ2. Early signs at day 27 and later non-completion\n")
    a = pl.read_csv(RES / "aq2_associations.csv")
    parts.append("**Associations.** Per sign: rates with and without it, unadjusted difference, adjusted difference "
                 "one sign at a time and mutually adjusted (average risk difference within module run, pp), odds "
                 "ratios at the average module, module direction count and the card's verdict (`aq2_associations.csv`).\n")
    parts.append(md_table(a.select("sign", "n", "n_with", "rate_with", "rate_without", "rd_unadj_pp",
                                   "rd_unadj_ci_low", "rd_unadj_ci_high", "or_unadj", "rd_adj_single_pp",
                                   "rd_adj_mutual_pp", "rd_adj_mutual_ci_low", "rd_adj_mutual_ci_high",
                                   "or_adj_mutual", "or_adj_mutual_ci_low", "or_adj_mutual_ci_high",
                                   "modules_same_direction", "modules_defined", "verdict")) + "\n")
    parts.append("**Sign prevalence.** Share of enrolments registered at day 27 with each sign, per run, with the "
                 "late-CMA share used by the rule variant (`aq2_sign_rates_by_run.csv`).\n")
    parts.append(md_table(pl.read_csv(RES / "aq2_sign_rates_by_run.csv")) + "\n")
    parts.append("**Module effects.** Module-specific unadjusted and mutually adjusted risk differences (pp) and odds "
                 "ratios from the sign × module terms (`aq2_module_effects.csv`).\n")
    parts.append(md_table(pl.read_csv(RES / "aq2_module_effects.csv")) + "\n")
    parts.append("**Sensitivity runs.** Mutually adjusted average risk difference (pp) per sign under each variant "
                 "(`aq2_sensitivity.csv`).\n")
    s = pl.read_csv(RES / "aq2_sensitivity.csv").with_columns(
        pl.format("{} ({}, {})", "rd_adj_mutual_pp", "rd_adj_mutual_ci_low", "rd_adj_mutual_ci_high").alias("v"))
    n = s.group_by("variant", maintain_order=True).agg(
        pl.col("n").max().alias("n_click_signs"), pl.col("n").min().alias("n_task_signs"))
    parts.append(md_table(n.join(s.pivot(on="sign", index="variant", values="v", aggregate_function="first"),
                                 on="variant")) + "\n")
    parts.append("**Binned residuals.** Observed minus predicted non-completion (pp) by run, activity level and "
                 "predicted-risk decile, with the ±2 SE band (`aq2_binned_residuals.csv`).\n")
    parts.append(md_table(pl.read_csv(RES / "aq2_binned_residuals.csv")) + "\n")
    parts.append("**Correlation.** Pearson correlation among the signs (phi for two binary signs) and the click "
                 "measures at day 27 (`aq2_sign_correlation.csv`).\n")
    parts.append(md_table(pl.read_csv(RES / "aq2_sign_correlation.csv")) + "\n")
    sg = pl.read_csv(RES / "aq2_subgroups.csv")
    parts.append("**Subgroups (description, not adjusted away).** Unadjusted and adjusted risk difference (pp) of "
                 "each sign within gender, disability and deprivation band (`aq2_subgroups.csv`).\n")
    parts.append(md_table(sg.select("attribute", "group", "n", "non_completers", "sign", "n_with", "rd_unadj_pp",
                                    "rd_unadj_ci_low", "rd_unadj_ci_high", "rd_adj_mutual_pp",
                                    "rd_adj_mutual_ci_low", "rd_adj_mutual_ci_high")) + "\n")
    (RES / "aq_summary.md").write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--scope", choices=sorted(SCOPES), default="2013")
    set_scope(ap.parse_args().scope)
    RES.mkdir(parents=True, exist_ok=True)
    enr = load_view("enrolment")
    f27 = load_view("features_d27")
    print(f"{SC['name']} rows loaded: enrolment {enr.height}, features_d27 {f27.height}; "
          f"presentations {sorted(enr['code_presentation'].unique().to_list())}")
    out: dict = {"scope": "9 module runs of 2013; no 2014 row of any prepared view read (filter pushed to the "
                          "reader and asserted); 2014 rates only as published by Milestone 3"
                 if SC["name"] == "2013" else f"{SC['label']}; no row outside these runs read (filter pushed to "
                 f"the reader and asserted)"}
    aq1(enr, f27, out)
    aq2(f27, out)
    (RES / "aq_results.json").write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str),
                                         encoding="utf-8")
    summary()
    a1, a2 = out["aq1"], out["aq2"]
    for den in ["day14_registered", "all_enrolments", "day14_registered_excl_flagged"]:
        x = a1[den]
        print(f"AQ1 {den}: n={x['n']} non-completers={x['non_completers']} rate={x['non_completion']}")
    print(f"AQ1 validation: {a1['validation']}")
    print(f"AQ2 population: {a2['population']['n']} enrolments, {a2['population']['non_completers']} non-completers")
    for x in a2["associations"]:
        print(f"AQ2 {x['sign']}: unadj {x['rd_unadj_pp']} pp; mutual {x['rd_adj_mutual_pp']} pp "
              f"({x['rd_adj_mutual_ci_low']}, {x['rd_adj_mutual_ci_high']}); OR {x['or_adj_mutual']}; "
              f"{x['modules_same_direction']}/{x['modules_defined']} modules; {x['verdict']}")
    print(f"Results written to {RES.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
