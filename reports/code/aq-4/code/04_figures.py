"""AQ4 step 4 – figures."""

import polars as pl

from aq4_common import FIGURES, RESULTS, lib

import chart_style as cs  # noqa: E402  (data-analyst skill; its folder is put on the path by lib)

lib.open_test_outcomes("aq-4/code/04_figures.py", "AQ4 figures")
cs.apply()
q = pl.read_csv(RESULTS / "list_quality_pooled.csv").filter(pl.col("cutoff") == 27)
fig, ax = cs.figure(7.8, 4.0)
labels, vals = [], []
for per20 in (3, 5):
    for name, lab in (("random (expected)", "random list"), ("rule", "rule-ranked list"), ("model", "model list")):
        r = q.filter((pl.col("per20") == per20) & (pl.col("ranking") == name)).row(0, named=True)
        labels.append(f"{per20} per 20 – {lab}"); vals.append(r["recall"])
    labels.append(f"{per20} per 20 – best possible list"); vals.append(r["attainable_recall"])
cs.bar(ax, labels, vals, highlight=["3 per 20 – model list", "5 per 20 – model list"], fmt="{:.1%}", sort=False)
cs.percent_axis(ax, "x"); ax.set_xlim(0, 0.7)
cs.title(ax, "A list of 5 per 20 reaches 42% of later non-completers; no list of that length can reach more than 57%",
         "Recall at day 27: share of the test runs' 6,911 non-completers who are on the list")
cs.source(fig, "13 runs of 2014, 15,724 enrolments; a random list reaches as many as its share of the run")
cs.save(fig, FIGURES / "fig-aq4-1-recall-at-capacity")

t = pl.read_csv(RESULTS / "tiers.csv").filter(pl.col("ranking") == "model")
order = ["tier 1 (top 3 per 20)", "tier 2 (next 2 per 20)", "not listed"]
fig, ax = cs.figure(7.0, 3.2)
cs.bar(ax, order, [t.filter(pl.col("tier") == o)["non_completion_rate"][0] for o in order], highlight="tier 1 (top 3 per 20)", fmt="{:.0%}", sort=False)
cs.percent_axis(ax, "x"); ax.set_xlim(0, 1)
cs.title(ax, "Eight in ten students in the first tier did not complete, six in ten in the second", "Non-completion rate by tier of the model list, day 27")
cs.source(fig, "13 runs of 2014; tier sizes 2,373 and 1,582 enrolments; 11,769 not listed")
cs.save(fig, FIGURES / "fig-aq4-2-tiers")

f = pl.read_csv(RESULTS / "fairness_confirmatory.csv").filter(pl.col("ranking") == "model")
fig, ax = cs.figure(7.8, 3.6)
cs.intervals(ax, f["group"].to_list(), f["gap"].to_list(), f["boot_ci95_low"].to_list(), f["boot_ci95_high"].to_list(), highlight="Age 55 or over", fmt="{:+.1%}", reference=0.0)
ax.axvline(-0.10, color=cs.ACCENT_2, linestyle="--", linewidth=1.2)
ax.annotate("−10-point review line", (-0.10, 1.5), xytext=(4, 0), textcoords="offset points", fontsize=8.5, color=cs.ACCENT_2)
cs.percent_axis(ax, "x")
cs.title(ax, "No audited group is flagged; the two small groups are listed less often and stay uncertain",
         "Recall at capacity of each group minus that of all other students (percentage points), 95% bootstrap interval, day 27, 5 per 20")
cs.source(fig, "13 runs of 2014. Confirmatory groups: disability (803 non-completers), band 0–10% (787), band missing (181). Age 55+: 42 non-completers, not cleared.")
cs.save(fig, FIGURES / "fig-aq4-3-fairness-gaps")
print("figures written to aq-4/figures/")
