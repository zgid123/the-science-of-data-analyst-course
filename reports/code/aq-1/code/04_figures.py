"""AQ1 step 4 – figures (house style of the data-analyst skill: claim titles, direct labels, PNG + SVG).

Every number in a title or source line is read from the result tables (PROTOCOL.md P23).
"""

import polars as pl

from aq1_common import FIGURES, RESULTS, lib

import chart_style as cs  # noqa: E402  (data-analyst skill; its folder is put on the path by lib)

lib.open_test_outcomes("aq-1/code/04_figures.py", "AQ1 figures for all 22 runs")
cs.apply()
r = pl.read_csv(RESULTS / "rates_all.csv")
runs = r.filter(pl.col("level") == "run").sort("rate", descending=True)
pooled = r.filter(pl.col("level") == "pooled").row(0, named=True)
top2 = r.filter(pl.col("level") == "module").sort("rate", descending=True)["group"].head(2).to_list()
fig, ax = cs.figure(7.8, 7.2)
cs.intervals(ax, runs["group"].to_list(), runs["rate"].to_list(), runs["ci_low"].to_list(), runs["ci_high"].to_list(),
             highlight=[g for g in runs["group"].to_list() if g.startswith(tuple(top2))], fmt="{:.0%}", reference=pooled["rate"])
cs.percent_axis(ax, "x")
cs.title(ax, f"Non-completion ranges from {runs['rate'].min():.0%} to {runs['rate'].max():.0%} across runs; {top2[0]} and {top2[1]} lose the most students",
         f"Share of enrolments ending in Fail or Withdrawn, Wilson 95% interval; dashed line = pooled {pooled['rate']:.1%}")
cs.source(fig, f"OULAD-N04-prepared-1.0, {runs.height} runs, {pooled['enrolments']:,} enrolments still registered at day 14")
cs.save(fig, FIGURES / "fig-aq1-1-non-completion-by-run")

c = pl.read_csv(RESULTS / "first_missed_task_cumulative_all.csv").filter(pl.col("week") <= 36)
weeks = sorted(c["week"].unique().to_list())
series = {g: c.filter(pl.col("group") == g).sort("week")["cumulative_share"].to_list() for g in sorted(c["group"].unique().to_list(), reverse=True)}
w4 = pl.read_csv(RESULTS / "first_missed_by_week4_all.csv").filter((pl.col("year") == "both years") & pl.col("group").str.starts_with("Non-completers"))
a4 = w4.filter(pl.col("population") == "all runs").row(0, named=True)
t4 = w4.filter(pl.col("population") != "all runs").row(0, named=True)
fig, ax = cs.figure(7.8, 4.4)
cs.lines(ax, weeks, series, highlight="Non-completers (Fail or Withdrawn)", fmt="{:.0%}")
cs.percent_axis(ax, "y")
ax.axvline(4, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
ax.annotate("day-27 cut-off\n(end of week 4)", (4, 0.72), xytext=(6, 0), textcoords="offset points", fontsize=9, color=cs.NEUTRAL_DARK)
ax.set_xlabel("Week of the run")
cs.title(ax, f"By week 4 only {a4['share']:.0%} of non-completers have missed a task",
         "Cumulative share of enrolments with a first assessed task due and not submitted, by final outcome")
cs.source(fig, f"OULAD-N04-prepared-1.0, 22 runs, KPI population; tasks = TMA and CMA due while enrolled. "
               f"In the {t4['runs']} runs with a task due by day 27 the week-4 share is {t4['share']:.0%}.")
cs.save(fig, FIGURES / "fig-aq1-2-first-missed-task")

# ---- year comparison: the difference under the two denominators -----------------------------------------
yc = pl.read_csv(RESULTS / "year_comparison_all.csv").filter((pl.col("level") == "overall") & pl.col("method").str.starts_with("pooled"))
short = {"registered at day 14 (KPI population)": "registered at day 14", "all enrolments": "all enrolments"}
labels, est, lo, hi = [], [], [], []
for row in yc.iter_rows(named=True):
    labels.append(f"{row['scope'].split(' (')[0].replace(' x ', ' × ')}\n{short[row['denominator']]}")
    est.append(row["difference_2014_minus_2013"]); lo.append(row["ci_low"]); hi.append(row["ci_high"])
kpi6 = yc.filter(pl.col("denominator").str.starts_with("registered") & pl.col("scope").str.contains("modules run in both years")).row(0, named=True)
all6 = yc.filter((pl.col("denominator") == "all enrolments") & pl.col("scope").str.contains("modules run in both years")).row(0, named=True)


def phrase(row: dict) -> str:
    d = row["difference_2014_minus_2013"] * 100
    if not row["interval_excludes_0"]:
        return f"no difference the data can show ({d:+.1f} points)"
    return f"{abs(d):.1f} points {'lower' if d < 0 else 'higher'} in 2014"


fig, ax = cs.figure(8.4, 4.8)
cs.intervals(ax, labels, est, lo, hi, highlight=[l for l in labels if "registered" in l], fmt="{:+.1%}", reference=0.0)
cs.percent_axis(ax, "x", decimals=0)
cs.title(ax, f"Same modules, students registered at day 14: {phrase(kpi6)}; all enrolments: {phrase(all6)}",
         "Non-completion in 2014 minus 2013, percentage points, Newcombe 95% interval")
cs.source(fig, f"OULAD-N04-prepared-1.0. Six modules ran in both years (CCC only in 2014). 2013: {kpi6['n_2013']:,} registered at day 14 of "
               f"{all6['n_2013']:,} enrolments; 2014, same modules: {kpi6['n_2014']:,} of {all6['n_2014']:,}.")
cs.save(fig, FIGURES / "fig-aq1-3-year-difference")
print("figures written to aq-1/figures/")
print(f"title of figure 3: Same modules, students registered at day 14: {phrase(kpi6)}; all enrolments: {phrase(all6)}")
