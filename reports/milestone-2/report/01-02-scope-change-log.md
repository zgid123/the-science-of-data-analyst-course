## 1.2. Scope of Milestone 2 and Change Log Summary

**What this milestone does.** Building on the frozen baseline, this milestone answers the two questions that the brief
sets: which data the four questions need, and whether the open dataset that the team collects actually provides them
[1]. Its work follows the brief's steps. Section 2 turns each question into a data requirement. Section 3 describes
the search for candidate open datasets, and Section 4 scores the candidates and selects one. Section 5 records how the
selected dataset was collected so that anyone can collect it again, and Section 6 checks that the collected files can
be read and match their documentation. Section 7 then maps every question to the real files and variables and states
how far each question can be answered. Sections 8 and 9 cover the risks and the use of generative
artificial intelligence (AI). Cleaning the data, filling in missing values, building features and training models are left to
later milestones, as the brief requires [1].

**What the data changed.** The selected dataset, the Open University Learning Analytics Dataset (OULAD), describes
distance-learning modules of a university in the United Kingdom (UK), not the courses of a Vietnamese program, so the
questions cannot be answered on it exactly as the proposal framed them. The team recorded eight controlled revisions,
C01 to C08, each with the old and the new content, the data evidence behind it and its effect on the questions, KPIs
and decisions. Four of them matter most. OULAD stands in for the university's courses in the analysis, while the
university's own records remain the target for the pilot (C01). A semester becomes a module run, one offering of a
module lasting eight to nine months, with time counted in days from the run's start (C02). Comparisons by delivery mode and year of study are dropped,
because OULAD holds neither (C04). The action part of AQ4, the record of contacts and their outcomes, stays a
requirement for the pilot, because no open dataset records it (C08). The other four adjust the KPI denominator to
OULAD's registration window (C03), drop the attendance sign (C05), build the week-3 list from activity alone and adapt the early-sign rule to OULAD's calendar (C06) and
test AQ3 on the 2014 runs of each module (C07). Section 7.2 explains every revision, and Appendix V (Table A.9) gives
the full Change Log.

None of the revisions alters the Business Goal, the SMART Goal or the decisions. They narrow how far each question can
be answered on open data, and they keep the full questions as the target for the university's own records.
