# S206 – Who, When, and Why: Prioritizing Students at Risk (Aguiar et al., LAK 2015)

## Summary in my own words

The Data Science for Social Good team built early-warning models for one US school district and argues that, because schools can intervene with only a small share of students, models should output a ranked list and be judged by precision at the top k% of risk scores, not by binary predictions. They add urgency models (when a student goes off track) and a teacher-facing interface. Their evaluation used the share of truly at-risk students among the top 10% of scores and grouped risk into tiers (top 10%, next 20%).

## Key facts

- Limited resources – "given limited resources, such programs must focus on the right students, at the right time, and with the right message."
- Binary versus ranked – "they often make binary, rather than continuous or ranked, predictions"
- Precision at top k% – "the precision at top k%, which is the predictive accuracy within the models’ top k% most confident predictions."
- Why that metric – "The choice of this metric reflected the reality that many schools can only intervene on a small percentage of their entire student"
- Risk tiers – "We defined high risk as the top 10% of risk scores, moderate risk as the following 20%"
- Ranked list as output – "The first one is to produce a ranked list that orders students according to their risk of not graduating on time."
- Timing as second output – "The second one is to predict when they’ll go off track, to help schools plan the urgency of the interventions."
- Bowers A. J. et al. (2013, The High School Journal; not registered) review of 36 early-warning indicator studies – "as indicated by Bowers et al.’s recent review of 36 studies on this topic [9]."

## Used in

02-02-technical-tasks.md, 03-04-ranking-capacity.md

## Against reference.md

Confirms the outline's "classification and ranking under capacity (predict)" and "recall at capacity" framing for AQ4. Extends it: the source uses precision at top k% (share of true positives in the contacted list); the outline names "gain over base rate and recall at capacity" — both are capacity-bound metrics and can be reported together (metric choice is T06's).

## Reliability

Primary; peer-reviewed LAK 2015 conference paper (doi:10.1145/2723576.2723619) by E. Aguiar, H. Lakkaraju, N. Bhanpuri, D. Miller, B. Yuhas, K. L. Addison; read from the author-hosted PDF. OpenAlex cited-by count 55 as of 2026-11-06. Secondary-school setting, not distance higher education.

## Open questions

None.
