# AI Decision Log (deliverable F, brief section 14.1)

Generative AI agents worked for the team in all seven roles the brief allows; team members verify every decision.
No AI answer served as evidence about the data: every accepted suggestion was checked by code, a recount on the raw
files, documentation or a test. Full prompts, outputs and per-item decisions: `preparation-critic-prompt.md`,
`preparation-critic.md`, `preparation-critic-decisions.md`, `leakage-auditor-prompt.md`, `leakage-auditor.md`,
`leakage-auditor-decisions.md`; research prompts in `PROGRESS.md` (T05, T06) and the research trail.

| # | Role (brief 14) | AI suggestion | Team decision | Accepted / Rejected | Evidence used to verify | Effect on pipeline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A1 | Data dictionary interpreter | A CMA score appears within 7 days and a CMA cannot be submitted late (OU policy, S201) | Use the 7-day lag for CMA scores; do not apply the no-late rule to 2013–2014 | Accepted in part | 32,991 of 69,956 CMA submissions are after the due day (profile.json) | `cma_score_mean_c` uses marks submitted ≤ c − 7; late counts split by TMA and CMA |
| A2 | Data dictionary interpreter | The English IMD covers England only; other UK nations use their own indices (S203, S204) | Keep imd_band as recorded, "Missing" as its own group, no pooling claims across nations | Accepted | imd_band missing for 40.1% of North Region, 22.5% of Ireland (profile.json) | imd_band is an audit column; fairness rows keep "Missing" apart |
| A3 | EDA / quality checklist partner | Test whether exact duplicate click rows are copies or separate records | Run a chance test on two-row groups | Accepted | 31.5% equal against 24.0% expected; below chance for quizzes (profile.json) | All rows kept, de-duplicated twin built |
| A4 | Preparation critic | Precision ≥ 50% is near the base rate; measure lift and attainable recall | Re-express the AQ4 limit (C13) | Accepted | 45.3% and 44.2% non-completion at the cut-offs | Capacity view; Milestone 4 metric plan |
| A5 | Preparation critic | Target-derived flags could reach the predictors | Role `target_derived`, kept out of feature views | Accepted | Flags defined from final_result | V14 and V13 forbid them |
| A6 | Preparation critic | CMA lateness of unclear meaning drives the rule | Rule uses TMA lateness; CMA variant kept | Accepted | 47.2% of CMA vs 16.8% of TMA submissions late | `early_sign_rule`, `early_sign_rule_cma` (C10) |
| A7 | Feature engineering ideator | Recency, trend, pre-start window, clicks by resource type, early submissions; first-click day | Add all but first-click day as an extended set | Accepted in part | Pre-start clicks already carried by `clicks_pre`, `clicks_pre14` | 10 extended predictors |
| A8 | Preparation critic | Report the outcome rate of test enrolments of students seen in 2013 before modelling | Report only their count now | Accepted in part | Looking at test outcomes while preparing breaks the independent test (brief section 11) | 1,962 flagged, outcome left to Milestone 4 |
| A9 | Preparation critic (leakage audit) | 93 Withdrawn without a day sit in the test views as easy positives | Evaluation flag; metrics with and without | Accepted | 89 of 92 at day 13 are test rows; 41% have no early click | `eval_withdrawal_day_unknown` |
| A10 | Preparation critic (leakage audit) | Tasks due before registration counted as missed; V13 could not fail; a V14 line commented out | Fix the formula and both checks | Accepted | 6 tasks at day 27; code reading | Pipeline rerun: 22 of 22 checks PASS |
| A11 | Code assistant | Draft every script of the package (understanding, profile, preparation, transforms, validation, notebooks) | Keep after review, tests and independent recounts | Accepted | 13 of 13 numbers equal a separate recount by the exploration code; 9 fixture tests; 6 features recomputed from raw for every row, 0 mismatches; one row recounted by hand from the raw files | Package `src/`, `tests/` |
| A12 | Documentation assistant | Draft the dictionary, lineage, README and transformation log | Generated from code and checked | Accepted | V14: every prepared column documented with role and source | `data_dictionary.md`, `lineage.md` |
| A13 | Synthetic-data assistant | Small invented enrolments to test the formulas | Level A fixtures only, labelled, never in a view or a finding | Accepted | Brief section 8.3, level A | `package/tests/test_features.py` |
