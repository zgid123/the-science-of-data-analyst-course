# AI leakage auditor – team decisions (T14)

The auditor (isolated AI agent, prompt in `leakage-auditor-prompt.md`, findings and its 17 read-only queries in
`leakage-auditor.md`) read the pipeline code and specifications and queried the prepared and raw files. It found no
feature using an event after its cut-off and no fitted parameter using test rows. All 8 findings were reproduced and
accepted; the pipeline was changed and rerun (logs/T14_rerun.log: 22 of 22 checks PASS, tests 9/9;
logs/T14_rerun_check.log: two runs from raw, 8 of 8 files identical).

| # | Finding (severity) | Decision | Evidence used to verify | Effect on the pipeline |
| :---- | :---- | :---- | :---- | :---- |
| F1 | 93 Withdrawn enrolments without a withdrawal day stay in both cut-off views as positives, 89 of the 92 at day 13 in test runs (medium) | Accepted | `eval_withdrawal_day_unknown` counts 92 (day 13) and 93 (day 27), 89 and 90 in test runs | Evaluation flag added to the feature views (role evaluation, never a predictor); Milestone 4 reports test metrics with and without these rows |
| F2 | Feature views hold id_student, final_result and non_completion, and tree models were told to use the views as they are (medium) | Accepted | Columns listed in the view schema | `predictor_sets.json` names the only model inputs for every model family; `fit_transforms.py` docstring corrected |
| F3 | Missing indicator of registration_lead duplicates the extended flag registration_missing in the primary matrix (low) | Accepted | 5 training rows, all non-completers | No indicator for registration_lead; the flag stays an extended predictor |
| F4 | Existence of a missing indicator was decided with test rows (low) | Accepted | `fit()` read df instead of the training rows | Indicators decided on training rows; training medians computed for every numeric column |
| F5 | Tasks due before a late registrant's registration counted as missed at day 27 (low) | Accepted | 6 such tasks at day 27 | A task counts only if due on or after the registration day; validator recount and fixture test changed accordingly |
| F6 | No-click students received the training median (1 day) for days_since_last_click (low) | Accepted | Median 1.0 in `transform_params.json` | Value c + 1 for students with no click in days 0…c, set in the view |
| F7 | V13 could never fail, because the data were filtered before the check (low) | Accepted | Code reading | V13 recounts clicks without any cut-off and requires the pipeline to differ exactly where later clicks exist (26,755 and 25,663 rows) |
| F8 | V14 check of extended predictors was commented out by a misplaced comment (low) | Accepted | `validate_prepared.py` line 170 | Line split; V14 checks both predictor lists |
