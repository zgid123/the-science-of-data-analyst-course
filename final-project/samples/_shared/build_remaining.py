"""Dataset-specific finding-led reports and portable analytical interfaces."""
from pathlib import Path
import sys,json
import pandas as pd,numpy as np
from delivery import setup,report,dashboard,mdtable,save

def rd(r,n):return pd.read_csv(r/'results'/(n+'.csv'))
def p(x):return 'undefined' if pd.isna(x) else f'{x*100:.1f}%'
def tables(r,n,cols=None,mask=None):
 d=rd(r,n)
 if mask is not None:d=d[mask(d)]
 if cols:d=d[cols]
 return mdtable(d)

def closing(r,scope,refs):
 checks=rd(r,'verification');passed=int((checks.status=='PASS').sum());gaps=checks[checks.status=='NOT VERIFIED']
 return f'''
## Scope, verification and handoff

Status: **{scope}**. The requested early-academic-risk objective is preserved; narrower evidence does not justify a substitute risk label or an unrelated ranking. Definitions not supplied by the user are proposed operationalizations. Stakeholder acceptance remains **PENDING**; no intervention exists, so intervention outcome evaluation is **NOT APPLICABLE**.

{passed} numerical/data checks passed in `results/verification.csv`. Checks include the quantities actually computed, with their expected conditions and methods; they do not verify missing real-world evidence. Remaining evidence boundaries:

{mdtable(gaps[['check','observed','consequence']]) if len(gaps) else 'See the explicitly stated timing and selection assumptions above.'}

Source CSVs are unchanged. `source_manifest.csv` identifies actual local inputs; preserved source metadata and exact dependency versions support reproduction. [Open the local dashboard](dashboard/index.html), [reproduce the analysis](README.md), or inspect [the criterion and reader-task review](QUALITY_REVIEW.md). Browser interaction, mobile rendering, local links and display reconciliation are documented in `evidence/browser-review.json`; screenshots preserve actual inspection. Those checks validate delivery, not causality, stakeholder approval or live alert effectiveness.

Metadata sources accessed 13 October 2026: {refs}. Original local acquisition dates and per-field vintages are not invented.
'''

METRIC_JS="""const MC=[['model','Signal'],['n','n',num],['prevalence','Observed risk',pc],['ap','Average precision',dec],['precision','Precision',pc],['recall','Recall',pc],['alert_rate','Alert volume',pc],['fp','False positives',num],['fn','False negatives',num],['brier','Brier loss',dec]];"""

def build_prediction(name):
 r,d=setup(name);isfff=name=='fff';m=rd(r,'model_metrics');u=rd(r,'uncertainty');lead=rd(r,'lead_time');c=60 if isfff else 30
 metric=m[(m.cutoff==c)&(m.model=='combined')&(m.capacity==.2)&(m.split=='test')].iloc[0]
 t=m[(m.split=='test')&((m.capacity==.2)|(m.capacity==0))]
 if isfff:
  a=rd(r,'behavior_comparisons');g=a[(a.cutoff==c)&(a.dimension=='behavior_group')].set_index('group');mis=g.loc['At least one absent due record'];complete=g.loc['All due records present'];diff=u[(u.cutoff==c)&(u.comparison=='combined minus score AP')].iloc[0];withdraw=lead[(lead.cutoff==c)&(lead.group=='flagged_future_withdrawals')].iloc[0]
  timing="""| Variable | Source / formula | Availability rule |
|---|---|---|
| Eligibility | num_of_prev_attempts=0; date_registration<=0; coherent outcome/withdrawal records; withdrawal not after scheduled course end | Withdrawals already recorded by cutoff excluded; coherence is retrospective quality selection |
| Future risk | final_result is Fail or Withdrawn, with withdrawal day>cutoff | Labels/audit only, never predictors |
| Due count | Non-Exam assessments.date between 0 and cutoff | Schedule assumed known/applicable to first attempts; extensions unknown |
| Missing fraction | 1 − recorded due submissions/due count | Non-banked date_submitted<=cutoff; undefined when none due |
| On-time fraction | Due submissions with date_submitted<=due day divided by due count | Same cutoff and denominator |
| Mean lateness | Mean max(submission day − due day,0) among visible due submissions | Undefined if none submitted; not active working time |
| Recency | cutoff − last visible non-exam non-banked submission day | Prefix only; undefined with no event |
| Early score | Mean/count nonmissing non-exam score | date_submitted+14<=cutoff; +28 sensitivity; actual release absent |
| Lead time | Future withdrawal day − cutoff | Retrospective audit; for Fail, course length−cutoff is a proxy only |
"""
  text=f'''# FFF: early assessment behavior adds warning information, while many later adverse outcomes remain missed

At day 60, combined assessment behavior and delayed scores achieved average precision **{metric.ap:.3f}** on **{int(metric.n):,}** later-cohort enrollments, against adverse-outcome prevalence **{p(metric.prevalence)}**. Its reference threshold flagged **{int(metric.alerts)}** enrollments ({p(metric.alert_rate)}), with **{p(metric.precision)} precision** and **{p(metric.recall)} recall**. It missed **{int(metric.fn)}** later Fail/Withdrawn outcomes. This supports a retrospective educator-review candidate; it does not establish sufficient standalone coverage or intervention benefit.

This is a dedicated FFF-module study, not an independent dataset replication: all five analysis tables were checked against the FFF-restricted parent OULAD records, with exact record-value equality. The assessment date column is inferred as float in the parent (because other modules have undated exams) and integer in FFF; this dtype difference does not change values. The unit is a student–FFF–presentation enrollment. The evaluation population is first module attempts registered by day 0, with coherent withdrawal records and no withdrawal by the warning cutoff. First attempts avoid carried-over-credit complications. One historical FFF withdrawal recorded at day 444 (after day 268 course end) is excluded outside the defined follow-up window, ensuring it cannot supply a future historical training label. The full local FFF snapshot spans four presentations; predictive results below refer to new-to-2013J students in 2014J. The descriptive cohort view includes all four presentations.

## Missing due records distinguish later outcomes

On day 60, later Fail/Withdrawn occurred in **{p(mis.risk_rate)}** of enrollments with an absent due-assessment record (n={int(mis.n)}), versus **{p(complete.risk_rate)}** with all due records present (n={int(complete.n)}). The difference is **{100*(mis.risk_rate-complete.risk_rate):.1f} percentage points**. This is an observed association within FFF; individual extensions/exemptions are not recorded, so absent records are proxies for completion behavior, not confirmed missed obligations.

{tables(r,'behavior_comparisons',['group','n','due_n','risk_rate','missing_mean','ontime_mean','lateness_median','score_mean'],lambda d:(d.cutoff==60)&(d.dimension=='final_result'))}

Failure and withdrawal are distinct educational outcomes; both require supportive review but are not silently equated. Successful outcomes are Pass/Distinction. Missing activity alone never defines the adverse-outcome target. Mean lateness conditions on recorded due submissions and cannot describe the behavior of non-submitters. The apparent value of missing records was challenged with a failure-only target and a seven-day logging-delay assumption, below.

## Combining behavior and marks improves ranking here

All fitted comparisons include FFF context (constant within this dataset). Behavior adds due count, missing/on-time fractions, mean positive lateness and submission recency. The score baseline includes mean early score and available score count, so it already carries some record-availability information. At day 60, combined minus score AP was **{diff.estimate:.3f}**, paired student-cluster bootstrap 95% interval **[{diff.lo:.3f}, {diff.hi:.3f}]**, using 300 replicates with fixed fitted models. These intervals describe test-population variability and omit training/availability uncertainty.

{mdtable(t[['cutoff','model','n','prevalence','ap','precision','recall','alert_rate','fp','fn','brier']])}

{tables(r,'behavior_increment_uncertainty')}

The combined signal gains over behavior-only at all three cutoffs in this FFF population. That does not establish superiority on other modules or current cohorts. The module-only baseline is constant and cannot rank students; a quantile threshold flags everyone because of ties. Its 100% alert rate is not a feasible 20% policy. A separate prevalence baseline flags nobody and exposes the no-skill reference.

## Timing and review workload must be assessed together

{tables(r,'coverage')}

At the day-60 reference threshold, flagged future withdrawals (n={int(withdraw.n)}) had a median **{withdraw['median']:.0f} days** before recorded withdrawal, IQR **{withdraw.q25:.0f}–{withdraw.q75:.0f} days**. **{int(withdraw.under_14)}** were under the proposed 14-day support interval. This measured interval does not apply to final Fail, for which remaining scheduled course duration is only a proxy; failure occurrence/publication times are unavailable.

{mdtable(lead)}

{tables(r,'model_metrics',['cutoff','capacity','split','n','threshold','alerts','alert_rate','precision','recall','fp','fn'],lambda d:d.model=='combined')}

Capacity is proposed at validation quantiles 10/20/30%, with higher observed quantiles and ties retained. Actual test alert volume changes under cohort shift; educators have not approved a capacity. No threshold was tuned against test labels. The common day-90 survivor panel below distinguishes increasing observation from changing enrollment membership; it is conditional on future survival and is not an operational eligibility rule.

{tables(r,'sensitivity',['cutoff','n','prevalence','ap','precision','recall','alert_rate'],lambda d:d.setting=='active_through_day90_common_panel')}

## Sensitivity, error concentration and probability reliability

{tables(r,'sensitivity',['cutoff','setting','model','n','prevalence','ap','precision','recall','alert_rate'],lambda d:(d.cutoff==60)&(d.setting!='active_through_day90_common_panel'))}

The +28-day mark-release and +7-day submission-recording challenges retain a combined day-60 AP near 0.718, versus 0.725 primary. Failure-only refits on final Fail versus Pass/Distinction, omitting future Withdrawn: this selected non-withdrawal population is diagnostic and cannot represent all active students. The previous-2013J-student inclusion challenge changes no FFF day-60 test rows; that absence of overlap is measured rather than assumed.

{tables(r,'subgroup_errors',['dimension','group','n','prevalence','precision','recall','alert_rate','fp','fn'],lambda d:(d.cutoff==60)&d.dimension.isin(['disability','age_band','final_result']))}

{tables(r,'calibration',mask=lambda d:d.cutoff==60)}

Demographic fields audit errors and are not model inputs. Small groups have unstable precision/recall and cannot support causal or fairness claims. Probability-bin gaps and Brier losses assess calibration; ranking value alone does not justify individual probability forecasts. A next supported decision is educator review of the chosen workload and a prospective study with actual score/log/label publication times, not automatic intervention.

## Design, preparation and feature timing

The 2013J population is split 75/25% by student with seed 20261013. Train-only median imputation, missingness indicators, scaling and categorical encoding precede fixed L2 logistic regression (C=1). Validation selects thresholds. Test is 2014J with every 2013J student excluded; repeated snapshots remain grouped, and uncertainty resamples students. Prior holdout reuse outside this run is unknown. Historical-label timing uses a checked calendar bound with an assumed 60-day publication lag; actual publication dates are unobserved. First attempts registered by start, within-scheduled-follow-up outcomes and retrospective coherent-outcome selection limit generalization to repeat/late/incoherent records.

{timing}

{tables(r,'data_quality')}

Exclusion issue counts overlap. Coverage reconciles raw, baseline and active counts. Source fields retain their meanings and raw files are never overwritten. Zero-weight formative assessments remain opportunities. Source keys/joins, denominators, cutoff rules, and train/test separation were checked; `independent_checks.csv` independently recomputes every test enrollment's due count/missing fraction directly from raw records. `parent_overlap.csv` demonstrates source overlap with OULAD; it does not prove independent validation.

All four priority questions have retrospective answers, with unavailable actual event/grade/label release times and failure lead time remaining precise boundaries. No deployment or causal benefit is established.
'''+closing(r,'complete retrospective analysis within the declared first-attempt FFF scope','[creator documentation](https://rdrr.io/github/jakubkuzilek/oulad/src/R/oulad.R) and [UCI OULAD attribution, CC BY 4.0](https://archive.ics.uci.edu/dataset/349/open+university+learning+analytics+dataset)')
  title='FFF: assessment behavior, timing and educator workload';scope='First-attempt FFF enrollments; 2013J historical train/validation and 2014J new-to-history test. Risk = future recorded withdrawal or final Fail. Source records overlap OULAD exactly; this is not independent replication. Availability times are assumed.'
  extras=['behavior_comparisons','coverage','lead_time','sensitivity','subgroup_errors','calibration','cohort_behaviors','behavior_increment_uncertainty']
  body='''<section><label>Warning cutoff <select id="cut"><option>30</option><option selected>60</option><option>90</option></select> days</label><label>Validation capacity <select id="cap"><option value="0.1">10%</option><option value="0.2" selected>20%</option><option value="0.3">30%</option></select></label><button id="reset">Reset</button><p>Cutoff changes all evidence. Capacity changes the model/workload rows; lead-time and subgroup audits stay at the labeled 20% reference.</p></section><div id="stats" class="stats"></div><section id="behavior"><h2>What early behavior differs by later outcome?</h2><div id="behaviorBars"></div><div id="behaviorRows"></div><div id="outcomeRows"></div><p>Absent records are scheduled due submissions not recorded by cutoff; extensions/exemptions are unknown. Mean fractions use only defined due denominators.</p></section><section id="models"><h2>Does behavior add to delayed marks?</h2><div id="modelBars"></div><div id="metricRows"></div><div id="uncertainty"></div><div id="increment"></div><p>All models share the same test enrollments. Scores assume submission +14 days; available-score count is included in the score baseline. Module-only ties can flag everyone, so capacity is not a hard cap.</p></section><section id="workload"><h2>Review workload and missed risk</h2><div id="workloadRows"></div><p>Validation chooses thresholds; test rates describe the resulting actual workload. No stakeholder capacity is confirmed.</p></section><section id="timing"><h2>Timing, eligibility and lead time</h2><div id="coverage"></div><div id="lead"></div><p>Lead-time audit: fixed 20% capacity. Withdrawal intervals use recorded future dates; remaining course days for Fail are proxies, not measured time to failure. The proposed useful support interval is 14 days.</p><h3>Same day-90 survivor enrollments</h3><div id="common"></div></section><section id="sensitivity"><h2>Challenge release timing and the risk definition</h2><div id="sensitivityRows"></div><p>Failure-only conditions on future non-withdrawal. The common panel conditions on survival to day 90. Neither is an operational population rule. No model was tuned against these test challenges.</p></section><section id="audit"><h2>Who is missed?</h2><label>Audit group <select id="auditGroup"><option>disability</option><option>age_band</option><option>final_result</option><option>behavior_group</option></select></label><div id="auditRows"></div><h3>Are the probabilities reliable?</h3><div id="calibrationRows"></div><p>Fixed 20% reference for errors; age/disability are not predictors. Calibration bins use all test enrollments and do not depend on capacity. Small groups are unstable.</p></section><details class="panel"><summary>All four presentations: descriptive behavior context</summary><div id="cohortRows"></div><p>First-attempt active enrollments; contextual comparisons are not extra holdouts. <a href="../results/parent_overlap.csv">Verified parent-source overlap</a> · <a href="../results/independent_checks.csv">Independent raw denominator checks</a>.</p></details>'''
  script=METRIC_JS+'''function render(){let c=Number($('cut').value),cap=Number($('cap').value),get=n=>D[n].filter(x=>x.cutoff===c),mm=get('model_metrics'),x=mm.find(x=>x.model==='combined'&&x.capacity===cap&&x.split==='test');$('stats').innerHTML=[['Test enrollments',num(x.n)],['Later adverse outcome',pc(x.prevalence)],['Flagged',num(x.alerts)+' / '+pc(x.alert_rate)],['Recall',pc(x.recall)]].map(a=>'<div class="stat">'+a[0]+'<strong>'+a[1]+'</strong></div>').join('');let bg=get('behavior_comparisons').filter(x=>x.dimension==='behavior_group').map(x=>({...x,label:x.group}));bars('behaviorBars',bg,'risk_rate','Later adverse outcomes by due-record group');tbl('behaviorRows',bg,[['group','Due-record group'],['n','n',num],['risk_rate','Later adverse outcome',pc],['fail_n','Final Fail',num],['future_withdrawn_n','Future Withdrawn',num]]);tbl('outcomeRows',get('behavior_comparisons').filter(x=>x.dimension==='final_result'),[['group','Final outcome'],['n','n',num],['due_n','Defined due n',num],['missing_mean','Mean missing fraction',pc],['ontime_mean','Mean on-time fraction',pc],['score_mean','Mean early score',dec]]);let models=mm.filter(x=>x.split==='test'&&(x.capacity===cap||x.capacity===0));bars('modelBars',models.map(x=>({...x,label:x.model})),'ap','Average precision by signal',dec);tbl('metricRows',models,MC);tbl('uncertainty',get('uncertainty'),[['comparison','Paired/ranking comparison'],['estimate','AP estimate',dec],['lo','95% low',dec],['hi','95% high',dec]]);tbl('increment',D.behavior_increment_uncertainty,[['cutoff','Cutoff day'],['estimate','Combined minus behavior AP',dec],['lo','95% low',dec],['hi','95% high',dec]]);tbl('workloadRows',mm.filter(x=>x.model==='combined'),[['split','Population'],['capacity','Validation capacity',pc],['n','n',num],['threshold','Threshold',dec],['alerts','Alerts',num],['precision','Precision',pc],['recall','Recall',pc],['fp','False positives',num],['fn','False negatives',num]]);tbl('coverage',get('coverage'),[['cohort','Presentation'],['raw_n','Raw n',num],['base_eligible_n','Baseline eligible',num],['already_withdrawn_n','Withdrawn by cutoff',num],['active_n','Active n',num],['due_n','With due opportunities',num],['test_n','Primary test n',num]]);tbl('lead',get('lead_time'),[['group','Fixed reference group'],['n','n',num],['q25','Q25 days',num],['median','Median days',num],['q75','Q75 days',num],['under_14','Under 14 days',num],['time_type','Meaning']]);tbl('common',D.sensitivity.filter(x=>x.setting==='active_through_day90_common_panel'),[['cutoff','Cutoff day'],...MC.filter(x=>!['model','fp','fn','brier'].includes(x[0]))]);tbl('sensitivityRows',get('sensitivity').filter(x=>x.setting!=='active_through_day90_common_panel'),[['setting','Challenge'],...MC]);tbl('auditRows',get('subgroup_errors').filter(x=>x.dimension===$('auditGroup').value),[['group','Group'],...MC.filter(x=>!['model','ap','brier'].includes(x[0]))]);tbl('calibrationRows',get('calibration'),[['bin','Probability bin'],['n','n',num],['mean_prediction','Mean predicted',pc],['observed_risk','Observed risk',pc]]);tbl('cohortRows',get('cohort_behaviors'),[['cohort','Presentation'],['outcome','Later outcome'],['n','n',num],['due_n','With due opportunities',num],['missing_fraction','Mean missing',pc],['ontime_fraction','Mean on-time',pc]]);}for(let id of ['cut','cap','auditGroup'])$(id).onchange=render;$('reset').onclick=()=>{$('cut').value='60';$('cap').value='0.2';$('auditGroup').value='disability';render()};render();'''
 else:
  meta=json.loads((r/'results/sampling.json').read_text());diff=u[u.cutoff==30].iloc[0];le=lead[(lead.cutoff==30)&(lead.group=='all eligible')].iloc[0];coverage=rd(r,'coverage');stability=rd(r,'sampling_stability')
  text=f'''# EdNet: prior accuracy predicts later practice difficulty, but behavior has not demonstrated added warning value

After 30 observed bundle sessions, combined prior accuracy and behavior achieved average precision **{metric.ap:.3f}** on {int(metric.n):,} held-out users, against **{p(metric.prevalence)}** later low-accuracy prevalence. Combined minus prior-score AP was only **{diff.estimate:.3f}**, paired user-bootstrap 95% interval **[{diff.lo:.3f}, {diff.hi:.3f}]**. The interval includes zero. At none of the three tested cutoffs does the paired interval establish added ranking value for behavior beyond prior accuracy and the common content-context feature. This is evidence against assuming that more behavioral features improve warnings.

The outcome is a **practice-underperformance proxy**, not course failure, withdrawal or official TOEIC attainment: correctness below 40% over the next 20 observed bundle sessions. The 40% threshold is proposed for comparison, not a documented pass standard. The local KT1 files supply presented-question times, responses and durations but no course enrollment/deadline/final academic result. Meaningful within-user future assessment investigation is possible; direct academic failure warning remains unsupported.

## A large user frame still leaves limited label coverage

The local ZIP contains **{meta['frame_users']:,} user CSVs** and {meta['archive_uncompressed_bytes']:,} uncompressed CSV bytes, verified from its central directory. A uniform sample of **{meta['sample_users']:,} users** without replacement (seed 20261013, sampling fraction {p(meta['sampling_fraction'])}) yielded 6,061,678 response records. Sampling limits repeated decoding over 784,309 files and permits multi-cutoff uncertainty/error checks on a fixed user sample; it yields about 1,000–1,300 eligible held-out users per cutoff, sufficient for bounded prevalence/workload estimates but limited for small incremental AP claims. This is user sampling, not the first files in directory order. Sampled reads are ordered by archive offset for efficient I/O. The complete frame fingerprint is saved; sampled file CRCs/IDs stay in ignored `prepared/`.

{mdtable(coverage)}

Only **{p(coverage[coverage.cutoff==30].iloc[0].coverage)}** of sampled users supply an eligible 30-bundle prefix and 20-bundle future window satisfying the timing condition. Those who stop before the outcome window are **unlabeled**, not failed or withdrawn. Therefore these findings concern continuing practice users with sufficient follow-up; they cannot be applied to all app users or used to infer dropout. Coverage differs across cutoffs and overlap exclusions, so naive time comparisons can mix behavior change and population selection.

{tables(r,'data_quality')}

Prefix completion is approximated as question presentation time plus recorded elapsed duration; first future presentation must occur strictly after the maximum prefix completion estimate. The 5,008 excluded overlapping windows are snapshots, not distinct people, and can affect several cutoffs for one user. Actual response-completion/insertion timestamps are unavailable. Because published timestamps are shifted without a verified common real-world calendar, evaluation holds out users within the local snapshot rather than claiming prospective calendar-cohort deployment.

## Compare behavior with prior performance on identical users

Behavior includes median/IQR bundle duration, median inter-bundle gap, prefix span and repeated-question exposure fraction. Bundle durations use one maximum elapsed value per `solving_id` group; repeated duration records for multi-question bundles are never summed as independent working time. Repeat exposure does not mean answer revisions. Prior performance is mean prefix correctness. All fitted models share early part-7 exposure share as a simple content-context feature; this is not complete adjustment for question difficulty or adaptive assignment.

{mdtable(t[['cutoff','model','n','prevalence','ap','precision','recall','alert_rate','fp','fn','brier']])}

{mdtable(u)}

The fixed low-prior-accuracy rule and prevalence baseline make the comparison interpretable. AP measures ranking, not the fraction correctly classified. At 60 bundles, prior accuracy AP exceeds combined, although the paired interval still includes zero. Strong early performance persistence is compatible with ability, repeated item exposure and adaptive item selection; it is not evidence that changing response speed or spacing changes academic outcomes.

{tables(r,'behavior_comparisons',mask=lambda d:d.cutoff==30)}

## Review burden and short lead time limit usefulness

At the 30-bundle reference threshold (selected for a proposed 20% validation review quantile), **{int(metric.alerts)}** users are flagged ({p(metric.alert_rate)}), **{int(metric.tp)}** later proxy-positive users caught, **{int(metric.fp)}** false positives and **{int(metric.fn)}** missed. Precision is **{p(metric.precision)}**, so most flags are false positives against this particular <40% proxy. Capacity is assumed, not stakeholder-approved, and test volume can change under shift/ties.

{tables(r,'model_metrics',['cutoff','split','capacity','n','threshold','alerts','precision','recall','fp','fn'],lambda d:d.model=='combined')}

The median time from the 30-bundle warning point to the **first future question** is **{le.first_hours_median*3600:.0f} seconds**; {int(le.first_under_1hour_n):,}/{int(le.n):,} eligible held-out users encounter it within one hour. The median time to completion of the entire 20-bundle outcome window is {le.last_days_median:.2f} days. Finishing a future window later does not imply that its earliest difficulties can be prevented: lead time to the next question is often too short for conventional educator outreach. No useful support-time requirement was supplied.

{mdtable(lead)}

## Challenge repetition, the threshold and sample instability

Could repeated question exposure account for the signal? The novel-future-item sensitivity uses future questions not seen in the prefix, requiring at least ten such responses; this changes the selected label population and still does not control unseen item difficulty. The <50% alternate proxy changes prevalence and practical error rates; its threshold is selected on its own validation labels and is not a retuned primary model.

{tables(r,'sensitivity',mask=lambda d:d.cutoff==30)}

The random sample-halves check uses the same fitted model/threshold on independently assigned halves of held-out users. It exposes substantial test AP variation, including day-30 combined AP 0.150 versus 0.264. The claimed extra behavior value remains uncertain; no stable improvement is inferred from the full-sample point estimate.

{mdtable(stability)}

{tables(r,'future_part_errors',mask=lambda d:d.cutoff==30)}

Future dominant part is an **outcome-window audit label**, never a predictor. It reveals content-related error differences but cannot identify difficulty-independent effects. Sex/disability or institutional groups are not available and are not invented.

{tables(r,'calibration',mask=lambda d:d.cutoff==30)}

## Timing, split and reproducibility definitions

| Quantity | Source / formula | Timing and limits |
|---|---|---|
| Observation unit | One sampled user at prefix 10, 30 or 60 `solving_id` bundles | All snapshots for a user stay in one split |
| Prefix completion | max(`timestamp` + `elapsed_time`) over prefix responses | Approximation; presentation timestamp is not submission time |
| Future target | mean(response == `correct_answer`) across next 20 bundle sessions <0.4 | Uses only future responses; no academic pass-standard claim |
| Behavior | One duration per bundle; gaps; span; repeated question exposure fraction | Prefix only; duration not verified active work time |
| Performance | Prefix accuracy joined many-to-one to question answer key | Assumes correct answers/feedback usable after prefix completion |
| Shared context | Prefix share of question `part == 7` | Known prefix metadata; not complete item-difficulty adjustment |
| Lead time | First future presentation / last future completion minus prefix completion | No official result or intervention deadline |

The 50,000 sampled users are split 70/15/15 before cutoff eligibility with seed 20261013. Median imputation, indicators and standardization fit train only; models are fixed L2 logistic regression (C=1), no test tuning. Validation chooses 10/20/30% thresholds; all comparisons use identical eligible users. Paired AP intervals resample held-out users 500 times with fixed fitted models. Prior external holdout reuse is unknown. Bad/unmatched records exclude an affected user's trajectory rather than silently shorten it; none were found in this sample. Source CRC checks occur on archive reads, and question IDs are unique. No student/user identifiers appear in public artifacts.

The four priority questions have bounded proxy-study answers: behavior associations are observed, added value is not demonstrated, coverage/lead time are limited, and workload/errors are quantified. Course academic risk, dropout and prospective calendar transport remain unsupported. A prospective evaluation with official outcomes and known feedback/insertion times would be needed before treating these estimates as academic warnings.
'''+closing(r,'partial analysis of the broader academic-risk objective; completed sampled practice-underperformance investigation','[EdNet creators’ schema and release notes](https://github.com/riiid/ednet)')
  title='EdNet: practice difficulty, added value and warning lead time';scope='Sampled KT1 users with sufficient continuing practice. Outcome = next-20-bundle accuracy below 40%, a proposed practice proxy, not course failure or TOEIC attainment. Held-out users within a shifted-timestamp snapshot; prospective calendar deployment is not established.'
  extras=['behavior_comparisons','coverage','lead_time','sensitivity','future_part_errors','calibration','sampling_stability']
  body='''<section><label>Observed bundle sessions <select id="cut"><option>10</option><option selected>30</option><option>60</option></select></label><label>Validation review capacity <select id="cap"><option value="0.1">10%</option><option value="0.2" selected>20%</option><option value="0.3">30%</option></select></label><button id="reset">Reset</button><p>Bundle sessions group question rows by solving_id. Cutoff changes the eligible continuing-user population. Capacity affects model/workload estimates; subgroup, stability and lead-time audits remain at the fixed 20% reference.</p></section><div id="stats" class="stats"></div><section id="coverage"><h2>Who has enough future practice to be evaluated?</h2><div id="coverageRows"></div><p>50,000 users sampled uniformly from 784,309 local user CSVs; six million sampled response rows. Users with insufficient follow-up are unlabeled, not adverse outcomes. Overlap exclusions require future questions after estimated prefix completion.</p></section><section id="models"><h2>Does behavior improve on prior accuracy?</h2><div id="modelBars"></div><div id="metricRows"></div><div id="uncertainty"></div><p>Each interval compares combined minus score AP using a paired held-out-user bootstrap. All three intervals include zero: added behavior value is not demonstrated. All models share early part-7 exposure context; adaptive question difficulty remains incompletely controlled.</p><div id="behaviorRows"></div></section><section id="timing"><h2>Does the warning leave time to act?</h2><div id="lead"></div><p>First-future-question intervals are often seconds. Time to the end of the entire outcome window is a different quantity and does not establish time to prevent its earliest difficulty. Fixed 20% reference; durations approximate completion from presentation timestamp plus elapsed_time.</p></section><section id="workload"><h2>How many flags are true later difficulties?</h2><div id="workloadRows"></div><p>False positives are users above the proposed future-accuracy threshold; they are not confirmed academically safe. Test outcomes do not choose the alert threshold. Most reference flags are false positives against the <40% proxy.</p></section><section id="sensitivity"><h2>Challenge the target, repetition and sampling stability</h2><div id="sensitivityRows"></div><div id="stability"></div><p>Novel-future-item labels omit questions seen in the prefix and require ten novel responses. The 50% threshold is a different proposed proxy. Sample-half variability limits confidence in small improvements; no model is selected on these challenges.</p></section><section id="audit"><h2>Content-related errors and probability reliability</h2><div id="partRows"></div><div id="calibrationRows"></div><p>Future dominant question part is an audit label, never a predictor. Fixed 20% reference for errors; calibration is independent of threshold. No demographic attributes or official academic outcomes were supplied.</p></section>'''
  script=METRIC_JS+'''function render(){let c=Number($('cut').value),cap=Number($('cap').value),get=n=>D[n].filter(x=>x.cutoff===c),mm=get('model_metrics'),x=mm.find(x=>x.model==='combined'&&x.capacity===cap&&x.split==='test');$('stats').innerHTML=[['Eligible held-out users',num(x.n)],['Future proxy-positive',pc(x.prevalence)],['Flagged for review',num(x.alerts)+' / '+pc(x.alert_rate)],['Precision',pc(x.precision)]].map(a=>'<div class="stat">'+a[0]+'<strong>'+a[1]+'</strong></div>').join('');tbl('coverageRows',D.coverage,[['cutoff','Prefix bundles'],['sampled_users','Sampled users',num],['eligible_users','Sufficient future window',num],['coverage','Sample coverage',pc],['train_n','Train',num],['validation_n','Validation',num],['test_n','Held-out users',num]]);let models=mm.filter(x=>x.split==='test'&&(x.capacity===cap||x.capacity===0));bars('modelBars',models.map(x=>({...x,label:x.model})),'ap','Average precision by signal',dec);tbl('metricRows',models,MC);tbl('uncertainty',D.uncertainty,[['cutoff','Prefix bundles'],['estimate','Combined minus score AP',dec],['lo','95% low',dec],['hi','95% high',dec]]);tbl('behaviorRows',get('behavior_comparisons'),[['group','Comparison'],['n','n',num],['future_risk','Future proxy risk',pc],['elapsed_median','Median bundle seconds',dec],['gap_median','Median gap hours',dec],['repeat_mean','Mean repeated exposure',pc]]);tbl('lead',get('lead_time'),[['group','Fixed reference group'],['n','n',num],['first_hours_median','Median to next question (hours)',dec],['first_hours_q25','Q25 hours',dec],['first_hours_q75','Q75 hours',dec],['last_days_median','Median to window end (days)',dec],['first_under_1hour_n','Under 1 hour',num]]);tbl('workloadRows',mm.filter(x=>x.model==='combined'),[['split','Population'],['capacity','Validation capacity',pc],['n','n',num],['threshold','Threshold',dec],['alerts','Alerts',num],['precision','Precision',pc],['recall','Recall',pc],['fp','False positives',num],['fn','False negatives',num]]);tbl('sensitivityRows',get('sensitivity'),[['setting','Executed challenge'],...MC]);tbl('stability',get('sampling_stability'),[['half','Random sample half'],...MC.filter(x=>x[0]!=='model')]);tbl('partRows',get('future_part_errors'),[['future_dominant_part','Future dominant part'],...MC.filter(x=>x[0]!=='model')]);tbl('calibrationRows',get('calibration'),[['bin','Predicted-risk bin'],['n','n',num],['predicted','Mean predicted',pc],['observed','Observed proxy rate',pc]]);}for(let id of ['cut','cap'])$(id).onchange=render;$('reset').onclick=()=>{$('cut').value='30';$('cap').value='0.2';render()};render();'''
 report(r,text);dashboard(r,title,scope,body,script,['model_metrics','uncertainty']+extras)

def build_mooc():
 r,d=setup('mooccubex');dist=rd(r,'opportunity_distribution');rel=rd(r,'relation_quality');link=rd(r,'content_linkage');join=rd(r,'field_join_coverage').iloc[0];manual=rd(r,'manual_label_sensitivity');ex=dist[dist.measure=='exercises'].iloc[0]
 text=f'''# MOOCCubeX: assessment content is visible, but this snapshot cannot support student early warnings

The actual local snapshot contains **{int(ex.courses):,} courses** and **{int(ex.total):,} exercise-container memberships**, yet it lacks the documented student–problem event file, exercise–problem mapping, problem entities and linked future academic outcomes. These are concrete blockers: course content and concept edges cannot establish who submitted an assessment, when a score became available, or which student later struggled. No risk model, accuracy score, lead time or alert list is fabricated.

This is a **feasibility assessment with a completed assessment-content investigation**, not a student-warning validation. The narrower investigation quantifies content opportunity heterogeneity, linkage coverage and source anomalies so an analyst can identify what additional extraction is actually needed. It retains the project purpose rather than replacing it with general course popularity or institutional ranking.

## Exercise opportunities vary substantially even before observing students

**{int(ex.zero_n)} courses** ({p(ex.zero_n/ex.courses)}) have no exercise container in their local resource list. The median is **{ex['median']:.0f} exercise containers**, IQR {ex.q25:.0f}–{ex.q75:.0f}; the mean is {ex['mean']:.1f}, and the 95th percentile is {ex.p95:.0f}. Content counts are skewed, so the mean alone would misdescribe typical course assessment infrastructure. An exercise container is a group of problems, not a completed student submission and not necessarily a required assessment.

{mdtable(dist)}

The 271,043 resource memberships decompose into 203,718 videos and 67,325 exercise containers, with no other prefixes or duplicate course–resource memberships. Chapters express content order, not deadlines. The code validates decomposition and uniqueness rather than converting resource position into invented warning time.

## Concept edges cover only part of the course universe

{mdtable(link)}

Concept-to-course edges reach **887 of 3,781 courses (23.5%)**. Only 43.9% of concepts attached to the observed problem IDs also appear in the concept–course relation. This is semantic overlap, not an exercise-to-problem linkage: linking a problem and course merely because they share a concept would create many-to-many fanout and unsupported assessment assignments. The missing exercise–problem mapping is necessary before constructing applicable student opportunity denominators.

{tables(r,'evidence_requirements')}

Both documented exercise–problem filename variants were checked and neither is present. The local user–reply and comment–reply edges lack the event text/time entities required to reconstruct assessment behavior. Help-query records provide user/type/question strings, not answer correctness or a linked academic result. Their measured coverage below cannot replace missing assessment logs.

{tables(r,'help_query_types')}

## Label coverage and repeated edges can distort a feasibility conclusion

Initial field joining assumed every manually labeled course would be in the local course file. The executed check found **{int(join.unmatched_memberships)} unmatched field memberships on {int(join.unmatched_courses)} courses**, out of {int(join.manual_courses)} manually labeled course IDs. The pipeline was corrected to retain this coverage evidence and restrict field summaries to the {int(join.matched_courses)} matched courses; it does not silently drop unmatched courses or infer resources for them.

{tables(r,'field_join_coverage')}

{mdtable(manual)}

Manually labeled matched courses have exercise coverage **96.7%**, versus **82.7%** among courses without a manual label. This executed sensitivity shows that analyzing only manually labeled courses would overstate exercise availability for the full local course universe. “No manual label” can still have field information in course entities; manual and other field sources are deliberately not treated as interchangeable. Courses can have multiple manual field memberships, so field rows are not independent courses and cannot be summed as a population.

{tables(r,'field_context',mask=lambda d:d.courses>=10)}

The concept–problem relation has 4,039 repeated pairs (12.2% of raw rows); course–teacher has 51,186 repeated pairs (52.7%). Unique-pair views are appropriate for linkage coverage, with raw and unique row counts retained. These repetitions are not extra student assessment attempts. Other mappings have legitimate many-to-many structure; uniqueness of a pair does not establish one-to-one entities.

{mdtable(rel)}

## What would make early warning answerable?

| Priority question | Actual support | Missing evidence |
|---|---|---|
| Early behavior associated with later academic risk | Unsupported at student level | User–problem attempts with submission times, scores and course linkage; later academic result |
| How early, with useful support time? | Content chapter order only | Enrollment start, applicable deadlines, event/availability timestamps, outcome timing |
| Added value beyond prior scores? | Unsupported | Correct early scores and a temporally separate later outcome |
| Misses, false flags and review volume? | Unsupported | Valid labels and held-out temporal/student evaluation |
| Assessment infrastructure feasibility | Answered by full local course/resource and relation investigation | Exercise–problem mapping and local problem entities still absent |

Raw JSONL and text relations are preserved; keys, malformed lines, decomposition and join cardinality were checked. No personal names, query text, or identifiable user records appear in the dashboard. All relevant course/resource/concept tables were read in full; no convenient small sample substitutes for the local scope. Documentation distinguishes `Ex_` exercise containers, `Pm_` problems and `U_` users; these namespaces are not interchangeable. Source scope is the local partial extraction, not an assumed full upstream release.

The next useful evidence is an authorized extraction of the missing linked user/problem/outcome files and their timing metadata. More content charts cannot validate warnings. Additional datasets were not acquired in this run.
'''+closing(r,'feasibility assessment; completed bounded assessment-content investigation','[local course schema](../../datasets/mooccubex/docs/course-en.md), [local user schema](../../datasets/mooccubex/docs/user-en.md), and the [MOOCCubeX creators’ repository](https://github.com/THU-KEG/MOOCCubeX)')
 report(r,text)
 body='''<section id="gaps"><h2>Which links needed for early warning are actually present?</h2><div id="gapRows"></div><p>Missing user–problem events and future outcomes block student warnings. Neither shared concepts, chapter positions, help queries nor reply edges supplies that missing evidence.</p></section><section id="opportunities"><h2>How uneven is assessment content?</h2><div id="distribution"></div><div id="exerciseChart"></div><p>The unit is a course resource list. Exercise containers group problems; they are not submissions, required obligations or timed deadlines. Quantiles show skewness that the mean hides.</p></section><section id="linkage"><h2>Can concepts establish applicable assessment opportunities?</h2><div id="linkRows"></div><p>Concept overlap is semantic context and does not directly map exercise containers to problems. It cannot justify a many-to-many course/problem join for students.</p></section><section id="fields"><h2>Does manual labeling overstate exercise coverage?</h2><div id="manualChart"></div><div id="manualRows"></div><div id="joinRows"></div><label>Minimum matched courses per field <select id="minCourses"><option>5</option><option selected>10</option><option>30</option><option>50</option></select></label><button id="reset">Reset</button><div id="fieldRows"></div><p>Only matched manually labeled courses enter these field summaries; 85 manual course IDs are absent from the course entities. Courses may belong to multiple fields, so field counts cannot be summed as independent courses.</p></section><section id="quality"><h2>Repeated edges are not repeated student attempts</h2><div id="relationRows"></div><div id="queryRows"></div><p>Unique-pair coverage removes exact duplicate relation edges while preserving raw counts. User help-query types have no correctness, deadlines or academic outcomes. No risk score is shown because none is supported.</p></section>'''
 script='''function render(){tbl('gapRows',D.evidence_requirements,[['required_file','Required local file'],['present','Present'],['needed_for','Needed for']]);tbl('distribution',D.opportunity_distribution,[['measure','Resource type'],['courses','Courses',num],['zero_n','Courses with zero',num],['mean','Mean',dec],['median','Median',dec],['q25','Q25',dec],['q75','Q75',dec],['p95','95th percentile',dec],['total','Memberships',num]]);let ex=D.opportunity_distribution.find(x=>x.measure==='exercises');bars('exerciseChart',[{label:'Courses with exercise content',coverage:1-ex.zero_n/ex.courses},{label:'Courses without exercise content',coverage:ex.zero_n/ex.courses}],'coverage','Exercise-container presence across local courses');tbl('linkRows',D.content_linkage,[['check','Linkage quantity'],['numerator','Numerator',num],['denominator','Denominator',num],['fraction','Fraction',pc]]);bars('manualChart',D.manual_label_sensitivity.map(x=>({...x,label:x.group})),'exercise_coverage','Exercise coverage with and without manual course labels');tbl('manualRows',D.manual_label_sensitivity,[['group','Course group'],['n','Courses',num],['mean_exercises','Mean exercise containers',dec],['median_exercises','Median exercise containers',dec],['exercise_coverage','At least one exercise',pc]]);tbl('joinRows',D.field_join_coverage,[['manual_courses','Manual course ids',num],['matched_courses','Matched course ids',num],['unmatched_courses','Unmatched course ids',num],['unmatched_memberships','Unmatched field memberships',num]]);tbl('fieldRows',D.field_context.filter(x=>x.courses>=Number($('minCourses').value)),[['field','Manual field'],['courses','Matched courses',num],['exercise_coverage','At least one exercise',pc],['median_exercises','Median exercise containers',dec],['median_videos','Median videos',dec]]);tbl('relationRows',D.relation_quality,[['relation','Relation'],['raw_rows','Raw rows',num],['unique_pairs','Unique pairs',num],['duplicate_rows','Repeated pairs',num],['duplicate_fraction','Duplicate share',pc],['left_entities','Distinct left entities',num],['right_entities','Distinct right entities',num]]);tbl('queryRows',D.help_query_types,[['type','Help-query type'],['rows','Records',num],['users','Distinct users',num],['distinct_questions','Distinct query strings',num]]);} $('minCourses').onchange=render;$('reset').onclick=()=>{$('minCourses').value='10';render()};render();'''
 dashboard(r,'MOOCCubeX: what the local assessment-content snapshot can support','Feasibility assessment. The local files contain course resources and semantic/help relations, with no linked student assessment trajectories or later academic outcomes. Content evidence is not a validated student warning.',body,script,['evidence_requirements','opportunity_distribution','content_linkage','manual_label_sensitivity','field_join_coverage','field_context','relation_quality','help_query_types'])

def build_scorecard():
 r,d=setup('college-scorecard');out=rd(r,'outcome_definitions');whole=out[out.sector=='All reported sectors'];completion=whole[whole.measure=='150% completion'];facts=rd(r,'grain_audit')
 text=f'''# College Scorecard: aggregate academic outcomes are available, but they cannot label early student risk

The local snapshot contains **6,273 institutions** and **227,980 institution–field–credential records**. It has completion and retention aggregates but no student-level assessment submissions, deadlines, availability times or later linked academic results. It cannot answer whether a student's early assessment behavior identifies future risk. No institution-ranking model or synthetic student label is substituted.

The bounded investigation asks how these outcome aggregates differ in grain, cohort and denominator, and whether coverage/weighting can mislead an early-warning design. The result is a **feasibility assessment with substantive outcome-definition context**, not a completed individual warning study.

## Completion and retention describe different populations

The completion fields (`C150_4`, `C150_L4`) describe completion within 150% of expected program time for full-time, first-time degree/certificate-seeking cohorts, with four-year and less-than-four-year metric families. Retention describes return after the first year, separating full-time and part-time students; the four-year retention population is bachelor's degree-seeking. The official documentation bases metric family on IPEDS institution level, **not predominant award code `PREDDEG`**. The analysis therefore uses each reported metric in its own family rather than imposing PREDDEG as a filter.

{mdtable(whole[['family','measure','raw_institutions','valid_institutions','coverage','unweighted_mean','median','weighted_mean','cohort_denominator','weight_meaning']])}

Coverage here is valid reporting rows divided by **all 6,273 snapshot institutions**, and includes institutions for which a metric family is inapplicable. It is not a nonresponse rate among eligible institutions. “NULL” and suppression tokens are retained in the missing-token audit; the same missing token cannot by itself distinguish inapplicability from unreported data.

Neither 1 − retention nor 1 − completion is a defensible individual Fail/Withdrawn label. Students can transfer or finish elsewhere, take longer, or belong to a different underlying cohort. Same institution IDs do not make completion and retention longitudinal measurements of the same students. The latest-cohort file can contain different measurement periods across fields; the exact local per-field vintage is not verified and is not inferred from the filename or the current website.

## Institution averages and cohort-weighted averages answer different questions

Four-year completion averages **52.1% across reporting institutions**, but **60.7% weighted by their completion cohort sizes** (`D150_4`, 1,857,898 cohort members). Less-than-four-year completion reverses that pattern: **62.1% institution-average versus 48.4% cohort-weighted** (`D150_L4`, 686,651 members). These are different estimands, not contradictory calculations. The reversal implies that institution size and sector composition matter; an unweighted institutional summary must not be described as an average student's risk.

{mdtable(out[out.measure=='150% completion'][['family','sector','valid_institutions','unweighted_mean','weighted_mean','cohort_denominator']])}

The executed small-cohort follow-up removes institutions with completion cohorts below 30 and 100, without redefining raw data or claiming small institutions are erroneous. Less-than-four-year institution means fall from 62.1% to 52.9% at a 100-member minimum, while the cohort-weighted estimate is 46.5%. Thus tiny cohorts materially affect the institution estimand, and removing them changes its population. Four-year cohort-weighted completion is comparatively stable under these restrictions.

{tables(r,'small_cohort_sensitivity',mask=lambda d:d.sector=='All reported sectors')}

Weights are **matching outcome cohort denominators**, never `UGDS` undergraduate enrollment, which represents a different population. Weighted numerators use published rounded rates times cohort counts and are approximate; they are not reconstructed exact person counts. No artificial confidence interval is attached to this full-snapshot accounting comparison.

## Pooled suppression changes what can be observed

Non-pooled retention lacks its matching cohort count in this selected local schema, so its average remains an institution-level mean. The suppressed pooled full-time retention fields do have supplied pooled denominators; they are analyzed as a distinct reporting measure. Four-year pooled retention is 74.2% institution-average versus 81.8% cohort-weighted; the less-than-four-year values are 71.2% versus 66.4%. These pooled cohorts are not silently equated to the non-pooled cohorts or completion cohorts.

{mdtable(out[out.measure=='Suppressed pooled FT retention'][['family','sector','valid_institutions','coverage','unweighted_mean','weighted_mean','cohort_denominator']])}

{tables(r,'missing_tokens',mask=lambda d:d.field.isin(['C150_4','C150_L4','RET_FT4','RET_FTL4','RET_FT4_POOLED_SUPP','RET_FTL4_POOLED_SUPP']))}

Official documentation explains rolling pooled retention and small-cohort suppression; the code preserves suppressed values as missing rather than zero. Because withheld outcomes are not observed, no warning accuracy or person-level alert volume can be validated from these aggregates.

## A common institution does not establish common students

{tables(r,'same_institution_comparison',mask=lambda d:d.sector=='All reported sectors')}

These same-institution comparisons are ecological diagnostics only. Spearman correlation across institution rates does not establish whether early assessment behavior predicts a later student outcome. Differences in cohort, reporting population, transfer and program duration remain unresolved by joining `UNITID`.

{tables(r,'predominant_vs_metric_coverage')}

The field-of-study table has a separate compound grain (`UNITID`, `OPEID6`, `CIPCODE`, `CREDLEV`) with no duplicate keys in the inspected local extract. It includes 7,020 rows without a numeric UNITID and aggregates partly by institutional grouping. It is not a second independent student sample; joining its many program rows to institutions without re-aggregation would fan out institutional metrics. No such join is performed.

{mdtable(facts)}

## What is missing for the project?

| Priority question | Local support | Exact blocker |
|---|---|---|
| Early assessment behavior versus future risk | Unsupported | Student/course identifiers, assessment events, submissions and scores absent |
| Warning cutoffs and support lead time | Unsupported | Applicable deadlines, observation/availability times and linked future event times absent |
| Added value over prior scores | Unsupported | No early individual score history or valid future student labels |
| False flags, missed students and review burden | Unsupported | No individual labels or held-out student/time cohort |
| Academic outcome suitability | Answered contextually | Aggregate reporting cohorts cannot be reinterpreted as individual Fail/Withdrawn |

All institution/program rows were scanned with relevant selected columns. Source preservation, institution key uniqueness, valid rate ranges, uninflated institutional denominator and an independent weighted completion recomputation were checked. No silent imputation, institution exclusion or outcome suppression reversal occurs. Sector comparisons are contextual denominator checks, not a ranking or causal judgment. The missing student/event/outcome linkage must be obtained from a separately authorized institutional source before this dataset can participate in an early-warning model.
'''+closing(r,'feasibility assessment; completed aggregate academic-outcome suitability investigation','[U.S. Department of Education institution-level methodology](https://collegescorecard.ed.gov/files/InstitutionDataDocumentation.pdf), with field definitions/retention details verified through indexed official text when direct PDF access returned 403')
 report(r,text)
 body='''<section id="definitions"><h2>Which outcome and denominator are being compared?</h2><label>Reporting metric family <select id="family"><option>Four-year metric</option><option>Less-than-four-year metric</option></select></label><label>Sector <select id="sector"><option>All reported sectors</option><option>Public</option><option>Private nonprofit</option><option>Private for-profit</option></select></label><button id="reset">Reset</button><div id="outcomeRows"></div><p>Coverage denominator is all snapshot institutions in the selected sector, including inapplicable metric families. Completion uses full-time first-time cohorts; retention uses prior-year return cohorts. IPEDS level defines reporting family; PREDDEG is not used to force the population.</p></section><section id="weights"><h2>Institution average versus relevant cohort average</h2><div id="weightBars"></div><div id="weightRows"></div><p>These compare different estimands. D150 cohort sizes weight completion; pooled retention uses matching pooled retention denominators. UGDS is not a matching denominator. Non-pooled retention has no matching cohort count in these selected local fields. Rounded rates make weighted totals approximate.</p></section><section id="small"><h2>Do tiny completion cohorts change the interpretation?</h2><div id="smallRows"></div><p>Minimum cohort restrictions change the population; small cohorts are not automatically invalid. Observe both institution and cohort-weighted means.</p></section><section id="cohorts"><h2>Same institution does not mean the same students</h2><div id="pairRows"></div><p>These ecological rate correlations cannot identify individual risk. Non-completion can include transfer, later completion or different cohorts; it is not a confirmed Fail/Withdrawn label.</p></section><section id="suppression"><h2>What values are missing or suppressed?</h2><div id="missingRows"></div><div id="predRows"></div><p>NULL includes unreported/inapplicable data; PrivacySuppressed is never recoded to zero. Pooled and unpooled rates have different cohorts. Exact per-field local cohort vintage is not verified.</p></section><section id="grain"><h2>Why the program table cannot create student warning labels</h2><div id="grainRows"></div><p>No student assessment events, deadlines, score availability or future academic result linkage is present. Program rows are not independent student records and are not joined to inflate institutional denominators. No risk score or alert accuracy is shown.</p></section>'''
 script='''function render(){let family=$('family').value,sector=$('sector').value,rows=D.outcome_definitions.filter(x=>x.family===family&&x.sector===sector);tbl('outcomeRows',rows,[['measure','Reported measure'],['raw_institutions','All sector institutions',num],['valid_institutions','Valid reporting rows',num],['coverage','Share of all snapshot rows',pc],['median','Median institution rate',pc]]);let comp=rows.find(x=>x.measure==='150% completion'),pooled=rows.find(x=>x.measure==='Suppressed pooled FT retention');let barsData=[];for(let x of [comp,pooled])if(x){barsData.push({label:x.measure+' / institution mean',rate:x.unweighted_mean});barsData.push({label:x.measure+' / cohort weighted',rate:x.weighted_mean});}bars('weightBars',barsData,'rate','Institution and matching-cohort outcome averages');tbl('weightRows',rows,[['measure','Measure'],['unweighted_mean','Institution mean',pc],['weighted_mean','Matching-cohort mean',pc],['weighted_institutions','Weighted reporting n',num],['cohort_denominator','Cohort denominator',num],['weight_meaning','Denominator field / boundary']]);tbl('smallRows',D.small_cohort_sensitivity.filter(x=>x.family===family&&x.sector===sector),[['min_completion_cohort','Minimum completion cohort'],['institutions','Institutions',num],['completion_mean','Institution mean',pc],['completion_weighted','Cohort weighted',pc],['cohort_students','Cohort members',num]]);tbl('pairRows',D.same_institution_comparison.filter(x=>x.family===family&&x.sector===sector),[['both_metrics_n','Institutions with both',num],['completion_only_n','Completion only',num],['retention_only_n','Retention only',num],['institution_spearman','Ecological Spearman',dec],['median_completion','Median completion',pc],['median_retention','Median retention',pc]]);let fields=family==='Four-year metric'?['C150_4','RET_FT4','RET_PT4','RET_FT4_POOLED_SUPP']:['C150_L4','RET_FTL4','RET_PTL4','RET_FTL4_POOLED_SUPP'];tbl('missingRows',D.missing_tokens.filter(x=>fields.includes(x.field)),[['field','Field (all sectors, fixed reference)'],['token','Missing token'],['rows','Rows',num]]);tbl('predRows',D.predominant_vs_metric_coverage,[['predominant_award_code','Predominant award code'],['institutions','All institutions',num],['completion_4_n','Four-year completion rows',num],['completion_l4_n','Less-than-four-year rows',num]]);tbl('grainRows',D.grain_audit,[['quantity','Grain/coverage quantity (fixed full snapshot)'],['n','Count',num]]);}for(let id of ['family','sector'])$(id).onchange=render;$('reset').onclick=()=>{$('family').value='Four-year metric';$('sector').value='All reported sectors';render()};render();'''
 dashboard(r,'College Scorecard: outcome definitions before student-risk labels','Feasibility and contextual analysis only. Institution/program aggregates do not contain student assessment trajectories or future academic-risk linkage. Reporting cohorts differ; 1 − completion/retention is not an individual Fail/Withdrawn label.',body,script,['outcome_definitions','small_cohort_sensitivity','same_institution_comparison','missing_tokens','predominant_vs_metric_coverage','grain_audit'])

def build_survey(name):
 r,d=setup(name);talis=name=='talis-2024';est=rd(r,'practice_estimates');pair=rd(r,'paired_feedback');meta=json.loads((r/'results/metadata.json').read_text());country='AUS'
 if talis:
  ref=est[(est.country=='AUS')&(est.level==2)].set_index('item');paired=pair[(pair.country=='AUS')&(pair.level==2)].iloc[0]
  refrows=est[(est.country=='AUS')&(est.level==2)];example=ref.loc['TT4G53C'];naive=example.unweighted*example.valid_n/example.n
  text=f'''# TALIS 2024: frequent assessment feedback coexists with training needs; student early-warning validity is unobservable

The local teacher files contain **278,383 respondents**, exactly matching the combined export's respondent keys, levels and selected assessment-practice items. The level files and combined file are overlapping exports and are **not concatenated as independent samples**. The lower-secondary teacher file has 194,521 respondents across 55 education-system codes, with additional level-1/3 domains. The files contain cross-sectional teacher/principal reports, not student assessment events and later linked results; therefore direct academic-risk warning, lead time and alert accuracy cannot be estimated.

A bounded assessment-practice context study is nevertheless supported. In the illustrative **Australia / ISCED 2** domain, **{p(ref.loc['TT4G53C'].weighted)}** of valid weighted respondents report frequent/always improvement feedback, while **{p(ref.loc['TT4G53D'].weighted)}** report student self-assessment and **{p(ref.loc['TT4G52C'].weighted)}** digital feedback. High feedback prevalence does not mean that a school has the event histories or outcome linkage required for warning analytics.

## Practice differences are substantive, not identifier counts

{mdtable(refrows[['item','meaning','n','valid_n','weighted','unweighted','lo','hi','adjudication']])}

Assessment-practice percentages use valid responses 1–4, with 3/4 indicating frequent/always use; professional-learning need percentages use 3/4 for moderate/high need. The units and denominators differ from a student risk rate. In Australia/ISCED 2, assessment-practice training need is **{p(ref.loc['TT4G24D'].weighted)}** and need in analysis/use of assessments **{p(ref.loc['TT4G24M'].weighted)}**. These areas are relevant to reviewing an early-warning workflow, but do not identify students or prove that training prevents academic failure.

The executed paired follow-up compares immediate task feedback with improvement feedback on the **same {int(paired.valid_n):,} valid respondents**, rather than subtracting rates from different item samples. The difference is **{100*paired.weighted:.1f} percentage points**, 95% Fay-BRR interval **[{100*paired.lo:.1f}, {100*paired.hi:.1f}]**. It includes zero; this comparison does not establish that one form is more prevalent in this domain. Other practice gaps, including digital feedback and self-assessment, are visible in the full country/level table and dashboard without selecting countries for a ranking.

{mdtable(pair[(pair.country=='AUS')&(pair.level==2)])}

## Rotated questionnaire missingness can halve a naive prevalence

In the Australian reference domain, {int(example.valid_n):,}/{int(example.n):,} teachers have a valid improvement-feedback response. The item is not administered identically on all forms. Among valid responses, the unweighted frequent/always proportion is **{p(example.unweighted)}**; treating every absent/nonvalid response as “does not provide feedback” would yield **{p(naive)}**. That naive number is invalid because it converts questionnaire design and nonresponse into behavior.

{tables(r,'form_coverage',mask=lambda d:(d.level==2)&d.item.isin(['TT4G53C','TT4G24D','TT4G24M']))}

Across the local lower-secondary extract, form 1 has **zero valid responses** for these selected items, while forms 2/3 have high valid-response coverage. The pipeline retains nonvalid codes, does not impute missing-by-design values, and computes each estimate only from valid positive-weight respondents. The form table is observed coverage; the full item routing for each individual is not reconstructed. This remaining limitation is stated rather than labeling all missing values item nonresponse.

## Frequent feedback does not imply no training need

The executed common-respondent comparison estimates moderate/high training need separately by reported feedback use. In Australia/ISCED 2, assessment-practice need is about 36% both among teachers giving feedback frequently and among those doing so less often. The less-frequent group has only 113 common valid respondents, with much wider uncertainty. These are exploratory associations conditional on available form/item responses, not evidence that feedback has no effect or that professional learning is unnecessary.

{tables(r,'need_feedback_association',mask=lambda d:(d.country=='AUS')&(d.level==2))}

Selection, self-report, school context and common causes can influence both reported practices and training needs. No student academic-risk outcome is present to assess whether either measure predicts or prevents failure.

## Country, level, weights and adjudication stay separate

{tables(r,'population_coverage')}

The dashboard filters country/system and ISCED 1/2/3. A country-level combination absent from the local files produces an explicit empty state, not zero practice. Level 1/2/3 populations are not assumed to be the same teachers. No pooled “global teacher rate” is reported. Final `TCHWGT` is used for teacher estimands; 100 `TRWGT` replicate weights with Fay factor 0.5 give variance **4/100 × sum((replicate − full estimate)²)**. Paired differences use the same replicate weights on common respondents, preserving covariance. Reported 95% intervals are normal approximations, unadjusted for multiple exploratory comparisons; they do not include measurement/nonresponse bias.

`ADJRT24` is a **data adjudication rating**, not a rotated-questionnaire adjustment weight: 0 insufficient, 1 poor, 2 fair, 3 good. Its meaning was verified before using the field. The dashboard shows it beside every teacher estimate; rating 0 populations remain descriptive and cannot support confident national inference. School/principal files were inspected for scope but not joined to create student labels or repeat teacher observations:

{tables(r,'principal_scope')}

## Preparation, timing and question coverage

| Element | Operational definition | Warning relevance |
|---|---|---|
| Unit | Teacher within country/system and ISCED population | Cross-sectional context, not a student trajectory |
| Practices | TT4G53A/C/D/E/F and TT4G52C/I, valid 1–4; success 3/4 | Reported frequency; no observed student submission timestamp |
| Training needs | TT4G24D/M, valid 1–4; success 3/4 | Current moderate/high need, not later academic risk |
| Weight / variance | TCHWGT; TRWGT1–100; Fay 0.5 | Design-aware country/level estimates and paired contrasts |
| Eligibility | Valid item and positive final weight | Missing/form routing not converted to zero |
| Target / cutoff / outcome window | Not available for individual students | Early-warning validation, support lead time and alert workload blocked |

CSV delimiters were verified as semicolons. Keys combine population, school and teacher identifiers; no raw names or identifiable respondent rows appear in public outputs. All level teacher rows were analyzed with selected items/replicate weights. Extracted-file CRCs were checked against the supplied archive, and the combined export was reconciled to the three level extracts on every respondent and selected item. A first comparison failed because column order differed; explicitly aligning columns fixed the comparison without changing values. Source hashes and an independent weighted-proportion calculation support reproducibility.

The project questions about early student behavior, warning timing, added prior-score value and error workload remain unsupported because linkage and future student outcomes are absent. The supported practice/training/form-design investigation is complete, and identifies infrastructure and measurement issues to resolve before using teacher survey context in a separate prospective warning study.
'''+closing(r,'feasibility assessment; completed country/level assessment-practice contextual investigation','[OECD teacher questionnaire, pp. 14/33–34](https://www.oecd.org/content/dam/oecd/en/about/programmes/edu/talis/talis2024questionnaires/TALIS2024TeacherQuestionnaireISCED1-2-3.pdf), [official BRR/adjudication guide](https://one.oecd.org/document/EDU/TALIS/GB%282025%299/en/pdf), and [official weighting/rotation notes](https://www.oecd.org/en/publications/results-from-talis-2024_90df6235-en/full-report/technical-notes-on-analyses-in-this-volume_286d707e.html)')
  title='TALIS 2024: assessment practices, training needs and survey design';scope='Assessment-practice context only: cross-sectional teachers/principals, without student assessment-event or future-outcome linkage. Country/system and ISCED estimates remain separate. Rating 0 adjudication is insufficient for national inference.'
  countries=sorted(est.country.unique());options=''.join('<option'+(' selected' if c=='AUS' else '')+'>'+c+'</option>' for c in countries)
  body='''<section><label>Education system <select id="country">'''+options+'''</select></label><label>ISCED population <select id="level"><option value="1">1 · Primary</option><option value="2" selected>2 · Lower secondary</option><option value="3">3 · Upper secondary</option></select></label><button id="reset">Reset</button><p>All country/level estimates use valid responses and positive teacher weights; no global pooled percentage. An unavailable combination is missing, not zero. Public outputs contain no teacher identifiers.</p></section><section id="practices"><h2>Which assessment methods and feedback are reported?</h2><div id="practiceBars"></div><div id="practiceRows"></div><p>Practice success means frequently/always (codes 3/4); need success means moderate/high need. Intervals use 100 Fay-BRR replicates, factor 0.5, and are exploratory normal 95% intervals. Adjudication: 0 insufficient, 1 poor, 2 fair, 3 good.</p></section><section id="paired"><h2>Compare feedback methods on the same respondents</h2><div id="pairRows"></div><p>Paired differences retain covariance and common-response denominators. An interval containing zero does not establish a difference or prove equivalence.</p></section><section id="needs"><h2>Does frequent feedback remove training needs?</h2><div id="needRows"></div><p>This is an exploratory, cross-sectional association on common valid item responses. Small less-frequent-feedback groups have wider uncertainty; no causal effect or student-risk outcome is measured.</p></section><section id="forms"><h2>Missing by design is not absence of practice</h2><div id="naiveRows"></div><div id="formRows"></div><p>Form coverage below is a fixed full-level reference and does not follow the country filter. Zero valid responses on form 1 are not teachers reporting zero feedback. Naively coding all absent responses as zero is shown only as an invalid sensitivity contrast.</p></section><details class="panel"><summary>Population coverage and principal-file scope</summary><div id="coverageRows"></div><div id="principalRows"></div><p>Teacher level extracts equal the combined export on all selected items and respondent keys. Use either representation once. Principal files contain school-level context; they cannot create the absent student assessment/outcome linkage.</p></details>'''
  script='''function render(){let country=$('country').value,level=Number($('level').value),est=D.practice_estimates.filter(x=>x.country===country&&x.level===level);bars('practiceBars',est.map(x=>({...x,label:x.meaning})),'weighted','Weighted reported practices and training needs');tbl('practiceRows',est,[['meaning','Reported measure'],['n','All respondents',num],['valid_n','Valid positive-weight n',num],['weighted','Weighted share',pc],['unweighted','Valid unweighted share',pc],['lo','95% low',pc],['hi','95% high',pc],['adjudication','Adjudication code']]);tbl('pairRows',D.paired_feedback.filter(x=>x.country===country&&x.level===level),[['comparison','Paired comparison'],['valid_n','Common valid n',num],['weighted','Difference (proportion)',dec],['lo','95% low',dec],['hi','95% high',dec]]);tbl('needRows',D.need_feedback_association.filter(x=>x.country===country&&x.level===level),[['need_meaning','Training need'],['feedback_group','Feedback use'],['valid_n','Common valid n',num],['weighted','Moderate/high need',pc],['lo','95% low',pc],['hi','95% high',pc]]);tbl('naiveRows',est.filter(x=>x.item==='TT4G53C').map(x=>({...x,naive:x.unweighted*x.valid_n/x.n})),[['meaning','Feedback item'],['valid_n','Valid n',num],['n','All respondents',num],['unweighted','Valid unweighted share',pc],['naive','INVALID zero-coded share',pc]]);tbl('formRows',D.form_coverage.filter(x=>x.level===level&&['TT4G53C','TT4G24D','TT4G24M'].includes(x.item)),[['item','Item (all systems, fixed level reference)'],['form','Form'],['rows','Rows',num],['valid_n','Valid n',num],['valid_fraction','Valid response coverage',pc]]);tbl('coverageRows',D.population_coverage.filter(x=>x.CNTRY===country&&x.IDPOP===level),[['CNTRY','System'],['IDPOP','ISCED'],['teachers','Teachers',num],['schools','Schools',num],['adjudication','Adjudication']]);tbl('principalRows',D.principal_scope,[['file','Principal file (fixed full snapshot)'],['rows','Rows',num],['country_populations','Country populations',num],['duplicate_school_keys','Duplicate school keys',num]]);}for(let id of ['country','level'])$(id).onchange=render;$('reset').onclick=()=>{$('country').value='AUS';$('level').value='2';render()};render();'''
  data=['practice_estimates','paired_feedback','need_feedback_association','form_coverage','population_coverage','principal_scope']
 else:
  ref=est[(est.country=='AUS')&(est.source=='teacher')&(est.teacher_type==1)].set_index('item');pr=pair[(pair.country=='AUS')&(pair.teacher_type==1)].iloc[0]
  text=f'''# PISA 2022: assessment practices provide context, but the local files cannot validate student early warnings

The local snapshot has **68,054 teacher respondents**, **21,629 school respondents** and an earlier-cycle **1,447,787-row ESCS trend export**. It does not include student assessment submissions, deadlines, score availability or later academic outcomes linked to early behavior. Direct student warning validation is therefore unsupported. The completed contextual investigation uses verified item meanings to examine recording practices, feedback and assessment-development needs, rather than substituting a generic socioeconomic profile.

In the illustrative **Australia mathematics-teacher domain**, weighted reported immediate feedback in most/every lesson is **{p(ref.loc['TC054Q06NA'].weighted)}**, versus **{p(ref.loc['TC054Q04NA'].weighted)}** for written feedback beyond marks. On the same **{int(pr.valid_n):,}** common valid respondents, the executed paired difference is **{100*pr.weighted:.1f} percentage points**, 95% Fay-BRR interval **[{100*pr.lo:.1f}, {100*pr.hi:.1f}]**. That describes different teacher practices, not a causal effect on student risk or a verified record of timely support.

## Feedback form matters for an assessment-warning workflow

{tables(r,'practice_estimates',['source','teacher_type','meaning','n','valid_n','weighted','unweighted','lo','hi'],lambda d:d.country=='AUS')}

The mathematics and general-teacher populations are distinct sampling domains. The general-teacher Australian paired gap is 41.6 percentage points, also positive. Comparing on common respondents rules out different item missingness as the sole explanation for this particular within-domain gap. It does not adjust away school context, self-report bias or different lesson tasks.

{mdtable(pair[pair.country=='AUS'])}

Both types of feedback can be useful, but immediate oral/task feedback may leave no submission-level historical record, while written feedback does not establish when its grade became available. These surveys cannot determine the availability times needed to prevent early-warning leakage.

## Reported result recording is not the actual student log

In Australia, 99.0% of valid school-base-weighted reports indicate systematic recording of test results/graduation rates, 98.5% report using teacher-developed tests to guide learning, and 93.4% adapting instruction using those tests. These school indicators show contextual infrastructure, not evidence that the local dataset supplies any student's ordered assessment history. The school and teacher estimands differ and are not joined as if they measured the same students.

{tables(r,'practice_estimates',['country','meaning','n','valid_n','weighted','unweighted','uncertainty'],lambda d:(d.country=='AUS')&(d.source=='school'))}

School points use the supplied **grade-nonresponse-adjusted school base weight** (`W_SCHGRNRABWT`), not a final student weight or a teacher weight. No school replicate weights are supplied in this local file, so school intervals are **NOT VERIFIED** and are deliberately not fabricated. School estimates are weighted descriptive context, with valid-response denominators that can differ across items. Country-specific survey participation/response quality can further constrain national interpretation.

## Assessment training needs remain a separate context measure

Australian weighted moderate/high assessment-practice development need is 21.1% among mathematics teachers and 23.9% among general teachers. The executed conditional follow-up compares training need by frequency of written feedback using common valid item responses; this describes an association, not whether professional learning changes student outcomes.

{tables(r,'training_need_context',mask=lambda d:d.country=='AUS')}

The dashboard exposes every available country/domain estimate and uncertainty, with a clear empty state when optional teacher data is absent. No across-country ranking, pooled global teacher mean or causal interpretation is inferred. All country/domain contrasts are exploratory; normal 95% intervals are not adjusted for selecting among multiple comparisons and do not account for systematic self-report or nonresponse bias.

## Verified codebooks and weights prevent invented constructs

{tables(r,'verified_codebook',['source','field','label','codes'])}

Teacher practice items use valid categories 1–4, with 3/4 meaning most/every lesson. Training need uses 3/4 for moderate/high need. School teacher-developed-test frequency uses monthly/more-than-monthly categories 4/5; result recording uses categories 1/2 versus no=3; teacher-test guidance/adaptation uses yes=1 versus no=2. Special skip/not-applicable/invalid/no-response codes are retained in `missing_codes.csv` and excluded from item denominators; they are not recoded as zero practice.

Teacher points use final `W_FTCHWT`; 80 `W_FTCHRWT` replicates and Fay factor 0.5 give variance **4/80 × sum((replicate − full estimate)²)**. The paired feedback calculation uses difference indicators on the same respondents and replicate weights, retaining covariance. No plausible achievement values are averaged because no achievement target is present in these local questionnaires.

## The ESCS export is not 2022 student outcome evidence

The local ReadMe and full streamed coverage check show that the ESCS trend export contains **cycles 5/6/7 = 2012/2015/2018**, with socioeconomic index components but no achievement outcome or survey weights. It is not a 2022 student questionnaire, and its historical school/student IDs cannot be silently joined to 2022 questionnaire IDs. This is a precise input-scope limitation, not a reason to build an unrelated socioeconomic-risk model.

{mdtable(rd(r,'trend_export_coverage').groupby(['cycle','year']).agg(countries=('country','nunique'),rows=('rows','sum'),escs_valid_n=('escs_valid_n','sum')).reset_index())}

All 1,447,787 trend rows were streamed to validate actual cycle/country coverage. The contextual survey analysis reads all relevant school/teacher rows and selected fields, not a small arbitrary sample. Source SPSS embedded labels verify substantive field semantics and category codes. Source keys and respondent totals reconcile; an independent weighted-rate calculation matches the primary result.

## Timing and project question coverage

| Quantity / question | Available evidence | Warning boundary |
|---|---|---|
| Student early behavior versus later academic risk | No linked timed student assessments or later academic results | Unsupported |
| Warning cutoff and lead time | Cross-sectional practice reports only | No event/score-release/outcome windows |
| Added value beyond prior marks | No individual score history or future target | Unsupported |
| Misses, false flags and review volume | No valid student labels | Unsupported |
| Assessment-practice infrastructure | Verified school recording/test-use and teacher feedback/need items | Completed context, not validated warnings |

The next meaningful evidence is timed student-level events, individual obligations and future academic results from a compatible authorized source. These reports can contextualize a warning implementation; they cannot validate an alert merely because a school reports maintaining records.
'''+closing(r,'feasibility assessment; completed assessment-practice contextual investigation','[OECD PISA database](https://www.oecd.org/en/data/datasets/pisa-2022-database.html), embedded SPSS codebooks and local ESCS ReadMe, and the [official replication methodology](https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/pisa-2022-technical-report_599753f0/01820d6d-en.pdf)')
  title='PISA 2022: feedback and assessment records before warning analytics';scope='Local school/teacher questionnaires provide assessment-practice context, without student assessment-event or later-outcome linkage. Mathematics/general-teacher domains stay separate. Historical ESCS export covers 2012/2015/2018, not 2022 student outcomes.'
  countries=sorted(est.country.unique());options=''.join('<option'+(' selected' if c=='AUS' else '')+'>'+c+'</option>' for c in countries)
  body='''<section><label>Country/economy <select id="country">'''+options+'''</select></label><label>Teacher sampling domain <select id="type"><option value="1">Mathematics teachers</option><option value="2">General teachers</option></select></label><button id="reset">Reset</button><p>Country controls teacher and school views. Type controls only teacher views. Optional teacher participation means some countries have school data but no teacher-domain observations. Empty rates stay undefined.</p></section><section id="feedback"><h2>Which feedback leaves a potential assessment record?</h2><div id="practiceBars"></div><div id="teacherRows"></div><p>Teacher practices: most/every lesson, codes 3/4. Need: moderate/high. Final teacher weights and 80 Fay-BRR replicates, factor 0.5; exploratory normal intervals. Reported feedback does not establish student-event availability or a causal effect.</p></section><section id="paired"><h2>Compare feedback on the same teachers</h2><div id="pairRows"></div><p>Common-response difference avoids attributing item-sample differences to practice. General and mathematics-teacher domains are not pooled.</p></section><section id="schools"><h2>Does a reported recording policy supply student histories?</h2><div id="schoolRows"></div><p>School points use grade-nonresponse-adjusted school base weights and are descriptive. School replicate weights were not supplied, so no design interval is claimed. Reports of recording or adapting instruction cannot replace actual student-level logs.</p></section><section id="needs"><h2>Assessment training needs by written-feedback practice</h2><div id="needRows"></div><p>Exploratory common-response association. Feedback frequency, training need and student academic outcomes are different concepts; there is no causal or early-warning target here.</p></section><section id="coverage"><h2>Who and what years are actually observed?</h2><div id="coverageRows"></div><div id="trendRows"></div><p>Historical trend coverage is a fixed full-export reference, independent of country/type filters. ESCS rows have no achievement outcome or survey weights and cannot be relabeled 2022 student records.</p></section><details class="panel"><summary>Read verified field meanings and response codes</summary><div id="codebookRows"></div><p>Special skip, not-applicable, invalid and nonresponse codes are excluded from the relevant item denominator, never treated as absence of practice. No risk score is fabricated.</p></details>'''
  script='''function render(){let country=$('country').value,type=Number($('type').value),teacher=D.practice_estimates.filter(x=>x.source==='teacher'&&x.country===country&&x.teacher_type===type),school=D.practice_estimates.filter(x=>x.source==='school'&&x.country===country);bars('practiceBars',teacher.map(x=>({...x,label:x.meaning})),'weighted','Weighted teacher feedback and assessment practices');tbl('teacherRows',teacher,[['meaning','Teacher-reported measure'],['n','Domain respondents',num],['valid_n','Valid positive-weight n',num],['weighted','Weighted share',pc],['unweighted','Valid unweighted',pc],['lo','95% low',pc],['hi','95% high',pc]]);tbl('pairRows',D.paired_feedback.filter(x=>x.country===country&&x.teacher_type===type),[['comparison','Common-respondent comparison'],['valid_n','Common valid n',num],['weighted','Difference (proportion)',dec],['lo','95% low',dec],['hi','95% high',dec]]);tbl('schoolRows',school,[['meaning','School-reported practice'],['n','Sample schools',num],['valid_n','Valid positive-weight n',num],['weighted','Base-weighted descriptive share',pc],['unweighted','Unweighted share',pc],['uncertainty','Uncertainty boundary']]);tbl('needRows',D.training_need_context.filter(x=>x.country===country&&x.teacher_type===type),[['written_feedback','Written-feedback use'],['valid_n','Common valid n',num],['weighted','Moderate/high training need',pc],['lo','95% low',pc],['hi','95% high',pc]]);tbl('coverageRows',D.coverage.filter(x=>x.country===country),[['source','Respondent source'],['teacher_type','Teacher type (0=school)'],['respondents','Respondents',num],['positive_weight_n','Positive-weight n',num],['schools','Distinct schools',num]]);let trend={};for(let row of D.trend_export_coverage){if(!trend[row.year])trend[row.year]={year:row.year,rows:0,countries:0,escs_valid_n:0};trend[row.year].rows+=row.rows;trend[row.year].countries++;trend[row.year].escs_valid_n+=row.escs_valid_n;}tbl('trendRows',Object.values(trend),[['year','Historical export year'],['rows','Full export rows',num],['countries','Country codes',num],['escs_valid_n','Nonmissing ESCS rows',num]]);tbl('codebookRows',D.verified_codebook,[['source','Source'],['field','Field'],['label','Verified label'],['codes','Embedded category codes']]);}for(let id of ['country','type'])$(id).onchange=render;$('reset').onclick=()=>{$('country').value='AUS';$('type').value='1';render()};render();'''
  data=['practice_estimates','paired_feedback','training_need_context','coverage','trend_export_coverage','verified_codebook']
 report(r,text);dashboard(r,title,scope,body,script,data)


def build(name):
 if name in ['fff','ednet']:build_prediction(name)
 elif name=='mooccubex':build_mooc()
 elif name=='college-scorecard':build_scorecard()
 elif name in ['pisa-2022','talis-2024']:build_survey(name)
 else:raise ValueError(name)
 print('Built report and question-specific dashboard:',name)
if __name__=='__main__':build(sys.argv[1])
