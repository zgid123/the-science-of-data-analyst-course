# Milestone 1 revision: full draft, then move to appendix (2026-11-07)

User instruction (2026-11-07): the condensed reports are hard to understand. Write the complete report without a
length limit, then reach the length by reasoning about which information moves to an appendix, never by condensing
sentences until they lose meaning. User decision (AskUserQuestion, 2026-11-07): target about 12–13 pages of main
content; remove repetition between sections; keep every brief-required element readable in the main text.

## Rule applied to every block

The main text keeps (1) every element that the brief's Section 6 table lists for a section, (2) the result of each
step stated in full sentences, (3) the definition of every term the main text uses, and (4) one reason for each key
choice. A block moves to an appendix when it is a derivation, an evidence list, a per-item detail table or a
background definition whose result the main text can state in full sentences. Each moved block leaves a summary and a
pointer naming the appendix (and table) that holds it.

## Measurements (code/estimate_parts.py, line model of build-report)

| Stage | Main content (Parts 1–9) | Log |
| :---- | :---- | :---- |
| Condensed version (before this revision) | 11.2 pages, 5,973 words | research/revision/condensed-2026-11-07/ |
| Full draft, no length limit | 20.4 pages, 12,272 words | logs/R1_full_draft_pages.log, R1_full_draft_blocks.log |
| Move 1: evidence, interview method, synthesis tables, AQ specification, technique rationale, framework definitions | 17.3 pages | logs/R2_move1_pages.log |
| Move 2: part introductions cut to signposts; SMART and KPI tables; data-source descriptions | 16.6 pages | logs/R3_move2_pages.log, R3_move2_blocks.log |
| Move 3: conflicts table; validation details | 16.2 pages, 9,603 words | logs/R4_move3_pages.log |
| Move 4: repetition removed (capacity, cut-offs, causal caveat); risk table; framework paragraph shortened | 16.0 pages | logs/R5_move4_pages.log |
| Move 5: out-of-scope reasons; interview approach; AQ explanations merged into one paragraph; SMART timeline; contact record defined once | 15.1 pages | logs/R6_move5_pages.log |

## Blocks moved

| Block (main text) | Moved to | Main text keeps | Reason |
| :---- | :---- | :---- | :---- |
| 1.1 How common / when / why non-completion (330 words) | Appendix V | One paragraph with every finding and citation [5]–[10] | Background evidence; the argument needs the findings, not the study detail |
| 2.2 Steps 1–4 of the interview method | Appendix VI §1 | Procedure, persona sources [12]–[18], questions, labels with definitions | Method detail; the brief needs the interview approach, which the summary states |
| 2.3 Organise table (brief Task 4 table) | Appendix VI §2, Table A.14 | Themes table with what was said, who raised it and priority | The themes are the synthesis; the organised input is its working step |
| 2.3 Priority scoring table | Appendix VI §3, Table A.15 | Priority column and a paragraph on why T1–T3 are core | Scoring detail; the priorities and reasons stay |
| 1.2 / 2.3 out-of-scope reasons | Appendix VI §4 | One sentence listing every exclusion | Each reason is detail; the scope itself stays |
| 2.4 Conflicts table | Appendix VI §5, Table A.16 | Paragraph naming the four conflicts, their statements and resolutions; review point defined | The resolutions shape the proposal and stay; the two-sided statements are detail |
| 2.4 Validation table (brief Task 4 table) | Appendix VI §6, Table A.17 | Paragraph on what was confirmed, corrected and added; the three suggestions not adopted with reasons | The brief places validation evidence in the appendix (brief section 9) |
| 3.2 SMART five-criteria table | Appendix VII, Table A.18 | Achievable and relevant arguments in prose | The argument stays; the criterion-by-criterion table is a check |
| 3.3 KPI summary table | Appendix VII, Table A.19 | Each KPI's definition, reason, timing and source in prose | The table repeated the prose |
| 4.1 Element-by-element specification of each AQ | Appendix VIII | Each AQ in full; one paragraph on how the questions connect, with unit, data cut-offs, recall, precision and the two limits | The questions and their definitions stay; the per-level checklist is detail |
| 5 Rationale for each technique family | Appendix IX §1 | The three choices that shape the approach | Detail behind Table 5.1 |
| 6.1 Description of each data source | Appendix IX §2 | The four sources named, with the linking problem (DO1) | Detail behind Table 6.1 |
| 6.2 Data quality risk table | Appendix IX §2, Table A.20 | Every risk with its handling, in prose | The prose states the full result |
| 7 Full definitions of the three classifications | Appendix IX §3 | One sentence per classification with citations | Background definitions |

## Not moved, with reason

- Table 2.1 stakeholder map, Table 4.1 quality check, Table 4.2 Before → After, Table 5.1, Table 6.1, Table 7.1,
  Table 9.1: listed by the brief as main-text content.
- Table 8.1 (AI roles): a full-sentence summary is as long as the table, so moving it saves nothing.
- Section 8's accepted and rejected critiques, and Section 2.4's three suggestions not adopted: the brief asks the
  main text to show which AI suggestions the team accepted or rejected and why.

## Reader test and fixes

An independent reader (fresh agent, reading only the built Word document) returned 21 items. Fixed: capacity figures
now cite the statements that give them (new VAD6, VAD7); "advisor" split into the support officer (AD persona) and the
lecturer-advisor; scope reasons restored to Section 1.2; pilot size (about four courses, about 600 enrolments,
assumption) and the 2027–2028 pooled target; D1 evidence wording; review points moved out of registration and exam
weeks; R12 pointer; codes explained at first use; KPI 1 counting rule; OULAD coverage of AQ1–AQ3; "the program"
defined; student affairs office glossed; DO1 scope of linking; priority labels; constraint versus conflict; wording.
Not changed: the follow-ups of the AI interviewer (no claim the team cannot verify), process wording inside the AI
evidence appendix (it is evidence), and length (decided). Main content after fixes: 15.6 pages (logs/R8_pages.log).

## Result against the agreed target

The main content is 15.1 pages, above the agreed 12–13: removing repetition saved about 1 page, not the 3 pages
estimated when the option was offered. The remaining blocks are brief-required content; shrinking them further would
mean condensing sentences again.
