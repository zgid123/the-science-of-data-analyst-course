# S306 – Ouroboros: Early Identification of At-Risk Students without Models Based on Legacy Data (Hlosta, Zdrahal & Zendulka, LAK 2017)

## Summary in my own words

The OU Analyse team addresses the case where no earlier presentation of a course exists to train a model on, which is how OU predictive models are usually built. They propose a "self-learner" that trains on data generated during the current presentation, using students who have already submitted assessments as proxy labels, which creates imbalanced training and test data. Only the abstract was readable.

## Key facts

- Legacy data is the norm – "The presented method proposes a solution in the absence of data from previous courses, which are usually used for training machine learning models."
- New courses lack it – "This situation typically occurs in new courses."
- Self-learner – "We present the concept of a "self-learner" that builds the machine learning models from the data generated during the current course."
- Imbalance – "The approach utilises information about already submitted assessments, which introduces the problem of imbalanced data for training and testing the classification models."

## Used in

03-03-predictive.md, 02-02-technical-tasks.md

## Against reference.md

Confirms the card handoff "train 2013, test 2014": training on previous presentations is the usual OU practice. Extends it: for a module without a previous run, a within-presentation fallback exists; out of scope for OULAD, where every module has a 2013 run.

## Reliability

Primary; peer-reviewed LAK 2017 paper (pp. 6–15, doi:10.1145/3027385.3027449) by M. Hlosta (Open University, Brno University of Technology), Z. Zdrahal and J. Zendulka — the OULAD/OU Analyse group. OpenAlex cited-by count 122 as of 2026-11-06. Status partial: abstract only (OU repository and CORE refused automated access).

## Open questions

The self-learner's reported comparison with legacy-data models was not readable.
