# 9. Evaluation Design

The evaluation design, fixed in Milestone 4 before any code ran, says how we know whether an answer is good enough;
for AQ1 and AQ2 it has been applied to 2013 and 2014, and for AQ3 and AQ4 it is the evaluation they would undergo, following the
TRIPOD+AI guideline (Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis, updated for AI),
which frames evaluation as discrimination, calibration and usefulness for the decision [11]. A
list's length is set by capacity k, 3 or 5 contacts per 20 students, with 5 per 20 at day 27 as the main operating
point. Recall at capacity is the share of a run's non-completers on the list; normalised recall divides it by the most a
list of length k can reach, because that ceiling ranges from 46% to 100% between training runs; and lift divides the
share of non-completers on the list by the run's base rate. Table 9.1 is the Evaluation Plan.

**Table 9.1. Evaluation Plan**

| AQ | Primary metric | Baseline | Validation | Success criterion |
| :---- | :---- | :---- | :---- | :---- |
| AQ1 | Non-completion rate and outcome shares with 95% intervals, by module, run, start month and year | Pooled rate; rate over all enrolments; rate without flagged enrolments | Denominator checks; two independent aggregation paths (prepared view and raw tables) | Both paths agree to the enrolment; every rate carries its denominator and interval; no rate compared across runs without its interval |
| AQ2 | Average risk difference of each sign within module run, in percentage points, with 95% interval; odds ratio beside it | Unadjusted rate difference per sign | Estimated on the 9 runs of 2013; sensitivity runs; replication on the 13 runs of 2014 | Adjusted risk difference of at least 5 points with an interval excluding 0, same direction in at least two-thirds of the modules where the sign is defined |
| AQ3 | Normalised recall at capacity, pooled over runs (day 27, 5 per 20) | Rule-ranked list; background-only model; random list | Leave-one-run-out folds in 2013; one logged test on all 13 runs of 2014 | Gate S1: the model's pooled normalised recall would have to exceed the rule list's, with the paired bootstrap interval above 0 and a sign-flip test p below 0.05 |
| AQ4 | Normalised recall at capacity | Random list; rule-ranked list | As AQ3, lists formed per test run | Gate S1 would have to be met by the list, and the fairness check pass or its flags be reviewed; risk order as need order stated as untested; no claim about the effect of contact |
