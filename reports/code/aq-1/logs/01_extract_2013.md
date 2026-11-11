# Log: aq-1 / 01_extract_2013

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T22:58:39Z |
| Finished (UTC) | 2026-11-11T22:58:40Z |
| Duration | 1.0 s |
| Command | `python aq-1/code/01_extract.py --scope 2013` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ1 extract, scope = 2013

prepared dataset: OULAD-N04-prepared-1.0 - hashes: {'enrolment.parquet': '1d1e397ac67ce774fec8be5d23bbf988ab70eb11f1bda5efc3d2f05510900a78', 'assessment_due.parquet': 'f67d7916dd95c2ab2321140b277a554145163b59e8d99f68b13d2d6c415cb498'}
[saved] aq-1/extracted-datasets/aq1_enrolments_2013.csv  (13,529 rows x 24 columns)  – all enrolments of the scope
[saved] aq-1/extracted-datasets/aq1_task_schedule_2013.csv  (83 rows x 8 columns)  – task calendar per run
[saved] aq-1/extracted-datasets/aq1_first_missed_recomputed_2013.csv  (5,753 rows x 5 columns)  – enrolments with at least one missed task

enrolments: 13,529; runs: 9; enrolled at day 14: 12,076
task rows read: 134,066; tasks in the calendar: 83

