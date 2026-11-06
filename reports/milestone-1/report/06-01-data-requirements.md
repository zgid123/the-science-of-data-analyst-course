## 6.1. Data Requirements per Question

At this milestone the data needs are stated as concepts, and no data are processed [1]. The needs draw on four sources that the university already holds:
the academic management system, the LMS, attendance lists of blended courses and staff rosters. The LMS and the academic records share a student
identifier, but nothing links them automatically, so records are matched by hand (DO1); attendance lists are kept by
lecturers and must also be matched by hand. Appendix IX describes what each source holds.

One source does not exist yet: the contact record defined in Section 3.3, which AQ4 and both secondary KPIs need.

Table 6.1 lists, for each question, the data it needs, their possible source, their granularity and time window,
their availability and a note on privacy. Availability reflects the data officer's account and remains an assumption
until the data audit of Milestone 2.

**Table 6.1. Preliminary data requirements**

| AQ | Data and variables needed | Possible source | Granularity and time | Availability | Privacy and ethics note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| AQ1 | Enrolment, final result, student status, course, delivery mode, year of study; due and submission dates of assessed tasks | Academic management system; LMS | One row per enrolment per semester; 2024–2025 and 2025–2026 | Held; status may mix leave and transfers with withdrawal (DO3) | The program sees groups, not names |
| AQ2 | AQ1 data, plus missed and late tasks, LMS activity relative to the course average, tasks missed across courses, and attendance in blended courses, for weeks 1–4 | LMS; attendance lists | One row per enrolment per week | Held in separate systems and matched by hand (DO1) | No sensitive personal categories, such as health or ethnicity, are used |
| AQ3 | AQ2 data recorded by the end of week 2 and by the end of week 4; outcome at the end of the semester | Same as AQ2 | One row per enrolment at each data cut-off | Available with about one week of delay (DO4) | Seen only by the staff who act on it; no automated decision |
| AQ4 | AQ3 output; weekly capacity of each office; contact record (who, when, how, result) | AQ3; staff rosters; a new shared contact record | One row per student per review point | The contact record does not exist yet (VCL4, VAD1) | Used for support only; family and employers are never told (VST2) |

Where the university's own records cannot be used in time, Milestone 2 may test the approach on an open dataset. The
Open University Learning Analytics Dataset is one possible source: it covers 22 course presentations and 32,593
student records of a distance-learning university in the United Kingdom, with their assessment results and daily summaries of
their activity in the virtual learning environment [21]. Its assessment dates, activity records, final results and
withdrawal dates could support AQ1–AQ3, whereas the routing of AQ4 and both secondary KPIs need the university's own
contact record. Its fit, and the limits of transferring results from it to a Vietnamese university, are assessed in
Milestone 2.
