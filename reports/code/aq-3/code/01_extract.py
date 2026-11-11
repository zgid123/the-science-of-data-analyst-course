"""AQ3 step 1 – reproduce the data input (brief step 1) and extract the modelling tables.

Reads   features_d13.parquet, features_d27.parquet, capacity_by_run.parquet (hash-checked against the Milestone 3 manifest)
Writes  extracted-datasets/aq3_dev_d<c>.csv                 2013 runs: keys, outcome, rule columns, allowed predictors
        extracted-datasets/aq3_test_features_blind_d<c>.csv 2014 runs: the same columns WITHOUT any outcome column
        results/input_check.csv                             row counts, hashes, capacity cross-check

No audit column (gender, age, disability, deprivation band, region) is written to a modelling table.
"""

import polars as pl

from aq3_models import EXTRACT, RESULTS, lib, model_columns

lib.banner("AQ3 input check and extraction")
files = ["features_d13.parquet", "features_d27.parquet", "capacity_by_run.parquet"]
hashes = lib.verify_prepared(files)
for f, h in hashes.items():
    print(f"- `{f}` sha256 `{h}` = manifest: PASS")
cap = lib.load_view("capacity_by_run", ())
rows = []
for c in (13, 27):
    tr = lib.load_features(c, "train")
    te = lib.load_features(c, "test_blind")
    assert not set(lib.OUTCOME_COLS) & set(te.columns), "outcome column in the blind test table"
    ident = lib.KEYS + ["run", "start_month", "split", "paired_run", "student_in_training_runs", "tiebreak_u"]
    rule = ["early_sign_rule", "early_sign_rule_cma", "rule_missed", "rule_tma_late"]
    feats = [x for x in model_columns(c) if x not in ident]
    dev = tr.select(ident + ["final_result", "non_completion"] + rule + feats).sort(lib.KEYS)
    blind = te.select(ident + rule + feats).sort(lib.KEYS)
    assert not set(lib.AUDIT_COLS) & set(dev.columns) and not set(lib.AUDIT_COLS) & set(blind.columns)
    lib.save_csv(dev, EXTRACT / f"aq3_dev_d{c}.csv", "development rows with outcome")
    lib.save_csv(blind, EXTRACT / f"aq3_test_features_blind_d{c}.csv", "test rows, no outcome column")
    # capacity cross-check: list length rule against the prepared capacity table
    both = pl.concat([tr.select("run"), te.select("run")]).group_by("run").agg(pl.len().alias("n"))
    capc = cap.filter(pl.col("cutoff_day") == c).select("run", "enrolled", "list_tutor_3", "list_tutor_5")
    j = both.join(capc, on="run")
    ok = all(n == e and lib.list_len(n, 5) == k5 and lib.list_len(n, 3) == k3 for n, e, k3, k5 in j.select("n", "enrolled", "list_tutor_3", "list_tutor_5").iter_rows())
    rows.append({"cutoff": c, "train_rows": dev.height, "train_non_completers": int(dev["non_completion"].sum()),
                 "train_runs": dev["run"].n_unique(), "test_rows": blind.height, "test_runs": blind["run"].n_unique(),
                 "predictors_available": len(feats) + 2, "capacity_rule_matches_prepared_table": ok,
                 "flagged_by_rule_share_all_runs": float(pl.concat([tr.select("early_sign_rule"), te.select("early_sign_rule")])["early_sign_rule"].mean())})
out = pl.DataFrame(rows)
print("\n" + lib.md_table(out, digits=4))
lib.save_csv(out, RESULTS / "input_check.csv")
expected = {13: (12080, 5519, 15989), 27: (11811, 5245, 15724)}
for r in rows:
    assert (r["train_rows"], r["train_non_completers"], r["test_rows"]) == expected[r["cutoff"]], "counts differ from the Level 1 report (Table A.6)"
    assert r["capacity_rule_matches_prepared_table"]
print("\nCounts equal the Level 1 report, Table A.6 (12,080 / 5,519 / 15,989 at day 13; 11,811 / 5,245 / 15,724 at day 27): PASS")
print("List-length rule reproduces capacity_by_run.parquet in all 22 runs at both cut-offs: PASS")
