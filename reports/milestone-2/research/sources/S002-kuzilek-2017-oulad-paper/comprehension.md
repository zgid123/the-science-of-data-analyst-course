# S002 – Open University Learning Analytics dataset (Kuzilek, Hlosta & Zdrahal, Scientific Data 2017)

## Summary in my own words

This data descriptor documents the Open University Learning Analytics Dataset (OULAD): seven Open University (OU) modules taught in 2013 and 2014, 22 module-presentations and 32,593 students, combining demographics, assessment results and daily summaries of clicks in the Virtual Learning Environment (VLE). It explains how modules were selected (more than 500 students, at least two presentations, VLE data, a significant number of failing students), how the data were anonymised (identifiers randomised, dates made relative to the presentation start, k-anonymity with k = 5 over six quasi-identifiers including IMD band and disability), and what each of the seven tables holds. Withdrawal is recorded through the un-registration date and the final_result value. The dataset is released under CC-BY 4.0 and was compared with 2015 data from one module to argue that it still reflects the student population.

## Key facts

- Scale – "The dataset contains the information about 22 courses, 32,593 students, their assessment results, and logs of their interactions with the VLE represented by daily summaries of student clicks (10,655,280 entries)."
- Licence – "The dataset is freely available at https://analyse.kmi.open.ac.uk/open_dataset under a CC-BY 4.0 license."
- Period and content – "the Open University Learning Analytics dataset (OULAD) contains a subset of the OU student data from 2013 and 2014"
- Seven modules – "we selected 7 modules: 4 Science, Technology, Engineering, and Mathematics (STEM) modules and 3 Social Sciences modules"
- Selection rule on failure – "The module has a significant number of failing students."
- Presentation naming – "so that ‘2013J’ means that the presentation started in October 2013"
- B and J presentations differ – "it is recommended to analyse the B and J presentations separately"
- Relative dates – "all temporal information has been expressed in relative terms with respect to the presentation start"
- Identifiers randomised – "all numeric identifiers (i.e., student_id, code_module, etc.) have been reassigned and completely randomised"
- Quasi-identifiers include IMD band and disability – "Index of multiple deprivation band (IMD band)" and "Disability."
- Anonymity level – "The main measure of anonymity we selected was the k-anonymity measure with k set to 5."
- Anonymisation reduced the cohort – "The anonymisation process reduced the number of students to 32,593 and generalised the Age and IMD band attributes."
- Consent and opt-out – "At present, the OU does not provide the possibility to opt-out of data usage for Learning Analytics research."
- Tutor groups – "Students in a module-presentation are organised into study groups of approximately 20 people."
- Withdrawal – "Students who unregistered have Withdrawal as the value of the final_result in the studentInfo table."
- final_result field – "final_result—student’s final result in the module-presentation."
- Assessment pass mark – "The score lower than 40 is interpreted as Fail."
- Missing exam results – "Results of the final exam are usually missing"
- VLE clickstream – "sum_click—the number of times the student interacted with the material."
- VLE table rows – "It consists of 10,655,280 rows with the following columns:"
- Typical length – "The typical length of presentations is 9 months."
- Intended uses – "It enables evaluation of predictive models for predicting student assessment results and final course results"
- Works cited: Prasser F. et al. (AMIA Annual Symposium Proceedings 2014) for the ARX anonymisation tool – "Prasser, F., Kohlmayer, F., Lautenschläger, R. & Kuhn, K. A. Arx-a comprehensive tool for anonymizing biomedical data."; Smith T. et al. (Department for Communities and Local Government 2015) for the IMD – "The English Indices of Deprivation 2015: Technical Report"; Stamper J. et al. (KDD Cup 2010) and Cao L. & Zhang C. (KDD Cup 2015) as the two earlier open datasets – "KDD Cup 2015—Predicting dropouts in MOOC".
- Citation traction – "602 Citations" (Nature page, as of 2026-11-02).

## Used in

01-01-situation-historical-evidence.md, 06-01-data-requirements.md, 06-03-privacy-ethics.md

## Against reference.md

Confirms the outline's use of OULAD as a historical proxy (section 1, [2]). Extends it: the modules were chosen because they had "a significant number of failing students", so OULAD over-represents failure relative to a typical module; a proxy claim must state this scope. The paper itself does not list the four final_result categories (Distinction, Pass, Fail, Withdrawn); those are measured in the local exploration (`datasets/oulad/exploration/results/columns.json`).

## Reliability

Primary; authors at the Knowledge Media Institute, The Open University; peer-reviewed data descriptor in Scientific Data (Nature), open access; 602 citations on the Nature page as of 2026-11-02.

## Open questions

The four final_result categories and their counts must be traced to the exploration results, not to this paper. Table 1 (per-module domain and student counts) is an image and was not captured.
