# Log: aq-2 / 01_extract_2013

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:00:23Z |
| Finished (UTC) | 2026-11-11T23:00:27Z |
| Duration | 3.7 s |
| Command | `python aq-2/code/01_extract.py --scope 2013` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 extract, scope = 2013

[saved] aq-2/extracted-datasets/aq2_signs_d27_2013.csv  (11,811 rows x 31 columns)

enrolments: 11,811; runs: 9; runs with a task due by day 27: 7; non-completion rate: 0.4441

**Share of enrolments with each sign, by module**

| code_module | enrolments | task_missed | tma_late | inactive_last7 | low_activity | no_pre_activity |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | 369 | 23 | 52 | 65 | 79 | 25 |
| BBB | 3,364 | 421 | 254 | 968 | 1,040 | 1,033 |
| DDD | 2,790 | 533 | 62 | 248 | 735 | 306 |
| EEE | 927 | 0 | 0 | 171 | 170 | 211 |
| FFF | 3,437 | 308 | 209 | 486 | 842 | 364 |
| GGG | 924 | 0 | 0 | 506 | 309 | 358 |

