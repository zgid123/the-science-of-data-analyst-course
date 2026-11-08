## 6.3. Split Strategy and Leakage Control

Leakage is the use of information about the target that would not be available at prediction time, and it inflates
estimated performance [10], [11]; Table 6.2 matches each risk the brief names to a control and a check.

**Table 6.2. Leakage risks and controls**

| Risk (brief) | Case in OULAD | Control | Check |
| :---- | :---- | :---- | :---- |
| Target leakage | Final result, withdrawal day, later events, TMA marks | Events up to the cut-off only; CMA marks 7 days after submission | V11, V13, V14 |
| Train–test contamination | Medians, scales, levels fitted on all runs | Fitted on 2013 runs only | V12 |
| Student leakage | 1,962 test enrolments of students seen in 2013 | Flagged; folds keep each student on one side | V15 |
| Temporal leakage | Random split across years | Training 2013 (9 runs), test 2014 (13 runs) | V15 |
| Augmentation leakage | None | No augmentation | – |

The time split follows the OU's practice of building at-risk models on previous runs of a module and applying them
to the run in progress [12], and the rule that time-dependent data are evaluated on future observations [13].
Transforms that learn parameters from the data, such as filling values and scaling, use the training runs alone [11];
as a check, they were fitted again after every test row had been changed, and the parameters stayed the same. Folds must keep each student on one side [13], so tuning in Milestone 4 uses leave-one-run-out
folds inside 2013 with each student in one fold, and test results are also reported for the 4 runs without a 2013
counterpart and without the 89 day-13 test enrolments that are Withdrawn without a withdrawal day.
