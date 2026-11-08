## 2.1. AQ Modeling Briefs

A Modeling Brief records, before any algorithm is named, the analytics level, the decision, the unit of analysis, the
target, the information allowed as input, the expected output and the main constraint of a question [1]. Naming the
output matters because a binary outcome can be reported as classes, probabilities or a ranking, and each form needs its
own measure of quality [3]. Table 2.1 condenses the four briefs; the full briefs are in Appendix I (Tables A.1–A.4),
and the level and decision of each question are those of Table 1.1.

**Table 2.1. AQ Modeling Briefs (summary)**

| AQ | Unit of analysis | Outcome or target | Input information and window | Expected output | Main constraint |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Enrolment registered at day 14, after the add-drop period (the KPI population); assessment task | None (descriptive measures) | Outcome, module, run, start month, year; due and submission days | Rates with 95% intervals; week of first missed task | Right denominator; run-specific task schedules |
| AQ2 | Enrolment registered at day 27 | non_completion as the outcome of an association model | Signs up to day 27; run, previous attempts, credits | Risk differences within run, odds ratios beside them | Association only; 2014 outcomes kept for the test |
| AQ3 | Enrolment registered at the cut-off | non_completion at the end of the run | 19 primary predictors dated up to day 13 or day 27; extended set and weekly clicks as alternative | Risk score per enrolment | Leakage; transfer to a later run; calibration; interpretability |
| AQ4 | Enrolment within its module run | Judged on the AQ3 target; no contact outcome exists | AQ3 scores; list size from 3 or 5 contacts per 20 students | Ranked list per run with reasons | Fixed capacity; risk is not benefit; tutor decides |

AQ3 and AQ4 share one target and one population, so AQ4 reuses the AQ3 scores, whereas AQ1 and AQ2 describe
completed runs and need no prediction. The OU's own early-warning system also gives tutors a weekly risk list, though
it predicts the submission of the next assignment rather than non-completion of the run [4].
