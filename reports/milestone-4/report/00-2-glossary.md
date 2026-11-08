# List of Terms

The terms below are listed in alphabetical order with their meaning in this report and the section that defines them.

| Term | Meaning in this report |
| :---- | :---- |
| Add-drop period | The first weeks of a course in which students may still register for or drop it (Section 1.1) |
| Attainable recall | The largest share of a run's non-completers that a list of length k can hold, min(k, non-completers) divided by non-completers (Section 4.3) |
| Background-only model | A logistic model using module, start month, previous attempts, credits, education and registration lead, without any activity (Section 3.3) |
| Base rate | The share of a run's enrolments who do not complete; the precision of a random list (Section 1.1) |
| Baseline | The simple method that a candidate must beat to be worth its complexity (Section 3.1) |
| Calibration slope | The coefficient of the score's log-odds in a logistic recalibration, a logistic regression of the outcome on that log-odds; 1 when risks are neither too extreme nor too flat (Section 4.3) |
| Calibration | Agreement between predicted risks and observed rates (Section 4) |
| Calibration-in-the-large | The intercept of a logistic model of the outcome with the score's log-odds as offset (a term whose coefficient is fixed at 1); 0 when the average predicted risk is right (Section 4.3) |
| Capacity | The number of students tutors can contact: 3 or 5 per tutor group, a group assumed to hold 20 students, that is 15% or 25% of a run's enrolments (Section 3.4) |
| Cut-off | The day up to which a predictor may use data: day 13 (end of week 2) or day 27 (end of week 4) (Section 1.1) |
| Discrimination | How well a model separates students who will not complete from those who will (Section 4) |
| Early-sign rule | A task due by the cut-off not submitted, or a TMA submitted late, or no platform activity in the seven days before the cut-off (Section 1.1) |
| Enrolment | One student in one module run, the unit of analysis (Section 1.1) |
| Fixed effects | Terms for each module run, so that students are compared only within the same run (Section 3.2) |
| Freeze | A recorded point after which a choice cannot change: the first before training, the second before testing (Section 4.2) |
| Gradient-boosted trees | An ensemble of small decision trees, each fitted to the errors of the previous ones; the AQ3 challenger (Section 3.3) |
| Labels-available variant | A sensitivity analysis that scores the 2014 February runs with a model trained only on the 2013 February runs, the runs whose outcomes are known at that time (Section 4.2) |
| Leave-one-run-out folds | Development folds in which each 2013 run is held out once (Section 4.2) |
| Lift | Precision at capacity divided by the run's base rate; 1 means chance (Section 4.3) |
| Module run | One offering of an OU module, named by its year and start month, B for February and J for October (Section 1.1) |
| Non-completion | A final result of Fail or Withdrawn, the target of AQ3 (Section 1.2) |
| Normalised recall | Recall at capacity divided by attainable recall, pooled over runs; the primary metric (Section 4.3) |
| Overfitting | A model learning the noise of its training data, so that it performs worse on new cases (Section 3.3) |
| Paired run | A 2014 test run whose module and start month also ran in 2013 (Section 4.2) |
| Penalised logistic regression | A logistic regression whose coefficients are shrunk towards zero to limit overfitting; the AQ3 primary approach (Section 3.3) |
| Primary approach | The candidate chosen for a question, with its reasons (Section 3.1) |
| Precision at capacity | The share of a run's list of length k who do not complete (Section 4.1) |
| Recall at capacity | The share of a run's non-completers who are on its list of length k (Section 4.3) |
| Risk difference | The difference in non-completion rate, in percentage points, between students with and without a sign (Section 3.2) |
| Separation | The fairness criterion of equal recall at capacity across groups (Section 4.4) |
| Sign-flip permutation test | A test of how often per-run differences as favourable would appear if the sign of each run's difference were random (Section 4.2) |
| Slicing analysis | Evaluation of the frozen model separately for each audit group (Section 4.4) |
| Technical task | The kind of analysis a question needs: aggregation, association, classification or ranking (Section 2.2) |
| Two-level bootstrap | Resampling of runs and then of enrolments within each run, to estimate uncertainty that respects the run structure (Section 4.2) |
