## 6.3. Split Strategy and Leakage Control

**Leakage.** Leakage is the use of information about the target that would not be available at the moment of
prediction, and it makes a model look better in evaluation than it can be in use [10], [11]. The brief names five
forms of it for education data and asks for a rule against each [1]. Table 6.2 matches each form to its case in
OULAD, the control the pipeline applies and the check that would fail if the control broke.

**Table 6.2. Leakage risks and controls**

| Risk (brief) | Case in OULAD | Control | Check |
| :---- | :---- | :---- | :---- |
| Target leakage | Final result, withdrawal day, activity or submissions after the cut-off, TMA marks, whole-run measures | Feature views built only from events dated up to the cut-off; CMA marks only, seven days after submission; target and whole-run measures outside the predictor lists | V11, V13, V14 |
| Train–test contamination | Medians, scales and category levels computed on all runs | Fitted on the 2013 runs only and applied to the 2014 runs | V12 |
| Student leakage | 1,962 test enrolments of students who also enrolled in 2013 | Kept in the main test and flagged for a strict check; tuning folds keep each student on one side | V15 |
| Temporal leakage | A random split mixing the two years; tuning on 2014 | Training on 2013 (9 runs), test on 2014 (13 runs); tuning only inside 2013 | V15 |
| Augmentation leakage | None: no synthetic augmentation | – | – |
| Cohort statistic | The activity ratio uses the median of the same run | Only activity up to the cut-off of students enrolled at it; no outcome | V13 |

**Time split.** The data are split by year: the 9 runs of 2013 form the training set and the 13 runs of 2014 the
test set. This follows the OU's own practice of building at-risk models on previous runs of a module and applying
them to the run in progress [12], and the rule that data ordered in time are evaluated on later observations [13]. A
random split would mix the two years and let a model learn from the year it is tested on. Of the 13 test runs, the 9
whose module and start month also ran in 2013 test the claim directly, and the other 4 test a model on a module or
start month it has not seen, so their results are reported separately.

**Students seen in both years.** The 1,962 test enrolments of students who also enrolled in a 2013 run stay in the
main test set, because a later run of the same modules also contains repeating students, and a flag marks them so that
Milestone 4 can repeat the test on students never seen in training. When Milestone 4 tunes a model, it uses
leave-one-run-out folds inside 2013, holding out one run at a time, and keeps each student in one fold only, since
the same student on both sides of a fold would inflate the estimate [13].

**Fitted transforms.** Transforms that learn parameters from the data, such as filling a missing value with a median
or scaling a variable, are fitted on the training runs alone and then applied to the test runs [11]. As a check, the
parameters were fitted again after every test row had been changed, and they stayed the same, which shows that no
test row informs them. In addition, the 2014 outcomes are not looked at while the data are prepared: the validation
reports test outcome rates only as counts, so that the test set remains an independent check, as the brief requires
[1]. Test results will also be reported without the 89 day-13 test enrolments that are Withdrawn without a withdrawal
day, because such students may have left before the cut-off without a record of it.
