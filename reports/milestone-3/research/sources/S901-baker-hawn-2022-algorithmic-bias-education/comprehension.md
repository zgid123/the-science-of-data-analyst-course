# S901 – Algorithmic bias in education

## Summary in my own words

Baker and Hawn (IJAIED 2022) review algorithmic bias in education, defined operationally as model performance that is substantially better or worse across mutually exclusive groups. Bias can arise even when demographics are not model inputs, because proxies for group membership enter as predictors. Their central practical point for this report is that group membership must be recorded to audit a model at all: "if we do not collect data on group membership, we cannot analyze our data sets for algorithmic bias". They recommend collecting extensive demographic data whenever possible, while noting the privacy risk (re-identification in small groups) and that disability data are protected differently across countries. The most-studied groups are race/ethnicity, gender and nationality; less-studied ones include socioeconomic status, disability, urbanicity and age. The crawl holds the published abstract (OpenAlex) and the full EdArXiv preprint (v3.7).

## Key facts

- Operational definition used – "model performance is substantially better or worse across mutually exclusive groups"
- Groups reviewed – "beginning with the most heavily-studied categories of race/ethnicity, gender, and nationality"
- Less-studied groups – "such as socioeconomic status, disability, and military-connected status"
- Bias without demographic inputs, via proxies – "Bias of this nature can also arise even when demographics are not"
- Group data are required to audit – "If we do not collect data on group membership, we cannot analyze our data sets"
- Recommendation – "we recommend that researchers collect extensive"
- Fairness evaluation needs group labels – "It is impossible to evaluate if a model is fair"
- Privacy risk of demographic data – "it may be possible to re-identify a student from their demographic data"
- Disability data protection varies by country – "differing protections on data on student disability status between"
- Biased proxy handling – "it may end up serving as a proxy for a group label"
- Gardner J., Brooks C. & Baker R. (2019, LAK '19; not in sources.md) found MOOC dropout models worse for female students – "studied MOOC dropout prediction and found that several algorithms studied performed worse"
- Riazy S., Simbeck K. & Schreck V. (2020, CSEDU; S902) on OULAD found models over-predicted success for students with disabilities – "algorithms applied to the data generally overpredicted success for students with disabilities"
- Paquette L. et al. (2020, Journal of Educational Data Mining; not in sources.md) found few EDM papers report learner demographics – "does not even mention learner demographics at an"
- Citation traction – "cited_by_count (OpenAlex): 1228"

## Used in

09-00-ethics-limitations.md (why sensitive attributes are kept for the fairness audit; which groups to check; privacy caveat for small groups).

## Against reference.md

Confirms and grounds the outline's Part 9 line "Sensitive variables, representativeness, fairness audit use": keep gender, disability, age band, IMD band and region in the prepared data for auditing even where they are not predictors. Note a nuance against Riazy (S902): Baker and Hawn summarise Riazy's disability finding as over-prediction of success, whereas Riazy's own conclusion says students with declared disabilities were predicted to fail with higher probability; the report should cite Riazy's own words.

## Reliability

Primary (review article, peer-reviewed): International Journal of Artificial Intelligence in Education 32, 1052–1092 (2022), DOI 10.1007/s40593-021-00285-9; Ryan S. Baker and Aaron Hawn, University of Pennsylvania. 1,228 citations in OpenAlex as of 2026-11-06. Body quotes come from the EdArXiv preprint (osf.io/pbmvz), which may differ slightly from the published version.

## Open questions

Gardner et al. (2019) slicing analysis (ABROCA) is not registered; the published IJAIED page numbers of quoted passages are not verified.
