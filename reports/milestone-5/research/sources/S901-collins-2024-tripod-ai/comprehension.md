# S901 – TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods (Collins et al., BMJ 2024)

## Summary in my own words

TRIPOD+AI is the 2024 consensus reporting guideline for studies that develop or evaluate prediction models, whether built by regression or machine learning; it replaces TRIPOD 2015. It was produced through a Delphi survey and a consensus meeting and consists of a 27 item checklist plus an abstracts checklist. For evaluation design it fixes the vocabulary the report needs: evaluation (test) data must not overlap with training, tuning or model selection data; internal validation covers split, cross-validation and bootstrapping; model evaluation means discrimination, calibration and clinical utility (decision curve analysis). It asks authors to justify the sample size separately for development and evaluation, to state every measure and its rationale, to report performance with confidence intervals including key sociodemographic subgroups, and to describe fairness approaches; fairness items are embedded across the checklist.

## Key facts

- Scope and status – "The new checklist supersedes the TRIPOD 2015 checklist, which should no longer be used."
- Size – "The TRIPOD+AI statement consists of a 27 item checklist, an expanded checklist that details reporting recommendations for each item, and a TRIPOD+AI for Abstracts checklist containing 13 items"
- Evaluation data separation – "Evaluation data should be distinct from the data used to train the model, tune hyperparameters, or do model selection, such that there is no overlap in participants between the training and evaluation data."
- Internal validation – "Evaluating the performance of a prediction model on the same population on which the model was developed (eg, train test split, cross validation, or bootstrapping)."
- What evaluation covers – "Evaluating predictive accuracy of a model by estimating model discrimination (eg, c statistic), model calibration (eg, calibration plot, calibration slope), and clinical utility (eg, decision curve analysis)."
- Calibration assessment – "Calibration is best assessed graphically with a plot of the estimated values on the x axis and observed values on the y axis, with a smoothed flexible calibration curve in the individual data."
- Sample size item – "Explain how the study size was arrived at (separately for development and evaluation), and justify that the study size was sufficient to answer the research question."
- Measures item – "Specify all measures and plots used (and their rationale) to evaluate model performance (eg, discrimination, calibration, clinical utility) and, if relevant, to compare multiple models"
- Class imbalance item – "If class imbalance methods were used, state why and how this was done, and any subsequent methods to recalibrate the model or the model predictions"
- Subgroup performance with uncertainty – "Report model performance estimates with confidence intervals, including for any key subgroups (eg, sociodemographic)."
- Fairness item – "Describe any approaches that were used to address model fairness and their rationale"
- Fairness embedded – "TRIPOD+AI has embedded items on fairness throughout"
- Representation is not enough – "representation alone does not guarantee fairness."
- The sample-size items rest on Riley R.D. et al. (Stat Med 2019; BMJ 2020, S303) and the external-validation series Collins G.S. et al. and Riley R.D. et al. (BMJ 2024) – "Calculating the sample size required for developing a clinical prediction model."

## Used in

09-01-validation-success.md (Milestone 5; reused by T07 from the Milestone 4 trail).

## Against reference.md

Confirms Section 9 of the Milestone 5 outline ("Metrics, baselines, split and validation, success criteria"): TRIPOD+AI lists what a prediction-model report must state, including discrimination, calibration and fairness.

## Reliability

Primary; consensus statement by Collins G.S., Moons K.G.M., Dhiman P., Riley R.D., Van Calster B. and 29 other authors (EQUATOR network); BMJ 385:e078378 (2024); open-access copy PMC11019967. Citation traction: 5152 Crossref / 5419 OpenAlex citations as of 2026-11-06. Current version as of November 2026: it is the latest TRIPOD statement and itself supersedes TRIPOD 2015; no later update found.

## Open questions

Health-care guideline: the education analogue of "clinical utility" (staff contact capacity) is the team's translation and needs to be labelled as such in the report.
