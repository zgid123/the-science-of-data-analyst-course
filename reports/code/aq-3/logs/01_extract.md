# Log: aq-3 / 01_extract

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:48:16Z |
| Finished (UTC) | 2026-11-12T15:48:17Z |
| Duration | 1.5 s |
| Command | `python aq-3/code/01_extract.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ3 input check and extraction

- `features_d13.parquet` sha256 `c58a44150e8c367cd702303998bb028aed3c9b763e89e5b171d229b075b32bd6` = manifest: PASS
- `features_d27.parquet` sha256 `4bf8a482b9ec7fa42c28ee96579c738faea8219124b74110ae53f54efcff6347` = manifest: PASS
- `capacity_by_run.parquet` sha256 `38f6868c2b74fcc7998c4c589b5d1a9420b6c11fd1bf2964e7abd86311f99e08` = manifest: PASS
[saved] aq-3/extracted-datasets/aq3_dev_d13.csv  (12,080 rows x 44 columns)  – development rows with outcome
[saved] aq-3/extracted-datasets/aq3_test_features_blind_d13.csv  (15,989 rows x 42 columns)  – test rows, no outcome column
[saved] aq-3/extracted-datasets/aq3_dev_d27.csv  (11,811 rows x 46 columns)  – development rows with outcome
[saved] aq-3/extracted-datasets/aq3_test_features_blind_d27.csv  (15,724 rows x 44 columns)  – test rows, no outcome column

| cutoff | train_rows | train_non_completers | train_runs | test_rows | test_runs | predictors_available | capacity_rule_matches_prepared_table | flagged_by_rule_share_all_runs |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 13 | 12,080 | 5,519 | 9 | 15,989 | 13 | 31 | yes | 0.2021 |
| 27 | 11,811 | 5,245 | 9 | 15,724 | 13 | 33 | yes | 0.2881 |
[saved] aq-3/results/input_check.csv  (2 rows x 9 columns)

Counts equal the Level 1 report, Table A.6 (12,080 / 5,519 / 15,989 at day 13; 11,811 / 5,245 / 15,724 at day 27): PASS
List-length rule reproduces capacity_by_run.parquet in all 22 runs at both cut-offs: PASS

