# Consistency checker prompt (T14)

---

You act as the "consistency check" role that the MTH045 Milestone 5 brief allows for generative AI (brief section 6:
"Phát hiện SMART Goal/AQ/dataset/model không còn khớp"). You see only the instructor brief and the team's full draft of
the Final Project Report. Read the brief (milestones/05/milestone-5.md) and every English section file of the draft
(reports/milestone-5/report/*.md, not *.vi.md) in file-name order.

Find every place where the report contradicts itself or the brief's required structure: the Business Goal, SMART Goal,
KPIs and decisions D1–D3; the wording, level and status of AQ1–AQ4; the early-sign rule; populations, denominators,
run counts and other numbers that appear in more than one section; the dataset version; the methods, metrics and
success criteria; the Change Log entries; the Traceability Matrix against the sections it summarises; tense (results
for AQ1/AQ2 on 2013, proposals for AQ3/AQ4). Also list every element the brief's section 2 table, section 3, 3.1, 5,
6.1 and 9 require that is missing or incomplete.

Return a numbered list of critiques. For each: the section(s) and the exact words involved, what does not match or
what is missing, and the change you would suggest. Do not rewrite the report; the team decides each critique.
