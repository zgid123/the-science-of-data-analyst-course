"""Reproduction, analytical gate and rubric evidence for each remaining study."""
from pathlib import Path
import sys,json
import pandas as pd
from delivery import BASE
DETAIL={
'fff':dict(status='Complete retrospective analysis within the first-attempt FFF scope; live timing remains conditional',files='Five corresponding analysis CSVs in datasets/fff/ and datasets/oulad/ (the latter verifies exact source overlap). VLE logs are not required.',extra='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/remaining-study-env/bin/python samples/fff/code/followup.py\n/tmp/remaining-study-env/bin/python samples/fff/code/supplement.py',source='OULAD creator documentation and UCI; source FFF subset is verified against the parent rather than treated as independent evidence.',entities='Source keys, banked-credit exclusions, split separation, 61 cutoff/denominator checks and independent full test-row raw reconciliation; parent_overlap.csv verifies all five tables.',depth='Separate future failure/withdrawal, day 30/60/90, score/behavior/rule baselines, delay/target/common-survivor sensitivities and paired AP intervals.',tasks=[('behavior','Missing due records and outcome-specific differences'),('models','Added behavior value, paired uncertainty and the constant-module baseline'),('workload','Validation threshold versus actual later-cohort review load'),('timing','Eligibility and withdrawal lead time versus course-end proxy'),('sensitivity','Release/logging/target/common-survivor challenges'),('audit','Demographic/outcome errors and calibration')]),
'ednet':dict(status='Partial against the broad academic-risk objective; completed sampled practice-underperformance investigation',files='datasets/ednet/ednet_kt1.zip and contents/questions.csv. The archive supplies the complete user sampling frame; extracted KT1 files are not individually listed or scanned.',extra='OPENBLAS_NUM_THREADS=1 /tmp/remaining-study-env/bin/python samples/ednet/code/verify.py',source='EdNet creators’ GitHub schema; archive central-directory fingerprint and sampled-member CRC validation; official TOEIC/course outcomes are not present.',entities='Unique question IDs, no invalid/unmatched sampled responses, prefix/outcome temporal nonoverlap, one split per user and direct AP/raw-window verification.',depth='Behavior versus score versus combined/rules, paired AP intervals, two random test sample halves, future-part audit, novel-item and target-threshold challenges, short lead-time accounting.',tasks=[('coverage','Continuing-user label coverage and selection'),('models','Whether added behavior value is demonstrated'),('timing','Next-question seconds versus entire future-window days'),('workload','False positives and missed later low accuracy'),('sensitivity','Novel questions, alternate proxy and sample instability'),('audit','Content errors and probability reliability')]),
'mooccubex':dict(status='Feasibility assessment with completed assessment-content investigation; no student-risk validation',files='Local datasets/mooccubex/data/entities/course.json and relevant relation JSONL/TXT files, plus local course/user documentation. See source_manifest.csv for actual analysis inputs; no missing upstream student logs are downloaded.',extra='',source='Local upstream documentation verifies exercise-container/problem namespaces and missing event/link files; all relevant local content is read.',entities='Course key uniqueness, resource decomposition, relation parsing, duplicate-edge accounting and matched/unmatched manual-field joins.',depth='Opportunity distribution rather than mean alone, semantic linkage limits, manual-label coverage sensitivity, unmatched course IDs and edge duplication.',tasks=[('gaps','Exact missing student event/outcome/mapping evidence'),('opportunities','Distribution of course exercise opportunities'),('linkage','Why concept overlap cannot establish student obligations'),('fields','Manual-label bias and unmatched-course coverage'),('quality','Repeated relations and help-query limits')]),
'college-scorecard':dict(status='Feasibility assessment with completed aggregate academic-outcome suitability investigation',files='Both Most-Recent-Cohorts Institution and Field-of-Study CSVs under datasets/college-scorecard/. All rows read with selected columns; no new release downloaded.',extra='',source='U.S. Department of Education official methodology text verified through indexed official excerpts; direct PDF returned 403. Exact local per-field cohort vintage remains unverified.',entities='Unique institution/program compound keys, valid rate ranges, distinct reporting cohorts, outcome-specific denominators and independent weighted completion recomputation.',depth='Institution versus cohort-weighted estimands, sector/size differences, minimum-cohort sensitivities, suppressed pooled versus non-pooled outcomes, ecological pairing limits.',tasks=[('definitions','Completion versus retention reporting populations'),('weights','Institution versus cohort-weighted interpretation'),('small','Consequences of small cohort restrictions'),('cohorts','Why same institution is not a longitudinal student link'),('suppression','Missing tokens and reporting-family limits'),('grain','Program grain and absent student warning evidence')]),
'pisa-2022':dict(status='Feasibility assessment with completed assessment-practice contextual investigation',files='CY08MSP_SCH_QQQ.SAV, CY08MSP_TCH_QQQ.SAV, escs_trend.csv and ReadMe.txt under datasets/pisa-2022/. SPSS embedded labels are the substantive codebook.',extra='OPENBLAS_NUM_THREADS=1 /tmp/remaining-study-env/bin/python samples/_shared/verify_survey.py pisa-2022',source='Embedded SPSS labels, local historical ESCS ReadMe and OECD technical replication methodology; teacher versus school populations and weights are separated.',entities='School/teacher key uniqueness, respondent reconciliation, actual historical trend cycles, final teacher weights/80 BRR replicates and independent scalar rate/SE verification.',depth='Within-domain paired feedback contrasts, school recording/test-use context, conditional assessment-training need, valid-code/missingness and teacher-type/weight comparisons.',tasks=[('feedback','Reported written/immediate feedback and assessment need'),('paired','Common-respondent feedback contrast with covariance'),('schools','Recording policy versus actual student histories'),('needs','Conditional training need, with causal limits'),('coverage','Optional teacher domains and historical export years')]),
'talis-2024':dict(status='Feasibility assessment with completed country/level assessment-practice contextual investigation',files='a/b/c teacher and principal CSVs plus ttg combined export and supplied teacher ZIP in datasets/talis-2024/. Level teacher extracts are used once, not concatenated with their combined duplicate.',extra='OPENBLAS_NUM_THREADS=1 /tmp/remaining-study-env/bin/python samples/_shared/verify_survey.py talis-2024',source='OECD master questionnaire for item meanings, user guide for BRR/adjudication and technical notes for final weighting/rotation; source URLs are in REPORT.md.',entities='Teacher-population keys, CRC archive matches, exact combined-versus-level selected-item equality, final weights/100 BRR replicates and independent scalar rate/SE verification.',depth='Assessment/feedback/self-assessment/digital practice, training need, common-response feedback differences, conditional need/practice association and observed form-design missingness.',tasks=[('practices','Assessment methods, valid denominators and adjudication'),('paired','Common-response paired feedback contrast'),('needs','Why frequent feedback can coexist with training needs'),('forms','Rotated-form absence versus invalid zero-coding')])}

for name in sys.argv[1:] or DETAIL:
 r=BASE/'samples'/name;d=DETAIL[name]
 command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/remaining-study-env/bin/python samples/'+name+'/code/analyze.py'
 extra=('\n'+d['extra']) if d['extra'] else ''
 readme=f'''# {name}: assessment behavior and early academic risk

[Open the rendered report](report.html) · [Open the interactive local dashboard](dashboard/index.html) · [Analytical review](QUALITY_REVIEW.md)

**Status:** {d['status']}. This executes the user's generic prompt for this dataset. All inferred cutoffs, target proxies and capacities are explicitly proposed. No intervention or stakeholder approval is claimed.

Open `report.html` or `dashboard/index.html` directly in a browser; they work offline with no server or hosted service. Markdown/CSV are supporting source/download artifacts. Outputs are static; rerun to refresh. No individually identifiable records are displayed.

## Reproduce from final-project/

```bash
python3 -m venv /tmp/remaining-study-env
/tmp/remaining-study-env/bin/pip install -r samples/requirements.txt
{command}{extra}
/tmp/remaining-study-env/bin/python samples/{name}/code/build.py
/tmp/remaining-study-env/bin/playwright install chromium
/tmp/remaining-study-env/bin/python samples/_shared/review_remaining.py {name}
```

Actual execution used `/tmp/oulad-venv/`; installed versions are saved in `samples/_shared/environment.txt`. Installing Chromium is necessary only for verification, not opening the dashboard. On systems missing browser libraries, Playwright's `install --with-deps chromium` may be needed.

Dataset requirements: {d['files']}

Source semantics/provenance: {d['source']} Original acquisition times and local release vintages are not invented. Raw data is preserved; SHA-256 manifests identify analyzed inputs. EdNet additionally records the full archive user-frame fingerprint, sample seed and selected member CRCs in ignored prepared data.

## Files

- `BRIEF.md`: proposed questions, analytical contract, definitions and acceptance before evaluation.
- `code/`: dataset-specific reproducible preparation/analysis and build entry point; shared rendering/survey helpers are in `samples/_shared/`.
- `results/`: saved aggregate evidence, numerical ledger and explicit unavailable-evidence boundaries.
- `prepared/`: local derived enrollment/user data where needed, ignored by Git; not published.
- `REPORT.md` / `report.html`: source-format and rendered finding-led report.
- `dashboard/index.html`: question-specific interactive views, with visible filter scope and empty states.
- `evidence/`: actual pipeline/independent/browser logs and screenshots.
- `QUALITY_REVIEW.md` / `PROCESS.md`: criterion evidence, reader paths, corrective work and remaining limits.

Question coverage and interpretation belong to this study's report; success on a proxy/contextual question does not establish student academic-warning validity. Prior holdout reuse outside this run is unknown for the predictive studies. No additional dataset acquisition or real-world outreach occurred.
'''
 (r/'README.md').write_text(readme)
 review=f'''# {name}: analytical quality and interface review

Analysis status: **{d['status']}**. Delivery status: **NOT VERIFIED until the final browser and visual review below passes**. This is an author/reviewer walkthrough, not blind independent review or actual user testing. Stakeholder acceptance is PENDING. No intervention exists; outcome evaluation is NOT APPLICABLE.

Scores use the installed skill's 0 missing/misleading, 1 superficial, 2 adequate, 3 strong anchors. All criteria below are material to this declared scope. A feasibility/contextual scope can be adequate as such while the broader individual warning aim remains unsupported; scores do not turn missing student evidence into successful prediction.

| Dimension / criterion | Score | Evidence, observed consequence and correction |
|---|---:|---|
| Technical: entities/grain/semantics | 2 | {d['entities']} Relevant records and codebook/source meanings are in REPORT.md; no invented target or denominator. |
| Technical: preparation/quality | 2 | Named checks and actual affected populations in results/verification.csv and report; raw inputs preserved. Missing, zero and undefined remain distinct. |
| Technical: numerical/statistical validity | 2 | {d['entities']} Independent checks recompute consequential quantities where feasible; uncertainty is limited to the verified design/evaluation scope. |
| Technical: evidence/reproducibility | 2 | Exact scripts/commands, source manifest, dependency versions, saved aggregates and executed logs. No claim that code existence establishes unavailable real-world evidence. |
| Technical: artifact functionality | NOT VERIFIED | Final Chromium checks, exact display/CSV reconciliation, interactions/reset/empty state, local links, mobile overflow and screenshots must be inspected. |
| Analytical: objective/audience | 2 | BRIEF.md retains early academic risk through assessment behavior; educator use and capacity are proposed, not stakeholder-agreed. |
| Analytical: feasibility/questions | 2 | REPORT.md answers supported questions and identifies specific linkage/timing/target blockers; no unsupported warning simulation. |
| Analytical: method selection | 2 | Simplest methods answer the supported comparisons. {d['depth']} |
| Analytical: depth/follow-up | 2 | {d['depth']} Executed results change or bound material initial interpretations rather than merely propose future analysis. |
| Analytical: uncertainty/bias/alternatives | 2 | Report ties uncertainty to actual selection, weighting, temporal/availability or context limits. No causal or general-population inference from unsupported evidence. |
| Analytical: interpretation/usefulness | 2 | Numerical magnitudes, populations, denominators and educational implications lead the report; exact missing evidence explains the next useful investigation. |
| Analytical: honest scope/completion | 2 | Explicit status distinguishes direct retrospective, proxy or feasibility/contextual work. Actual prior shallow-output feedback was addressed through investigation; acceptance remains pending. |
| Communication: visual analytical value | NOT VERIFIED | Dataset-specific question views expose consequential comparisons and denominators. Final rendered review must verify readability and useful encodings. |
| Communication: synthesis/accessibility | NOT VERIFIED | Required report and dashboard each expose essential findings; final reader-task paths below and screenshots must be inspected. Raw Markdown/CSV are supporting, not essential browser delivery. |

## Finding-to-interface coverage / reader tasks

The following map links questions/findings through comparison to the actual interface. Final review records the executed default/filtered path, observed evidence and exact limitations in `evidence/browser-review.json`; until executed it is not a PASS.

| Reader task / comparison | Interface path | Population, limitation and supporting detail |
|---|---|---|
'''
 for ident,task in d['tasks']:review+='| '+task+' | Dashboard `#'+ident+'`; corresponding rendered report section | Active selector state and fixed-reference labels define population/time/denominator; explanation beside table gives limits; aggregate CSVs and README link to reproduction. |\n'
 review+='''
## Decisions and unavailable evidence

Analysis minimum across applicable reviewed criteria: 2. Numerical gates do not establish actual record availability, prospective transport, causal impact or stakeholder acceptance. Missing evidence remains NOT VERIFIED in the ledger and report; NOT APPLICABLE is reserved for no intervention, not unavailable analysis. Delivery is separately unverified until the final recorded browser/visual walkthrough. No average score can offset a critical failure.
'''
 (r/'QUALITY_REVIEW.md').write_text(review)
 process=f'''# {name}: gate decisions and corrections

13 October 2026. User explicitly extended the approved OULAD generic-prompt workflow to all remaining datasets. Existing OULAD outputs were preserved; this study was framed independently rather than inheriting its result or layout.

1. Read project instructions/installed analytical skill and relevant references; inspect actual files/schema/records and metadata before defining analytical scope. Save BRIEF.md before predictive evaluation or substantial contextual comparison.
2. Establish unit, question support, measures, denominators and availability limits. {d['source']}
3. Execute preparation and relevant quality checks without writing raw inputs. {d['entities']}
4. Execute the supported investigation and discriminating follow-ups. {d['depth']}
5. Build a finding-led rendered report and a purpose-specific local dashboard; retain exact CSV evidence rather than handwritten display calculations. Essential uncertainty/selection/evidence gaps stay visible.
6. Final browser/display and visual review is recorded separately. A working control is not analytical acceptance; reader paths must expose the answer, comparison, population/denominator/period, limitation and supporting detail.

Stopping rationale: the supported priority questions have measured comparisons or precise blockers, with material alternatives investigated. More model complexity cannot supply absent student event/availability/outcome linkage. Status: {d['status']}. No intervention exists; no effect or acceptance is claimed.
'''
 if name=='mooccubex':process+='\nCorrection: the initial zero-unmatched-field-join assumption failed (110 memberships/85 course IDs absent locally). Revisited preparation, retained the missing-course evidence, and restricted field statistics to matched courses; the manual-label coverage sensitivity exposes selection bias. Repeated relation pairs are separately counted and unique-pair views used only for linkage coverage.\n'
 if name=='talis-2024':process+='\nCorrection: combined-versus-level comparison initially failed because column order differed; explicitly aligning columns verified exact key/level/selected-item equality without changing source values. Verified ADJRT24 means adjudication quality, not a rotated-form weight adjustment. Retained by-design/other missingness and common-response denominators.\n'
 (r/'PROCESS.md').write_text(process)
print('Wrote reproduction, scope, gate and provisional review documentation.')
