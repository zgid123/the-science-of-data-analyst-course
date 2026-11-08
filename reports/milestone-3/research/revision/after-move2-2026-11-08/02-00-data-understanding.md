# 2. Data Understanding

The brief requires the dataset to be described in the terms of the education domain before any profiling or
cleaning, and not by its column names alone [1]. A few facts about the Open University frame that description. The
OU teaches courses called modules, each taught in runs, which the data call presentations and which are named by the
year and month they start [2]. Assessment takes three forms: tutor-marked assessments (TMA), marked by the student's
tutor; computer-marked assessments (CMA), marked automatically; and a final exam [2]. Every time field in the data is
a count of days from the start of the run, not a calendar date [2]. The seven tables join through four identifiers:
the student, the module run, the assessment and the learning resource on the virtual learning platform [2].

Building on these facts, Section 2.1 sets the population, the unit of analysis and the keys; Section 2.2 the meaning
of the outcome, of time and of the measures; and Section 2.3 the categorical codes and the sensitive attributes.
Every statement about the data in this part rests on a computed check written by the first script of the Prepared
Data Package, `src/01_understand.py`, to `data/metadata/understanding.json`.
