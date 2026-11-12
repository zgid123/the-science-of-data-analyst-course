"""T27: three appendix tables for AQ1 and AQ2, 2013 and 2014 apart, with the definitions of aq_analysis.py.

Reads the same prepared views as code/aq_analysis.py (Milestone 3 package: enrolment.parquet, features_d27.parquet),
filtered to one year at a time, and reuses its sign definitions (build_signs: low relative activity = clicks on days
0-27 below the run median), its Wilson and Newcombe intervals and its populations:

1. AQ2, Appendix XIII: non-completion by the number of early signs present at day 27, enrolments registered at day 27.
   The two task signs are defined only in the runs with a task due by day 27, so the count runs over five signs in
   those runs and over the three click signs in the runs with no task due (EEE and GGG); the two blocks are kept apart
   rather than counting an undefined task sign as absent.
2. AQ1, Appendix XII: week of the first missed TMA or CMA for the non-completers of the day-14 (KPI) population, by
   module: n, share who ever missed one, median first missed week among them, share missed by week 4 and by week 8.
3. AQ1, Appendix XII: February (B) minus October (J) non-completion within each module that ran in both start months
   in the year, day-14 population, Newcombe hybrid score interval.

Writes results/<year>/aq2_sign_count.csv, aq1_first_missed_week_by_module.csv, aq1_start_month_difference_by_module.csv
for 2013 and 2014, and results/compare/t27_appendix_tables.md (the three tables as the report shows them). Prints one
cross-check line per table against an existing result file of the same population.

Usage (from the repository root): venv/bin/python reports/milestone-5/code/t27_appendix_tables.py
"""
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import polars as pl

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import aq_analysis as aq  # noqa: E402  (definitions, intervals and input paths of the AQ analysis)

TASK = HERE.parent
RES = TASK / "results"
YEARS = {"2013": ["2013B", "2013J"], "2014": ["2014B", "2014J"]}
CLICK_SIGNS = ["inactive_last7", "low_relative_activity", "no_pre_start_activity"]


def load(view: str, year: str) -> pl.DataFrame:
    df = pl.scan_parquet(aq.PROC / f"{view}.parquet").filter(
        pl.col("code_presentation").is_in(YEARS[year])).collect()
    assert set(df["code_presentation"].unique()) <= set(YEARS[year])
    return df


def one(v: float) -> str:
    """Percent with one decimal, rounded half up from the 4-decimal stored value, as the report's tables are."""
    return str((Decimal(str(v)) * 100).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def pct(p: float, lo: float, hi: float) -> str:
    return f"{one(p)}% ({one(lo)}–{one(hi)})"


def pp(d: float, lo: float, hi: float) -> str:
    """A difference in points as Table A.32 writes it: +2.8 (−3.6 to 9.3)."""
    def f(v: float) -> str:
        return one(v).replace("-", "−")
    return f"{'+' if d > 0 else ''}{f(d)} ({f(lo)} to {f(hi)})"


def n_fmt(n: int) -> str:
    return f"{n:,}"


# --- 1. AQ2: number of early signs present at day 27 --------------------------------------------------------------
def sign_count(year: str) -> pl.DataFrame:
    f = aq.build_signs(load("features_d27", year))
    rows = []
    for block, mask, signs in [
        ("runs with a task due by day 27 (five signs)", pl.col("task_run"), list(aq.SIGNS)),
        ("runs with no task due by day 27 (three click signs)", ~pl.col("task_run"), CLICK_SIGNS),
    ]:
        d = f.filter(mask).with_columns(pl.sum_horizontal(signs).alias("signs_present"))
        runs = d.select(pl.struct("code_module", "code_presentation").n_unique()).item()
        for k in range(len(signs) + 1):
            s = d.filter(pl.col("signs_present") == k)
            x = int(s["y"].sum())
            p, lo, hi = aq.wilson(x, s.height)
            rows.append(dict(year=year, block=block, runs=runs, block_n=d.height, signs_present=k, n=s.height,
                             non_completers=x, rate=aq.r(p), ci_low=aq.r(lo), ci_high=aq.r(hi)))
    out = pl.DataFrame(rows)
    out.write_csv(RES / year / "aq2_sign_count.csv")
    return out


# --- 2. AQ1: first missed week of the non-completers by module ----------------------------------------------------
def first_missed_by_module(year: str) -> pl.DataFrame:
    e = load("enrolment", year).filter(pl.col("enrolled_d14") & pl.col("non_completion"))
    rows = []
    for mod, s in sorted([(m, e.filter(pl.col("code_module") == m)) for m in e["code_module"].unique()]) + [
            ("All modules", e)]:
        w = s["first_missed_week"]
        row = dict(year=year, module=mod, n=s.height)
        for key, x in [("ever", int(w.drop_nulls().len())), ("by_week4", int((w <= 4).sum())),
                       ("by_week8", int((w <= 8).sum()))]:
            p, lo, hi = aq.wilson(x, s.height)
            row |= {f"{key}_n": x, f"share_{key}": aq.r(p), f"{key}_ci_low": aq.r(lo), f"{key}_ci_high": aq.r(hi)}
        row["median_first_missed_week"] = float(w.drop_nulls().median())
        rows.append(row)
    out = pl.DataFrame(rows)
    out.write_csv(RES / year / "aq1_first_missed_week_by_module.csv")
    return out


# --- 3. AQ1: February minus October within module -----------------------------------------------------------------
def start_month_difference(year: str) -> pl.DataFrame:
    e = load("enrolment", year).filter(pl.col("enrolled_d14")).with_columns(
        pl.col("code_presentation").str.slice(4, 1).alias("sm"))
    g = e.group_by("code_module", "sm").agg(pl.len().alias("n"), pl.col("non_completion").sum().alias("x"))
    rows = []
    both = sorted(m for m in g["code_module"].unique() if g.filter(pl.col("code_module") == m).height == 2)
    groups = [(m, g.filter(pl.col("code_module") == m)) for m in both]
    # all modules of the year that ran in both start months, pooled
    pooled = e.filter(pl.col("code_module").is_in(both)).group_by("sm").agg(
        pl.len().alias("n"), pl.col("non_completion").sum().alias("x"))
    for mod, s in groups + [("Modules run in both start months, pooled", pooled)]:
        b = s.filter(pl.col("sm") == "B").row(0, named=True)
        j = s.filter(pl.col("sm") == "J").row(0, named=True)
        pb, lb, hb = aq.wilson(b["x"], b["n"])
        pj, lj, hj = aq.wilson(j["x"], j["n"])
        d, dl, dh = aq.newcombe(b["x"], b["n"], j["x"], j["n"])
        rows.append(dict(year=year, module=mod, n_february=b["n"], nc_february=b["x"], rate_february=aq.r(pb),
                         february_ci_low=aq.r(lb), february_ci_high=aq.r(hb), n_october=j["n"], nc_october=j["x"],
                         rate_october=aq.r(pj), october_ci_low=aq.r(lj), october_ci_high=aq.r(hj),
                         difference_pp=aq.r(100 * d), difference_ci_low=aq.r(100 * dl),
                         difference_ci_high=aq.r(100 * dh)))
    out = pl.DataFrame(rows)
    out.write_csv(RES / year / "aq1_start_month_difference_by_module.csv")
    return out


def check(label: str, ok: bool, detail: str) -> bool:
    print(f"{'PASS' if ok else 'FAIL'} {label}: {detail}")
    return ok


def main() -> int:
    sc, fm, sm = {}, {}, {}
    for y in YEARS:
        sc[y], fm[y], sm[y] = sign_count(y), first_missed_by_module(y), start_month_difference(y)
    ok = True
    # cross-checks against result files written by aq_analysis.py for the same populations
    for y in YEARS:
        a = pl.read_csv(RES / y / "aq2_associations.csv")
        n_task = a.filter(pl.col("sign") == "missed_task")["n"][0]
        n_all = a.filter(pl.col("sign") == "inactive_last7")["n"][0]
        blk = sc[y].group_by("block").agg(pl.col("n").sum(), pl.col("block_n").first())
        tot = int(blk["n"].sum())
        ok &= check(f"{y} sign count: blocks add up to the day-27 population", tot == n_all,
                    f"{tot} vs {n_all} (aq2_associations.csv)")
        nt = int(blk.filter(pl.col("block").str.starts_with("runs with a task"))["n"][0])
        ok &= check(f"{y} sign count: five-sign block equals the task-sign population", nt == n_task,
                    f"{nt} vs {n_task}")
        # zero signs in the five-sign block = enrolments with none of the five; recount without sum_horizontal
        f = aq.build_signs(load("features_d27", y)).filter(pl.col("task_run"))
        none = f.filter(pl.all_horizontal([pl.col(s) == 0 for s in aq.SIGNS]))
        z = sc[y].filter(pl.col("block").str.starts_with("runs with a task") & (pl.col("signs_present") == 0))
        ok &= check(f"{y} sign count: 0-sign cell recounted", (none.height, int(none["y"].sum())) ==
                    (z["n"][0], z["non_completers"][0]), f"{none.height}/{int(none['y'].sum())}")
        both = int(((f["missed_task"] == 1) & (f["late_tma"] == 1)).sum())
        print(f"INFO {y}: enrolments with both a missed task and a late TMA at day 27: {both}")
        summ = pl.read_csv(RES / y / "aq1_first_missed_week_summary.csv").filter(
            (pl.col("denominator") == "day14_registered") & (pl.col("group") == "Not completed"))
        allm = fm[y].filter(pl.col("module") == "All modules").row(0, named=True)
        ok &= check(f"{y} first missed by module: all-module row equals aq1_first_missed_week_summary.csv",
                    (allm["n"], allm["share_ever"], allm["share_by_week4"], allm["median_first_missed_week"]) ==
                    (summ["n"][0], summ["share_any"][0], summ["share_by_week4"][0], summ["week_median"][0]),
                    f"n {allm['n']}, ever {allm['share_ever']}, week 4 {allm['share_by_week4']}, "
                    f"median {allm['median_first_missed_week']}")
        cum = pl.read_csv(RES / y / "aq1_first_missed_week_cumulative.csv").filter(
            (pl.col("denominator") == "day14_registered") & (pl.col("group") == "Not completed")
            & (pl.col("week") == 8))
        ok &= check(f"{y} first missed by module: week-8 share equals the cumulative file",
                    allm["by_week8_n"] == cum["events"][0], f"{allm['by_week8_n']} vs {cum['events'][0]}")
        ok &= check(f"{y} first missed by module: module n add up", int(fm[y].filter(
            pl.col("module") != "All modules")["n"].sum()) == allm["n"], str(allm["n"]))
        rates = pl.read_csv(RES / y / "aq1_rates.csv").filter(
            (pl.col("level") == "run") & (pl.col("denominator") == "day14_registered")
            & (pl.col("measure") == "non_completion"))
        for row in sm[y].filter(~pl.col("module").str.starts_with("Modules")).iter_rows(named=True):
            for smc, col in [("B", "february"), ("J", "october")]:
                rr = rates.filter(pl.col("group") == f"{row['module']} {y}{smc}")
                ok &= check(f"{y} start month: {row['module']} {y}{smc} equals the run row of aq1_rates.csv",
                            (rr["events"][0], rr["n"][0], rr["rate"][0]) ==
                            (row[f"nc_{col}"], row[f"n_{col}"], row[f"rate_{col}"]),
                            f"{row[f'nc_{col}']}/{row[f'n_{col}']}")

    # --- the three tables as the report shows them --------------------------------------------------------------
    md = ["# T27 appendix tables (written by code/t27_appendix_tables.py)", ""]
    md += ["## AQ2: non-completion by number of early signs at day 27", "",
           "| Runs and signs present | n, 2013 | Non-completion, 2013 | n, 2014 | Non-completion, 2014 |",
           "| :---- | :---- | :---- | :---- | :---- |"]
    for blk, short, maxk in [("runs with a task due by day 27 (five signs)", "Runs with a task due by day 27", 5),
                             ("runs with no task due by day 27 (three click signs)", "Runs with no task due by day 27",
                              3)]:
        for k in range(maxk + 1):
            if all(sc[y].filter((pl.col("block") == blk) & (pl.col("signs_present") == k))["n"][0] == 0
                   for y in YEARS):
                md.append(f"<!-- no enrolment with {k} of {maxk} signs in either year: row left out -->")
                continue
            cells = []
            for y in YEARS:
                r = sc[y].filter((pl.col("block") == blk) & (pl.col("signs_present") == k)).row(0, named=True)
                cells += [n_fmt(r["n"]), pct(r["rate"], r["ci_low"], r["ci_high"]) if r["n"] else "–"]
            md.append(f"| {short}: {k} of {maxk} | " + " | ".join(cells) + " |")
    md += ["", "## AQ1: first missed TMA or CMA of the non-completers by module, day-14 population", "",
           "| Year | Module | n | Missed any task | Missed by week 4 | Missed by week 8 | First missed week, median |",
           "| :---- | :---- | :---- | :---- | :---- | :---- | :---- |"]
    for y in YEARS:
        for r in fm[y].iter_rows(named=True):
            med = r["median_first_missed_week"]
            md.append(f"| {y} | {r['module']} | {n_fmt(r['n'])} | "
                      f"{pct(r['share_ever'], r['ever_ci_low'], r['ever_ci_high'])} | "
                      f"{pct(r['share_by_week4'], r['by_week4_ci_low'], r['by_week4_ci_high'])} | "
                      f"{pct(r['share_by_week8'], r['by_week8_ci_low'], r['by_week8_ci_high'])} | "
                      f"{med:g} |")
    md += ["", "## AQ1: February minus October within module, day-14 population", "",
           "| Year | Module | February start (n) | October start (n) | Difference, points (95% Newcombe interval) |",
           "| :---- | :---- | :---- | :---- | :---- |"]
    for y in YEARS:
        for r in sm[y].iter_rows(named=True):
            md.append(f"| {y} | {r['module']} | {one(r['rate_february'])}% ({n_fmt(r['n_february'])}) | "
                      f"{one(r['rate_october'])}% ({n_fmt(r['n_october'])}) | "
                      f"{pp(r['difference_pp'] / 100, r['difference_ci_low'] / 100, r['difference_ci_high'] / 100)} |")
    (RES / "compare" / "t27_appendix_tables.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print(f"SUMMARY: cross-checks {'all PASS' if ok else 'with FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
