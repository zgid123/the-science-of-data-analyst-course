# S205 – A Machine Learning Framework to Identify Students at Risk (Lakkaraju et al., KDD 2015)

## Summary in my own words

Working with two US school districts (about 200,000 students), the authors build an ML framework to identify and prioritise students at risk of not graduating on time and design evaluation metrics with school administrators. The point for this report is that the evaluation was shaped by what educators need, i.e. who to prioritise given limited intervention capacity. Only the abstract was readable.

## Key facts

- Prioritising is the hard part – "identifying and prioritizing students who need those interventions the most remains challenging."
- Educator-centred metrics – "evaluates them using metrics important to school administrators."
- Scale – "two U.S. school districts with a combined enrollment of approximately 200,000 students."
- Co-designed evaluation – "We together designed several evaluation metrics to assess the goodness of machine learning algorithms from an educator's perspective."

## Used in

02-02-technical-tasks.md, 03-04-ranking-capacity.md

## Against reference.md

Confirms the outline's "classification and ranking under capacity" for AQ4: the output form should be a prioritised list judged by educator-facing metrics.

## Reliability

Primary; peer-reviewed KDD 2015 paper (pp. 1909–1918, doi:10.1145/2783258.2788620) by H. Lakkaraju, E. Aguiar, C. Shan, D. Miller, N. Bhanpuri, R. Ghani and K. L. Addison (Data Science for Social Good, University of Chicago). OpenAlex cited-by count 231 as of 2026-11-06. Status partial: abstract only (publisher and typeset.io copies refused). The precision-at-top-k details are taken from the companion paper S206.

## Open questions

Exact metric definitions in the KDD paper not read; S206 covers precision at top k%.
