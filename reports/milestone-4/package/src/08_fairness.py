"""Confirmatory fairness check FR1 (Table 4.5; Appendix IV, Tables A.7-A.8) on the 13 test runs of 2014.

Recall at capacity of each group minus the other students, lists formed per run from the frozen M1 scores, pooled
within run. Confirmatory (day 27, k = 5 per 20): declared disability, deprivation band 0-10%, deprivation band
missing (eligibility >= 400 test enrolments, checked here); flagged when the gap is below -10 points AND the one-sided
95% bootstrap upper bound, Holm-adjusted over the three, lies below 0. Age 55 or over: point gap only, "insufficient
data, not cleared". Gender: descriptive. Audit attributes are read here only; no model ever reads them.

Run: venv/bin/python reports/milestone-4/package/src/08_fairness.py
Writes results/fairness.csv.
"""
import numpy as np
import pandas as pd

import common as C
import gates as G

CONFIRMATORY = {
    "disability: declared": lambda d: d["disability"] == "Y",
    "deprivation band: 0-10%": lambda d: d["imd_band"] == "0-10%",
    "deprivation band: missing": lambda d: d["imd_band"] == "Missing",
}
POINT_ONLY = {"age band: 55 or over": lambda d: d["age_band"] == "55<="}
DESCRIPTIVE = {"gender: female": lambda d: d["gender"] == "F", "gender: male": lambda d: d["gender"] == "M"}
MIN_ELIGIBLE = 400


def main() -> None:
    rows = []
    for cutoff in C.CUTOFFS:
        df = C.test_scores(cutoff)
        for per20 in C.PER20:
            main_point = cutoff == C.MAIN_CUTOFF and per20 == C.MAIN_PER20
            boots, point = {}, {}
            for gname, fn in {**CONFIRMATORY, **POINT_ONLY, **DESCRIPTIVE}.items():
                mask = fn(df).to_numpy(bool)
                runs = G.group_runs(df, "score_M1", mask)
                rg, ro, diff = G.recall_gap(runs, per20)
                point[gname] = (int(mask.sum()), int((mask & (df["y"].to_numpy() == 1)).sum()), rg, ro, diff)
                if main_point and gname in CONFIRMATORY:
                    if mask.sum() < MIN_ELIGIBLE:
                        raise SystemExit(f"{gname}: {mask.sum()} test enrolments, below the eligibility size")
                    code = list(CONFIRMATORY).index(gname) + 10
                    boots[gname] = G.bootstrap_gap(runs, per20, C.BOOT_B, [C.BOOT_SEED, code])
            holm = G.holm_upper_bounds(boots) if boots else {}
            for gname, (n, nnc, rg, ro, diff) in point.items():
                if gname in holm:
                    hi = holm[gname][0]
                    flagged = "yes" if (diff < -0.10 and hi < 0) else "no"
                elif gname in POINT_ONLY and main_point:
                    hi, flagged = None, "insufficient data, not cleared"
                else:
                    hi, flagged = None, "descriptive"
                rows.append({"group": gname, "cutoff": cutoff, "k": per20, "n": n, "n_noncompleters": nnc,
                             "recall_group": rg, "recall_others": ro, "difference": diff, "holm_ci_high": hi,
                             "flagged": flagged})
    out = pd.DataFrame(rows)
    out.to_csv(C.RESULTS / "fairness.csv", index=False, float_format="%.6f")
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
