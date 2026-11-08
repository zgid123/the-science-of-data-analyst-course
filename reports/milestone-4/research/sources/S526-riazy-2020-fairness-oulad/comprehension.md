# S526 – Riazy, S., Simbeck, K., & Schreck, V. (2020). Fairness in learning analytics: Student at-r

## Summary in my own words

Riazy, Simbeck and Schreck predict course outcomes on OULAD with several classifiers and measure fairness by gender and declared disability. A 5-6 percentage point disparate impact in favour of male students in the data is reproduced and slightly amplified by most models; bias against the under-represented group with declared disability is reproduced but behaves erratically; removing the sensitive attribute usually lowers accuracy.

## Key facts

- Gender disparity reproduced (author-reported) – "impact of 5–6 percentage points in favor of male participants from the training and test set is reproduced and"
- Disability under-represented – "students with declared disability are strongly underrepresented"
- Erratic behaviour for small groups – "are underrepresented in the dataset (in this case: disability), bias is sometimes amplified and sometimes"
- Dropping the attribute costs accuracy – "the models tend to lose accuracy when the sensitive attribute is not used"

## Used in

05-02-causal-fairness-use.md (OULAD-specific fairness evidence).

## Against reference.md

The outline line for Part 5 reads "fairness and high-stakes use with human oversight" (reference.md, Part 5). Extends with OULAD evidence: audit by gender and disability, and expect unstable estimates for the small disability group.

## Reliability

Primary, peer-reviewed conference paper: CSEDU 2020 (HTW Berlin). OpenAlex cited_by_count 42 (as of 2026-11-06).

## Open questions

Their target and cut-offs differ from this project's (non_completion at day 13 and 27), so figures are not transferable.
