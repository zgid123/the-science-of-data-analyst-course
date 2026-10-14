"""Build finding-led report, local SVG dashboard and static publication figures."""
from pathlib import Path
import json,html
import numpy as np,pandas as pd
import markdown
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parents[1];O=R/'results';FIG=R/'figures';FIG.mkdir(exist_ok=True)
def read(n):return pd.read_csv(O/(n+'.csv'))
m=read('model_metrics');u=read('uncertainty');a=read('behavior_comparisons');s=read('sensitivity');l=read('lead_time');cov=read('coverage');sg=read('subgroup_errors');cal=read('calibration');q=read('data_quality');cb=read('cohort_behaviors');follow=read('model_followup');shift=read('feature_shift');bu=read('behavior_increment_uncertainty')
t=m[(m.split=='test')&(m.capacity==.2)].copy()
def metric(c,name='combined'):return t[(t.cutoff==c)&(t.model==name)].iloc[0]
def pct(v):return 'undefined' if pd.isna(v) else f'{100*v:.1f}%'
def table(df,cols=None):
 df=df.copy() if cols is None else df[cols].copy()
 for col in df:
  if pd.api.types.is_float_dtype(df[col]):df[col]=df[col].map(lambda x:'—' if pd.isna(x) else f'{x:.3f}')
 return df.to_html(index=False,escape=True,border=0)
def mdtable(df):
 vals=df.fillna('—').astype(str);return '| '+' | '.join(vals.columns)+' |\n|'+'|'.join(['---']*len(vals.columns))+'|\n'+'\n'.join('| '+' | '.join(row)+' |' for row in vals.values)
d60=metric(60);assoc=a[(a.cutoff==60)&(a.dimension=='behavior_group')].set_index('group')
miss=assoc.loc['At least one absent due record'];present=assoc.loc['All due records present']
diff=u[(u.cutoff==60)&(u.comparison=='combined minus score AP')].iloc[0]
le=l[(l.cutoff==60)&(l.group=='flagged_future_withdrawals')].iloc[0]
# Reusable export figures with honest zero baselines and labeled denominators.
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(figsize=(8,4.5))
for name,color in [('behavior','#126b70'),('score','#a36d20'),('combined','#222d54'),('module','#9b9b9b')]:
 d=t[t.model==name];ax.plot(d.cutoff,d.ap,'o-',label=name,color=color)
ax.set(xlabel='Warning cutoff (days after start)',ylabel='Average precision (AP)',xticks=[30,60,90],ylim=(0,1),title='Later-cohort ranking: behavior, delayed scores and combination')
ax.legend(ncol=4);ax.grid(alpha=.15);fig.tight_layout();fig.savefig(FIG/'ranking_by_cutoff.png',dpi=180);plt.close(fig)
fig,ax=plt.subplots(figsize=(8,4.5));d=a[(a.cutoff==60)&(a.dimension=='module_behavior')];mods=sorted(d.group.str[:3].unique());pos=np.arange(len(mods));width=.37
for j,(label,color) in enumerate([('All due records present','#126b70'),('At least one absent due record','#c06b30')]):
 dd=d[d.group.str.endswith(' / '+label)].set_index(d[d.group.str.endswith(' / '+label)].group.str[:3]).reindex(mods)
 bars=ax.bar(pos+(j-.5)*width,dd.risk_rate,width,label=label,color=color)
 for bar,n in zip(bars,dd.n):
  if pd.notna(n):ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.02,f'n={int(n)}',ha='center',fontsize=8)
ax.set(xticks=pos,xticklabels=mods,ylabel='Later Fail or Withdrawn proportion',ylim=(0,1.15),title='Day 60: absent records versus complete due records, within module');ax.legend(fontsize=8);fig.tight_layout();fig.savefig(FIG/'within_module_behavior.png',dpi=180);plt.close(fig)
# Human-readable report values generated directly from the saved evidence.
perf=t[['cutoff','model','n','ap','precision','recall','alert_rate','fp','fn','brier']]
behavior=a[(a.cutoff==60)&(a.dimension=='final_result')][['group','n','due_n','missing_mean','ontime_mean','lateness_median','score_mean']]
selectedsens=s[(s.cutoff==60)][['setting','model','n','ap','precision','recall','alert_rate']]
module=a[(a.cutoff==60)&(a.dimension=='module_behavior')][['group','n','risk_rate','future_withdrawn_n','fail_n']]
sub=sg[(sg.cutoff==60)&sg.dimension.isin(['code_module','disability','age_band'])][['dimension','group','n','prevalence','precision','recall','alert_rate','fp','fn']]
raw=read('raw_outcomes');rawtotal=raw.groupby('final_result').n.sum()
report=f'''# Assessment records offer early warnings, with limited coverage and substantial missed risk

OULAD · analysis snapshot 13 October 2026 · unit: student–module–presentation enrollment.

**Complete retrospective analysis within the stated first-attempt, six-module evaluation scope; live warning validity remains conditional on unobserved recording and score-release times.** This study does not establish intervention effectiveness or performance on repeat attempts, late registrants, CCC, or current students.

On day 60, the combined model achieved average precision **{d60.ap:.3f}** against a test risk prevalence of **{pct(d60.prevalence)}**. A threshold selected to review approximately 20% of validation enrollments flagged **{int(d60.alerts):,} of {int(d60.n):,}** later-cohort enrollments ({pct(d60.alert_rate)}), with **{pct(d60.precision)} precision** and **{pct(d60.recall)} recall**. It missed **{int(d60.fn):,}** later adverse outcomes. These estimates support an educator-review candidate, with substantial missed risk remaining.

[Open interactive dashboard](dashboard/index.html). All comparisons below refer to the common evaluated population for the selected cutoff unless stated otherwise. Report tables show proportions on 0–1 scales; the dashboard formats percentages. Supporting CSVs are in `results/`.

## 1. Missing due records are associated with later risk, including within modules

At day 60, enrollments with at least one absent due-assessment record had later Fail/Withdrawn prevalence **{pct(miss.risk_rate)}** (n={int(miss.n):,}), compared with **{pct(present.risk_rate)}** among enrollments with all due records present (n={int(present.n):,}); an observed difference of **{100*(miss.risk_rate-present.risk_rate):.1f} percentage points**. “Absent” means no non-banked submission recorded by the cutoff for a scheduled, due, non-exam assessment; it does not prove a missed individual obligation. Extensions, exemptions and recording delays are unavailable.

Could module composition explain the difference? The executed follow-up compares both groups inside each module, below. GGG has no due assessment by day 60 and is not forced into the complete/missing contrast. Other modules can differ in how many and which assessments are due, so neither the aggregate nor within-module gaps identify a causal effect of completion. Outcome-specific rows further distinguish eventual failure from future withdrawal; they are not interchangeable educational outcomes.

![Within-module comparison](figures/within_module_behavior.png)

{mdtable(module.round(3))}

Outcome-specific behavior on day 60 (mean missing/on-time fractions use only defined due denominators; lateness median is across enrollment-level means for recorded due submissions):

{mdtable(behavior.round(3))}

The local data contains {int(raw.n.sum()):,} enrollment records across 22 presentations and seven modules, not that many distinct people. Full-snapshot final outcomes are Fail {int(rawtotal['Fail']):,}, Withdrawn {int(rawtotal['Withdrawn']):,}, Pass {int(rawtotal['Pass']):,}, Distinction {int(rawtotal['Distinction']):,}. `cohort_behaviors.csv` gives the executed first-attempt descriptive comparisons across all local cohorts, including CCC and February starts; these are not additional predictive holdouts. VLE click data was not needed to answer the assessment-centered questions and was not scanned.

## 2. Earlier warnings trade evidence for support time

Day 30/60/90 were proposed in advance, not selected for the best test score. At day 30, EEE and GGG have no due assessment; GGG's first due assessment is day 61. A zero opportunity count gives **undefined completion fractions**, not perfect compliance or noncompliance. Models can still return module-prior-based estimates, which must not be mistaken for assessment-behavior evidence. Coverage is shown for all cohorts below. `test_n` is the stricter six-module, new-to-2013J subset, not the full active population.

{mdtable(cov[cov.cohort.isin(['2013J','2014J'])])}

![Ranking by cutoff](figures/ranking_by_cutoff.png)

The active enrollment population shrinks with each cutoff as withdrawals occur. The executed `active_through_day90_common_panel` sensitivity evaluates all three cutoffs on the same day-90 survivor enrollments, separating added observation time from changing membership. That panel conditions on future survival and is a diagnostic, not an operational eligibility rule.

{mdtable(s[s.setting=='active_through_day90_common_panel'][['cutoff','n','prevalence','ap','precision','recall','alert_rate']].round(3))}

For flagged future withdrawals at day 60 (n={int(le.n):,}), the observed median interval to withdrawal was **{le['median']:.0f} days**, with interquartile range **{le.q25:.0f}–{le.q75:.0f} days**. **{int(le.under_14):,}** were fewer than the proposed 14 support days away. Do not apply this withdrawal lead time to Fail. For final Fail, only the remaining scheduled course duration is available; it is a course-end proxy and cannot establish when academic difficulty became irreversible or grades were published.

{mdtable(l.round(1))}

## 3. Behavior adds information beyond a delayed-score baseline

All four fitted comparisons share the same train, validation and test enrollments at each cutoff. Every logistic model includes module context. “Behavior” adds due count, missing fraction, on-time fraction, mean positive lateness and recency; “score” adds mean available early score and count of nonmissing available scores. That score-count feature already conveys some assessment-record availability, making this a comparatively strong prior-score baseline rather than a pure marks-only comparison. “Combined” adds both sets. Missing scores never remove students from the comparison.

{mdtable(perf.round(3))}

At day 60, combined minus score average precision was **{diff.estimate:.3f}**, with a paired student-cluster bootstrap 95% interval **[{diff.lo:.3f}, {diff.hi:.3f}]** (300 replicates, fixed fitted models). This estimates evaluation-population variability; it excludes training uncertainty, delay uncertainty, alternate cohorts and model-selection uncertainty. AP is a ranking measure, not a percentage of students correctly identified. No-skill AP equals prevalence; module-only AP may exceed that by exploiting course differences. The simple absent-due-record rule is evaluated separately:

{mdtable(m[(m.split=='test')&(m.capacity==0)][['cutoff','model','n','ap','precision','recall','alert_rate','fp','fn']].round(3))}

Could unknown mark-release times explain the result? The executed sensitivity delays usable marks from submission +14 to +28 days. Could absent records reflect delayed logging? A second challenge hides submissions for seven additional days while retaining the scheduled due denominator. Could the composite outcome hide a different failure problem? A third challenge refits for Fail versus Pass/Distinction, omitting future withdrawals; this is a selected retrospective non-withdrawal population and not a policy for all active students. A fourth adds students previously present in 2013J back to the test population. These comparisons bound interpretations; none was used to retune the primary model.

{mdtable(selectedsens.round(3))}

### Combining scores can reduce early warning quality under cohort shift

Behavior-only beats combined at days 30 and 60; combined leads at day 90. The paired comparison below shows that this is not merely ranking noise in the evaluated population. More feature groups do not guarantee stronger warnings.

{mdtable(bu.round(3))}

The executed follow-up shows a reversal from within-2013J validation to later-cohort testing. On day 60 validation, combined AP was 0.731 versus behavior-only 0.680; on test it fell to 0.586 versus behavior-only 0.646. This is evidence that a same-cohort validation gain does not establish transport to the next year. Module-specific testing and feature distributions localize part of the problem: BBB combined AP is 0.542 versus behavior 0.638, while DDD combined is 0.755 versus behavior 0.581. The pattern is heterogeneous, rather than uniformly harmful scores.

{mdtable(follow[(follow.cutoff==60)&(follow.split=='test')].pivot(index='module',columns='model',values='ap').reset_index().round(3))}

For BBB, historical training mean available early score was 72.0 versus 59.0 on test; the due count changed from 3 to 2. The saved assessment schedule confirms that BBB 2013J had an early CMA due at day 54 and TMA deadlines at days 19/47; 2014J had no CMAs, TMA deadlines at 19/54, and the first TMA changed from 5% to 0% weight. The analysis deliberately retains zero-weight formative assessments as behavior opportunities, but unweighted average marks across this changed schedule have limited comparability. These observed shifts provide a plausible explanation, not proof that schedule changes caused the performance loss. The 28-day score-delay challenge leaves combined day-60 AP nearly unchanged (0.584 versus 0.586), so that release-delay choice alone does not explain the reversal.

{mdtable(shift[(shift.cutoff==60)&shift.split.isin(['train','test'])].round(3))}

The implication is to retain behavior-only as a serious candidate, avoid claiming that combined is always preferable, and verify assessment comparability in a fresh future cohort before choosing a deployed model. The report uses combined at a fixed reference threshold to demonstrate workload, not to name it as the winning model at every cutoff. This follow-up was exploratory after the initial results and did not change any model or threshold.

## 4. Review workload, missed students and probability reliability matter

The proposed 10/20/30% capacities select score quantiles on validation, using the higher observed quantile. Tied probabilities can exceed capacity even on validation; cohort shift can change test alert volume. The dashboard shows the actual validation and test volumes, confusion counts and separate outcome recalls. Capacity is an assumption for comparison, not an educator-approved workload or a hard operational cap. Test outcomes were not used to set thresholds.

{mdtable(m[(m.cutoff==60)&(m.model=='combined')][['split','capacity','n','threshold','alerts','alert_rate','precision','recall','fp','fn']].round(3))}

At the reference threshold, these module, disability and age comparisons show where errors concentrate. Disability and age are audit fields only and never predictors. Denominators are each group's eligible test enrollments; recall divides by that group's positive outcomes, precision by its flagged enrollments. Small groups are descriptive and unstable; these are exploratory comparisons, without confirmatory significance or fairness certification.

{mdtable(sub.round(3))}

At day 60, 937 enrollments in the highest probability bin had mean predicted risk **95.6%**, but observed adverse-outcome frequency was only **59.1%**. This is substantial overconfidence, not an operationally reliable probability estimate. BBB had 42.5% of enrollments flagged with 38.5% precision, compared with DDD at 10.0% flagged with 93.8% precision; the single global threshold distributes workload unevenly. These are exploratory observed comparisons, not evidence of a causal demographic effect.

Probability reliability is assessed with Brier loss (lower is better) above and fixed probability-bin observations below. The model was not recalibrated to the holdout. Differences between mean predicted and observed risk are evidence against treating probabilities as validated individualized forecasts. Course shift and missing delay metadata remain practical concerns even when ranking improves.

{mdtable(cal[cal.cutoff==60].round(3))}

A proposed next step is educator review of whether these signals and workloads suit a real support process, followed by a prospective study with logged alert, outreach, score-release and outcome times. No individual alert list is published. No actual intervention exists here; intervention outcome evaluation is **NOT APPLICABLE**. Stakeholder acceptance of these deliverables is **PENDING**.

## Definitions, timing and reproducible design

The intended question is future final Fail or future recorded withdrawal, not detecting withdrawal that already occurred. Pass and Distinction are successful outcomes; combining Fail/Withdrawn is a proposed support-review operationalization, with separate summaries and the failure-only challenge above. Withdrawal eligibility uses dates only to exclude past events. Future withdrawal dates and final outcomes are labels/audit quantities only, never predictors.

| Variable | Source and formula | Availability and cutoff |
|---|---|---|
| Enrollment eligibility | `num_of_prev_attempts == 0`, `date_registration <= 0`; withdrawal not after scheduled end; coherent `final_result`/`date_unregistration` | Baseline first attempt, registration by start; coherent outcome requirement is retrospective quality selection, disclosed below |
| Future risk | `final_result` in Fail/Withdrawn, withdrawal date > cutoff | Label through end of presentation; withdrawal time directly recorded, Fail event time absent |
| Due count | Count non-Exam `assessments` with 0 <= `date` <= cutoff for the enrollment's module/presentation | Scheduled deadlines assumed known; all scheduled assessments assumed applicable to first attempts |
| Missing fraction | 1 − recorded due submissions / due count | Non-banked `studentAssessment.date_submitted <= cutoff`; no due opportunities gives undefined |
| On-time fraction | Due submissions with `date_submitted <= assessments.date` / due count | Also submission-visible by cutoff; same denominator as missing fraction |
| Mean lateness | Mean max(submission − due, 0), only recorded due submissions | Undefined if none submitted; conditional on submitting, not time spent working |
| Recency | cutoff − most recent non-exam non-banked submission day | All visible submissions, including assessments not yet due; undefined with no record |
| Early score mean/count | Mean/count nonmissing `score` on non-exam, non-banked submissions | submission +14 days <= cutoff; +28-day challenge; actual grade release unknown |
| Module context | `code_module` | Categorical, known at registration; shared in all fitted models |
| Lead time | withdrawal day − cutoff | Retrospective audit only; course length − cutoff for Fail is explicitly a proxy |

The six-module evaluation includes AAA, BBB, DDD, EEE, FFF, GGG. CCC has no 2013J history and cannot support this temporal comparison. The 2013J historical population is split by student (75%/25%, seed 20261013) before cutoff-specific eligibility; all module records for a student stay in one side. The 2014J test excludes everyone appearing anywhere in 2013J, including ineligible historical records. Students may have multiple test enrollments, so uncertainty resamples student clusters. This supports new-to-that-historical-cohort later-presentation generalization only. It does not guarantee these are first-ever OU students.

All models are L2 logistic regression with C=1, no test-based tuning. Numerical medians, missingness indicators, scaling and one-hot module encoding are learned on train only; an entirely missing training column is retained with a constant placeholder. Validation fits no preprocessing and chooses thresholds only. Separate cutoff models use only information available by their cutoff under the timing assumptions. Validation is a within-2013J partition for tuning, not a simulated future deployment. The temporal claim comes from 2014J test evaluation. Prior reuse of this dataset/holdout outside this run is **unknown**, and a fresh external cohort is needed for independent confirmation.

To bound label timing without inventing start dates, the latest possible October 2013 start plus longest course plus an assumed 60-day final-result publication lag ends on **{json.loads((O/'metadata.json').read_text())['label_publication_latest_bound']}**, before the earliest October 2014 start. The calendar inequality was checked; actual label-release dates were not observed. This assumption is essential to a simulated deployment claim, rather than merely retrospectively training on earlier cohorts.

Raw source files are preserved; hashes and row counts are saved in `source_manifest.csv`. Relevant source semantics were checked against the [dataset creator's documentation](https://rdrr.io/github/jakubkuzilek/oulad/src/R/oulad.R) (scheduled cutoffs, submission days, banked credits, registration, outcomes). The [UCI record](https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset) confirms February/October presentation codes and CC BY 4.0 attribution. Sources were accessed 13 October 2026; no historical acquisition date is inferred. Dataset attribution: Jakub Kuzilek, Martin Hlosta and Zdenek Zdrahal, Open University Learning Analytics Dataset; DOI 10.24432/C5KK69, research paper DOI 10.1038/sdata.2017.171.

## Quality, selection and limits

{mdtable(q)}

Exclusion issue counts overlap. `coverage.csv` reconciles raw → baseline eligible → active at cutoff. One historical FFF/2013J withdrawal recorded at day 444, after scheduled day 268 end, is excluded outside the defined follow-up window before fitting. Missing registration dates and incoherent withdrawal/outcome records are excluded, rather than assigning an invented day. Missing scores stay missing, with train-only imputation and indicators. Banked credits appear only in repeat attempts; restricting to first attempts avoids imposing already-credited assessments as current obligations. No source outliers or duplicate submissions were dropped; keys and ranges were checked. Schedule changes and individual extensions remain unknown, so missing records are proxy behavior signals.

The coherent-outcome filter and first-attempt selection limit generalization; they are not operationally available future predictors. Incoherence is detected retrospectively to ensure auditable eligibility; the excluded population must be resolved before live deployment. Course end is not grade publication. Current activity or grade logging could be backfilled, and the seven-day logging challenge cannot verify actual historical availability. Two years and seven selected anonymized modules do not represent all higher education, and within-module contrasts do not adjust for all causes of risk. Associations are not causal effects of submitting earlier or outreach.

## Verification and question coverage

Reproduce with the commands in [README](README.md). Executed evidence is in `results/verification.csv`, `results/independent_checks.csv`, `evidence/analysis-run.txt`, and `evidence/browser-review.json`. Exact dependency versions are in `evidence/environment.txt`. The numerical ledger includes source keys, join coverage, banked-credit exclusion, score range, cutoff compliance, due-denominator bounds, student split separation, historical-label calendar bounds and independently reconciled confusion counts. Independent raw lookup recomputes due count and missing fraction for every primary test enrollment. The ledger verifies calculations under assumptions; it does not verify missing real-world timestamps.

| Priority question | Status and supported answer | Unresolved boundary |
|---|---|---|
| Early assessment behavior and later risk | Answered by outcome-specific and within-module missing/on-time comparisons | Individual obligations, causal mechanism, accommodations unavailable |
| Warning timing and coverage | Answered at 30/60/90 and common day-90 panel; withdrawal lead time measured | Failure-event time and actual useful support deadline unavailable |
| Added warning value | Answered by same-population baselines, paired AP intervals and delay/target challenges | Score release and current-record availability are assumed, prior holdout reuse unknown |
| Workload and errors | Answered by validation capacity thresholds, actual test volumes, confusion counts and subgroup/calibration audit | Stakeholder capacity, intervention effect and prospective transport unobserved |

See [quality and interface review](QUALITY_REVIEW.md) for criterion-specific review, reader-task paths and distinct analysis/delivery judgments. No claim of stakeholder approval or prevention of failure is made.
'''
(R/'REPORT.md').write_text(report)
CSS='''body{margin:0;background:#f4f5f8;color:#17233a;font:16px/1.65 system-ui,sans-serif}main{max-width:1160px;margin:auto;padding:32px}h1{font-size:34px;line-height:1.2;max-width:950px}h2{font-size:25px;margin-top:42px}h3{font-size:20px}a{color:#126b70}section,.panel{background:white;border:1px solid #dce1e8;padding:24px;margin:20px 0;border-radius:10px}table{border-collapse:collapse;width:100%;font-size:13px;white-space:nowrap}td,th{text-align:left;padding:9px 12px;border-bottom:1px solid #dce1e8}th{background:#edf1f4}tr:hover{background:#f3f8f8}.scroll{overflow:auto}select,button{font:inherit;padding:8px;border:1px solid #afb8c6;border-radius:5px;background:white}label{margin-right:20px;display:inline-block}.note{border-left:4px solid #bc7735;padding:12px 18px;background:#fff5e8}.muted{color:#516077}.stats{display:flex;flex-wrap:wrap;gap:22px}.stat{min-width:180px;flex:1;padding:12px;border-top:3px solid #126b70}.stat strong{display:block;font-size:29px}img,svg{max-width:100%;height:auto}nav{display:flex;gap:16px;flex-wrap:wrap}details{padding:12px 0}svg text{font-family:system-ui,sans-serif}@media(max-width:650px){main{padding:16px}h1{font-size:27px}.panel,section{padding:16px}label{display:block;margin:10px 0}}'''
rendered=markdown.markdown(report,extensions=['tables','fenced_code','toc'])
# Local relative figures and links; wrap tables for narrow-screen reading.
rendered=rendered.replace('<table>','<div class="scroll"><table>').replace('</table>','</table></div>')
(R/'report.html').write_text(f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>OULAD research report</title><style>{CSS}</style><main><nav><a href="dashboard/index.html">Dashboard</a><a href="README.md">Reproduction instructions</a></nav>{rendered}</main></html>')
# Embed aggregate evidence only, without individual IDs or external assets.
DATA={n:read(n).replace({np.nan:None}).to_dict('records') for n in ['model_metrics','coverage','behavior_comparisons','uncertainty','sensitivity','lead_time','subgroup_errors','calibration','cohort_behaviors','model_followup','feature_shift','behavior_increment_uncertainty']}
(R/'dashboard'/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>OULAD · Assessment behavior early warnings</title><style>'''+CSS+'''</style><main>
<p class="muted">OULAD / Retrospective assessment-behavior study / 13 October 2026</p><h1>What assessment records can tell us before a course ends</h1>
<p>Explore early behavior, later academic risk and the review workload. Evaluation: first module attempts registered by day 0; six modules, October 2014; students absent from October 2013 history. Unit: student–module–presentation enrollment.</p>
<p class="note">Risk = final Fail or withdrawal recorded after the cutoff. These are retrospective estimates, conditional on timely submission logging and assumed grade-release delays. Fail and withdrawal are reported separately. No intervention effect is measured.</p>
<nav><a href="../report.html">Read the research report</a><a href="../README.md">Reproduce</a><a href="../results/model_metrics.csv">Metric evidence CSV</a></nav>
<section><label>Warning cutoff <select id="cut"><option>30</option><option selected>60</option><option>90</option></select> days</label><label>Validation review capacity <select id="cap"><option value="0.1">10%</option><option value="0.2" selected>20%</option><option value="0.3">30%</option></select></label><button id="reset">Reset</button><p class="muted">Cutoff updates all sections. Capacity updates combined-model workload and confusion counts; subgroup, outcome-recall and lead-time audits remain at the labeled 20% reference. No module filter changes the primary test population.</p></section>
<div class="stats" id="stats"></div>
<section id="coverage"><h2>How much assessment evidence exists by this point?</h2><div id="cov"></div><p>Raw counts include all enrollments. Baseline excludes repeat attempts, late/unknown registration and incoherent withdrawal records. Active excludes withdrawals already recorded by the cutoff. Due coverage is the fraction of active enrollments with at least one scheduled assessment due. Test is the narrower six-module population, excluding historical students and CCC.</p></section>
<section id="behavior"><h2>Absent due records and later outcomes</h2><div id="bars"></div><div id="behaviorTable"></div><h3>Does the contrast survive within modules?</h3><div id="moduleBehavior"></div><p class="muted">Due denominators include scheduled non-exam assessments by the cutoff. “Absent” is a missing recorded submission, with individual extensions/exemptions unobserved. No assessments due is distinct from complete due records. Outcome means below use defined fractions only.</p><div id="outcomes"></div></section>
<section id="ranking"><h2>Does behavior add to early scores?</h2><div id="rankingChart"></div><div id="models"></div><p id="interval"></p><p>All fitted comparisons include module context and use the same test population. Scores assume a 14-day release delay; the score baseline includes score availability count. AP is average precision, a ranking statistic; no-skill AP equals prevalence. Brier loss is probability error (lower is better). The absent-record rule flags any due missing record, independent of selected capacity. Probability ties and cohort shift can exceed validation capacity.</p></section>
<section id="transport"><h2>Why more features do not always help</h2><div id="behaviorIncrement"></div><p>Negative differences mean behavior-only ranked risk better. Day-60 validation favored combined (AP 0.731 versus 0.680), but later-cohort test reversed that result. The module comparison and feature shifts below show heterogeneous transport; BBB early scores changed from mean 72.0 to 59.0 and its due opportunities fell from three to two. BBB also lost CMAs and changed its first TMA weight from 5% to 0%. These changes are plausible explanations, not causal proof. The 28-day release assumption barely changes combined day-60 AP. No model was retuned to these test findings.</p><div id="moduleModels"></div><details><summary>Compare historical and later-cohort feature distributions</summary><div id="featureShift"></div></details></section><section id="workload"><h2>What would educators need to review?</h2><div id="tradeoffs"></div><p id="workloadText"></p><div id="outcomeRecall"></div><p>False positives later Pass/Distinction; false negatives later Fail/Withdrawn. Validation quantiles select thresholds; test outcomes do not. Separate outcome recalls use each final-outcome group's count, with flagged successful students representing false positive rates.</p></section>
<section id="timing"><h2>How much support time remains?</h2><div id="lead"></div><p>The 14-day support window is proposed, not stakeholder approved. Withdrawal intervals use observed future unregistration days; course-end intervals for Fail are proxies and cannot establish time before failure or score publication.</p><h3>Compare the same enrollments across cutoffs</h3><div id="common"></div><p>The common panel is active through day 90, so membership stays fixed. It conditions on future survival and is only a diagnostic for changing cohort membership.</p></section>
<section id="sensitivity"><h2>Which assumptions change the result?</h2><div id="sens"></div><p>28-day mark release challenges the primary 14-day assumption. Seven-day logging delay hides recent submissions and scores. Failure-only omits future withdrawals and refits Fail versus Pass/Distinction; it evaluates a selected retrospective non-withdrawal population. Including previous 2013J students broadens the test population with unchanged models and threshold. Sensitivities did not select the primary model.</p></section>
<section id="audit"><h2>Who is missed or falsely flagged?</h2><label>Audit group <select id="dimension"><option value="code_module">Module</option><option value="disability">Declared disability</option><option value="age_band">Age band</option><option value="behavior_group">Due-record group</option></select></label><div id="errors"></div><p>Fixed 20% validation-capacity reference, combined model. Disability and age are audit fields, not predictors. Each group's eligible test enrollment count is the denominator; small groups are unstable. This is an exploratory error audit, not fairness certification.</p><h3>Do shown probabilities match observed risk?</h3><p class="note">At day 60, the highest risk bin averaged 95.6% predicted risk but only 59.1% observed risk (n=937). Probabilities are substantially overconfident. This fixed finding is a day-60 reference; the table below follows the cutoff selector.</p><div id="calibration"></div><p>Fixed probability bins; calibration uses the full eligible test population and does not depend on the selected alert capacity. Gaps between prediction and observed risk limit use of individualized probabilities.</p></section>
<details class="panel"><summary>Full-snapshot context, definitions and evidence</summary><label>Descriptive cohort <select id="cohort"><option>2013B</option><option>2013J</option><option>2014B</option><option selected>2014J</option></select></label><div id="cohorts"></div><p>These are first-attempt, active, coherently recorded enrollments across all local modules. CCC and February cohorts are descriptive, not extra predictive tests. Cohort control affects only this context table.</p><p>Primary train/validation: student-group split of 2013J, seed 20261013. All learned preprocessing fits train only. Historical label-release dates are not recorded; the calendar check assumes publication within 60 days after course end. Source CSVs are unchanged and identified by SHA-256 in <a href="../results/source_manifest.csv">the source manifest</a>. <a href="../results/verification.csv">Calculation ledger</a> · <a href="../results/independent_checks.csv">Independent raw reconciliation</a> · <a href="../report.html">Definitions, limitations and full findings</a>.</p><p>Dataset: Kuzilek, Hlosta &amp; Zdrahal; <a href="https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset">UCI OULAD, CC BY 4.0</a>. Snapshot is static; rerun local scripts to refresh. No student identifiers are embedded. Stakeholder acceptance is pending; no intervention has been implemented.</p></details></main>
<script>const D='''+json.dumps(DATA,allow_nan=False)+''';
const $=id=>document.getElementById(id), esc=x=>String(x??'—').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const pc=x=>x==null?'—':(100*x).toFixed(1)+'%',num=x=>x==null?'—':Number(x).toLocaleString('en-US',{maximumFractionDigits:0}),dec=x=>x==null?'—':Number(x).toFixed(3);
function tbl(id,rows,cols){$(id).innerHTML=rows.length?'<div class="scroll"><table><thead><tr>'+cols.map(c=>'<th>'+esc(c[1])+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+cols.map(c=>'<td>'+esc((c[2]||String)(r[c[0]]))+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>':'<p>No observations for this selection; the rate is undefined.</p>';}
function barChart(id,rows,key,label,color='#126b70',formatter=pc) {let height=rows.length*46+40;$(id).innerHTML='<svg viewBox="0 0 900 '+height+'" role="img" aria-label="'+esc(label)+'">'+rows.map((r,i)=>'<text x="0" y="'+(i*46+25)+'" font-size="13">'+esc(r.group||r.model)+'</text><rect x="270" y="'+(i*46+7)+'" width="'+(r[key]*480)+'" height="24" fill="'+color+'"/><text x="'+(280+r[key]*480)+'" y="'+(i*46+25)+'" font-size="13">'+formatter(r[key])+'</text>').join('')+'<text x="270" y="'+(height-2)+'" font-size="12">'+(key==='ap'?'0.0':'0%')+'</text><text x="750" y="'+(height-2)+'" font-size="12">'+(key==='ap'?'1.0':'100%')+'</text></svg>';}
const metricCols=[['model','Signal'],['n','Test n',num],['ap','AP',dec],['precision','Precision',pc],['recall','Recall',pc],['alert_rate','Alert volume',pc],['fp','False positives',num],['fn','False negatives',num],['brier','Brier',dec]];
function render(){let c=Number($('cut').value),cap=Number($('cap').value),get=n=>D[n].filter(x=>x.cutoff===c);let mm=get('model_metrics'),base=mm.find(x=>x.split==='test'&&x.model==='combined'&&x.capacity===cap),audit=get('subgroup_errors');
$('stats').innerHTML=[['Eligible test enrollments',num(base.n)],['Later adverse outcomes',pc(base.prevalence)],['Flagged for review',num(base.alerts)+' / '+pc(base.alert_rate)],['Recall at this workload',pc(base.recall)]].map(x=>'<div class="stat">'+x[0]+'<strong>'+x[1]+'</strong></div>').join('');
tbl('cov',get('coverage'),[['cohort','Cohort'],['raw_n','Raw n',num],['base_eligible_n','Baseline eligible',num],['already_withdrawn_n','Withdrawn by cutoff',num],['active_n','Active n',num],['due_n','At least one due',num],['test_n','Primary test n',num]]);
let aa=get('behavior_comparisons'),groups=aa.filter(x=>x.dimension==='behavior_group');barChart('bars',groups,'risk_rate','Later risk by due-record group');tbl('behaviorTable',groups,[['group','Due-record group'],['n','n',num],['risk_rate','Later risk',pc],['fail_n','Final Fail',num],['future_withdrawn_n','Future Withdrawn',num]]);
tbl('moduleBehavior',aa.filter(x=>x.dimension==='module_behavior'),[['group','Module / due-record group'],['n','n',num],['risk_rate','Later risk',pc],['fail_n','Final Fail',num],['future_withdrawn_n','Future Withdrawn',num]]);
tbl('outcomes',aa.filter(x=>x.dimension==='final_result'),[['group','Later final outcome'],['n','n',num],['due_n','Defined due denominator n',num],['missing_mean','Mean missing fraction',pc],['ontime_mean','Mean on-time fraction',pc],['lateness_median','Median mean lateness (days)',dec],['score_mean','Mean enrollment score',dec]]);
let selected=mm.filter(x=>x.split==='test'&&(x.capacity===cap||x.capacity===0));barChart('rankingChart',selected,'ap','Average precision by signal','#126b70',dec);tbl('models',selected,metricCols);
tbl('behaviorIncrement',D.behavior_increment_uncertainty,[['cutoff','Cutoff day'],['estimate','Combined − behavior AP',dec],['lo','95% interval low',dec],['hi','95% interval high',dec]]);
let pivot={};for(let row of get('model_followup').filter(x=>x.split==='test')){if(!pivot[row.module])pivot[row.module]={module:row.module,n:row.n,risk:row.risk};pivot[row.module][row.model]=row.ap;}tbl('moduleModels',Object.values(pivot),[['module','Module'],['n','n',num],['risk','Risk prevalence',pc],['behavior','Behavior AP',dec],['score','Score AP',dec],['combined','Combined AP',dec]]);
tbl('featureShift',get('feature_shift').filter(x=>x.split!=='validation'),[['split','Population'],['module','Module'],['n','n',num],['due_count_mean','Mean due count',dec],['available_score_fraction','Score available',pc],['mean_score','Mean early score',dec],['missing_fraction','Mean missing fraction',pc]]);
let un=get('uncertainty').find(x=>x.comparison==='combined minus score AP');$('interval').textContent='Combined − score AP: '+dec(un.estimate)+'; paired student-cluster bootstrap 95% interval ['+dec(un.lo)+', '+dec(un.hi)+'] (300 replicates, fixed fitted models).';
tbl('tradeoffs',mm.filter(x=>x.model==='combined'),[['split','Population'],['capacity','Validation capacity',pc],['threshold','Risk threshold',dec],['n','n',num],['alerts','Alerts',num],['alert_rate','Alert volume',pc],['precision','Precision',pc],['recall','Recall',pc],['fp','False positives',num],['fn','False negatives',num]]);
$('workloadText').textContent='Selected threshold '+dec(base.threshold)+' flags '+num(base.alerts)+' enrollments; '+num(base.tp)+' later adverse outcomes caught, '+num(base.fp)+' false positives and '+num(base.fn)+' adverse outcomes missed. Precision '+pc(base.precision)+'.';
// outcome-specific errors at selected capacity are saved only for 20%; expose fixed reference explicitly.
tbl('outcomeRecall',audit.filter(x=>x.dimension==='final_result'),[['group','Later outcome (fixed 20% reference)'],['n','Outcome n',num],['alerts','Flagged',num],['alert_rate','Flagged fraction of outcome',pc],['fn','Missed adverse outcomes',num]]);
tbl('lead',get('lead_time'),[['group','Fixed 20% reference group'],['n','n',num],['q25','25th percentile (days)',num],['median','Median days',num],['q75','75th percentile (days)',num],['under_14','Under 14 days',num],['time_type','Timing meaning']]);
tbl('common',D.sensitivity.filter(x=>x.setting==='active_through_day90_common_panel'),[['cutoff','Cutoff day'],['n','Same panel n',num],['prevalence','Risk',pc],['ap','AP',dec],['precision','Precision',pc],['recall','Recall',pc],['alert_rate','Alert volume',pc]]);
tbl('sens',get('sensitivity').filter(x=>x.setting!=='active_through_day90_common_panel'),[['setting','Executed challenge'],...metricCols.filter(x=>!['fp','fn','brier'].includes(x[0]))]);
tbl('errors',audit.filter(x=>x.dimension===$('dimension').value),[['group','Group'],['n','Group n',num],['prevalence','Later risk',pc],['precision','Precision',pc],['recall','Recall',pc],['alert_rate','Flagged',pc],['fp','False positives',num],['fn','False negatives',num]]);
tbl('calibration',get('calibration'),[['bin','Probability bin'],['n','n',num],['mean_prediction','Mean predicted risk',pc],['observed_risk','Observed risk',pc]]);
tbl('cohorts',get('cohort_behaviors').filter(x=>x.cohort===$('cohort').value),[['module','Module'],['outcome','Later outcome'],['n','n',num],['due_n','With due denominator',num],['missing_fraction','Mean missing fraction',pc],['ontime_fraction','Mean on-time fraction',pc],['mean_score','Mean score',dec]]);
}
for(let id of ['cut','cap','dimension','cohort'])$(id).addEventListener('change',render);$('reset').onclick=()=>{$('cut').value='60';$('cap').value='0.2';$('dimension').value='code_module';$('cohort').value='2014J';render()};render();
</script></html>''')
print('Built REPORT.md, report.html, dashboard/index.html and figures from saved tables.')
