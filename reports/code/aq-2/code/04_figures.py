"""AQ2 step 4 – figures. Every number in a title or source line is read from the result tables (PROTOCOL.md P23)."""

import polars as pl

from aq2_model import ACTIVITY_LEVELS5, FIGURES, RESULTS, SIGNS, lib

import chart_style as cs  # noqa: E402  (data-analyst skill; its folder is put on the path by lib)

lib.open_test_outcomes("aq-2/code/04_figures.py", "AQ2 figures including the 2014 replication")
cs.apply()
a = pl.read_csv(RESULTS / "associations_2013.csv")
labels = [SIGNS[s] for s in a["sign"].to_list()]
top = a.sort("adjusted_rd", descending=True).row(0, named=True)
ns = sorted(set(a["n_support"].to_list()), reverse=True)
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
cs.title(ax, f"A missed task goes with a {top['adjusted_rd'] * 100:.0f}-point higher non-completion risk among otherwise similar students",
         "Risk difference in non-completion, students with the sign minus students without it, 95% interval")
cs.source(fig, f"9 runs of 2013, enrolments registered at day 27 (click signs: n = {ns[0]:,}; task signs: runs with a TMA due, n = {ns[-1]:,}). Association, not cause.")
cs.save(fig, FIGURES / "fig-aq2-1-risk-differences")

# ---- replication: both years with their intervals -----------------------------------------------------
rep = pl.read_csv(RESULTS / "replication.csv")
fig, ax = cs.figure(8.2, 4.4)
for y, r in zip(ys, rep.iter_rows(named=True)):
    ax.plot([r["adj_ci_low"], r["adj_ci_high"]], [y + 0.14, y + 0.14], color=cs.NEUTRAL, linewidth=2.2, solid_capstyle="round")
    ax.plot(r["adjusted_rd"], y + 0.14, "o", color=cs.NEUTRAL, markersize=6)
    ax.plot([r["adj_ci_low_2014"], r["adj_ci_high_2014"]], [y - 0.14, y - 0.14], color=cs.ACCENT, linewidth=2.2, solid_capstyle="round")
    ax.plot(r["adjusted_rd_2014"], y - 0.14, "o", color=cs.ACCENT, markersize=7)
    ax.annotate(f"{r['adjusted_rd_2014'] * 100:+.1f}", (r["adj_ci_high_2014"], y - 0.14), xytext=(6, 0), textcoords="offset points", va="center", fontsize=9.5, color=cs.ACCENT)
    ax.annotate(f"{r['adjusted_rd'] * 100:+.1f}", (r["adj_ci_high"], y + 0.14), xytext=(6, 0), textcoords="offset points", va="center", fontsize=9, color=cs.NEUTRAL_DARK)
ax.set_yticks(ys, rep["label"].to_list()); ax.tick_params(axis="y", length=0); ax.grid(axis="y", visible=False); ax.grid(axis="x", visible=True)
ax.axvline(0.05, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
cs.percent_axis(ax, "x"); ax.set_xlim(0, 0.5)
ax.plot([], [], "o", color=cs.NEUTRAL, label="2013 runs (estimation)"); ax.plot([], [], "o", color=cs.ACCENT, label="2014 runs (replication)")
ax.legend(loc="lower right", fontsize=9, frameon=False)
same = int(rep["change_interval_includes_0"].sum())
biggest = rep.sort(pl.col("change_2014_minus_2013").abs(), descending=True).row(0, named=True)
cs.title(ax, f"All {int(rep['same_verdict'].sum())} associations reappear in the 2014 runs; no sign moves by more than {abs(biggest['change_2014_minus_2013']) * 100:.1f} points"
         if same == rep.height else f"{same} of {rep.height} associations are unchanged in the 2014 runs within their intervals",
         "Adjusted risk difference per sign with 95% interval, estimated on 2013 and re-estimated on 2014")
tma = rep.filter(pl.col("sign") == "sign_tma_late").row(0, named=True)
cs.source(fig, f"Each estimate averages over the runs where the sign can occur: late TMA n = {tma['n_support']:,} (2013) and {tma['n_support_2014']:,} (2014, "
               f"without CCC, which has no TMA due by day 27). Dashed line = 5-point criterion.")
cs.save(fig, FIGURES / "fig-aq2-2-replication")

# ---- binned residuals by five activity levels: the main model and the post hoc model -------------------------
fig, axes = cs.plt.subplots(1, 2, figsize=(9.2, 4.4), sharey=True)
fig.subplots_adjust(top=0.78, bottom=0.2, wspace=0.08)
short = ["No click", "Below half\nthe median", "Half to\nthe median", "Median to\ntwice", "Twice the\nmedian or more"]
main_name, post_name = "main model (low activity = below half the run median)", "post hoc: main model + log(1 + clicks on days 0-27)"
outside = {}
for ax, scope in zip(axes, ("2013", "2014")):
    r5 = pl.read_csv(RESULTS / f"binned_residuals_activity5_{scope}.csv")
    for name, color, dx in ((main_name, cs.ACCENT, -0.12), (post_name, cs.ACCENT_2, 0.12)):
        t = r5.filter(pl.col("model") == name).sort("activity_level5")
        assert t["activity_level5"].to_list() == ACTIVITY_LEVELS5
        xs = [i + dx for i in range(5)]
        ax.errorbar(xs, t["residual"].to_list(), yerr=t["two_se"].to_list(), fmt="o", color=color, markersize=6, capsize=3, linewidth=1.6)
        outside[(scope, name)] = int(t["outside_2se"].sum())
    ax.axhline(0, color=cs.NEUTRAL_DARK, linewidth=1)
    ax.set_xticks(range(5), short, fontsize=8.5)
    ax.set_title(f"{scope} runs", loc="left", fontsize=10.5, color=cs.NEUTRAL_DARK)
    ax.grid(axis="x", visible=False)
cs.percent_axis(axes[0], "y")
axes[0].set_ylabel("Observed minus predicted non-completion")
axes[1].plot([], [], "o", color=cs.ACCENT, label="Main model (five yes/no signs)"); axes[1].plot([], [], "o", color=cs.ACCENT_2, label="Post hoc: plus log(1 + clicks)")
axes[0].legend(handles=axes[1].get_legend_handles_labels()[0], labels=axes[1].get_legend_handles_labels()[1], loc="lower left", fontsize=8.5, frameon=False)
cs.title(axes[0], f"The yes/no activity signs miss a graded effect: {outside[('2013', main_name)]} of 5 activity levels misfit in 2013 and {outside[('2014', main_name)]} of 5 in 2014",
         "Binned residuals by activity level on days 0-27; bars = ±2 standard errors; a bar that does not cross 0 is a misfit")
cs.source(fig, f"With clicks as a continuous adjustment (added after seeing the misfit): {outside[('2013', post_name)]} of 5 levels misfit in 2013, {outside[('2014', post_name)]} of 5 in 2014.")
cs.save(fig, FIGURES / "fig-aq2-3-residuals-by-activity")
print("figures written to aq-2/figures/")
