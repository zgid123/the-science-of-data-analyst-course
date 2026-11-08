# S418 – Application of the hierarchical bootstrap to multi-level data in neuroscience (Saravanan, Berman & Sober, NBDT 2020)

## Summary in my own words

Measurements nested within higher-level units (neurons within animals) are not independent, and tests that treat them as independent inflate the false positive rate: in the authors' simulations the "traditional" method exceeded 45% false positives at a nominal 5%. Averaging within each unit first fixes the error rate but loses power. The hierarchical bootstrap resamples with replacement first at the top level (subjects) and then within each sampled subject, which kept the type I error near the intended bound while retaining more power than summarising. The bootstrap still has assumptions: the metric must obey the law of large numbers, and the resampling scheme must match how the data were generated. The paper notes that the method originated in education research on class size and achievement.

## Key facts

- Non-independence – "the measurements constituting the dataset are not independent, even though the traditional statistical analyses often applied in such cases (e.g., Student’s t-test) treat them as such."
- Inflated error (author-reported simulation) – "traditional statistical tests can result in a false positive rate of over 45%, even if the Type-I error rate is set at 5%."
- Summarising loses power – "this approach greatly reduces the statistical power of the analysis."
- Hierarchical bootstrap works – "The hierarchical bootstrap, when applied sequentially over the levels of the hierarchical structure, keeps the Type-I error rate within the intended bound and retains more statistical power than summarizing methods."
- Procedure – "by resampling with replacement first at the level of subjects followed by neurons within a subject."
- Any metric – "the bootstrap can be used more broadly to measure the uncertainty in any metric of interest as long as it obeys the law of large numbers and scales linearly in the probability space."
- Assumption on scheme – "how one chooses to resample their data defines assumptions that must match the true data distribution in order to provide accurate results."
- Design effect formula, after Kish – "DEFF=σ2(data)σ2(data if independent)=1+ρ*(n¯j−1)"
- Origin in education, citing Goldstein H. (school class size studies) – "was developed to quantify the relationship between school class sizes and achievement"
- Few clusters, citing Huang F.L. (Educational and Psychological Measurement 2018) – "Using cluster bootstrapping to analyze nested data with a few clusters."

## Used in

04-03-metrics-success.md, 04-04-error-fairness.md

## Against reference.md

Extends the outline's "uncertainty" bullet: OULAD students are nested in 13 test runs (and tutor groups), so confidence intervals for recall at capacity, AUC, the model-minus-rule difference and subgroup gaps should come from a bootstrap that resamples runs first and students within runs (a paired bootstrap when both models score the same resampled students). No contradiction; with only 13 test runs the run-level resampling is coarse, which the report must state as a condition.

## Reliability

Primary; peer-reviewed methods article by Saravanan V., Berman G.J. and Sober S.J. (Emory University); Neurons, Behavior, Data analysis, and Theory 3(5) (2020); author manuscript PMC7906290 (also arXiv:2007.07797). Citation count not retrieved (metadata lookup failed) as of 2026-11-06. Current as of November 2026; neuroscience examples transfer by analogy to students nested in module runs.

## Open questions

Behaviour of the bootstrap with only 13 top-level clusters (the 2014 runs) is not studied here; Huang F.L. (2018) on few clusters was not fetched.
