# S414 – Student success prediction in MOOCs (Gardner & Brooks, User Modeling and User-Adapted Interaction 2018)

## Summary in my own words

This survey of predictive models of student success in MOOCs identifies three methodological gaps: heavy filtering of the student population, ineffective model evaluation, and the use of data that would not be available when predictions are needed. Most surveyed studies trained and evaluated on the same course after it ended (post hoc), so labels used for training were not knowable during the course; fewer than 10% used architectures that could predict for a course in progress, for example training on an earlier run and predicting a later one. It reports that predicting on future courses generally performs worse than same-course prediction, so same-course results are optimistic. It also criticises inference from averaged cross-validation scores and uncorrected multiple comparisons, and notes that the right metric depends on the intervention: recall for cheap nudges, precision for costly support.

## Key facts

- Gaps – "This survey reveals several key methodological gaps, which include extensive filtering of experimental subpopulations, ineffective student model evaluation, and the use of experimental data which would be unavailable for real-world student success prediction"
- Realistic context – "A realistic context matches the situation in which predictive models would be employed for active use in MOOCs, particularly with respect to the information available at the time of prediction."
- Post hoc architectures – "model evaluation takes place by evaluating test predictions made on the same course used for training – not a disjoint future course."
- Labels unknown in progress – "by definition, a users’ dropout status is not knowable until the course completes."
- Few realistic studies – "fewer than 10% – examine prediction architectures in which the test predictions could be made for an incomplete course"
- Future-course penalty, after Veeramachaneni K. et al. (2014) – "Veeramachaneni et al (2014) find that predicting on future courses generally achieves lower performance than same-course prediction"
- Optimism of post hoc, after Whitehill J. et al. (2017) – "same-course (post hoc) prediction architectures optimistically bias estimates of model performance"
- CV inference – "Utilizing average cross-validated performance with unadjusted statistical tests (such as a paired t-test) makes such research susceptible to both high Type I error rates"
- Tests, after Dietterich T.G. (Neural Computation 1998; S412) and Demšar J. (JMLR 2006) – "are not appropriate or calibrated for testing predictive models"
- Metric depends on intervention – "recall might be an appropriate model evaluation metric; in contrast, when the goal is to provide an expensive or resource-intensive support to predicted dropouts, precision might be a better choice."

## Used in

04-02-validation-strategy.md, 04-03-metrics-success.md, 04-00-evaluation-design.md

## Against reference.md

Confirms the outline's "time split" (train 2013 runs, predict 2014 runs) as the realistic architecture the survey calls for, and its warning that future-run performance is generally lower than same-run performance explains why the 2014 estimate should be the reported one. Extends the metrics bullet: the choice between recall and precision at capacity follows the cost of the intervention. No contradiction.

## Reliability

Primary; peer-reviewed survey by Gardner J. and Brooks C. (University of Michigan); User Modeling and User-Adapted Interaction 28(2):127–203 (2018); arXiv:1711.06349 (v3, April 2018, matching the journal version). Citation traction: 160 Crossref / 229 OpenAlex citations as of 2026-11-06. Current as of November 2026; evidence is from MOOCs, not a distance-learning university such as the OU.

## Open questions

MOOC populations differ from OU registrations (fees, credit), so the size of the future-run penalty may differ for OULAD.
