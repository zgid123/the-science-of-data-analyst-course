# Part 9 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 09-00-ethics-limitations.md

**Claims:** C9-001, C9-002, C9-003, C9-004, C9-005, C9-006, C9-007, C9-008, C9-009, C9-010, C9-011, C9-012, C9-013, C9-014, C9-015

**Outline:**
- Why keep sensitive attributes: bias is defined as a performance gap between groups (C9-001), it can arise through proxies even when demographics are not inputs (C9-002), and without group membership a model cannot be audited at all (C9-003, S901).
- Which groups: the literature checks gender, race/ethnicity and nationality most, with socioeconomic status and disability less studied (C9-004); in OULAD the available attributes are gender, disability, age band, IMD band and region.
- Evidence on OULAD: Riazy et al. audited gender and declared disability; disability is strongly under-represented (C9-006); gender disparity is reproduced (C9-007); removing the attributes barely helps and costs accuracy (C9-008); under-represented groups behave erratically (C9-009); check balance before modelling (C9-010).
- Privacy: re-identification risk in small groups and different legal protection of disability data (C9-005).
- Vietnamese legal frame: Law 91/2025/QH15 defines sensitive personal data, in force 1 January 2026 (C9-011); health information is a sensitive example and gender a basic one (C9-012, briefing); de-identified data are not personal data and re-identification is barred (C9-013); no named research or statistics exemption from consent (C9-014); purpose limitation (C9-015).

**Conflicts with the outline:** None with the outline text. Note for the human: Baker and Hawn (S901) summarise Riazy's disability finding as over-prediction of success, while Riazy's own conclusion (S902, C9-009) says students with declared disabilities were in some cases predicted to fail with higher probability; the report should quote Riazy directly.

**Gaps:** Whether disability status counts as sensitive (health) data depends on the implementing decree (reported as Decree 356/2025/NĐ-CP), not fetched. Gardner et al. (2019, LAK) slicing analysis / ABROCA is cited only through S901 and S902. Riazy used random splits, so their accuracy figures are not comparable with the team's time split. Age band and IMD band have no OULAD fairness evidence on disk.
