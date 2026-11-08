## 1.1. Motivation and Stakeholders

The late moment of notice described in Section 1 matters because support works only while a student can still catch
up, and because the people who could give that support each see a different part of the picture. The problem is
therefore worth analysing for two reasons: the records that could show the drift early already exist, and several
groups of staff would act on them if they had them in a usable form.

**Who uses the results.** The course brief requires three stakeholders, the Academic Program Manager, the Course
Lecturer and the Academic Advisor or Student Support Officer, and we added the Student and the Learning Technology and
Data Officer, because the project acts on students and depends on the office that holds the data. In our setting the
third role is an officer of the student support office, the faculty office that advises and supports students, while
the academic advisors of student classes (cố vấn học tập) are lecturers, called lecturer-advisors below. Table 1.1
lists each stakeholder with the role in the problem, the need that the project serves and the decision that the
results support; the decisions D1–D3 are classified in Section 2.1.

**Table 1.1. Stakeholders, needs and decisions supported**

| Stakeholder | Role in the problem | Need served by the project | Decision supported |
| :---- | :---- | :---- | :---- |
| Program Manager | Owns the program's completion figures and assigns teaching and support staff | A view, during the semester, of which courses and groups lose students and when | D2: where to place the time of the support office and the lecturer-advisors each semester; with the pilot results, D3 |
| Course Lecturer | Runs a course; the first to see who stops submitting work | A short weekly list of students to contact, with a factual reason for each name | D1: whom to contact at each review point |
| Student Support Officer and lecturer-advisors | Contact and support students, with little time for each | Reach students before the academic warning list, within a fixed weekly capacity | D1: whom to contact first, by whom and with which offer |
| Student | Takes the course; the subject of every data use and every contact | Contact from someone known, with a practical offer, and use of data for support only | Whether to accept help, reduce the study load or pause in time |
| Learning Technology and Data Officer | Holds and links LMS and academic records; applies privacy rules | A lawful, stated purpose before any data are linked, and data clean enough to trust | D3: whether to link data routinely, with university leadership and legal staff |

**How the needs were established.** The needs in Table 1.1 come from interviews and a validation round carried out in
Milestone 1, in which generative AI took both sides of each conversation: an isolated AI persona answered as the
stakeholder and an AI interviewer asked our questions and follow-ups. We verified every transcript and drew 51 key
statements from the interviews, each labelled as an opinion, an assumption or scenario information. These statements
are simulated stakeholder views. They motivate the design of the project, such as the timing of the lists and the
length that staff can follow up, but they are never used as evidence for a finding; every finding in Section 11 rests
on the data or on published work.

**What the stakeholders need.** Six themes recur across the five stakeholders. Three form the core of the project:
late detection (T1), an early start of disengagement, usually signalled by a missed quiz or assignment (T2), and a
small, fixed capacity for follow-up, which calls for a short list with a reason for each name (T3). A fourth theme
supports the design, namely that contact helps when it comes from someone the student knows and offers something
practical (T4). Two themes act as constraints: trust in the data, which requires linked records, correct status and a
lawful purpose (T5), and use for support only, so that results never label students, affect grades or evaluate
lecturers (T6). The capacity behind theme T3 rests on two stakeholder estimates, not on data: the three officers of the
support office can follow up about 30–40 students a week between them, and each lecturer-advisor can contact three to
five students a week from their own classes.

**How the conflicts were settled.** The stakeholders agreed on the problem but differed on early contact against the
risk of false alarms, on who should make contact, and on program figures against names for staff. We settled these
points in four ways. Contact lists reach staff at two review points, week 3 and week 5; each name carries a factual
reason checked by a member of staff; contact comes from the lecturer or the student's lecturer-advisor, with the
support office taking the harder cases; and no step is automated. The validation round confirmed this core and fixed
three further points: completion means passing the course, the review points avoid registration and examination
weeks, and the target is pursued over a full academic year rather than one semester.

**Published practice points the same way.** Early-semester data help to identify and predict students at risk, and
early intervention is the leading recommendation of a review of online retention [S111], which also calls for a
collective effort of several stakeholders [S111]. The Open University, the institution that published the dataset we
analyse, runs a predictive tool, OU Analyse, designed to inform teachers about students at risk of not submitting
their next assignment so that the teachers act [S112]. In a study of 59 teachers, nine courses and 1,325 students,
teachers who engaged with these predictions were associated with better student performance [S112], and the window
for effective support of a student at risk is short, between two and four weeks [S112]. At scale, the tool reached
1,159 teachers and 23,180 students in 231 online courses [S113], with a weekly traffic-light output that marks students
at risk in red, those with a moderate probability of failing in amber and those likely to succeed in green [S113].
Building on this evidence, our project gives the people who already contact students a better-timed list, rather than
a new office or an automated decision, and Section 1.2 sets the scope within which that list is built.
