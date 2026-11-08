# S602 – Modelling student online behaviour in a virtual learning environment

## Summary in my own words

Hlosta et al. (arXiv 2018, written for LAK '14) describe the Open University setting that OU Analyse builds on and analyse VLE activity with GUHA and Markov chains. They aggregate daily VLE clicks into weekly counts per content type and binary weekly activity flags, and they relate activity in the first weeks to submitting the first tutor-marked assignment (TMA 1). The paper was fetched as a replacement for S601 but does not discuss training on a previous presentation or drift; its value for Milestone 3 is the precedent for weekly VLE features and the first-assessment focus.

## Key facts

- The OU team examined several successive presentations of each module – "We examined a number of subsequent presentations of each module."
- Daily VLE data are summarised by week – "For our analysis we summarise the data by weeks and content types."
- Weekly features used – "click counts aggregated by week and content type,"
- Binary activity flags – "binary flags indicating whether student was active in the VLE and in various content types."
- Modules have five to seven TMAs – "There are several assignments in each module, typically between five and seven."
- Wolff A. & Zdrahal Z. (2012, cited in S602) found decision trees outperform other methods on VLE and assessment data – "decision trees generally outperform the other methods"
- Wolff A. et al. (2013, cited in S602) added demographic data without a significant gain – "this research did not confirm that this data provide a significant increase in performance"
- Interventions are rationed, so targeting matters – "the resources available for the interventions are limited, the interventions have to be carefully planned"

## Used in

06-02-integration-features.md (weekly aggregation of studentVle clicks per activity type as a precedent for pre-cut-off features).

## Against reference.md

Confirms the outline's Part 6 "feature construction" line: weekly aggregation of VLE clicks by content type is the Open University's own feature design. It does not address the split or leakage rules.

## Reliability

Primary: authors are the OU Analyse team (Knowledge Media Institute, The Open University); arXiv preprint 1811.06369 of a LAK '14 contribution, not peer-reviewed in this form. OpenAlex lists 23 citations as of 2026-11-06 (from `fetch.py find`). The cited Wolff (2012, 2013) works are not registered in sources.md.

## Open questions

Does not state how OU Analyse trains its weekly models; S605 covers that.
