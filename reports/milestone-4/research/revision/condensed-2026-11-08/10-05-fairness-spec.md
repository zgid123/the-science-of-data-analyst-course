## Appendix V – Error and Fairness Analysis Specification

Aggregate metrics can hide differences between groups, so the frozen model is evaluated separately for each audit
group of the test runs, an approach known as slicing analysis [34]. Gender, disability, deprivation band and age band
stay out of the predictors and serve only the audit, because leaving them out does not make a model blind to them:
activity, previous attempts or credits can carry the same information [36]. Table A.15 gives each group's size in the
prepared views and how it is handled; outcome counts are for the 2013 training runs, test sizes are enrolments only,
and eligibility for the confirmatory check is fixed in this proposal from enrolment counts, before any test outcome is opened.

**Table A.15. Audit groups at day 27**

| Group | Training enrolments / non-completers | Test enrolments | Smallest test run | Handling |
| :---- | :---- | :---- | :---- | :---- |
| Female / male | 5,697 / 2,488 and 6,114 / 2,757 | 6,666 and 9,058 | 66 and 139 | Descriptive, per run and pooled |
| Declared disability | 1,123 / 602 | 1,488 | 18 | Confirmatory, pooled over runs |
| Deprivation band 0–10% | 1,163 / 699 | 1,486 | 17 | Confirmatory, pooled over runs |
| Deprivation band missing | 418 / 118 | 610 | 1 | Confirmatory, pooled; its own group, never merged with a band |
| Age 55 or over | 75 / 18 | 118 | 1 | Below the eligibility size: point gap only, "insufficient data, not cleared" |

Fairness criteria cannot all hold at once when non-completion rates differ between groups: a score with equal
positive predictive value across groups cannot also have equal error rates [35], and calibration within groups and
balanced error rates conflict except in degenerate cases [53]. The audit therefore names one primary criterion:
separation, measured as equal recall at capacity across groups, which suits a supportive contact where missing a
struggling student is the main harm [36]. Table A.16 lists the checks; only the first row is confirmatory, and every
other row is descriptive.

**Table A.16. Fairness and error checks**

| Check | Measure | Rule |
| :---- | :---- | :---- |
| Confirmatory fairness (separation) | Recall at capacity of each eligible group (at least 400 test enrolments) minus the rest, day 27, k = 5 per 20, pooled within run | A group is flagged for review when its recall at capacity is more than 10 percentage points below that of the other students and the one-sided 95% bootstrap interval of the difference, Holm-adjusted over the three confirmatory groups, lies entirely below 0; groups below 400 test enrolments are reviewed on the point gap alone and reported as not cleared |
| Selection | Share of each group on the list against its share of non-completers | Descriptive |
| Precision by group | Precision at capacity per group | Descriptive; differences expected when base rates differ [35] |
| Calibration by group | Calibration-in-the-large and slope; a curve only with about 200 events and 200 non-events [31] | Descriptive, with intervals |
| Threshold-free gap | ABROCA within run, pooled, with the sign of the difference in discrimination and a reference from group labels shuffled within run [34] | Descriptive; never triggers review on its own |
| Proxy check | Score distribution and predictor means by group | Descriptive; shows which predictors carry group information |
| Errors by run and module | Missed non-completers and listed completers per run; module CCC reported separately | Runs below the rule are examined |
| Errors by activity and history | No, low and normal activity; previous attempts; late registration | Shows whether the model adds value beyond inactivity |
| Errors by outcome kind and reach | Fail and Withdrawn among missed and listed non-completers; withdrawal within 7 days after the cut-off | Shows which non-completion the list misses and whom it cannot reach |
| List stability | Share of bootstrap resamples in which a student near rank k stays on the list | Shows how arbitrary the cut at k is |

Earlier work on OULAD found a gap in favour of male students that most at-risk models reproduced and slightly
amplified, and erratic bias for the under-represented students with a declared disability, which is why the small
groups are pooled over runs and reported with intervals [37].
