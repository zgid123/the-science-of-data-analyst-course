"""Gates and secondary metrics on the 13 test runs of 2014 (Table 4.5; Appendix II; Appendix III).

S1: pooled normalised recall of M1 vs the rule-ranked list (B2), day 27, k = 5 per 20, paired two-level bootstrap
interval, exact one-sided sign-flip test, wins/ties/losses, mean per-run difference.
S2/secondary: precision at capacity vs base rate and attainable maximum, PR-AUC and ROC-AUC within run, net benefit.
S3/calibration: calibration-in-the-large and slope (pooled), Brier score, decile bins for the plot.

Run: venv/bin/python reports/milestone-4/package/src/07_gates.py
Writes results/s1_gate.csv, s1_per_run.csv, secondary.csv, net_benefit.csv, calibration.csv, calibration_bins.csv,
brier.csv.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import average_precision_score

import common as C
import gates as G

S1_COLS = ["pooled_nr_model", "pooled_nr_rule", "difference", "boot_ci_low", "boot_ci_high", "signflip_p", "wins",
           "ties", "losses", "mean_per_run_difference", "verdict"]


def logit(p):
    p = np.clip(p, 1e-12, 1 - 1e-12)
    return np.log(p / (1 - p))


def calibration(y, p) -> tuple[float, float]:
    lp = logit(p)
    citl = sm.GLM(y, np.ones((len(y), 1)), family=sm.families.Binomial(), offset=lp).fit().params[0]
    slope = sm.GLM(y, sm.add_constant(lp), family=sm.families.Binomial()).fit().params[1]
    return float(citl), float(slope)


def main() -> None:
    views = {c: C.test_scores(c) for c in C.CUTOFFS}
    tr = pd.read_csv(C.RESULTS / "test_runs.csv")

    # ---- S1 (single gate)
    df = views[C.MAIN_CUTOFF]
    runs = G.run_arrays(df, lambda g: G.model_keys(g, "score_M1"), G.rule_keys)
    s1 = G.s1_stats(runs, C.MAIN_PER20)
    pd.DataFrame([{k: s1[k] for k in S1_COLS}]).to_csv(C.RESULTS / "s1_gate.csv", index=False, float_format="%.6f")
    per_run = []
    for r in runs:
        a, b, mx = G.run_counts(r, C.MAIN_PER20)
        per_run.append({"test_run": r["run"], "nr_model": a / mx, "nr_rule": b / mx, "difference": (a - b) / mx,
                        "noncompleters_on_list_model": a, "noncompleters_on_list_rule": b, "max_attainable": mx})
    pd.DataFrame(per_run).to_csv(C.RESULTS / "s1_per_run.csv", index=False, float_format="%.6f")
    print({k: s1[k] for k in S1_COLS})

    # ---- secondary metrics
    sec, nb, cal, bins, brier = [], [], [], [], []
    for cutoff in C.CUTOFFS:
        df = views[cutoff]
        pr = {"B1": None, "B2": [], "B3": [], "M1": []}
        for run, g in df.groupby(C.RUN, sort=True):
            y = g["y"].to_numpy()
            pr["B2"].append(average_precision_score(y, C.rule_score(g)))
            for cfg in ("B3", "M1"):
                pr[cfg].append(average_precision_score(y, g[f"score_{cfg}"].to_numpy()))
        for cfg in ("B1", "B2", "B3", "M1"):
            for per20 in C.PER20:
                t = tr[(tr.config == cfg) & (tr.cutoff == cutoff) & (tr.k == per20)]
                sec.append({"config": cfg, "cutoff": cutoff, "k": per20,
                            "precision": t.noncompleters_on_list.sum() / t.list_length.sum(),
                            "base_rate": t.n_noncompleters.sum() / t.n_enrolments.sum(),
                            "max_attainable_precision": t.max_attainable.sum() / t.list_length.sum(),
                            "pr_auc": float(np.mean(pr[cfg])) if pr[cfg] else None,
                            "roc_auc_within_run": t.roc_auc_within_run.mean(),
                            "net_benefit_by_threshold": "results/net_benefit.csv" if cfg != "B1" else None})
        # net benefit (context only)
        y = df["y"].to_numpy()
        n = len(y)
        for pt in np.round(np.arange(0.05, 0.951, 0.05), 2):
            w = pt / (1 - pt)
            pol = {"M1": df["score_M1"].to_numpy() >= pt, "B3": df["score_B3"].to_numpy() >= pt,
                   "rule (B2 flags)": df["early_sign_rule"].to_numpy(bool), "contact all": np.ones(n, bool),
                   "contact none": np.zeros(n, bool)}
            for name, sel in pol.items():
                tp, fp = int((sel & (y == 1)).sum()), int((sel & (y == 0)).sum())
                nb.append({"cutoff": cutoff, "threshold": pt, "strategy": name, "net_benefit": tp / n - fp / n * w})
        # calibration
        for cfg in ("M1", "B3"):
            p = df[f"score_{cfg}"].to_numpy()
            citl, slope = calibration(y, p)
            met = -0.2 <= citl <= 0.2 and 0.8 <= slope <= 1.2
            role = "S3" if (cfg == "M1" and cutoff == C.MAIN_CUTOFF) else "descriptive"
            cal.append({"config": cfg, "cutoff": cutoff, "citl": citl, "slope": slope,
                        "s3_verdict": f"{role}: {'met' if met else 'not met'}"})
            brier.append({"config": cfg, "cutoff": cutoff, "brier": float(np.mean((p - y) ** 2)),
                          "brier_base_rate": float(np.mean((y.mean() - y) ** 2))})
            dec = pd.qcut(pd.Series(p).rank(method="first"), 10, labels=False)
            for d_, g in pd.DataFrame({"p": p, "y": y, "d": dec}).groupby("d"):
                bins.append({"config": cfg, "cutoff": cutoff, "decile": int(d_) + 1, "n": len(g),
                             "mean_predicted": g.p.mean(), "observed": g.y.mean()})
    pd.DataFrame(sec).to_csv(C.RESULTS / "secondary.csv", index=False, float_format="%.6f")
    pd.DataFrame(nb).to_csv(C.RESULTS / "net_benefit.csv", index=False, float_format="%.6f")
    pd.DataFrame(cal).to_csv(C.RESULTS / "calibration.csv", index=False, float_format="%.6f")
    pd.DataFrame(bins).to_csv(C.RESULTS / "calibration_bins.csv", index=False, float_format="%.6f")
    pd.DataFrame(brier).to_csv(C.RESULTS / "brier.csv", index=False, float_format="%.6f")
    print(pd.DataFrame(sec).to_string(index=False))
    print(pd.DataFrame(cal).to_string(index=False))


if __name__ == "__main__":
    main()
