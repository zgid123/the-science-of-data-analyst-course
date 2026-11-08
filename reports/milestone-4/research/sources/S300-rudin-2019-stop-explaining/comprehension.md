# S300 – Stop Explaining Black Box ML Models for High Stakes Decisions (Rudin, Nature Machine Intelligence 2019)

## Summary in my own words

Rudin argues that for high-stakes decisions one should build inherently interpretable models rather than explain black boxes after the fact, because post-hoc explanations are approximations that can mislead. She calls the accuracy–interpretability trade-off a myth for structured data with meaningful features, where simple classifiers such as logistic regression or decision lists usually perform about as well as boosted trees or neural networks after preprocessing. She also notes that high-stakes decisions combine the risk score with information outside the database, which a transparent model makes easier. Her example is COMPAS, matched in accuracy by a three-rule model.

## Key facts

- Thesis – "trying to explain black box models, rather than creating models that are interpretable in the first place, is likely to perpetuate bad practices and can potentially cause catastrophic harm to society."
- Trade-off myth – "(i) It is a myth that there is necessarily a trade-off between accuracy and interpretability."
- Structured data – "When considering problems that have structured data with meaningful features, there is often no significant difference in performance between more complex classifiers (deep neural networks, boosted decision trees, random forests) and much simpler classifiers (logistic regression, decision lists) after preprocessing."
- Standard process – "there tends to be little difference between algorithms, assuming that the data scientist follows a standard process for knowledge discovery"
- Outside information – "In high stakes decisions, there are often considerations outside the database that need to be combined with a risk calculation."
- COMPAS example – "The COMPAS model is equally accurate for recidivism prediction as the very simple three rule interpretable machine learning model involving only age and number of past crimes"

## Used in

03-00-candidate-approaches.md, 03-01-criteria-matrix.md, 03-03-predictive.md

## Against reference.md

Confirms the outline's Part 3 criterion "interpretability" and supports choosing regularised logistic regression as the primary approach for AQ3–AQ4 when tree ensembles do not beat it on the frozen evaluation. Extends Part 5 "high-stakes use with human oversight": tutors combine the score with what they know about the student.

## Reliability

Primary; peer-reviewed perspective by Cynthia Rudin (Duke University), *Nature Machine Intelligence* 1, 206–215 (2019), doi:10.1038/s42256-019-0048-x; read from arXiv 1811.10154 (author version). OpenAlex cited-by count 11,399 as of 2026-11-06. A position paper: its "often no significant difference" is an argued generalisation, not a meta-analysis; S301 gives the systematic evidence.

## Open questions

None.
