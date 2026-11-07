## 1.2. Scope of Milestone 2 and Change Log Summary

**What this milestone does.** Building on the frozen baseline, this milestone answers the two questions that the brief
sets: which data the four questions need, and whether the open dataset that the team collects actually provides them
[1]. Its work follows the brief's steps. Section 2 turns each question into a data requirement. Section 3 describes
the search for candidate open datasets, and Section 4 scores the candidates and selects one. Section 5 records how the
selected dataset was collected so that anyone can collect it again, and Section 6 checks that the collected files can
be read and match their documentation. Section 7 then maps every question to the real files and variables and states
how far each question can be answered. Sections 8 and 9 cover the risks and the use of generative artificial
intelligence (AI). Cleaning the data, filling in missing values, building features and training models are left to
later milestones, as the brief requires [1].

**What the data changed.** The selected dataset, the Open University Learning Analytics Dataset (OULAD), describes
distance-learning modules of a university in the United Kingdom (UK), not the courses of a Vietnamese program, so the
questions cannot be answered on it exactly as the proposal framed them. The team recorded eight controlled revisions,
C01 to C08, each with the old and the new content, the data evidence behind it and its effect on the questions, KPIs
and decisions (Appendix V). Table 1.2 summarises them; Sections 6 and 7 give the evidence.

**Table 1.2. Summary of the controlled revisions**

| ID | What changes | Why |
| :---- | :---- | :---- |
| C01 | OULAD stands in for the university's courses in the analysis; the university's own records remain the target for the pilot | No open dataset of Vietnamese courses exists, and OULAD is the only candidate that passes the must-have requirements |
| C02 | A semester becomes a module run of about nine months, with time counted in days from the run's start | OULAD dates are days from the start of each run, and runs last 234–269 days |
| C03 | The KPI denominator becomes the enrolments still registered on day 14 | Registration closes two weeks after the start; OULAD cannot separate leave or transfer from withdrawal |
| C04 | Comparisons by delivery mode and year of study are dropped; the fairness check uses deprivation band and disability instead | OULAD has no delivery-mode or year-of-study field |
| C05 | The attendance sign of AQ2 is dropped | OULAD records no in-class sessions |
| C06 | The week-3 list uses activity only; task-based signs start with the week-5 list | A task is due by the end of week 2 in only 1 of 22 runs |
| C07 | AQ3 trains on 2013 runs and tests on 2014 runs of the same module and start month | Each module has at most one earlier and one later run of the same start month |
| C08 | The action part of AQ4 stays a requirement for the pilot; AQ4 is limited to a ranking | No candidate records contacts, staff capacity or interventions |

None of the revisions alters the Business Goal, the SMART Goal or the decisions. They narrow how far each question can
be answered on open data, and they keep the full questions as the target for the university's own records.
