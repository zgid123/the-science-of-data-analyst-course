# Log: aq-2 / 01_extract_2014

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T16:00:22Z |
| Finished (UTC) | 2026-11-12T16:00:24Z |
| Duration | 1.5 s |
| Command | `python aq-2/code/01_extract.py --scope 2014` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### AQ2 extract, scope = 2014

[saved] aq-2/extracted-datasets/aq2_signs_d27_2014.csv  (15,724 rows x 35 columns)

enrolments: 15,724; runs: 13; non-completion rate: 0.4395
runs with a TMA or CMA due by day 27: 9 (12,585 enrolments); runs with a TMA due by day 27: 7 (9,064 enrolments)

**Task calendar and number of enrolments with each sign and sensitivity variant, by run**

| code_module | run | enrolments | run_has_task_due | run_has_tma_due | run_has_cma_due | with_task_missed | with_tma_late | with_inactive_last7 | with_low_activity | with_no_pre_activity | with_low_activity_q25 | with_low_activity_median | with_low_activity_dedup | with_any_task_late |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AAA | AAA-2014J | 348 | yes | yes | no | 28 | 53 | 71 | 91 | 21 | 46 | 174 | 94 | 53 |
| BBB | BBB-2014B | 1,280 | yes | yes | no | 108 | 123 | 427 | 425 | 412 | 266 | 637 | 426 | 123 |
| BBB | BBB-2014J | 1,786 | yes | yes | no | 112 | 68 | 510 | 491 | 489 | 273 | 889 | 491 | 68 |
| CCC | CCC-2014B | 1,500 | yes | no | yes | 210 | 0 | 335 | 353 | 234 | 162 | 749 | 360 | 1,290 |
| CCC | CCC-2014J | 2,021 | yes | no | yes | 192 | 0 | 420 | 451 | 298 | 199 | 1,008 | 462 | 1,789 |
| DDD | DDD-2014B | 1,029 | yes | yes | no | 188 | 30 | 104 | 274 | 122 | 133 | 513 | 275 | 30 |
| DDD | DDD-2014J | 1,463 | yes | yes | no | 114 | 69 | 224 | 352 | 133 | 163 | 730 | 356 | 69 |
| EEE | EEE-2014B | 605 | no | no | no | 0 | 0 | 109 | 124 | 117 | 79 | 299 | 128 | 0 |
| EEE | EEE-2014J | 1,020 | no | no | no | 0 | 0 | 189 | 223 | 210 | 125 | 510 | 226 | 0 |
| FFF | FFF-2014B | 1,299 | yes | yes | no | 183 | 41 | 131 | 338 | 229 | 185 | 648 | 335 | 41 |
| FFF | FFF-2014J | 1,859 | yes | yes | no | 233 | 45 | 162 | 480 | 204 | 244 | 925 | 483 | 45 |
| GGG | GGG-2014B | 797 | no | no | no | 0 | 0 | 413 | 257 | 371 | 181 | 396 | 254 | 0 |
| GGG | GGG-2014J | 717 | no | no | no | 0 | 0 | 345 | 240 | 321 | 175 | 355 | 239 | 0 |
[saved] aq-2/results/sign_calendar_2014.csv  (13 rows x 15 columns)

**Enrolments by activity level on days 0-27**

| activity_level5 | enrolments |
| :---- | :---- |
| 1 no click on days 0-27 | 624 |
| 2 below half the run median | 3,475 |
| 3 half the median to the median | 3,734 |
| 4 median to twice the median | 4,660 |
| 5 twice the median or more | 3,231 |

