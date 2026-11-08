## 4.3. Metrics and Success Criteria

**Primary metric.** Under the protocol of Section 4.2, the primary metric is normalised recall at capacity: the
non-completers on a run's list divided by the most a list of that length can hold, pooled over runs (Table A.4). It
reads the quality of a list against the ceiling that capacity sets, and that ceiling varies widely: in the training
runs, a list of 5 per 20 at day 27 can hold between 46% and 100% of a run's non-completers (C13). At a fixed list
length, recall, precision and lift are re-expressions of the same count of non-completers on the list, so they serve
as secondary views rather than separate criteria.

**Secondary metrics.** Precision and PR-AUC must be read against the base
rate, which is their level by chance [24]. The ROC curve plots the rate of true
positives against the rate of false positives at every threshold, and the area under it (ROC-AUC) is the probability
that a non-completer scores above a completer; it is computed within each run, so that a model cannot score well
merely by separating high-rate runs from low-rate ones.

**Calibration.** Calibration is assessed because predicted risks can be unreliable even when discrimination is good
[33]. Two numbers summarise it: the calibration-in-the-large, the intercept of a recalibration model (a logistic
regression of the outcome on the score's log-odds) with the slope fixed at 1, whose target is 0 and which shows whether risks are too high or too low on average; and the calibration slope,
whose target is 1 and which falls below 1 when risks are too extreme [33]. Calibration cannot be a success criterion on
its own, since a model that gives every student the base rate is perfectly calibrated and useless [27].

**Net benefit.** Net benefit compares the model with contacting every student, no student or the students the rule
flags, at a range of threshold probabilities [25]. It describes a policy of contacting everyone above a threshold,
whereas AQ4 acts on a fixed capacity, so it serves as context rather than as a criterion.

**Success criteria fixed before testing.** A difference smaller than the variation between samples has little
practical meaning [31], and judging a model on several gates or populations would let one of them pass by chance, so
the design names a single gate and a single population. Table 4.5 fixes the success
criteria before any result exists.

**Table 4.5. Success criteria fixed before testing**

| ID | Criterion | Population and operating point | Role |
| :---- | :---- | :---- | :---- |
| S1 | Pooled normalised recall of the primary model above that of the rule-ranked list, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses reported | All 13 test runs, all eligible enrolments, day 27, 5 per 20 | Single gate for AQ3 and AQ4 (who is listed, D1) |
| S2 | Precision at capacity against the base rate and the attainable maximum | Same | Reported, not a gate |
| S3 | Calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2, pooled point estimates | Same | Condition for showing probabilities; otherwise ranks and reasons only |
| FR1 | No confirmatory group in which recall at capacity is more than 10 percentage points below that of the other students and the one-sided 95% bootstrap interval of the difference, Holm-adjusted over the three confirmatory groups (a correction that keeps the chance of any false flag at 5% across them), lies entirely below 0; a group meeting both conditions is flagged for review | Same; three confirmatory groups (Section 4.4) | Condition for use; a flag leads to review |

**Reading the gate.** S1 asks whether the model's lists, at the main operating point, reach more non-completers than
the rule's lists of the same length, with enough certainty that the gain is not chance. The paired two-level bootstrap and the
sign-flip test of Section 4.2 supply that certainty. Every other population, cut-off and capacity is a sensitivity analysis that
cannot change the verdict. The bounds of S3 allow an average predicted risk between about 40% and 49% when the training rate is 44.4%, a tolerance
of about five points, the size of the SMART Goal's target gain, and a spread of risks 20% too wide or too narrow. A
failed calibration check limits the output to ranks and reasons, and it never leads to
recalibration on the 2014 runs, which would let the test data shape the model.
