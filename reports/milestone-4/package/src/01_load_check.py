"""Step 1 (Table 7.1): check input hashes, load the 2013 rows only, report populations per run and cut-off.

Run: venv/bin/python reports/milestone-4/package/src/01_load_check.py [--m3 <milestone-3 package>]
Writes results/input_hashes.csv, results/populations_2013.csv, results/folds_2013.csv.
"""
import argparse
from pathlib import Path

import pandas as pd

import common as C


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m3", type=Path, default=C.M3_DEFAULT)
    a = ap.parse_args()
    C.RESULTS.mkdir(parents=True, exist_ok=True)

    rows = C.check_hashes(a.m3)                      # stops on any mismatch
    for r in rows:
        print(f"hash {'OK ' if r['match'] else 'BAD'} {r['file']} {r['actual']}")
    meta = C.metadata_hashes(a.m3)
    for f, h in meta.items():
        print(f"recorded {f} {h}")
    pd.DataFrame(rows + [{"file": f, "expected": "", "actual": h, "match": ""} for f, h in meta.items()]) \
        .to_csv(C.RESULTS / "input_hashes.csv", index=False)

    cap = C.load_capacity(a.m3)
    pops, folds = [], []
    for cutoff in C.CUTOFFS:
        df = C.load_view(cutoff, a.m3)
        C.assert_2013(df)
        print(f"day {cutoff}: {len(df)} rows of 2013, {df[C.RUN].nunique()} runs, years {sorted(df['year'].unique())}")
        for run, g in df.groupby(C.RUN, sort=True):
            n, n_nc = len(g), int(g["y"].sum())
            crow = cap[(cap[C.RUN] == run) & (cap["cutoff_day"] == cutoff)].iloc[0]
            assert int(crow["enrolled"]) == n, (run, cutoff, crow["enrolled"], n)
            k3, k5 = int(crow["list_tutor_3"]), int(crow["list_tutor_5"])
            assert k3 == C.list_length(n, 3) and k5 == C.list_length(n, 5), (run, cutoff)
            pops.append({"cutoff": cutoff, "run": run, "code_module": g["code_module"].iloc[0],
                         "code_presentation": g["code_presentation"].iloc[0], "n_enrolments": n,
                         "n_noncompleters": n_nc, "base_rate": round(n_nc / n, 4),
                         "list_length_k3": k3, "list_length_k5": k5,
                         "max_attainable_k3": min(k3, n_nc), "max_attainable_k5": min(k5, n_nc),
                         "rule_flagged": int(g["early_sign_rule"].sum())})
        for run, train, valid in C.loro_folds(df):
            removed = df[(df[C.RUN] != run) & df["id_student"].isin(set(valid["id_student"]))]
            folds.append({"cutoff": cutoff, "validation_run": run, "n_valid": len(valid),
                          "n_train": len(train), "removed_rows": len(removed),
                          "removed_students": removed["id_student"].nunique(),
                          "training_runs": train[C.RUN].nunique()})
    pop = pd.DataFrame(pops)
    tot = pop.groupby("cutoff")[["n_enrolments", "n_noncompleters", "max_attainable_k5"]].sum()
    print(tot.to_string())
    pop.to_csv(C.RESULTS / "populations_2013.csv", index=False)
    fd = pd.DataFrame(folds)
    print(fd.to_string(index=False))
    fd.to_csv(C.RESULTS / "folds_2013.csv", index=False)
    for cutoff in C.CUTOFFS:
        df = C.load_view(cutoff, a.m3)
        rep = df.groupby("id_student")[C.RUN].nunique()
        rep_ids = set(rep[rep > 1].index)
        print(f"day {cutoff}: overlap removal over all folds: {fd[fd.cutoff == cutoff]['removed_rows'].sum()} rows, "
              f"{len(rep_ids)} distinct students in two or more 2013 runs")
    print("removed rows per fold: min", fd["removed_rows"].min(), "max", fd["removed_rows"].max(),
          "| removed students: min", fd["removed_students"].min(), "max", fd["removed_students"].max())


if __name__ == "__main__":
    main()
