"""AQ1 step 4 – figures (house style of the data-analyst skill: claim titles, direct labels, PNG + SVG)."""

import polars as pl

from aq1_common import FIGURES, RESULTS, lib

import chart_style as cs  # noqa: E402  (data-analyst skill; its folder is put on the path by lib)

lib.open_test_outcomes("aq-1/code/04_figures.py", "AQ1 figures for all 22 runs")
cs.apply()
r = pl.read_csv(RESULTS / "rates_all.csv")
runs = r.filter(pl.col("level") == "run").sort("rate", descending=True)
pooled = r.filter(pl.col("level") == "pooled")["rate"][0]
fig, ax = cs.figure(7.8, 7.2)
cs.intervals(ax, runs["group"].to_list(), runs["rate"].to_list(), runs["ci_low"].to_list(), runs["ci_high"].to_list(),
             highlight=[g for g in runs["group"].to_list() if g.startswith(("CCC", "DDD"))], fmt="{:.0%}", reference=pooled)
cs.percent_axis(ax, "x")
cs.title(ax, "Non-completion ranges from 25% to 58% across runs; CCC and DDD runs lose the most students",
         f"Share of enrolments ending in Fail or Withdrawn, Wilson 95% interval; dashed line = pooled {pooled:.1%}")
cs.source(fig, "OULAD-N04-prepared-1.0, 22 runs, 28,061 enrolments still registered at day 14")
cs.save(fig, FIGURES / "fig-aq1-1-non-completion-by-run")

c = pl.read_csv(RESULTS / "first_missed_task_cumulative_all.csv").filter(pl.col("week") <= 36)
weeks = sorted(c["week"].unique().to_list())
series = {g: c.filter(pl.col("group") == g).sort("week")["cumulative_share"].to_list() for g in sorted(c["group"].unique().to_list(), reverse=True)}
fig, ax = cs.figure(7.8, 4.4)
cs.lines(ax, weeks, series, highlight="Non-completers (Fail or Withdrawn)", fmt="{:.0%}")
cs.percent_axis(ax, "y")
ax.axvline(4, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
ax.annotate("day-27 cut-off\n(end of week 4)", (4, 0.72), xytext=(6, 0), textcoords="offset points", fontsize=9, color=cs.NEUTRAL_DARK)
ax.set_xlabel("Week of the run")
cs.title(ax, "By week 4 only one non-completer in six has missed a task",
         "Cumulative share of enrolments with a first assessed task due and not submitted, by final outcome")
cs.source(fig, "OULAD-N04-prepared-1.0, 22 runs, KPI population; tasks = TMA and CMA due while enrolled")
cs.save(fig, FIGURES / "fig-aq1-2-first-missed-task")
print("figures written to aq-1/figures/")
