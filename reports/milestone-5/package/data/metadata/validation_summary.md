# Validation summary (Task 8)

Written by `src/validate_prepared.py` at 2026-11-10T17:57:51Z. Each check names its expected and observed value.

| ID | Check | Expected | Observed | Status |
| :---- | :---- | :---- | :---- | :---- |
| V01a | enrolment rows and outcome mix equal raw studentInfo | 32,593; [('Distinction', 3024), ('Fail', 7052), ('Pass', 12361), ('Withdrawn', 10156)] | 32,593; [('Distinction', 3024), ('Fail', 7052), ('Pass', 12361), ('Withdrawn', 10156)] | PASS |
| V01b | students | 28,785 | 28,785 | PASS |
| V01c | population sizes equal the profile (C09) | {'d14': 28061, 'd13': 28069, 'd27': 27535} | {'d14': 28061, 'd13': 28069, 'd27': 27535} | PASS |
| V01d | non-completion count per feature view equals the profile | {'d13': 12708, 'd27': 12156} | {'d13': 12708, 'd27': 12156} | PASS |
| V02 | missing values after = before (no imputation in views) | {'imd_band Missing': 1111, 'date_registration': 45, 'TMA/CMA score null (submitted)': 173} | {'imd_band Missing': 1111, 'date_registration': 45, 'TMA/CMA score null (submitted)': 173} | PASS |
| V03 | key unique in every view | 0 duplicates | {'enrolment': 0, 'assessment_due': 0, 'student_week': 0, 'features_d13': 0, 'features_d27': 0, 'capacity_by_run': 0} | PASS |
| V04a | enrolment clicks + clicks after withdrawal = raw clicks | 39,605,099 | 39,506,354 + 98,745 = 39,605,099 | PASS |
| V04b | student_week clicks = enrolment clicks | 39,506,354 | 39,506,354 | PASS |
| V04c | de-duplicated total ≤ raw total | dedup ≤ raw | 38,247,422 ≤ 39,506,354 | PASS |
| V05 | every category in its expected set | no other label | {'imd_band': [], 'age_band': [], 'highest_education': [], 'final_result': [], 'start_month': [], 'split': []} | PASS |
| V06 | banked results carry no lateness and no missed status | 0 | 0 | PASS |
| V07 | ranges after = before (no capping) | score [0, 100]; credits [30, 655] | {'score': [0.0, 100.0], 'studied_credits': [30, 655]} | PASS |
| V08 | no student_week row after the withdrawal week | 0 | 0 | PASS |
| V09 | every logged join kept its rows | 25 joins, rows in = rows out | 25 | PASS |
| V10 | enrolments without any click row kept with 0 clicks | ≥ 3,365 | 3,554 | PASS |
| V11-d13 | 6 features recomputed from raw for all 28,069 rows (independent code) | 0 mismatches | {'clicks_0c': 0, 'clicks_pre': 0, 'active_days_0c': 0, 'sites_0c': 0, 'tasks_missed_c': 0, 'tasks_late_c': 0} | PASS |
| V13-d13 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 26,755 rows with later clicks; no forbidden column | 26,755 rows differ; forbidden [] | PASS |
| V11-d27 | 6 features recomputed from raw for all 27,535 rows (independent code) | 0 mismatches | {'clicks_0c': 0, 'clicks_pre': 0, 'active_days_0c': 0, 'sites_0c': 0, 'tasks_missed_c': 0, 'tasks_late_c': 0} | PASS |
| V13-d27 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 25,663 rows with later clicks; no forbidden column | 25,663 rows differ; forbidden [] | PASS |
| V12 | transform parameters identical with and without test rows, equal to the stored ones | identical | d13: identical, d27: identical | PASS |
| V14 | every column documented; predictor lists hold no audit, target or descriptive column | none | {'undocumented': [], 'wrong role': []} | PASS |
| V15 | no run in both partitions; 2013 = train; student flag recomputed | 9 train, 13 test runs; 0 flag mismatches | {'train runs': 9, 'test runs': 13, 'test enrolments of students seen in 2013': 1962, 'flag mismatches': 0} | PASS |

## Reports for the analysis plan

- cma_score_coverage_training_rows: {"d13": 0.0138, "d27": 0.0525}
- kpi_sensitivity: {"completion_day14": 0.5474, "enrolled_day14": 28061, "completion_without_138_flagged": 0.5493, "enrolled_without_flagged": 27962}
- rule_rate_overall: {"d13": 0.2021, "d27": 0.2881}
- rule_rate_cma_variant: {"d13": 0.2021, "d27": 0.4123}
- runs_where_rule_exceeds_list_of_5_per_20: {"13": 7, "27": 10}
- runs_where_rule_exceeds_list_of_3_per_20: {"13": 15, "27": 22}
- rule_rate_by_run_range: {"13": [0.0838, 0.4401], "27": [0.1791, 0.5476]}

Rule firing rates per run and cut-off (no outcome used): `rule_rates.csv`. Five training-run rows per cut-off (two with a missed task, two with a late task where the cut-off has one, one at random) recomputed from raw rows: `manual_check_d13.csv`, `manual_check_d27.csv`.
