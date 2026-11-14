# Brief for the speech-script drafts (Milestone 5 final presentation, team N04)

**Talk.** About 25 minutes, exactly 30 slides, group talk by team N04 (MTH045 – The Science of Data Analytics,
University of Science, VNU-HCM). Audience: the lecturers (Dr. Nguyễn Trần Minh Thư, MSc. Phạm Minh Tú) and
classmates: analytically literate, not experts in this dataset. Title of the project: "Early Identification of
Disengaging Students in Online Courses". Members: Lê Ngọc Trúc Huỳnh, Phan Trần Khanh, Dương Tấn Huỳnh Phong.

**Story to tell.** The journey from the problem to the integrated answer, milestone by milestone:
- Milestone 1 – the problem and the requirement analysis (stakeholders, business goal, SMART goal, KPIs, decisions
  D1–D3, analytical questions AQ1–AQ4): `reports/milestone-1/report/*.md` (English files, not `*.vi.md`).
- Milestone 2 – data requirements, the open-dataset search and selection (OULAD), reproducible collection:
  `reports/milestone-2/report/*.md`.
- Milestone 3 – data understanding, quality findings, preparation, leakage controls, the prepared dataset:
  `reports/milestone-3/report/*.md`.
- Milestone 4 – modeling and evaluation design (Level 1): method per AQ, baselines, the early-sign rule, gate S1,
  fairness rule FR1, the frozen protocol: `reports/milestone-4/report/*.md`.
- Milestone 5 – the integration: what is now known, the Traceability Matrix, AQ1 and AQ2 answered on 2013 and 2014,
  AQ3 and AQ4 as designs with expected outputs, decision support, limitations, future work and the pilot, generative
  AI use: `reports/milestone-5/report/*.md` (main text 00-1 to 14-00; appendices 16-* for detail).
The Milestone 5 report is the source of truth for every number and status; earlier reports supply the story of how
each step was reached. Where a later milestone changed an earlier choice, tell the final choice and, briefly, why the
data forced it (e.g. the day-14 add-drop rule, the early-sign rule needing an activity part) — the Change Log
(Milestone 5 Appendix III, Table A.8) names these changes.

**Hard rules.**
1. Every number comes from the Milestone 5 report (or an earlier report when the Milestone 5 report repeats it);
   give its source section beside it in the draft (e.g. "[M5 §11.2]"). Never invent or round differently.
2. AQ3 and AQ4 are designs (Level 1): no model metric, no test result exists. Never mention any experiment,
   prototype run or trained model result. Results exist only for AQ1 and AQ2.
3. AQ2 results are associations, never causes; contact is an option to test in a pilot.
4. No repository paths, file names, internal IDs (claim or source IDs, task IDs) on slides or in notes.
5. Team voice: "we". Names appear only on the title slide.
6. Slide titles are short topic headings in plain words (not claims); the message goes in a one-sentence lead line.
   Every term is defined on the slide where it first appears; every chart has its key on the slide.
7. Flow problem → data → preparation → method → evidence → assessment → use → conclusions; each slide's notes open
   from the previous slide and hand over to the next. Closing: conclusions (firmest first), open problems /
   take-home, thank-you.

**Output format** (one Markdown file): a header with the big idea / core message and the arc; then for each of the
30 slides:

```
## Slide N – <Title>   [part label]   (~NN seconds)
**Lead:** <one sentence>
**On the slide:** <short complete clauses, cards, table or numbers that appear on the slide>
**Visual:** <the visual and why: sequence / structure / comparison-trend / worked example; or "none">
**Speaker notes:** <what we say, spoken register, 90–140 words; opens from the previous slide, ends with the hand-over>
**Sources:** <report sections behind every number>
```
