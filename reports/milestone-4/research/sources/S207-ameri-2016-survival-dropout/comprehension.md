# S207 – Survival Analysis Based Framework for Early Prediction of Student Dropouts (Ameri et al., CIKM 2016)

## Summary in my own words

Ameri and colleagues frame university dropout as time-to-event and fit Cox and time-dependent Cox models on Wayne State University data, so that the model predicts both whether and in which semester a student drops out. They argue that the timing matters because limited resources call for prioritised, proactive interventions. Only the abstract was readable.

## Key facts

- Early dropout risk – "The most vulnerable students are the freshman, who are at the highest risk of dropping out at the beginning of their study."
- Survival framework – "we develop a survival analysis framework for early prediction of student dropout using Cox proportional hazards regression model (Cox)."
- Time-varying covariates – "We also applied time-dependent Cox (TD-Cox), which captures time-varying factors"
- Whether and when – "not only correctly classifying whether a student is going to dropout is important but also when this is going to happen is crucial for a focused intervention."
- Prioritised intervention – "This study enables us to perform proactive interventions in a prioritized manner where limited academic resources are available."

## Used in

02-02-technical-tasks.md, 03-03-predictive.md

## Against reference.md

Confirms the outline's Part 3 "survival framing" as a candidate. Its own accuracy claims are author-reported against their baselines and are not used.

## Reliability

Primary; peer-reviewed CIKM 2016 paper by S. Ameri, M. J. Fard, R. B. Chinnam and C. K. Reddy (Wayne State University), doi:10.1145/2983323.2983351. OpenAlex cited-by count 128 as of 2026-11-06. Status partial: abstract only. Campus university setting.

## Open questions

Full text not read; time-dependent Cox details not needed for a Level 1 proposal.
