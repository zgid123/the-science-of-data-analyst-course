# S203 – Hidden Technical Debt in Machine Learning Systems (Sculley et al., NeurIPS 2015)

## Summary in my own words

Google engineers argue that ML systems are quick to build but costly to maintain, because the model is a small part of a large system of data dependencies, configuration and glue code. They name ML-specific risks: entanglement (changing anything changes everything), hidden feedback loops where a model influences its own future training data, undeclared consumers, unstable data dependencies and changes in the external world. For a design proposal this argues for adding complexity only where it pays, and for watching feedback once predictions drive interventions.

## Key facts

- Main thesis – "developing and deploying ML systems is relatively fast and cheap, but maintaining them over time is difficult and expensive."
- Small model, large system – "Only a small fraction of real-world ML systems is composed of the ML code"
- CACE – "as the CACE principle: Changing Anything Changes Everything."
- Risk factors – "These include boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, changes in the external world"
- Direct feedback loop – "A model may directly influence the selection of its own future training data."

## Used in

02-02-technical-tasks.md, 03-01-criteria-matrix.md

## Against reference.md

Extends the outline's criterion "complexity vs baseline" (scope rules) with the maintenance-cost argument. The feedback-loop point is relevant to Part 5 (outreach changes the outcome that later models learn from); noted for T07, not used in Parts 2–3 beyond one sentence.

## Reliability

Primary; peer-reviewed NeurIPS 2015 paper (Advances in Neural Information Processing Systems 28) by D. Sculley and colleagues at Google; read from the official proceedings PDF. One of the most cited ML-engineering papers. No newer version as of 2026-11-06.

## Open questions

None.
