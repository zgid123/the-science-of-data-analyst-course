## 3.3. Predictive Question

AQ3 differs from AQ2 in purpose: a model is judged by its accuracy on cases it has not seen, not by its fit [5],
and the main threat is overfitting [3]. Three baselines set the bar: a random list; the early-sign rule (Change Log entry C10, Section 1.1), ranked by its number
of signs with ties broken by lower activity relative to the run, which Milestone 1 named as the comparison for deciding who is listed for contact (D1);
and a background-only logistic model (module, start month, previous attempts, credits, education, registration lead),
which shows how much of a ranking comes from who the student is rather than from what the student does.

The primary approach is a penalised logistic regression on the 19 usable primary predictors, one model per cut-off with module and start-month terms (23 parameters); the weekly clicks, whose sum is already a primary predictor, are added to the extended set of 10 further predictors (Appendix I). The reasons are rooted in this project. Tutors must see why a
student is listed, and a transparent model gives each student's reasons from the same equation that ranks them [11].
The training runs hold 5,245 non-completers at day 27 and 5,519 at day 13, about 230 per parameter, and the 11,811 training enrolments at day 27 are about seven times the 1,731 that the minimum sample size criteria of Riley et al. require under their default assumptions [14], so the size of the training data does not limit the logistic model. Transfer to a later run is the risk to be tested, and training on earlier runs mirrors use
[6], as OU early-warning studies do [15]; course differences enter as module terms [16] rather than as per-module
models, because shrinkage does not rescue small samples [17]. A review of 71 clinical comparisons supports the choice:
at low risk of bias it found no difference in discrimination between logistic regression and machine learning
(author-reported) [18].

Gradient-boosted trees are the challenger, since tree ensembles outperform deep learning on tabular data of about
10,000 rows; that benchmark removed datasets on which logistic regression came within 5% of the best models, so it does not show that
trees beat it [19]. They replace the primary approach only if they beat it by the margin fixed in Section 4.2. A discrete-time
survival model fits a weekly hazard of withdrawal with the same software [8], but the target joins Fail, decided at
the end of the run, with Withdrawn, so it remains an extension. Penalisation improves calibration only on average
[17], so calibration is checked rather than assumed (Section 4.3).
