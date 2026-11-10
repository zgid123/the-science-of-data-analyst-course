# Split and leakage specification (Task 6, brief section 11)

| Risk (brief 11) | Case in this project | Control | Where | Check |
| :---- | :---- | :---- | :---- | :---- |
| Target leakage | final_result, withdrawal day, activity or submissions after the cut-off, TMA marks (release day unknown), whole-run measures | Feature views computed only from events dated ≤ c; target and whole-run measures kept out of the predictor list; CMA marks only | `prepare_data.py` step 8; dictionary role | V13 (max event day per feature ≤ c), V14 (roles) |
| Train–test contamination | Imputation values, scaling, category levels, log transforms fitted on all runs | Fitted on training runs (2013) only and applied to test runs | `fit_transforms.py` | V12 (parameters unchanged when test rows are altered) |
| Student leakage | 2014 enrolments of students already seen in 2013 runs | Main test keeps them (the claim is a later run of the same modules, where repeaters exist); `student_in_training_runs` marks them for a strict unseen-student check | `prepare_data.py` step 9 | V15 flag recomputed independently |
| Temporal leakage | Random split across years; tuning on 2014 | Split by run year: training 2013B, 2013J (9 runs); test 2014B, 2014J (13 runs); tuning only inside 2013 by leave-one-run-out folds that also keep each student in one fold; intervals by bootstrap clustered by student; 2014 outcomes are not looked at while preparing | `prepare_data.py` step 9; Milestone 4 protocol | V15 (no run in both partitions); validation reports test outcome rates only as counts |
| Cohort statistic | `activity_ratio_run` uses the same run's median up to c | Uses only pre-cut-off activity of students enrolled at c, no outcome; the same value is known to staff on day c | step 8 | V13 |
| Augmentation leakage | None: no synthetic augmentation | – | – | – |

Paired subset: the 9 test runs whose module and start month also ran in 2013 (BBB-B, DDD-B, FFF-B, AAA-J, BBB-J,
DDD-J, EEE-J, FFF-J, GGG-J); the other 4 test runs (CCC-B, CCC-J, EEE-B, GGG-B) test a model trained on other
modules or start months and are reported separately.
