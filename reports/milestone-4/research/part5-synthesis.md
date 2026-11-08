# Part 5 Synthesis

One entry per planned report file: the claim IDs that feed it, the paragraph outline, the conflicts with the outline and the open gaps.

## 05-00-risk-ethics.md

**Claims:** C5-031, C5-025, C5-022, C5-030, C5-044, C5-053, C5-055, C5-032

**Outline:**
- Frame Part 5 with a risk-management lens: the four NIST AI RMF functions (govern, map, measure, manage) as the structure of the section (C5-031).
- State why the early-warning model counts as high-stakes use: EU AI Act Annex III point 3 and Article 14 (C5-022, C5-025), application date after the Digital Omnibus (C5-030).
- State the Vietnamese frame for transfer to the university: AI Law in force 1 March 2026 and Personal Data Protection Law in force 1 January 2026 (C5-044, C5-053); de-identified OULAD versus identifiable university data (C5-055).
- Close with the monitoring obligation that runs through the rest of the part (C5-032).

**Conflicts with the outline:**
- The outline's sources for regulation are the EU AI Act and NIST only; as of November 2026 Vietnam has its own AI Law (134/2025/QH15), Decree 142/2026/NĐ-CP and Decision 33/2026/QĐ-TTg, which are the rules that apply to a Vietnamese university (extends the outline; human to decide how much weight to give the EU text).

**Gaps:** The decree and Decision 33/2026/QĐ-TTg were read through official or state-media notices, not their own texts.

## 05-01-leakage-interpretability.md

**Claims:** C5-033, C5-034, C5-035

**Outline:**
- Documentation as part of interpretability: a model card for the early-warning model (intended use: ranking for tutor contact; out-of-scope: grading, sanctions) with metrics by group (C5-033, C5-034).
- A datasheet for the prepared dataset OULAD-N04-prepared-1.0 (C5-035).
- Leakage, overfitting and test reuse are T06's evidence (Part 4); this task adds only the documentation sources.

**Conflicts with the outline:** None.

**Gaps:** Leakage and interpretability-method sources are outside T07 (T05/T06).

## 05-02-causal-fairness-use.md

**Claims:** C5-001, C5-002, C5-003, C5-004, C5-009, C5-005, C5-006, C5-007, C5-008, C5-010, C5-011, C5-012, C5-013, C5-014, C5-015, C5-016, C5-018, C5-019, C5-020, C5-021, C5-017, C5-022, C5-023, C5-024, C5-025, C5-026, C5-027, C5-028, C5-029, C5-030, C5-044, C5-045, C5-046, C5-047, C5-048, C5-049, C5-050, C5-051, C5-052, C5-053, C5-054, C5-055, C5-036, C5-037, C5-038, C5-039, C5-040, C5-041, C5-042, C5-043, C5-056, C5-057, C5-058, C5-032, C5-033

**Outline:**
- Causal limits: the model ranks risk; the effect of contact needs a randomised or target-trial design with time zero at the cut-off and a treatment variable OULAD lacks (C5-001 to C5-006, C5-009); risk ranking is not benefit ranking (C5-007, C5-008), so the contact decision (AQ4) stays deferred and a randomised contact pilot is the recommended next step.
- Fairness: criteria conflict when non-completion rates differ by group (C5-010 to C5-014); separation as the primary audit criterion for a supportive intervention (C5-015); unawareness does not remove bias (C5-016); audit groups in OULAD and expected instability for small groups (C5-018 to C5-021), with toolkits (C5-017).
- High-stakes use and human oversight: EU AI Act Annex III point 3 and the profiling rule (C5-022 to C5-024), Article 14 oversight, automation bias and override (C5-025 to C5-027), deployer duties and explanation right (C5-028, C5-029), dates (C5-030).
- Vietnam: AI Law principles, education as a stricter-risk sector, provider and deployer duties, dates (C5-044 to C5-049); Decision 33/2026/QĐ-TTg education entries (ranking learners, analysing learner behaviour) and deadline 1 September 2027 (C5-050, C5-051); decree (C5-052); personal data law (C5-053 to C5-055).
- Institutional practice: risk labels lead to support and stay revisable (C5-036, C5-037); Jisc code on labelling and review (C5-038, C5-039); OU scale versus human intermediation (C5-040); OU Responsible AI Policy (C5-041 to C5-043).
- Feedback and monitoring: performative prediction; log contacts with outcomes before retraining (C5-056 to C5-058); ongoing monitoring (C5-032) and model card (C5-033).

**Conflicts with the outline:**
- Task card names "OU policy on ethical use of student data for learning analytics": that 2014 policy is superseded; the current OU document is the Responsible AI Policy V1.3 (October 2025), which replaces the Data Ethics Policy (S522).
- EU AI Act: Annex III point 3 does not name dropout or early-warning prediction; such a model is high-risk only through point 3(b) (evaluating learning outcomes or steering learning) or as profiling under Article 6(3); the Annex III obligations apply from 2 December 2027 after Regulation (EU) 2026/1744, not 2 August 2026. The outline's "high-stakes use" label holds as a design assumption; the legal classification is for the university.
- Vietnam: Decision 33/2026/QĐ-TTg lists AI that ranks learners or analyses learner behaviour as high-risk, so a deployed early-warning ranking at a Vietnamese university is likely high-risk (team reading, not a ruling).

**Gaps:** Kohavi et al. 2020 (Trustworthy Online Controlled Experiments) not read (no open copy); Ascarza 2018 read from the abstract only; the current Jisc code (2018) not readable (S520 blocked; S523 used); Decree 142/2026/NĐ-CP Article 8(2) exclusions and Decree 356/2025/NĐ-CP (data protection) not read; EU text read from the AI Act Explorer, not EUR-Lex.
