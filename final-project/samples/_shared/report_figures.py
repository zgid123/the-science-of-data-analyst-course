"""Evidence-backed report figures, rebuilt from aggregate result tables only."""
from pathlib import Path
import json,hashlib,textwrap
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter, FuncFormatter

TEAL='#126b70';ORANGE='#bb7029';BLUE='#354b87'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})

def add_report_figures(r,text):
 name=r.name;folder=r/'figures';folder.mkdir(exist_ok=True);ledger=[];placements={}
 def read(table):return pd.read_csv(r/'results'/(table+'.csv'))
 def wrap(labels):return ['\n'.join(textwrap.wrap(str(x),30)) for x in labels]
 def percent(ax,axis='x'):
  if axis=='x':ax.set_xlim(0,1);ax.xaxis.set_major_formatter(PercentFormatter(1))
  else:ax.set_ylim(0,1);ax.yaxis.set_major_formatter(PercentFormatter(1))
 def finish(fig,slug,data,heading,caption,sources):
  nonlocal text
  fig.tight_layout();fig.savefig(folder/(slug+'.png'),dpi=180,bbox_inches='tight');fig.savefig(folder/(slug+'.svg'),bbox_inches='tight');plt.close(fig)
  data.to_csv(folder/(slug+'.csv'),index=False)
  sourceinfo=[]
  for src in sources:
   p=r/'results'/(src+'.csv');sourceinfo.append(dict(file='results/'+p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
  ledger.append(dict(figure=slug,plotted_rows=len(data),sources=sourceinfo,caption=caption,png='figures/'+slug+'.png',svg='figures/'+slug+'.svg',plotted_data='figures/'+slug+'.csv'))
  assert heading in text,heading
  insertion=f'\n\n![{caption}](figures/{slug}.png)\n\n*{caption} Source: '+', '.join('`'+x['file']+'`' for x in sourceinfo)+'.*\n'
  insertion+=f'\n[SVG figure](figures/{slug}.svg) · [Plotted data](figures/{slug}.csv)\n'
  placements.setdefault(heading,[]).append(insertion)
 if name=='fff':
  d=read('behavior_comparisons');d=d[(d.cutoff==60)&(d.dimension=='behavior_group')].copy()
  fig,ax=plt.subplots(figsize=(9.4,4));ax.barh(wrap(d.group),d.risk_rate,color=[TEAL,ORANGE]);ax.invert_yaxis();percent(ax);ax.set_xlabel('Later final Fail or future recorded withdrawal');ax.set_title('Day 60: absent due records distinguish later risk',loc='left',pad=15)
  for i,x in enumerate(d.itertuples()):ax.text(min(x.risk_rate+.02,.92),i,f'{x.risk_rate:.1%}\nn={x.n:,}',va='center',fontsize=10)
  finish(fig,'due_records_and_risk',d[['group','n','risk_rate']], '## Missing due records distinguish later outcomes','FFF day-60 eligible 2014J first-attempt test enrollments; rates divide later adverse outcomes by each due-record group. Individual deadline exceptions are unknown.',['behavior_comparisons'])
  m=read('model_metrics');u=read('uncertainty');d=m[(m.split=='test')&(m.capacity==.2)&m.model.isin(['behavior','score','combined'])][['cutoff','model','n','ap']].copy()
  fig,ax=plt.subplots(figsize=(9.4,4.8))
  for model,color,offset in [('behavior',TEAL,-1.2),('score',ORANGE,0),('combined',BLUE,1.2)]:
   g=d[d.model==model].sort_values('cutoff');ci=u[u.comparison==model+' AP'].sort_values('cutoff');ax.errorbar(g.cutoff+offset,g.ap,yerr=np.array([g.ap.to_numpy()-ci.lo.to_numpy(),ci.hi.to_numpy()-g.ap.to_numpy()]),fmt='o-',color=color,label=model,capsize=4);d.loc[g.index,'lo']=ci.lo.to_numpy();d.loc[g.index,'hi']=ci.hi.to_numpy()
  ax.set(xlabel='Warning cutoff (days after presentation start)',ylabel='Average precision (0–1)',xticks=[30,60,90],ylim=(0,1),title='Later-cohort ranking across early warning cutoffs');ax.legend(ncol=3,loc='lower right');ax.grid(axis='y',alpha=.15)
  finish(fig,'ranking_across_cutoffs',d,'## Combining behavior and marks improves ranking here','FFF held-out 2014J first attempts; all signals use the same eligible population at each cutoff. Whiskers are 95% student-cluster bootstrap intervals (300 replicates, fixed models); population changes across cutoffs.',['model_metrics','uncertainty'])
 elif name=='ednet':
  d=read('uncertainty');fig,ax=plt.subplots(figsize=(9.4,4.4));y=np.arange(len(d));ax.errorbar(d.estimate,y,xerr=np.array([d.estimate-d.lo,d.hi-d.estimate]),fmt='o',color=TEAL,capsize=5);ax.axvline(0,color='#777',linestyle='--',linewidth=1);ax.set(yticks=y,yticklabels=[str(x)+' prefix bundles' for x in d.cutoff],xlabel='Combined minus prior-score average precision',title='Behavior adds no demonstrated ranking improvement');ax.invert_yaxis();ax.grid(axis='x',alpha=.15)
  finish(fig,'incremental_behavior_value',d,'## Compare behavior with prior performance on identical users','EdNet held-out continuing users. Every paired 95% user-bootstrap interval includes zero (500 replicates, fixed models); the target is next-20-bundle accuracy below 40%, not course failure.',['uncertainty'])
  d=read('lead_time');d=d[d.group=='all eligible'].copy();d['median_seconds']=d.first_hours_median*3600;d['q25_seconds']=d.first_hours_q25*3600;d['q75_seconds']=d.first_hours_q75*3600
  fig,ax=plt.subplots(figsize=(9.4,4.6));ax.errorbar(d.cutoff,d.median_seconds,yerr=np.array([d.median_seconds-d.q25_seconds,d.q75_seconds-d.median_seconds]),fmt='o',capsize=5,color=ORANGE);ax.set(xlabel='Observed prefix bundle sessions',ylabel='Seconds until first future question',xticks=[10,30,60],ylim=(0,max(d.q75_seconds)*1.3),title='The next practice question often arrives within seconds')
  for x in d.itertuples():ax.annotate(f'n={x.n:,}',(x.cutoff,x.q75_seconds),xytext=(0,9),textcoords='offset points',ha='center',fontsize=10)
  ax.grid(axis='y',alpha=.15)
  finish(fig,'next_question_lead_time',d[['cutoff','n','median_seconds','q25_seconds','q75_seconds']],'## Review burden and short lead time limit usefulness','EdNet eligible held-out users; dots are median intervals to the first future question and whiskers are the interquartile range, not confidence intervals. Completion timing is approximated by presentation time plus recorded duration.',['lead_time'])
 elif name=='mooccubex':
  x=read('course_summary').exercises;bounds=[(-1,0),(0,5),(5,10),(10,20),(20,40),(40,80),(80,np.inf)];labels=['0','1–5','6–10','11–20','21–40','41–80','81+'];d=pd.DataFrame([dict(exercise_containers=label,courses=int(((x>lo)&(x<=hi)).sum())) for label,(lo,hi) in zip(labels,bounds)]);assert d.courses.sum()==len(x)
  fig,ax=plt.subplots(figsize=(9.4,4.6));bars=ax.bar(d.exercise_containers,d.courses,color=TEAL);ax.bar_label(bars,fmt='%d',padding=4);ax.set(xlabel='Exercise containers listed per course',ylabel='Local courses',ylim=(0,d.courses.max()*1.17),title='Assessment content is uneven across local courses');ax.grid(axis='y',alpha=.15)
  finish(fig,'exercise_opportunity_distribution',d,'## Exercise opportunities vary substantially even before observing students','All 3,781 local courses, grouped by exercise-container count. Containers are groups of problems, not student submissions, obligations or deadlines. The 81+ bin includes counts up to 228.',['course_summary'])
  d=read('manual_label_sensitivity');fig,ax=plt.subplots(figsize=(9.4,4));ax.barh(wrap(d.group),d.exercise_coverage,color=[ORANGE,TEAL]);ax.invert_yaxis();percent(ax);ax.set_xlabel('Courses with at least one exercise container');ax.set_title('Manual-label coverage would overstate exercise availability',loc='left',pad=15)
  for i,x in enumerate(d.itertuples()):ax.text(.03,i,f'{x.exercise_coverage:.1%} · n={x.n:,} courses',color='white',va='center',weight='bold')
  finish(fig,'manual_label_selection',d,'## Label coverage and repeated edges can distort a feasibility conclusion','Matched manually labeled courses versus the remaining local course universe; 85 unmatched manual course IDs are excluded only from field summaries. No student academic-risk inference is supported.',['manual_label_sensitivity'])
 elif name=='college-scorecard':
  d=read('outcome_definitions');d=d[(d.sector=='All reported sectors')&(d.measure=='150% completion')].copy();fig,ax=plt.subplots(figsize=(9.4,4.7));y=np.arange(len(d));ax.barh(y-.18,d.unweighted_mean,.34,color=ORANGE,label='Institution mean');ax.barh(y+.18,d.weighted_mean,.34,color=TEAL,label='Completion-cohort weighted');ax.set_yticks(y,wrap(d.family));ax.invert_yaxis();percent(ax);ax.set_xlabel('Reported completion within 150% of expected time');ax.set_title('The institution average differs from the cohort average',loc='left',pad=15);ax.legend(loc='lower right')
  for i,x in enumerate(d.itertuples()):
   ax.text(x.unweighted_mean+.015,i-.18,f'{x.unweighted_mean:.1%}',va='center');ax.text(x.weighted_mean+.015,i+.18,f'{x.weighted_mean:.1%}',va='center')
  finish(fig,'completion_estimand_comparison',d[['family','valid_institutions','unweighted_mean','weighted_mean','cohort_denominator']],'## Institution averages and cohort-weighted averages answer different questions','All valid reporting institutions in each metric family. Cohort weights are D150_4/D150_L4, not total enrollment. Different institutional and cohort estimands do not identify individual academic risk.',['outcome_definitions'])
  d=read('small_cohort_sensitivity');d=d[d.sector=='All reported sectors'].copy();fig,axes=plt.subplots(1,2,figsize=(10,4.7),sharey=True)
  for ax,(family,g) in zip(axes,d.groupby('family',sort=False)):
   g=g.sort_values('min_completion_cohort');xx=np.arange(len(g));ax.plot(xx,g.completion_mean,'o-',color=ORANGE,label='Institution mean');ax.plot(xx,g.completion_weighted,'s-',color=TEAL,label='Cohort weighted');ax.set_xticks(xx,[str(int(v))+'\nn='+str(int(n)) for v,n in zip(g.min_completion_cohort,g.institutions)]);ax.set(xlabel='Minimum cohort size / retained institutions',title=family);percent(ax,'y');ax.grid(axis='y',alpha=.15)
  axes[0].set_ylabel('Completion proportion');axes[1].legend(loc='upper right',fontsize=9);fig.suptitle('Small-cohort restrictions change the institution estimand',y=1.04)
  finish(fig,'small_cohort_sensitivity',d,'## Institution averages and cohort-weighted averages answer different questions','Completion-cohort minimums 1/30/100, with retained institution counts labeled. Restrictions change the population; they are sensitivity checks, not removal of proven errors. Rounded published rates make weighted totals approximate.',['small_cohort_sensitivity'])
 elif name=='pisa-2022':
  d=read('practice_estimates');d=d[(d.source=='teacher')&(d.country=='AUS')].copy();items=['TC054Q01NA','TC054Q04NA','TC054Q06NA','TC185Q04HA'];labels=['Develop own assessment','Written feedback beyond marks','Immediate task feedback','Moderate/high training need'];fig,ax=plt.subplots(figsize=(10,5.3));yy=np.arange(4)
  for typ,color,off,label in [(1,TEAL,-.12,'Mathematics teachers'),(2,ORANGE,.12,'General teachers')]:
   g=d[d.teacher_type==typ].set_index('item').reindex(items);ax.errorbar(g.weighted,yy+off,xerr=np.array([g.weighted-g.lo,g.hi-g.weighted]),fmt='o',capsize=4,color=color,label=label)
  ax.set_yticks(yy,wrap(labels));ax.invert_yaxis();percent(ax);ax.set_xlabel('Weighted share of valid teacher responses');ax.set_title('Australia: feedback practices differ across teacher domains',loc='left',pad=15);ax.legend(loc='lower right',fontsize=10);ax.grid(axis='x',alpha=.15)
  finish(fig,'teacher_feedback_domains',d[['teacher_type','item','meaning','n','valid_n','weighted','lo','hi']],'## Feedback form matters for an assessment-warning workflow','Australia only; mathematics/general-teacher sampling domains remain separate. Practice success is most/every lesson; need is moderate/high. Whiskers: normal 95% intervals from 80 Fay-BRR replicates (factor 0.5); denominators vary by item.',['practice_estimates'])
  d=read('paired_feedback');d=d[d.country=='AUS'].copy();fig,ax=plt.subplots(figsize=(9.4,4));yy=np.arange(len(d));ax.errorbar(d.weighted,yy,xerr=np.array([d.weighted-d.lo,d.hi-d.weighted]),fmt='o',capsize=5,color=BLUE);ax.axvline(0,color='#888',linestyle='--');ax.set_yticks(yy,['Mathematics teachers','General teachers']);ax.invert_yaxis();ax.set_xlim(0,.65);ax.xaxis.set_major_formatter(FuncFormatter(lambda x,_:f'{x*100:.0f} pp'));ax.set_xlabel('Immediate minus written feedback (percentage-point difference)');ax.set_title('The feedback gap remains on common respondents',loc='left',pad=15)
  for i,x in enumerate(d.itertuples()):ax.text(x.hi+.015,i,f'n={x.valid_n:,}',va='center',fontsize=10)
  finish(fig,'paired_feedback_gap',d,'## Feedback form matters for an assessment-warning workflow','Australia common valid respondents within each teacher domain; paired differences retain covariance under 80 Fay-BRR replicates. Whiskers are normal 95% intervals, exploratory and not multiplicity-adjusted. This is practice context, not student warning validation.',['paired_feedback'])
 elif name=='talis-2024':
  d=read('practice_estimates');d=d[(d.country=='AUS')&(d.level==2)].copy();fig,ax=plt.subplots(figsize=(10,7));yy=np.arange(len(d));ax.errorbar(d.weighted,yy,xerr=np.array([d.weighted-d.lo,d.hi-d.weighted]),fmt='o',color=TEAL,capsize=4);ax.set_yticks(yy,wrap(d.meaning));ax.invert_yaxis();percent(ax);ax.set_xlabel('Weighted share of valid positive-weight respondents');ax.set_title('Australia / ISCED 2: feedback and training need coexist',loc='left',pad=15);ax.grid(axis='x',alpha=.15)
  finish(fig,'assessment_practices_and_need',d[['item','meaning','n','valid_n','weighted','lo','hi','adjudication']],'## Practice differences are substantive, not identifier counts','Australia lower-secondary teachers; practice success is frequent/always, need is moderate/high. Whiskers: normal 95% intervals using 100 Fay-BRR replicates (factor 0.5). Item-specific denominators differ; adjudication rating 2 (fair).',['practice_estimates'])
  d=read('form_coverage');d=d[(d.level==2)&d.item.isin(['TT4G53C','TT4G24D','TT4G24M'])].copy();fig,ax=plt.subplots(figsize=(9.4,4.8));xx=np.arange(3)
  for i,(item,color,label) in enumerate([('TT4G53C',TEAL,'Improvement feedback'),('TT4G24D',ORANGE,'Assessment-practice need'),('TT4G24M',BLUE,'Assessment-analysis need')]):
   g=d[d.item==item].sort_values('form');ax.bar(xx+(i-1)*.24,g.valid_fraction,.22,color=color,label=label)
  ax.set_xticks(xx,['Form 1','Form 2','Form 3']);percent(ax,'y');ax.set_ylabel('Valid response fraction of form respondents');ax.set_title('Rotated-form absence must not be coded as zero practice',loc='left',pad=15);ax.legend(loc='lower right',fontsize=9);ax.grid(axis='y',alpha=.15)
  finish(fig,'rotated_form_coverage',d,'## Rotated questionnaire missingness can halve a naive prevalence','Fixed full local ISCED-2 extract across all systems, not Australia only. Each bar divides valid item responses by that form’s respondents; zero valid responses on Form 1 indicates design/routing absence, not zero feedback.',['form_coverage'])
 else:return text
 for heading,blocks in placements.items():text=text.replace(heading,heading+''.join(blocks),1)
 (r/'evidence/report-figures.json').write_text(json.dumps(ledger,indent=2));return text
