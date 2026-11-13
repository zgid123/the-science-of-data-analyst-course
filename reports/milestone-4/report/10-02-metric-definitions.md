## Appendix II – Evaluation Design Cards and Metric Definitions

### 1. Evaluation Design Cards

Section 4.1 (Table 4.1) gives the four cards side by side in short form; each card below holds the seven items that
the brief requires.

**AQ1.** Table A.8 gives the card of the descriptive question, whose evaluation checks counts and denominators rather
than accuracy.

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

**AQ2.** Table A.9 gives the card of the diagnostic question, whose evaluation judges the size and consistency of each
association.

**Table A.9. Evaluation Design Card of AQ2**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Average risk difference of each sign within module run, in percentage points, with 95% interval; odds ratios reported beside it, since at 44–46% non-completion they read larger than risk ratios; p-values are not used as the sole basis for a conclusion [13] |
| Secondary metric(s) | Unadjusted rate difference per sign; module-specific risk differences from the sign × module terms of the same model |
| Validation strategy | Estimated on the 9 runs of 2013 (6 modules); task-based signs only in runs with a task due by day 27; replicated on the 13 runs of 2014, including module CCC, the one module with no 2013 run, only after the AQ3 model is frozen and scored; no 2014 AQ2 result may change AQ3 |
| Baseline | Unadjusted rate difference per sign, shown beside the adjusted estimate |
| Error analysis | Binned residuals by run and activity level; correlation among the click-based signs; sensitivity to de-duplicated clicks, to the rule variant that also counts late CMAs, to the 138 flagged enrolments and to dropping runs with no task due |
| Fairness / subgroup check | Associations by gender, disability and deprivation band, described, not adjusted away |
| Success criterion | A sign is a consistent association when its adjusted risk difference is at least 5 percentage points with an interval excluding 0, the smallest gap we treat as worth a tutor's attention, which equals the SMART Goal's target gain, and has the same direction in at least two-thirds of the modules where it is defined; otherwise weak or inconsistent. No association is stated as a cause [1] |

**AQ3.** Table A.10 gives the card of the predictive question, the one with a single success gate.

**Table A.10. Evaluation Design Card of AQ3**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity, computed per run with the run's own list and pooled over runs: the non-completers listed in all runs divided by the most the lists could hold, which for each list is k non-completers, or all of the run's non-completers if there are fewer (day 27, k = 5 per 20) |
| Secondary metric(s) | Recall, precision and lift at capacity (re-expressions of the same true positives at fixed k); unweighted mean of per-run differences between model and rule; ROC-AUC and PR-AUC computed within run and averaged; calibration-in-the-large and calibration slope; Brier score; net benefit as context only, since it describes a threshold policy rather than a fixed capacity [25]; the same at day 13 and at k = 3 per 20 |
| Validation strategy | Development on the 9 runs of 2013 with leave-one-run-out folds; a single, logged scoring of the 13 runs of 2014 after the second freeze, which fixes the final model before any test outcome is opened (Section 4.2) [21], [26] (Section 4.2; Appendix III) |
| Baseline | Early-sign rule as frozen in Change Log entry C10, ranked by its number of signs with ties broken by lower relative activity; a background-only logistic model (module, start month, previous attempts, credits, education, registration lead, no activity); random list |
| Error analysis | Missed non-completers and listed completers by run, module, activity level, previous attempts, late registration and kind of non-completion (Fail or Withdrawn); recall among active students only; recall among reachable non-completers, those not withdrawn within 7 days after the cut-off; stability of list membership near rank k under the bootstrap; CCC runs apart |
| Fairness / subgroup check | Confirmatory check of recall at capacity by group (a formal test on groups fixed in advance) and descriptive checks (Section 4.4) |
| Success criterion | S1 (single gate): on all 13 test runs, all eligible enrolments, day 27, k = 5 per 20, the primary model's pooled normalised recall exceeds the rule-ranked list's, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip permutation test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses are counted apart. S2, precision at capacity, is reported and is not a gate (Table 4.2). S3 (condition for showing probabilities): calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2 on the pooled point estimates; otherwise tutors see ranks and reasons only. All other populations, cut-offs and capacities are sensitivity analyses that cannot change the verdict |

**AQ4.** Table A.11 gives the card of the ranking question, which shares the AQ3 gate and adds the fairness check.

**Table A.11. Evaluation Design Card of AQ4**

| Item | Content |
| :---- | :---- |
| Primary metric(s) | Normalised recall at capacity (recall against the attainable maximum, Change Log C13) |
| Secondary metric(s) | Lift over the run base rate; overlap of the model list with the rule list; true positives on the list split into Fail and Withdrawn; recall at 3 and 5 per 20 |
| Validation strategy | As AQ3: lists formed per test run of 2014 from the frozen scores |
| Baseline | Random list (expected recall k/n) and rule-ranked list of the same length |
| Error analysis | Runs where the list fills its capacity with completers; students with no activity at all, whom every list catches, separated from active students at risk |
| Fairness / subgroup check | Selection rate, recall and precision at capacity by deprivation band and disability (named in AQ4), and by gender and age band (Appendix IV) |
| Success criterion | Gate S1 met by the list; the confirmatory fairness check of Section 4.4 passes or its flags are reviewed before use; the assumption that risk order matches need is stated as untested; no statement about the effect of contact [1] |

### 2. Metric Definitions

The Evaluation Design Cards of Section 4.1 and Tables A.8–A.11 use the metrics that Table A.12 defines, for a run r with n enrolments, the set Y of its non-completers, base rate b = |Y|/n, and a list L of the k highest scores; Section 4.1 explains the main ones in words.

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
| Calibration-in-the-large | Intercept of a logistic model of the outcome with the score's log-odds as offset | Target 0 [33] |
| Calibration slope | Coefficient of the score's log-odds in a logistic recalibration | Target 1; below 1 means risks too extreme [33] |
| Brier score | Mean squared difference between predicted risk and outcome | Overall accuracy of probabilities |
| Net benefit | true positives/n − false positives/n × pt/(1 − pt) at threshold probability pt | Context: contact-all, contact-none and the rule [25] |
| ABROCA | Absolute area between the ROC curves of a group and the rest | Threshold-free differential discrimination [34] |
