# S406 – Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure (Roberts et al., Ecography 2017)

## Summary in my own words

The paper reviews and simulates cross-validation on structured data and shows that random k-fold cross-validation, which ignores temporal, spatial, hierarchical (group) or phylogenetic dependence, seriously underestimates the error a model will make on new data. Block cross-validation – splitting by time period, region or group rather than at random – gave the more appropriate estimate in nearly all instances tested when the goal is prediction to new data. The authors recommend blocking wherever a dependence structure exists, even when residuals look independent, while warning that blocks can restrict the predictor ranges seen in training and so induce extrapolation. They suggest each block be its own fold to keep as much training data as possible, which corresponds to leaving one group out.

## Key facts

- Problem – "when performing cross-validation, these structures are regularly ignored, resulting in serious underestimation of predictive error."
- Overfitting to structure – "structured data also provides ample opportunity for overfitting with non-causal predictors."
- Main result – "for all instances tested, block cross-validation is nearly universally more appropriate than random cross-validation if the goal is predicting to new data or predictor space, or for selecting causal predictors."
- Recommendation – "that block cross-validation be used wherever dependence structures exist in a dataset, even if no correlation structure is visible in the fitted model residuals, or if the fitted models account for such correlations."
- Caveat – "may also unwittingly induce extrapolations by restricting the ranges or combinations of predictor variables available for model training, thus overestimating interpolation errors."
- Group structure is one of the four structures – "form groups (herds, flocks, schools, packs) with synchronised activity or movement (hierarchical structure"
- Temporal splits miss conditions – "or in temporal splits, as some periods will not have experienced certain predictor conditions"
- One block per fold – "each block should be its own fold."
- The usual 5–10 folds of Kohavi R. (IJCAI 1995) and Hastie T. et al. (Springer 2009) fit random splitting – "such recommendations are perhaps more appropriate for random splitting where an ad hoc number of folds must be chosen."

## Used in

04-02-validation-strategy.md

## Against reference.md

Confirms the outline's validation bullet "grouped folds inside the training years": OULAD students are nested in module runs (and tutor groups), a hierarchical structure, so folds that leave out whole runs (LORO) follow the paper's advice and "each block should be its own fold". Extends it with a caveat: a left-out run may contain module types or predictor ranges absent from the training runs, so fold errors partly measure extrapolation. No contradiction.

## Reliability

Primary; review with simulations by Roberts D.R., Bahn V., Ciuti S., Boyce M.S., Elith J., Guillera-Arroita G., Hauenstein S., Lahoz-Monfort J.J., Schröder B., Thuiller W., Warton D.I., Wintle B.A., Hartig F., Dormann C.F.; Ecography 40(8):913–929 (2017); author-hosted copy (University of Freiburg). Citation traction: 3883 Crossref / 4074 OpenAlex citations as of 2026-11-06. Current as of November 2026; ecological examples transfer by analogy to students nested in module runs.

## Open questions

The paper's evidence is ecological; no learning-analytics study of grouped versus random folds was fetched for this task.
