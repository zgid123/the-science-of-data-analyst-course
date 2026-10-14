"""Follow up behavior beating the combined model: paired AP, modules, validation, schedules."""
import pandas as pd,numpy as np
from analyze import ROOT,OUT,SEED,K,BEH,SCORE,fit,bootstrap
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import average_precision_score
D=ROOT.parents[1]/'datasets'/'oulad';info=pd.read_csv(D/'studentInfo.csv');history=info[info.code_presentation=='2013J'];hids=set(history.id_student)
tri,vai=next(GroupShuffleSplit(n_splits=1,test_size=.25,random_state=SEED).split(history,groups=history.id_student));trids=set(history.iloc[tri].id_student);vaids=set(history.iloc[vai].id_student)
rows=[];unc=[];dist=[]
for c in [30,60,90]:
 f=pd.read_csv(ROOT/'prepared'/f'features_day_{c}.csv')
 train=f[(f.code_presentation=='2013J')&f.id_student.isin(trids)]
 val=f[(f.code_presentation=='2013J')&f.id_student.isin(vaids)].reset_index(drop=True)
 test=f[(f.code_presentation=='2014J')&f.code_module.isin(history.code_module.unique())&~f.id_student.isin(hids)].reset_index(drop=True)
 probs={}
 for name,cols in [('behavior',BEH),('score',SCORE),('combined',BEH+SCORE)]:
  model=fit(train,cols)
  for split,d in [('validation',val),('test',test)]:
   p=model.predict_proba(d)[:,1];probs[(split,name)]=p
   for group,ix in [('All',np.arange(len(d))),*d.groupby('code_module').indices.items()]:
    g=d.iloc[ix];rows.append(dict(cutoff=c,split=split,model=name,module=group,n=len(g),ap=average_precision_score(g.risk,p[ix]),risk=g.risk.mean()))
 lo,hi=bootstrap(test,probs[('test','combined')],probs[('test','behavior')]);unc.append(dict(cutoff=c,comparison='combined minus behavior AP',estimate=average_precision_score(test.risk,probs[('test','combined')])-average_precision_score(test.risk,probs[('test','behavior')]),lo=lo,hi=hi))
 for split,d in [('train',train),('validation',val),('test',test)]:
  for mod,g in d.groupby('code_module'):
   dist.append(dict(cutoff=c,split=split,module=mod,n=len(g),due_count_mean=g.due_count.mean(),available_score_fraction=g.mean_score.notna().mean(),mean_score=g.mean_score.mean(),missing_fraction=g.missing_fraction.mean()))
pd.DataFrame(rows).to_csv(OUT/'model_followup.csv',index=False);pd.DataFrame(unc).to_csv(OUT/'behavior_increment_uncertainty.csv',index=False);pd.DataFrame(dist).to_csv(OUT/'feature_shift.csv',index=False)
print(pd.DataFrame(rows).query('module == "All"').to_string(index=False));print(pd.DataFrame(unc).to_string(index=False))

a=pd.read_csv(D/'assessments.csv');a[(a.code_module=='BBB')&a.code_presentation.isin(['2013J','2014J'])].to_csv(OUT/'bbb_schedule.csv',index=False)
