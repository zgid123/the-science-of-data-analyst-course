"""AQ1 step 3 – evaluation checks of the Evaluation Design Card (Level 1 report, Table 4.1).

A check passes only when its condition is evaluated here. Writes results/checks_<scope>.csv; exits 1 on a failure.

C1  control totals: 32,593 enrolments and 28,061 in the KPI population (scope all); 2013 part for scope 2013
C2  second aggregation path: rates per run recomputed from the raw OULAD tables agree to the enrolment
C3  first missed week stored in the prepared view equals the week re-derived from the task table
C4  the pooled count equals the sum of the run counts; outcome shares sum to 1 in every run
C5  every published rate carries its denominator and interval, and the interval contains the rate
C6  (scope all) the counts behind the year comparison, recomputed from the raw tables by a second code path, equal
    the counts of results/year_comparison_all.csv for the three overall scopes under both denominators
C7  (scope all) every Newcombe interval of the year comparison equals the interval computed by statsmodels
"""

import sys

import polars as pl

from aq1_common import EXTRACT, RESULTS, lib, scope_args

scope, years = scope_args(__doc__)
enr = pl.read_csv(EXTRACT / f"aq1_enrolments_{scope}.csv")
kpi = enr.filter(pl.col("enrolled_d14"))
checks = []


def check(cid, what, ok, detail):
    checks.append({"check": cid, "what": what, "result": "PASS" if ok else "FAIL", "detail": detail})


# C1 ---------------------------------------------------------------------------------------------------
if scope == "all":
    check("C1", "control totals 32,593 enrolments / 28,061 KPI", enr.height == 32593 and kpi.height == 28061,
          f"found {enr.height:,} / {kpi.height:,}")
else:
    check("C1", "2013 runs: 9 runs, every enrolment of year 2013", enr["run"].n_unique() == 9 and enr["year"].unique().to_list() == [2013],
          f"{enr.height:,} enrolments, {kpi.height:,} in the KPI population, {enr['run'].n_unique()} runs")

# C2 ---------------------------------------------------------------------------------------------------
if scope == "all":
    lib.open_test_outcomes("aq-1/code/03_checks.py", "AQ1 second aggregation path from the raw tables (2014 runs included)")
info = pl.read_csv(lib.RAW / "studentInfo.csv", infer_schema_length=None)
reg = pl.read_csv(lib.RAW / "studentRegistration.csv", infer_schema_length=None, null_values=[""])
raw = info.join(reg, on=lib.KEYS, how="left", validate="1:1")
raw = raw.filter(pl.col("code_presentation").str.slice(0, 4).cast(pl.Int64).is_in(list(years)))
raw = raw.with_columns(
    ((pl.col("date_registration").is_null() | (pl.col("date_registration") <= 14))
     & (pl.col("date_unregistration").is_null() | (pl.col("date_unregistration") > 14))).alias("enrolled_d14_raw"),
    pl.col("final_result").is_in(["Fail", "Withdrawn"]).alias("nc_raw"),
    (pl.col("code_module") + "-" + pl.col("code_presentation")).alias("run"),
)
p1 = kpi.group_by("run").agg(pl.len().alias("n_prepared"), pl.col("non_completion").sum().alias("events_prepared"))
p2 = raw.filter(pl.col("enrolled_d14_raw")).group_by("run").agg(pl.len().alias("n_raw"), pl.col("nc_raw").sum().alias("events_raw"))
cmp = p1.join(p2, on="run", how="full", coalesce=True).sort("run").with_columns(
    ((pl.col("n_prepared") == pl.col("n_raw")) & (pl.col("events_prepared") == pl.col("events_raw"))).fill_null(False).alias("agree"))
lib.banner("C2 – prepared view against raw tables, per run (KPI population)")
print(lib.md_table(cmp))
lib.save_csv(cmp, RESULTS / f"check_two_paths_{scope}.csv")
check("C2", "two aggregation paths agree to the enrolment in every run", bool(cmp["agree"].all()) and raw.height == enr.height,
      f"{int(cmp['agree'].sum())} of {cmp.height} runs agree; raw rows {raw.height:,} = prepared rows {enr.height:,}: {raw.height == enr.height}")

# C3 ---------------------------------------------------------------------------------------------------
rec = pl.read_csv(EXTRACT / f"aq1_first_missed_recomputed_{scope}.csv")
j = enr.select(lib.KEYS + ["first_missed_week"]).join(rec, on=lib.KEYS, how="left")
same = j.filter(pl.col("first_missed_week").eq_missing(pl.col("first_missed_week_recomputed"))).height
check("C3", "first missed week equals the value re-derived from the task table", same == j.height, f"{same:,} of {j.height:,} enrolments equal")

# C4 ---------------------------------------------------------------------------------------------------
rates = pl.read_csv(RESULTS / f"rates_{scope}.csv")
pooled = rates.filter(pl.col("level") == "pooled")
runs = rates.filter(pl.col("level") == "run")
sum_ok = int(runs["enrolments"].sum()) == int(pooled["enrolments"][0]) == kpi.height and int(runs["events"].sum()) == int(pooled["events"][0])
shares = pl.read_csv(RESULTS / f"outcome_shares_{scope}.csv").filter(pl.col("level") == "run")
tot = shares.group_by("group").agg(pl.col("events").sum().alias("events"), pl.col("enrolments").first().alias("n"))
check("C4", "pooled counts equal the sum over runs; the four outcome counts sum to the enrolments of every run",
      sum_ok and bool((tot["events"] == tot["n"]).all()),
      f"sum of run enrolments {int(runs['enrolments'].sum()):,} = pooled {int(pooled['enrolments'][0]):,}; runs whose outcome counts sum to n: {int((tot['events'] == tot['n']).sum())} of {tot.height}")

# C5 ---------------------------------------------------------------------------------------------------
ok5 = rates.filter((pl.col("enrolments") > 0) & (pl.col("ci_low") <= pl.col("rate")) & (pl.col("rate") <= pl.col("ci_high"))).height == rates.height
check("C5", "every rate has a denominator and an interval that contains it", ok5, f"{rates.height} rates checked")

# C6, C7 -----------------------------------------------------------------------------------------------
if scope == "all":
    yc = pl.read_csv(RESULTS / "year_comparison_all.csv")
    # second code path: plain Python over the raw rows, no shared function
    cnt: dict[tuple, list[int]] = {}
    runs_by_year: dict[int, set] = {2013: set(), 2014: set()}
    raw_rows = raw.select("code_module", "code_presentation", "enrolled_d14_raw", "nc_raw").rows()
    for m, pres, _, _ in raw_rows:
        runs_by_year[int(pres[:4])].add((m, pres[4]))
    shared_mod = {m for m, _ in runs_by_year[2013]} & {m for m, _ in runs_by_year[2014]}
    pairs = runs_by_year[2013] & runs_by_year[2014]
    for m, pres, reg14, nc in raw_rows:
        yr, sm = int(pres[:4]), pres[4]
        for den in ("all enrolments", "registered at day 14 (KPI population)"):
            if den.startswith("registered") and not reg14:
                continue
            for sc, inside in (("all", True), ("modules", m in shared_mod), ("pairs", (m, sm) in pairs)):
                if inside:
                    c = cnt.setdefault((den, sc, yr), [0, 0])
                    c[0] += 1
                    c[1] += int(nc)
    ov = yc.filter((pl.col("level") == "overall") & pl.col("method").str.starts_with("pooled"))
    bad6, n6 = [], 0
    for r in ov.iter_rows(named=True):
        sc = "all" if r["scope"].startswith("all runs") else ("modules" if "modules run in both years" in r["scope"] else "pairs")
        for yr in (2013, 2014):
            n6 += 1
            if cnt[(r["denominator"], sc, yr)] != [r[f"n_{yr}"], r[f"events_{yr}"]]:
                bad6.append((r["denominator"], r["scope"], yr, cnt[(r["denominator"], sc, yr)], [r[f"n_{yr}"], r[f"events_{yr}"]]))
    check("C6", "year-comparison counts recomputed from the raw tables equal the result table (3 scopes x 2 denominators x 2 years)", not bad6,
          f"{n6 - len(bad6)} of {n6} count pairs equal; {len(shared_mod)} shared modules, {len(pairs)} shared module x start-month pairs" + (f"; differences: {bad6}" if bad6 else ""))

    from statsmodels.stats.proportion import confint_proportions_2indep
    worst, n7 = 0.0, 0
    for r in yc.filter(pl.col("method").str.starts_with("pooled")).iter_rows(named=True):
        lo, hi = confint_proportions_2indep(r["events_2014"], r["n_2014"], r["events_2013"], r["n_2013"], method="newcomb", compare="diff")
        worst = max(worst, abs(lo - r["ci_low"]), abs(hi - r["ci_high"]))
        n7 += 1
    check("C7", "Newcombe intervals of the year comparison equal the statsmodels implementation (tolerance 1e-5; stored with 6 decimals)", worst < 1e-5,
          f"{n7} intervals compared; largest absolute difference of a bound {worst:.1e}")

out = pl.DataFrame(checks)
lib.banner(f"AQ1 check ledger, scope = {scope}")
print(lib.md_table(out))
lib.save_csv(out, RESULTS / f"checks_{scope}.csv")
sys.exit(0 if (out["result"] == "PASS").all() else 1)
