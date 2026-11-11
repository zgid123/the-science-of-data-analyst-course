# Log: aq-3 / 10_crosscheck_earlier_run

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:25:44Z |
| Finished (UTC) | 2026-11-11T23:25:47Z |
| Duration | 2.6 s |
| Command | `python aq-3/code/10_crosscheck_earlier_run.py` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### Cross-check: this prototype against the team's earlier run (same frozen Level 1 design, independent code)

| quantity | this_prototype | earlier_run | difference |
| :---- | :---- | :---- | :---- |
| Rule-ranked list, pooled normalised recall | 0.7044 | 0.7044 | 0.0000 |
| Model M1, pooled normalised recall | 0.7257 | 0.7259 | -0.0003 |
| Difference model − rule | 0.0212 | 0.0215 | -0.0003 |
| Bootstrap interval, lower bound | 0.0065 | 0.0093 | -0.0027 |
| Bootstrap interval, upper bound | 0.0364 | 0.0337 | 0.0026 |
| Sign-flip p-value | 0.0032 | 0.0002 | 0.0029 |
| Runs won by the model (of 13) | 11.0000 | 12.0000 | -1.0000 |
| Calibration-in-the-large, M1, day 27 | 0.1240 | 0.0580 | 0.0660 |
| Calibration slope, M1, day 27 | 0.8726 | 1.3106 | -0.4380 |
| Fairness gap in recall, Declared disability | 0.0543 | 0.0541 | 0.0002 |
| Fairness gap in recall, Deprivation band 0–10% | 0.0117 | 0.0173 | -0.0056 |
| Fairness gap in recall, Deprivation band missing | -0.0690 | -0.0805 | 0.0115 |
[saved] aq-3/results/crosscheck_earlier_run.csv  (12 rows x 4 columns)

S1 verdict: this prototype PASS; earlier run S1 met.
S3 at day 27: this prototype met; earlier run 'S3: not met'.
Frozen M1 penalty at day 27: this prototype {"C": 10.0}; earlier run: M1 logistic primary cutoff=27 params={"C": 0.001} seed=20131 spec=models/frozen_M1_d27.spec.json

**Non-completers on the list per run**

| run | model_new | rule_new | model_earlier | rule_earlier | rule_identical | model_difference |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2014J | 41 | 38 | 41 | 38 | yes | 0 |
| BBB-2014B | 225 | 221 | 230 | 221 | yes | -5 |
| BBB-2014J | 261 | 244 | 258 | 244 | yes | 3 |
| CCC-2014B | 321 | 310 | 321 | 310 | yes | 0 |
| CCC-2014J | 389 | 383 | 387 | 383 | yes | 2 |
| DDD-2014B | 223 | 217 | 222 | 217 | yes | 1 |
| DDD-2014J | 287 | 273 | 284 | 273 | yes | 3 |
| EEE-2014B | 115 | 111 | 113 | 111 | yes | 2 |
| EEE-2014J | 173 | 156 | 172 | 156 | yes | 1 |
| FFF-2014B | 264 | 259 | 266 | 259 | yes | -2 |
| FFF-2014J | 341 | 338 | 341 | 338 | yes | 0 |
| GGG-2014B | 124 | 128 | 127 | 128 | yes | -3 |
| GGG-2014J | 106 | 108 | 109 | 108 | yes | -3 |

rule list identical in 13 of 13 runs; model lists differ by -1 non-completers in total (largest per-run difference 5).
[saved] aq-3/results/crosscheck_per_run.csv  (13 rows x 7 columns)

