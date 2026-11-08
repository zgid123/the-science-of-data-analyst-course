## 4.3. Metrics and Success Criteria

Under the protocol of Section 4.2, the primary metric is normalised recall at capacity: the non-completers on a run's
list divided by the most a list of that length can hold, pooled over runs. It reads list quality against the ceiling
set by capacity, which ranges from 46% to 100% of a run's non-completers for 5 per 20 at day 27 in the training runs (Change Log entry C13); at a fixed length, recall, precision and lift re-express the same count, so they are secondary views.
Precision and the area under the precision–recall curve (PR-AUC) must be read against the base rate [24]. The
receiver operating characteristic (ROC) curve plots true against false positive rates, and the area under the ROC curve (ROC-AUC) is computed within run, so that
separating high-rate from low-rate runs cannot inflate it. Calibration is assessed because risks can be unreliable even when discrimination is good, using the calibration-in-the-large, the intercept estimated with the slope fixed (target 0), and the calibration slope (target 1) [31]. Calibration cannot be a success criterion alone, since a model giving everyone the base rate is perfectly calibrated and useless [25]. Net benefit against contacting everyone, no one or by the rule [32] describes a threshold policy,
so it serves as context.

Table 4.2 fixes the success criteria before any result exists. A difference smaller than sampling variation has little
practical meaning [29], so the design names one gate and one population.

**Table 4.2. Success criteria fixed before testing**

| ID | Criterion | Population and operating point | Role |
| :---- | :---- | :---- | :---- |
| S1 | Pooled normalised recall of the primary model above that of the rule-ranked list, with the 95% paired two-level bootstrap interval of the difference above 0 and a one-sided sign-flip test on the 13 per-run differences with a p-value below 0.05; wins, ties and losses reported | All 13 test runs, all eligible enrolments, day 27, 5 per 20 | Single gate for AQ3 and AQ4 (who is listed, D1) |
| S2 | Precision at capacity against the base rate and the attainable maximum | Same | Reported, not a gate |
| S3 | Calibration-in-the-large between −0.2 and 0.2 and slope between 0.8 and 1.2, pooled point estimates | Same | Condition for showing probabilities; otherwise ranks and reasons only |
| F1 | No confirmatory group in which recall at capacity is more than 10 percentage points below that of the other students and the one-sided 95% bootstrap interval of the difference, Holm-adjusted over the three confirmatory groups, lies entirely below 0; a group meeting both conditions is flagged for review | Same; three confirmatory groups (Section 4.4) | Condition for use; a flag leads to review |

The bootstrap resamples runs and then enrolments, re-forms each run's list and compares model and rule on the same
resample, because treating nested observations as independent inflates false positives [33]; with only 13 runs such
intervals can be too narrow, so the sign-flip test is also required. Every other population, cut-off and capacity is a
sensitivity analysis that cannot change the verdict. A failed calibration check limits the output to ranks and
reasons and never leads to recalibration on the 2014 runs.
