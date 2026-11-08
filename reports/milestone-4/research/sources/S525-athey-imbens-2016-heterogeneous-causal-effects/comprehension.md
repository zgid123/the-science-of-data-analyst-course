# S525 – Recursive Partitioning for Heterogeneous Causal Effects

## Summary in my own words

Athey and Imbens develop causal trees that estimate how treatment effects vary across subgroups, using honest sample splitting. The method works on data with a treatment indicator W and assumes randomisation or unconfoundedness given covariates; the individual causal effect is never observed, the fundamental problem of causal inference. For this report it shows that targeting by expected benefit (uplift) needs data in which the treatment varied.

## Key facts

- Fundamental problem – "the causal effect is not observed for any individual unit"
- Data need a treatment indicator – "Our data consist of the triple"
- Assumption of randomisation or unconfoundedness – "Throughout the paper, we maintain the assumption of randomization conditional on the covariates"
- Holds in a randomised experiment – "is satisfied in a randomized experiment without conditioning on covariates"

## Used in

05-02-causal-fairness-use.md (why ranking by risk is not ranking by benefit).

## Against reference.md

The outline line for Part 5 reads "causal limits and the deferred contact decision" (reference.md, Part 5). Confirms: heterogeneous-effect (uplift) targeting needs observed variation in contact; OULAD has none.

## Reliability

Primary, peer-reviewed: PNAS 113(27), 2016 (Stanford); arXiv HTML copy. OpenAlex cited_by_count 1618 (as of 2026-11-06).

## Open questions

None.
