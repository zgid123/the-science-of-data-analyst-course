# Playbook: what goes with an outcome

Use when the question is "what is associated with a good or bad outcome?" or "which factors matter, and is it the same in each group?" on observational data: customer attributes and churn, measurements and a quality score, habits and a result.

The answer is a short ranked list of associations a reader can trust, with their size in plain units, and a clear line between "goes with" and "causes". It is not a table of every coefficient.

## Frame it (stages 1–3)

| Decision | Ask | Typical trap |
| --- | --- | --- |
| Outcome | The raw score, or a threshold ("good" = 7 or more)? State it; show that the ranking of factors does not depend on the threshold | A threshold chosen after looking |
| Unit and repeats | One row per what? Are identical rows repeats of one entity or separate entities? | Repeats counted as independent evidence |
| Groups | Which groups must be compared (product line, region, segment)? Analyse each on its own before pooling | A pooled result driven by the larger group |
| Candidate factors | Which fields could a reader act on or observe? Which are consequences of the outcome? | A field recorded after the outcome used as a "driver" |

## Analysis sequence (stage 7)

1. **One factor at a time, in reader units.** For each factor, the outcome across quarters (or categories) of the factor, with counts: "36% of the top alcohol quarter score 7 or more, against 1% of the bottom quarter". Add a rank correlation as a summary, never alone.
2. **Shape.** Look at all quarters, not only top against bottom: a factor whose best outcomes sit in the middle has a near-zero correlation and still matters.
3. **Overlap between factors.** Check which factors move together (correlations among factors, or one factor largely determined by others). Say so, and do not present two overlapping factors as two separate findings.
4. **Like for like.** Compare within levels of the other main factors (`stats_helpers.standardized_rates` for a rate across groups) or fit one simple model with the factors together (linear or logistic), and report raw and adjusted side by side. Only say an association "disappears once adjusted" for an adjustment you actually ran, for factors that were in the model.
5. **Same in each group?** Estimate each group separately with intervals, then the difference between groups with its interval. "The same" needs the measure named: a correlation can be equal while the size per unit differs. With many factors, treat a single group difference among many as tentative.
6. **How much is explained.** One honest number for how far the factors account for the outcome (cross-validated fit or a simple accuracy against the base rate), so the reader knows what is left unexplained. Cross-validation used only to describe fit needs no holdout freeze; a claim about performance on new data does.
7. **Stress tests.** Another threshold for the outcome; repeats counted once against as given; outliers in or out. Report what changed.

## Say it right

- "Goes with", "is associated with", "among wines with more alcohol": yes. "Raises", "improves", "drives", "because of": only with an experiment or an identification strategy.
- Give sizes in the outcome's units and the factor's units, with the population and the counts.
- Rank the factors by size and robustness, and say which ones depend on a single group.

## Charts that work

- Outcome by quarter of a factor, one small panel per factor, the same y axis, one line per group.
- Dot and interval per factor: raw and adjusted, or one group against another.
- A heat map of correlations among the factors, to show overlap.

## Traps checklist

- A factor that is a consequence or a component of the outcome.
- Top-against-bottom contrasts hiding a middle peak.
- Collinear factors reported as separate drivers.
- "Equal in both groups" claimed from one measure only.
- Many comparisons, the largest one reported as a finding without saying how many were made.
- Causal verbs on observational data.
