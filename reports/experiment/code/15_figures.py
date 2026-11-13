"""Report figures. Every number in a title is read from a result table, so a chart cannot state a number the
tables do not hold."""

import _tools  # noqa: F401
import chart_style as cs
import numpy as np
import pandas as pd

import common as c

cs.apply()
R = c.RESULTS
SRC = "Source: OULAD (Kuzilek et al., 2017), prepared dataset OULAD-N04-prepared-1.0; team N04 analysis."
pct = lambda v, d=0: f"{100 * v:.{d}f}%"  # noqa: E731

# ---------------------------------------------------------------- AQ1: when non-completers leave
ex = pd.read_csv(R / "aq1_exit_timing.csv")
late = ex[ex["band"].isin(["Withdrew days 28–90", "Withdrew after day 90", "Failed at the end of the run"])]
share_late = late["non_completers"].sum() / ex["non_completers"].sum()
fig, ax = cs.figure(8, 4.4)
labels = ex["band"].str.replace(r" \(.*\)", "", regex=True).tolist()
cs.bar(ax, labels[::-1], ex["share"].tolist()[::-1], highlight=late["band"].str.replace(r" \(.*\)", "", regex=True).tolist(),
       fmt="{:.0%}", sort=False)
cs.percent_axis(ax, "x")
cs.title(ax, f"{pct(share_late)} of non-completers are still enrolled when the week-5 list goes out",
         f"When the {ex['non_completers'].sum():,} non-completers of all 32,593 enrolments left; blue = still reachable after day 27")
cs.source(fig, SRC)
cs.save(fig, c.FIGURES / "fig1_aq1_exit_timing")

# ---------------------------------------------------------------- AQ1: February against October, same module
gap = pd.read_csv(R / "aq1_start_month_gap.csv")
clear = gap[gap["low"] > 0]
fig, ax = cs.figure(7.5, 4.0)
fig.subplots_adjust(bottom=0.22)
cs.intervals(ax, gap["module"].tolist(), (gap["difference"] * 100).tolist(), (gap["low"] * 100).tolist(),
             (gap["high"] * 100).tolist(), fmt="{:+.1f}", reference=0.0)
ax.set_xlabel("February minus October non-completion, percentage points (95% interval)")
cs.title(ax, f"In {len(clear)} of {len(gap)} modules, February runs lose {clear['difference'].min()*100:.0f} to {clear['difference'].max()*100:.0f} points more students than October runs",
         "Students still registered at day 14, both years pooled; modules that run in both start months")
cs.source(fig, SRC)
cs.save(fig, c.FIGURES / "fig2_aq1_start_month")

# ---------------------------------------------------------------- AQ2: adjusted risk differences, both years
rep = pd.read_csv(R / "aq2_replication.csv")
fig, ax = cs.figure(8, 4.4)
ys = np.arange(len(rep))[::-1]
for off, yr, col in [(0.15, "2013", cs.NEUTRAL), (-0.15, "2014", cs.ACCENT)]:
    for y, (_, r) in zip(ys, rep.iterrows()):
        ax.plot([r[f"low_{yr}"] * 100, r[f"high_{yr}"] * 100], [y + off] * 2, color=col, lw=2.2)
        ax.plot(r[f"rd_{yr}"] * 100, y + off, "o", color=col, ms=7)
        ax.annotate(f"{r[f'rd_{yr}']*100:+.1f}", (r[f"high_{yr}"] * 100, y + off), xytext=(5, 0),
                    textcoords="offset points", va="center", fontsize=9, color=col)
ax.set_yticks(ys, rep["label"])
ax.axvline(5, color=cs.NEUTRAL_DARK, lw=1, ls="--")
ax.text(5.3, ys[0] + 0.45, "5-point criterion", fontsize=8.5, color=cs.NEUTRAL_DARK)
ax.set_xlim(0, 50)
ax.set_xlabel("Adjusted risk difference, percentage points (95% interval); grey = 2013, blue = 2014")
top = rep.iloc[rep["rd_2014"].idxmax()]
cs.title(ax, f"A missed task goes with {top['rd_2013']*100:.0f} points more non-completion; all five signs hold in both years",
         "Within module run, adjusted for the other signs, previous attempts and credits; students registered at day 27")
cs.source(fig, SRC + " Association, not cause.")
cs.save(fig, c.FIGURES / "fig3_aq2_signs")

# ---------------------------------------------------------------- AQ2: signs stack
st = {y: pd.read_csv(R / f"aq2_sign_count_{y}.csv") for y in (2013, 2014)}
fig, ax = cs.figure(7.5, 4.2)
for y, col in [(2013, cs.NEUTRAL), (2014, cs.ACCENT)]:
    d = st[y]
    ax.errorbar(d["n_signs"] + (0.06 if y == 2014 else -0.06), d["rate"], yerr=[d["rate"] - d["low"], d["high"] - d["rate"]],
                fmt="o-", color=col, lw=2, ms=6, capsize=0)
    ax.annotate(str(y), (d["n_signs"].iloc[0], d["rate"].iloc[0]), xytext=(-14, 12 if y == 2013 else -14),
                textcoords="offset points", color=col, va="center", fontsize=9.5)
ax.set_xticks(range(0, int(max(st[2013]["n_signs"].max(), st[2014]["n_signs"].max())) + 1))
ax.set_xlabel("Number of the five signs present at day 27")
cs.percent_axis(ax, "y")
ax.set_ylim(0, 1)
d14 = st[2014]
cs.title(ax, f"Signs add up: non-completion rises from {pct(d14['rate'].iloc[0])} with no sign to {pct(d14['rate'].iloc[-1])} with {int(d14['n_signs'].iloc[-1])}",
         "Non-completion rate by number of signs (95% interval), runs with a TMA due by day 27")
cs.source(fig, SRC)
cs.save(fig, c.FIGURES / "fig4_aq2_sign_count")

# ---------------------------------------------------------------- AQ3: recall against list size
cv = pd.read_csv(R / "aq3_capacity_curve.csv")
fig, ax = cs.figure(8, 4.4)
series = {}
for meth, label in [("M1", "Model (logistic)"), ("RULE", "Early-sign rule"), ("B3", "Background only"), ("RANDOM", "Random list")]:
    series[label] = cv[cv["method"] == meth].sort_values("per20")["recall"].tolist()
cs.lines(ax, list(range(1, 11)), series, highlight="Model (logistic)", fmt="{:.0%}")
ax.set_xticks(range(1, 11))
ax.axvline(5, color=cs.NEUTRAL_DARK, lw=1, ls="--")
ax.set_xlabel("Contacts per tutor group of 20 (list length)")
cs.percent_axis(ax, "y")
m5 = cv[(cv["method"] == "M1") & (cv["per20"] == 5)].iloc[0]
r5 = cv[(cv["method"] == "RULE") & (cv["per20"] == 5)].iloc[0]
cs.title(ax, f"At 5 contacts per 20 the model reaches {pct(m5['recall'], 1)} of non-completers, the rule {pct(r5['recall'], 1)}",
         "Share of all non-completers on the list (recall), 13 test runs of 2014, data up to day 27")
cs.source(fig, SRC + " Model trained on the 9 runs of 2013.")
cs.save(fig, c.FIGURES / "fig5_aq3_capacity")

# ---------------------------------------------------------------- AQ4: yield of each extra contact
y = pd.read_csv(R / "aq4_contact_yield.csv")
ym = y[y["method"] == "model"]
fig, ax = cs.figure(8, 4.2)
ax.bar(ym["contact"], ym["precision"], color=[cs.ACCENT if k <= 5 else cs.NEUTRAL for k in ym["contact"]], width=0.7)
for _, r in ym.iterrows():
    ax.text(r["contact"], r["precision"] + 0.015, f"{r['precision']:.0%}", ha="center", fontsize=9)
ax.axhline(ym["base_rate"].iloc[0], color=cs.ACCENT_2, lw=1.5, ls="--")
ax.text(0.45, ym["base_rate"].iloc[0] + 0.01, f"base rate {ym['base_rate'].iloc[0]:.0%}", color=cs.ACCENT_2, va="bottom", ha="left", fontsize=9)
ax.set_xticks(range(1, 11))
ax.set_xlabel("n-th contact per tutor group of 20, in model rank order (blue = the 5 planned contacts)")
cs.percent_axis(ax, "y")
ax.set_ylim(0, 1)
cs.title(ax, f"The first contact finds a non-completer {pct(ym['precision'].iloc[0])} of the time, the seventh {pct(ym['precision'].iloc[6])}",
         "Share of students at each list position who did not complete, 13 test runs of 2014, day 27")
cs.source(fig, SRC)
cs.save(fig, c.FIGURES / "fig6_aq4_contact_yield")

# ---------------------------------------------------------------- AQ4: fairness
fr = pd.read_csv(R / "aq4_fairness_confirmatory.csv")
fig, ax = cs.figure(8, 4.0)
fig.subplots_adjust(bottom=0.24)
cs.intervals(ax, fr["group"].tolist(), (fr["gap"] * 100).tolist(), (fr["low"] * 100).tolist(), (fr["high"] * 100).tolist(),
             fmt="{:+.1f}", reference=0.0)
ax.axvline(-10, color=cs.ACCENT_2, lw=1.2, ls="--")
ax.text(-10.3, 1.5, "−10-point\nflag line", color=cs.ACCENT_2, fontsize=8.5, ha="right", va="center")
ax.set_xlabel("Recall of the group minus recall of the other students, points (95% interval)")
cs.title(ax, f"No group is flagged: {int((~fr['flagged']).sum())} of {len(fr)} groups pass the fairness rule",
         "Share of each group's non-completers on the 5-per-20 lists, 13 test runs of 2014")
cs.source(fig, SRC)
cs.save(fig, c.FIGURES / "fig7_aq4_fairness")
print("figures written:", sorted(p.name for p in c.FIGURES.glob("*.png")))
