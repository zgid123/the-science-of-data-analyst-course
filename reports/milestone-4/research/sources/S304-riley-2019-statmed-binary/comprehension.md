# S304 – Minimum Sample Size for Developing a Multivariable Prediction Model, Part II: Binary and Time-to-Event Outcomes (Riley et al., Statistics in Medicine 2019)

## Summary in my own words

Riley and colleagues replace the "10 events per variable" rule of thumb with sample-size criteria computed from the number of candidate predictor parameters, the outcome proportion and an anticipated Cox–Snell R². The development data must give (i) a global shrinkage factor of at least 0.9, (ii) an optimism of at most 0.05 in Nagelkerke's R², and (iii) a precise estimate of the overall risk. Because the required events per parameter depend on the setting (4.8 in one of their examples, 23 in another), blanket rules should be avoided. Overfitting makes predictions too extreme and apparent performance optimistic.

## Key facts

- Three criteria – "(i) small optimism in predictor effect estimates as defined by a global shrinkage factor of ≥0.9, (ii) small absolute difference of ≤ 0.05 in the model's apparent and adjusted Nagelkerke's R2, and (iii) precise estimation of the overall risk in the population."
- Rules of thumb vary – "Harrell generally recommends at least 15 EPP,15 and others identify situations where at least 20 EPP or up to 50 EPP are required."
- Rules of thumb too simple – "a concern is that any blanket rule of thumb is too simplistic"
- Courvoisier D. S. et al. (2011, Journal of Clinical Epidemiology; not registered) quoted – "There is no single rule based on EPP that would guarantee an accurate estimation of logistic regression parameters."
- Example EPP values (author-reported) – "a new diagnostic model for Chagas disease requires an EPP of at least 4.8 and a new prognostic model for recurrent venous thromboembolism requires an EPP of at least 23."
- Avoid 10 EPP – "This reinforces why rules of thumb (eg, 10 EPP) should be avoided."
- Overfitting consequence – "Overfitting leads to model predictions that are more extreme than they ought to be when applied to new individuals"
- EPP formula – "E = nϕ and EPP = nϕ/p, where ϕ is the overall outcome proportion"
- Harrell F. E. (2015, *Regression Modeling Strategies*, 2nd ed., Springer; not registered) is the source of the 15 EPP recommendation.

## Used in

03-03-predictive.md, 03-01-criteria-matrix.md

## Against reference.md

Confirms the outline's Part 3 "sample size" consideration. Applied to the project, the criteria must be computed on the 2013 training runs with about 44–45% non-completion and the primary predictor set of 20 (the card's handoff), counting parameters (dummy levels, splines), not variables; the computation belongs in the protocol (from the prepared data), not as an assumed result.

## Reliability

Primary; peer-reviewed methods paper by R. D. Riley, K. I. E. Snell, J. Ensor, D. L. Burke, F. E. Harrell Jr, K. G. M. Moons and G. S. Collins, *Statistics in Medicine* 38(7), 1276–1296, doi:10.1002/sim.7992 (open access, read from PMC6519266). OpenAlex cited-by count 1,472 as of 2026-11-06. Current: extended by the BMJ guide (S303); no superseding version.

## Open questions

None.
