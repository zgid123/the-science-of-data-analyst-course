"""AQ3 step 11 – figures."""

import numpy as np
import polars as pl

from aq3_models import FIGURES, RESULTS, lib

import chart_style as cs  # noqa: E402  (data-analyst skill; its folder is put on the path by lib)

lib.open_test_outcomes("aq-3/code/11_figures.py", "AQ3 figures of the test results")
cs.apply()
pool = pl.read_csv(RESULTS / "test_pooled.csv").filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
val = {r["ranking"]: r["pooled_normalised_recall"] for r in pool.iter_rows(named=True)}
rand = pool["random_list_normalised_recall"][0]
labels = ["Random list (expected)", "Background-only model", "Early-sign rule, ranked", "Logistic regression (M1, chosen)", "Boosted trees (M3)"]
vals = [rand, val["B3"], val["B2_rule"], val["M1"], val["M3"]]
fig, ax = cs.figure(7.8, 3.9)
cs.bar(ax, labels, vals, highlight="Logistic regression (M1, chosen)", fmt="{:.1%}", sort=False)
cs.percent_axis(ax, "x"); ax.set_xlim(0, 1)
cs.title(ax, "The model's lists hold 73% of the non-completers a perfect list could hold; the simple rule holds 70%",
         "Pooled normalised recall at day 27, 5 contacts per tutor group of 20 (3,955 list places)")
cs.source(fig, "Test: 13 runs of 2014, 15,724 enrolments, models frozen on the 9 runs of 2013 before the test")
cs.save(fig, FIGURES / "fig-aq3-1-pooled-normalised-recall")

pr = pl.read_csv(RESULTS / "s1_gate_per_run.csv").sort("difference", descending=True)
fig, ax = cs.figure(7.8, 5.2)
cs.dumbbell(ax, pr["run"].to_list(), pr["nr_b"].to_list(), pr["nr_a"].to_list(), names=("Rule-ranked list", "Model M1"), fmt="{:.0%}")
cs.percent_axis(ax, "x")
cs.title(ax, "The model beats the rule in 11 of 13 test runs, by 1 to 7 points; it loses both GGG runs",
         "Normalised recall per test run, day 27, 5 per 20")
cs.source(fig, "13 runs of 2014; sorted by the model's gain over the rule")
cs.save(fig, FIGURES / "fig-aq3-2-per-run")

b = pl.read_csv(RESULTS / "s1_bootstrap.csv")["difference"].to_numpy()
s1 = pl.read_csv(RESULTS / "s1_gate.csv").row(0, named=True)
fig, ax = cs.figure(7.8, 3.8)
ax.hist(b, bins=50, color=cs.NEUTRAL, edgecolor="white")
for x, c, ls in [(s1["boot_ci_low"], cs.ACCENT, "-"), (s1["boot_ci_high"], cs.ACCENT, "-"), (0, cs.INK, "--")]:
    ax.axvline(x, color=c, linestyle=ls, linewidth=1.6)
ax.annotate(f"95% interval\n{s1['boot_ci_low']:+.3f} to {s1['boot_ci_high']:+.3f}", (s1["boot_ci_high"], ax.get_ylim()[1] * 0.85), xytext=(6, 0), textcoords="offset points", fontsize=9, color=cs.ACCENT)
ax.set_xlabel("Model − rule, pooled normalised recall"); ax.set_ylabel("Bootstrap replicates")
cs.title(ax, "The gain over the rule is small but its interval stays above zero",
         f"Paired two-level bootstrap (runs, then enrolments), 2,000 replicates; point estimate {s1['difference']:+.3f}")
cs.source(fig, "13 test runs of 2014, day 27, 5 per 20")
cs.save(fig, FIGURES / "fig-aq3-3-bootstrap-difference")

bins = pl.read_csv(RESULTS / "calibration_bins.csv")
fig, ax = cs.figure(5.6, 5.0)
ax.plot([0, 1], [0, 1], color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
ax.plot(bins["mean_predicted"], bins["observed_rate"], "-o", color=cs.ACCENT)
ax.set_xlabel("Predicted risk (mean of the bin)"); ax.set_ylabel("Observed non-completion"); cs.percent_axis(ax, "x"); cs.percent_axis(ax, "y")
ax.grid(axis="x", visible=True)
cs.title(ax, "Low predicted risks run 5 points too low", "Observed against predicted risk in tenths, frozen M1, day 27")
cs.source(fig, "13 test runs of 2014, n = 15,724; no recalibration")
cs.save(fig, FIGURES / "fig-aq3-4-calibration")

cr = pl.read_csv(RESULTS / "calibration_by_run.csv").sort("citl", descending=True)
fig, ax = cs.figure(7.8, 4.8)
cs.bar(ax, cr["run"].to_list(), cr["citl"].to_list(), highlight=[r for r in cr["run"].to_list() if r.startswith("CCC")], fmt="{:+.2f}", sort=False)
ax.axvline(0.2, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1); ax.axvline(-0.2, color=cs.NEUTRAL_DARK, linestyle="--", linewidth=1)
cs.title(ax, "Risks are far too low in module CCC, which the model never saw", "Calibration-in-the-large per test run (0 = right on average; dashed lines = the ±0.2 bounds of S3)")
cs.source(fig, "Frozen M1, day 27; CCC has no 2013 run, so it receives the average module effect")
cs.save(fig, FIGURES / "fig-aq3-5-calibration-by-run")
print("figures written to aq-3/figures/")
