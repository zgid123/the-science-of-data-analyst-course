## Appendix VI – Interview Method and Requirement Synthesis in Detail

This appendix gives the detail behind Sections 2.2–2.4: how the interviews were prepared and carried out, how the
stakeholders' answers were organised, how the themes were ranked, the requests left outside the scope, the conflicts
between stakeholders, and the full results of the validation round.

### 1. Interview Method

The interviews were prepared and carried out in four steps.

**Step 1: personas grounded in published accounts.** A persona is the role description that the AI follows when it
answers as a stakeholder. To keep the answers close to what real people in these roles report, each persona trait was
taken from a published source. The student persona draws on students who said that a "you are at risk" message could
make them give up [12], on withdrawal surveys in which work, family and health lead the reasons [13], and on
Vietnamese students who keep silent in online classes for fear of losing face [14]. The lecturer persona draws on
tutors who lose students between the second and the fourth assignment [15]. The advisor persona draws on advisor
caseloads of about 300 students each in the United States [16] and on evidence that students answer an advisor they
already know more readily [17]. The program manager persona draws on the regulated withdrawal limits [3], and the data
officer persona on Vietnam's personal data protection law, under which consent is given separately for each purpose
[18]. Details of identity, such as each persona's office, years of service and workload, are scenario
assumptions. So are the capacity figures
that the personas gave, such as three officers for about 4,000 students (AD2, AD3): they are the persona's own
estimates, not published figures.

**Step 2: open questions, written before the interviews.** The team wrote seven or eight open questions for each
stakeholder. Every list covers the five information groups of the brief: business goals (what the stakeholder wants
to improve), success vision (how improvement would be recognised), challenges (what makes the problem hard), decision
making (what the stakeholder would decide with better information) and risk anticipation (what would stop the
stakeholder from trusting or using the results) [1]. To avoid leading the stakeholder, no question names a cause, a
data source or a tool, and none can be answered with a simple yes or no. The words "at risk", "dashboard",
"prediction" and "AI" appear only after the stakeholder has used them. Two draft questions broke these rules and were
rewritten: a lecturer question that proposed "an early-warning dashboard of LMS activity" and a student question that
asked whether "low online activity" caused the student to fall behind. Appendix I lists every question and both
rewrites.

**Step 3: one conversation per stakeholder.** Each conversation began with the role prompt of the brief, which tells
the AI to answer from the stakeholder's perspective, not to write AQs or technical solutions for the
team, and to state clearly when something is an assumption or the stakeholder's own view rather than a verified fact
[1]. The interviewer then asked the prepared questions in order. Where an earlier answer had already covered a
question in full, the interviewer asked a follow-up on the point that answer opened instead. Each interview has one or
two follow-ups, for example the question to the program manager about which staff should act first (PM4) and the
question to the support officer about how many students the office could follow up each week (AD3).

**Step 4: labelled key statements.** After each interview, the team drew out its key statements, 51 in all across the
five interviews, and labelled each one in the three categories of the brief [1]. An opinion is the stakeholder's own
view or preference. An assumption is a figure or fact that the stakeholder gives as an estimate or impression, such as
the size of the support office. Scenario information is a fact given in the brief's scenario, such as the data that
the university holds. Team members checked every quoted statement against its transcript. Appendix II quotes the
statements with their labels.

### 2. Stakeholder Input Organised by Heading

Table A.14 sorts each stakeholder's answers under the five headings of the brief: the goal or need the stakeholder
expressed, the main challenge, the decision the stakeholder needs to take, how the stakeholder would recognise
success, and the risks and constraints the stakeholder raised. The six themes of Section 2.3 were read across its rows.

**Table A.14. Stakeholder input organised by the brief's synthesis headings**

| Stakeholder | Goal or need | Challenge | Decision needed | Success indicator | Risk or constraint |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Program Manager | Know within the semester which courses and groups lose students; real completion, not a better-looking rate (PM1, PM2) | Only end-of-semester and yearly figures; no new resources during a semester (PM5, PM8) | Where to put advisors' and tutors' time during the semester (PM6) | Students supported to complete; a pattern confirmed over several semesters (PM2, PM7) | Students labelled; results without reasons that cannot be defended (PM9, PM10) |
| Course Lecturer | Students who start the course finish it, having done the work (CL2) | Silence noticed only in week 5 or 6; messages to silent students go unanswered; one to one and a half hours a week for this work (CL4, CL5, CL10) | Whom to message before the second or third assignment deadline (CL6) | Every assignment submitted, not only the final one (CL2) | False alarms about students who are fine; results used to judge teaching (CL8, CL9) |
| Support Officer | Reach students before they reach the academic warning list (AD1) | Three officers for about 4,000 students; about 30–40 follow-ups a week (AD2, AD3, VAD7) | Whom to contact first, and with which kind of support (AD4, AD7, AD8) | Contacted students finish their courses, judged with care because those who answer may have finished anyway (AD6) | Lists too long to act on; students feeling watched; judgement must stay with a person (AD9, AD10) |
| Student | The course fits around work and family; some flexibility (ST1, ST5) | Too embarrassed to ask for help; nobody noticed when the student fell behind (ST2, ST4) | Whether to accept help, or pause in time | A practical option, such as an extension, offered early (ST5) | Labels such as "at risk"; effects on grades or records; contact in front of others (ST8, ST9) |
| Data Officer | Link the data the university already holds; agree what each number means (DO1, DO2) | Records matched by hand; about one week of delay; status records that may mix leave with withdrawal (DO3, DO4) | The purpose of data use and the rules of access, agreed by leadership and legal staff (DO7) | Data that staff can check by hand, delivered on an agreed schedule (DO6) | Consent for each purpose; data not clean enough for automated use (DO8, DO9) |

### 3. Priority of the Themes

Table A.15 scores each theme of Table 2.2 against the three criteria of the brief: its link to the organisation's
goal, its effect on decisions and its feasibility.

**Table A.15. Priority of the themes against the brief's three criteria**

| Theme | Link to the organisational goal | Effect on decisions | Feasibility | Priority |
| :---- | :---- | :---- | :---- | :---- |
| T1. Late detection | Direct: completion is the outcome the program reports | Makes decisions within the semester possible | Data already held (DO1) | Core |
| T2. Early start | Direct | Sets when staff can act | Quiz and assignment records are the most reliable LMS data (CL2, DO2) | Core |
| T3. Capacity | Indirect | Sets the length and order of a list | A known limit, with no new budget (PM8) | Core |
| T4. Contact | Indirect | Sets the action for each student | Depends on staff, not on data | Defines the actions of AQ4 |
| T5. Data trust | Enabling condition | A gate before any use | Needs governance decisions (DO7) | Constraint for Section 6 |
| T6. Support only | Enabling condition | Limits how results may be used | A matter of policy | Constraint for Sections 6 and 7 |

### 4. Requests Outside the Scope

Refining the core themes into the problem statement of Section 1.2 also removed the requests that lie outside the
project. Several related matters are outside the scope, each for a stated reason. Assessment rules and course content are
excluded, because a lecturer can change how students are supported during a semester but not what they are assessed
on (CL7). Admissions, enrolment quotas and financial aid are university policies that the program cannot change
within a semester. Students' circumstances outside the course, such as work and family, are outside the university's
control, so the project addresses the university's response to them, such as an extension or a short pause, rather
than the circumstances themselves (ST1, ST5). The evaluation of lecturers is excluded, because lecturers would stop using any result that might
be used to judge their teaching (CL9). Any automated decision about a student is excluded, because the stakeholders
want a person to decide whether and how to contact each student (AD9) and the data office judges that the data are not
yet clean enough for automation (DO9).

### 5. Conflicts between Stakeholders

Table A.16 sets out the three conflicts and the data constraint of Section 2.4, the statements on each side and the resolution the team
adopted.

**Table A.16. Conflicts between stakeholders and the team's resolution**

| Conflict | One side | Other side | Resolution |
| :---- | :---- | :---- | :---- |
| Early contact against false alarms | The program manager and the lecturer want contact in the first weeks, while it can still help (PM3, CL6) | The lecturer, the student and the advisor warn that early lists are less certain, that flagging students who are fine destroys trust, and that students may feel watched (CL8, ST7, AD9) | Two review points, in weeks 3 and 5; a factual reason for each name; a member of staff checks each name before any contact; students are told about the process at the start of the course |
| Who makes contact | The program manager would have the lecturer-advisor or homeroom teacher call first (PM4) | The student prefers the course lecturer or a tutor who knows the course, and the support officer finds that students answer their own lecturer-advisor (ST6, AD5) | Contact comes from someone who knows the student, the lecturer or the student's lecturer-advisor; the support office takes the harder cases |
| Program figures against student-level action | The program manager needs figures by course and group to place staff (PM6) | The advisor and the lecturer need names to contact (AD4, CL6) | Two outputs: course and group patterns for the program manager, and a short contact list for lecturers and advisors |
| Constraint: automation against unready data | An automated list would save staff time, the usual reason for building an early-warning system | The data officer judges that the data are not yet clean enough for anything automated (DO9) | No automated action; data quality is checked in the data audit of Milestone 2 before any model is built |

### 6. Validation Results

Table A.17 gives the full results of the validation round of Section 2.4 under the four headings of the brief.

**Table A.17. Validation results under the brief's four headings**

| Validation content | Result |
| :---- | :---- |
| Points the stakeholders confirmed | A short list in order of urgency, with a factual reason for each name (all five stakeholders); contact by someone who knows the student, in supportive words that never say "at risk"; use for support only, with a person taking the final decision; missed quizzes and assignments as a better early sign than LMS activity (VDO1); the revised SMART Goal (VPM7) |
| Points the stakeholders asked to adjust | Detection is late and patchy rather than absent, because lecturers do sometimes alert the support office (VCL1, VAD1); two review points, in week 3 and week 5, kept away from registration and examination weeks (VCL2, VAD2); completion means passing the course, not merely staying enrolled (VPM6); the target is assessed over the 2027–2028 academic year rather than one semester, against a baseline recounted under Circular 83/2026 (VPM5, VPM8); consent for each purpose, and legal approval before any linking of records (VDO2); the student's family and employer are never told (VST2) |
| Points the stakeholders added | A program-level view of the courses and groups that lose students (VPM3); first-year students as a group of their own (VPM4); a shared record of each contact (VCL4); students who drift in several courses at once as a separate, more urgent case (VAD3); a simple "I'm fine, thanks" reply that closes the contact (VST3); a small pilot with comparison courses, so that a good result cannot come from choosing easy courses (VDO4, VPM9) |
| Points the team did not adopt, with the reason | The advisor's suggestion to drop the completion target (VAD4); the lecturer's definition of completion as having done all the work (CL2); a general email instead of personal contact (VST5). Section 2.4 gives the reason for each |
