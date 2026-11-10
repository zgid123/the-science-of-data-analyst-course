"""Code-generated prototype report: report/prototype_report.md and report/prototype_report.html, with figures in
report/figures/, built from the CSV files in results/ only (no number is typed by hand; protocol constants come from
common.py).

Run: venv/bin/python reports/milestone-4/package/src/12_report.py
"""
from __future__ import annotations

import html
import json

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import common as C  # noqa: E402

REPORT = C.PKG / "report"
FIG = REPORT / "figures"
R = C.RESULTS
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.hashsalt": "n04", "figure.dpi": 150})
MODEL_C, RULE_C, GREY = "#1f5aa6", "#c0504d", "#7f7f7f"


def f3(x) -> str:
    return "–" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.3f}"


def fp(p) -> str:
    return f"{p:.4f}" if p >= 0.001 else f"{p:.1e}"


def pp(x) -> str:
    return f"{100 * x:+.1f} points"


def pct(x) -> str:
    return f"{100 * x:.1f}%"


def read(name, **kw) -> pd.DataFrame:
    return pd.read_csv(R / name, keep_default_na=False, na_values=[""], **kw)


class Doc:
    def __init__(self):
        self.blocks = []

    def h(self, level, text):
        self.blocks.append(("h", level, text))

    def p(self, text):
        self.blocks.append(("p", text))

    def ul(self, items):
        self.blocks.append(("ul", list(items)))

    def table(self, df: pd.DataFrame, intro: str):
        self.p(intro)
        self.blocks.append(("table", df.map(lambda v: "–" if v is None or (not isinstance(v, str) and pd.isna(v))
                                            else str(v))))

    def fig(self, path, caption, intro):
        self.p(intro)
        self.blocks.append(("img", path, caption))

    def code(self, text):
        self.blocks.append(("code", text))

    def markdown(self) -> str:
        out = []
        for b in self.blocks:
            if b[0] == "h":
                out.append("#" * b[1] + " " + b[2])
            elif b[0] == "p":
                out.append(b[1])
            elif b[0] == "ul":
                out.append("\n".join(f"- {i}" for i in b[1]))
            elif b[0] == "table":
                df = b[1]
                lines = ["| " + " | ".join(df.columns) + " |", "| " + " | ".join(":----" for _ in df.columns) + " |"]
                lines += ["| " + " | ".join(v.replace("|", "/") for v in row) + " |" for row in df.values.tolist()]
                out.append("\n".join(lines))
            elif b[0] == "img":
                out.append(f"![{b[2]}]({b[1]})\n\n*{b[2]}*")
            elif b[0] == "code":
                out.append("```bash\n" + b[1] + "\n```")
        return "\n\n".join(out) + "\n"

    def html(self, title) -> str:
        e = html.escape
        body = []
        for b in self.blocks:
            if b[0] == "h":
                body.append(f"<h{b[1]}>{e(b[2])}</h{b[1]}>")
            elif b[0] == "p":
                body.append(f"<p>{e(b[1])}</p>")
            elif b[0] == "ul":
                body.append("<ul>" + "".join(f"<li>{e(i)}</li>" for i in b[1]) + "</ul>")
            elif b[0] == "table":
                df = b[1]
                head = "".join(f"<th>{e(c)}</th>" for c in df.columns)
                rows = "".join("<tr>" + "".join(f"<td>{e(v)}</td>" for v in r) + "</tr>" for r in df.values.tolist())
                body.append(f"<div class='t'><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>")
            elif b[0] == "img":
                body.append(f"<figure><img src='{e(b[1])}' alt='{e(b[2])}'><figcaption>{e(b[2])}</figcaption></figure>")
            elif b[0] == "code":
                body.append(f"<pre>{e(b[1])}</pre>")
        css = ("body{font-family:Georgia,serif;max-width:60rem;margin:2rem auto;padding:0 1rem;line-height:1.5;"
               "color:#222;background:#fff}table{border-collapse:collapse;font-size:.85rem}td,th{border:1px solid "
               "#ccc;padding:.2rem .4rem;text-align:left}.t{overflow-x:auto}img{max-width:100%}"
               "figcaption{font-style:italic;font-size:.9rem}pre{background:#f4f4f4;padding:.5rem;overflow-x:auto}")
        return (f"<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' "
                f"content='width=device-width,initial-scale=1'><title>{e(title)}</title><style>{css}</style></head>"
                f"<body>{''.join(body)}</body></html>\n")


def save(fig, name):
    path = FIG / name
    fig.savefig(path, bbox_inches="tight", metadata={"Software": None})
    plt.close(fig)
    return f"figures/{name}"


def fig_nr(s1run, s1, sens):
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1.3, 1]})
    d = s1run.sort_values("difference")
    yy = np.arange(len(d))
    a.hlines(yy, d.nr_rule, d.nr_model, color=GREY, lw=1)
    a.plot(d.nr_rule, yy, "s", color=RULE_C, label="Early-sign rule (B2)")
    a.plot(d.nr_model, yy, "o", color=MODEL_C, label="Frozen model (M1)")
    a.set_yticks(yy, d.test_run)
    a.set_xlabel("Normalised recall, day 27, 5 per 20")
    a.legend(frameon=False, loc="lower right", fontsize=8)
    rows = [("Main test (S1)", s1)] + [(r.variant, r) for r in sens.itertuples()]
    yy = np.arange(len(rows))[::-1]
    for y_, (lab, r) in zip(yy, rows):
        diff, lo, hi = (r["difference"], r["boot_ci_low"], r["boot_ci_high"]) if isinstance(r, pd.Series) else \
            (r.difference, r.boot_ci_low, r.boot_ci_high)
        b.errorbar(diff, y_, xerr=[[diff - lo], [hi - diff]], fmt="o", color=MODEL_C if y_ == yy[0] else GREY,
                   capsize=3)
    b.axvline(0, color="black", lw=0.8)
    b.set_yticks(yy, [x[0] for x in rows], fontsize=8)
    b.set_xlabel("Pooled difference M1 − rule (95% bootstrap interval)")
    fig.tight_layout()
    return save(fig, "fig1_nr_model_vs_rule.png")


def fig_cal(bins):
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    for (cfg, cut), g in bins.groupby(["config", "cutoff"]):
        style = {"M1": "o-", "B3": "s--"}[cfg]
        col = MODEL_C if cfg == "M1" else GREY
        ax.plot(g.mean_predicted, g.observed, style, color=col, alpha=1 if cut == 27 else 0.45, ms=4,
                label=f"{cfg}, day {cut}")
    ax.plot([0, 1], [0, 1], color="black", lw=0.8)
    ax.set_xlabel("Mean predicted risk (decile)")
    ax.set_ylabel("Observed non-completion")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    return save(fig, "fig2_calibration.png")


def fig_fair(fair):
    d = fair[(fair.cutoff == C.MAIN_CUTOFF) & (fair.k == C.MAIN_PER20)].reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    yy = np.arange(len(d))[::-1]
    for y_, r in zip(yy, d.itertuples()):
        conf = not pd.isna(r.holm_ci_high)
        ax.plot(r.difference, y_, "o", color=MODEL_C if conf else GREY)
        if conf:
            ax.plot([r.difference, r.holm_ci_high], [y_, y_], color=MODEL_C, lw=1)
            ax.plot([r.holm_ci_high], [y_], "|", color=MODEL_C, ms=12, mew=1.5)
    ax.axvline(0, color="black", lw=0.8)
    ax.axvline(-0.10, color=RULE_C, lw=0.8, ls="--")
    ax.set_yticks(yy, d.group, fontsize=8)
    ax.set_xlabel("Recall at capacity, group − others (day 27, 5 per 20); bar = Holm one-sided upper bound")
    fig.tight_layout()
    return save(fig, "fig3_fairness.png")


def fig_aq2(aq):
    d = aq[aq.module == "all"].reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(7, 3.6))
    yy = np.arange(len(d))[::-1]
    for off, yr, col in ((0.12, "2013", GREY), (-0.12, "2014", MODEL_C)):
        est = d[f"estimate_{yr}"].astype(float)
        ci = d[f"ci_{yr}"].map(lambda s: json.loads(s))
        lo = np.array([c[0] for c in ci])
        hi = np.array([c[1] for c in ci])
        ax.errorbar(est, yy + off, xerr=[est - lo, hi - est], fmt="o", color=col, capsize=3, label=yr)
    ax.axvline(0, color="black", lw=0.8)
    ax.axvline(5, color=RULE_C, lw=0.8, ls="--")
    ax.set_yticks(yy, d.sign.str.replace("_", " "))
    ax.set_xlabel("Adjusted average risk difference, percentage points (95% interval)")
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    return save(fig, "fig4_aq2_2013_vs_2014.png")


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    pop = read("populations_2013.csv")
    folds = read("folds_2013.csv")
    choice = read("model_choice.csv")
    freeze = read("freeze.csv", dtype=str)
    b3fit = read("b3_fit.csv", dtype=str)
    tr = read("test_runs.csv")
    s1 = read("s1_gate.csv").iloc[0]
    s1run = read("s1_per_run.csv")
    sec = read("secondary.csv")
    cal = read("calibration.csv")
    bins = read("calibration_bins.csv")
    brier = read("brier.csv")
    fair = read("fairness.csv")
    sens = read("sensitivity.csv")
    sdet = read("sensitivity_detail.csv")
    aq4 = read("aq4_lists_summary.csv")
    aq2 = read("aq2_replication.csv")
    aq2d = read("aq2_replication_detail.csv")
    nb = read("net_benefit.csv")

    d = Doc()
    title = "Prototype report – Milestone 4, Level 2 (team N04)"
    d.h(1, title)
    d.p("This report is written by src/12_report.py from the CSV files in results/ alone; every number comes from "
        "those files. It covers the eight steps of the prototype protocol: development on the 9 runs of 2013, the "
        "second freeze, the single test on the 2014 runs, error and fairness analysis, sensitivity analyses and the "
        "AQ2 replication.")

    # 1 purpose
    d.h(2, "1. Purpose and frozen protocol")
    d.p(f"The prototype tests whether the Level 1 choices hold on data the model never saw. The primary model (M1) is "
        f"a penalised logistic regression on the primary predictor set; it is compared with three baselines (B1 random "
        f"list, B2 early-sign rule ranked by number of signs, B3 background-only logistic model) and three challengers "
        f"(M2 logistic, extended set; M3 and M4 gradient-boosted trees on the primary and extended sets). A challenger "
        f"replaces M1 only with a gain of at least {C.MARGIN} in pooled normalised recall at day {C.MAIN_CUTOFF}, "
        f"k = {C.MAIN_PER20} per 20, and a gain in at least {C.MIN_FOLDS_WITH_GAIN} of the 9 development folds. "
        f"Normalised recall is the number of non-completers on a run's list divided by the most a list of that length "
        f"can hold, min(k, number of non-completers), pooled over runs. The single gate S1 requires M1's pooled "
        f"normalised recall on the 2014 runs to exceed the rule's, with the 95% paired two-level bootstrap interval of "
        f"the difference above 0 and a one-sided sign-flip p-value below 0.05.")

    # 2 data
    d.h(2, "2. Data and populations")
    tot = pop.groupby("cutoff")[["n_enrolments", "n_noncompleters", "max_attainable_k5"]].sum().reset_index()
    t27 = tr[(tr.config == "M1") & (tr.k == C.MAIN_PER20)].groupby("cutoff")[["n_enrolments", "n_noncompleters"]].sum()
    tot["test_enrolments_2014"] = tot.cutoff.map(t27.n_enrolments)
    tot["test_noncompleters_2014"] = tot.cutoff.map(t27.n_noncompleters)
    d.table(tot.rename(columns={"n_enrolments": "dev_enrolments_2013", "n_noncompleters": "dev_noncompleters_2013",
                                "max_attainable_k5": "dev_max_attainable_k5"}),
            "The inputs are the Milestone 3 prepared package OULAD-N04-prepared-1.0; every file hash matched its "
            "manifest before use. The table gives the development (2013) and test (2014) populations at each cut-off.")
    d.p(f"In each development fold, training rows of students who also appear in the validation run are removed: "
        f"{int(folds[folds.cutoff == 13].removed_rows.sum())} rows over the folds at day 13 and "
        f"{int(folds[folds.cutoff == 27].removed_rows.sum())} at day 27.")

    # 3 development
    d.h(2, "3. Development results and model choice")
    ch = choice.copy()
    ch["folds_with_gain"] = ch["folds_with_gain"].astype("Int64")
    for c in ("pooled_normalised_recall_d27_k5", "gain_vs_M1"):
        ch[c] = ch[c].map(f3)
    d.table(ch, f"The selection rule was applied to the nine leave-one-run-out folds of 2013 (nested leave-one-run-out "
                f"tuning inside each training set). The table gives each configuration's pooled normalised recall at "
                f"day {C.MAIN_CUTOFF}, k = {C.MAIN_PER20} per 20, its gain over M1 and the folds with a gain.")
    chosen = choice[choice.chosen == "yes"].config.iloc[0]
    d.p(f"The rule chose {chosen}. These fold results serve the choice only and are not an estimate of performance "
        f"in use.")

    # 4 test
    d.h(2, "4. The single test")
    acc = freeze.first_test_access_utc.iloc[0]
    d.p(f"The 2014 outcomes were opened once, at {acc} (UTC), after both frozen model files were re-verified against "
        f"their recorded SHA-256 values; the access time and hashes were written to the experiment log before any "
        f"2014 row was read.")
    d.table(pd.concat([freeze[["chosen_config", "parameter_file", "model_sha256"]].rename(columns={"chosen_config": "config"}),
                       b3fit[["parameter_file", "model_sha256"]].assign(config="B3")], ignore_index=True),
            "The table lists the scored model files and their hashes; B3 was refitted on all 2013 runs with the M1 "
            "procedure before the access.")

    # 5 gates
    d.h(2, "5. Success criteria S1–S3")
    s2 = sec[(sec.config == "M1") & (sec.cutoff == C.MAIN_CUTOFF) & (sec.k == C.MAIN_PER20)].iloc[0]
    s3 = cal[(cal.config == "M1") & (cal.cutoff == C.MAIN_CUTOFF)].iloc[0]
    s1met = s1.verdict == "S1 met"
    d.p(f"S1, the single gate: on all 13 test runs at day {C.MAIN_CUTOFF}, k = {C.MAIN_PER20} per 20, M1's pooled "
        f"normalised recall is {f3(s1.pooled_nr_model)} against {f3(s1.pooled_nr_rule)} for the rule-ranked list, a "
        f"difference of {f3(s1.difference)} (95% paired two-level bootstrap interval {f3(s1.boot_ci_low)} to "
        f"{f3(s1.boot_ci_high)}; one-sided sign-flip p = {fp(s1.signflip_p)}). M1 wins {int(s1.wins)} runs, ties "
        f"{int(s1.ties)} and loses {int(s1.losses)}; the unweighted mean of the per-run differences is "
        f"{f3(s1.mean_per_run_difference)}. Verdict: {s1.verdict}. In counts, M1's lists hold "
        f"{int(s1run.noncompleters_on_list_model.sum())} non-completers and the rule's "
        f"{int(s1run.noncompleters_on_list_rule.sum())}, out of at most {int(s1run.max_attainable.sum())}.")
    if not s1met:
        d.p("Unfavourable result: S1 is not met, so the frozen model is not shown to list more non-completers than "
            "the early-sign rule with enough certainty; under the protocol the rule remains the comparison standard.")
    if s1.difference <= 0:
        d.p("Unfavourable result: the early-sign rule matches or beats M1 on pooled normalised recall at the main "
            "operating point.")
    if int(s1.losses) > 0:
        lost = s1run[s1run.difference < 0].test_run.tolist()
        d.p(f"M1's list holds fewer non-completers than the rule's in {len(lost)} run(s): {', '.join(lost)}.")
    d.p(f"S2 (reported, not a gate): M1's precision at capacity is {pct(s2.precision)} against a base rate of "
        f"{pct(s2.base_rate)} and an attainable maximum of {pct(s2.max_attainable_precision)}.")
    s3met = s3.s3_verdict.endswith(": met")
    d.p(f"S3 (condition for showing probabilities): calibration-in-the-large {f3(s3.citl)} (bounds −0.2 to 0.2) and "
        f"slope {f3(s3.slope)} (bounds 0.8 to 1.2): {'met, so probabilities may be shown' if s3met else 'not met, so tutors see ranks and reasons only'}.")
    if not s3met:
        d.p("Unfavourable result: S3 is not met. "
            + (f"A slope of {f3(s3.slope)}, above 1, means the predicted risks are less extreme than the observed "
               "outcomes (too close to the average), which fits the strong shrinkage the tuning chose; the ranking, "
               "and so the lists, are unaffected." if s3.slope > 1.2 else
               f"A slope of {f3(s3.slope)}, below 1, means the predicted risks are too extreme." if s3.slope < 0.8 else
               "Calibration-in-the-large lies outside its bounds."))
    d.fig(save_fig := fig_nr(s1run, s1, sens), "Figure 1. Normalised recall by test run (left) and pooled M1 − rule "
          "difference with 95% bootstrap interval, main test and sensitivity variants (right)",
          "Figure 1 shows, for each 2014 run, the normalised recall of M1 and of the rule at the main operating point, "
          "and the pooled difference with its interval for the main test and every sensitivity variant.")

    # 6 secondary
    d.h(2, "6. Secondary metrics")
    sc = sec.copy()
    for c in ("precision", "base_rate", "max_attainable_precision", "pr_auc", "roc_auc_within_run"):
        sc[c] = sc[c].map(f3)
    d.table(sc.drop(columns=["net_benefit_by_threshold"]),
            "The table gives precision at capacity with its base rate and attainable maximum, and the within-run PR-AUC "
            "and ROC-AUC averaged over the 13 test runs, per configuration, cut-off and list length.")
    nb27 = nb[(nb.cutoff == C.MAIN_CUTOFF)].pivot(index="threshold", columns="strategy", values="net_benefit")
    better = nb27.index[(nb27["M1"] > nb27["rule (B2 flags)"]) & (nb27["M1"] > nb27["contact all"]) &
                        (nb27["M1"] > nb27["contact none"])]
    notb = [f"{t:.2f}" for t in nb27.index if t not in set(better)]
    d.p(f"Net benefit (context only, results/net_benefit.csv): at day {C.MAIN_CUTOFF}, M1 has a higher net benefit "
        f"than contacting everyone, no one and the rule-flagged students at {len(better)} of {len(nb27)} thresholds "
        f"between {nb27.index.min():.2f} and {nb27.index.max():.2f}"
        + (f"; it does not at {', '.join(notb)}." if notb else "."))

    # 7 calibration
    d.h(2, "7. Calibration")
    cc = cal.merge(brier, on=["config", "cutoff"])
    for c in ("citl", "slope", "brier", "brier_base_rate"):
        cc[c] = cc[c].map(f3)
    d.table(cc, "The table gives calibration-in-the-large, calibration slope and Brier score (with the Brier score of "
                "predicting the test base rate) for M1 and B3; only M1 at day 27 is judged against S3.")
    d.fig(fig_cal(bins), "Figure 2. Observed non-completion against mean predicted risk by decile, 2014 test runs",
          "Figure 2 plots observed against predicted risk by decile of predicted risk; points on the diagonal are "
          "well calibrated.")

    # 8 fairness
    d.h(2, "8. Fairness (FR1)")
    fm = fair[(fair.cutoff == C.MAIN_CUTOFF) & (fair.k == C.MAIN_PER20)].copy()
    for c in ("recall_group", "recall_others", "difference", "holm_ci_high"):
        fm[c] = fm[c].map(f3)
    d.table(fm, f"The table gives, at day {C.MAIN_CUTOFF} and k = {C.MAIN_PER20} per 20, each audit group's recall "
                f"at capacity against the other students, the difference and, for the three confirmatory groups, the "
                f"Holm-adjusted one-sided 95% upper bound. A group is flagged when the gap is below −10 points and the "
                f"bound lies below 0.")
    flagged = fm[fm.flagged == "yes"].group.tolist()
    neg = fair[(fair.cutoff == C.MAIN_CUTOFF) & (fair.k == C.MAIN_PER20) & (fair.difference < 0) &
               (fair.flagged == "no")]
    if len(neg):
        d.p("Not flagged but below the other students: " + "; ".join(
            f"{r.group} ({pp(r.difference)}, upper bound {pp(r.holm_ci_high)})" for r in neg.itertuples()) + ".")
    d.p("Flagged for review: " + (", ".join(flagged) if flagged else "no confirmatory group") + ". "
        + "; ".join(f"{r.group}: insufficient data, not cleared (point gap {r.difference})"
                    for r in fm[fm.flagged == "insufficient data, not cleared"].itertuples()) + ".")
    d.fig(fig_fair(fair), "Figure 3. Recall gap by audit group with the Holm one-sided upper bound (confirmatory "
          "groups); dashed line at −10 points", "Figure 3 shows the recall gap of each audit group at the main "
          "operating point.")

    # 9 sensitivity
    d.h(2, "9. Sensitivity analyses")
    sv = sens.merge(sdet, on=["variant", "cutoff", "k"])
    for c in ("pooled_nr_model", "pooled_nr_rule", "difference", "boot_ci_low", "boot_ci_high",
              "mean_per_run_difference"):
        sv[c] = sv[c].map(f3)
    sv["signflip_p"] = sv["signflip_p"].map(fp)
    d.table(sv.drop(columns=["note"]), "The table repeats the S1 statistics for each variant; none can change the "
                                       "S1 verdict.")
    diverge = sens[sens.verdict.str.startswith("would meet") != s1met].variant.tolist()
    d.p("Variants whose S1 reading differs from the main test: " + (", ".join(diverge) if diverge else "none") + ".")
    rule_wins = sens[sens.difference <= 0].variant.tolist()
    if rule_wins:
        d.p("Unfavourable result: the rule matches or beats M1 in these variants: " + ", ".join(rule_wins) + ".")
    d.ul(f"{r.variant}: {r.note}" for r in sdet.itertuples() if isinstance(r.note, str) and r.note)

    # 10 AQ4
    d.h(2, "10. AQ4 lists under capacity")
    pooled = aq4[aq4.test_run == "all 13 runs (pooled)"].copy()
    for c in ("recall", "precision", "lift", "normalised_recall", "overlap_with_rule_list"):
        pooled[c] = pooled[c].map(f3)
    d.table(pooled.drop(columns=["test_run"]), "The table summarises the M1-ranked lists of the 13 test runs per "
            "cut-off and list length, pooled: recall, precision, the C13 check that precision is at least 50%, lift, "
            "overlap with the rule's list and the Fail and Withdrawn students among the listed non-completers.")
    low = aq4[(aq4.test_run != "all 13 runs (pooled)") & (aq4.cutoff == C.MAIN_CUTOFF) & (aq4.k == C.MAIN_PER20) &
              (aq4.precision_ge_50 == "no")]
    if len(low):
        d.p("Unfavourable result: the C13 limit of 50% precision is not reached in every run.")
    d.p(f"Runs whose day-{C.MAIN_CUTOFF} list of {C.MAIN_PER20} per 20 has precision below 50%: "
        + (", ".join(f"{r.test_run} ({pct(r.precision)})" for r in low.itertuples()) if len(low) else "none") + ". "
        "Each listed student carries up to three contributing predictors (coefficient × standardised value); the "
        "per-student lists are in results/aq4_lists/.")

    # 11 AQ2
    d.h(2, "11. AQ2 replication on 2014")
    a2 = aq2.merge(aq2d, on=["sign", "module"])
    d.table(a2[a2.module == "all"][["sign", "estimate_2013", "ci_2013", "verdict_2013", "estimate_2014", "ci_2014",
                                    "verdict_2014", "modules_same_direction_2014"]],
            "The table compares the adjusted average risk difference (percentage points) of each early sign in 2013 "
            "and 2014, re-estimated with the same model only after the AQ3 test (Change Log C14); module-specific "
            "estimates, CCC included, are in results/aq2_replication.csv.")
    changed = a2[(a2.module == "all") & (a2.verdict_2013 != a2.verdict_2014)].sign.tolist()
    d.p("Signs whose verdict differs between 2013 and 2014: " + (", ".join(changed) if changed else "none") + ".")
    d.fig(fig_aq2(aq2), "Figure 4. Adjusted risk difference of each sign, 2013 and 2014, with 95% intervals; dashed "
          "line at 5 points", "Figure 4 compares the adjusted risk difference of each sign between the two years.")

    # 12 deviations
    d.h(2, "12. Deviations from the contract")
    d.p("The contract and the Milestone 4 report leave these implementation details open; each was fixed as below.")
    d.ul(C.DEVIATIONS + C.TEST_DEVIATIONS)

    # 13 limitations
    d.h(2, "13. Limitations")
    d.ul([
        f"The test rests on {len(s1run)} runs of 2014; the sign-flip test has at most 2^{len(s1run)} assignments, and "
        f"the unpaired and CCC-only variants have too few runs for a p-value below 0.05.",
        "Development fold results served the model choice only; the test estimates are the honest ones.",
        "Recall and precision count non-completion as recorded; they do not show that a contact changes the outcome, "
        "and the order of risk is assumed, not shown, to match the order of need.",
        "The fairness check covers recall at capacity only; other criteria cannot all hold when base rates differ.",
        "Reasons per student are linear contributions of the frozen model, not causes.",
    ])

    # 14 reproduction
    d.h(2, "14. Reproduction")
    d.code("venv/bin/pip install -r reports/milestone-4/package/requirements.txt\n"
           "bash reports/milestone-4/package/src/run_dev.sh      # phase 1 (refused once the test is accessed)\n"
           "bash reports/milestone-4/package/src/run_test.sh     # phase 2: 06 --reproduce, 07-12, tests")

    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / "prototype_report.md").write_text(d.markdown())
    (REPORT / "prototype_report.html").write_text(d.html(title))
    print("wrote report/prototype_report.md and report/prototype_report.html")


if __name__ == "__main__":
    main()
