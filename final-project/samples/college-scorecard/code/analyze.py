"""Bounded aggregate-outcome suitability study; no individual academic-risk model."""
import sys
from pathlib import Path
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'_shared'))
from delivery import setup,save,check,evidence_gap,manifest
R,D=setup('college-scorecard');checks=[]
p=D/'Most-Recent-Cohorts-Institution.csv';header=pd.read_csv(p,nrows=0).columns
cols=['UNITID','OPEID6','PREDDEG','CONTROL','UGDS','C150_4','C150_L4','D150_4','D150_L4','C150_4_PELL','C150_L4_PELL','D150_4_PELL','D150_L4_PELL','RET_FT4','RET_FTL4','RET_PT4','RET_PTL4','RET_FT4_POOLED_SUPP','RET_FTL4_POOLED_SUPP','RET_FT_DEN4_POOLED','RET_FT_DENL4_POOLED','C150_4_POOLED','C150_L4_POOLED','D150_4_POOLED','D150_L4_POOLED']
x=pd.read_csv(p,usecols=cols,dtype=str,keep_default_na=False);d=x.apply(lambda col:pd.to_numeric(col,errors='coerce'))
check(checks,'institution UNITID duplicate rows',int(d.UNITID.duplicated().sum()),'0',not d.UNITID.duplicated().any())
missing=[]
for col in cols:
 if col in ['UNITID','OPEID6','PREDDEG','CONTROL']:continue
 for token,n in x.loc[d[col].isna(),col].value_counts(dropna=False).items():missing.append(dict(field=col,token=token or '(empty)',rows=n))
save(R,'missing_tokens',missing)
rows=[];pair=[];small=[]
sectors={1:'Public',2:'Private nonprofit',3:'Private for-profit'}
for family,suffix in [('Four-year metric','4'),('Less-than-four-year metric','L4')]:
 rate='C150_'+suffix;den='D150_'+suffix;ret='RET_FT'+suffix;pt='RET_PT'+suffix;pool='RET_FT'+suffix+'_POOLED_SUPP';poolden='RET_FT_DEN'+suffix+'_POOLED'
 for sector in [0,1,2,3]:
  pop=d if sector==0 else d[d.CONTROL==sector];label='All reported sectors' if sector==0 else sectors[sector]
  for name,rcol,wcol in [('150% completion',rate,den),('Full-time retention',ret,None),('Part-time retention',pt,None),('Suppressed pooled FT retention',pool,poolden)]:
   valid=pop[rcol].between(0,1);g=pop[valid];w=valid&(pop[wcol]>0) if wcol else valid
   rows.append(dict(family=family,sector=label,measure=name,raw_institutions=len(pop),valid_institutions=len(g),coverage=len(g)/len(pop),unweighted_mean=g[rcol].mean(),median=g[rcol].median(),q25=g[rcol].quantile(.25),q75=g[rcol].quantile(.75),weighted_mean=np.average(pop.loc[w,rcol],weights=pop.loc[w,wcol]) if wcol and w.any() else np.nan,weighted_institutions=int(w.sum()) if wcol else 0,cohort_denominator=pop.loc[w,wcol].sum() if wcol else np.nan,weight_meaning=wcol or 'Unavailable matching non-pooled retention cohort denominator'))
   check(checks,f'{family}/{label}/{name} rate range violations',int((pop[rcol].notna()&~pop[rcol].between(0,1)).sum()),'0',not (pop[rcol].notna()&~pop[rcol].between(0,1)).any())
  common=pop[pop[rate].between(0,1)&pop[ret].between(0,1)]
  pair.append(dict(family=family,sector=label,both_metrics_n=len(common),completion_only_n=int((pop[rate].notna()&pop[ret].isna()).sum()),retention_only_n=int((pop[rate].isna()&pop[ret].notna()).sum()),institution_spearman=common[rate].corr(common[ret],method='spearman'),median_completion=common[rate].median(),median_retention=common[ret].median()))
  for minimum in [1,30,100]:
   mask=pop[rate].between(0,1)&(pop[den]>=minimum);g=pop[mask]
   small.append(dict(family=family,sector=label,min_completion_cohort=minimum,institutions=len(g),completion_mean=g[rate].mean(),completion_weighted=np.average(g[rate],weights=g[den]) if len(g) else np.nan,cohort_students=g[den].sum()))
save(R,'outcome_definitions',rows);save(R,'same_institution_comparison',pair);save(R,'small_cohort_sensitivity',small)
# Do not force the predominant award variable to select IPEDS outcome metric families.
familycounts=[]
for value,g in d.groupby('PREDDEG'):
 familycounts.append(dict(predominant_award_code=value,institutions=len(g),completion_4_n=int(g.C150_4.notna().sum()),completion_l4_n=int(g.C150_L4.notna().sum()),retention_4_n=int(g.RET_FT4.notna().sum()),retention_l4_n=int(g.RET_FTL4.notna().sum())))
save(R,'predominant_vs_metric_coverage',familycounts)
# Field-of-study has program/cohort aggregates, not students; do not join to inflate institutions.
f=pd.read_csv(D/'Most-Recent-Cohorts-Field-of-Study.csv',usecols=['UNITID','OPEID6','CIPCODE','CREDLEV','MAIN','IPEDSCOUNT1','IPEDSCOUNT2'],dtype=str,keep_default_na=False)
key=['UNITID','OPEID6','CIPCODE','CREDLEV'];duplicates=int(f.duplicated(key).sum());identical=int(f.duplicated().sum())
facts=[dict(quantity='institution rows',n=len(d)),dict(quantity='institution fields',n=len(header)),dict(quantity='field-of-study rows',n=len(f)),dict(quantity='field-of-study compound-key duplicate rows',n=duplicates),dict(quantity='field-of-study identical selected rows',n=identical),dict(quantity='field-of-study distinct nonempty UNITID',n=f.loc[~f.UNITID.isin(['','NULL']), 'UNITID'].nunique()),dict(quantity='field-of-study rows without numeric UNITID',n=int(pd.to_numeric(f.UNITID,errors='coerce').isna().sum()))]
save(R,'grain_audit',facts)
# Reconciliation independent of rate weighting: weighted numerator from all valid institution records.
g=d[d.C150_4.between(0,1)&(d.D150_4>0)];direct=sum(float(r)*float(w) for r,w in zip(g.C150_4,g.D150_4))/sum(g.D150_4)
expected=[r for r in rows if r['family']=='Four-year metric' and r['sector']=='All reported sectors' and r['measure']=='150% completion'][0]['weighted_mean']
check(checks,'independent weighted completion recomputation',direct,f'{expected} within 1e-12',abs(direct-expected)<1e-12)
check(checks,'field of study is not joined into institution denominator',len(d),f'{len(x)} raw institutions',len(d)==len(x))
for name,obs in [('student assessment behavior linkage','Aggregate UNITID/OPEID/CIP identifiers; no student assessment records'),('future academic risk timing','Mixed aggregate reporting cohorts and no student event/deadline times'),('snapshot measurement years','Most-Recent filename without verified per-field local cohort vintage')]:evidence_gap(checks,name,obs,'Verified student/course events and later academic outcome','Blocks direct student early-warning inference; contextual only')
save(R,'verification',checks);manifest(R,[p,D/'Most-Recent-Cohorts-Field-of-Study.csv'])
print(pd.DataFrame(rows).query('sector == "All reported sectors"').to_string(index=False));print(pd.DataFrame(facts).to_string(index=False))
