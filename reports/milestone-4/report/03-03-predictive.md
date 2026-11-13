## 3.3. Predictive Question

**Purpose.** AQ3 differs from AQ2 in purpose: a predictive model is judged by its accuracy on cases it has not seen,
not by how well it fits the cases it learned from [5], and the main threat is overfitting, a model that learns the
noise of its training data [3].

**Baselines.** Three baselines set the bar. The first is a random list, the level that any method must beat. The
second is the early-sign rule (C10), ranked by its number of signs, with ties broken by lower activity relative to the run (a student's clicks up to the
cut-off against the median of the same run); Milestone 1 named this rule as the comparison for deciding who is listed (D1), so beating it is what makes a
model worth using. The third is a background-only logistic model, with module, start month, previous attempts, credits, education and registration lead (how many days before the start
the student registered) but no activity, which shows how much of a ranking comes from who the
student is rather than from what the student does.

**Primary approach.** The primary approach is a penalised logistic regression, a logistic regression whose
coefficients are shrunk towards zero to limit overfitting, on the 19 usable primary predictors, with one model per cut-off; module and start month are categorical and enter
as dummy terms, one per level except a reference level, so the model has 23 parameters in all. The primary predictors, all dated on or before the cut-off, fall into four
groups: background, activity, assessment tasks and the number of computer-marked assessment (CMA) marks known by the
cut-off; the extended set adds 10 further predictors and the weekly click counts and is tried as an alternative (Table
2.1). A logistic model assumes that each predictor shifts the log-odds of non-completion by a fixed amount per unit,
while activity is strongly skewed, so counts enter as logarithms and every predictor is standardised, with every
transform refitted inside each fold (Section 4.2); Appendix I lists the predictors of each set and the transforms. The reasons
come from this project. Tutors must see why a student is listed, and a transparent model gives each student's reasons
from the same equation that ranks them [11]. The training runs hold 5,245 non-completers at day 27 and 5,519 at day
13, about 230 events (non-completers) per parameter, and the 11,811 training enrolments at day 27 are about seven times the 1,731 that the
minimum sample size criteria of Riley et al. require under their default assumptions [14], so the size of the data does not limit a logistic model. The two classes are close in size, 44–46% of enrolments not
completing, so no resampling or reweighting for imbalance is needed, and metrics are read against each run's base
rate (Section 4.3). The risk to be tested is transfer to a later run, and training on earlier runs
mirrors use [6], as OU early-warning studies do [15]. Differences between courses enter as module terms [16] rather
than as one model per module, because shrinkage does not rescue small samples [17]. A review of 71 clinical
comparisons supports the choice: among comparisons at low risk of bias, it found no difference in discrimination
between logistic regression and machine learning (author-reported) [18].

**Challenger and extension.** Gradient-boosted trees, an ensemble of small decision trees each fitted to the errors of
the previous ones, are the challenger, since tree ensembles outperform deep learning on tabular data of about 10,000
rows. That benchmark removed the datasets on which logistic regression came within 5% of the best models, so it does
not show that trees beat logistic regression [19]; they replace the primary approach only if they beat it by the
margin fixed in advance in Section 4.2. Discrete-time survival remains an extension, for the
reasons given in Section 2.2. Penalisation improves calibration only on average [17], so calibration is checked rather than assumed
(Section 4.3). Appendix I (Table A.6) compares the AQ3 baselines and candidates cell by cell against the eight criteria.

