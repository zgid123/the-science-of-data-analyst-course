## Appendix IX – Technique Families, Data Sources, Privacy Rules and Decision Classification in Detail

This appendix explains the choice of each candidate technique family of Section 5, describes the data sources, the quality risks and the privacy and ethics rules of
Section 6, and gives the full definitions of the three decision classifications used in Section 7.

### 1. Choice of the Technique Families

The descriptive and diagnostic questions use the simplest families that answer them. AQ1 needs counts and rates broken
down by course, mode and year of study, and a comparison of timing between two groups. AQ2 compares the later
non-completion rate of students with and without each sign. Explanatory regression lets us see whether a sign
still differs once other signs are taken into account, for example whether missed tasks matter beyond low LMS
activity. AQ2 reports differences, not causes, because the records are observational: they show what students did,
not why they did it, and the brief warns against causal language without a causal design [1].

The predictive question is judged against a simple rule. In the blended first-year course described in Appendix V,
continuous-assessment results such as quizzes and assignments were the strongest early predictor [8], so a rule that
simply counts missed tasks is a demanding standard. A classification method earns its place only if it reaches more
of the students who later fail or withdraw than the rule does on a list of the same length. Validation is
time-based: the method learns from earlier semesters and is tested on a later one, as it would be used in practice.
Courses that have no earlier semesters can use methods that learn from the current course's own submitted
assessments [20]. Survival analysis, which models the time until an event such as withdrawal, is a candidate for the
withdrawal part of the target.

The prescriptive question turns the AQ3 ordering into a list that staff can act on. Decision rules cut the ordering at
the length that capacity allows, apply the precision and fairness limits, and route each student to the lecturer,
the lecturer-advisor or the support office. What-if analysis shows how the limits change the list, for example how
many more non-completers a list of 40 names would reach than a list of 30. Each name carries its reason as an observed
fact, such as two quizzes missed since week 2, because staff said that a score without a reason would be ignored
(VCL3, PM9).

### 2. Data Sources

The data needs of Table 6.1 draw on four sources. The academic management system, run by the academic affairs office, holds each student's enrolments, final
results, status (enrolled, on leave, transferred, withdrawn) and year of study. The LMS holds course pages, quiz and
assignment records with their due and submission dates, and activity logs of what each student opened and when.
Attendance lists of in-class sessions exist only for blended courses and are kept by lecturers. Staff rosters give the
weekly capacity of lecturer-advisors and the support office. According to the data officer, these sources share a
student identifier, but nothing links them automatically, so records are matched by hand (DO1).

**Quality risks.** Five risks could make the data mislead the analysis, and the project handles each one. Student
status may mix approved leave and transfers with real withdrawal (DO3, VPM2), so the baseline years are recounted under
the definitions of Circular 83/2026 [4], as the program manager asked (VPM8). The same LMS measure means different things in courses built
differently (DO2), so activity is compared within each course and quiz and assignment records are the main source
(VDO1). Activity is not learning, because a student can keep logging in while falling behind (CL3, VST1) [22], so
missed and late tasks are the main signs and a member of staff checks each name. Records are matched by hand with
about one week of delay (DO1, DO4), which the data cut-offs absorb. Small groups give unstable rates and can identify
individual students, so group results are reported only above an agreed minimum size.

Table A.20 sets out the five data quality and feasibility risks of Section 6.2, where each was raised and how the
project handles it.

**Table A.20. Data quality and feasibility risks**

| Risk | Raised by | Handling |
| :---- | :---- | :---- |
| Student status mixes approved leave and transfers with real withdrawal, which distorts the outcome | Data officer and program manager (DO3, VPM2); Circular 83/2026 [4] | Recount the baseline years under the definitions of Circular 83/2026 (VPM8) |
| The same LMS measure means different things in courses built differently | Data officer (DO2) | Compare activity within each course; rely mainly on quiz and assignment records (VDO1) |
| Activity is not learning: a student can keep logging in while falling behind | Lecturer and student (CL3, VST1); published work [22] | Use missed and late tasks as the main signs; a member of staff checks each name |
| Records are matched by hand, with about one week of delay | Data officer (DO1, DO4) | Data of weeks 2 and 4 feed the lists of weeks 3 and 5 (VDO3) |
| Small groups give unstable rates and can identify individual students | Group comparisons in AQ2 and AQ3 | Report group results only above an agreed minimum group size |

### 3. Privacy and Ethics Rules

The privacy and ethics rules of Section 6.2, with the source of each, are as follows.

**Privacy and ethics.** Privacy and ethics set firm limits on the project. Vietnam's Personal Data Protection Law, in
force since 1 January 2026, ties consent to a stated purpose and does not treat silence as consent [18]. The Ministry
of Education and Training requires universities to secure their education databases and to report data breaches
within 72 hours [23]. Codes of practice for learning analytics add rules that the project adopts. The purpose, the
data, who has access and how results are used are explained to staff and students [11]. Students are told at the start
of the course and consulted on how their data are used [22]. Consent is sought before any personal intervention [11].
Access is limited to staff with a legitimate need [11]. The data have an agreed lifespan [22]. Results are never used for grading, for profiling students or for judging lecturers [11].

Two further rules come from the interviews and from published work. Once a university knows that a student is
struggling, it has an obligation to act [22], and the data officer warned that flagging students whom nobody has time
to follow up is worse than not knowing (DO10); a list therefore never exceeds the capacity to follow it up. The
student's family and employer are never told about a contact, as the student asked (VST2). Finally, no real student
data are entered into public AI tools, as the brief requires [1].

### 4. Decision Classifications

The brief asks for three classifications [1], each from an established
framework. The first is the level of the decision. Gorry and Scott Morton [24] draw on Anthony's three levels of
managerial activity: strategic planning decides on the organisation's objectives and the resources used to attain
them; management control ensures that resources are used effectively and efficiently towards those objectives; and
operational control ensures that specific tasks are carried out. These correspond to the brief's strategic, tactical
and operational levels. The second is whether a decision is programmed. Gorry and Scott Morton also draw on Simon, for
whom a decision is programmed to the extent that it is repetitive and routine, with a definite procedure worked out
for it, and non-programmed to the extent that it is novel, unstructured and consequential; the two are ends of a
continuum, not sharp categories [24]. The third is reversibility. Bezos separates one-way doors, decisions that are
consequential and nearly irreversible and must be made slowly, with great deliberation and consultation, from two-way
doors, decisions that can be reversed and can therefore be made quickly [25].
