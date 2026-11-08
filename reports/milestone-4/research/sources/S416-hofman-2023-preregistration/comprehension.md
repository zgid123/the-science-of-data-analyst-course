# S416 – Pre-registration for predictive modeling (Hofman, Chatzimparmpas, Sharma, Watts & Hullman, arXiv 2023)

## Summary in my own words

The authors argue that predictive modelling has its own "researcher degrees of freedom" – choice of outcome, data filtering, split, metric, baselines – and that adjusting these after seeing results, or re-optimising after looking at the test set ("over-hyping"), inflates reported performance. They propose a lightweight two-step pre-registration: phase A before training fixes the research question, outcome, predictors, train/test construction, filtering, metrics and baselines; phase B after model selection but before testing fixes the final model, seeds and hyperparameters and records whether the test set was accessed. In a qualitative study with ML researchers, the protocol prevented several biased out-of-sample estimates, though half of the participants were willing to re-access the test data after poor results. They caution that pre-registration is not a panacea.

## Key facts

- Degrees of freedom – "that can affect how problems are operationalized and how models are developed and tested"
- Over-hyping – "(e.g., by adjusting hyperparameters or changing evaluation metrics after accessing the test set), known as"
- Single access – "While multiple accesses to the test set clearly violate the underlying principle of out-of-sample testing"
- Two steps – "a two-step pre-registration process, with the first step prior to training and the second step prior to testing."
- Phase A contents – "what metrics will be used, and what baselines the model will be compared to."
- Purpose of phase A – "to discourage adjustment of the problem definition based on the results of the modeling exercise."
- Phase B – "the researcher completes phase (B) of the pre-registration form before testing the model."
- Effect – "This helps to cleanly separate model building from model evaluation and should reduce the prevalence of issues like algorithmic leakage and overfitting by multiple accesses of the test set."
- Study finding – "multiple participants might have produced biased estimates of out-of-sample performance had they not adhered to the protocol"
- Limits – "pre-registration is not a panacea"
- Degrees of freedom follow Hullman J. et al. (2022) – "resulting in replication issues (Hullman et al., 2022)."

## Used in

04-00-evaluation-design.md, 04-03-metrics-success.md, 04-02-validation-strategy.md

## Against reference.md

Confirms the outline's "frozen plan" and "single use of the test runs": phase A matches the evaluation design cards (metrics, baselines, success criteria fixed before training) and phase B matches freezing the model before the 2014 runs are scored. No contradiction.

## Reliability

Primary but not peer-reviewed in the fetched form: arXiv:2311.18807v1 (30 November 2023) by Hofman J.M., Sharma A., Watts D.J. (Microsoft Research; University of Pennsylvania), Chatzimparmpas A. and Hullman J. (Northwestern University). Citation count not retrieved (arXiv metadata lookup failed) as of 2026-11-06. Only v1 found on arXiv as of November 2026; no journal version located.

## Open questions

Preprint status: the report should present it as a proposal with a small qualitative study, not as an established standard.
