# Brief for the full speech-script drafts (Milestone 5 final presentation, team N04)

**Talk.** Group talk by team N04 (MTH045 – The Science of Data Analytics, University of Science, VNU-HCM), project
"Early Identification of Disengaging Students in Online Courses". Audience: the lecturers (Dr. Nguyễn Trần Minh Thư,
MSc. Phạm Minh Tú) and classmates: analytically literate (rates, intervals, logistic regression, recall), new to OULAD
and to our five reports. Members, with master's student IDs: 25C12002 – Lê Ngọc Trúc Huỳnh, 25C12003 – Phan Trần
Khanh, 25C12031 – Dương Tấn Huỳnh Phong.

**This draft is the full version.** There is **no limit on the number of slides and no time limit**. Write the
complete, comprehensive deck: every step of the journey from the problem to the integrated answer, every piece of
evidence the course brief requires, each on its own slide when it needs one. Do not merge two ideas onto one slide to
save space, and do not cut a slide because the talk would be long. A later step moves detail slides to an appendix
section at the end of the deck; that step needs every slide written out in full first. Still keep one idea per slide.

**Coverage the full deck must reach.** The course brief (milestones/05/milestone-5.md, section 2) lists the parts of
the final report and the evidence each must show; the deck covers every one of them:
Abstract / executive summary; 1 Introduction and educational context (context, motivation, stakeholders, scope,
objective); 2 Business understanding and success criteria (Business Goal, SMART Goal, primary and secondary KPIs,
decision needs D1–D3); 3 Analytical questions and analytics levels (final AQ1–AQ4, levels, scope, decision supported,
AQ quality check, AQ revision status); 4 Data requirements and dataset selection (unit of analysis, outcome,
concepts, time, population, candidate datasets, selection rationale, provenance and licence; Data Requirement
Matrix); 5 Dataset description and requirement–data fit (tables, keys, coverage, gaps, AQ status keep/modify/defer;
data dictionary and AQ–Data Fit Matrix); 6 Data understanding and quality (distribution, missingness, duplicates,
invalids, outliers, imbalance, temporal coverage, representativeness, sensitive fields); 7 Data preparation
(cleaning, transformations, joins, derived variables, encoding, missing handling, leakage control, final versioned
dataset; Preparation Decision Matrix); 8 Modeling and analysis strategy (AQ → analytics type → task → baseline →
candidate families → primary proposal → rationale; Method Selection Matrix); 9 Evaluation design (metric, baseline,
split and validation, success criterion, leakage, fairness and interpretability checks); 10 Experimental status
(Level 2 not run, and why); 11 Findings, discussion and decision support (AQ-by-AQ answers, the Final Project
Traceability Matrix, decision support for D1–D3); 12 Limitations and future work (limitation log, deferred AQs, next
data needed, the pilot); 13 Generative AI use and reflection (AI decision log: used for, verification,
accepted/rejected, final human decision); 14 Conclusion.

**Sources.** The Milestone 5 report is the source of truth for every number and status:
`reports/milestone-5/report/*.md` (English files only, not `*.vi.md`; main text 00-1 to 14-00, appendices 16-* hold
the detail tables and the full results). Earlier reports give the story of how each step was reached:
`reports/milestone-1/report/*.md` … `reports/milestone-4/report/*.md`. Where a later milestone changed an earlier
choice, tell the final choice and briefly why the data forced it (Milestone 5 Appendix III, Table A.8 names these
changes: the day-14 add-drop rule, the early-sign rule needing an activity part, and others).

**Hard rules.**
1. Every number comes from the Milestone 5 report (or an earlier report when the Milestone 5 report repeats it); give
   its source section beside it (e.g. "[M5 §11.2]", "[M5 App XII Table A.32]"). Never invent, never round
   differently.
2. AQ3 and AQ4 are designs (Level 1): no model metric and no test result exists. Never mention an experiment,
   prototype run or trained-model result. Results exist only for AQ1 and AQ2.
3. AQ2 results are associations, never causes; contact is an option to test in a pilot.
4. The stakeholder interviews were simulated with AI on both sides; they motivate the design and are never evidence.
5. No repository paths, file names or internal IDs (claim IDs, source IDs, task IDs) on slides or in notes.
6. Team voice: "we". Names appear only on the title slide.
7. Slide titles are short topic headings in plain words; the message goes in a one-sentence lead. Every term,
   abbreviation and identifier (D1–D3, AQ1–AQ4, S1, FR1, TMA, CMA, KPI, OULAD) is defined on the slide where it
   appears, so each slide reads on its own; every chart or diagram has its key on the slide.
8. Flow: problem → data → preparation → method → evidence → assessment → use → conclusions. Each slide's notes open
   from the previous slide and hand over to the next. Close with conclusions (firmest first), limitations and open
   problems, take-home, thank-you / questions.

**Output format** (one Markdown file, English). A header with the method used, the big idea (core message), the arc,
and a coverage table that maps each brief part above to the slide numbers that cover it. Then, for every slide:

```
## Slide N – <Title>   [part label]   [Line: main | detail]
**Lead:** <one sentence>
**On the slide:** <complete short clauses, cards, a table (rows written out) or numbers that appear on the slide>
**Visual:** <the visual and why: sequence / structure / comparison / trend / worked example / table; or "none">
**Speaker notes:** <what we say, spoken register, 90–140 words; opens from the previous slide, ends with the hand-over>
**Sources:** <report sections behind every number>
```

`Line: main` marks a slide the story cannot do without; `Line: detail` marks a slide that carries evidence a reader
may want but the spoken story can point to. This is a suggestion for the later appendix step, not a cut: write every
slide in full either way.
