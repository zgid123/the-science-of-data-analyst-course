# Milestone 2 report outline: from requirements to collection (team N04)

Derived on 2026-11-06 from the instructor brief `final-project/milestones/02/milestone-2.md` [1], which fixes the
steps (section 4), Tasks 1–7 (sections 5–11), the AI rules (section 12), the deliverables (section 15) and the report
structure (section 15.1). The baseline is the team's Milestone 1 proposal in `reports/milestone-1/report/`.

## Scope and rules

- Requirements decide the data: each AQ of Milestone 1 becomes a data requirement before any dataset is looked at;
  data never rewrites the goals. Gaps are recorded and any change to Milestone 1 goes into a Controlled Change Log.
- Search at least three open education datasets from verifiable sources, read documentation and licenses first, log
  every query; score every candidate on the same criteria with must-have gates.
- Acquire reproducibly: raw files unchanged, source URL, access date, version, license, SHA-256 checksums, citation.
- Initial structural verification only (files, rows, columns, keys, types, target and time fields, differences with
  the documentation); no cleaning, imputation, feature engineering or modelling. Results of the OULAD exploration
  (`datasets/oulad/exploration/`) may support statements where needed; Milestone 2 reports structure, not analysis.
- Coverage per AQ: Full / Partial / None, with real file and variable names only.
- AI as search strategist, metadata interpreter, requirement critic, selection reviewer and documentation assistant;
  every dataset fact verified on the official source.
- Length: 6–10 pages of main content, appendices excluded. English source, Vietnamese twin.

## 1. Milestone 1 Baseline and Scope

- Business Goal, SMART Goal and KPIs, AQ ladder, analytics types, decisions; frozen baseline; Change Log summary.

## 2. Data Requirement Specification

- AQ–Data Requirement Matrix; unit, target/measure, features, time and granularity, availability timing,
  sensitivity; requirements per analytics level; prediction point and leakage table (Tasks 1–2).

## 3. Open Dataset Search Strategy

- Keywords from the AQs, sources searched, search log, at least three candidates (Task 3).

## 4. Dataset Evaluation and Selection

- Criteria, must-have gates, selection matrix, rationale, limits (Task 4).

## 5. Data Acquisition and Provenance

- Provider, URL/DOI, version, access date, license, citation, files, checksums, reproducible collection (Task 5).

## 6. Initial Structural Verification

- Files and tables, shape, schema, identifiers, target and time fields, differences from the documentation (Task 6).

## 7. Requirement Coverage and Data Gaps

- Updated traceability matrix with Full / Partial / None; gap handling; controlled revisions (Task 7).

## 8. Risks, Ethics and Limitations

- Privacy, sensitive attributes, representativeness, generalisation, claims the data cannot support.

## 9. Generative AI Usage and Reflection

- AI roles, what was accepted or rejected, how dataset facts were verified.

## Appendices

- Search log; scoring details; acquisition plan and Data Collection Package; structural verification details and
  data dictionary check; Controlled Change Log; AI usage evidence.

## References

1. MTH045 – The Science of Data Analytics. (2026). Milestone P2: From requirements to collection [Course brief].
   final-project/milestones/02/milestone-2.md
