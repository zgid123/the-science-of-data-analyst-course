# AQ–Data Fit Decision Log (Task 3, brief section 8)

Evidence keys: `P.` = `package/data/metadata/profile.json`, `U.` = `package/data/metadata/understanding.json`,
DQnn = `package/data/metadata/quality_issue_log.md`, Cnn = Controlled Change Log. Each AQ is rated against the claim
it carries after the Milestone 2 revisions C01–C08 (`research/baseline/m3-baseline.md`), then walked through the
decision procedure of brief section 8.1: (1) documentation and semantics, (2) valid derivation, (3) compatible open
dataset, (4) narrow or rewrite, (5) defer or drop, (6) synthetic data only within the policy of section 8.3.

## 1. Ratings

| AQ | Type | Claim as committed (after C01–C08) | Supported by real data | Missing | Rating | Action (procedure step) | Revised claim | Change |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | Shares passing, failing, withdrawing by module, run and start month over four runs (2013B–2014J); week of the first missed assessed task, completers vs others | final_result for 32,593 enrolments in 22 runs (U.outcome); due days of 182 TMA/CMA tasks and submissions (U.time); population enrolled at day 14 (P.outcome) | Year of study, delivery mode (all runs are distance learning) (C04); exam results for 5 of 7 modules (DQ08) | YELLOW | (2) derive first missed task from due days and submissions over TMA/CMA only; (4) keep the comparisons OULAD holds | Rates by module, run, start month and year; first missed TMA/CMA week for completers vs non-completers; enrolled at day 14 | C09 |
| AQ2 | Diagnostic | Signs in weeks 1–4 (missed or late tasks, platform activity against the run's average, tasks missed in several modules at once) and their difference in non-completion, across modules | Click records by day (P.shape), tasks due by day 27 in 16 of 22 runs (P.temporal), concurrent enrolments: 1,382 enrolled at day 14, 1,370 of them in 2014 runs (P.temporal.concurrent_enrolments_day14) | Attendance (C05); year of study and mode (C04) | YELLOW | (2) derive each sign with a formula and a window; (4) task signs only in the 16 runs with a task due by day 27; the several-modules sign described for 2014 runs only | Association of each sign with non-completion within module; no causal reading | C12 |
| AQ3 | Predictive | Fail or withdrawal estimated at day 13 and day 27; recall and precision on a capacity-length list; compared with a simple rule; checked across deprivation band and disability; trained on 2013 runs, tested on 2014 runs | Target for every enrolment (U.outcome); 28,069 enrolled at day 13 and 27,535 at day 27, 45.3% and 44.2% non-completion (P.outcome); 9 module/start-month pairs with both years (P.temporal) | The comparison rule "two or more tasks missed or late by week 4" can fire in 1 of 22 runs, and its OULAD form of one task (C06) in 16 runs at day 27 and 1 at day 13 (DQ18); TMA mark release day (no field) | YELLOW | (1) checked: no other field holds marking dates; (2) restate the rule on tasks actually due plus inactivity; (4) narrow the score features to marks known at the cut-off | As committed, with the restated rule and CMA scores only | C10 |
| AQ4 | Prescriptive | Which students to list, in what order, with which contact, within weekly capacity, precision ≥ 50% and a fairness limit | Ranking from AQ3; run sizes for capacity scenarios (P.outcome) | Contacts, contact types, capacity, outcomes after contact: no field in OULAD or any candidate of Milestone 2 (C08) | RED | (3) no compatible open dataset (Milestone 2 search, 7 candidates); (4) rewrite to the ranking part; (5) defer the contact choice and its effect to the pilot | Under an assumed weekly capacity, which enrolments rank first at each cut-off, and what recall and precision the list reaches overall and by deprivation band and disability | C11, C13 |

## 2. Missing value, missing variable, missing label (brief section 8.2)

| Situation | Case in OULAD | Evidence | Handling |
| :---- | :---- | :---- | :---- |
| Missing value | imd_band 1,111; date_registration 45; TMA score 173; withdrawal day of 93 Withdrawn; due day of 11 exams | DQ04, DQ08, DQ11–DQ13 | Category "Missing" (imd_band); indicator, no imputation in the prepared views; fitted filling only in the training runs; exams left out of task counts |
| Recorded absence (not missing) | No click row; no submission row; empty unregistration day of students who stayed | DQ17; descriptor: "If the student does not submit the assessment, no result is recorded" | Zero counts after left joins; empty unregistration = did not unregister |
| Missing variable / concept | Year of study, delivery mode, attendance, leave or transfer status, contacts and their outcomes, staff capacity, TMA marking day | C04, C05, C08; U.tables | Not imputed or simulated; questions narrowed (AQ1–AQ3) or deferred (AQ4 contact part) |
| Missing target / label | None: final_result is present for every enrolment | U.outcome | Supervised target available; completion = Pass or Distinction |

## 3. Synthetic-data decision (brief section 8.3)

No synthetic record enters any prepared view, statistic or finding (levels D and E are not used). The only synthetic
data are level A fixtures: a few hand-made, labelled enrolments in `package/tests/` that check the feature formulas
of the pipeline. No augmentation (level C) is planned.

## 4. Change Log entries (from C09)

| ID | Old content | New content | Reason (data evidence) | Effect on AQ / KPI / decision |
| :---- | :---- | :---- | :---- | :---- |
| C09 | KPI denominator: enrolments still registered at day 14 (28,119; C03) | Enrolled at day d = registered by day d (or registration day unknown) and not unregistered by day d; day 14 for the KPI (28,061), days 13 and 27 for the lists (28,069; 27,535) | 58 enrolments registered after day 14, up to day 167 (DQ05) | Primary KPI recomputed on 28,061 enrolments; same rule for every population |
| C10 | AQ3 comparison rule and secondary KPI 1 early-sign rule: two or more assessed tasks missed or late by week 4 (Milestone 1); on OULAD one missed or late task, in the 16 runs with a task due by day 27 (C06) | Early-sign rule: at least one TMA or CMA due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off; CMA lateness only in a sensitivity variant | Two or more tasks are due by day 27 in 1 of 22 runs, one or more in 16, and by day 13 in 1 (DQ18), so a rule on tasks alone cannot fire in 6 runs at day 27 or in 21 at day 13; the meaning of a late CMA in 2013–2014 is undocumented (DQ10) | The rule can fire in every run; secondary KPI 1 (sign part) uses the same rule |
| C11 | AQ4: whom to list, in what order and with which contact, within capacity | AQ4 (rewritten): ranking under an assumed capacity with recall and precision overall and by deprivation band and disability; the choice of contact and its effect deferred to the pilot | No contact, capacity or outcome-after-contact data (C08; AQ4 RED) | No prescriptive claim; D1 receives an ordered list and its measured quality, not a contact plan |
| C12 | AQ2 sign "tasks missed in several modules at once", all runs | Described for 2014 runs only; not a predictor in AQ3 | Of 1,382 concurrent enrolments at day 14, 12 fall in 2013 runs (training runs) | AQ2 narrowed; AQ3 feature set excludes it |
| C13 | AQ4 list limit: precision of at least 50% | List quality measured as lift over the run's base rate and as recall against the most a list of the same size can reach, with a random list and the early-sign rule as baselines | Non-completion is 45.3% at day 13 and 44.2% at day 27, and 24.9–58.3% by run, so a random list already reaches about 45% precision; lists of 3 or 5 per 20 students cap recall | AQ4 limit re-expressed; D1 judges a list by its gain over chance |
