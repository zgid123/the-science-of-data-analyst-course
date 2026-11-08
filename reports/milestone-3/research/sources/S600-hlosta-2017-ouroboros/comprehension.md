# S600 – Ouroboros: early identification of at-risk students without models based on legacy data

## Summary in my own words

Hlosta, Zdrahal and Zendulka (LAK 2017) address at-risk prediction for Open University courses that have no previous presentation to learn from. The standard approach trains models on data from previous runs of the same course; their "self-learner" instead trains on data generated during the current run, using the assessments students have already submitted as labels. This turns the task into a classification problem with imbalanced training and test data. Only the OpenAlex record and abstract were readable: the ACM page, the CORE copy and the Open Research Online PDF all returned HTTP 403 to fetch.py and WebFetch, so the paper's experiments, prediction weeks and drift argument are not on disk.

## Key facts

- The usual training data are previous presentations of the course – "in the absence of data from previous courses, which are usually used for training machine learning models"
- The missing-legacy case arises mainly for new courses – "This situation typically occurs in new courses."
- Ouroboros trains on the current run – "builds the machine learning models from the data generated during the current course"
- Labels come from already submitted assessments, which makes the classes imbalanced – "which introduces the problem of imbalanced data for training and testing the classification models"
- Citation traction – "cited_by_count (OpenAlex): 122"

## Used in

06-03-split-leakage.md (training on a previous presentation vs the current one; why the team's 2013 → 2014 time split mirrors the OU practice).

## Against reference.md

Extends the outline's Part 6 line "split and leakage rules (Tasks 5–6)" and the scope rule "entity and time split": the OU practice of training on an earlier presentation and predicting the running one is the operational analogue of the team's train 2013 → test 2014 split. The abstract does not state the weekly prediction schedule or a drift argument, so the outline's prediction points (day 13, day 27) are neither confirmed nor contradicted here.

## Reliability

Primary: peer-reviewed full paper, Proceedings of the Seventh International Learning Analytics & Knowledge Conference (LAK '17), ACM, pp. 6–15, DOI 10.1145/3027385.3027449; authors from The Open University (KMi) and Brno University of Technology, the same group that published OULAD (S002). Citation traction: 122 citations in OpenAlex as of 2026-11-06. Only the abstract is on disk (status partial).

## Open questions

The full text (prediction weeks, the comparison with legacy-data models, the stated reasons why legacy data may not transfer) is blocked (HTTP 403 at ACM, CORE 83955564 and oro.open.ac.uk/49731). The team or a reader with ACM access should check the paper's section on legacy-data limitations before the report states any drift reason in its name.
