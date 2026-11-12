# Log: logs / tests_lib

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:48:06Z |
| Finished (UTC) | 2026-11-12T15:48:08Z |
| Duration | 1.7 s |
| Command | `python common/tests/test_lib.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output

- PASS: list_len(40, 5) = 10
- PASS: list_len(41, 5) = 15
- PASS: list_len(3, 5) capped at n = 3
- PASS: rank_desc: higher score first, tie by smaller tie-break
- PASS: tp = 2, recall = 0.5, precision = 2/3
- PASS: attainable recall = 3/4 and normalised recall = 2/3
- PASS: lift = precision / base rate = (2/3)/0.4
- PASS: random list expects k x base rate = 1.2 non-completers
- PASS: ceiling = all non-completers when the list is longer
- PASS: expected_tp_with_ties = 4/3
- PASS: 13 positive differences: p = 1/8192
- PASS: symmetric differences: p = 3/4 (sum >= 0 in 3 of 4 assignments)
- PASS: three positive differences: p = 1/8
- PASS: identical rankings: every bootstrap difference is 0
- PASS: perfect ranking: normalised recall 1 in every replicate, reversed ranking far below
- PASS: well-calibrated synthetic risks: |citl| < 0.08 and |slope - 1| < 0.08
- PASS: risks 15 points too high: citl clearly negative

17 of 17 checks passed (synthetic inputs, code paths only)

