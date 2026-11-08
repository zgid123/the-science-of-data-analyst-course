# S509 – Performative Prediction

## Summary in my own words

Perdomo, Zrnic, Mendler-Dünner and Hardt define performative prediction: when predictions support decisions, the resulting actions change the outcome being predicted, which shows up as distribution shift. Retraining then chases a moving target; the desirable state is a performatively stable model, one that is optimal for the distribution it induces.

## Key facts

- Definition – "When predictions support decisions they may influence the outcome they aim to predict. We call such predictions performative; the prediction influences the target."
- Self-fulfilling prophecy example – "In a self-fulfilling prophecy, the high interest rate further increases the customer's default risk."
- Shows up as distribution shift – "When ignored, performativity can surface as a form of distribution shift."
- Retraining chases a moving target – "Retraining is often considered an undesired — yet necessary — cat and mouse game of chasing a moving target."

## Used in

05-02-causal-fairness-use.md (feedback effects and monitoring after deployment).

## Against reference.md

The outline line for Part 5 reads "causal limits and the deferred contact decision" (reference.md, Part 5). Extends: once tutors contact flagged students, later cohorts' outcomes reflect the contact, so a model retrained on them learns from outcomes it influenced; monitoring must record who was contacted.

## Reliability

Primary, peer-reviewed: ICML 2020 (UC Berkeley); arXiv HTML copy. Citation count not retrieved.

## Open questions

None.
