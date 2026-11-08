# S507 – Fair prediction with disparate impact: A study of bias in recidivism prediction instrument

## Summary in my own words

Chouldechova shows that when prevalence differs between groups, a risk score that satisfies predictive parity (equal positive predictive value) cannot also have equal false positive and false negative rates across groups. Using COMPAS recidivism data, she shows the error-rate imbalance persists at any cut-off where predictive parity holds, and that unequal error rates can produce disparate impact.

## Key facts

- Core result – "an instrument that satisfies predictive parity cannot have equal false positive and negative rates across groups when the recidivism prevalence differs across those groups."
- Holds at any cut-off – "error rate imbalance persists—indeed, must persist—for any choice of cutoff at which the score satisfies the predictive parity criterion."
- Predictive parity is equal PPV – "Predictive parity at a given threshold"
- Prevalence definition – "Prevalence, also termed the base rate, is the proportion of individuals who recidivate in a given population."
- Hardt M. et al. (NeurIPS 2016; not registered) introduced equalized odds, linked to error-rate balance – "Error rate balance is also closely connected to the notions of equalized odds and equal opportunity as introduced in the recent work of Hardt et al."

## Used in

05-02-causal-fairness-use.md (fairness criteria conflict).

## Against reference.md

The outline line for Part 5 reads "fairness and high-stakes use with human oversight" (reference.md, Part 5). Confirms the outline's anchor: if non-completion rates differ by group in OULAD (for example by IMD band or disability), the team must choose which criterion to report as primary.

## Reliability

Primary, peer-reviewed: Big Data 5(2), 2017 (Carnegie Mellon University); arXiv copy. OpenAlex cited_by_count 2271 (as of 2026-11-06).

## Open questions

None.
