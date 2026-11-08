## 4.4. Error, Subgroup and Fairness Analysis

**Why groups are checked separately.** Building on the criteria of Section 4.3, the frozen model is evaluated
separately for each audit group, because aggregate metrics can hide differences between groups, an approach known as
slicing analysis [34]; TRIPOD+AI likewise asks for estimates by subgroup with intervals and for the approach used to
address fairness [21]. Gender, disability, deprivation band and age band stay out of the predictors and serve only the
audit, because leaving them out does not make a model blind to them: activity, previous attempts or credits can carry
the same information [36].

**One criterion must lead.** Fairness criteria cannot all hold at once when non-completion rates differ between
groups: a score with equal positive predictive value across groups cannot also have equal error rates [35], and
calibration within groups and balanced error rates conflict except in degenerate cases [53]. The audit therefore names
one primary criterion, separation, measured as equal recall at capacity across groups. Separation is recommended for
dropout prediction that allocates extra support [36], and it matches a contact whose main harm is missing a student
who struggles.

**The audit groups.** The confirmatory check covers the three groups that AQ4 names and that hold at least 400 test
enrolments: students with a declared disability (1,488 at day 27), the most deprived band, 0–10% (1,486), and the
missing deprivation band (610). At the training non-completion rates even the lowest-rate eligible group, the missing
band (28%), holds more than 100 non-completers. Students aged 55 or over (118 test enrolments, below the threshold of
400) are reported as a point gap, marked "insufficient data, not cleared". Table 4.9 gives each group's size and how
it is handled; eligibility is fixed here from enrolment counts, before any test outcome is opened.

**Table 4.9. Audit groups at day 27**

| Group | Training enrolments / non-completers | Test enrolments | Smallest test run | Handling |
| :---- | :---- | :---- | :---- | :---- |
| Female / male | 5,697 / 2,488 and 6,114 / 2,757 | 6,666 and 9,058 | 66 and 139 | Descriptive, per run and pooled |
| Declared disability | 1,123 / 602 | 1,488 | 18 | Confirmatory, pooled over runs |
| Deprivation band 0–10% | 1,163 / 699 | 1,486 | 17 | Confirmatory, pooled over runs |
| Deprivation band missing | 418 / 118 | 610 | 1 | Confirmatory, pooled; its own group, never merged with a band |
| Age 55 or over | 75 / 18 | 118 | 1 | Below the eligibility size: point gap only, "insufficient data, not cleared" |

**The checks.** Rule F1 of Table 4.8 flags a group for review; it does not reject the model, because a flag calls for
human judgement on why the gap arises. Earlier work on OULAD found that most published at-risk models reproduced and
slightly amplified a gap in favour of male students and showed erratic bias for students with a declared disability
(author-reported) [37], which is why the small groups are pooled over runs and reported with intervals. A proxy check
compares scores and predictors across groups, to show which predictors carry group information. The absolute
between-ROC area (ABROCA), the area between a group's ROC curve and that of the other students [34], stays
descriptive, because it measures differences across all thresholds rather than at the capacity where the decision is
made. Table 4.10 lists every fairness and error check; only the first row is confirmatory, and every other row is
descriptive.

**Table 4.10. Fairness and error checks**

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
