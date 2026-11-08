## Appendix III – Evaluation Design Cards and Metric Definitions

Each question has an Evaluation Design Card with the seven rows the brief sets: primary and secondary metrics,
validation strategy, baseline, error analysis, fairness or subgroup check and success criterion [1]. The criteria are
fixed before any model is trained, so that metrics and thresholds cannot be chosen after the results are seen [30].
Tables A.8, A.9, A.10 and A.11 give the four cards, and Table A.12 defines the metrics. The capacity k of a run is 3 or 5 contacts
per tutor group of about 20 students [2], that is 15% or 25% of the enrolments registered at the cut-off. OULAD holds
no tutor-group field, so one list per run stands in for the tutors' lists, and a run-wide list can give one group more
names than another. The main operating point is 5 per 20 at day 27, because it serves the list delivered in week 5 and
is close to the share of students the early-sign rule flags at day 27 (28.8%).

**Table A.8. Evaluation Design Card of AQ1**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Non-completion rate and outcome shares per module, run, start month and year, with 95% confidence intervals for proportions |
| Secondary metric(s) | Cumulative share of enrolments with a first missed task by week, by outcome |
| Validation strategy | Denominator checks: 32,593 enrolments in total and 28,061 in the KPI population; two independent aggregation paths (prepared view and raw tables) must agree exactly |
| Baseline | Pooled rate over all runs; rate over all 32,593 enrolments (second denominator); rate without the 138 enrolments flagged for missing withdrawal or registration days |
| Error analysis | Runs whose rate moves by more than its interval between the two denominators; runs with no task due by day 27 |
| Fairness / subgroup check | Rates by gender, disability, deprivation band and age band reported as description only |
| Success criterion | Both aggregation paths agree to the enrolment; every rate carries its denominator and interval; no rate is compared across runs without its interval |

**Table A.9. Evaluation Design Card of AQ2**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Average risk difference of each sign within module run, in percentage points, with 95% interval; odds ratios reported beside it, since at 44–46% non-completion they read larger than risk ratios; p-values are not used as the sole basis for a conclusion [13] |
| Secondary metric(s) | Unadjusted rate difference per sign; module-specific risk differences from a model with sign × module interactions |
| Validation strategy | Estimated on the 9 runs of 2013 (6 modules); task-based signs only in runs with a task due by day 27; replicated on the 13 runs of 2014, including module CCC, only after the AQ3 model is frozen and scored; no 2014 AQ2 result may change AQ3 |
| Baseline | Unadjusted rate difference per sign, shown beside the adjusted estimate |
| Error analysis | Binned residuals by run and activity level; correlation among the click-based signs; sensitivity to de-duplicated clicks, to the rule variant that also counts late CMAs, to the 138 flagged enrolments and to dropping runs with no task due |
| Fairness / subgroup check | Associations by gender, disability and deprivation band, described, not adjusted away |
| Success criterion | A sign is a consistent association when its adjusted risk difference is at least 5 percentage points with an interval excluding 0, the size of the SMART Goal's target gain, and has the same direction in at least two-thirds of the modules where it is defined; otherwise weak or inconsistent. No association is stated as a cause [1] |

**Table A.10. Evaluation Design Card of AQ3**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity, computed per run with the run's own list and pooled over runs (day 27, k = 5 per 20) |
| Secondary metric(s) | Recall, precision and lift at capacity (re-expressions of the same true positives at fixed k); unweighted mean of per-run differences; ROC-AUC and PR-AUC computed within run and averaged; calibration-in-the-large and calibration slope; Brier score; net benefit as context only, since it describes a threshold policy rather than a fixed capacity [32]; the same at day 13 and at k = 3 per 20 |
| Validation strategy | Development on the 9 runs of 2013 with leave-one-run-out folds; a single, logged scoring of the 13 runs of 2014 after the second freeze [21], [30] (Appendix IV) |
| Baseline | Early-sign rule as frozen in Change Log entry C10, ranked by its number of signs with ties broken by lower relative activity; a background-only logistic model (module, start month, previous attempts, credits, education, registration lead, no activity); random list |
| Error analysis | Missed non-completers and listed completers by run, module, activity level, previous attempts, late registration and kind of non-completion (Fail or Withdrawn); recall among active students only; recall among reachable non-completers, those not withdrawn within 7 days after the cut-off; stability of list membership near rank k under the bootstrap; CCC runs apart |
| Fairness / subgroup check | Appendix V |
| Success criterion | S1 (single gate): on all 13 test runs, all eligible enrolments, day 27, k = 5 per 20, the primary model's pooled normalised recall exceeds the rule-ranked list's, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip permutation test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses are counted apart. S3 (condition for showing probabilities): calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2 on the pooled point estimates; otherwise tutors see ranks and reasons only. All other populations, cut-offs and capacities are sensitivity analyses that cannot change the verdict |

**Table A.11. Evaluation Design Card of AQ4**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity (recall against the attainable maximum, Change Log C13) |
| Secondary metric(s) | Lift over the run base rate; overlap of the model list with the rule list; true positives on the list split into Fail and Withdrawn; recall at 3 and 5 per 20 |
| Validation strategy | As AQ3: lists formed per test run of 2014 from the frozen scores |
| Baseline | Random list (expected recall k/n) and rule-ranked list of the same length |
| Error analysis | Runs where the list fills its capacity with completers; students with no activity at all, whom every list catches, separated from active students at risk |
| Fairness / subgroup check | Selection rate, recall and precision at capacity by deprivation band and disability (named in AQ4), and by gender and age band (Appendix V) |
| Success criterion | Gate S1 met by the list; the confirmatory fairness check of Appendix V passes or its flags are reviewed before use; the assumption that risk order matches need is stated as untested; no statement about the effect of contact [1] |

Table A.12 defines each metric for run r with n enrolments, non-completers Y, base rate b = |Y|/n, and list L of the
k highest scores.

**Table A.12. Metric definitions**

| Metric | Definition | Reading |
| :---- | :---- | :---- |
| Recall at capacity | \|L ∩ Y\| / \|Y\| | Share of the run's non-completers on the list |
| Attainable recall | min(k, \|Y\|) / \|Y\| | The most a list of length k can reach |
| Normalised recall | recall / attainable recall | 1 = best attainable; equals precision when \|Y\| ≥ k |
| Pooled normalised recall | Σ\|L ∩ Y\| / Σ min(k, \|Y\|) over runs | Each run keeps its own list and k |
| Precision at capacity | \|L ∩ Y\| / k | Share of the list who do not complete |
| Lift | precision / b | 1 = chance; a random list has expected recall k/n |
| ROC-AUC (within run) | Probability that a non-completer scores above a completer of the same run | Discrimination without run differences |
| PR-AUC (within run) | Area under a run's precision–recall curve | Read against its chance level b [24] |
| Calibration-in-the-large | Intercept of a logistic model of the outcome with the score's log-odds as offset | Target 0 [31] |
| Calibration slope | Coefficient of the score's log-odds in a logistic recalibration | Target 1; below 1 means risks too extreme [31] |
| Brier score | Mean squared difference between predicted risk and outcome | Overall accuracy of probabilities |
| Net benefit | true positives/n − false positives/n × pt/(1 − pt) at threshold probability pt | Context: contact-all, contact-none and the rule [32] |
| ABROCA | Absolute area between the ROC curves of a group and the rest | Threshold-free differential discrimination [34] |
