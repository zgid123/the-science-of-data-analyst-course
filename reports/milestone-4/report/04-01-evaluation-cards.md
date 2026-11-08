## 4.1. Evaluation Design Cards

**What a card holds.** The brief asks for an Evaluation Design Card for each question with seven items: the primary
and secondary metrics, the validation strategy, the baseline, the error analysis, the fairness or subgroup check and
the success criterion [1]. The metric follows the decision it supports: recall matters when a contact is cheap and
missing a struggling student is costly, precision when a contact is costly [23], and when only a limited number of
top-ranked cases can be acted on, performance among those cases is the practical measure [24].

**Capacity and the main operating point.** The capacity k of a run is 3 or 5 contacts per tutor group, with a group
assumed to hold 20 students, that is 15% or 25% of the enrolments registered at the cut-off. The main operating point
is 5 per 20 at day 27, because it serves the list delivered in week 5 and is close to the share of students the early-sign rule flags at day 27: 28.8% of the 27,535 enrolments registered then
across all 22 runs, a share computed without any outcome. A confusion matrix of listed and unlisted students against
their outcome is reported for each run; at a fixed list length its cells give recall, precision and lift, which
replace the F1 score, because the list length is set by capacity rather than chosen to balance the two kinds of error.
The Brier score that the AQ3 card lists is the mean squared difference between predicted risk and outcome.

**AQ1.** Table 4.1 gives the card of the descriptive question, whose evaluation checks counts and denominators rather
than accuracy.

**Table 4.1. Evaluation Design Card of AQ1**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Non-completion rate and outcome shares per module, run, start month and year, with 95% confidence intervals for proportions |
| Secondary metric(s) | Cumulative share of enrolments with a first missed task by week, by outcome |
| Validation strategy | Denominator checks: 32,593 enrolments in total and 28,061 in the KPI population; two independent aggregation paths (prepared view and raw tables) must agree exactly |
| Baseline | Pooled rate over all runs; rate over all 32,593 enrolments (second denominator); rate without the 138 enrolments flagged for missing withdrawal or registration days |
| Error analysis | Runs whose rate moves by more than its interval between the two denominators; runs with no task due by day 27 |
| Fairness / subgroup check | Rates by gender, disability, deprivation band and age band reported as description only |
| Success criterion | Both aggregation paths agree to the enrolment; every rate carries its denominator and interval; no rate is compared across runs without its interval |

**AQ2.** Table 4.2 gives the card of the diagnostic question, whose evaluation judges the size and consistency of each
association.

**Table 4.2. Evaluation Design Card of AQ2**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Average risk difference of each sign within module run, in percentage points, with 95% interval; odds ratios reported beside it, since at 44–46% non-completion they read larger than risk ratios; p-values are not used as the sole basis for a conclusion [13] |
| Secondary metric(s) | Unadjusted rate difference per sign; module-specific risk differences from the sign × module terms of the same model |
| Validation strategy | Estimated on the 9 runs of 2013 (6 modules); task-based signs only in runs with a task due by day 27; replicated on the 13 runs of 2014, including module CCC, the one module with no 2013 run, only after the AQ3 model is frozen and scored; no 2014 AQ2 result may change AQ3 |
| Baseline | Unadjusted rate difference per sign, shown beside the adjusted estimate |
| Error analysis | Binned residuals by run and activity level; correlation among the click-based signs; sensitivity to de-duplicated clicks, to the rule variant that also counts late CMAs, to the 138 flagged enrolments and to dropping runs with no task due |
| Fairness / subgroup check | Associations by gender, disability and deprivation band, described, not adjusted away |
| Success criterion | A sign is a consistent association when its adjusted risk difference is at least 5 percentage points with an interval excluding 0, the smallest gap the team treats as worth a tutor's attention, which equals the SMART Goal's target gain, and has the same direction in at least two-thirds of the modules where it is defined; otherwise weak or inconsistent. No association is stated as a cause [1] |

**AQ3.** Table 4.3 gives the card of the predictive question, the one with a single success gate.

**Table 4.3. Evaluation Design Card of AQ3**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity, computed per run with the run's own list and pooled over runs: the non-completers listed in all runs divided by the most the lists could hold, which for each list is k non-completers, or all of the run's non-completers if there are fewer (day 27, k = 5 per 20) |
| Secondary metric(s) | Recall, precision and lift at capacity (re-expressions of the same true positives at fixed k); unweighted mean of per-run differences between model and rule; ROC-AUC and PR-AUC computed within run and averaged; calibration-in-the-large and calibration slope; Brier score; net benefit as context only, since it describes a threshold policy rather than a fixed capacity [25]; the same at day 13 and at k = 3 per 20 |
| Validation strategy | Development on the 9 runs of 2013 with leave-one-run-out folds; a single, logged scoring of the 13 runs of 2014 after the second freeze, which fixes the final model before any test outcome is opened (Section 4.2) [21], [26] (Section 4.2; Appendix III) |
| Baseline | Early-sign rule as frozen in Change Log entry C10, ranked by its number of signs with ties broken by lower relative activity; a background-only logistic model (module, start month, previous attempts, credits, education, registration lead, no activity); random list |
| Error analysis | Missed non-completers and listed completers by run, module, activity level, previous attempts, late registration and kind of non-completion (Fail or Withdrawn); recall among active students only; recall among reachable non-completers, those not withdrawn within 7 days after the cut-off; stability of list membership near rank k under the bootstrap; CCC runs apart |
| Fairness / subgroup check | Confirmatory check of recall at capacity by group (a formal test on groups fixed in advance) and descriptive checks (Section 4.4) |
| Success criterion | S1 (single gate): on all 13 test runs, all eligible enrolments, day 27, k = 5 per 20, the primary model's pooled normalised recall exceeds the rule-ranked list's, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip permutation test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses are counted apart. S2, precision at capacity, is reported and is not a gate (Table 4.5). S3 (condition for showing probabilities): calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2 on the pooled point estimates; otherwise tutors see ranks and reasons only. All other populations, cut-offs and capacities are sensitivity analyses that cannot change the verdict |

**AQ4.** Table 4.4 gives the card of the ranking question, which shares the AQ3 gate and adds the fairness check.

**Table 4.4. Evaluation Design Card of AQ4**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity (recall against the attainable maximum, Change Log C13) |
| Secondary metric(s) | Lift over the run base rate; overlap of the model list with the rule list; true positives on the list split into Fail and Withdrawn; recall at 3 and 5 per 20 |
| Validation strategy | As AQ3: lists formed per test run of 2014 from the frozen scores |
| Baseline | Random list (expected recall k/n) and rule-ranked list of the same length |
| Error analysis | Runs where the list fills its capacity with completers; students with no activity at all, whom every list catches, separated from active students at risk |
| Fairness / subgroup check | Selection rate, recall and precision at capacity by deprivation band and disability (named in AQ4), and by gender and age band (Appendix IV) |
| Success criterion | Gate S1 met by the list; the confirmatory fairness check of Section 4.4 passes or its flags are reviewed before use; the assumption that risk order matches need is stated as untested; no statement about the effect of contact [1] |

**Metric definitions.** The cards use metrics that are defined once here, for a run r with n enrolments, the set Y of
its non-completers, base rate b = |Y|/n, and a list L of the k highest scores. In words: recall at capacity is the
share of the run's non-completers who are on the list; attainable recall is the most a list of length k can reach,
which is below 1 when the run has more non-completers than places on the list; normalised recall divides recall by
that ceiling, so that 1 means the best list possible; precision is the share of the list who do not complete; and
lift divides precision by the base rate, so that 1 means no better than chance. Appendix II (Table A.4) gives the formula of every metric.

