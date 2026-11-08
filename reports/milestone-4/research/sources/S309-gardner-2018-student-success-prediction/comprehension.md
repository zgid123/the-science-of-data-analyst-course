# S309 – Student Success Prediction in MOOCs (Gardner & Brooks, User Modeling and User-Adapted Interaction 2018)

## Summary in my own words

Gardner and Brooks review the literature on predicting dropout and success in MOOCs, covering features, models and evaluation. On evaluation architecture they find that most studies train and test within the same course after it ends ("a posteriori"), which gives optimistic estimates; models trained on earlier runs and applied to later runs perform somewhat lower but remain useful, and few studies test such transfer. They also note survival models (Cox) as a recurring family and the independence assumptions such models make across time steps.

## Key facts

- Boyer S. & Veeramachaneni K. (2015, AIED; not registered) on transfer – "when developing stopout models for MOOCs for real time use, one must evaluate the performance of the model on successive offerings and report its performance"
- Few studies predict for an incomplete course – "fewer than 10% – examine prediction architectures in which the test predictions could be made for an incomplete course"
- Future courses predicted less well – "Veeramachaneni et al (2014) find that predicting on future courses generally achieves lower performance than same-course prediction"
- Conclusion on transfer – "These works collectively suggest that same-course training and prediction may optimistically bias results, but that accurate prediction on future iterations is possible and that multiple methods for such prediction exist."
- Survival models as a model class – "A second broad class of work utilizes survival models."
- Cox model assumption critique (Wang W. & Chen L. 2016; not registered) – "an assumption which is almost certainly violated"
- Variation across courses – "the substantial variation across courses in the way assignments are used."

## Used in

03-03-predictive.md, 03-00-candidate-approaches.md, 02-02-technical-tasks.md

## Against reference.md

Confirms the card's "train 2013 / test 2014" design for AQ3–AQ4 (prediction on future presentations, the honest architecture). Validation design itself is T06's; here it supports why the model family must be one that is trained on earlier runs. MOOC context, not OU credit-bearing modules: the transfer to OULAD is by analogy.

## Reliability

Primary; peer-reviewed review by J. Gardner and C. Brooks (University of Michigan), *User Modeling and User-Adapted Interaction* 28, 127–203, doi:10.1007/s11257-018-9203-z; read from arXiv 1711.06349. OpenAlex cited-by count 229 as of 2026-11-06. Duplicate note: the same work is also registered by T06 as S414 (registered after S309); both crawls hold the same arXiv text.

## Open questions

None.
