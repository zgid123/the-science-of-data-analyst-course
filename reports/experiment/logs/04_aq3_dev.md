# Log: 04_aq3_dev

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-13T10:33:37Z |
| Finished (UTC) | 2026-11-13T10:33:41Z |
| Duration | 4.1 s |
| Command | `../../venv/bin/python code/04_aq3_dev.py` |
| Exit status | 0 |

## Console output

```text
wrote results/aq3_dev_summary.csv (6 rows)
config  norm_recall  gain_over_M1  folds_better_than_M1  chosen
    B3       0.5679       -0.1825                     0   False
    M1       0.7503        0.0000                     0    True
    M2       0.7490       -0.0013                     4   False
    M3       0.7487       -0.0017                     5   False
    M4       0.7480       -0.0024                     3   False
  RULE       0.7272       -0.0232                     2   False
{
 "B3_d27": {
  "C": 0.01
 },
 "M1_d27": {
  "C": 10
 },
 "M2_d27": {
  "C": 10
 },
 "M3_d27": {
  "learning_rate": 0.05,
  "max_depth": 3,
  "max_iter": 100
 },
 "M4_d27": {
  "learning_rate": 0.05,
  "max_depth": 2,
  "max_iter": 200
 },
 "B3_d13": {
  "C": 0.01
 },
 "M1_d13": {
  "C": 0.01
 },
 "M2_d13": {
  "C": 0.01
 },
 "M3_d13": {
  "learning_rate": 0.05,
  "max_depth": 2,
  "max_iter": 200
 },
 "M4_d13": {
  "learning_rate": 0.05,
  "max_depth": 2,
  "max_iter": 200
 }
}
```
