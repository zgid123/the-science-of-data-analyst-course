# Log: aq-1 / 03_checks_all

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-11T23:33:51Z |
| Finished (UTC) | 2026-11-11T23:33:51Z |
| Duration | 0.6 s |
| Command | `python aq-1/code/03_checks.py --scope all` (run from `reports/code`) |
| Git commit | `5c1f96f` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output


### C2 – prepared view against raw tables, per run (KPI population)

| run | n_prepared | events_prepared | n_raw | events_raw | agree |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AAA-2013J | 370 | 92 | 370 | 92 | yes |
| AAA-2014J | 350 | 97 | 350 | 97 | yes |
| BBB-2013B | 1,606 | 804 | 1,606 | 804 | yes |
| BBB-2013J | 1,851 | 781 | 1,851 | 781 | yes |
| BBB-2014B | 1,289 | 564 | 1,289 | 564 | yes |
| BBB-2014J | 1,791 | 648 | 1,791 | 648 | yes |
| CCC-2014B | 1,591 | 928 | 1,591 | 928 | yes |
| CCC-2014J | 2,079 | 1,066 | 2,079 | 1,066 | yes |
| DDD-2013B | 1,197 | 688 | 1,197 | 688 | yes |
| DDD-2013J | 1,675 | 849 | 1,675 | 849 | yes |
| DDD-2014B | 1,050 | 572 | 1,050 | 572 | yes |
| DDD-2014J | 1,479 | 687 | 1,479 | 687 | yes |
| EEE-2013J | 933 | 325 | 933 | 325 | yes |
| EEE-2014B | 613 | 256 | 613 | 256 | yes |
| EEE-2014J | 1,027 | 343 | 1,027 | 343 | yes |
| FFF-2013B | 1,520 | 739 | 1,520 | 739 | yes |
| FFF-2013J | 1,998 | 903 | 1,998 | 903 | yes |
| FFF-2014B | 1,309 | 656 | 1,309 | 656 | yes |
| FFF-2014J | 1,886 | 769 | 1,886 | 769 | yes |
| GGG-2013J | 926 | 334 | 926 | 334 | yes |
| GGG-2014B | 802 | 324 | 802 | 324 | yes |
| GGG-2014J | 719 | 275 | 719 | 275 | yes |
[saved] aq-1/results/check_two_paths_all.csv  (22 rows x 6 columns)

### AQ1 check ledger, scope = all

| check | what | result | detail |
| :---- | :---- | :---- | :---- |
| C1 | control totals 32,593 enrolments / 28,061 KPI | PASS | found 32,593 / 28,061 |
| C2 | two aggregation paths agree to the enrolment in every run | PASS | 22 of 22 runs agree; raw rows 32,593 = prepared rows 32,593: True |
| C3 | first missed week equals the value re-derived from the task table | PASS | 32,593 of 32,593 enrolments equal |
| C4 | pooled counts equal the sum over runs; the four outcome counts sum to the enrolments of every run | PASS | sum of run enrolments 28,061 = pooled 28,061; runs whose outcome counts sum to n: 22 of 22 |
| C5 | every rate has a denominator and an interval that contains it | PASS | 38 rates checked |
[saved] aq-1/results/checks_all.csv  (5 rows x 4 columns)

