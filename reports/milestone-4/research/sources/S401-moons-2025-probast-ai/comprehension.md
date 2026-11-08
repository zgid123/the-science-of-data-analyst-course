# S401 – PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool (Moons et al., BMJ 2025)

## Summary in my own words

PROBAST+AI updates the 2019 PROBAST appraisal tool so that it covers prediction models built with regression or AI/machine learning. It separates the model development phase (judged on quality) from the model evaluation phase (judged on risk of bias in the performance estimate), with four domains and 34 signalling questions. For evaluation design the most useful questions are those in the analysis domain of evaluation: a reasonable sample size, evaluation without class-imbalance correction, evidence that data leakage was avoided when data were split, replication of all development steps inside resampling, and an appropriate performance evaluation covering calibration, discrimination and net benefit. It also defines data leakage and stresses that one model can and should be evaluated several times on data not used in development.

## Key facts

- Structure – "PROBAST+AI includes four domains, 34 signalling questions (16 for model development, 18 for model evaluation), and six applicability items"
- Earlier tool – "PROBAST assesses the risk of bias and applicability using 20 signalling questions across four domains: participants, predictors, outcome, and analysis."
- Leakage definition – "When data from the model development phase are somehow inadvertently included during the model evaluation (testing) phase, typically leading to overly optimistic performance estimates"
- Leakage question – "4.5 If data splitting was done to create training and test datasets, was there evidence that data leakage was avoided?"
- Resampling question – "4.6 If resampling methods were used to evaluate model performance, were all model development steps replicated in the resampling process?"
- Imbalance question – "4.4 If methods to address class imbalance were used, was the evaluation done in a dataset without correction for imbalance?"
- Performance question – "4.7 Was the predictive performance of the model evaluated appropriately—for example, calibration, discrimination, and net benefit?"
- Predictor timing – "2.4 Were the predictors included in the model available at the time the model was intended to be used?"
- Sample size – "4.2 Was there evidence that the sample size was reasonable?"
- Evaluation measures – "overall predictive accuracy (eg, Brier score), model discrimination (eg, C statistic), model calibration (eg, calibration plot, calibration slope), and clinical usefulness (eg, decision curve analysis)"
- Repeated evaluation – "it can and ideally should be evaluated more than once on its predictive performance, in participant data not used for model development."
- Fairness emphasis – "Aspects of fairness and algorithmic bias are embedded throughout the signalling questions of the four domains."
- Harmonised with Collins G.S. et al. (BMJ 2024; S400) – "Consistent with the TRIPOD+AI"

## Used in

04-00-evaluation-design.md, 04-02-validation-strategy.md, 04-03-metrics-success.md

## Against reference.md

Confirms the outline's validation bullet ("time split, grouped folds inside the training years, single use of the test runs, frozen plan"): PROBAST+AI asks for leakage-free splits, full replication of development steps in resampling and evaluation on data not used for development. Confirms the metrics bullet (discrimination, calibration) and extends it with net benefit and the Brier score. No contradiction.

## Reliability

Primary; consensus tool by Moons K.G.M., Damen J.A.A., Kaul T., Hooft L., Navarro C.A., Dhiman P., Riley R.D., Collins G.S., van Smeden M. et al.; BMJ 388:e082505 (2025); open-access copy PMC11931409. Citation traction: 1231 Crossref / 1283 OpenAlex citations as of 2026-11-06. Current version as of November 2026; it supersedes PROBAST-2019.

## Open questions

The full signalling-question explanations sit in supplementary tables 3 and 4, not fetched; the report uses the question wording from the main table only.
