## Appendix I – AQ Modeling Briefs

Each AQ receives a Modeling Brief before any method is named, so the method follows from the
question, the output it needs and the decision it serves [1]. The briefs use the prepared dataset
OULAD-N04-prepared-1.0, in which an enrolment is one student in one module run, the cut-offs are the ends of day 13
and day 27 of the run, and non-completion means a final result of Fail or Withdrawn. Tables A.1, A.2, A.3 and A.4 give the eight
attributes of the brief for each question.

**Table A.1. Modeling Brief of AQ1**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ1: pass, fail and withdrawal shares by module, run, start month and year, and the week of the first missed task |
| Analytics level | Descriptive |
| Decision supported | D2 (where advisors' time goes) and D3 (whether to extend after the pilot): programme leaders see which modules and runs lose most students and how early the first missed task appears |
| Unit of analysis | Enrolment, restricted to enrolments still registered at day 14 (the KPI population); assessment task for the first missed task |
| Outcome / target | N/A (no supervised task); measures: completion and non-completion rates, outcome shares, week of the first task due and not submitted |
| Input information | Enrolment view (outcome, module, run, start month, year); assessment-due view (task, due day, submission); whole run, because the question describes completed runs |
| Expected output | Rate tables with 95% confidence intervals by module, run, start month and year; distribution of the week of the first missed task by outcome |
| Main constraint | Correct denominator (enrolled at day 14) and per-run task schedules, which differ by module; exams missing in five modules |

**Table A.2. Modeling Brief of AQ2**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ2: which signs by the end of week 4 go with later non-completion, within each module |
| Analytics level | Diagnostic (association; no causal claim) |
| Decision supported | D2 and the reasons attached to each name on the D1 list: which signs tutors should look at |
| Unit of analysis | Enrolment registered at day 27 |
| Outcome / target | non_completion at the end of the run, used as the outcome of an association model, not as a prediction target |
| Input information | Signs up to day 27: a task missed, a TMA submitted late, no platform activity in the last seven days, activity relative to the run median, activity before the start; adjustment for module run, previous attempts and credits studied |
| Expected output | Risk differences in percentage points with 95% intervals, unadjusted and within module run, odds ratios beside them; direction of each association per module |
| Main constraint | Association only; tasks due by day 27 exist in 16 of 22 runs; correlated signs; estimation on the 9 training runs of 2013 (6 modules) so that the 2014 test outcomes stay unseen |

**Table A.3. Modeling Brief of AQ3**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ3: how well non-completion is estimated by the end of week 2 (day 13) and week 4 (day 27), against the early-sign rule, on a later run |
| Analytics level | Predictive |
| Decision supported | D1 (who is listed for contact) |
| Unit of analysis | Enrolment registered at the cut-off |
| Outcome / target | non_completion (Fail or Withdrawn) at the end of the run, known only after the run |
| Input information | The 19 usable primary predictors of the prepared views (the mean computer-marked assessment (CMA) score is left out because fewer than 10% of training rows carry it) all dated on or before the cut-off; an extended set of 10 predictors, with the weekly clicks, as an alternative |
| Expected output | A risk score per enrolment at each cut-off, used as a rank within the run; shown as a probability only if calibration holds |
| Main constraint | Leakage and transfer to a later run; interpretability for tutors; calibration; train on 2013 runs, test once on 2014 runs |

**Table A.4. Modeling Brief of AQ4**

| Attribute | Content |
| :---- | :---- |
| AQ ID and wording | AQ4: which enrolments rank first under an assumed capacity, with which gain over the run's base rate and recall, overall and by deprivation band and disability |
| Analytics level | Prescriptive (ranking), as decision support; the choice of contact is deferred |
| Decision supported | D1: tutors receive a ranked list and decide whom to contact |
| Unit of analysis | Enrolment within a module run |
| Outcome / target | Uses the AQ3 target to judge the list; no outcome of contact exists in the data |
| Input information | AQ3 scores and the reasons behind them; list size per run for 3 or 5 contacts per tutor group of about 20 students |
| Expected output | A ranked list per run of the size the capacity allows, with the signs behind each name |
| Main constraint | Fixed capacity; risk is not benefit; human decision; fairness across deprivation band and disability; no claim that contact works |
