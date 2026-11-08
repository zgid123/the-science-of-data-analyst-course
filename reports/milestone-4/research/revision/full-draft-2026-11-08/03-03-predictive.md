## 3.3. Predictive Question

**Purpose.** AQ3 differs from AQ2 in purpose: a predictive model is judged by its accuracy on cases it has not seen,
not by how well it fits the cases it learned from [5], and the main threat is overfitting, a model that learns the
noise of its training data [3].

**Baselines.** Three baselines set the bar. The first is a random list, the level that any method must beat. The
second is the early-sign rule (C10), ranked by its number of signs, with ties broken by lower activity relative to the
run; Milestone 1 named this rule as the comparison for deciding who is listed (D1), so beating it is what makes a
model worth using. The third is a background-only logistic model, with module, start month, previous attempts,
credits, education and registration lead but no activity, which shows how much of a ranking comes from who the
student is rather than from what the student does.

**Primary approach.** The primary approach is a penalised logistic regression, a logistic regression whose
coefficients are shrunk towards zero to limit overfitting, on the 19 usable primary predictors, with one model per
cut-off and module and start-month terms, 23 parameters in all. The weekly clicks, whose sum is already a primary
predictor, join the extended set of 10 further predictors (Table 2.3), which is tried as an alternative. The reasons
come from this project. Tutors must see why a student is listed, and a transparent model gives each student's reasons
from the same equation that ranks them [11]. The training runs hold 5,245 non-completers at day 27 and 5,519 at day
13, about 230 per parameter, and the 11,811 training enrolments at day 27 are about seven times the 1,731 that the
minimum sample size criteria of Riley et al. require under their default assumptions [14], so the size of the data
does not limit a logistic model. The risk to be tested is transfer to a later run, and training on earlier runs
mirrors use [6], as OU early-warning studies do [15]. Differences between courses enter as module terms [16] rather
than as one model per module, because shrinkage does not rescue small samples [17]. A review of 71 clinical
comparisons supports the choice: among comparisons at low risk of bias, it found no difference in discrimination
between logistic regression and machine learning (author-reported) [18].

**Challenger and extension.** Gradient-boosted trees, an ensemble of small decision trees each fitted to the errors of
the previous ones, are the challenger, since tree ensembles outperform deep learning on tabular data of about 10,000
rows. That benchmark removed the datasets on which logistic regression came within 5% of the best models, so it does
not show that trees beat logistic regression [19]; they replace the primary approach only if they beat it by the
margin fixed in advance in Section 4.2. A discrete-time survival model would fit a weekly hazard of withdrawal with
the same software [8], but the target joins Fail, decided at the end of the run, with Withdrawn, so survival remains an
extension. Penalisation improves calibration only on average [17], so calibration is checked rather than assumed
(Section 4.3). Table 3.3 compares the AQ3 baselines and candidates against the eight criteria.

**Table 3.3. AQ3 candidates against the eight criteria**

| Criterion | Baseline 1: early-sign rule | Baseline 2: background-only logistic model | Candidate 1: penalised logistic regression (primary) | Candidate 2: gradient-boosted trees | Candidate 3: discrete-time survival model |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Fit to question | Flags a task missed, a TMA late or no activity in the last 7 days; ranks by number of signs | Risk from module, start month, previous attempts, credits, education and registration lead only | Risk of non-completion at each cut-off from all primary predictors | Same, with non-linear effects and interactions | Weekly hazard of withdrawal [8] |
| Fit to data | No fitting | Few parameters | 23 parameters against 5,245–5,519 training non-completers, about 230 per parameter; the 11,811–12,080 training enrolments are about seven times the 1,728–1,731 that the minimum sample size criteria require for this set [14] | Suits tabular data of about 10,000 rows [19] | Fail is decided at the end of the run, not at a time, and few enrolments are censored |
| Assumptions | Signs equally weighted | Additive log-odds | Additive log-odds on transformed predictors | Few; tuning of depth, rate and number of trees | Non-informative censoring; a competing-risk or separate model for Fail |
| Interpretability | Highest | High | Coefficients and per-student contributions from the same model that ranks [11] | Post-hoc explanations, which can mislead [11] | Readable, but per week |
| Complexity vs baseline | – | Small | Small step from the rule | Larger; maintenance and entanglement risks [10] | Moderate; same software as logistic regression [8] |
| Robustness and reproducibility | Exact | Stable | Stable; penalty tuned in grouped folds | More tuning choices; selection bias risk [29] | Stable |
| Ethics and fairness | Equal weights do not give equal error rates; audited like the models | Audit | Audit; proxy check | Same audit; harder to explain a disparity | Same audit |
| Actionability | Directly explainable | Shows what background alone gives | Score plus each student's own largest contributions | Score; reasons only through approximations | Adds timing, which D1 does not use at fixed cut-offs |
