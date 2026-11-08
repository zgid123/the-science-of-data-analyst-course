# 10. Generative AI Usage and Reflection

**Roles.** Generative artificial intelligence (AI) supported this milestone in all seven roles that the brief allows,
and every finding about the data was confirmed by code, statistics, documentation or a direct check on the dataset, as
the brief requires [1]. AI was never treated as a source of data: no AI answer served as evidence that a dataset holds
a number of records, that students tend to behave in some way or that one variable causes another [1]. AI agents
worked on both sides of each review, as critic and as the drafter whose work was criticised, and team members
verified the decisions. Table 10.1 gives each role, what AI did in it and how the result was verified.

**Table 10.1. AI roles and verification**

| Role (brief) | What AI did | How the result was verified |
| :---- | :---- | :---- |
| Data dictionary interpreter | Read the data descriptor, the OU's assessment policy and the IMD documentation | Each fact kept only with a verbatim quotation; the 2025 rule that a CMA cannot be late tested on the data and not applied |
| EDA and quality checklist partner | Proposed a test of whether duplicate click rows are copies | Test run on the data: 31.5% equal counts against 24.0% by chance |
| Code assistant | Drafted every script of the package | 13 figures equal to an independent recount; 9 unit tests; 6 features recomputed for every row without a difference; one row recounted by hand |
| Preparation critic | Reviewed the plan in isolation (12 critiques) and audited leakage (8 findings) | Each critique checked on the data or the code before a decision |
| Feature engineering ideator | Proposed recency, trend, a pre-start window, clicks by resource type and early submissions | Each feature computable from real fields before the cut-off; added as the extended set |
| Documentation assistant | Drafted the dictionary, lineage, package guide and transformation log | Generated from the code; V14 fails if a column lacks an entry |
| Synthetic-data assistant | Wrote small labelled test enrolments | Level A of the brief's policy only; never in a view or a finding |

**Accepted and rejected suggestions.** The preparation critic raised 12 critiques, of which the team accepted 9 and
3 in part, and the leakage auditor raised 8 findings, all accepted; the auditor found no use of data dated after a
cut-off. The reviews shaped four rules that the pipeline applies. The AQ4 list is judged by its gain over chance,
because a precision limit of 50% sits close to the base rate (C13). CMA lateness, seen in 47.2% of CMA submissions
against 16.8% of TMA submissions, stays out of the early-sign rule (C10). A task counts as missed only if it falls
due on or after the student's registration day, after the auditor found six tasks at day 27 counted as missed before
the student had registered. And the leakage check was rebuilt so that it can fail, after the auditor showed that its
first form could not.

One suggestion was rejected in part. The critic asked for the outcome rate of the test enrolments of students seen in
2013 to be reported before modelling. The team reports their number, 1,962, but not their outcomes, because looking
at test outcomes while preparing the data would make the test set part of the preparation, which the brief rules out
[1]. A second suggestion was accepted in part: the interpreter's reading of the 2025 policy gave a usable rule for
CMA marks, which appear within seven days, but its rule that a CMA cannot be submitted late does not hold in data
where 32,991 CMA submissions are late, so it was not applied.

**Reflection.** The reviews were most useful where the AI critic had to argue from the data rather than from general
advice: the duplicate test, the base-rate argument and the registration-day error each changed the pipeline, and each
was confirmed by a count before it was accepted. Appendix V gives the AI Decision Log with all thirteen entries, the
prompts and every decision on the critiques and findings.
