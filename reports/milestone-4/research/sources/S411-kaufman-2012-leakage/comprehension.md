# S411 – Leakage in data mining: formulation, detection, and avoidance (Kaufman, Rosset & Perlich, KDD 2011; journal version ACM TKDD 2012)

## Summary in my own words

The paper defines leakage as the introduction of information about the target that should not be legitimately available to the model, and documents it in real projects and in competitions such as KDD Cup 2008 and the INFORMS 2010 challenge, where leaked models reached implausible accuracy. It formalises legitimacy and proposes to avoid leakage by tagging every observation with legitimacy tags during collection and then enforcing a learn–predict separation. In the common "no time machine" case, the tags are time-stamps and the separation is a cut in time that divides training from evaluation examples. The authors stress that the modeller should not even be exposed to information beyond the separation point.

## Key facts

- Definition – "leakage is essentially the introduction of information about the data mining target, which should not be legitimately available to mine from."
- Remedy – "it is possible to avoid leakage with a simple specific approach to data management followed by what we call a learnpredict separation"
- Tags – "process of tagging every observation with legitimacy tags during collection and then observing what we call a learn-predict separation."
- Time cut – "Learn-predict separation is implemented by a cut at some point in time that segments training from evaluation examples."
- Self-control – "the modeler has to be careful not to even get exposed to information beyond the separation point, for this we can only prescribe self-control."
- Competitions – "or the INFORMS 2010 Data Mining Challenge, though judiciously organized by capable individuals, suffered from severe leakage."
- Author-reported leaked accuracy – "groups achieved more than 0.9 AUC, with the best model surpassing 0.99 AUC."

## Used in

04-02-validation-strategy.md

## Against reference.md

Confirms the outline's validation bullet "time split ... single use of the test runs, frozen plan": the 2013/2014 cut is a learn–predict separation, and the "self-control" principle supports not looking at the 2014 runs until the plan is frozen. Extends it: each predictor must carry a time-stamp that falls before the day-13 or day-27 cut-off. No contradiction.

## Reliability

Primary; peer-reviewed paper by Kaufman S., Rosset S. and Perlich C. (Tel-Aviv University; media6degrees). The crawl is the KDD 2011 conference version (pages 556–563) hosted on a University of Massachusetts Boston course page; the registered DOI points to the extended journal version (ACM TKDD 6(4), article 15, 2012, with Stitelman O. as fourth author), which is paywalled. Citation traction of the journal version: 819 Crossref / 919 OpenAlex citations as of 2026-11-06. Current as of November 2026.

## Open questions

Quotes come from the 2011 conference version; the 2012 journal version may word them differently.
