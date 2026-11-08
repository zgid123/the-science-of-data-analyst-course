---
id: S207
url: https://api.openalex.org/works/doi:10.1145/2983323.2983351
requested: 10.1145/2983323.2983351
fetched: 2026-11-06T23:13+07:00
tool: fetch.py (curl + json-metadata; ladder L4)
fetch_prompt: "none (full text conversion, not a model extract)"
status: partial
task: T05
part: 2
raw: raw.json (19 KB)
conversion: json-metadata of https://api.openalex.org/works/doi:10.1145/2983323.2983351 (metadata, 344 words)
---
source: OpenAlex
title: Survival Analysis based Framework for Early Prediction of Student Dropouts
authors: Sattar Ameri; Mahtab Jahanbani Fard; Ratna Babu Chinnam; Chandan K. A. Reddy
institutions: Virginia Tech; Wayne State University
venue: ACM International Conference on Information and Knowledge Management (CIKM)
publication date: 2016-10-24
volume: None
issue: None
pages: 903–912
doi: https://doi.org/10.1145/2983323.2983351
cited_by_count (OpenAlex): 128
type: conference-paper
location: https://dl.acm.org/doi/pdf/10.1145/2983323.2983351?download=true (open access: True)

abstract:
Retention of students at colleges and universities has been a concern among educators for many decades. The consequences of student attrition are significant for students, academic staffs and the universities. Thus, increasing student retention is a long term goal of any academic institution. The most vulnerable students are the freshman, who are at the highest risk of dropping out at the beginning of their study. Therefore, the early identification of {\emph{``at-risk''}} students is a crucial task that needs to be effectively addressed. In this paper, we develop a survival analysis framework for early prediction of student dropout using Cox proportional hazards regression model (Cox). We also applied time-dependent Cox (TD-Cox), which captures time-varying factors and can leverage those information to provide more accurate prediction of student dropout. For this prediction task, our model utilizes different groups of variables such as demographic, family background, financial, high school information, college enrollment and semester-wise credits. The proposed framework has the ability to address the challenge of predicting dropout students as well as the semester that the dropout will occur. This study enables us to perform proactive interventions in a prioritized manner where limited academic resources are available. This is critical in the student retention problem because not only correctly classifying whether a student is going to dropout is important but also when this is going to happen is crucial for a focused intervention. We evaluate our method on real student data collected at Wayne State University. Results show that the proposed Cox-based framework can predict the student dropouts and semester of dropout with high accuracy and precision compared to the other state-of-the-art methods.
