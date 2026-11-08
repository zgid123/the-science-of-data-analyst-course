# 10. Generative AI Usage and Reflection

**Roles.** Generative artificial intelligence (AI) supported this milestone in all seven roles that the brief allows,
and every finding about the data was confirmed by code, statistics, documentation or a direct check on the dataset, as
the brief requires [1]. AI was never treated as a source of data: no AI answer served as evidence that a dataset holds
a number of records, that students tend to behave in some way or that one variable causes another [1]. AI agents
worked on both sides of each review, as critic and as the drafter whose work was criticised, and team members
verified the decisions. The seven roles were data dictionary interpreter, exploratory data analysis (EDA) and quality checklist partner, code assistant, preparation
critic, feature engineering ideator, documentation assistant and synthetic-data assistant; Appendix V describes what AI
did in each role and how the result was verified. Table 10.1 gives the main entries of the AI Decision Log in the
brief's format: the suggestion, the team's decision, whether it was accepted, the evidence used to verify it and its
effect on the pipeline [1].

**Table 10.1. AI Decision Log, main entries**

| AI suggestion | Team decision | Accepted / Rejected | Evidence used to verify | Effect on pipeline |
| :---- | :---- | :---- | :---- | :---- |
| A CMA score appears within 7 days and a CMA cannot be submitted late (OU policy of 2025) | Use the 7-day lag for CMA scores; do not apply the no-late rule to 2013–2014 | Accepted in part | 32,991 of 69,956 CMA submissions are after the due day | CMA scores only from submissions made at least 7 days before the cut-off; lateness counted by task type |
| Test whether exact duplicate click rows are copies | Run a chance test on two-row groups | Accepted | 31.5% equal counts against 24.0% by chance | All rows kept; de-duplicated twin built |
| A precision limit of 50% sits near the base rate; measure lift and attainable recall | Re-express the AQ4 limit (C13) | Accepted | 45.3% and 44.2% non-completion at the cut-offs | Capacity view; list quality as lift and recall |
| CMA lateness of unclear meaning drives the rule | The rule uses TMA lateness; a CMA variant is kept | Accepted | 47.2% of CMA against 16.8% of TMA submissions late | early_sign_rule and early_sign_rule_cma (C10) |
| Report the outcome rate of test enrolments of students seen in 2013 before modelling | Report only their number now | Accepted in part | Looking at test outcomes while preparing breaks the independent test | 1,962 flagged; outcomes left to Milestone 4 |
| Tasks due before registration counted as missed; the leakage check could not fail | Correct the formula and the check | Accepted | 6 tasks at day 27; reading of the code | Missed only if due on or after registration; V13 can fail |

**Accepted and rejected suggestions.** The preparation critic raised 12 critiques, of which the team accepted 9 and
3 in part, and the leakage auditor raised 8 findings, all accepted; the auditor found no use of data dated after a
cut-off. The reviews shaped four rules that the pipeline applies. The AQ4 list is judged by its gain over chance,
because a precision limit of 50% sits close to the base rate (C13). CMA lateness, seen in 47.2% of CMA submissions
against 16.8% of TMA submissions, stays out of the early-sign rule (C10). A task counts as missed only if it falls
due on or after the student's registration day, the auditor having pointed to six tasks at day 27 that fell due before
the student registered. And the leakage check is built so that it can fail, as the auditor required.

The fourth of the critic's twelve critiques was accepted only in part, because of a rule the team keeps. The critic asked for the outcome rate of the test enrolments of
students seen in 2013 to be reported before modelling. The team reports their number, 1,962, but not their outcomes, because looking
at test outcomes while preparing the data would make the test set part of the preparation, which the brief rules out
[1].

Appendix V gives the AI Decision Log with all thirteen entries, the prompts, every decision on the critiques and
findings, and a reflection on where the reviews helped most.
