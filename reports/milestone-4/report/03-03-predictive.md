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
as dummy terms, one per level except a reference level, so the model has 23 parameters in all. The primary predictors fall into four groups, all dated on or before the cut-off: background (module, start month,
highest education, previous attempts, credits studied, registration lead, banked results, which are assessment results carried over from an earlier run of the module); activity (clicks before
the start and from the start to the cut-off, active days, resources used, inactivity in the last seven days, activity
relative to the run); assessment tasks (tasks due, missed and late, with late TMAs and late CMAs counted apart); and
the number of CMA marks known by the cut-off. The extended set adds 10 further predictors (a missing-registration
indicator, clicks counted with exactly repeated records taken once, clicks in the 14 days before the start, days since the last click, the trend over the
last week, tasks submitted early and clicks on four kinds of resource) and the weekly click counts, 2 at day 13 and 4 at
day 27; it is tried as an alternative (Table 2.3). A logistic model assumes that each predictor shifts the log-odds of
non-completion by a fixed amount per unit, while activity is strongly skewed: per enrolment the median is 602 clicks over
the whole run, and 2,503 enrolments lie beyond the upper interquartile-range fence. The predictors are therefore
transformed before the model reads them: counts enter as the logarithm of one plus the count, missing values are
filled with the training median and marked by a missing-value indicator, and every predictor is standardised with the
training mean and standard deviation, so that the penalty shrinks all coefficients on the same scale. Milestone 3
fitted these transforms on the 2013 runs alone and showed that no test row changes them; here they are refitted inside
each fold (Section 4.2), while gradient-boosted trees read the predictors untransformed. The reasons
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
margin fixed in advance in Section 4.2. A discrete-time survival model would fit a weekly hazard of withdrawal with
the same software [8], but the target joins Fail, decided at the end of the run, with Withdrawn, so survival remains an
extension. Penalisation improves calibration only on average [17], so calibration is checked rather than assumed
(Section 4.3). Appendix I (Table A.2) compares the AQ3 baselines and candidates cell by cell against the eight criteria.

