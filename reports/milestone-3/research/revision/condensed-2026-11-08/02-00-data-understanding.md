# 2. Data Understanding

The brief requires the dataset to be described in the terms of the education domain before any profiling or
cleaning, not by column names alone [1]. OULAD records OU courses, called modules, each taught in
runs named by the year and month they start [2]. Assessment takes three forms, tutor-marked assessments (TMA),
computer-marked assessments (CMA) and a final exam [2], and every time field is a count of days from the start of
the run [2]. The seven tables join through the student, the module run, the assessment and the learning resource
[2]. Building on these facts, Section 2.1 sets the population, unit of analysis and keys, Section 2.2 the meaning
of the outcome, time and measures, and Section 2.3 the codes and sensitive attributes. Every statement about the
data rests on a computed check in `data/metadata/understanding.json`, written by `src/01_understand.py`.
