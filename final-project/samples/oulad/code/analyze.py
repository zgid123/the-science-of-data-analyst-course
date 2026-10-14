"""OULAD early-warning study. All paths relative to this file; no raw writes."""
from pathlib import Path
import json, hashlib, datetime, warnings
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score, brier_score_loss, confusion_matrix
warnings.filterwarnings('ignore', category=FutureWarning)
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT.parents[1]/'datasets'/'oulad'
OUT=ROOT/'results'; OUT.mkdir(exist_ok=True)
SEED=20261013; K=['code_module','code_presentation','id_student']; C=K[:2]
checks=[]
def check(name, quantity, expected, status=True):
 checks.append(dict(check=name,observed=quantity,expected=expected,status='PASS' if status else 'FAIL',method='Executed named assertions in code/analyze.py; see evidence/analysis-run.txt',unit='count of rows/enrollments/students as named; calendar date for publication bound',consequence='Numerical gate passes under documented availability assumptions' if status else 'Blocks scoped numerical conclusion'))
def save(name, rows):
 df=rows if isinstance(rows,pd.DataFrame) else pd.DataFrame(rows)
 df.to_csv(OUT/(name+'.csv'),index=False);return df

def load():
 tables={n:pd.read_csv(DATA/(n+'.csv')) for n in ['courses','assessments','studentInfo','studentRegistration','studentAssessment']}
 manifest=[]
 for name,t in tables.items():
  p=DATA/(name+'.csv'); manifest.append(dict(file=p.name,rows=len(t),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size))
 save('source_manifest',manifest)
 for n,key in [('courses',C),('assessments',['id_assessment']),('studentInfo',K),('studentRegistration',K),('studentAssessment',['id_assessment','id_student'])]:
  d=int(tables[n].duplicated(key).sum());check(n+' duplicate keys',d,'0 duplicate rows',d==0)
 i=tables['studentInfo'];r=tables['studentRegistration'];a=tables['assessments'];s=tables['studentAssessment']
 e=i.merge(r,on=K,validate='one_to_one',indicator=True);check('registration join unmatched enrollments',int((e._merge!='both').sum()),'0',bool((e._merge=='both').all()));e=e.drop(columns='_merge')
 e=e.merge(tables['courses'],on=C,validate='many_to_one')
 s=s.merge(a,on='id_assessment',validate='many_to_one',indicator=True);check('submission unmatched assessments',int((s._merge!='both').sum()),'0',bool((s._merge=='both').all()));s=s.drop(columns='_merge')
 joined=s.merge(i[K+['num_of_prev_attempts']],on=K,validate='many_to_one',indicator=True)
 check('submission unmatched enrollments',int((joined._merge!='both').sum()),'0',bool((joined._merge=='both').all()))
 check('banked rows in first-attempt enrollments',int(((joined.is_banked==1)&(joined.num_of_prev_attempts==0)).sum()),'0',not ((joined.is_banked==1)&(joined.num_of_prev_attempts==0)).any())
 check('score out of 0–100 range',int(((s.score<0)|(s.score>100)).sum()),'0',not ((s.score<0)|(s.score>100)).any())
 # Incoherent withdrawal records cannot establish at-risk eligibility or event timing.
 e['coherent']=((e.final_result=='Withdrawn') & e.date_unregistration.notna()) | ((e.final_result!='Withdrawn') & e.date_unregistration.isna())
 e['within_followup']=e.date_unregistration.isna()|(e.date_unregistration<=e.module_presentation_length)
 e['base_eligible']=(e.num_of_prev_attempts==0)&(e.date_registration<=0)&e.coherent&e.within_followup
 check('included historical withdrawals after course end',int(((e.code_presentation=='2013J')&e.base_eligible&(e.date_unregistration>e.module_presentation_length)).sum()),'0 historical enrollments',not ((e.code_presentation=='2013J')&e.base_eligible&(e.date_unregistration>e.module_presentation_length)).any())
 quality=[dict(issue='withdrawal after scheduled course end (outside follow-up; excluded)',n=int((~e.within_followup).sum())),dict(issue='missing registration day',n=int(e.date_registration.isna().sum())),dict(issue='registered after day zero',n=int((e.date_registration>0).sum())),dict(issue='repeat module attempt',n=int((e.num_of_prev_attempts>0).sum())),dict(issue='incoherent withdrawal/outcome record',n=int((~e.coherent).sum())),dict(issue='banked submission rows',n=int((s.is_banked==1).sum())),dict(issue='missing score rows',n=int(s.score.isna().sum())),dict(issue='undated non-exam assessments',n=int(((a.assessment_type!='Exam')&a.date.isna()).sum()))]
 save('data_quality',quality)
 save('raw_outcomes',i.groupby(['code_module','code_presentation','final_result']).size().rename('n').reset_index())
 return e,a,s

def features(e,a,s,cut,lag=14,logdelay=0):
 """Only first attempts: all scheduled non-exam opportunities assumed applicable."""
 f=e[e.base_eligible & (e.date_unregistration.isna()|(e.date_unregistration>cut))].copy()
 f['risk']=f.final_result.isin(['Fail','Withdrawn']).astype(int);f['cutoff']=cut
 due=a[(a.assessment_type!='Exam')&(a.date<=cut)&(a.date>=0)]
 opp=f[K].merge(due,on=C,how='inner',validate='many_to_many')
 visible=s[(s.is_banked==0)&(s.date_submitted<=cut-logdelay)]
 opp=opp.merge(visible[['id_assessment','id_student','date_submitted']],on=['id_assessment','id_student'],how='left',validate='one_to_one')
 opp['recorded']=opp.date_submitted.notna().astype(int)
 opp['ontime']=(opp.date_submitted<=opp.date).astype(int)
 opp['late']=np.maximum(opp.date_submitted-opp.date,0)
 g=opp.groupby(K).agg(due_count=('id_assessment','size'),submitted_due=('recorded','sum'),ontime_due=('ontime','sum'),mean_lateness=('late','mean')).reset_index()
 f=f.merge(g,on=K,how='left',validate='one_to_one');f['due_count']=f.due_count.fillna(0)
 f['missing_fraction']=1-f.submitted_due/f.due_count
 f['ontime_fraction']=f.ontime_due/f.due_count
 nonexam=visible[visible.assessment_type!='Exam']
 rec=nonexam.groupby(K).date_submitted.max().rename('last_submission').reset_index()
 f=f.merge(rec,on=K,how='left',validate='one_to_one');f['recency']=cut-f.last_submission
 # Scores use a release lag; missing scores stay missing and gain a model indicator.
 scored=s[(s.is_banked==0)&(s.assessment_type!='Exam')&(s.date_submitted<=cut-max(lag,logdelay))]
 sc=scored.groupby(K).agg(mean_score=('score','mean'),score_count=('score','count')).reset_index()
 f=f.merge(sc,on=K,how='left',validate='one_to_one');f.score_count=f.score_count.fillna(0)
 check(f'cutoff {cut} lag {lag} logging {logdelay}: future submission use',int((visible.date_submitted>cut-logdelay).sum()),'0',bool((visible.date_submitted<=cut-logdelay).all()))
 check(f'cutoff {cut} lag {lag} logging {logdelay}: future score use',int((scored.date_submitted+lag>cut).sum()),'0',bool((scored.date_submitted+lag<=cut).all()))
 check(f'cutoff {cut} lag {lag} logging {logdelay}: due opportunities',int((opp.date>cut).sum()),'0',not (opp.date>cut).any())
 check(f'cutoff {cut}: denominator violations',int(((f.submitted_due>f.due_count)|(f.ontime_due>f.submitted_due)).sum()),'0',not ((f.submitted_due>f.due_count)|(f.ontime_due>f.submitted_due)).any())
 f['behavior_group']=np.where(f.due_count==0,'No assessments due',np.where(f.missing_fraction>0,'At least one absent due record','All due records present'))
 f['withdrawal_lead']=f.date_unregistration-cut
 f['course_end_remaining']=f.module_presentation_length-cut
 return f

BEH=['due_count','missing_fraction','ontime_fraction','mean_lateness','recency']
SCORE=['mean_score','score_count']
def fit(train,cols):
 num=make_pipeline(SimpleImputer(strategy='median',add_indicator=True,keep_empty_features=True),StandardScaler())
 pre=ColumnTransformer([('numeric',num,cols),('module',OneHotEncoder(handle_unknown='ignore'),['code_module'])])
 model=make_pipeline(pre,LogisticRegression(C=1,max_iter=2000,random_state=SEED))
 model.fit(train[cols+['code_module']],train.risk);return model

def metrics(d,p,t):
 y=d.risk.to_numpy();pred=p>=t;tn,fp,fn,tp=confusion_matrix(y,pred,labels=[0,1]).ravel()
 return dict(n=len(d),positives=int(y.sum()),prevalence=float(y.mean()),ap=float(average_precision_score(y,p)) if y.sum()>0 else np.nan,auc=float(roc_auc_score(y,p)) if len(np.unique(y))>1 else np.nan,brier=float(brier_score_loss(y,p)),threshold=float(t),alerts=int(pred.sum()),alert_rate=float(pred.mean()),precision=float(tp/(tp+fp)) if tp+fp else np.nan,recall=float(tp/(tp+fn)) if tp+fn else np.nan,fp=int(fp),fn=int(fn),tp=int(tp),tn=int(tn))

def bootstrap(d,score,other=None):
 # Resample students, retaining multiple module enrollments in each sampled cluster.
 rng=np.random.default_rng(SEED);ids=d.id_student.unique();groups=d.groupby('id_student',sort=False).indices;vals=[]
 y=d.risk.to_numpy()
 for _ in range(300):
  ix=np.concatenate([groups[x] for x in rng.choice(ids,len(ids),replace=True)])
  if len(np.unique(y[ix]))<2:continue
  v=average_precision_score(y[ix],score[ix]);
  if other is not None:v-=average_precision_score(y[ix],other[ix])
  vals.append(v)
 return np.quantile(vals,[.025,.975]).tolist()

def main():
 e,a,s=load();allf={c:features(e,a,s,c) for c in [30,60,90]}
 # Bounds avoid inventing precise presentation dates. Calendar labels remain conditional on a 60-day release assumption.
 latest_label=datetime.date(2013,10,31)+datetime.timedelta(days=int(e[e.code_presentation=='2013J'].module_presentation_length.max())+60)
 earliest_deploy=datetime.date(2014,10,1)
 check('historical label publication bound',f'{latest_label} < {earliest_deploy}','latest possible prior outcome +60 days before earliest test start',latest_label<earliest_deploy)
 history=e[e.code_presentation=='2013J'];hids=set(history.id_student)
 split=GroupShuffleSplit(n_splits=1,test_size=.25,random_state=SEED)
 tri,vai=next(split.split(history,groups=history.id_student));trainids=set(history.iloc[tri].id_student);validids=set(history.iloc[vai].id_student)
 check('train-validation student overlap',len(trainids&validids),'0',not trainids&validids)
 modules=sorted(history.code_module.unique())
 rows=[];coverage=[];associations=[];subgroups=[];calibration=[];uncertainty=[];sens=[];lead=[];coefs=[];cuts={};predictions=[]
 for c,f in allf.items():
  print(f'Analyzing day {c}',flush=True)
  train=f[(f.code_presentation=='2013J')&f.id_student.isin(trainids)]
  val=f[(f.code_presentation=='2013J')&f.id_student.isin(validids)]
  fulltest=f[(f.code_presentation=='2014J')&f.code_module.isin(modules)]
  test=fulltest[~fulltest.id_student.isin(hids)].copy().reset_index(drop=True)
  check(f'day {c} history-test student overlap',len(set(test.id_student)&hids),'0',not set(test.id_student)&hids)
  check(f'day {c} already withdrawn test enrollments',int((test.date_unregistration<=c).sum()),'0',not (test.date_unregistration<=c).any())
  for cohort in sorted(e.code_presentation.unique()):
   raw=e[e.code_presentation==cohort];eligible=f[f.code_presentation==cohort]
   coverage.append(dict(cutoff=c,cohort=cohort,raw_n=len(raw),base_eligible_n=int(raw.base_eligible.sum()),active_n=len(eligible),already_withdrawn_n=int((raw.base_eligible&(raw.date_unregistration<=c)).sum()),due_n=int((eligible.due_count>0).sum()),future_withdrawn_n=int((eligible.final_result=='Withdrawn').sum()),fail_n=int((eligible.final_result=='Fail').sum()),test_n=len(test) if cohort=='2014J' else 0,train_n=len(train) if cohort=='2013J' else 0,validation_n=len(val) if cohort=='2013J' else 0))
  f.to_csv(ROOT/'prepared'/f'features_day_{c}.csv',index=False)
  # Primary descriptive comparisons use the same test population to align with model utility.
  for col in ['code_module','final_result','behavior_group']:
   for label,d in test.groupby(col):
    associations.append(dict(cutoff=c,dimension=col,group=label,n=len(d),due_n=int((d.due_count>0).sum()),risk_rate=d.risk.mean(),missing_mean=d.missing_fraction.mean(),ontime_mean=d.ontime_fraction.mean(),lateness_median=d.mean_lateness.median(),score_mean=d.mean_score.mean(),future_withdrawn_n=int((d.final_result=='Withdrawn').sum()),fail_n=int((d.final_result=='Fail').sum())))
  for (mod,bg),d in test.groupby(['code_module','behavior_group']):
   associations.append(dict(cutoff=c,dimension='module_behavior',group=mod+' / '+bg,n=len(d),due_n=int((d.due_count>0).sum()),risk_rate=d.risk.mean(),missing_mean=d.missing_fraction.mean(),ontime_mean=d.ontime_fraction.mean(),future_withdrawn_n=int((d.final_result=='Withdrawn').sum()),fail_n=int((d.final_result=='Fail').sum())))
  probs={};models={};thresholds={}
  for name,cols in [('module',[]),('behavior',BEH),('score',SCORE),('combined',BEH+SCORE)]:
   model=fit(train,cols);models[name]=model
   pv=model.predict_proba(val)[:,1];pt=model.predict_proba(test)[:,1];probs[name]=pt
   for capacity in [.1,.2,.3]:
    # Higher observed quantile; ties explicitly counted, not silently broken.
    threshold=float(np.quantile(pv,1-capacity,method='higher'));thresholds[(name,capacity)]=threshold
    m=metrics(test,pt,threshold);rows.append(dict(cutoff=c,model=name,capacity=capacity,split='test',**m))
    rows.append(dict(cutoff=c,model=name,capacity=capacity,split='validation',**metrics(val,pv,threshold)))
   if name!='module':
    lo,hi=bootstrap(test,pt);uncertainty.append(dict(cutoff=c,comparison=name+' AP',estimate=average_precision_score(test.risk,pt),lo=lo,hi=hi))
   if name=='combined':
    names=model[0].get_feature_names_out();coefs += [dict(cutoff=c,feature=n,coefficient=float(v)) for n,v in zip(names,model[1].coef_[0])]
  threshold=thresholds[('combined',.2)];pt=probs['combined'];alert=pt>=threshold
  # Fixed baselines; no-score population never disappears from model comparisons.
  for name,p,t in [('prevalence',np.full(len(test),train.risk.mean()),1.0),('absent_due_rule',(test.missing_fraction>0).astype(float).to_numpy(),.5)]:
   rows.append(dict(cutoff=c,model=name,capacity=0,split='test',**metrics(test,p,t)))
  lo,hi=bootstrap(test,probs['combined'],probs['score']);uncertainty.append(dict(cutoff=c,comparison='combined minus score AP',estimate=average_precision_score(test.risk,pt)-average_precision_score(test.risk,probs['score']),lo=lo,hi=hi))
  for col in ['code_module','disability','age_band','final_result','behavior_group']:
   for group,ix in test.groupby(col).indices.items():
    d=test.iloc[ix]
    subgroups.append(dict(cutoff=c,dimension=col,group=group,**metrics(d,pt[ix],threshold)))
  for binid in range(5):
   mask=(pt>=binid/5)&((pt<(binid+1)/5) if binid<4 else (pt<=1))
   if mask.any():calibration.append(dict(cutoff=c,bin=f'{binid/5:.1f}–{(binid+1)/5:.1f}',n=int(mask.sum()),mean_prediction=float(pt[mask].mean()),observed_risk=float(test.risk.to_numpy()[mask].mean())))
  for label,mask in [('all_future_withdrawals',(test.final_result=='Withdrawn').to_numpy()),('flagged_future_withdrawals',((test.final_result=='Withdrawn').to_numpy())&alert),('flagged_final_fail',((test.final_result=='Fail').to_numpy())&alert)]:
   d=test[mask];v=d.withdrawal_lead if 'withdrawals' in label else d.course_end_remaining
   lead.append(dict(cutoff=c,group=label,n=len(d),q25=v.quantile(.25),median=v.median(),q75=v.quantile(.75),under_14=int((v<14).sum()),at_least_14=int((v>=14).sum()),time_type='observed withdrawal day' if 'withdrawals' in label else 'course-end proxy, not failure event'))
  # Independent confusion-count reconciliation.
  m=metrics(test,pt,threshold)
  manual_tp=int(np.logical_and(alert,test.risk.to_numpy()==1).sum());check(f'day {c} manual true positives',manual_tp,f"{m['tp']} enrollments",manual_tp==m['tp'])
  check(f'day {c} confusion population',m['tp']+m['tn']+m['fp']+m['fn'],f'{len(test)} test enrollments',m['tp']+m['tn']+m['fp']+m['fn']==len(test))
  # Sensitivities are fixed challenges, not model-selection candidates.
  for setting,lag,logdelay,failonly in [('score_delay_28',28,0,False),('submission_logging_delay_7',14,7,False),('failure_only',14,0,True)]:
   ff=features(e,a,s,c,lag,logdelay) if not failonly else f.copy()
   if failonly:ff=ff[ff.final_result!='Withdrawn'].copy();ff['risk']=(ff.final_result=='Fail').astype(int)
   tr=ff[(ff.code_presentation=='2013J')&ff.id_student.isin(trainids)]
   va=ff[(ff.code_presentation=='2013J')&ff.id_student.isin(validids)]
   te=ff[(ff.code_presentation=='2014J')&ff.code_module.isin(modules)&~ff.id_student.isin(hids)].reset_index(drop=True)
   for name,cols in [('score',SCORE),('combined',BEH+SCORE)]:
    model=fit(tr,cols);pv=model.predict_proba(va)[:,1];p=model.predict_proba(te)[:,1];t=np.quantile(pv,.8,method='higher')
    sens.append(dict(cutoff=c,setting=setting,model=name,**metrics(te,p,t)))
  p=models['combined'].predict_proba(fulltest)[:,1];sens.append(dict(cutoff=c,setting='include_previous_2013J_students',model='combined',**metrics(fulltest,p,threshold)))
  # Common enrollment panel removes changing eligibility as an explanation for timing comparison.
  cuts[c]=dict(test=test,prob=pt,threshold=threshold)
  local=test[K+['risk','final_result']].copy();local['probability']=pt;local['alert']=alert;local['cutoff']=c;predictions.append(local)
 common=set(map(tuple,cuts[90]['test'][K].to_numpy()))
 for c,ob in cuts.items():
  mask=np.array([tuple(row) in common for row in ob['test'][K].to_numpy()]);d=ob['test'][mask];p=ob['prob'][mask]
  sens.append(dict(cutoff=c,setting='active_through_day90_common_panel',model='combined',**metrics(d,p,ob['threshold'])))
 save('model_metrics',rows);save('coverage',coverage);save('behavior_comparisons',associations);save('subgroup_errors',subgroups);save('calibration',calibration);save('uncertainty',uncertainty);save('sensitivity',sens);save('lead_time',lead);save('coefficients',coefs)
 pd.concat(predictions).to_csv(ROOT/'prepared'/'test_predictions.csv',index=False)
 save('verification',checks)
 assert all(c['status']=='PASS' for c in checks),[x for x in checks if x['status']!='PASS']
 meta=dict(seed=SEED,source='local OULAD CSV snapshot',analysis_date='2026-10-13',modules=modules,cutoffs=[30,60,90],score_delay_days=14,bootstrap_replicates=300,prior_holdout_reuse='unknown',label_publication_latest_bound=str(latest_label))
 (OUT/'metadata.json').write_text(json.dumps(meta,indent=2))
 print(save('model_metrics',rows).query('split == "test" and (capacity == .2 or capacity == 0)')[['cutoff','model','n','ap','precision','recall','alert_rate']].to_string(index=False))
 print('ALL CHECKS PASS:',len(checks))
if __name__=='__main__':main()
