## 8.2. Model Readiness Matrix

Table 8.1, the Model Readiness Matrix of the brief, gives for each question the prepared view, the target or measure,
the feature set or dimensions, the split or time rule and the readiness for Milestone 4 [1]. A question is Ready when
its view, target and rules are fixed and validated, and Revise when part of it still lacks data.

**Table 8.1. Model Readiness Matrix**

| AQ | Analytics type | Prepared view | Target / measure | Feature set / dimensions | Split / time rule | Readiness |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Descriptive | enrolment, assessment_due | Completion rate; week of the first missed task | Module, run, start month, year | All 22 runs; KPI population enrolled at day 14 | Ready |
| AQ2 | Diagnostic | features_d27, enrolment | non_completion | Missed tasks, late TMA and CMA, inactivity in the last seven days, activity against the run median; concurrent runs for 2014 only | Signs up to day 27; task signs in the 16 runs with a task due | Ready, for association only |
| AQ3 | Predictive | features_d13, features_d27, model_ready | non_completion at the run end | 20 primary and 10 extended predictors and weekly clicks; the early-sign rule as comparison | Train on 2013, test on 2014; tuning by leave-one-run-out folds inside 2013 | Ready; the day-13 list rests on activity only |
| AQ4 | Prescriptive (ranking) | capacity_by_run with AQ3 scores | Lift over the run's rate; recall against the most a list of that size can reach | Lists of 3 or 5 per tutor group of 20, or 30 or 40 per run; audit by deprivation band and disability | Per run and cut-off, test runs only | Revise: the ranking is ready; the choice of contact is deferred |

**Why a ranking is needed.** The early-sign rule flags 20.2% of enrolled students at day 13 and 28.8% at day 27,
while lists of 3 or 5 per group of 20 students hold 15% or 25% of them. The rule names more students than a list of 5
per 20 can hold in 7 of the 22 runs at day 13 and in 10 at day 27, and more than a list of 3 per 20 can hold in 15 runs
at day 13 and in all 22 at day 27. Staff therefore need an order of whom to contact first, which is what AQ3 and AQ4
provide; the rule alone cannot set it.

**Questions not yet feasible.** Three parts of the proposal cannot be answered with OULAD and need the pilot's own
records: which contact, a lecturer's message, a call from the support office or a referral, works best for which
student, and its effect on completion (AQ4, C08, C11); comparisons by year of study, by delivery mode and by attendance
(C04, C05); and the follow-up rate of secondary KPI 2 with the contact part of secondary KPI 1 (C08).

**Entry conditions for Milestone 4.** The brief sets six conditions for starting to model [1]: the core questions
have prepared views with clear traceability; target, features and dimensions are stable; leakage and split are defined
for predictive tasks; important quality issues are handled or kept on purpose; no synthetic data serve as evidence;
and the prepared data can be rebuilt from the raw files. All six hold for AQ1 to AQ3, so Milestone 4 can
start with them; AQ4 enters it as a ranking question, and its contact part waits for the pilot. Appendix VI (Table
A.19) gives the state of each condition.
