## Appendix II – Candidate Comparison by Criterion

The brief asks that each choice be argued against eight criteria: fit to the question, fit to the data, assumptions,
interpretability, complexity against the baseline, robustness and reproducibility, ethics and fairness, and
actionability [1]. AQ1 is a descriptive question answered by grouped rates with confidence intervals, which need no
model, so the comparison applies to AQ2, AQ3 and AQ4. Facts about the data come from the 9 training runs of 2013, which
cover 6 of the 7 modules: 11,811 enrolments with 5,245 non-completers at day 27 and 12,080 with 5,519 at day 13.

Table A.5 compares the candidates for AQ2, whose purpose is association within module rather than prediction, so its
yardstick is the size and precision of each association, not accuracy on new data [3].

**Table A.5. AQ2 candidates against the eight criteria**

| Criterion | Baseline: unadjusted rate difference per sign | Candidate 1: logistic regression with run fixed effects and sign × module terms (primary) | Candidate 2: mixed-effects logistic regression | Candidate 3: shallow classification tree (supplement) |
| :---- | :---- | :---- | :---- | :---- |
| Fit to question | Unadjusted rate difference per sign and module | Pooled within-run risk difference per sign, and module-specific differences from the interaction terms | Same, with module effects drawn from a population of modules | Shows which combinations of signs separate outcomes |
| Fit to data | 9 runs, 6 modules | Smallest run 369 enrolments and 91 non-completers; task signs only in runs with a task due by day 27 | 6 modules and 9 runs are few for estimating a variance | Many rows, but the splits change between samples |
| Assumptions | None beyond counting | Additive log-odds within module; all runs of these modules observed, so fixed effects suit the design [12] | Normal random effects; inference to unseen modules | None parametric; unstable splits |
| Interpretability | Highest | Risk differences in percentage points, with odds ratios beside them | Similar, plus variance terms | High for a depth of 2–3 |
| Complexity vs baseline | – | One model per cut-off with a few interaction terms | Adds a variance component for little gain within the observed modules | Low, but adds no effect size |
| Robustness and reproducibility | Exact | Deterministic; robust standard errors; sensitivity runs; signs correlated with each other checked | Convergence and few-cluster issues | Unstable across samples |
| Ethics and fairness | No sensitive attribute used | Sensitive attributes not used as signs | Same | Same |
| Actionability | Gives tutors the size of each sign's gap | Tells D2 which signs to look at; shown beside the unadjusted gap, because mutually adjusted estimates are partial effects | No extra action | Gives readable rules for tutors |

Table A.6 compares the candidates for AQ3, a predictive question judged by performance on a later run [5],
[6].

**Table A.6. AQ3 candidates against the eight criteria**

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

The choice of logistic regression rests first on this project's constraints. Tutors must see why a student is listed,
and a transparent model gives each student's reasons from the same equation that ranks them [11]; the 23 parameters
leave about 230 events each, so the training data are large enough for a stable logistic model [14]; and the risk to be
tested is transfer to a later run, which favours a simple, stable model [6]. The literature supports this choice:
a systematic review of 71 clinical prediction comparisons found, as its authors report, no difference in discrimination between logistic regression and machine learning among comparisons at low risk of bias [18].
Gradient-boosted trees stay as the challenger, since a benchmark that removed datasets where logistic regression came within 5% of the best models cannot show that trees beat it [19]; they replace logistic regression only if they beat it by the margin fixed in Appendix IV (Table A.13, step 4). The background-only model shows how much of the ranking comes from engagement rather than
from module and history. The survival model fits withdrawal timing, whereas the target joins Fail and Withdrawn at the
end of the run, so it stays a later extension.

Table A.7 compares the candidates for AQ4, where the output is a list of fixed length per run.

**Table A.7. AQ4 candidates against the eight criteria**

| Criterion | Baseline 1: random list | Baseline 2: rule-ranked list | Candidate 1: top-k by AQ3 score (primary) | Candidate 2: risk tiers | Rejected: benefit (uplift) ranking |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Fit to question | Chance level | List from the number of signs, ties broken by lower relative activity | The k enrolments with the highest risk per run, k from capacity | First tier the top 3 per 20, second tier the next 2 per 20, both fixed from capacity | Ranks by expected benefit of contact |
| Fit to data | – | Rule known at each cut-off | k = 3 or 5 per 20 enrolled | Same scores | No contact or treatment variable in the data [9] |
| Assumptions | – | Signs equally weighted | Risk order matches need: untested | Same | Randomised or unconfounded treatment [9] |
| Interpretability | – | High | Score and reasons | High | Low |
| Complexity vs baseline | – | – | Uses AQ3 scores only | Same | Needs an experiment first |
| Robustness | – | Exact | As AQ3 | As AQ3 | – |
| Ethics and fairness | Audit | Audit | Confirmatory audit of recall at capacity by group (Appendix V) | Same | – |
| Actionability | – | Direct | Tutor decides on the list; ranks and reasons, probabilities only if calibrated | Adds a second tier for lighter contact | Not available |

Ranking by risk is not ranking by benefit: in field experiments the customers at highest risk were not the best
targets of an intervention [20]. The list therefore supports the tutor's decision, and choosing whom to contact by
expected benefit needs a randomised study first (Section 5.2).
