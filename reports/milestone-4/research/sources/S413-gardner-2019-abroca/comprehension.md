# S413 – Evaluating the fairness of predictive student models through slicing analysis (Gardner, Brooks & Baker, LAK 2019)

## Summary in my own words

The paper proposes slicing analysis for learning analytics: evaluate a trained model's performance separately for each subgroup of a protected attribute in the test set, rather than only overall. It defines unfairness as differential accuracy between subgroups and measures it with ABROCA, the absolute area between the ROC curves of a baseline group and a comparison group, integrated over all thresholds so that differences in opposite directions cannot cancel out (which a simple AUC difference allows when curves cross). A gender-based slicing analysis of five replicated dropout models over 44 MOOCs and more than four million learners found that ABROCA varied with the algorithm and feature set, with course gender imbalance and curricular area, and showed no strict trade-off between performance and fairness. Slicing analysis is presented as exploratory: it does not by itself correct unfairness.

## Key facts

- Definition of unfairness – "We define this in terms of differential accuracy between subgroups, and measure it using a new metric we term the Absolute Between-ROC Area (ABROCA)."
- Scale (author-reported) – "five different models replicated from other works and a dataset of 44 unique MOOCs and over four million learners."
- Findings – "significant differences in model fairness according to (a) statistical algorithm and (b) feature set used"
- No strict trade-off – "there is not evidence of a strict tradeoff between performance and fairness."
- Aggregate metrics hide effects, quoting Sculley D. et al. (NeurIPS 2015; S203) – "Performance measures such as accuracy or AUC on a full test set may mask important effects"
- Slicing – "to evaluate a predictive model’s performance by"
- AUC difference can cancel – "(3) can substantially underestimate the degree of unfairness in such cases."
- ABROCA – "ABROCA measures the absolute value of the area between the baseline group ROC curve ROCb and those of one or more comparison groups ROCc ."
- Threshold-free – "First, ABROCA is not threshold-dependent."
- Exploratory – "slicing analysis is an exploratory methodology that can be used to understand models or, optionally, to inform model selection."
- Equalized odds of Hardt M. et al. (NeurIPS 2016) is criticised for a single predetermined threshold – "not just a single intervention where the decision threshold is predetermined."

## Used in

04-04-error-fairness.md, 04-01-evaluation-cards.md

## Against reference.md

Confirms the outline's bullet "Error analysis, subgroup and fairness checks": slicing analysis over subgroups is the learning-analytics method for this. Qualifies it: ABROCA summarises differences across all thresholds, while the OULAD action uses one operating point (top 3–5 per tutor group of about 20), so the report should pair ABROCA with subgroup recall and precision at the capacity cut-off. The paper states that ABROCA's range is "practically restricted to the interval [0 .5, 1]", which looks inconsistent with its own definition as an area between two ROC curves (a difference of AUCs that cannot exceed 0.5 in the usual case); the report should not repeat that range.

## Reliability

Primary; peer-reviewed full paper by Gardner J., Brooks C. and Baker R. (University of Michigan; University of Pennsylvania); Proceedings of LAK19, ACM, pp. 225–234, doi:10.1145/3303772.3303791; camera-ready copy on R. Baker's university site (pypdf conversion, special characters garbled, hence partial). Citation traction: 154 Crossref / 207 OpenAlex citations as of 2026-11-06. Current as of November 2026; it remains the reference for ABROCA in learning analytics.

## Open questions

Typographic quotation marks around "slicing analysis" are garbled in the crawl, so short quotes avoid them. Later critiques of ABROCA's sampling variability (e.g. 2023–2024 work) were not fetched – a gap on how to attach uncertainty to ABROCA.
