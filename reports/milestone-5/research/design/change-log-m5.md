# Controlled Change Log entries added in Milestone 5 (design file, T09)

Continues the Controlled Change Log C01–C14 of Milestones 2–4 in the same columns as Milestone 4 Table A.13 (ID,
Milestone, Before, After, Reason, Effect). C15 is a Milestone 5 change. C16 records a change made in Milestones 3–4
that no entry recorded (conflict R3). C17 settles an ambiguity left by C06 and C10 (conflict R2); the team confirmed it on
2026-11-08 (one rule, C10, on OULAD and in the pilot). The report shows the full log C01–C17 in an appendix and names the entries in the Revision Log.

## Table 1. Change Log entries C15–C17

| ID | Milestone | Before | After | Reason | Effect |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C15 | 5 | AQ1 rates and first missed week computed over all 22 runs under two denominators (32,593 enrolments; 28,061 registered at day 14) | AQ1 computed on the 9 runs of 2013 (13,529 enrolments; 12,076 registered at day 14); the year comparison uses the 2014 outcome counts per run that Milestone 3 published (19,064 enrolments, all-enrolment denominator); 2014 rates on the day-14 population, the 2014 first missed week and module CCC follow the AQ3 test | Relating 2014 outcomes to task and activity measures before the AQ3 model is frozen would open the test outcomes, the leak C14 prevents for AQ2; the published counts carry outcomes per run only, with no predictor | AQ1 is answered for 2013 and the year comparison only on the all-enrolment denominator; the 22-run totals (28,061; 54.7% completion) are quoted from Milestone 3, not recomputed; the AQ3 test stays independent |
| C16 | 3–4 (recorded in 5) | AQ3 tested on the 2014 runs of the 9 module and start-month pairs (C07) | AQ3 tested once on all 13 runs of 2014 (15,724 enrolments at day 27); gate S1 judged on all 13 runs; the 9 paired runs (10,801) and the 4 unpaired runs (4,923: CCC February and October, EEE February, GGG February) reported apart | Milestone 3 kept the 4 unpaired runs in the test set to test the model on a module or start month it has not seen; the Milestone 4 evaluation review found that no primary test population had been fixed | The test also covers transfer to an unseen module and start month; module terms are deviation-coded so an unseen module gets the average, with a labels-available variant for the February runs; the paired-only result becomes a sensitivity analysis that cannot change the verdict |
| C17 | 5 | Secondary KPI 1: on OULAD the C10 rule; for the university the Milestone 1 two-task rule ("two or more assessed tasks missed or late by week 4"), kept by C06 and not revisited by C10 | One early-sign rule for the project, on OULAD and in the pilot: a task due by the cut-off not submitted, a TMA submitted late, or no platform activity in the seven days before the cut-off (C10) | Milestone 4 carries only the C10 rule through the report, and C10 makes secondary KPI 1 use the same rule as the AQ3 comparison; two rules would let the pilot's KPI count different students from the rule the model must beat | Secondary KPI 1 has one definition; the pilot checks the rule against the university's own task calendar and records before use, as C01 requires for every result |

**Sources**

- Columns: Milestone 4 Table A.13 (baseline file, "Milestone 4: Full traceability and Change Log").
- C15: Before C9-005, C8-021; After `results/README.md` (Populations table, "The 2013-only rule", "Deferred items"),
  `results/aq1_year_difference.csv` (n_2014 = 19,064), `logs/T08_checks.log` (INFO: 13,529 + 19,064 = 32,593;
  22-run figures not recomputed); Reason C3-019 / C9-043 (C14 reason), PROGRESS.md T02 and T04 decisions; Effect
  C6-015 (28,061; 54.7%), C7-037 (0.5474).
- C16: Before C3-021 (C07), S102 crawl line 503; After C9-010, C9-018, C7-034, S104 crawl line 1152 (10,801 /
  4,923 at day 27) and line 1151 (15,724); Reason S103 crawl lines 617–622, S104 crawl line 1275 (critique 5);
  Effect C9-019, C9-012.
- C17: Before C2-006, C06 row (S103 crawl line 1471), C10 row (S103 crawl line 1475); After C2-008, C7-011; Reason
  S104 crawl lines 57, 140, C10 Effect "secondary KPI 1 (sign part) uses the same rule"; Effect C12-007 (C01).
  Status: confirmed by the team on 2026-11-08 (AskUserQuestion: C10 rule everywhere).
