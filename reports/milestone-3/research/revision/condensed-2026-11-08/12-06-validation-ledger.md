## Appendix VI – Validation Ledger

Table A.18 lists the 22 checks of `src/validate_prepared.py` with their expected and observed values, from `data/metadata/validation_summary.json`.

**Table A.18. Validation ledger**

| ID | Check | Expected | Observed | Status |
| :---- | :---- | :---- | :---- | :---- |
| V01a | enrolment rows and outcome mix equal raw studentInfo | 32,593; Distinction 3,024, Fail 7,052, Pass 12,361, Withdrawn 10,156 | as expected | PASS |
| V01b | students | 28,785 | as expected | PASS |
| V01c | population sizes equal the profile (C09) | d14: 28,061; d13: 28,069; d27: 27,535 | as expected | PASS |
| V01d | non-completion count per feature view equals the profile | d13: 12,708; d27: 12,156 | as expected | PASS |
| V02 | missing values after = before (no imputation in views) | imd_band Missing: 1,111; date_registration: 45; TMA/CMA score null (submitted): 173 | as expected | PASS |
| V03 | key unique in every view | 0 duplicates | 0 in all 6 | PASS |
| V04a | enrolment clicks + clicks after withdrawal = raw clicks | 39,605,099 | 39,506,354 + 98,745 = 39,605,099 | PASS |
| V04b | student_week clicks = enrolment clicks | 39,506,354 | as expected | PASS |
| V04c | de-duplicated total ≤ raw total | dedup ≤ raw | 38,247,422 ≤ 39,506,354 | PASS |
| V05 | every category in its expected set | no other label | none | PASS |
| V06 | banked results carry no lateness and no missed status | 0 | as expected | PASS |
| V07 | ranges after = before (no capping) | score 0–100; credits 30–655 | score: 0–100; studied_credits: 30–655 | PASS |
| V08 | no student_week row after the withdrawal week | 0 | as expected | PASS |
| V09 | every logged join kept its rows | 25 joins, rows in = rows out | 25 | PASS |
| V10 | enrolments without any click row kept with 0 clicks | ≥ 3,365 | 3,554 | PASS |
| V11-d13 | 6 features recomputed from raw for all 28,069 rows (independent code) | 0 mismatches | 0 in all 6 | PASS |
| V11-d27 | 6 features recomputed from raw for all 27,535 rows (independent code) | 0 mismatches | 0 in all 6 | PASS |
| V12 | transform parameters identical with and without test rows, equal to the stored ones | identical | d13: identical, d27: identical | PASS |
| V13-d13 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 26,755 rows with later clicks; no forbidden column | 26,755 rows differ; no forbidden column | PASS |
| V13-d27 | pipeline clicks differ from an unfiltered recount exactly for students with later clicks; no target-derived or whole-run column in the view | 25,663 rows with later clicks; no forbidden column | 25,663 rows differ; no forbidden column | PASS |
| V14 | every column documented; predictor lists hold no audit, target or descriptive column | none | as expected | PASS |
| V15 | no run in both partitions; 2013 = train; student flag recomputed | 9 train, 13 test runs; 0 flag mismatches | train runs: 9; test runs: 13; test enrolments of students seen in 2013: 1,962; flag mismatches: 0 | PASS |

The validation also reports, without using any test outcome, the figures that the Milestone 4 plan relies on: the early-sign rule flags 20.2% of enrolled students at day 13 and 28.8% at day 27 (41.2% with CMA lateness); CMA marks known by the cut-off cover 1.4% and 5.2% of training rows; and completion in the day-14 population is 54.7%, or 54.9% without the 138 enrolments flagged for an unknown withdrawal day (93) or registration day (45). Rule rates per run and cut-off are in `rule_rates.csv`.
