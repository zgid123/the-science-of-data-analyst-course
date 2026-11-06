## Appendix IV – AI Critique, Team Decisions and Reviewer Prompt

An isolated AI reviewer read the brief and Sections 1–7 with the prompt below and returned twelve critiques. Table A.13 gives each critique in short form, the team's decision and the reason or change; Section 8 discusses three of them.

**Table A.13. AI critique, team decision and reason**

| No. | AI critique | Team decision | Reason or change |
| :---- | :---- | :---- | :---- |
| R1 | AQ3 data cut-off contradicts Table 6.2 | Accepted | Cut-offs end of week 2 and week 4; lists delivered in weeks 3 and 5 (Sections 4.1, 4.2, 6.1 and 6.2) |
| R2 | Secondary KPI 1 uses an end-of-semester denominator that falls when contact works; week 6 matches no review point | Accepted | Replaced by the early-sign contact rate (Section 3.3) |
| R3 | D3 has no analytic path; no traceability matrix | Partly accepted | D3 rests on AQ1 and the KPIs repeated for pilot and comparison courses; causal effect left to the Milestone 4 evaluation plan (Sections 5 and 7). The matrix is Section 9, which the reviewer did not receive |
| R4 | SMART population and aggregation unclear | Accepted | Pilot courses fixed before the pilot, pooled rate, comparison courses (Section 3.2) |
| R5 | Achievable criterion acknowledged, not argued | Accepted | Added the reasoning that five more passes per 100 enrolments means helping one in six of the 30 non-completers to finish, and that pilot size fits weekly capacity (Section 3.2) |
| R6 | AQ4 objective counterfactual, limits without values, capacity figures differ | Accepted | Objective on likelihood of non-completion; precision of at least 50% and first-year recall within ten points of later-year recall, both as assumptions; referral destination; 30–40 everywhere (Sections 2.3 and 4.1) |
| R7 | AQ3 metric and threshold undefined; training data unclear | Accepted | Recall and precision at capacity length; D1 threshold = higher recall than the simple rule; training on earlier semesters of the course, or on the current course's submitted assessments when no earlier semester exists (Sections 4.1, 4.2 and 7) |
| R8 | Primary KPI counting rule unclear | Accepted | Course withdrawal and fail count as non-completion; leave and transfers leave the denominator (Section 3.3) |
| R9 | AQ1 compound and one-sided; period unclear | Partly accepted | Timing compared for both groups; period named as 2024–2025 and 2025–2026; one question kept, because timing and outcome describe the same enrolments |
| R10 | AQ2 "differ most" undefined; attendance absent in online courses | Accepted | Difference in later non-completion rates; attendance for blended courses only; weeks 1–4 (Sections 4.1 and 6.1) |
| R11 | Business Goal contains the means | Not accepted | The brief's own "better" example is "Nhận diện sớm sinh viên có nguy cơ không hoàn thành để hỗ trợ kịp thời" (identify early the students at risk of not completing, to support them in time); the goal leads with the outcome and names the timing that stakeholders asked for (PM1, AD1) |
| R12 | Persona caseload (300) and scenario capacity (4,000 for 3) unexplained | Accepted | Section 2.2 states that published figures shape the persona and the persona's own estimates drive capacity |

The reviewer prompt, with documents named by their place in this report:

```text
You are a reviewer of a student team's analytics project proposal for the course MTH045 – The Science of Data
Analytics. Read the instructor brief and Sections 1–7 of the proposal (English). Do not read any other
document.

Review the proposal as the brief's reviewer would. Check in particular:
1. SMART: is the SMART Goal specific, measurable, achievable, relevant and time-bound; are baselines and targets
   labelled as assumptions?
2. KPIs: one primary and at most two secondary; does each have a rationale and track the SMART Goal?
3. Analytical questions: are AQ1–AQ4 clear, specific, scoped, data-oriented and answerable; does the diagnostic
   question avoid causal language; does the predictive question state target, unit, horizon and data cut-off; does the
   prescriptive question state the decision, the action alternatives, the objective and the constraints?
4. Traceability: does each step follow from the previous one (stakeholder needs → Business Goal → SMART → KPI → AQ →
   analytics type → technique family → data → decision)?
5. Scope: does the proposal stay within Milestone 1 (no dataset analysis, no fixed algorithm)?
6. Anything vague, contradictory, unsupported or likely to confuse a reader.

Do not rewrite the proposal and do not propose new analytical questions of your own. Return a numbered list of at
most 12 critiques. For each: the section and sentence concerned (quote a few words), the problem, and why it matters.
Order them from most to least important.
```
