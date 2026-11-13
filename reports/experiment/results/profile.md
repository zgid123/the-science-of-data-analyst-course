# Data profile

## enrolment.parquet

- Rows read: 32,593 rows; columns: 39
- Exact duplicate rows: 0
- Candidate keys (unique, non-null here): `code_module` + `code_presentation` + `id_student`, `code_module` + `id_student` + `num_of_prev_attempts`

| Column | Type | Null % | Distinct | Values |
| --- | --- | --- | --- | --- |
| `code_module` | str | 0.0% | 7 | BBB (24%), FFF (24%), DDD (19%) |
| `code_presentation` | str | 0.0% | 4 | 2014J (35%), 2013J (27%), 2014B (24%) |
| `id_student` | int64 | 0.0% | 28,785 | min 3,733 · median 5.903e+05 · max 2.717e+06 |
| `gender` | str | 0.0% | 2 | M (55%), F (45%) |
| `region` | str | 0.0% | 13 | Scotland (11%), East Anglian Region (10%), London Region (10%) |
| `highest_education` | str | 0.0% | 5 | A Level or Equivalent (43%), Lower Than A Level (40%), HE Qualification (15%) |
| `imd_band` | str | 0.0% | 11 | 20-30% (11%), 30-40% (11%), 10-20% (11%) |
| `age_band` | str | 0.0% | 3 | 0-35 (70%), 35-55 (29%), 55<= (1%) |
| `num_of_prev_attempts` | int64 | 0.0% | 7 | min 0 · median 0 · max 6 · zeros 87% |
| `studied_credits` | int64 | 0.0% | 61 | min 30 · median 60 · max 655 |
| `disability` | str | 0.0% | 2 | N (90%), Y (10%) |
| `final_result` | str | 0.0% | 4 | Pass (38%), Withdrawn (31%), Fail (22%) |
| `date_registration` | float64 | 0.1% | 332 | min -322 · median -57 · max 167 |
| `date_unregistration` | float64 | 69.1% | 416 | min -365 · median 27 · max 444 |
| `enrolled_d13` | bool | 0.0% | 2 | True (86%), False (14%) |
| `enrolled_d14` | bool | 0.0% | 2 | True (86%), False (14%) |
| `enrolled_d27` | bool | 0.0% | 2 | True (84%), False (16%) |
| `year` | int64 | 0.0% | 2 | min 2,013 · median 2,014 · max 2,014 |
| `start_month` | str | 0.0% | 2 | J (62%), B (38%) |
| `run_length` | int64 | 0.0% | 7 | min 234 · median 262 · max 269 |
| `completed` | bool | 0.0% | 2 | False (53%), True (47%) |
| `non_completion` | bool | 0.0% | 2 | True (53%), False (47%) |
| `split` | str | 0.0% | 2 | test (58%), train (42%) |
| `registration_missing` | bool | 0.0% | 2 | False (100%), True (0%) |
| `withdrawal_day_missing` | bool | 0.0% | 2 | False (100%), True (0%) |
| `unregistered_not_withdrawn` | bool | 0.0% | 2 | False (100%), True (0%) |
| `unregistered_after_run_end` | object | 69.1% | 2 | False (100%), True (0%) |
| `registration_lead` | float64 | 0.1% | 332 | min -167 · median 57 · max 322 |
| `banked_results` | uint32 | 0.0% | 13 | min 0 · median 0 · max 12 · zeros 98% |
| `concurrent_runs` | uint32 | 0.0% | 3 | min 0 · median 0 · max 2 · zeros 93% |
| `student_in_training_runs` | bool | 0.0% | 2 | False (94%), True (6%) |
| `paired_run` | bool | 0.0% | 2 | True (82%), False (18%) |
| `first_missed_week` | float64 | 61.0% | 33 | min 2 · median 13 · max 35 |
| `tasks_due_while_enrolled` | uint32 | 0.0% | 14 | min 0 · median 6 · max 13 · zeros 15% |
| `tasks_missed_while_enrolled` | uint32 | 0.0% | 14 | min 0 · median 0 · max 13 · zeros 61% |
| `tasks_late_while_enrolled` | uint32 | 0.0% | 13 | min 0 · median 0 · max 12 · zeros 53% |
| `total_clicks` | int64 | 0.0% | 5,380 | min 0 · median 599 · max 2.414e+04 · zeros 11% |
| `total_clicks_dedup` | int64 | 0.0% | 5,257 | min 0 · median 572 · max 2.351e+04 · zeros 11% |
| `active_days` | uint32 | 0.0% | 284 | min 0 · median 40 · max 286 · zeros 11% |

## features_d13.parquet

- Rows read: 28,069 rows; columns: 50
- Exact duplicate rows: 0
- Candidate keys (unique, non-null here): `code_module` + `code_presentation` + `id_student`

| Column | Type | Null % | Distinct | Values |
| --- | --- | --- | --- | --- |
| `code_module` | str | 0.0% | 7 | FFF (24%), BBB (23%), DDD (19%) |
| `code_presentation` | str | 0.0% | 4 | 2014J (33%), 2013J (28%), 2014B (24%) |
| `id_student` | int64 | 0.0% | 25,234 | min 6,516 · median 5.883e+05 · max 2.71e+06 |
| `year` | int64 | 0.0% | 2 | min 2,013 · median 2,014 · max 2,014 |
| `split` | str | 0.0% | 2 | test (57%), train (43%) |
| `paired_run` | bool | 0.0% | 2 | True (82%), False (18%) |
| `student_in_training_runs` | bool | 0.0% | 2 | False (94%), True (6%) |
| `eval_withdrawal_day_unknown` | bool | 0.0% | 2 | False (100%), True (0%) |
| `final_result` | str | 0.0% | 4 | Pass (44%), Fail (25%), Withdrawn (20%) |
| `non_completion` | bool | 0.0% | 2 | False (55%), True (45%) |
| `early_sign_rule` | bool | 0.0% | 2 | False (80%), True (20%) |
| `early_sign_rule_cma` | bool | 0.0% | 2 | False (80%), True (20%) |
| `rule_missed` | bool | 0.0% | 2 | False (99%), True (1%) |
| `rule_tma_late` | bool | 0.0% | 2 | False (100%), True (0%) |
| `start_month` | str | 0.0% | 2 | J (61%), B (39%) |
| `highest_education` | str | 0.0% | 5 | A Level or Equivalent (44%), Lower Than A Level (39%), HE Qualification (15%) |
| `num_of_prev_attempts` | int64 | 0.0% | 7 | min 0 · median 0 · max 6 · zeros 87% |
| `studied_credits` | int64 | 0.0% | 51 | min 30 · median 60 · max 630 |
| `registration_lead` | float64 | 0.0% | 291 | min -13 · median 53 · max 311 |
| `banked_results` | uint32 | 0.0% | 13 | min 0 · median 0 · max 12 · zeros 98% |
| `clicks_pre` | int64 | 0.0% | 839 | min 0 · median 26 · max 3,731 · zeros 20% |
| `clicks_0c` | int64 | 0.0% | 1,025 | min 0 · median 74 · max 4,733 · zeros 10% |
| `active_days_0c` | uint32 | 0.0% | 15 | min 0 · median 4 · max 14 · zeros 10% |
| `sites_0c` | uint32 | 0.0% | 97 | min 0 · median 12 · max 155 · zeros 10% |
| `inactive_last7` | bool | 0.0% | 2 | False (80%), True (20%) |
| `activity_ratio_run` | float64 | 0.0% | 6,538 | min 0.005634 · median 1 · max 56.59 |
| `tasks_due_c` | uint32 | 0.0% | 2 | min 0 · median 0 · max 1 · zeros 95% |
| `tasks_missed_c` | uint32 | 0.0% | 2 | min 0 · median 0 · max 1 · zeros 99% |
| `tasks_late_c` | uint32 | 0.0% | 2 | min 0 · median 0 · max 1 · zeros 100% |
| `tma_late_c` | uint32 | 0.0% | 2 | min 0 · median 0 · max 1 · zeros 100% |
| `cma_late_c` | uint32 | 0.0% | 1 | min 0 · median 0 · max 0 · zeros 100% |
| `cma_marked_c` | uint32 | 0.0% | 3 | min 0 · median 0 · max 2 · zeros 99% |
| `cma_score_mean_c` | float64 | 98.9% | 63 | min 13 · median 88.5 · max 100 |
| `registration_missing` | bool | 0.0% | 2 | False (100%), True (0%) |
| `clicks_0c_dedup` | int64 | 0.0% | 999 | min 0 · median 71 · max 4,722 · zeros 10% |
| `clicks_pre14` | int64 | 0.0% | 694 | min 0 · median 20 · max 3,538 · zeros 23% |
| `days_since_last_click` | int64 | 0.0% | 15 | min 0 · median 2 · max 14 · zeros 32% |
| `trend_last_week` | int64 | 0.0% | 877 | min -4,037 · median 0 · max 1,149 · zeros 11% |
| `tasks_submitted_early_c` | uint32 | 0.0% | 4 | min 0 · median 0 · max 3 · zeros 93% |
| `clicks_oucontent_0c` | int64 | 0.0% | 362 | min 0 · median 6 · max 1,001 · zeros 30% |
| `clicks_forumng_0c` | int64 | 0.0% | 580 | min 0 · median 15 · max 1,799 · zeros 30% |
| `clicks_quiz_0c` | int64 | 0.0% | 417 | min 0 · median 0 · max 1,735 · zeros 68% |
| `clicks_homepage_0c` | int64 | 0.0% | 295 | min 0 · median 16 · max 4,129 · zeros 10% |
| `gender` | str | 0.0% | 2 | M (55%), F (45%) |
| `age_band` | str | 0.0% | 3 | 0-35 (70%), 35-55 (30%), 55<= (1%) |
| `disability` | str | 0.0% | 2 | N (90%), Y (10%) |
| `imd_band` | str | 0.0% | 11 | 20-30% (11%), 30-40% (11%), 10-20% (10%) |
| `region` | str | 0.0% | 13 | Scotland (11%), East Anglian Region (10%), South Region (10%) |
| `clicks_w1` | int64 | 0.0% | 682 | min 0 · median 33 · max 4,385 · zeros 19% |
| `clicks_w2` | int64 | 0.0% | 628 | min 0 · median 29 · max 1,566 · zeros 20% |

## features_d27.parquet

- Rows read: 27,535 rows; columns: 52
- Exact duplicate rows: 0
- Candidate keys (unique, non-null here): `id_student` + `activity_ratio_run`

| Column | Type | Null % | Distinct | Values |
| --- | --- | --- | --- | --- |
| `code_module` | str | 0.0% | 7 | FFF (24%), BBB (23%), DDD (19%) |
| `code_presentation` | str | 0.0% | 4 | 2014J (33%), 2013J (28%), 2014B (24%) |
| `id_student` | int64 | 0.0% | 24,841 | min 6,516 · median 5.887e+05 · max 2.71e+06 |
| `year` | int64 | 0.0% | 2 | min 2,013 · median 2,014 · max 2,014 |
| `split` | str | 0.0% | 2 | test (57%), train (43%) |
| `paired_run` | bool | 0.0% | 2 | True (82%), False (18%) |
| `student_in_training_runs` | bool | 0.0% | 2 | False (94%), True (6%) |
| `eval_withdrawal_day_unknown` | bool | 0.0% | 2 | False (100%), True (0%) |
| `final_result` | str | 0.0% | 4 | Pass (45%), Fail (26%), Withdrawn (19%) |
| `non_completion` | bool | 0.0% | 2 | False (56%), True (44%) |
| `early_sign_rule` | bool | 0.0% | 2 | False (71%), True (29%) |
| `early_sign_rule_cma` | bool | 0.0% | 2 | False (59%), True (41%) |
| `rule_missed` | bool | 0.0% | 2 | False (90%), True (10%) |
| `rule_tma_late` | bool | 0.0% | 2 | False (96%), True (4%) |
| `start_month` | str | 0.0% | 2 | J (61%), B (39%) |
| `highest_education` | str | 0.0% | 5 | A Level or Equivalent (44%), Lower Than A Level (39%), HE Qualification (15%) |
| `num_of_prev_attempts` | int64 | 0.0% | 7 | min 0 · median 0 · max 6 · zeros 87% |
| `studied_credits` | int64 | 0.0% | 51 | min 30 · median 60 · max 630 |
| `registration_lead` | float64 | 0.0% | 300 | min -27 · median 53 · max 311 |
| `banked_results` | uint32 | 0.0% | 13 | min 0 · median 0 · max 12 · zeros 98% |
| `clicks_pre` | int64 | 0.0% | 835 | min 0 · median 27 · max 3,731 · zeros 20% |
| `clicks_0c` | int64 | 0.0% | 1,616 | min 0 · median 176 · max 6,084 |
| `active_days_0c` | uint32 | 0.0% | 29 | min 0 · median 10 · max 28 |
| `sites_0c` | uint32 | 0.0% | 121 | min 0 · median 19 · max 257 |
| `inactive_last7` | bool | 0.0% | 2 | False (79%), True (21%) |
| `activity_ratio_run` | float64 | 0.0% | 9,912 | min 0.002342 · median 1 · max 52.74 |
| `tasks_due_c` | uint32 | 0.0% | 3 | min 0 · median 1 · max 2 · zeros 18% |
| `tasks_missed_c` | uint32 | 0.0% | 3 | min 0 · median 0 · max 2 · zeros 90% |
| `tasks_late_c` | uint32 | 0.0% | 3 | min 0 · median 0 · max 2 · zeros 82% |
| `tma_late_c` | uint32 | 0.0% | 2 | min 0 · median 0 · max 1 · zeros 96% |
| `cma_late_c` | uint32 | 0.0% | 2 | min 0 · median 0 · max 1 · zeros 85% |
| `cma_marked_c` | uint32 | 0.0% | 3 | min 0 · median 0 · max 2 · zeros 91% |
| `cma_score_mean_c` | float64 | 91.0% | 91 | min 0 · median 80 · max 100 |
| `registration_missing` | bool | 0.0% | 2 | False (100%), True (0%) |
| `clicks_0c_dedup` | int64 | 0.0% | 1,588 | min 0 · median 169 · max 6,008 |
| `clicks_pre14` | int64 | 0.0% | 694 | min 0 · median 20 · max 3,538 · zeros 23% |
| `days_since_last_click` | int64 | 0.0% | 29 | min 0 · median 2 · max 28 · zeros 32% |
| `trend_last_week` | int64 | 0.0% | 864 | min -1,489 · median -6 · max 2,149 · zeros 10% |
| `tasks_submitted_early_c` | uint32 | 0.0% | 4 | min 0 · median 0 · max 3 · zeros 92% |
| `clicks_oucontent_0c` | int64 | 0.0% | 586 | min 0 · median 20 · max 1,912 · zeros 20% |
| `clicks_forumng_0c` | int64 | 0.0% | 857 | min 0 · median 30 · max 3,301 · zeros 21% |
| `clicks_quiz_0c` | int64 | 0.0% | 575 | min 0 · median 0 · max 1,784 · zeros 54% |
| `clicks_homepage_0c` | int64 | 0.0% | 465 | min 0 · median 34 · max 4,160 |
| `gender` | str | 0.0% | 2 | M (55%), F (45%) |
| `age_band` | str | 0.0% | 3 | 0-35 (70%), 35-55 (30%), 55<= (1%) |
| `disability` | str | 0.0% | 2 | N (91%), Y (9%) |
| `imd_band` | str | 0.0% | 11 | 30-40% (11%), 20-30% (11%), 10-20% (10%) |
| `region` | str | 0.0% | 13 | Scotland (11%), East Anglian Region (10%), South Region (10%) |
| `clicks_w1` | int64 | 0.0% | 681 | min 0 · median 34 · max 4,385 · zeros 19% |
| `clicks_w2` | int64 | 0.0% | 628 | min 0 · median 30 · max 1,566 · zeros 19% |
| `clicks_w3` | int64 | 0.0% | 659 | min 0 · median 45 · max 1,709 · zeros 16% |
| `clicks_w4` | int64 | 0.0% | 614 | min 0 · median 25 · max 2,334 · zeros 21% |

## assessment_due.parquet

- Rows read: 286,898 rows; columns: 14
- Exact duplicate rows: 0
- Candidate keys (unique, non-null here): `id_student` + `id_assessment`

| Column | Type | Null % | Distinct | Values |
| --- | --- | --- | --- | --- |
| `code_module` | str | 0.0% | 7 | FFF (32%), BBB (26%), DDD (16%) |
| `code_presentation` | str | 0.0% | 4 | 2014J (29%), 2013J (27%), 2014B (24%) |
| `id_student` | int64 | 0.0% | 28,785 | min 3,733 · median 5.852e+05 · max 2.717e+06 |
| `id_assessment` | int64 | 0.0% | 182 | min 1,752 · median 2.536e+04 · max 3.744e+04 |
| `assessment_type` | str | 0.0% | 2 | TMA (57%), CMA (43%) |
| `due_day` | int64 | 0.0% | 70 | min 12 · median 144 · max 241 |
| `weight` | float64 | 0.0% | 23 | min 0 · median 9 · max 35 · zeros 28% |
| `date_submitted` | float64 | 41.1% | 301 | min -11 · median 112 · max 608 |
| `is_banked` | float64 | 41.1% | 2 | min 0 · median 0 · max 1 · zeros 99% |
| `score` | float64 | 41.2% | 101 | min 0 · median 80 · max 100 |
| `status` | str | 0.0% | 4 | not_submitted (41%), on_time (41%), late (17%) |
| `lateness_days` | float64 | 41.8% | 390 | min -246 · median -1 · max 372 · zeros 18% |
| `due_while_enrolled` | bool | 0.0% | 2 | True (76%), False (24%) |
| `due_week` | int64 | 0.0% | 33 | min 2 · median 21 · max 35 |
