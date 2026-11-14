# Speech script – 15-slide deck (v3-15)

Speaker notes of the 15 main slides and the closing slide of `N04_Milestone5_Slides-15_EN.pptx`, built by
`build_slides_milestone5_15.py`. Audience: a manager who hears the story of a data analytics team once, without the
reports. The slides carry the key information; these notes carry the full delivery of each slide from end to end: the
point, a walk through every element on the slide (visual, cards, table rows, key and footnotes) with the numbers it
shows, the reasoning that links them, and the hand-over to the next slide. Each note is split into paragraphs, one
step of the delivery each; a blank line here becomes a paragraph break in the deck's notes. Each heading names the
full-deck plan slide it reuses (`[plan n]`); plan 95 is the new slide "What Changed Along the Way". At 125 words a
minute the notes run to about 43 minutes.

## Slide 1 – Early Identification of Disengaging Students in Online Courses [plan 1]

**Speaker notes:**

Thank you for your time. We are team N04 of the course MTH045, The Science of Data Analytics, and this is our final project report: early identification of disengaging students in online courses. In the next half hour we tell the story of one data analytics project, from the business question to the last result, including the turns it took.

The project is about one kind of student. Picture a student in week five of an online course. She has not failed anything and has not withdrawn, so on paper she is fine. But she has stopped opening the course, and by the time her name reaches anyone, the weeks in which help still works are gone. Our aim was to find such students early enough for staff to act, with a factual reason beside each name.

The talk follows the analytics lifecycle over our five milestones, the five delivery stages of the course project: the problem and its questions in Milestone 1, the data in Milestone 2, its preparation in Milestone 3, the method in Milestone 4 and the evidence in Milestone 5. On each slide you will see the result; where the plan changed, we say so, and one slide near the end collects every turn. The detail behind each slide sits in the appendix of this deck, and the grey line at the top right of a slide names the appendix slides to look at. Let us start with why timing is the problem.

**Sources:** Milestone 5 report, Sections 1 and 2.

## Slide 2 – Noticed Too Late [plan 3]

**Speaker notes:**

The headline of this slide: staff notice a student who has stopped taking part only after the early weeks, when help is easiest.

The timeline runs from week 1 to the end of the semester and beyond. The orange band covers weeks 1 to 4, the early weeks when help is easiest. That band is not our guess: a published study of predictive learning analytics at the Open University, by Herodotou and colleagues in 2019, finds the window for effective support of a student at risk short, two to four weeks, and published work places the useful moment for support in the first weeks of a course, so the band starts at week 1. The three grey markers show when each group of staff notices a student who has stopped taking part. Lecturers become sure around week five or six. The support office meets the student only when the name reaches the academic warning list, at the end of the semester. The program manager sees counts after the semester. Every marker falls after the band.

The three cards below give the setting and the opportunity. Setting: a Vietnamese university is expanding online and blended learning on its learning management system, the LMS, and one program has about 1,200 students; the university is a case scenario set by the brief of our course, MTH045, so the figure of 1,200 students is an assumption too. Disengagement: a student misses a task, opens the course less often and falls silent before a fail or a withdrawal is recorded, and the records show these traces weeks before any final result. The gap: every moment of notice falls after the early weeks, so by the time anyone acts the student has been drifting for weeks, and help comes when it is hardest to give.

One honest point on the basis line at the foot of the slide: the moments when staff notice come from interviews in which generative AI played the stakeholders. They shape our requirements, but they still need confirming with real staff. The traces in the records are the opportunity; next, what the university wants to achieve with them.

**Sources:** Milestone 5 report, Sections 1 and 1.1; Appendix I.

## Slide 3 – Business Goal and SMART Goal [plan 12]

**Speaker notes:**

We started from the business, not from a model. The lead line says it: the goal is more students passing their courses, not a model or a dashboard, and the SMART Goal makes it measurable with assumed values.

The top box is the Business Goal: improve successful course completion in the program's online and blended courses by identifying students who stop taking part early enough to support them within the semester. Beneath it is the reminder we kept throughout: this is an outcome for the organisation, and a model, a list or a dashboard is only a means to it.

The second box turns it into a SMART Goal, that is specific, measurable, achievable, relevant and time-bound: raise the course completion rate of students enrolled after the add-drop period in the pilot courses from their recounted baseline, assumed 70 percent, by five percentage points, to an assumed 75 percent, by the end of the 2027–2028 academic year. Counting only students enrolled after the add-drop period keeps out those who leave during that period, the first two weeks, while students may still register for or drop a course.

The pilot design says how the goal will be read. About four pilot courses with about 600 enrolments are fixed in advance and compared with similar courses outside the pilot. The baseline is the completion of the same courses in 2024–2025 and 2025–2026, recounted under Circular 83/2026, the new national rule for counting withdrawals, so that approved leave and transfers do not count. The orange tile shows 70 to 75 percent and is marked Assumed, because the case university gives no real completion rate; the university's recount replaces both numbers. At the assumed 70 percent baseline, about 180 of the 600 enrolments would not complete, by failing or withdrawing; five points means about 30 more passes, roughly one in six of those 180, a load that fits the weekly capacity staff reported (Appendix A10).

The grey card states the limit we keep for the whole talk: students who are contacted may have passed anyway, so a rise in completion shows progress, not why. Whether contact itself helps is tested only in the randomised pilot. To reach the goal, we first needed questions the data could answer.

**Sources:** Milestone 5 report, Sections 2 and 2.1, Table 2.1.

## Slide 4 – Four Questions, Four Analytics Levels [plan 16]

**Speaker notes:**

This slide turns the goal into four analytical questions, one per level of analysis, and the lead line gives the rule behind the staircase: each answer may claim only what its level allows.

The line above the cards fixes the vocabulary. Every question is about the same unit: one student's enrolment in one module run: a module is a course in the dataset we use, and a run is one offering of a module. AQ stands for analytical question. And the questions serve three decisions: D1, whom to contact; D2, where to place support time; D3, whether to extend the approach.

Read the cards from left to right. AQ1 is descriptive: what share pass, fail or withdraw, and in which week non-completers first miss a task. It serves D2 and D3 and reads as what happened. AQ2 is diagnostic: which signs by week 4 go with later non-completion, comparing students within the same module run. It serves D2 and gives the reasons for D1, and it reads as an association, never a cause.

AQ3 is predictive: how well data up to day 13 or day 27, the end of week 2 or week 4, estimate non-completion, against the early-sign rule, which flags a missed or late task or a week with no activity (Slide 7). It serves D1 and reads as a forecast, valid only on data the model never saw. AQ4 is prescriptive: who ranks first on a list as long as staff can contact, overall and by student group, so that fairness can be checked. It also serves D1, and because it comes from observational data it reads only as an option to test.

The status at the foot of each card is the outcome at the end of the project: AQ1, AQ2 and AQ3 were run on the data; AQ4 is answered for its ranking, while its contact part has no data. The key also fixes the two data cut-offs, day 13 for the week-3 list and day 27 for the week-5 list, and repeats the early-sign rule, which Slide 7 builds. First, the data.

**Sources:** Milestone 5 report, Sections 3 and 3.2, Tables 3.1 and 3.2.

## Slide 5 – Seven Candidates Screened [plan 24]

**Speaker notes:**

The lead line gives the result of the data search: of seven public candidates, only OULAD passes every gate, so we chose it for fit, not for ease.

We wrote the data requirements before searching, so that the choice could not bend toward a convenient dataset. The line above the table states them. Six must-have gates decide first: a dated outcome, dated tasks, dated activity, at least three runs in time order, an open licence and an anonymised student ID. Only then do ten criteria score each candidate from 0 to 2, so 20 at most.

The table lists the seven candidates with their score, the gates they fail and the decision. The three named UCI come from the University of California, Irvine, repository, and the number beside each is its number in that repository: 697 on dropout, 320 on school pupils and 856 a single survey. XuetangX and HarvardX are massive open online courses, and the last is xAPI-Edu-Data. Read the red cells: every candidate but one fails the dated-outcome gate, because it holds grades or totals but no date at which a student withdrew, and without that date no early list can be tested. Their scores run from 4 to 10, and all six are rejected.

The orange row is OULAD, the Open University Learning Analytics Dataset: about 32,600 enrolments in 22 runs of seven distance-learning modules in 2013 and 2014, and the only candidate that records a dated withdrawal, dated submissions and daily clicks. Its score is only 12 of 20, because scores count only what the documentation states. So we chose it on three conditions its files had to confirm: pass and fail are told apart, each module has enough runs, and one student keeps one ID. The files confirmed all three (Appendix A20). Once the data were in, however, the files showed problems their documentation did not mention.

**Sources:** Milestone 5 report, Sections 4 and 4.1, Tables 4.1 and 4.2; Appendix IV.

## Slide 6 – Three Quality Issues That Change the Method [plan 35]

**Speaker notes:**

The lead line: of nineteen logged quality issues, three are serious enough to change the method.

We profiled all 10.9 million rows of the seven tables and logged nineteen issues, each rated against the four questions. The line at the top gives the scale. High means that ignoring the issue would change a rate, the target, which is the outcome we predict, or a feature, an input we compute for each enrolment. Medium means it shifts a number by an amount we can measure, and Low covers the rest. The diagram pairs each High issue, on the left, with the change in method it forced, on the right.

First, 18 of 24 exams have no result rows. Counting exams would make every student of those modules appear to miss one, so in this project a task means only a TMA, a tutor-marked assignment, or a CMA, a computer-marked assessment, which is a quiz.

Second, the orange row: few tasks fall due by the cut-offs. No 2013 run has a task due by day 13, and 7 of 9 have one due by day 27. A rule built on tasks alone would stay silent in the weeks when a list is needed, so the early-sign rule needs an activity part, a week with no click. This issue reshapes the rule on the next slide.

Third, the data are seven UK modules of 2013 and 2014. We state that scope with every result, and we compare students only within a module, never across modules that differ in design.

The card at the bottom covers the Medium and Low issues, and nothing is deleted or imputed: duplicate click rows are kept and tested against a copy without them, activity after unregistration, the day a student withdraws, is cut at that day, missing values are flagged or grouped as "Missing", and outliers are kept as recorded. For example, 7.4 percent of the click rows are exact duplicates, and removing them leaves the comparison of early clicks between students who complete and those who do not practically unchanged. Now the rule that the orange issue forced.

**Sources:** Milestone 5 report, Sections 6 and 6.1, Table 6.2; Appendix VI.

## Slide 7 – The Early-sign Rule [plan 40]

**Speaker notes:**

This is one of the clearest turns in the project, and the lead line gives the reason: few tasks fall due in the first weeks, so the early-sign rule also counts a week without activity.

On the left is the rule Milestone 1 planned: two or more assessed tasks missed or late by week 4. The big number shows why it could not work: only 1 of the 22 runs has two or more tasks due by day 27. The line below adds the detail: one or more tasks fall due by day 27 in 16 of 22 runs, and by day 13 in only 1, and no 2013 run has a task due by day 13. So the planned rule would stay silent almost everywhere, exactly when a list is needed.

On the right is the final early-sign rule. By the data cut-off, a student is flagged for any one of three parts. Missed task: a TMA or CMA due by the cut-off and not submitted. Late TMA: a tutor-marked assignment submitted late. Late CMAs are left out: almost half of all CMA submissions are late, and counting them would raise the share flagged at day 27 from 28.8 to 41.2 percent. And, in orange, no click in the last 7 days: no platform activity in the seven days before the cut-off. The orange part is the one the data forced on us. As the key says, the cut-off is day 13 for the week-3 list and day 27 for the week-5 list.

The cards at the bottom complete the picture. One rule serves both the analysis on OULAD and the later pilot, so what we test is what staff would use. AQ2, the diagnostic question, tests these three parts and two more activity signs: activity below the run median, that is in the less active half of its run, and no click before the start. And the reach: the rule flags 20.2 percent of 28,069 enrolments at day 13 and 28.8 percent of 27,535 enrolments at day 27.

This rule is also the benchmark any model has to beat. A rule, and a model, can only be tested properly if they see no future data, which is the next slide.

**Sources:** Milestone 5 report, Section 7, Tables 7.1 and 7.2; Appendix VII.

## Slide 8 – Leakage Control [plan 45]

**Speaker notes:**

The lead line: leakage, using information that would not yet exist when the list is made, is blocked in four ways, and a test shows the date check catches it. A list made in week three may use only what is known in week three; later information makes a model look far better than it can be in practice.

The timeline runs from day 0, the module start, to the data cut-off at day 27; the same rule holds at day 13. The grey events before the cut-off, registration, clicks up to day 27 and tasks due by day 27, may feed a feature, an input per enrolment. The red crosses after it, later clicks, the withdrawal day and the final result, never enter.

The table lists the four forms of leakage, the case each takes in OULAD and our control. Two terms first: the training set is the data used to build the model, the 2013 runs, and the test set is the data held apart to score it, the 2014 runs. Target leakage: the final result, the withdrawal day, later activity and TMA marks would reveal the outcome, so features come only from events dated up to the cut-off. Train–test contamination: medians and the values that put inputs on one scale, computed with 2014 included, would let the test year's own values shape the model's inputs, so they are learned on the 2013 training runs only. Student leakage: 1,586 test enrolments at day 27 belong to students already seen in 2013, so the test and training data share some students; they stay in, as returning students would in real use on a later run, and without them the model's gain over the rule still holds. Temporal leakage: a random split would mix the two years, so we train on 9 runs of 2013 and test on 13 runs of 2014.

This is also where generative AI helped most, as a critic: an AI leakage audit of our preparation code found eight errors that our own checks had passed, including a check that always passed and so could catch nothing. We fixed each one.

The green box shows that the date check works. As a test, we switched the date filter off on purpose: exactly the enrolments with clicks after the cut-off changed, and no others, 26,755 of 28,069 at day 13 and 25,663 of 27,535 at day 27. Most enrolments have later clicks, so most changed; what matters is that no other record did, so a real leak would not go unseen. Next, how to judge a list.

**Sources:** Milestone 5 report, Sections 7.1 and 13; Appendix VII.

## Slide 9 – Judging a List by Capacity [plan 52]

**Speaker notes:**

Before running any model, we fixed how a list would be judged, and the lead line states the rule: a list is judged by how many later non-completers it reaches against the most a list of its length could reach.

The length of a list is set by how many students staff can contact, not by a probability threshold. The first card on the right fixes that capacity, k: 3 or 5 contacts per 20 students, that is 15 or 25 percent of a run. The main operating point is 5 per 20 at day 27.

The worked example on the left is an illustration, not data. There are twenty students; the orange figures are the nine who will not complete, and the navy box is a list of five. Four of the nine are on the list, so recall, the share of a run's non-completers who are on its list, is 4 of 9. But a list of five can hold at most five non-completers, so normalised recall divides by that ceiling: 4 of 5, where 1 would be the best list possible. Across the training runs this ceiling is 46 to 100 percent of a run's non-completers, which is why we normalise.

This replaced the Milestone 1 target of a precision of at least 50 percent. Precision is the share of the list who do not complete, and with non-completion near 45 percent a random list already reaches about 45 percent, so the target said almost nothing. The last card lists what else is judged: whether later non-completers are ranked first, whether predicted risks match the observed rates, which is called calibration, and whether the list helps the decision.

The plan also fixed, in advance, gate S1: to replace the simple rule, a model's list had to find more non-completers than the rule's list on the 13 test runs of 2014, by more than chance. Then we ran it.

**Sources:** Milestone 5 report, Sections 9 and 9.1, Table 9.1; Appendix IX.

## Slide 10 – What We Ran: Level 2 for AQ3 and AQ4 [plan 59]

**Speaker notes:**

The lead line: every question now has real results, AQ1 and AQ2 on both years, and AQ3 and AQ4 by one test of a model frozen on 2013 and scored once on the 13 runs of 2014.

In Milestone 5 we ran the optional prototype test that the brief calls Level 2, exactly as Milestone 4 had fixed it. The four tiles give the outcome per question: AQ1 descriptive, AQ2 diagnostic and AQ3 predictive are Answered, in filled orange; AQ4 prescriptive is Partial, in light orange, because its ranking is answered while its contact part has no data.

The model was developed only on the 2013 runs, frozen, and scored once on the 13 runs of 2014: 15,724 enrolments at day 27, of whom 6,911 did not complete. In development no more complex model beat the penalised logistic model, a regression that shrinks weak signs, so it stayed.

The table compares four lists of 5 per 20 students. Read the third column, the share of all non-completers on the list. One row needs a word: the background-only model uses module, start month, previous attempts, credits studied, education and how early the student registered, but no activity. The model's lists hold 2,868 non-completers, 41.5 percent; the early-sign rule, ranked by number of signs, 2,786, or 40.3 percent; a model that knows only the students' background 2,244, or 32.5 percent; and a random list is expected to hold 1,738, or 25.1 percent. The last column, the share of the list that does not complete, runs from 72.5 percent for the model and 70.4 percent for the rule to 56.7 percent for the background-only model and 43.9 percent for a random list. Background alone does much worse than behaviour.

The orange box gives the verdict on gate S1: met. The model's normalised recall is 72.5 percent against 70.4 percent for the rule, and it is ahead in 11 of the 13 runs, a small margin but beyond chance. Normalised recall equals the last column here because each list of five per twenty is shorter than its run's number of non-completers, so the best possible list would hold only non-completers. This share means something here because it is compared with the rule and with a random list on the same runs, 43.9 percent, not with a fixed target like the 50 percent of Milestone 1. Which list to use? The model ranks the list, and the early-sign rule, which finds 97 percent of the model's hits, is the fallback whenever the model cannot run. Now the answers question by question, starting with the size of the problem.

**Sources:** Milestone 5 report, Section 10, Table 10.1.

## Slide 11 – AQ1: How Many Do Not Complete [plan 64]

**Speaker notes:**

AQ1, the descriptive question, measures the size of the problem, and the lead line gives the answer: close to half of the enrolments still registered at day 14 do not complete, a quarter by failing and a fifth by withdrawing, and the two years agree.

The big number: of the 28,061 enrolments still registered at day 14, over 22 runs, 45.3 percent, that is 12,700, did not complete, with a 95 percent confidence interval, the range that holds the true rate with 95 percent confidence, of 44.7 to 45.8 percent. The key gives the definitions: day 14 is the first day after the add-drop period, the first two weeks, days 0 to 13, and non-completion means a fail or a withdrawal. By year, the rate is 45.7 percent of 12,076 enrolments in 2013 and 44.9 percent of 15,985 in 2014.

The bars split each year into its final outcomes: grey for distinction and pass, orange for fail, dark brown for withdrawn. About a quarter fail and a fifth withdraw in both years. Behind this average the runs differ strongly, from 24.9 to 58.3 percent, so one target for every course would hide where the problem sits.

Two further lines say how far to trust the number. The success criterion is met: two independent counts, one from the prepared data and one from the raw files, agree exactly. Confidence is high for OULAD in 2013 and 2014, while validity for the university's courses remains open; for the university, this is a hypothesis to recheck on its own records before D2, the decision on where to place support time, and D3, whether to extend the approach, rely on it.

The timing finding matters most for an early list: fewer than one in five non-completers had missed a task by week 4, 19.6 percent in 2013 and 14.7 percent in 2014. Missed tasks alone come too late, which is why the rule also watches activity. Next, which signs go with non-completion.

**Sources:** Milestone 5 report, Section 11.2; Appendix XII.

## Slide 12 – AQ2: Five Early Signs [plan 71]

**Speaker notes:**

The second question, AQ2, asks which early signs go with later non-completion, and the lead line gives the answer: all five early signs, inactivity included, go with later non-completion within module run, by similar amounts in 2013 and 2014.

The five signs are the rule's three parts, a missed task, a late TMA and no click in the last 7 days, that is days 21 to 27, plus two activity signs tested only here: activity below the run median, counted over days 0 to 27, and no click before the start, day 0.

How to read the chart: each dot is a risk difference, the extra percentage points of later non-completion among enrolments with the sign against those without, within the same module run and adjusted for the other signs, so that each dot shows that sign alone. Grey dots are 2013, orange dots 2014, and the whiskers are 95 percent intervals. The population is everyone registered at day 27: 11,811 enrolments in 2013, with 44.4 percent non-completion, and 15,724 in 2014, with 44.0 percent. Task signs are measured only on runs with a task due by day 27, which covers 9,960 and 12,585 enrolments.

The dashed line marks our criterion, fixed in advance: at least 5 points, an interval excluding zero, that is wholly above zero, and the same direction, higher non-completion with the sign, in at least two-thirds of modules. All five signs clear it in both years. A missed task stands out, adding about 40 points in both years. A late TMA adds about 20. The three activity signs add roughly 9 to 16 points each.

These are associations, not causes: they explain why a name is on the list, not that removing a sign would keep the student. For the contact decision they become the reason printed beside each name, which staff check before they call. Next, the ranked list itself.

**Sources:** Milestone 5 report, Section 11.3; Appendix XIII, Table A.33.

## Slide 13 – AQ3 and AQ4: The Ranked List [plan 76]

**Speaker notes:**

The third and fourth questions turn the signs into a list. The lead line: a model built on 2013 ranks the 2014 students slightly better than the early-sign rule, gives a reason beside each name, and its score is a rank, not a probability. The second line sets the limit: neither answer says who should make contact or whether contact helps, and the order of risk is not shown to match the need for help: the students most at risk may not be those who gain most from a contact.

The left card answers AQ3, the predictive question, which is Answered. Both cut-offs: lists of 5 per 20 hold 38.6 percent of later non-completers at day 13 and 41.5 percent at day 27, so waiting two more weeks adds little and the week-3 list is almost as good. Model and rule: they share most names, and each list holds 903 students the other does not; of the students only the model picks, 59.7 percent do not complete, against 50.6 percent of those only the rule picks. Probability: the predicted risks match the observed rates, which is calibration, in only 5 of the 13 runs, so staff should see ranks and reasons, not probabilities.

The right card answers AQ4, the prescriptive question, which is Partial. Order: counted per 20 students, the size of one tutor group, the top-ranked student is a later non-completer 92.4 percent of the time, the fifth-ranked 57.6 percent and the sixth-ranked 55.2 percent; from the seventh on it is 47.3 percent or less, close to the base rate of 44.0 percent, the share of 2014 enrolments still registered at day 27 that did not complete. We tested lists of five, and since the sixth-ranked student is still clearly above chance, five to six per twenty is where effort pays.

Reasons: for 80.7 percent of listed students the main reason is behaviour, that is low activity, a missed task or a late submission, rather than background. Fairness: the check, which flags any group reached more than 10 points less well than other students, found none of the three groups fixed in advance disadvantaged: students with a declared disability, students in the most deprived band, and students with no deprivation band recorded. What these data cannot say is whether contact helps; that needs the pilot. Before the take-home, a look back at how the plan changed.

**Sources:** Milestone 5 report, Sections 10 and 11.4; Appendix XIV.

## Slide 14 – What Changed Along the Way [plan 95]

**Speaker notes:**

The plan of Milestone 1 did not survive the data, and the lead line says how we handled that: each turning point was recorded, tested and turned into a rule the next milestone could rely on. The table has one row per turning point, read from what happened, through what we did, to where it stands.

Milestone 1: we had no real staff, so generative AI played the five stakeholders. We checked all 51 key quotes against the transcripts and ran a validation round, in which the AI stakeholders confirmed the agreed design; the requirements still need confirming with real staff before a pilot.

Milestones 2 and 3, first row: the data brought duplicate clicks, missing exam results and documentation unlike the files. We logged nineteen issues, each with a decision, and the duplicates barely matter: the early-click comparison stays the same. Second row: the Milestone 1 rule could fire in only 1 of 22 runs, so we built the early-sign rule, a missed task, a late TMA or seven silent days. That is resolved, with one rule for the analysis and the pilot.

Milestone 3: an AI leakage audit of our preparation code found eight errors our checks had missed. We reproduced and fixed each one and showed that every check can catch an error; all 22 data checks now pass. Milestones 3 to 5: the 50 percent precision target proved meaningless, since a random list reaches about 45 percent, so all four questions were revised and lists are judged within capacity. AQ1 to AQ3 are answered, and AQ4 in part.

Milestone 5: the plan had not named the measure for tuning the model, that is for choosing the strength of its penalty on the 2013 runs. We tuned it on log loss, a standard measure of how far predicted risks fall from the actual outcomes, a choice made after the tuning results under both log loss and recall were known, and we disclose it. The 2014 test set also grew from the 9 runs that have a 2013 twin to all 13 runs of 2014, a change not recorded until Milestone 5; the 9 runs are still reported apart, and the gain holds on them too. Both changes sit in the Change Log, the record of every change with its reason, and gate S1 is met whether the model is tuned on log loss or on recall. Now, the take-home.

**Sources:** Self-assessment, Section 1, Table 1.1; Milestone 5 report, Change Log (Appendix III).

## Slide 15 – Take-home [plan 93]

**Speaker notes:**

Three things to take home: what to watch, how long a list should be, and what to prove first.

First, watch for inactivity, not only missed tasks. About 45 percent of students still registered after the add-drop period do not complete, and fewer than one in five of them have missed a task by week 4. Inactivity shows earlier: each of the three activity signs, such as a week without platform activity, goes with roughly 9 to 16 more points of later non-completion, and they can be seen even in runs where no task is yet due.

Second, size the list to the people who will call. The top-ranked student in each group of twenty was a future non-completer more than nine times in ten, and from the seventh on the list was hardly better than chance. So five to six names per twenty is where effort pays, each with the reason it is there, which staff check before they call.

Third, read scores as ranks, and pilot before scaling. The model's risks are not reliable probabilities in every course, and no open dataset shows whether calling helps. So our recommendation is staged: recount the results on the university's own records; classify the list's risk before use, because Vietnam's Law on Artificial Intelligence, No. 134/2025/QH15, requires a person to keep control of every decision of an AI system, and Decision 33/2026/QĐ-TTg lists systems that assess or rank learners among the high-risk uses of AI in education; and run a randomised pilot with every contact and outcome logged.

The line at the bottom puts it in one sentence: watch for inactivity, size the list to capacity, and prove that contact works before scaling.

**Sources:** Milestone 5 report, Sections 11.2, 11.4, 12.1 and 14.

## Slide 16 – Thank You and Questions [plan 94]

**Speaker notes:**

Thank you for your time. In short: an early list should watch for inactivity as well as missed tasks, be as long as the staff who will call can manage, and be tried in a randomised pilot before it is used more widely.

Every number in the talk comes from the Open University Learning Analytics Dataset, by Kuzilek, Hlosta and Zdrahal, published under the CC BY 4.0 licence. We are happy to take questions on any step, from the data we chose to the pilot we propose; the appendix slides hold the detail behind every number.

**Sources:** Milestone 5 report, Sections 12.1 and 14.
