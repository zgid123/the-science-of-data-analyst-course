## 2.1. AQ Modeling Briefs

A Modeling Brief records, for one question and before any algorithm is named, eight attributes: the question's
identifier and wording, its analytics level, the decision it supports, the unit of analysis, the outcome or target,
the information allowed as input with its time window, the expected output and the main constraint [1]. Naming the
expected output matters, because the same binary outcome can be reported as classes, as probabilities or as a
ranking, and each form needs its own measure of quality [3]. All four briefs use the prepared dataset
OULAD-N04-prepared-1.0, in which an enrolment is one student in one module run, the cut-offs are the ends of day 13
and day 27 of the run, and non-completion means a final result of Fail or Withdrawn.

Table 2.1 gives the four briefs side by side, one column per question, with each of the eight attributes in short
form; Appendix I (Tables A.1–A.4) gives each brief in full.

**Table 2.1. AQ Modeling Briefs in summary**

| Attribute | AQ1 | AQ2 | AQ3 | AQ4 |
| :---- | :---- | :---- | :---- | :---- |
| AQ ID and wording | AQ1: outcome shares by module, run, start month and year; week of the first missed task (Table 1.1) | AQ2: signs by the end of week 4 that go with later non-completion, within module (Table 1.1) | AQ3: non-completion estimated at weeks 2 and 4 against the early-sign rule, 2013 runs applied to 2014 runs (Table 1.1) | AQ4: who ranks first on a list of assumed capacity, with gain over a random list and recall, overall and by group (Table 1.1) |
| Analytics level | Descriptive | Diagnostic (association; no causal claim) | Predictive | Prescriptive (ranking), as decision support |
| Decision supported | D2, D3 | D2; reasons beside each name on the D1 list | D1 | D1: tutors decide whom to contact |
| Unit of analysis | Enrolment registered at day 14; assessment task | Enrolment registered at day 27 | Enrolment registered at the cut-off | Enrolment within a module run |
| Outcome / target | N/A; completion rates and outcome shares | non_completion as the outcome of an association model | non_completion (Fail or Withdrawn) at the end of the run | The AQ3 target, to judge the list; no outcome of contact |
| Input information | Enrolment and assessment-due views, whole run | Signs up to day 27; adjustment for run, previous attempts and credits | 19 primary predictors dated by the cut-off; extended set as an alternative | AQ3 scores and reasons; 3 or 5 contacts per 20 |
| Expected output | Rates with 95% intervals; week of the first missed task by outcome | Risk differences with 95% intervals; odds ratios beside them | Risk score per enrolment, ranked within run; a probability only if calibrated | Ranked list per run with the signs behind each name |
| Main constraint | Denominator; per-run task schedules | Association only; correlated signs; 2013 runs only | Leakage; transfer to a later run; interpretability; calibration | Fixed capacity; risk is not benefit; fairness; human decision |

Read together, the briefs show how the questions depend on each other. AQ3 and AQ4 share one target and one
population, so AQ4 reuses the AQ3 scores and adds only the rule that cuts the ranking at the length capacity allows,
whereas AQ1 and AQ2 describe runs that have ended and need no prediction. The design resembles the OU's own
early-warning system, which also gives tutors a weekly list of students at risk, although that system predicts
whether a student will submit the next assignment rather than whether the student will complete the run [4].
