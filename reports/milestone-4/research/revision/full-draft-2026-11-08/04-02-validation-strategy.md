## 4.2. Validation Strategy

**Test on unseen runs.** The cards of Section 4.1 rest on one validation design, shown in Figure 4.1. Testing on data
not used in model development is the core requirement of TRIPOD+AI [21], and the 13 test runs of 2014 share no run with
development. Testing on a later period is in addition a form of external validation [25], and in predicting student
success only an evaluation on a future course gives an honest estimate of how a model will perform in use [23]. The
1,586 test enrolments at day 27 of students already seen in 2013 stay in the test, as they would in use, and are
removed in a sensitivity analysis.

![Figure 4.1. Validation and test protocol from the first freeze to the single test on the 2014 runs](assets/figures/fig-4-1-validation.png){width=100%}

**Development folds.** Development uses only the 9 runs of 2013. Each run forms its own fold, so each model is
validated on a whole run it did not see, because ignoring the group structure of data seriously underestimates
prediction error [26]. Students who also appear in the held-out run are removed from that fold's training data, since
a validation fold must hold only groups that are absent from training [27]. Every step that learns from data, including
the filling of missing values, the scaling and the tuning of the model, is repeated inside each fold, because a tuned
cross-validation score is substantially optimistic [28], and over-fitting the criterion used to select a model can
bias results as much as the differences between algorithms [29].

**When a challenger wins.** Gradient-boosted trees, or the extended set of 10 further predictors with the weekly
clicks, replace the primary choice only with a gain of at least 0.03 in pooled normalised recall, about 89 more
non-completers listed over the 9 runs, and a gain in at least 7 of the 9 folds. The margin is fixed now, before any
fold result exists, so that a small, chance improvement cannot change the choice.

**Two freezes and one test.** The protocol follows the two-step freeze proposed for predictive modeling: the
question, splits, metrics and baselines are fixed before training, and the final model is fixed, with access to the
test data recorded, before testing [30]. The chosen model is refitted on all 2013 runs and scored once on the 13 runs
of 2014. Results are also reported apart for the 9 paired runs, whose module and start month also ran in 2013, and for
the 4 unpaired runs.

**Two features of the run structure.** Module CCC has no run in 2013, so module terms are coded as deviations from the
average module, and an unseen module receives the average. Presentations coded B start in February and those coded J
in October [2], and the 2013 J runs last 261–268 days, so their outcomes are not yet known when the 2014 B runs reach
their cut-offs; a labels-available variant therefore also scores the 2014 B runs with a model trained only on the 2013
B runs, the only runs whose outcomes a university would hold at that time.

**The protocol step by step.** Table 4.6 lists the steps of the protocol in order, with the data each uses, what
happens and why.

**Table 4.6. Validation and test protocol**

| Step | Data | What happens | Why |
| :---- | :---- | :---- | :---- |
| 1. First freeze | – | This proposal fixes AQs, populations, predictor sets, the early-sign rule (Change Log entry C10), splits, metrics, baselines and success criteria | Choices cannot follow the results [30] |
| 2. Development folds | 9 runs of 2013 (6 modules) | Leave-one-run-out: each run is the validation fold once; rows of students who also appear in the validation run (121–129 students, 242–258 rows) are removed from that fold's training data, in outer and inner loops alike | Validation folds must hold only groups absent from training [27]; random folds underestimate error on structured data [26] |
| 3. Fitting inside folds | Training fold only | Imputation, scaling and encoding refitted in each fold; penalty of the logistic regression and depth, learning rate and number of trees of the boosted trees tuned by an inner leave-one-run-out loop; optional logistic recalibration fitted inside development | Preprocessing learnt on training data only [27]; tuning inside each loop keeps the estimate nearly unbiased [28], [29] |
| 4. Model choice | Outer-fold results | Four configurations, penalised logistic regression and gradient-boosted trees each with the primary and with the extended predictor set, compared on pooled normalised recall at day 27, k = 5 per 20, the S1 metric: boosted trees replace logistic regression, and the extended predictor set the primary set, only with a gain of at least 0.03, about 89 more non-completers listed over the 9 runs, and a gain in at least 7 of 9 folds. Fold results serve the choice only and are never reported as expected performance | Ties go to the simpler model [5]; differences within sampling variation have little practical meaning [29], [52] |
| 5. Second freeze | All 2013 runs | The chosen model refitted on all 9 runs; specification, parameters and file hash recorded with the time of the first test access | Final model fixed before testing [30] |
| 6. Single test | 13 runs of 2014 | Scores, lists and all metrics of Appendix III computed once; S1 judged on all 13 runs and all eligible enrolments | Data sharing no run with development [21]; a later run is a temporal validation [25] |
| 7. Sensitivity | 13 runs of 2014 | Paired runs (9, module and start month also run in 2013) and unpaired runs (4); module CCC apart; without test enrolments of students seen in 2013; without the Withdrawn enrolments that lack a withdrawal day; labels-available variant; day 13 and k = 3 per 20. None can change the S1 verdict | Later-run estimates are the honest ones [23]; one declared primary comparison prevents choosing a favourable variant |
| 8. AQ2 replication | 13 runs of 2014 | AQ2 associations re-estimated, CCC included | Opens the test outcomes only after step 6; changes nothing in AQ3 |

**Uncertainty.** Uncertainty about the gate comes from a paired two-level bootstrap: runs are resampled, then
enrolments within each sampled run, each run's list is formed again from its resampled enrolments, and the difference
between model and rule is computed on the same resample, because treating nested observations as independent inflates
false positives [33]. With only 13 test runs such intervals can be too narrow, so the gate also requires a sign-flip
permutation test on the 13 per-run differences, which asks how often differences as favourable would appear if the sign
of each run's difference were random.

**Sample sizes.** Table 4.7 gives the sample sizes behind these choices, computed from the prepared views without
fitting a model; outcome counts come from the 2013 runs only, so the 2014 outcomes stay unseen. The minimum
development size follows the three criteria of Riley et al.: expected shrinkage of at least 0.9, optimism in
Nagelkerke R² of at most 0.05, and the overall risk estimated within 0.05 [14].

**Table 4.7. Sample sizes for development and evaluation**

| Quantity | Day 13 | Day 27 |
| :---- | :---- | :---- |
| Training enrolments (2013, 9 runs, 6 modules) | 12,080 | 11,811 |
| Training non-completers | 5,519 (45.7%) | 5,245 (44.4%) |
| Smallest training run: enrolments / non-completers | 370 / 92 | 369 / 91 |
| Most non-completers a list of 5 per 20 can hold, 9 training runs | 3,032 | 2,976 |
| Parameters, primary set (19 predictors, module and start-month terms) | 23 | 23 |
| Parameters, primary and extended sets with weekly clicks | 35 | 37 |
| Events per parameter, primary set / with extended set and weekly clicks | 240 / 158 | 228 / 142 |
| Minimum development size (Riley criteria), primary set / with extended set and weekly clicks | 1,728 / 2,629 | 1,731 / 2,784 |
| Test enrolments (2014, 13 runs, 7 modules) | 15,989 | 15,724 |
| Test enrolments in the 9 paired / 4 unpaired runs | 10,902 / 5,087 | 10,801 / 4,923 |
| Test enrolments of students seen in 2013 | 1,637 | 1,586 |
| Test enrolments Withdrawn without a withdrawal day | 89 | 90 |
| Test run size, smallest / largest | 350 / 2,079 | 348 / 2,021 |

**C14.** AQ2 is replicated on 2014 only after the single test, which is Change Log entry C14: it changes when AQ2 is
estimated on the test runs, not what AQ2 asks, and it protects the independence of the AQ3 test.
