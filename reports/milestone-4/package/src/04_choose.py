"""Step 4 of Appendix III: model choice on the outer-fold results (day 27, k = 5 per 20).

A challenger (M2-M4) replaces M1 only with a pooled normalised recall gain >= 0.03 AND a gain in >= 7 of 9 folds;
if several qualify, the highest pooled value wins, ties to the simpler model (M1 < M2 < M3 < M4).
Baselines are listed for reference and are not eligible; a baseline that beats M1 is stated in the reason.

Run: venv/bin/python reports/milestone-4/package/src/04_choose.py
Reads results/dev_folds.csv; writes results/model_choice.csv.
"""
import numpy as np
import pandas as pd

import common as C


def choose(dev: pd.DataFrame) -> pd.DataFrame:
    d = dev[(dev["cutoff"] == C.MAIN_CUTOFF) & (dev["k"] == C.MAIN_PER20)]
    pooled = {cfg: C.pooled_normalised_recall(g["noncompleters_on_list"], g["max_attainable"])
              for cfg, g in d.groupby("config")}
    fold = d.pivot(index="validation_run", columns="config", values="normalised_recall")
    n_folds = len(fold)
    rows = []
    for cfg in C.CONFIGS:
        gain = pooled[cfg] - pooled["M1"]
        fwg = int((fold[cfg] > fold["M1"]).sum())
        rows.append({"config": cfg, "pooled_normalised_recall_d27_k5": pooled[cfg],
                     "gain_vs_M1": gain if cfg != "M1" else 0.0,
                     "folds_with_gain": fwg if cfg != "M1" else None,
                     "qualifies": cfg in ("M2", "M3", "M4") and gain >= C.MARGIN - 1e-12 and fwg >= C.MIN_FOLDS_WITH_GAIN})
    t = pd.DataFrame(rows)
    t["folds_with_gain"] = t["folds_with_gain"].astype("Int64")
    q = t[t["qualifies"]]
    if len(q):
        best = q["pooled_normalised_recall_d27_k5"].max()
        tied = [c for c in C.SIMPLICITY_ORDER if c in set(q[np.isclose(q["pooled_normalised_recall_d27_k5"], best)]["config"])]
        chosen = tied[0]
    else:
        chosen = "M1"
    reasons = []
    for _, r in t.iterrows():
        cfg = r["config"]
        kind = C.CONFIGS[cfg][0]
        if kind == "baseline":
            beat = " it is above M1 (a baseline beats the primary model on the development folds; reported, not a choice)" \
                if r["gain_vs_M1"] > 0 else ""
            reason = f"baseline, not eligible for the choice; gain {r['gain_vs_M1']:+.4f}, gain in {r['folds_with_gain']} of {n_folds} folds;{beat}"
        elif cfg == "M1":
            reason = ("primary model; kept because no challenger met the margin" if chosen == "M1"
                      else f"primary model; replaced by {chosen}, which met the margin")
        else:
            met_gain = r["gain_vs_M1"] >= C.MARGIN - 1e-12
            met_folds = r["folds_with_gain"] >= C.MIN_FOLDS_WITH_GAIN
            parts = [f"gain {r['gain_vs_M1']:+.4f} {'>=' if met_gain else '<'} {C.MARGIN}",
                     f"gain in {r['folds_with_gain']} of {n_folds} folds {'>=' if met_folds else '<'} {C.MIN_FOLDS_WITH_GAIN}"]
            verdict = "chosen: margin met" if cfg == chosen else ("margin met but another qualifying challenger ranks higher"
                                                                     if r["qualifies"] else "margin not met")
            reason = f"{verdict} ({'; '.join(parts)})"
        reasons.append(reason)
    t["chosen"] = np.where(t["config"] == chosen, "yes", "no")
    t["reason"] = reasons
    return t[["config", "pooled_normalised_recall_d27_k5", "gain_vs_M1", "folds_with_gain", "chosen", "reason"]]


def main() -> None:
    dev = pd.read_csv(C.RESULTS / "dev_folds.csv")
    t = choose(dev)
    t.to_csv(C.RESULTS / "model_choice.csv", index=False, float_format="%.6f")
    print(t.to_string(index=False))


if __name__ == "__main__":
    main()
