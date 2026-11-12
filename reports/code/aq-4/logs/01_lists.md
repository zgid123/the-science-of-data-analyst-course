# Log: aq-4 / 01_lists

| Field | Value |
| :---- | :---- |
| Started (UTC) | 2026-11-12T15:59:46Z |
| Finished (UTC) | 2026-11-12T15:59:48Z |
| Duration | 1.7 s |
| Command | `python aq-4/code/01_lists.py` (run from `reports/code`) |
| Git commit | `11f4aca` (working tree may hold uncommitted files) |
| Exit status | 0 |

## Console output

[saved] aq-4/extracted-datasets/aq4_ranked_d27.csv  (15,724 rows x 47 columns)  – all test enrolments with ranks and tiers
[saved] aq-4/extracted-datasets/aq4_ranked_d13.csv  (15,989 rows x 47 columns)  – all test enrolments with ranks and tiers
[saved] aq-4/extracted-datasets/aq4_contact_list_d27.csv  (3,955 rows x 17 columns)  – day-27 list, 5 per 20, with reasons

### AQ4 contact list, day 27, 5 per 20 – first rows of one run (risk score shown as fitted; outcome columns are evaluation only)

| run | rank | tier | id_student | risk_score | reason_1 | reason_2 | also_on_rule_list |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| FFF-2014J | 1 | 1 | 64,777 | 0.985 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 2 | 1 | 276,337 | 0.984 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 3 | 1 | 426,410 | 0.984 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 4 | 1 | 590,543 | 0.983 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 5 | 1 | 682,050 | 0.983 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 6 | 1 | 171,692 | 0.982 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 7 | 1 | 622,910 | 0.979 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |
| FFF-2014J | 8 | 1 | 411,688 | 0.979 | task(s) due and not submitted (tasks_missed_c = 1; +1.51) | few active days since the start (active_days_0c = 0; +1.30) | yes |

**First reason of the listed students**

| first_reason_column | listed_students | non_completion_rate | share_of_list |
| :---- | :---- | :---- | :---- |
| active_days_0c | 1,500 | 0.644 | 0.379 |
| tasks_missed_c | 1,362 | 0.890 | 0.344 |
| highest_education | 572 | 0.649 | 0.145 |
| tma_late_c | 292 | 0.620 | 0.074 |
| num_of_prev_attempts | 94 | 0.606 | 0.024 |
| clicks_pre | 69 | 0.522 | 0.017 |
| studied_credits | 37 | 0.811 | 0.009 |
| cma_late_c | 29 | 0.586 | 0.007 |
[saved] aq-4/results/reason_frequency.csv  (8 rows x 4 columns)

listed: 3,955 places in 13 runs; with at least one reason: 3,955

