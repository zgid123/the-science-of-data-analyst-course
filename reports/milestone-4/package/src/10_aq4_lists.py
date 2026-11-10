"""AQ4, ranking under capacity: per 2014 test run and cut-off, the M1-ranked list of length k (3 and 5 per 20, tiers:
first tier = top 3 per 20, second tier = next 2 per 20) with each listed enrolment's top contributing predictors
(coefficient x standardised value of the frozen logistic model, summed over the columns of one predictor).

Run: venv/bin/python reports/milestone-4/package/src/10_aq4_lists.py
Writes results/aq4_lists/lists_d<cutoff>.csv (anonymised OULAD id_student only; no outcome column) and
results/aq4_lists_summary.csv (per run and pooled: recall, precision, C13 precision >= 50% check, lift, overlap with
the rule list, Fail/Withdrawn among the listed non-completers).
"""
import numpy as np
import pandas as pd

import common as C

TOP_REASONS = 3


def predictor_of(feature: str, cols: list[str]) -> str:
    if "=" in feature:
        return feature.split("=")[0]
    if feature.endswith("_missing") and feature[: -len("_missing")] in cols:
        return feature[: -len("_missing")]
    return feature


def contributions(pipe, cols, df) -> pd.DataFrame:
    X = df[cols].copy()
    for c in cols:
        if X[c].dtype == bool:
            X[c] = X[c].astype(float)
    Z = pipe.named_steps["prep"].transform(X)
    names = pipe.named_steps["prep"].named_steps["encode"].get_feature_names_out()
    contrib = Z * pipe.named_steps["model"].coef_[0]
    out = pd.DataFrame(contrib, columns=names, index=df.index)
    return out.T.groupby([predictor_of(n, cols) for n in names]).sum().T


def main() -> None:
    lists_dir = C.RESULTS / "aq4_lists"
    lists_dir.mkdir(parents=True, exist_ok=True)
    summary = []
    for cutoff in C.CUTOFFS:
        df = C.test_scores(cutoff)
        pipe, cols, _ = C.frozen_m1(cutoff)
        contrib = contributions(pipe, cols, df)
        list_rows = []
        for run, g in df.groupby(C.RUN, sort=True):
            n = len(g)
            order = C.model_order(g, g["score_M1"].to_numpy())
            k3, k5 = C.list_length(n, 3), C.list_length(n, 5)
            top = g.iloc[order[:k5]]
            for rank, (idx, row) in enumerate(top.iterrows(), start=1):
                c = contrib.loc[idx].sort_values(ascending=False)
                c = c[c > 0].head(TOP_REASONS)
                list_rows.append({"test_run": run, "rank": rank, "tier": 1 if rank <= k3 else 2,
                                  "id_student": int(row["id_student"]), "score": round(float(row["score_M1"]), 6),
                                  **{f"reason_{i + 1}": f"{p} ({v:+.3f})" for i, (p, v) in enumerate(c.items())}})
            rule_order = C.b2_order(g)
            for per20, k in ((3, k3), (5, k5)):
                listed = C.on_list(order, k)
                rule_listed = C.on_list(rule_order, k)
                summary.append(_summary(run, cutoff, per20, g, listed, rule_listed, k))
        pd.DataFrame(list_rows).to_csv(lists_dir / f"lists_d{cutoff}.csv", index=False)
    s = pd.DataFrame(summary)
    pooled = []
    for (cutoff, per20), g in s.groupby(["cutoff", "k"]):
        tp, k, nnc, n = g.noncompleters_on_list.sum(), g.list_length.sum(), g.n_noncompleters.sum(), g.n_enrolments.sum()
        pooled.append({"test_run": "all 13 runs (pooled)", "cutoff": cutoff, "k": per20, "n_enrolments": n,
                       "n_noncompleters": nnc, "list_length": k, "noncompleters_on_list": tp, "recall": tp / nnc,
                       "precision": tp / k, "precision_ge_50": "yes" if tp / k >= 0.5 else "no",
                       "lift": (tp / k) / (nnc / n), "normalised_recall": tp / g.max_attainable.sum(),
                       "max_attainable": g.max_attainable.sum(),
                       "overlap_with_rule_list": (g.overlap_with_rule_list * g.list_length).sum() / k,
                       "listed_fail": g.listed_fail.sum(), "listed_withdrawn": g.listed_withdrawn.sum()})
    s = pd.concat([s, pd.DataFrame(pooled)], ignore_index=True).sort_values(["cutoff", "k", "test_run"])
    s.to_csv(C.RESULTS / "aq4_lists_summary.csv", index=False, float_format="%.6f")
    print(pd.DataFrame(pooled).to_string(index=False))
    print("runs with precision < 50% at day 27, k = 5:",
          s[(s.cutoff == 27) & (s.k == 5) & (s.precision_ge_50 == "no")]["test_run"].tolist())


def _summary(run, cutoff, per20, g, listed, rule_listed, k) -> dict:
    y = g["y"].to_numpy() == 1
    n, nnc, tp = len(g), int(y.sum()), int((listed & y).sum())
    fr = g["final_result"].to_numpy()
    return {"test_run": run, "cutoff": cutoff, "k": per20, "n_enrolments": n, "n_noncompleters": nnc,
            "list_length": k, "noncompleters_on_list": tp, "recall": tp / nnc, "precision": tp / k,
            "precision_ge_50": "yes" if tp / k >= 0.5 else "no", "lift": (tp / k) / (nnc / n),
            "normalised_recall": tp / min(k, nnc), "max_attainable": min(k, nnc),
            "overlap_with_rule_list": float((listed & rule_listed).sum() / k),
            "listed_fail": int((listed & (fr == "Fail")).sum()),
            "listed_withdrawn": int((listed & (fr == "Withdrawn")).sum())}


if __name__ == "__main__":
    main()
