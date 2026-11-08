# S112 – A large-scale implementation of predictive learning analytics in higher education: the teachers' role and perspective (Herodotou et al., ETR&D 2019)

## Summary in my own words

The paper evaluates OU Analyse (OUA), the Open University's predictive learning analytics system, in nine first-year distance-learning courses in 2015–2016 with 59 teachers (Associate Lecturers) and 1,325 students. OUA predicts each week whether a student will fail to submit the next tutor-marked assessment, using demographics and weekly VLE activity, by voting across four models (Naive Bayes, CART and two k-NN models) trained on the previous presentation of the same course; teachers see the predictions in a dashboard and contact students outside it. Binary logistic regression found that teachers' weekly OUA usage, together with students' best previous score, was associated with completion (odds ratio 7.4 per 10% more course weeks with access; Nagelkerke R² .181), and six interviews explored how teachers used the data. The authors are the system's developers, teachers and courses were self-selected, many teachers rarely logged in, and the authors warn against causal interpretation, so the evidence is author-reported and observational.

## Key facts

- Study scale – "a university-wide, multi-methods study with 59 teachers, nine courses, and 1325 students revealed that teachers can positively affect students’ performance when engaged with PLA"
- Prediction target – "The primary objective of OUA is the early identification of students who may fail to submit their next teacher marked assessment (TMA)."
- Overall prediction – "the system also provides information about whether students will complete a course"
- Users – "OUA was designed as a tool that would inform teachers about their students’ behaviour and motivate them towards taking an action when students are at-risk of not submitting their next assignment."
- Broader aim – "The broader objective was to increase students’ retention and completion of their studies."
- Data used – "(a) static data: demographics, such as age, gender, geographic region, previous education, and (b) behavioural data: students’ interactions within the VLE hosting a course"
- Models – "OUA employs three machine learning methods: (1) Naïve Bayes classifier (NB), (2) Classification and regression tree (CART), (3) k-Nearest Neighbours (k-NN)."
- Voting rule – "the result of the prediction is ‘will-not submit next assignment’ if three or all four models give a prediction of ‘will-not submit’"
- Training on legacy data – "predictive models are constructed by machine learning methods from legacy data recorded in the previous presentation of the same course"
- Weekly timing – "OUA algorithms make use of weekly aggregates."
- Prediction quality varies over time – "Precision increases the closer the assignment submission deadline is."
- Contact outside the tool – "Contact with students takes place outside the OUA dashboard, either by emailing, texting, or phoning students."
- Self-selection – "Participating courses were self-selected."
- Teacher self-selection – "Participating teachers (see Table 1) were self-selected with the obvious (self-selecting) biases"
- Low usage – "although teachers had access to OUA they did not access OUA predictions regularly"
- Seven of the 59 teachers never opened the dashboard – "teachers did not access the dashboard at all"
- Method – "binary logistic regression analysis was performed to identify whether teachers’ engagement with PLA through the OUA dashboard significantly predicts pass and completion rates (RQ1)"
- Effect size – "students are 7,4 times more likely to complete the course"
- Weak model fit – "Nagelkerke’s R2 of .181 indicated a moderately weak relationship between prediction and grouping"
- Causal caution – "any causal interpretation of the above findings should be treated with caution"
- Intervention window – "the time window of opportunity to effectively support students at-risk is relatively short (Gasevic et al. 2016; Tempelaar et al. 2015), ranging between 2 and 4 weeks"
- Student consent basis – "Informed consent applies at the point of reservation or registration on to a course or qualification."
- Works cited: Tanes Z., Arnold K. E., King A. S. & Remnet M. A. (Computers & Education 2011), on Course Signals feedback – "summative feedback had no effect on students’ learning"; Kuzilek J. et al. (Learning Analytics Review LAK15-1, 2015), OU Analyse – "OU analyse: Analysing at-risk students at The Open University"; Wolff A. et al. (LAK 2013) – "Improving retention: Predicting at-risk students by analysing clicking behaviour in a virtual learning environment"; Herodotou C. et al. (Journal of Learning Analytics 2019) – "Predictive learning analytics ‘at scale’: Guidelines to successful implementation in higher education".
- Citation traction – "cited_by_count (OpenAlex): 188" (as of 2026-11-02)

## Used in

01-01-motivation-stakeholders.md, 11-05-decision-support.md (Milestone 5; reused by T07 from the Milestone 1 trail).

## Against reference.md

Extends Section 1 ("stakeholders and their needs") and Section 11 ("decision support for D1–D3") of the Milestone 5 outline: at the Open University, the institution behind OULAD, predictions were used by teachers, and use rather than availability drove the benefit.

## Reliability

Primary, author-reported (the authors include the OUA technical lead, Hlosta M.); peer-reviewed journal article in Educational Technology Research and Development 67(5), 1273–1306, open access (CC BY); 188 citations in OpenAlex as of 2026-11-02. Read from the Open Research Online PDF via the Wayback Machine.

## Open questions

The pass-rate model figures (odds ratio for pass) and the precision/recall values in Fig. 1 are images or were not read in full; check before quoting. An independent (non-author) evaluation of OUA was not found.
