# Full deck script, part 4: plan slides 70–94

From the AQ2 findings to the thank-you slide: AQ2 in five slides, the expected outputs of AQ3 and AQ4, the answers by
question, decision support for D1–D3, limitations and future work with the pilot, generative AI use, conclusions,
take-home and closing. Every number comes from the Milestone 5 report (English sections); the Sources line of each
slide names the section or table behind it.

## Slide 70 – AQ2: How We Tested the Signs   [11 Findings]   [Line: detail]
**Lead:** We compared each early sign within its own module run, adjusted for the other signs, on 2013 and again, unchanged, on 2014.
**On the slide:** Population: enrolments still registered at day 27; 2013: 11,811 in 9 runs (44.4% non-completion);
2014: 15,724 in 13 runs (44.0%), including module CCC. Task signs, in runs with a task due by day 27 (9,960 and 12,585
enrolments): Missed task (a TMA or CMA due by day 27, not submitted); Late TMA. Click signs, in every run: No click in
the last 7 days (days 21–27); Activity below the run median (clicks on days 0–27); No click before the start (day 0).
Model and result: logistic regression with a fixed effect for each run, background terms (previous attempts,
credits) and sign × module terms; result = risk difference in percentage points, each sign adjusted for the other four;
an association, not an effect. Criterion fixed in Milestone 4: at least 5 points, 95% interval excluding 0, same direction
in at least two-thirds of the modules; p-values take no part. Key: AQ2 = the diagnostic question; TMA = tutor-marked
assignment; CMA = computer-marked assessment; run = one offering of a module.
**Visual:** five sign tiles in two groups (task signs, click signs), each group with its population, beside the model
and criterion cards (structure: which sign is defined where).
**Speaker notes:** Missed tasks came too late for most non-completers, so the diagnostic question, AQ2, asks what else shows by day 27. We took the enrolments still registered at day 27: 11,811 in the nine runs of 2013, and 15,724 in the thirteen runs of 2014, where we reran the same model unchanged. Each sign is dated on or before day 27. Task signs exist only in runs with a task due by then; click signs exist in every run. The model is a logistic regression with a fixed effect for each run, so a student is compared only with others in the same run, and each sign is adjusted for the other four. Each result is a risk difference in percentage points: an association, not an effect. The verdict rule was fixed in Milestone 4. Here is what the signs show.
**Sources:** [M5 §11.3], [M5 App XIII, Population, signs and model], [M5 §9 Table 9.1]

## Slide 71 – AQ2: Five Early Signs   [11 Findings]   [Line: main]
**Lead:** All five early signs, inactivity included, go with later non-completion within module run, by similar amounts in 2013 and 2014.
**On the slide:** Chart (Figure A.3): mutually adjusted risk difference, 2013 / 2014, points with 95% intervals:
missed task 40.8 (37.7–43.9) / 39.3 (36.4–42.1); late TMA 20.2 / 20.3; no click in the last 7 days 14.5 / 15.8;
activity below the run median 13.4 / 14.6; no click before the start 10.6 / 8.7. The five signs defined; risk
difference defined; population: registered at day 27, 11,811 enrolments in 2013 (44.4% non-completion) and 15,724 in
2014 (44.0%), task signs on 9,960 and 12,585; criterion: at least 5 points, interval excluding 0, same direction in
two-thirds of modules. These are associations, not causes.
**Visual:** the report's Figure A.3 as a dot plot with 95% intervals, grey dots for 2013 and orange for 2014, dashed
line at the 5-point criterion (comparison with uncertainty).
**Speaker notes:** With the method fixed, here are the results. Each dot is a risk difference: how many more percentage points of later non-completion students with the sign show, against students without it in the same run. A missed task by day 27 goes with 40.8 more points in 2013 and 39.3 in 2014; in raw terms, 90.0 percent of the 2013 students with a missed task did not complete, against 39.6 percent without one. A late TMA goes with 20.2 and 20.3 points. No click in the last seven days, 14.5 and 15.8. Activity below the run median, 13.4 and 14.6. No click before the start, 10.6 and 8.7. All five clear the criterion in both years, and no sign moves by more than two points between them. These are associations, not causes. Do they hold module by module?
**Sources:** [M5 §11.3], [M5 App XIII Figure A.3, Table A.33], [M5 §9 Table 9.1]

## Slide 72 – AQ2: Consistent Across Modules   [11 Findings]   [Line: detail]
**Lead:** Each sign points the same way in every module in 2013 and in 29 of 30 module estimates in 2014, but its size varies between modules.
**On the slide:** Heat table of Table A.34: mutually adjusted risk difference of each sign in each module, 2013 and
2014. 2013: every sign in the same direction in every module where it is defined (4 of 4 modules for the task signs,
6 of 6 for the click signs). 2014: 29 of 30 module estimates; the exception is a late TMA in AAA, −1.2 points
(−14.4 to 12.1) on 348 enrolments, an interval that includes 0; no CCC student had a late TMA by day 27. Size varies:
no click in the last 7 days goes with 27.5 points in EEE but 3.8 in GGG (2013). Intervals including 0 lie mostly in the
small module AAA: no evidence there, not evidence that the sign carries no information. Consistency means the same
direction, not the same size. Key: AAA–GGG = the seven anonymised OULAD modules; TMA = tutor-marked assignment.
**Visual:** heat table, signs × modules for each year, colour = risk difference, cells whose interval includes 0 in
italics with a dashed outline, the AAA 2014 exception outlined in red (comparison).
**Speaker notes:** Two years agreeing is encouraging; the next test is module by module. In this heat table each cell is one sign in one module, and the darker the cell, the larger the risk difference. In 2013 every sign points the same way in every module where it is defined. In 2014, 29 of the 30 module estimates do. The one exception is a late TMA in the small module AAA: minus 1.2 points on 348 enrolments, with an interval from minus 14.4 to plus 12.1, so it tells us little either way. What does vary is size: no click in the last seven days goes with 27.5 points in EEE but only 3.8 in GGG. So consistency means the same direction, not the same size, and a new run may differ. Next, did our own analysis choices drive these results?
**Sources:** [M5 §11.3], [M5 App XIII Table A.34]

## Slide 73 – AQ2: Sensitivity Runs   [11 Findings]   [Line: detail]
**Lead:** Six sensitivity runs in each year change no verdict: every sign stays above 5 points with an interval excluding 0.
**On the slide:** Chart of Table A.35 (2013): each sign's mutually adjusted risk difference in the primary analysis and
under six variants (de-duplicated clicks; late CMAs counted as late; flagged enrolments removed; the 2 runs with no task
due removed; low activity cut at half the run median; one sign effect for all modules). Largest shift: counting late
CMAs lowers the late sign from 20.2 to 15.2 points, because by day 27 a late CMA occurs only in DDD 2013B, in 85.65% of
its enrolments. 2014: the smallest estimate under any variant is 6.9 points, lowest interval bound 4.3. Pooled over all
22 runs (27,535 enrolments at day 27): 39.8, 20.6, 14.7, 14.0 and 9.4 points, criterion met in every module. Key:
sensitivity run = the same model with one analysis choice changed; CMA = computer-marked assessment.
**Visual:** dot strips, one row per sign, an orange dot for the primary estimate and grey dots for the six variants,
dashed line at the 5-point criterion (comparison: how far the choices move each sign).
**Speaker notes:** Next, were these results an artefact of our choices? We reran the 2013 model six times, each time changing one choice: removing duplicate clicks, counting late computer-marked tasks as late, dropping uncertain records, dropping the two runs with no task due, cutting low activity at half the median, and forcing one sign effect for all modules. On the chart, the orange dot is the primary estimate and the grey dots are the variants; every dot stays to the right of the five-point line. The biggest move is the late sign, from 20.2 to 15.2, because only one run had late computer-marked tasks by day 27, in 85.65 percent of its enrolments. In 2014 the smallest estimate under any variant is 6.9 points. One model check, though, found a real weakness.
**Sources:** [M5 App XIII Table A.35], [M5 App XIII, Sensitivity runs and model checks], [M5 App XIII, Comparison of the two years]

## Slide 74 – AQ2: Activity Works as a Gradient   [11 Findings]   [Line: detail]
**Lead:** The yes-or-no click signs miss a graded activity pattern, and once clicks enter as a continuous measure the below-median sign falls below the criterion in 2014 while the other four still meet it.
**On the slide:** Chart of Table A.36 (2013): observed minus predicted non-completion by activity level on days 0–27,
with the ±2 standard-error band: no click +5.6 (band 3.0); below half the median +2.6 (1.7); half the median to the
median −3.7 (1.8); median to twice the median +1.9 (1.5); twice the median or more −2.6 (1.8); all five outside the
band. Table: each sign planned → with a continuous click adjustment: missed task 40.8 → 37.3 (2013), 39.3 → 35.6
(2014); late TMA 20.2 → 19.5, 20.3 → 19.5; no click in the last 7 days 14.5 → 9.3, 15.8 → 10.7; activity below the run
median 13.4 → 5.8, 14.6 → 5.9 (same direction in only 4 of 7 modules: criterion not met); no click before the start
10.6 → 8.9, 8.7 → 6.5. The added run was chosen after the residuals were seen, so it qualifies the verdict; the planned
estimates remain the primary result. Design consequence: the AQ3 model uses continuous click measures. Key: residual =
observed minus predicted; continuous adjustment = log(1 + clicks on days 0–27) added to the model.
**Visual:** bar chart of residuals by activity level with the ±2 standard-error band as a whisker (trend: risk keeps
falling as activity rises, not in one step), beside a before-and-after table.
**Speaker notes:** One model check found a real weakness. Observed against predicted non-completion by activity level, the model is off in all five levels. Students with no click at all in four weeks did not complete 5.6 points more often than predicted; students between half the median and the median, 3.7 points less often. The yes-or-no sign treats everyone under the median alike, yet non-completion keeps falling as activity rises. So, after seeing this, we added one run with clicks as a continuous measure. The misfit disappears in 2013 and shrinks in 2014. The click signs shrink, and the below-median sign falls to 5.8 points in 2013 and 5.9 in 2014, where it no longer meets the criterion. The other four still do. Chosen after looking, this run qualifies the verdict. So what do the signs mean for a list?
**Sources:** [M5 §11.3], [M5 App XIII Table A.36], [M5 App XIII, Sensitivity runs and model checks]

## Slide 75 – AQ2: What the Signs Mean for the List   [11 Findings]   [Line: main]
**Lead:** The signs give each name on a contact list a factual reason staff can check and show that the early-sign rule needs its activity part, but they do not show that contact would help.
**On the slide:** Three numbers: 40.8 points, the strongest sign, a missed task (2013; 39.3 in 2014); 19.6%, the share
of 2013 non-completers (Fail or Withdrawn) with a missed task by week 4 (14.7% in 2014); 6 of 22 runs had no task due by day 27, while the
click signs are defined in every run. The signs can: give each listed name a factual reason a member of staff checks
against the record; show that each part of the early-sign rule carries information on its own, inactivity included;
suggest, as a hypothesis, where early support could go. The signs cannot: show a cause, since a student
who stops clicking may already have decided to leave; show that contact helps; justify treating a group differently
(the missed-task sign holds in each of the 15 groups of 2013, as a description). Confidence: moderate: two years agree,
but the click signs rest on a known misfit, and unrecorded reasons could explain the associations. The early-sign rule
is spelled out in the "can" card (missed task, late TMA, no click in the last 7 days).
**Visual:** a row of three number tiles (strength against reach) above two cards "The signs can" / "The signs cannot", with
the confidence bar at the bottom (comparison).
**Speaker notes:** Let us put timing and signs together, because this is the turning point of the project. A missed task is the strongest sign, 40.8 points in 2013. Yet by week 4 it has appeared for only 19.6 percent of the students who will not complete, and in six of the 22 runs nothing was even due. A week without clicks can be measured in every run. So the early-sign rule must keep its activity part. What can the signs do? They give each name on a list a factual reason that a member of staff can check, and each part of the rule carries information on its own. What can they not do? Show a cause: a student who stops clicking may already have decided to leave. So confidence is moderate. Now, the two questions still waiting for their test.
**Sources:** [M5 §11.2], [M5 §11.3], [M5 App XII Table A.31], [M5 App XIII Table A.33], [M5 App XIII, Groups of students and What AQ2 means for the project]

## Slide 76 – AQ3 and AQ4: Expected Outputs   [11 Findings]   [Line: main]
**Lead:** AQ3 and AQ4 would give a ranked, capacity-limited list with reasons, and the simple rule stays if the model does not beat it.
**On the slide:** A mock-up card "Expected output – not a result": five anonymous rows, each with the sign tags behind
the name. AQ3 would give: a risk rank per enrolment at days 13 and 27, a probability only if calibration holds; gate S1
answers it on the 13 runs of 2014. If the model does not beat the rule: the rule's order stays, and its list is
measured as a baseline. AQ4 would give: a list of 3 or 5 per 20 students per run, with the signs behind each name;
answered when it meets S1, rule FR1 passes or its flags are reviewed, and the assumption that the order of risk matches
the order of need is stated as untested. Status:
Deferred; expected outputs, no model metric. Key: AQ3 = predictive question; AQ4 = prescriptive ranking question;
S1 = the gate to replace the rule; FR1 = the fairness review rule. Callout at the bottom: neither says who should make
contact or whether contact helps.
**Visual:** a dashed mock-up of the list, labelled "expected output – not a result", with no names and no numbers
(worked example of the output's form).
**Speaker notes:** Those were the questions we could answer. The predictive and ranking questions, AQ3 and AQ4, have expected outputs, not results, because no model has been trained. AQ3 would give each enrolment a risk rank at day 13 and day 27, shown as a probability only if calibration holds, and gate S1 alone, judged once on the 13 runs of 2014, decides whether it beats the rule. If it does not, the rule's order stays, and the same test measures how good the rule's own list is. AQ4 would turn the ranking into a list of three or five per twenty students, with the signs beside each name, and is answered only with the fairness rule passed or its flags reviewed. Neither output says who should call a student or whether calling helps. Here are the four answers side by side.
**Sources:** [M5 §11.4], [M5 App XIV Table A.37]

## Slide 77 – Answers by Question   [11 Findings]   [Line: main]
**Lead:** We can describe the size and timing of non-completion and name its early signs; we cannot yet rank better than the rule or say whether contact helps.
**On the slide:** Table 11.3 in four columns: AQ1 (descriptive) – 22 runs, day 14: 28,061 enrolments; Wilson rates
under two denominators – 45.3% did not complete; runs 24.9–58.3%; under 20% missed a task by week 4 – high for OULAD
2013–2014; KPI proxy – D2 hypothesis; tasks alone come too late. AQ2 (diagnostic) – day 27: 11,811 and 15,724;
logistic, run fixed effects – five signs consistent in both years; missed task 40.8 and 39.3 points – moderate;
association – D1 reasons; contact to test. AQ3 (predictive) – proposed: 2013 → 2014; penalised logistic – expected:
risk rank; gate S1 – not applicable – D1 order only if S1 is met. AQ4 (prescriptive ranking) – proposed: AQ3 scores;
top-k list; FR1 – expected: 3 or 5 per 20 with signs – not applicable; no contact data – D1 list, not a contact plan.
Key: D1 = whom to contact; D2 = where support time goes; S1 = the gate to replace the rule; FR1 = the fairness review
rule; KPI = key performance indicator; OULAD = Open University Learning Analytics Dataset.
**Visual:** the answers table, status coloured: answered rows orange, deferred rows blue (lookup table).
**Speaker notes:** The four answers, each read at its own level. AQ1, descriptive: 45.3 percent of the enrolments registered at day 14 did not complete, runs ranged from 24.9 to 58.3 percent, and fewer than one in five non-completers had missed a task by week 4; high confidence for OULAD. AQ2, diagnostic: five signs consistent in both years, a missed task at 40.8 and 39.3 points; moderate confidence, because these are associations. AQ3 and AQ4: expected outputs only, so their confidence reads not applicable. Read across the rows: we can describe the problem and name its early signs, but we cannot yet say whether a model ranks better than the rule, and not at all whether contact helps. The last column is what matters to staff, so let us take the decisions one by one, starting with whom to contact.
**Sources:** [M5 §11.5 Table 11.3], [M5 App XIV Tables A.38 and A.39]

## Slide 78 – Decision D1: Whom to Contact   [11 Decision support]   [Line: main]
**Lead:** For whom to contact, the early-sign rule is the candidate list, with its signs shown as reasons, once its own list performance has been measured.
**On the slide:** Decided by course lecturers, lecturer-advisors and the support office; reversible. Evidence now: a
missed task goes with 40.8 more points of non-completion (37.7–43.9) in 2013; each part of the early-sign rule carries
information on its own; by week 4 only 19.6% of non-completers had missed a task, and 2 of the 9 runs of 2013 had no
task due by day 27. Decision option: build the week-3 and week-5 lists of the pilot from the early-sign rule, including
its activity part, ordered by the number of signs, with the signs beside each name; a member of staff checks every name;
the AQ3 ranking replaces the order only if gate S1 is met. Check before adoption: the rule's list of 3 or 5 per 20
reaches more later non-completers than a random list of the same length (baseline B2 of the AQ3 test); contact raises
completion against usual support, in a randomised pilot; the contact person and the offer stay open choices for that
pilot. Number box: 28.8% – the rule flags 28.8% of the 27,535 enrolments registered at day 27 across the 22 runs, more than a
list of 5 per 20 students (25%) can hold, so the list is ordered by the number of signs. Key: early-sign rule; S1; B2.
**Visual:** three linked columns, evidence now → decision option → check before adoption, the option in orange
(sequence), above a number box for the 28.8% the rule flags.
**Speaker notes:** Starting with D1, whom to contact, a decision of the lecturers, the lecturer-advisors and the support office, and a reversible one. The evidence supports a clear candidate: the early-sign rule. It is interpretable, computable from records the university already holds, and each of its parts goes with later non-completion in both years. So the option is to build the week-3 and week-5 lists from it, ordered by the number of signs, with the signs shown beside each name, and a member of staff checks every name. Two checks come first. How well its list reaches non-completers has not been measured; that is baseline B2 of the AQ3 test. And whether contact helps can only be tested in a randomised pilot. Next, where support time goes.
**Sources:** [M5 §11.5], [M5 App XIV Table A.40], [M5 App IX, list scenario] (28.8% of 27,535 at day 27)

## Slide 79 – Decision D2: Where Support Time Goes   [11 Decision support]   [Line: main]
**Lead:** Support time could go first where non-completion and early signs are highest, as a hypothesis to check on the university's own records.
**On the slide:** Decided by the program manager, each semester. Chart: non-completion by module, 2013, registered at day
14 (Table A.30), February against October starts. Evidence now: non-completion from 24.9% to 57.5% between the runs of
2013; February runs 51.6% against October runs 42.4% (2013); no click on days 21–27 in 54.8% of GGG 2013J but 7.6% of
DDD 2013B. Decision option, as a hypothesis: place early support time first in the courses and intakes with the
highest non-completion and the highest share of early signs, measured on the university's own records. Caution: high
risk marks where non-completion concentrates, not where support helps most. Check before adoption: the pattern repeats
in the university's courses over several semesters; the baseline is recounted under the add-drop rule. Key: run = one
offering of a module (B = February start, J = October start); add-drop rule = only students still registered at day 14
count.
**Visual:** bar chart of 2013 non-completion by module and by start month with 95% Wilson intervals (comparison: where
losses concentrate), beside the evidence → option → check column.
**Speaker notes:** From D1 to D2, the program manager's choice of where support time goes each semester. In the 2013 runs of OULAD, non-completion ranged from 24.9 to 57.5 percent, February intakes lost more than October ones, 51.6 against 42.4 percent, and the share of students with no click in the last week before day 27 ranged from 7.6 percent in one run to 54.8 in another. So the option is to place early support time first where both non-completion and early signs are highest. But it is a hypothesis, for two reasons. OULAD is not the university, so the pattern must repeat in its own courses over several semesters, under one add-drop rule. And a high-risk course shows where losses concentrate, not where support would help most. Finally, the largest decision, D3.
**Sources:** [M5 §11.5], [M5 App XIV Table A.40], [M5 App XII Table A.30]

## Slide 80 – Decision D3: Whether to Extend   [11 Decision support]   [Line: main]
**Lead:** For extending the approach, the project offers a measurement method, a gate and a fairness audit, not a verdict; extension waits for a pilot result.
**On the slide:** Decided by leadership with the legal and data office, on the pilot's results; close to a one-way door.
Evidence now: the denominator alone can move a completion rate by up to 13.6 points; AQ3 and AQ4 have no result; no
evidence on the effect of contact exists. What the project offers: a measure, one completion rule for pilot and comparison
courses (the AQ1 method); a gate, S1, fixed in advance; an audit, fairness by rule FR1. Extend only if all three hold: a completion gain against comparison courses; legal approval under
Vietnam's rules on high-risk AI use; staff capacity confirmed. Closing line: even a negative pilot result shows, at small scale,
which part of the path fails. Key: D3; S1; FR1; AI = artificial intelligence.
**Visual:** the evidence card, then the three offered tools as stacked boxes, then the three numbered conditions (structure: what must hold before a
one-way decision).
**Speaker notes:** D3 is the decision closest to a one-way door: extending the approach to all courses and linking data routinely. Here the project offers tools rather than a verdict. First, a way to count completion by one rule in pilot and comparison courses, which matters because the denominator alone can move a rate by up to 13.6 points. Second, a gate a model must pass, fixed in advance. Third, a fairness audit. What it cannot offer yet is any evidence that contact helps. So extension waits for three conditions: a completion gain against comparison courses, legal approval under Vietnam's rules on high-risk AI, and confirmed staff capacity. Even a negative pilot is valuable, because it shows at small scale which part of the path fails. That brings us to the limits of everything we have shown.
**Sources:** [M5 §11.5], [M5 App XIV Table A.40], [M5 App XII] (13.6 points)

## Slide 81 – Three Kinds of Limit   [12 Limitations]   [Line: main]
**Lead:** We keep three kinds of limit apart, because each calls for a different next step.
**On the slide:** No evidence found: a comparison was made and showed no clear difference (e.g. the year difference over
all enrolments in the six shared modules, −0.2 points, −1.4 to 0.9) → no claim; reported as uncertain. No data to test:
OULAD and every screened dataset lack the data (contacts and their outcomes, delivery mode, year of study, attendance,
staff capacity) → collected in the randomised pilot. Not yet tested: the data exist, but the analysis waits for the
single AQ3 test (AQ3 and AQ4 results) → the single test, design unchanged. Three conditions on every answer: UK
distance-learning modules of 2013–2014, and instructional conditions change what predicts success; confounding makes the
effect of contact unknowable from these data; a flag must not become a label. Key: OULAD; AQ3.
**Visual:** three labelled boxes, each with an arrow to its next step, above a strip of the three conditions
(structure).
**Speaker notes:** Every answer we gave has a boundary, and we sort the boundaries into three boxes, because each needs a different next step. "No evidence found" means we compared and saw no clear difference, such as the year difference within the six shared modules over all enrolments; we make no claim. "No data to test" means neither OULAD nor any dataset we screened holds the data: contacts, delivery mode, year of study, attendance, staff capacity. Only the pilot can create them. "Not yet tested" means the data exist, but the analysis waits for the single AQ3 test. On top of that, three conditions hang over every answer: two years of UK distance learning, confounding that hides the effect of contact, and a flag that must never become a label. Here is the full log.
**Sources:** [M5 §12], [M5 App XV Table A.41]

## Slide 82 – Limitation Log   [12 Limitations]   [Line: detail]
**Lead:** Each limit is logged with its kind and its handling, so a reader knows where each answer can and cannot be used.
**On the slide:** Table 12.1: year difference over all enrolments in shared modules; small-module click signs
(intervals include 0) – no evidence found – no claim; reported as uncertain. Contact and its outcome; delivery mode,
year of study, attendance; capacity – no data to test – randomised pilot. Several-modules sign before 2014; leave and
transfer – no data to test – described on 2014; university recount. AQ3 and AQ4 results – not yet tested – single AQ3
test, design unchanged. Binary click signs; below-median sign weak in 2014 once adjusted; KPI proxy and denominator –
measurement – continuous measures in AQ3; one add-drop rule. UK distance learning of 2013–2014; observational design –
scope and causal – re-check on the university's records; options as hypotheses. Key: KPI; several-modules sign = tasks
missed in more than one module at once.
**Visual:** the log table with the kind column colour-coded, red, blue and orange for the three kinds of the previous
slide (lookup table).
**Speaker notes:** Following those three boxes, here is the log. Where we saw no clear difference, such as the year difference in shared modules over all enrolments, or click signs in the smallest module, we make no claim. Contacts, delivery mode, year of study, attendance and capacity have no data anywhere, so they go to the pilot. The several-modules sign has almost no cases before 2014, and leave or transfer cannot be told apart from withdrawal, so the university must recount. AQ3 and AQ4 are not yet tested, and their design stays unchanged until the single test. Then measurement: the click signs are binary, the below-median sign is weak in 2014 once adjusted, and the KPI is a proxy. And the largest: two years of UK distance learning, observed rather than randomised. Next, a closer look at measurement.
**Sources:** [M5 §12 Table 12.1], [M5 App XV Table A.41]

## Slide 83 – Measurement and Model Limits   [12 Limitations]   [Line: detail]
**Lead:** Several design values are assumptions and several estimates are lenient, so the sizes of the estimates matter more than the verdicts.
**On the slide:** Table, limit – what it affects: KPI proxy: completion of a module run stands for course completion,
and approved leave or transfer counts as withdrawal – the baseline completion rate. Denominator: up to 13.6 points
between definitions – every year comparison. Capacity assumed: 3 or 5 per 20 students; runs stand in for each
lecturer-advisor's groups – the list lengths of D1 and AQ4. Lenient criterion: 5 points at a base rate near 44% – the
AQ2 verdicts; sizes separate the signs. Intervals treat the runs as fixed – a later run may vary more (3.8 to 27.5 points
across modules). Run length 234 to 269 days, longer than a semester – the meaning of "week 4". Gate S1 sets no minimum
gain – a pass is read with the number of extra non-completers listed. Fairness criteria cannot all hold when base rates
differ – one criterion, equal recall at capacity. Key: KPI; AQ2; AQ4; D1; S1.
**Visual:** a two-column table, limit and what it affects (lookup).
**Speaker notes:** Following the log, a closer look at measurement and model limits. The KPI is a proxy: a module run stands for a course, and approved leave or transfer counts as withdrawal; and the denominator alone moves a rate by up to 13.6 points. Capacity is assumed, three or five per twenty, with runs standing in for each lecturer-advisor's groups. Our five-point criterion is lenient when the base rate is near 44 percent, so the sizes, not the verdicts, separate the signs. The intervals treat runs as fixed, so a new run may vary more. A module run lasts 234 to 269 days, longer than a semester. Gate S1 sets no minimum gain. And fairness criteria cannot all hold at once when base rates differ, so we fixed one. Next, the work that would lift these limits.
**Sources:** [M5 §12], [M5 App XV, Measurement and Model and analysis limits], [M5 App XII] (13.6 points), [M5 App XIII Table A.34]

## Slide 84 – Future Work in Order   [12 Future work]   [Line: main]
**Lead:** Two steps can run on OULAD as it stands; three need the university, and the last, a randomised pilot, alone can show whether contact helps.
**On the slide:** Table A.42 as five steps: 1. The AQ3 test (Level 2 prototype): does a model at day 27 list more non-completers
than the early-sign rule (gate S1); the rule's own list performance; calibration – OULAD as prepared – the frozen
protocol of Milestone 4. 2. AQ4 list and fairness audit: recall at 3 and 5 per 20, gain over a random list, FR1 by
disability and deprivation band – the frozen AQ3 scores – step 1. 3. Transfer to the university: baseline completion
under the add-drop rule; the rule on the university's task calendar; AQ1 and AQ2 re-checked – two years of the
university's records – data access approved. 4. Risk classification and consent – legal review; consultation with
students in Vietnam – step 3. 5. Randomised pilot: does contact raise completion; which contact and offer work; KPI 1
contact part and KPI 2 – contact record with time, person, offer and outcome – steps 3 and 4. Key: S1; FR1; KPI 1 =
early-sign contact rate; KPI 2 = follow-up rate.
**Visual:** a five-step staircase, steps 1–2 under "On OULAD now", steps 3–5 under "At the university", step 5 in
orange (sequence).
**Speaker notes:** The limits translate directly into work, in order. Two steps run on OULAD as it stands. Step one is the Level 2 prototype of AQ3, exactly as Milestone 4 froze it: does a model list more non-completers than the rule, and how good is the rule's own list. Step two takes those frozen scores, forms the AQ4 lists of three or five per twenty, and runs the fairness audit by disability and deprivation band. Then three steps need the university. Step three recounts the baseline under the add-drop rule and re-checks AQ1 and AQ2 on its records. Step four is a legal risk classification and consultation with real students. Step five is the randomised pilot, which finally answers whether contact raises completion. Let us look at the university steps in turn.
**Sources:** [M5 §12.1], [M5 App XV Table A.42]

## Slide 85 – Next at the University: Recount and Replace Assumptions   [12 Future work]   [Line: detail]
**Lead:** At the university, the baseline is recounted under the add-drop rule, the early-sign rule is checked on its task calendar, and every assumed value is replaced by its records.
**On the slide:** Step 3, transfer to the university: recount baseline completion under the add-drop rule; check the
early-sign rule on the university's task calendar; re-check the AQ1 and AQ2 results. Data: two years of the
university's enrolment, task and platform records, with access approved by the legal and data office. Five assumed
values to replace: the baseline completion rate; the capacity figures; the one-week data delay; the list-length
scenarios (3 or 5 per 20); the ten-point fairness gap of rule FR1. Not imputed or simulated: contacts, attendance,
year of study. Acceptance of activity-based contact was voiced only by simulated students, so real students in Vietnam
must be asked. Key: add-drop rule = only students still registered at day 14 count; FR1.
**Visual:** a checklist of five assumed values with an arrow to "the university's records" (structure).
**Speaker notes:** Step three moves to the university. First, recount the baseline completion rate under the same add-drop rule we used, because, as AQ1 showed, the denominator can move a rate by more than ten points. Second, check the early-sign rule against the university's own task calendar. Third, re-check the AQ1 and AQ2 patterns on two years of its records. Along the way, five assumed values get replaced: the baseline rate, the staff capacity, the one-week data delay, the list lengths and the ten-point fairness gap. We do not impute or simulate contacts, attendance or year of study, because invented values would look like evidence. And one more honest point: only simulated students said they would accept contact based on their activity, so real students must be asked. Then come the legal duties.
**Sources:** [M5 §12.1], [M5 App XV Table A.42 and the text after it]

## Slide 86 – Risk Classification and Human Control   [12 Future work]   [Line: detail]
**Lead:** A contact list built from a model is likely a high-risk use of AI in education under Vietnamese law, so it needs a risk classification first, and staff keep the final say.
**On the slide:** Law on Artificial Intelligence, No. 134/2025/QH15, applies from 1 March 2026: human control and the
ability to intervene over every decision of an AI system. Decision 33/2026/QĐ-TTg lists among high-risk uses in
education AI systems that automatically assess or rank learners, and those that monitor or analyse learner behaviour.
So: step 4, a risk classification with legal review and consultation with students, before any contact; staff keep
the final say on every contact. Personal data: a declared disability is health information, so the pilot needs the
student's consent. Ethics: predictive analysis carries a potential for bias and stereotyping, so a flag leads to
support, expires with the run and never becomes a label. Key: AI = artificial intelligence.
**Visual:** a gate between step 3 and the pilot: "risk classification" with the two legal sources above it (sequence).
**Speaker notes:** Following the transfer step, the law. Vietnam's Law on Artificial Intelligence applies from 1 March 2026 and requires human control, and the ability to intervene, over every decision of an AI system. A 2026 government decision lists among high-risk uses in education systems that rank learners and systems that analyse learner behaviour. A contact list built from a model is likely to fall in that class. So step four is a risk classification first, with legal review and consultation with students, and staff keep the final say on every contact. A declared disability is health information, so the pilot needs consent to use it. Ethically, a flag leads to support and expires with the run; it never follows a student as a label. That brings us to the pilot itself.
**Sources:** [M5 §12.1], [M5 App XV], [M5 App VI, sensitive fields], [M5 §12]

## Slide 87 – The Randomised Pilot   [12 Future work]   [Line: main]
**Lead:** Only a randomised pilot among flagged students can separate the effect of contact from the reasons students are flagged, and its contacts are logged before any model is retrained.
**On the slide:** Design: among the flagged students of the pilot courses, random assignment to contact or usual
support, time zero at the eligibility cut-off; completion compared. Why random: only random assignment separates the
effect of contact from the reasons a student was flagged. Answers: whether contact raises completion; which contact and
offer work; the contact part of KPI 1 and KPI 2. Needs: a contact record with time, person, offer and outcome; year of
study, delivery mode, attendance. Rule: contacts logged with their outcomes before any model is retrained, since a model
retrained on outcomes shaped by contact would learn its own influence. Timing: steps 3 and 4 complete before contact
begins in Semester 2 of 2026–2027. Key: KPI 1 = early-sign contact rate; KPI 2 = follow-up rate.
**Visual:** a randomisation diagram: flagged students → random assignment → contact / usual support → outcome logged →
completion compared (sequence).
**Speaker notes:** And step five, the pilot. Among the flagged students in the pilot courses, some are randomly assigned to contact and the rest receive usual support, with time zero at the eligibility cut-off. Why randomise? Because flagged students differ from others in ways we cannot see; only random assignment separates the effect of contact from the reasons they were flagged. The pilot logs every contact: when, by whom, which offer, and what happened, which also measures the contact parts of our two secondary KPIs. One subtle rule: contacts are logged before any model is retrained, or the model would learn its own influence. Steps three and four must be complete before contact starts in Semester 2 of 2026–2027. Before we conclude, one more part of our process to account for: generative AI.
**Sources:** [M5 §12.1], [M5 App XV Table A.42 and the text after it]

## Slide 88 – Generative AI: Roles and One Rule   [13 Generative AI]   [Line: main]
**Lead:** AI proposed and challenged, and we verified; it was never a source of data, statistics, licence information or results.
**On the slide:** AI proposed, in four roles: simulated stakeholder; research and code assistant; critic; writing
partner. We verified with checks matched to what could go wrong: quotes against transcripts; literature against saved
copies with verbatim quotations; code against fixtures (small inputs with known answers) and independent recounts;
critics confined to the brief and the data. One rule: AI is never a source of data, statistics, licence information or
results; every fact it offered was checked against a saved source, the data files or code we ran. No AI produced a
metric value, threshold or result. Guidance followed: UNESCO holds that generative AI cannot be trusted to be accurate
and its information should never be accepted at face value. Key: AI = artificial intelligence; UNESCO = United Nations
Educational, Scientific and Cultural Organization.
**Visual:** four role chips → arrow → four verification chips, with the one rule beside them (structure: each role
paired with its check).
**Speaker notes:** We used generative AI in every milestone, and we owe you an account of how. It played four roles: a simulated stakeholder in Milestone 1, which is why we always call the interviews simulated; a research and code assistant; a critic of our plans; and a writing partner. In every role one rule held: AI was never a source of data, statistics, licence information or results. We matched each check to what could go wrong: quotes against transcripts, literature against saved copies with exact quotations, code against fixtures and independent recounts, and critics confined to the brief and the data. No AI produced a metric value, a threshold or a result. This follows UNESCO's guidance never to accept generative AI's output at face value. Here is what that looked like milestone by milestone.
**Sources:** [M5 §13], [M5 §13.1], [M5 §13.2], [M5 App XVI]

## Slide 89 – AI Decision Log   [13 Generative AI]   [Line: detail]
**Lead:** Each milestone records what AI was used for, how we checked its output and what we decided.
**On the slide:** Table A.43 in brief, stage – AI used for – our check – our decision: Milestone 1 – simulated
stakeholders and a reviewer, 12 critiques – each quote checked against its transcript; 9 accepted, 2 in part, 1
rejected – cut-offs moved to the end of weeks 2 and 4; the interviews count as simulated. Milestone 2 – requirement
critic and selection reviewer, 22 critiques – no dataset fact without the official source – gates require a dated
withdrawal and dated tasks. Milestone 3 – code assistant and a leakage auditor, 8 findings – fixture tests; 13 of 13
numbers equal to an independent recount – all eight findings acted on. Milestone 4 – three isolated reviewers, 24
critiques – each checked against design facts and arithmetic – switching rule with a margin fixed in advance; gate S1
fixed on all 13 test runs. Milestone 5 – evidence extraction, AQ1 and AQ2 code, drafting and review – 369 statements
checked against 32 sources, 0 errors; 2014 associations re-estimated by separate code, 35 of 35 agree – 66 critiques:
42 accepted, 14 in part, none rejected, 10 handled in finishing. Key: S1; AQ1; AQ2.
**Visual:** the log table, one row per milestone (lookup).
**Speaker notes:** Behind that rule is a decision log for every milestone. In Milestone 1, a reviewer gave twelve critiques; we accepted nine, two in part, and rejected one. In Milestone 2, critics pushed the gates to require a dated withdrawal and dated tasks. In Milestone 3, every script was kept only after review, thirteen of thirteen numbers matched an independent recount, and all eight findings of the leakage auditor were acted on. In Milestone 4, three isolated reviewers led us to fix a switching rule and the single gate in advance. In this milestone, 369 extracted statements were checked against 32 sources with no errors, the 2014 estimates were re-estimated by separate code, 35 of 35 agreeing, and the full draft drew 66 critiques. What did AI actually change, and what did we refuse?
**Sources:** [M5 §13.1], [M5 App XVI Table A.43]

## Slide 90 – What AI Changed, and What We Rejected   [13 Generative AI]   [Line: detail]
**Lead:** AI helped most when it had to argue from the data, and the decisions stayed ours.
**On the slide:** Where it helped: the Milestone 3 auditor found tasks due before registration counted as missed, and a
leakage check that could not fail, that is, one that would pass even with leakage; the Milestone 4 reviewer found that
the 2013 runs hold 6 modules, not 7, which made the AQ2 criterion a share of modules. What we rejected: removing early
identification from the Business Goal; an imbalance argument for precision–recall curves (non-completion is 44–46%);
looking at the outcomes of repeat test students, which would break the independent test. Decisions that stayed ours:
keep the 2014 runs out of every AQ3 choice; one early-sign rule for OULAD and the pilot; AQ3 and AQ4 reported as
designs; every association stated as an association. Key: AQ2, AQ3, AQ4.
**Visual:** three columns: helped (accepted) / rejected / decisions that stayed ours (comparison).
**Speaker notes:** Looking back, AI helped most when it had to argue from our data rather than from general advice. In Milestone 3 the auditor found real errors: tasks due before registration counted as missed, and a leakage check that could never fail. In Milestone 4 a reviewer noticed that the 2013 runs hold six modules, not seven, which changed our AQ2 criterion. Rejections mattered as much. We kept early identification in the Business Goal, did not use an imbalance argument when the classes are near half and half, and refused to look at repeat students' outcomes, which would have broken the test. And the key choices were ours: protect 2014, keep one rule, report designs as designs, and associations as associations. With that, we can draw our conclusions.
**Sources:** [M5 §13.2], [M5 App XVI]

## Slide 91 – Conclusions, Firmest First   [14 Conclusion]   [Line: main]
**Lead:** On OULAD, an early list cannot rest on missed tasks alone, and the early signs can serve as reasons that staff check beside each name.
**On the slide:** Three tiers, firmest at the top. 1. High confidence, OULAD 2013–2014: 45.3% of the enrolments
registered at day 14 did not complete; runs varied from 24.9% to 58.3%; the year comparison depends on the add-drop
rule; most non-completers first missed a task after week 4. 2. Moderate confidence: all five early signs go with later
non-completion in both years, a missed task by 40.8 and 39.3 points, in the same direction across modules, with one wide
exception; these are associations. 3. Design only: a penalised logistic model judged once against the rule, and a
capacity-limited list audited for fairness; outputs are expected, not measured. Key: OULAD; add-drop rule.
**Visual:** three stepped tiers, green, orange and grey, narrowing as confidence falls (structure).
**Speaker notes:** Let us draw it together, firmest first. With high confidence on OULAD: 45.3 percent of the enrolments still registered at day 14 did not complete, runs ranged from 24.9 to 58.3 percent, any year comparison depends on the add-drop rule, and most non-completers first missed a task after week 4. Two independent computations agree on these counts. With moderate confidence: all five early signs go with later non-completion in both years, a missed task by 40.8 and 39.3 points, in the same direction across modules; they are associations, useful as reasons, not causes. And as a design only: a penalised logistic model judged once against the rule, and a capacity-limited list audited for fairness; those outputs are expected, not measured. Just as important is what we cannot conclude.
**Sources:** [M5 §14], [M5 §11.2], [M5 §11.3], [M5 §11.4]

## Slide 92 – What We Cannot Conclude, and Open Problems   [14 Conclusion]   [Line: main]
**Lead:** Three claims stay out of reach of these data, and each maps to an open problem with a planned answer.
**On the slide:** Table, we cannot conclude that … – because – open problem and planned answer: the signs cause
non-completion – a regression capturing associations is descriptive, not causal – treat the signs as reasons to check,
never as causes; a model ranks students better than the rule – no model has been trained or tested – the single AQ3
test under the frozen protocol; contacting a listed student raises completion – no data record contact, and questions
of effectiveness need a randomised experiment – a randomised pilot with contacts and outcomes logged. Scope over all
three: every result describes UK distance-learning modules of 2013–2014 and is recounted on the university's records,
after a risk classification of the list. Key: AQ3; the rule = the early-sign rule.
**Visual:** a three-row table, the planned-answer column in orange (structure: claim → reason → next step).
**Speaker notes:** Equally firm is what we cannot say. We cannot say the signs cause non-completion: a regression that captures associations describes them; it does not explain them. So the signs stay reasons to check, never causes. We cannot say a model ranks students better than the simple rule, because no model has been tested; that is the single AQ3 test we kept clean. And we cannot say that contacting a listed student raises completion, because no data record a contact, and questions of effectiveness need a randomised experiment; that is the pilot. Over all three sits the scope: UK distance-learning modules of 2013 and 2014, to be recounted on the university's own records after a risk classification of the list. If you remember one thing, make it this.
**Sources:** [M5 §14], [M5 §12], [M5 §12.1]

## Slide 93 – Take-home   [14 Conclusion]   [Line: main]
**Lead:** Start early with an interpretable list that counts inactivity, test a model against it once, and let a randomised pilot decide whether contact helps.
**On the slide:** Three lines, large: Don't wait for missed tasks: under one in five non-completers had missed one by
week 4 (19.6% in 2013, 14.7% in 2014). Start simple, test once: the early-sign rule, with its signs as reasons beside
each name, is the list to beat; a model replaces it only by passing one gate fixed in advance. Prove it before scaling:
only a randomised pilot can show whether, and for whom, early contact improves completion. Take-home box: a missed task
comes too late; count silence too, and test contact before trusting it.
**Visual:** three numbered lines in large type, the first in orange, and the navy take-home box (none beyond type).
**Speaker notes:** So here is what we hope you take away. Do not wait for missed tasks: by week 4, fewer than one in five of the students who will fail or withdraw have missed one, so an early list has to look at whether students are still active. Start simple and test once: the early-sign rule is interpretable and computable from records the university already has, its signs give staff a reason beside every name, and a model replaces it only by passing one gate fixed in advance. And prove it before scaling: only a randomised pilot can tell us whether, and for whom, early contact improves completion. That is the question no open dataset can answer, and it is where this project hands over to the university.
**Sources:** [M5 §11.2], [M5 App XII Table A.31], [M5 §11.5], [M5 §14]

## Slide 94 – Thank You and Questions   [Closing]   [Line: main]
**Lead:** Thank you; we welcome your questions on any link of the chain, from the problem to the pilot.
**On the slide:** "Thank you. Questions?"; the project title and team N04; the take-home line: a missed task comes too
late; count silence too, and test contact before trusting it; the data credit: Open University Learning Analytics
Dataset (Kuzilek, Hlosta and Zdrahal), CC BY 4.0.
**Visual:** none (navy closing layout; the take-home line stays visible during questions).
**Speaker notes:** Thank you for following the chain with us: from students noticed too late, through open data and its preparation, methods fixed in advance and evidence on two years of runs, to the two questions we could answer and the two we have designed and kept for one honest test. Our report and its appendices hold every table behind the numbers you saw, with its population and interval, and the Final Project Package carries the code, the data access instructions, the pipeline, the data dictionary and the AI Decision Log, so anyone can rebuild our results from the public download. We are happy to take your questions on any link of the chain: the add-drop rule, the early signs, the gate, the fairness audit or the pilot.
**Sources:** [M5 §7.2], [M5 App XVI], [M5 §5] (data credit and licence)
