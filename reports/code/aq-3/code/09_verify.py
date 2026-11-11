"""AQ3 step 9 – independent verification of the decision-critical numbers.

V1  refit the chosen model from the development table with the frozen hyperparameters: its test scores must equal the
    scores written at the test (the frozen file is reproducible from data + code + seed);
V2  recompute the S1 point estimates from the scored table with a second, deliberately different code path
    (a plain per-run sort on (score, tie-break) – no shared metric function);
V3  the list counts of AQ4 and of the error analysis agree with the S1 counts;
V4  no audit column and no outcome column is a model input;
V5  every feature used is dated on or before the cut-off according to the Milestone 3 dictionary roles
    (only 'predictor' and 'predictor_extended' columns enter a model);
V6  the test-access record starts after the freeze time;
V7  the data files read still match the Milestone 3 manifest.
Writes results/verification.csv; exits 1 on a failure.
"""

import json
import re
import sys

import numpy as np
import polars as pl

from aq3_models import AQ, CONFIGS, EXTRACT, MODELS, RESULTS, fit_final, lib, predict, predictors

freeze = json.loads(lib.FREEZE_FILE.read_text())
chosen = freeze["chosen_config"]
lib.open_test_outcomes("aq-3/code/09_verify.py", "independent verification of the S1 numbers")
out = []


def check(cid, what, ok, detail):
    out.append({"check": cid, "what": what, "result": "PASS" if ok else "FAIL", "detail": detail})


# V1 (scores are stored with 6 decimals, so the tolerance is 1e-6) and V1b (rounding does not move any list)
worst, tp_full, tp_saved = 0.0, 0, 0
for cut in (27, 13):
    dev = pl.read_csv(EXTRACT / f"aq3_dev_d{cut}.csv")
    blind = pl.read_csv(EXTRACT / f"aq3_test_features_blind_d{cut}.csv")
    hp = freeze["models"][f"{chosen}_d{cut}"]["hyperparameters"]
    p = predict(fit_final(chosen, cut, dev, hp), blind)
    sc = pl.read_csv(EXTRACT / f"aq3_test_scored_d{cut}.csv").sort(lib.KEYS)
    mine = blind.select(lib.KEYS).with_columns(pl.Series("p", p)).sort(lib.KEYS)["p"].to_numpy()
    worst = max(worst, float(np.max(np.abs(mine - sc[chosen].to_numpy()))))
    if cut == 27:
        for run in sc["run"].unique().to_list():
            m = (sc["run"] == run).to_numpy()
            y, tie, k = sc["non_completion"].to_numpy()[m], sc["tiebreak_u"].to_numpy()[m], lib.list_len(int(m.sum()), 5)
            tp_full += int(y[lib.rank_desc(mine[m], tie) < k].sum())
            tp_saved += int(y[lib.rank_desc(sc[chosen].to_numpy()[m], tie) < k].sum())
check("V1", "refitted model reproduces the saved test scores (stored with 6 decimals)", worst < 1e-6, f"largest absolute score difference over both cut-offs: {worst:.2e}")
check("V1b", "lists from unrounded scores hold the same number of non-completers as lists from the stored scores", tp_full == tp_saved,
      f"day 27, 5 per 20: {tp_full:,} from unrounded scores, {tp_saved:,} from stored scores")

# V2 – second code path
d = pl.read_csv(EXTRACT / "aq3_test_scored_d27.csv").to_dicts()
by_run = {}
for row in d:
    by_run.setdefault(row["run"], []).append(row)
tp = {"model": 0, "rule": 0}
ceil_sum = 0
for run, rows in by_run.items():
    n = len(rows)
    k = 5 * -(-n // 20)
    pos = sum(1 for r in rows if r["non_completion"])
    ceil_sum += min(k, pos)
    for tag, col in (("model", chosen), ("rule", "B2_rule")):
        top = sorted(rows, key=lambda r: (-r[col], r["tiebreak_u"]))[:k]
        tp[tag] += sum(1 for r in top if r["non_completion"])
s1 = pl.read_csv(RESULTS / "s1_gate.csv").row(0, named=True)
ok2 = tp["model"] == s1["tp_a"] and tp["rule"] == s1["tp_b"] and ceil_sum == s1["max_attainable"]
check("V2", "S1 counts recomputed by a second code path", ok2,
      f"model {tp['model']:,} / rule {tp['rule']:,} / ceiling {ceil_sum:,} against saved {s1['tp_a']:,} / {s1['tp_b']:,} / {s1['max_attainable']:,}; "
      f"normalised recall {tp['model'] / ceil_sum:.4f} and {tp['rule'] / ceil_sum:.4f}")

# V3
q = pl.read_csv(AQ.parent / "aq-4" / "results" / "list_quality_pooled.csv").filter((pl.col("cutoff") == 27) & (pl.col("per20") == 5))
m4 = int(q.filter(pl.col("ranking") == "model")["non_completers_on_list"][0]); r4 = int(q.filter(pl.col("ranking") == "rule")["non_completers_on_list"][0])
e = pl.read_csv(RESULTS / "errors_by_run.csv")
ok3 = m4 == s1["tp_a"] and r4 == s1["tp_b"] and int(e["model_hits"].sum()) == s1["tp_a"] and int(e["rule_hits"].sum()) == s1["tp_b"]
check("V3", "AQ4 list counts and error-analysis counts equal the S1 counts", ok3, f"AQ4 {m4:,} / {r4:,}; error analysis {int(e['model_hits'].sum()):,} / {int(e['rule_hits'].sum()):,}")

# V4, V5
dic = (lib.PREPARED / "metadata" / "data_dictionary.md").read_text()
sec = dic.split("## features_d27.parquet")[1].split("## capacity_by_run")[0]
roles = {m.group(1): m.group(2) for m in re.finditer(r"^\| (\w+) \| \w+ \| (\w+) \|", sec, re.M)}
used = sorted({c for cfg in CONFIGS for cut in (13, 27) for c in predictors(cfg, cut)})
bad_role = [c for c in used if roles.get(c) not in ("predictor", "predictor_extended") and c != "code_module"]
check("V4", "no audit or outcome column among the model inputs", not (set(used) & set(lib.AUDIT_COLS + lib.OUTCOME_COLS)), f"{len(used)} input columns checked")
check("V5", "every model input has the role predictor or predictor_extended in the Milestone 3 dictionary (code_module is the run's module)", not bad_role,
      f"columns with another role: {bad_role or 'none'}")

# V6
acc = [l for l in lib.TEST_ACCESS_LOG.read_text().splitlines() if l.startswith("| 20")]
first = acc[0].split("|")[1].strip()
check("V6", "first test access is after the freeze", first >= freeze["frozen_utc"], f"freeze {freeze['frozen_utc']}; first access {first}; {len(acc)} accesses recorded")

# V7
h = lib.verify_prepared(["features_d13.parquet", "features_d27.parquet", "enrolment.parquet", "assessment_due.parquet", "capacity_by_run.parquet"])
check("V7", "prepared files still match the Milestone 3 manifest", True, f"{len(h)} files hash-checked")

res = pl.DataFrame(out)
lib.banner("AQ3 verification ledger")
print(lib.md_table(res))
lib.save_csv(res, RESULTS / "verification.csv")
sys.exit(0 if (res["result"] == "PASS").all() else 1)
