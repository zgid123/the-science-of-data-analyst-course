## 4.2. Validation Strategy

**Test on unseen runs.** The cards of Section 4.1 rest on one validation design, drawn in Appendix III (Figure A.2). Testing on data
not used in model development is the core requirement of TRIPOD+AI [21], and the 13 test runs of 2014 share no run with
development. Testing on a later period is in addition a form of external validation [27], and in predicting student
success only an evaluation on a future course gives an honest estimate of how a model will perform in use [23]. The
1,586 test enrolments at day 27 of students already seen in the 2013 development data stay in the test, as they would in use, and are
removed in a sensitivity analysis.


**Development folds.** Development uses only the 9 runs of 2013. Each run forms its own fold, so each model is
validated on a whole run it did not see, because ignoring the group structure of data seriously underestimates
prediction error [28]. Students who also appear in the held-out run are removed from that fold's training data, since
a validation fold must hold only groups that are absent from training [29]. Every step that learns from data, including
the filling of missing values, the scaling and the tuning of the model, is repeated inside each fold, because a tuned
cross-validation score is substantially optimistic [30], and over-fitting the criterion used to select a model can
bias results as much as the differences between algorithms [31].

**When a challenger wins.** Gradient-boosted trees, or the extended set of 10 further predictors with the weekly
clicks, replace the primary choice only with a gain of at least 0.03 in pooled normalised recall, about 89 more non-completers listed over the 9 runs, and a gain in at least 7 of the 9 folds; if the two were equal,
a gain in 7 or more folds would occur by chance with a probability of about 0.09. The margin is fixed now, before any
fold result exists, so that a small, chance improvement cannot change the choice.

**Two freezes and one test.** The protocol follows the two-step freeze proposed for predictive modeling: the
question, splits, metrics and baselines are fixed before training, and the final model is fixed, with access to the
test data recorded, before testing [26]. The chosen model is refitted on all 2013 runs and scored once on the 13 runs
of 2014. Results are also reported apart for the 9 paired runs, whose module and start month also ran in 2013, and for
the 4 unpaired runs.

**Two features of the run structure.** Module CCC, which has no run in 2013, and the February 2014 runs, which reach
their cut-offs before the October 2013 runs end, each receive a rule of their own: an unseen module receives the
average module, and a labels-available variant scores the 2014 B runs with a model trained only on the 2013 B runs
(Appendix III).

**The protocol step by step.** Appendix III (Table A.13) lists the eight steps of the protocol in order, with the data
each uses, what happens and why; the paragraphs above describe each of them.

**Uncertainty.** Uncertainty about the gate comes from a paired two-level bootstrap over runs and over enrolments
within runs, because treating nested observations as independent inflates false positives [32], and, since 13 test
runs can make such intervals too narrow, from a sign-flip permutation test on the 13 per-run differences (Appendix
III).

**Sample sizes.** Appendix III (Table A.14) gives the sample sizes behind these choices, computed from the prepared
views without fitting a model, with the minimum development size under the three criteria of Riley et al. [14];
outcome counts come from the 2013 runs only, so the 2014 outcomes stay unseen.
