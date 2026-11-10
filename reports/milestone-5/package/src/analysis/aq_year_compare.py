"""AQ1 and AQ2 compared between the 9 runs of 2013 and the 13 runs of 2014, from the prepared views (Change Log C15).

Run after `aq_analysis.py --scope 2013` and `--scope 2014` and `aq1_year_shared_modules.py`. Writes results/compare/:
- aq1_year_comparison_computed.csv: non-completion per year under both denominators (registered at day 14; all
  enrolments) overall, over the six modules that ran in both years, per start month, per shared module and per
  module and start month present in both years, with the 2014 - 2013 difference (Newcombe 95% interval); module CCC
  (2014 only) as its own row without a difference.
- aq1_first_missed_week_by_year.csv: share of the day-14 population with a missed assessed task, the share by week 4
  and the median first missed week, by year and completion group, with the 2014 - 2013 difference of the shares.
- aq1_left_before_day14.csv: share of all enrolments no longer registered at day 14 (left before day 14 or
  registered after it), by year, overall and over the six modules that ran in both years, with the 2014 - 2013
  difference (Newcombe 95% interval); it explains why the year difference changes sign between the two denominators.
- aq2_year_comparison.csv: the mutually adjusted average risk difference of each early sign in 2013 and 2014 (refitted
  here and kept to four decimals), the difference of the two (independent samples; normal interval from the two
  delta-method robust standard errors), modules with the same direction and the verdict in each year.
- aq2_concurrent_2014.csv: the sign "tasks missed in several modules at once" (Change Log C12), described for the
  2014 runs only: among enrolments registered at day 27, those with a missed task by day 27 in this enrolment and in
  at least one other enrolment of the same student in the same presentation, against the rest; unadjusted.
- aq_summary.md: every comparison table in Markdown with one line on what it shows, including the three cross-check
  files written by the 2013 scope of aq_analysis.py and by aq1_year_shared_modules.py (`*_published.csv`).

Usage (from the package folder): python src/analysis/aq_year_compare.py   (run_all.sh step 16)
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import polars as pl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import aq_analysis as A  # noqa: E402

OUT = A.ROOT / "results" / "compare"
Z = A.Z


def load(name: str) -> pl.DataFrame:
    df = pl.read_parquet(A.PROC / f"{name}.parquet")
    assert set(df["year"].unique().to_list()) == {2013, 2014}, name
    return df.with_columns(pl.col("code_presentation").str.slice(4, 1).alias("start_month_code"),
                           pl.col("code_presentation").str.slice(0, 4).alias("yr"))


def year_rows(enr: pl.DataFrame) -> list[dict]:
    shared = sorted(set(enr.filter(pl.col("year") == 2013)["code_module"].unique().to_list()))
    pairs = (enr.group_by("code_module", "start_month_code").agg(pl.col("year").n_unique().alias("k"))
             .filter(pl.col("k") == 2).select("code_module", "start_month_code").sort("code_module", "start_month_code"))
    units = [("overall", "all runs", pl.lit(True)),
             ("shared_modules", f"the {len(shared)} modules run in both years", pl.col("code_module").is_in(shared))]
    units += [("start_month", m, pl.col("start_month_code") == m) for m in ["B", "J"]]
    units += [("module", m, pl.col("code_module") == m) for m in shared]
    units += [("module_start_month", f"{a} {b}", (pl.col("code_module") == a) & (pl.col("start_month_code") == b))
              for a, b in pairs.rows()]
    rows = []
    for den, d in [("day14_registered", enr.filter(pl.col("enrolled_d14"))), ("all_enrolments", enr)]:
        for level, unit, cond in units:
            s = d.filter(cond)
            c = {y: (int(s.filter(pl.col("year") == y)["non_completion"].sum()), s.filter(pl.col("year") == y).height)
                 for y in (2013, 2014)}
            (e13, n13), (e14, n14) = c[2013], c[2014]
            p13, l13, h13 = A.wilson(e13, n13)
            p14, l14, h14 = A.wilson(e14, n14)
            dd, lo, hi = A.newcombe(e14, n14, e13, n13)
            rows.append(dict(level=level, unit=unit, denominator=den, nc_2013=e13, n_2013=n13, rate_2013=A.r(p13),
                             ci_low_2013=A.r(l13), ci_high_2013=A.r(h13), nc_2014=e14, n_2014=n14,
                             rate_2014=A.r(p14), ci_low_2014=A.r(l14), ci_high_2014=A.r(h14),
                             diff_pp_2014_minus_2013=A.r(100 * dd, 2), ci_low_pp=A.r(100 * lo, 2),
                             ci_high_pp=A.r(100 * hi, 2)))
        s = d.filter((pl.col("code_module") == "CCC") & (pl.col("year") == 2014))
        p, lo, hi = A.wilson(int(s["non_completion"].sum()), s.height)
        rows.append(dict(level="module", unit="CCC (2014 only)", denominator=den, nc_2013=None, n_2013=0,
                         rate_2013=None, ci_low_2013=None, ci_high_2013=None, nc_2014=int(s["non_completion"].sum()),
                         n_2014=s.height, rate_2014=A.r(p), ci_low_2014=A.r(lo), ci_high_2014=A.r(hi),
                         diff_pp_2014_minus_2013=None, ci_low_pp=None, ci_high_pp=None))
    return rows


def first_missed(enr: pl.DataFrame) -> list[dict]:
    d = enr.filter(pl.col("enrolled_d14"))
    rows = []
    for grp, cond in [("all", pl.lit(True)), ("Completed", pl.col("completed")),
                      ("Not completed", pl.col("non_completion"))]:
        c = {}
        for y in (2013, 2014):
            s = d.filter(cond & (pl.col("year") == y))
            miss = s["first_missed_week"].drop_nulls()
            c[y] = dict(n=s.height, any=miss.len(), w4=int((s["first_missed_week"] <= 4).sum()),
                        med=float(miss.quantile(0.5, "lower")) if miss.len() else None)
        for y in (2013, 2014):
            x = c[y]
            pa, la, ha = A.wilson(x["any"], x["n"])
            p4, l4, h4 = A.wilson(x["w4"], x["n"])
            row = dict(group=grp, year=y, n=x["n"], with_missed_task=x["any"], share_any=A.r(pa),
                       ci_low_any=A.r(la), ci_high_any=A.r(ha), missed_by_week4=x["w4"], share_by_week4=A.r(p4),
                       ci_low_week4=A.r(l4), ci_high_week4=A.r(h4), median_first_missed_week=x["med"],
                       diff_any_pp=None, diff_any_ci_low=None, diff_any_ci_high=None,
                       diff_week4_pp=None, diff_week4_ci_low=None, diff_week4_ci_high=None)
            if y == 2014:
                a = A.newcombe(c[2014]["any"], c[2014]["n"], c[2013]["any"], c[2013]["n"])
                b = A.newcombe(c[2014]["w4"], c[2014]["n"], c[2013]["w4"], c[2013]["n"])
                row.update(diff_any_pp=A.r(100 * a[0], 2), diff_any_ci_low=A.r(100 * a[1], 2),
                           diff_any_ci_high=A.r(100 * a[2], 2), diff_week4_pp=A.r(100 * b[0], 2),
                           diff_week4_ci_low=A.r(100 * b[1], 2), diff_week4_ci_high=A.r(100 * b[2], 2))
            rows.append(row)
    return rows


def left_before_day14(enr: pl.DataFrame) -> list[dict]:
    shared = sorted(set(enr.filter(pl.col("year") == 2013)["code_module"].unique().to_list()))
    rows = []
    for unit, cond in [("all runs", pl.lit(True)), (f"the {len(shared)} modules run in both years",
                                                     pl.col("code_module").is_in(shared))]:
        c = {}
        for y in (2013, 2014):
            s = enr.filter(cond & (pl.col("year") == y))
            c[y] = (int((~s["enrolled_d14"]).sum()), s.height)
        d, lo, hi = A.newcombe(c[2014][0], c[2014][1], c[2013][0], c[2013][1])
        for y in (2013, 2014):
            p, plo, phi = A.wilson(*c[y])
            rows.append(dict(unit=unit, year=y, n_all=c[y][1], not_registered_day14=c[y][0], share=A.r(p),
                             ci_low=A.r(plo), ci_high=A.r(phi),
                             diff_pp_2014_minus_2013=A.r(100 * d, 2) if y == 2014 else None,
                             diff_ci_low=A.r(100 * lo, 2) if y == 2014 else None,
                             diff_ci_high=A.r(100 * hi, 2) if y == 2014 else None))
    return rows


def exact_ame() -> dict:
    """Mutually adjusted average risk difference per sign and year, refitted here at full precision (the result CSVs
    hold two decimals, which can round a value such as 20.25 the wrong way)."""
    import numpy as np
    out = {}
    for scope in ("2013", "2014"):
        A.set_scope(scope)
        f = A.build_signs(A.load_view("features_d27"))
        m = A.Fit(f, list(A.SIGNS))
        for s in A.SIGNS:
            e, lo, hi, se = m.ame(s, np.where(A.defined_mask(f, s))[0])
            out[(scope, s)] = (100 * e, 100 * lo, 100 * hi, 100 * se)
    A.set_scope("2013")
    return out


def aq2_compare() -> list[dict]:
    a = pl.read_csv(A.ROOT / "results" / "2013" / "aq2_associations.csv")
    b = pl.read_csv(A.ROOT / "results" / "2014" / "aq2_associations.csv")
    ex = exact_ame()
    rows = []
    for s in A.SIGNS:
        x = a.filter(pl.col("sign") == s).row(0, named=True)
        y = b.filter(pl.col("sign") == s).row(0, named=True)
        e13, e14 = ex[("2013", s)], ex[("2014", s)]
        assert abs(A.r(e13[0], 2) - x["rd_adj_mutual_pp"]) < 1e-9 and abs(A.r(e14[0], 2) - y["rd_adj_mutual_pp"]) < 1e-9
        d = e14[0] - e13[0]
        sd = math.sqrt(e13[3] ** 2 + e14[3] ** 2)
        rows.append(dict(sign=s, n_2013=x["n"], rd_2013_pp=A.r(e13[0]), ci_low_2013=A.r(e13[1]),
                         ci_high_2013=A.r(e13[2]),
                         modules_2013=f"{x['modules_same_direction']}/{x['modules_defined']}", verdict_2013=x["verdict"],
                         n_2014=y["n"], rd_2014_pp=A.r(e14[0]), ci_low_2014=A.r(e14[1]), ci_high_2014=A.r(e14[2]),
                         modules_2014=f"{y['modules_same_direction']}/{y['modules_defined']}", verdict_2014=y["verdict"],
                         diff_pp_2014_minus_2013=A.r(d), diff_ci_low=A.r(d - Z * sd), diff_ci_high=A.r(d + Z * sd),
                         rd_unadj_2013_pp=x["rd_unadj_pp"], rd_unadj_2014_pp=y["rd_unadj_pp"]))
    return rows


def concurrent(f27: pl.DataFrame, enr: pl.DataFrame) -> list[dict]:
    keys = ["code_module", "code_presentation", "id_student"]
    f = f27.join(enr.select(*keys, "concurrent_runs"), on=keys, how="left")
    assert f["concurrent_runs"].null_count() == 0
    f = f.with_columns((pl.col("tasks_missed_c") >= 1).alias("missed"))
    f = f.with_columns(pl.col("missed").cast(pl.Int32).sum().over("code_presentation", "id_student").alias("k_missed"),
                       pl.len().over("code_presentation", "id_student").alias("k_d27"))
    f = f.with_columns((pl.col("missed") & (pl.col("k_missed") >= 2)).alias("several"))
    rows = []
    for y in (2013, 2014):
        s = f.filter(pl.col("year") == y)
        rows.append(dict(year=y, population="registered at day 27", group="concurrent enrolment (another enrolment "
                         "in the same presentation, registered at day 27)",
                         n=int((s["k_d27"] >= 2).sum()), non_completers=int(s.filter(pl.col("k_d27") >= 2)["non_completion"].sum()),
                         rate=None, ci_low=None, ci_high=None, rd_pp=None, rd_ci_low=None, rd_ci_high=None))
    s = f.filter(pl.col("year") == 2014)
    for pop, d in [("all 2014 enrolments registered at day 27", s),
                   ("2014 concurrent enrolments registered at day 27", s.filter(pl.col("k_d27") >= 2))]:
        w, wo = d.filter(pl.col("several")), d.filter(~pl.col("several"))
        ew, ewo = int(w["non_completion"].sum()), int(wo["non_completion"].sum())
        for grp, e, n in [("missed tasks in several modules at once", ew, w.height), ("all others", ewo, wo.height)]:
            p, lo, hi = A.wilson(e, n)
            rows.append(dict(year=2014, population=pop, group=grp, n=n, non_completers=e, rate=A.r(p),
                             ci_low=A.r(lo), ci_high=A.r(hi), rd_pp=None, rd_ci_low=None, rd_ci_high=None))
        dd, lo, hi = A.newcombe(ew, w.height, ewo, wo.height)
        rows[-2].update(rd_pp=A.r(100 * dd, 2), rd_ci_low=A.r(100 * lo, 2), rd_ci_high=A.r(100 * hi, 2))
    return rows


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    enr = load("enrolment")
    f27 = load("features_d27")
    for name, rows in [("aq1_year_comparison_computed.csv", year_rows(enr)),
                       ("aq1_first_missed_week_by_year.csv", first_missed(enr)),
                       ("aq1_left_before_day14.csv", left_before_day14(enr)),
                       ("aq2_year_comparison.csv", aq2_compare()),
                       ("aq2_concurrent_2014.csv", concurrent(f27, enr))]:
        df = pl.DataFrame(rows, infer_schema_length=None)
        df.write_csv(OUT / name)
        with pl.Config(tbl_rows=-1, tbl_cols=-1, tbl_width_chars=250, fmt_str_lengths=60):
            print(f"== {name}\n{df}")
    summary()
    print(f"Results written to {OUT.relative_to(A.ROOT)}")


DESCRIBE = [
    ("aq1_year_comparison_computed.csv", "AQ1. Non-completion by year under both denominators, computed from the prepared "
     "views of each year, with the 2014 − 2013 difference (points, 95% Newcombe interval); module CCC ran only in 2014."),
    ("aq1_left_before_day14.csv", "AQ1. Share of all enrolments not registered at day 14, by year, with the 2014 − 2013 "
     "difference; it explains why the year difference changes sign between the two denominators."),
    ("aq1_first_missed_week_by_year.csv", "AQ1. Share of the day-14 population with a missed assessed task and with one by "
     "week 4, and the median first missed week, by year and completion group."),
    ("aq2_year_comparison.csv", "AQ2. Mutually adjusted average risk difference of each early sign in 2013 and 2014 "
     "(points, four decimals), the 2014 − 2013 difference with its 95% interval, module direction and verdict."),
    ("aq2_concurrent_2014.csv", "AQ2. The sign 'tasks missed in several modules at once', described on the 2014 runs "
     "only (Change Log C12), unadjusted; with the count of concurrent enrolments in each year."),
    ("aq1_year_comparison_published.csv", "Cross-check. Outcome shares by year over all enrolments, 2013 computed and 2014 "
     "as the per-run counts Milestone 3 published (written by the 2013 scope of aq_analysis.py); the computed 2014 counts "
     "equal these cell by cell."),
    ("aq1_year_difference_published.csv", "Cross-check. The 2014 − 2013 difference over all enrolments from the published "
     "2014 counts; equal to the all-enrolment rows of aq1_year_comparison_computed.csv."),
    ("aq1_year_shared_modules_published.csv", "Cross-check. The same difference restricted to the six modules that ran in "
     "both years, from the published counts (Wald interval)."),
]


def summary() -> None:
    """compare/aq_summary.md: every comparison table in Markdown, one line each on what it shows."""
    parts = ["# Comparisons between 2013 and 2014\n",
             "Written by `src/analysis/aq_year_compare.py` (and, for the three cross-check files, by the 2013 scope of "
             "`src/analysis/aq_analysis.py` and by `src/analysis/aq1_year_shared_modules.py`). Rates carry 95% Wilson "
             "intervals and differences of two rates 95% Newcombe intervals unless a line says otherwise. Methods: "
             "`results/README.md`.\n"]
    for name, text in DESCRIBE:
        parts.append(f"**`{name}`.** {text}\n")
        parts.append(A.md_table(pl.read_csv(OUT / name, infer_schema_length=None)) + "\n")
    (OUT / "aq_summary.md").write_text("\n".join(parts), encoding="utf-8")


if __name__ == "__main__":
    main()
