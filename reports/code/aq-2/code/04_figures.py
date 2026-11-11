"""AQ2 step 4 – figures."""

import matplotlib.pyplot as plt
import polars as pl

from aq2_model import FIGURES, RESULTS, SIGNS, lib

import chart_style as cs  # noqa: E402  (data-analyst skill; its folder is put on the path by lib)

lib.open_test_outcomes("aq-2/code/04_figures.py", "AQ2 figures including the 2014 replication")
cs.apply()
a = pl.read_csv(RESULTS / "associations_2013.csv")
labels = [SIGNS[s] for s in a["sign"].to_list()]
fig, ax = cs.figure(8.2, 4.4)
ys = list(range(len(labels)))[::-1]
for y, r in zip(ys, a.iter_rows(named=True)):
    ax.plot([r["unadj_ci_low"], r["unadj_ci_high"]], [y + 0.14, y + 0.14], color=cs.NEUTRAL, linewidth=2.2, solid_capstyle="round")
    ax.plot(r["unadjusted_rd"], y + 0.14, "o", color=cs.NEUTRAL, markersize=6)
    ax.plot([r["adj_ci_low"], r["adj_ci_high"]], [y - 0.14, y - 0.14], color=cs.ACCENT, linewidth=2.2, solid_capstyle="round")
    ax.plot(r["adjusted_rd"], y - 0.14, "o", color=cs.ACCENT, markersize=7)
    ax.annotate(f"{r['adjusted_rd'] * 100:+.0f} pts", (r["adj_ci_high"], y - 0.14), xytext=(6, 0), textcoords="offset points", va="center", fontsize=9.5, color=cs.ACCENT)
    ax.annotate(f"{r['unadjusted_rd'] * 100:+.0f}", (r["unadj_ci_high"], y + 0.14), xytext=(6, 0), textcoords="offset points", va="center", fontsize=9, color=cs.NEUTRAL_DARK)
ax.set_yticks(ys, labels); ax.tick_params(axis="y", length=0); ax.grid(axis="y", visible=False); ax.grid(axis="x", visible=True)
ax.axvline(0.05, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
ax.annotate("5-point criterion", (0.05, len(labels) - 0.45), xytext=(4, 0), textcoords="offset points", fontsize=8.5, color=cs.NEUTRAL_DARK)
cs.percent_axis(ax, "x"); ax.set_xlim(0, 0.6)
ax.plot([], [], "o", color=cs.NEUTRAL, label="Unadjusted difference"); ax.plot([], [], "o", color=cs.ACCENT, label="Adjusted within run, for the other signs")
ax.legend(loc="lower right", fontsize=9, frameon=False)
cs.title(ax, "A missed task goes with a 41-point higher non-completion risk, even among otherwise similar students",
         "Risk difference in non-completion, students with the sign minus students without it, 95% interval")
cs.source(fig, "9 runs of 2013, enrolments registered at day 27 (n = 11,811; task signs: 7 runs with a task due, n = 9,960). Association, not cause.")
cs.save(fig, FIGURES / "fig-aq2-1-risk-differences")

rep = pl.read_csv(RESULTS / "replication.csv")
fig, ax = cs.figure(8.2, 4.2)
cs.dumbbell(ax, rep["label"].to_list(), rep["adjusted_rd"].to_list(), rep["adjusted_rd_2014"].to_list(), names=("2013 runs (estimation)", "2014 runs (replication)"), fmt="{:.0%}")
cs.percent_axis(ax, "x"); ax.set_xlim(0, 0.5); ax.axvline(0.05, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
cs.title(ax, "All five associations reappear in the 2014 runs; the late-TMA gap is 5 points smaller",
         "Adjusted risk difference per sign, estimated on 2013 and re-estimated on 2014 after the AQ3 test")
cs.source(fig, "2013: 9 runs, n = 11,811. 2014: 13 runs including module CCC, n = 15,724. Dashed line = 5-point criterion.")
cs.save(fig, FIGURES / "fig-aq2-2-replication")
print("figures written to aq-2/figures/")
