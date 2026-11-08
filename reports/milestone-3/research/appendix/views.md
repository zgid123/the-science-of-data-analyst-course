| Level | Prepared view | Population | Grain | Check before Milestone 4 | Result |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Descriptive | enrolment, assessment_due, student_week | 32,593 enrolments; KPI on 28,061 | enrolment; enrolment × task; enrolment × week | No double counting, no join bias | Keys unique; joins kept rows; clicks reconcile |
| Diagnostic | features_d27 + enrolment | 27,535 enrolled at day 27 | enrolment | Associations from real data with comparison groups | Signs up to day 27; seven modules for within-module comparison |
| Predictive | features_d13, features_d27, model_ready | 28,069 and 27,535 | enrolment | Target, prediction point, pre-point features, split, enough of each class | Smaller class ≥ 92 per run; 9 training and 13 test runs; train-only transforms |
| Prescriptive | capacity_by_run | 44 run × cut-off rows | run × cut-off | Action, constraint, cost and outcome data | Assumed capacities only; no contact or outcome data |
