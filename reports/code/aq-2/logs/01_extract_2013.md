# Log: aq-2 / 01_extract_2013

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:48:11Z |
| Finished (UTC) | 2026-11-12T15:48:13Z |
| Duration | 1.6 s |
| Command | `python aq-2/code/01_extract.py --scope 2013` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 extract, scope = 2013

[saved] aq-2/extracted-datasets/aq2_signs_d27_2013.csv  (11,811 rows x 35 columns)

enrolments: 11,811; runs: 9; non-completion rate: 0.4441
runs with a TMA or CMA due by day 27: 7 (9,960 enrolments); runs with a TMA due by day 27: 7 (9,960 enrolments)

**Task calendar and number of enrolments with each sign and sensitivity variant, by run**

| code_module | run | enrolments | run_has_task_due | run_has_tma_due | run_has_cma_due | with_task_missed | with_tma_late | with_inactive_last7 | with_low_activity | with_no_pre_activity | with_low_activity_q25 | with_low_activity_median | with_low_activity_dedup | with_any_task_late |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | AAA-2013J | 369 | yes | yes | no | 23 | 52 | 65 | 79 | 25 | 35 | 184 | 77 | 52 |
| BBB | BBB-2013B | 1,530 | yes | yes | no | 229 | 132 | 384 | 438 | 480 | 249 | 765 | 441 | 132 |
| BBB | BBB-2013J | 1,834 | yes | yes | no | 192 | 122 | 584 | 602 | 553 | 405 | 910 | 603 | 122 |
| DDD | DDD-2013B | 1,143 | yes | yes | yes | 251 | 23 | 87 | 296 | 136 | 147 | 571 | 305 | 979 |
| DDD | DDD-2013J | 1,647 | yes | yes | no | 282 | 39 | 161 | 439 | 170 | 227 | 823 | 447 | 39 |
| EEE | EEE-2013J | 927 | no | no | no | 0 | 0 | 171 | 170 | 211 | 92 | 461 | 169 | 0 |
| FFF | FFF-2013B | 1,454 | yes | yes | no | 134 | 96 | 175 | 350 | 151 | 157 | 726 | 350 | 96 |
| FFF | FFF-2013J | 1,983 | yes | yes | no | 174 | 113 | 311 | 492 | 213 | 246 | 991 | 491 | 113 |
| GGG | GGG-2013J | 924 | no | no | no | 0 | 0 | 506 | 309 | 358 | 234 | 458 | 305 | 0 |
[saved] aq-2/results/sign_calendar_2013.csv  (9 rows x 15 columns)

**Enrolments by activity level on days 0-27**

| activity_level5 | enrolments |
| :---- | :---- |
| 1 no click on days 0-27 | 607 |
| 2 below half the run median | 2,568 |
| 3 half the median to the median | 2,714 |
| 4 median to twice the median | 3,447 |
| 5 twice the median or more | 2,475 |

