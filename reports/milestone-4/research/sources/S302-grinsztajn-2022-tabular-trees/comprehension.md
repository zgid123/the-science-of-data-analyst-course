# S302 – Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? (Grinsztajn, Oyallon & Varoquaux, NeurIPS 2022)

## Summary in my own words

The authors benchmark tree ensembles (random forest, gradient-boosted trees, XGBoost) against deep-learning models on 45 tabular datasets of medium size (about 10,000 training samples) and find that tree-based models remain the best, even with extensive hyperparameter search. They trace this to inductive biases: trees handle irregular target functions and uninformative features better. The benchmark deliberately removed datasets on which a default logistic regression came within 5% of the strong models, so it does not compare trees with logistic regression on typical data.

## Key facts

- Main result (author-reported) – "Results show that tree-based models remain state-of-the-art on medium-sized data"
- Benchmark – "We define a standard set of 45 datasets from varied domains with clear characteristics of tabular data"
- Medium-size regime – "We truncate the training set to 10,000 samples for bigger datasets."
- Tree models used – "For tree-based models, we choose 3 state-of-the-art models used by practitioners: Scikit Learn’s RandomForest, GradientBoostingTrees (GBTs)"
- Irregular targets – "NNs struggle to fit these irregular functions compared to tree-based models."
- Logistic-regression-easy datasets removed – "we remove a dataset if a default Logistic Regression (or Linear Regression for regression) reach a score whose relative difference with the score of both a default Resnet (from Gorishniy et al. (2021)) and a default HistGradientBoosting model (from scikit learn) is below 5%."
- Fernández-Delgado M. et al. (2014, JMLR; not registered) cited for trees beating logistic regression – "As tree-based methods have been shown to be superior to Logistic Regression (Fernández-Delgado et al., 2014) in our setting"

## Used in

03-00-candidate-approaches.md, 03-03-predictive.md

## Against reference.md

Confirms the outline's "tree ensembles" (gradient boosting) as the right flexible challenger for tabular OULAD features, rather than deep learning. Qualifies it: the benchmark excluded datasets where logistic regression was close, so it cannot show that trees beat logistic regression on OULAD; the report must not cite it for that.

## Reliability

Primary; peer-reviewed NeurIPS 2022 Datasets and Benchmarks Track paper by L. Grinsztajn, E. Oyallon and G. Varoquaux (Inria, Sorbonne); read from arXiv 2207.08815. Widely cited benchmark. No newer version of the paper; later tabular foundation models (e.g. TabPFN) were not checked and are outside the card.

## Open questions

Newer tabular benchmarks after 2022 not checked.
