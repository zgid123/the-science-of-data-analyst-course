# S202 – Rules of Machine Learning: Best Practices for ML Engineering (Zinkevich, Google)

## Summary in my own words

Google's guide (by Martin Zinkevich) sets out 43 rules for building ML products. Its early rules say a product can launch on a simple heuristic first, that metrics come before the model, that ML should replace a heuristic only once the heuristic grows complex, and that the first model should be simple so that the pipeline can be trusted. It recommends interpretable probabilistic models (linear, logistic, Poisson regression) for the first model because their outputs are probabilities that can be checked for calibration, scales model complexity to the amount of data, judges models by how their output is used (a ranking or a cut-off), and tests on data collected after the training period.

## Key facts

- Rule 1 – "Rule #1: Don’t be afraid to launch a product without machine learning."
- Heuristic gets half the gain – "If you think that machine learning will give you a 100% boost, then a heuristic will get you 50% of the way there."
- Rule 3 – "A simple heuristic can get your product out the door. A complex heuristic is unmaintainable."
- Rule 4 – "The first model provides the biggest boost to your product, so it doesn't need to be fancy."
- Rule 14 – "Rule #14: Starting with an interpretable model makes debugging easier."
- Logistic regression outputs probabilities – "Each prediction is interpretable as a probability or an e"
- Rule 21 – "The number of feature weights you can learn in a linear model is roughly proportional to the amount of data you have."
- Rule 25 – "If you are using it to rank documents, then the quality of the final ranking matters more than the prediction itself."
- Rule 33 – "In general, measure performance of a model on the data gathered after the data you trained the model on, as this better reflects what your system will do in production."
- Page currency – "Last updated 2025-08-25 UTC."

## Used in

02-02-technical-tasks.md, 03-00-candidate-approaches.md, 03-01-criteria-matrix.md, 03-04-ranking-capacity.md

## Against reference.md

Confirms the outline's scope rule "Every AQ gets a baseline" and Part 3 "AQ3 and AQ4: rule and simple baselines; regularised logistic regression; tree ensembles", in that order. Rule 25 confirms "ranking under capacity" as the evaluated output for AQ4. Rule 33 supports "train on 2013 runs, test on 2014 runs" (the temporal split belongs to T06's Part 4).

## Reliability

Primary; official Google for Developers guide, author Martin Zinkevich, an industry practice document (not peer reviewed) with wide uptake. Page "Last updated 2025-08-25 UTC" — the current version as of 2026-11-06.

## Open questions

None.
