# Transformation log
Written by `src/prepare_data.py` at 2026-11-10T17:57:48Z. One row per operation, in the order run; every join is a checked left join (rows in = rows out).

| Step | Operation | Rows in | Rows out | Note |
| :---- | :---- | :---- | :---- | :---- |
| 1 load | courses.csv (SHA-256 pinned, columns as documented) |  | 22 |  |
| 1 load | assessments.csv (SHA-256 pinned, columns as documented) |  | 206 |  |
| 1 load | vle.csv (SHA-256 pinned, columns as documented) |  | 6,364 |  |
| 1 load | studentInfo.csv (SHA-256 pinned, columns as documented) |  | 32,593 |  |
| 1 load | studentRegistration.csv (SHA-256 pinned, columns as documented) |  | 32,593 |  |
| 1 load | studentAssessment.csv (SHA-256 pinned, columns as documented) |  | 173,912 |  |
| 1 load | studentVle.csv (SHA-256 pinned, columns as documented) |  | 10,655,280 |  |
| 2 population | studentInfo + studentRegistration | 32,593 | 32,593 | left join, rows kept |
| 2 population | + courses (run length) | 32,593 | 32,593 | left join, rows kept |
| 2 population | flag enrolled_d13 | 32,593 | 28,069 | enrolled at the day (C09) |
| 2 population | flag enrolled_d14 | 32,593 | 28,061 | enrolled at the day (C09) |
| 2 population | flag enrolled_d27 | 32,593 | 27,535 | enrolled at the day (C09) |
| 3 standardise | imd_band label '10-20' -> '10-20%' | 3,516 | 0 |  |
| 3 standardise | year, start_month, completed, non_completion, split derived | 32,593 | 32,593 |  |
| 3 standardise | tasks = TMA and CMA (exams excluded, DQ08) | 206 | 182 |  |
| 4 keys | studentVle rows -> enrolment x day (records, clicks, clicks_dedup) | 10,655,280 | 1,808,119 | clicks 39,605,099, de-duplicated 38,343,063 |
| 4 keys | studentVle rows -> distinct enrolment x site x day | 10,655,280 | 8,459,320 |  |
| 5 missing | imd_band missing -> category 'Missing' (no imputation) | 1,111 | 1,111 |  |
| 5 missing | flag registration_missing | 32,593 | 45 |  |
| 5 missing | flag withdrawal_day_missing | 32,593 | 93 |  |
| 5 missing | flag unregistered_not_withdrawn | 32,593 | 9 |  |
| 5 missing | flag unregistered_after_run_end | 32,593 | 1 |  |
| 6 truncate | enrolment x day click records up to the unregistration day | 1,808,119 | 1,802,593 | clicks removed 98,745 |
| 6 truncate | enrolment x site x day records up to the unregistration day | 8,459,320 | 8,435,429 |  |
| 7 integrate | enrolment x task grid (TMA, CMA of the run) | 32,593 | 286,898 |  |
| 7 integrate | + submission (if any) | 286,898 | 286,898 | left join, rows kept |
| 7 integrate | TMA/CMA submissions placed in the grid | 168,953 | 168,953 |  |
| 9 views | + banked results | 32,593 | 32,593 | left join, rows kept |
| 9 views | + concurrent runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + student seen in training runs | 32,593 | 32,593 | left join, rows kept |
| 9 views | + paired run flag | 32,593 | 32,593 | left join, rows kept |
| 9 views | + first missed task week | 32,593 | 32,593 | left join, rows kept |
| 9 views | + tasks while enrolled | 32,593 | 32,593 | left join, rows kept |
| 9 views | + whole-run activity (truncated at withdrawal) | 32,593 | 32,593 | left join, rows kept |
| 9 views | student_week grid + weekly clicks | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + weekly distinct resources | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | + logging-gap flag (DQ15) | 1,052,344 | 1,052,344 | left join, rows kept |
| 9 views | student_week rows (weeks -3..run end, cut at withdrawal) |  | 1,052,344 | clicks before week -3 not in this view: 0 |
| 8 features d13 | + activity up to the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + distinct resources | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks due by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + CMA marks known by the cut-off | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + tasks submitted before their due day (due after the cut-off) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | + run median of clicks up to the cut-off (same run, no outcome) | 28,069 | 28,069 | left join, rows kept |
| 8 features d13 | features built; max event day <= cut-off | 28,069 | 28,069 | early_sign_rule 5,673 |
| 8 features d27 | + activity up to the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + distinct resources | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks due by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + CMA marks known by the cut-off | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + tasks submitted before their due day (due after the cut-off) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | + run median of clicks up to the cut-off (same run, no outcome) | 27,535 | 27,535 | left join, rows kept |
| 8 features d27 | features built; max event day <= cut-off | 27,535 | 27,535 | early_sign_rule 7,933 |
| 10 persist | processed/enrolment.parquet |  | 32,593 | 39 columns |
| 10 persist | processed/assessment_due.parquet |  | 286,898 | 14 columns |
| 10 persist | processed/student_week.parquet |  | 1,052,344 | 10 columns |
| 10 persist | processed/features_d13.parquet |  | 28,069 | 50 columns |
| 10 persist | processed/features_d27.parquet |  | 27,535 | 52 columns |
| 10 persist | processed/capacity_by_run.parquet |  | 44 | 9 columns |
