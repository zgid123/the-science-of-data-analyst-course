# Log: aq-1 / 01_extract_all

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:00:29Z |
| Finished (UTC) | 2026-11-12T16:00:29Z |
| Duration | 0.5 s |
| Command | `python aq-1/code/01_extract.py --scope all` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ1 extract, scope = all

prepared dataset: OULAD-N04-prepared-1.0 - hashes: {'enrolment.parquet': '1d1e397ac67ce774fec8be5d23bbf988ab70eb11f1bda5efc3d2f05510900a78', 'assessment_due.parquet': 'f67d7916dd95c2ab2321140b277a554145163b59e8d99f68b13d2d6c415cb498'}
[saved] aq-1/extracted-datasets/aq1_enrolments_all.csv  (32,593 rows x 24 columns)  – all enrolments of the scope
[saved] aq-1/extracted-datasets/aq1_task_schedule_all.csv  (182 rows x 8 columns)  – task calendar per run
[saved] aq-1/extracted-datasets/aq1_first_missed_recomputed_all.csv  (12,720 rows x 5 columns)  – enrolments with at least one missed task

enrolments: 32,593; runs: 22; enrolled at day 14: 28,061
task rows read: 286,898; tasks in the calendar: 182

