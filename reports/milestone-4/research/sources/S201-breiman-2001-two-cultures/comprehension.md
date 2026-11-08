# S201 – Statistical Modeling: The Two Cultures (Breiman, Statistical Science 2001)

## Summary in my own words

Breiman contrasts a data-modeling culture, which assumes a stochastic model (linear or logistic regression, Cox model) and validates it with goodness-of-fit tests, with an algorithmic-modeling culture, which treats the mechanism as unknown and validates by predictive accuracy on test data. He argues that predictive accuracy on held-out data should be the yardstick when the aim is prediction, and that many different models often reach nearly the same error ("Rashomon"), which makes the interpretation of any single fitted model fragile. He also names the tension between simplicity and accuracy ("Occam"). The paper, with comments by D. R. Cox, B. Efron, B. Hoadley and E. Parzen, is the classic statement of the explain-versus-predict split from the prediction side.

## Key facts

- Two cultures – "There are two cultures in the use of statistical modeling to reach conclusions from data."
- Data-model culture – "The analysis in this culture starts with assuming a stochastic data model for the inside of the black box."
- Algorithmic culture validates by accuracy – "Model validation. Measured by predictive accuracy."
- Criterion – "(d) Predictive accuracy on test sets is the criterion for how good the model is."
- Rashomon and Occam – "Rashomon: the multiplicity of good models;"
- Occam – "Occam: the conflict between simplicity and accuracy;"
- Rashomon effect – "What I call the Rashomon Effect is that there is often a multitude of different descriptions [equations f(x)] in a class of functions giving about the same minimum error rate."

## Used in

02-02-technical-tasks.md, 03-00-candidate-approaches.md

## Against reference.md

Confirms the outline's "explain-versus-predict distinction" (Part 2) and supports judging AQ3–AQ4 candidates by out-of-sample accuracy. Breiman's "Occam" claim (simplicity costs accuracy) is contested for structured data by Rudin 2019 (S300); the report should present both, not Breiman alone.

## Reliability

Primary; peer-reviewed discussion paper by Leo Breiman (UC Berkeley), *Statistical Science* 16(3), 199–231, doi:10.1214/ss/1009213726; read from a full-text copy hosted at Uppsala University (the publisher page gave only metadata). OpenAlex cited-by count 4,842 as of 2026-11-06. Classic, no newer version; its "Occam" view is dated relative to later interpretable-ML work.

## Open questions

The discussants' counterpoints (Cox, Efron) were not read in detail; not needed for the design decision.
