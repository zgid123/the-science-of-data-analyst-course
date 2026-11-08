# S902 – Fairness in learning analytics: student at-risk prediction in virtual learning environments

## Summary in my own words

Riazy, Simbeck and Schreck (CSEDU 2020) predict course outcomes on OULAD with several classifiers, including fairness-constrained ones, and audit them by gender and declared disability. Gender is balanced in OULAD, while students with declared disability are strongly under-represented. A 5–6 point disparate impact in favour of male students in the data is reproduced and slightly amplified by most models; bias against students with declared disability is reproduced but not consistently amplified, and the behaviour for the under-represented group is erratic. Dropping the sensitive attributes as features cost 1–3 accuracy points (Naive Bayes gained 4) and slightly improved fairness, but disparate impact for disabled students remained for LR and NB. They recommend checking data balance (UEI and NMI measures) before analysis; ABROCA did not detect the disability disparity. Their train/test split was random, not by presentation.

## Key facts

- OULAD scope – "The dataset contains anonymized student data from a virtual learning environment (VLE) for seven courses in"
- Sensitive groups checked – "fairness between genders and students with or without"
- Representation – "the distribution of the genders seems to be balanced, while the students"
- Disability under-representation – "with declared disability are strongly underrepresented"
- Gender bias reproduced – "The disparate impact of 5–6 percentage points in favor of male participants from the training and test set is reproduced and"
- Design with and without sensitive features – "feeding them sensitive information (gender, declared"
- Removing sensitive features does not remove disparity – "disparate impact could still be detected for students"
- Accuracy cost of removal – "There was usually a loss of 1"
- Under-represented groups behave erratically – "bias is sometimes amplified and sometimes"
- Conclusion on disability – "students with declared disabilities were predicted to fail courses with a"
- Pre-analysis balance check – "Two measures are recommended for the prior investigation of learning data, to ensure their balance and fitness"
- Gardner J. et al. (2019, LAK '19; not in sources.md) introduced ABROCA, which missed the disability disparity – "did not detect the disparate impact measured for students"
- Kuzilek J., Hlosta M. & Zdrahal Z. (2017, Scientific Data; S002) published OULAD – "by the Open University (Kuzilek et al., 2017)"
- Random split used – "data were split randomly for each execution of an algorithm"
- Citation traction – "cited_by_count (OpenAlex): 42"

## Used in

09-00-ethics-limitations.md (fairness audit groups and the case for keeping sensitive attributes for auditing; disability under-representation).

## Against reference.md

Confirms the outline's Part 9 "fairness audit use" and "representativeness": on OULAD itself, removing gender and disability from the features did not remove disparities, so the attributes must stay available for auditing. Contrast with the team's design (not a conflict): Riazy used random splits, whereas the team uses a time split (2013 → 2014), so their accuracy figures are not comparable with the team's.

## Reliability

Primary, peer-reviewed conference paper: Proceedings of CSEDU 2020, vol. 1, pp. 15–25, SCITEPRESS, DOI 10.5220/0009324100150025; HTW Berlin. 42 citations in OpenAlex as of 2026-11-06. Cited by Baker and Hawn (S901).

## Open questions

The training-set share is garbled in the PDF text ("training data was chosen to have 20% of the samples and the training data to contain…"); the exact split ratio is unclear. Age band and IMD band were not audited.
