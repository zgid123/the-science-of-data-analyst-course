# S200 – To Explain or to Predict? (Shmueli, Statistical Science 2010)

## Summary in my own words

Shmueli separates three purposes of statistical modeling: explanatory (testing causal hypotheses), predictive (predicting new or future observations) and descriptive (summarising associations compactly). She argues that the purpose changes every step of the modeling process, from variable choice to validation and model selection, and that explanatory power does not imply predictive power. The bias–variance decomposition shows why: explanation minimises bias to represent the theory, prediction minimises bias plus estimation variance, so a "wrong" model can predict better. Predictive power must be assessed on holdout or new data, and binary predictions can take the form of classes, probabilities or rankings, each needing its own metric.

## Key facts

- Explanatory modeling defined – "I define explaining as causal explanation and explanatory modeling as the use of statistical models for testing causal explanations."
- Predictive modeling defined – "I define predictive modeling as the process of applying a statistical model or data mining algorithm to data for the purpose of predicting new or future observations."
- Rankings are a form of prediction – "Predictions include point or interval predictions, prediction regions, predictive distributions, or rankings of new observations."
- Descriptive modeling – "This type of modeling is aimed at summarizing or representing the data structure in a compact manner."
- Regression can be descriptive – "Fitting a regression model can be descriptive if it is used for capturing the association between the dependent and independent variables rather than for causal inference or for prediction."
- Explanatory power is not predictive power – "While explanatory power provides information about the strength of an underlying causal relationship, it does not imply its predictive power."
- Bias–variance difference – "In explanatory modeling the focus is on minimizing bias to obtain the most accurate representation of the underlying theory. In contrast, predictive modeling seeks to minimize the combination of bias and estimation variance, occasionally sacrificing theoretical accuracy for improved empirical precision."
- Wrong model may predict better – "model can sometimes predict better than the correct one."
- Overfitting is the main danger in prediction – "In predictive modeling, the biggest danger to generalization is overfitting the training data."
- Output form decides the metric – "These three different types of predictions would warrant different performance metrics."
- Konishi S. & Kitagawa G. (2007, book *Information Criteria and Statistical Modeling*, Springer; not registered) quoted on the gap between true-model estimation and prediction – "an optimal model for prediction purposes may be different from one obtained by estimating the"

## Used in

02-00-aq-task-mapping.md, 02-01-modeling-briefs.md, 02-02-technical-tasks.md

## Against reference.md

Confirms the outline's Part 2 bullet "explain-versus-predict distinction" and "association (explain)" for AQ1–AQ2 versus "classification and ranking under capacity (predict)" for AQ3–AQ4. Extends it: Shmueli reserves "explanatory" for causal explanation and calls association-only regression "descriptive"; since the outline's AQ2 is "association … without causal claim", the report should label AQ2 regression descriptive/associational (or define "explain" as association within module) to stay consistent with the source.

## Reliability

Primary; peer-reviewed article by Galit Shmueli (University of Maryland at the time), *Statistical Science* 25(3), 289–310, doi:10.1214/10-STS330; read from the arXiv version 1101.0891, which is the published text released by the Institute of Mathematical Statistics. A foundational, widely cited paper on the topic. Current: no newer version; the 2010 article remains the reference as of 2026-11-06.

## Open questions

None.
