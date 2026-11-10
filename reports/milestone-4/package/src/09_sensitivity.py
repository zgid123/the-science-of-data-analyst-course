"""Step 7 of Appendix III: sensitivity analyses of S1 on the 2014 test runs. None can change the S1 verdict.

Variants (contract): paired runs; unpaired runs; module CCC apart (CCC only, and without CCC); without test enrolments
of students seen in 2013; without Withdrawn enrolments lacking a withdrawal day; labels-available (M1 specification
fitted on the 2013B runs, scored on the 2014B runs); day 13; k = 3 per 20.

Run: venv/bin/python reports/milestone-4/package/src/09_sensitivity.py
Writes results/sensitivity.csv (contract columns) and results/sensitivity_detail.csv (runs, rows, notes).
"""
import pandas as pd
from threadpoolctl import threadpool_limits

import common as C
import gates as G

S1_COLS = ["pooled_nr_model", "pooled_nr_rule", "difference", "boot_ci_low", "boot_ci_high", "signflip_p", "wins",
           "ties", "losses", "mean_per_run_difference", "verdict"]


def s1_row(variant, cutoff, per20, df, score_col, code, note=""):
    if df.empty:
        return {"variant": variant, "cutoff": cutoff, "k": per20, **{c: None for c in S1_COLS},
                "n_runs": 0, "n_enrolments": 0, "note": note or "no rows"}
    runs = G.run_arrays(df, lambda g: G.model_keys(g, score_col), G.rule_keys)
    s = G.s1_stats(runs, per20, seed=(C.BOOT_SEED, code))
    s["verdict"] = ("would meet S1" if s["verdict"] == "S1 met" else "would not meet S1") + " (sensitivity only)"
    return {"variant": variant, "cutoff": cutoff, "k": per20, **{c: s[c] for c in S1_COLS},
            "n_runs": len(runs), "n_enrolments": len(df), "note": note}


def labels_available(cutoff: int):
    """M1 specification tuned and fitted on the 2013B runs only; scores the 2014B runs."""
    tr = C.load_view(cutoff)
    tr = tr[tr["start_month"] == "B"]
    cols = C.columns_for("M1", cutoff, C.predictor_sets())
    with threadpool_limits(limits=1):
        params, _ = C.tune("M1", cols, tr)
        pipe = C.fit_pipeline("M1", cols, params, tr)
    te = C.test_scores(cutoff)
    te = te[te["start_month"] == "B"].copy()
    te["score_LA"] = C.predict_any(pipe, cols, te)
    return te, params, sorted(tr[C.RUN].unique())


def main() -> None:
    rows = []
    d27 = C.test_scores(C.MAIN_CUTOFF)
    k5 = C.MAIN_PER20
    rows.append(s1_row("paired runs", 27, k5, d27[d27["paired_run"]], "score_M1", 21))
    rows.append(s1_row("unpaired runs", 27, k5, d27[~d27["paired_run"]], "score_M1", 22))
    rows.append(s1_row("module CCC only", 27, k5, d27[d27["code_module"] == "CCC"], "score_M1", 23))
    rows.append(s1_row("without module CCC", 27, k5, d27[d27["code_module"] != "CCC"], "score_M1", 24))
    rows.append(s1_row("without students seen in 2013", 27, k5, d27[~d27["student_in_training_runs"]], "score_M1", 25,
                       "lists re-formed on the remaining enrolments"))
    rows.append(s1_row("without Withdrawn lacking a day", 27, k5, d27[~d27["eval_withdrawal_day_unknown"]],
                       "score_M1", 26, "lists re-formed on the remaining enrolments"))
    te, params, runs13 = labels_available(27)
    rows.append(s1_row("labels-available (2013B -> 2014B)", 27, k5, te, "score_LA", 27,
                       f"M1 spec fitted on {', '.join(runs13)} with {params}; scored on the 2014B runs"))
    rows.append(s1_row("day 13", 13, k5, C.test_scores(13), "score_M1", 28))
    rows.append(s1_row("k = 3 per 20", 27, 3, d27, "score_M1", 29))
    out = pd.DataFrame(rows)
    out[["variant", "cutoff", "k"] + S1_COLS].to_csv(C.RESULTS / "sensitivity.csv", index=False, float_format="%.6f")
    out[["variant", "cutoff", "k", "n_runs", "n_enrolments", "note"]].to_csv(
        C.RESULTS / "sensitivity_detail.csv", index=False)
    print(out.to_string(index=False))


if __name__ == "__main__":
    main()
