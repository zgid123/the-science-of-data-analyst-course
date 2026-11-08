# S508 – Inherent Trade-Offs in the Fair Determination of Risk Scores

## Summary in my own words

Kleinberg, Mullainathan and Raghavan formalise three fairness conditions for risk scores, calibration within groups and balance for the positive and negative classes, and prove that no method satisfies all three except when prediction is perfect or base rates are equal; even approximate satisfaction requires approximately those special cases.

## Key facts

- Impossibility theorem – "we prove that except in highly constrained special cases, there is no method that can satisfy these three conditions simultaneously."
- Approximation does not help – "even satisfying all three conditions approximately requires"
- Special cases – "Then the instance must either allow for perfect prediction"
- Balance for the positive class definition – "We could think of this as balance for the positive class,"

## Used in

05-02-causal-fairness-use.md (fairness criteria conflict).

## Against reference.md

The outline line for Part 5 reads "fairness and high-stakes use with human oversight" (reference.md, Part 5). Confirms: with unequal non-completion rates across groups and imperfect prediction, the team cannot have calibrated scores and equal error rates at once.

## Reliability

Primary, peer-reviewed: ITCS 2017 (LIPIcs 67); Cornell and Harvard authors; arXiv copy. OpenAlex cited_by_count 1435 (as of 2026-11-06).

## Open questions

None.
