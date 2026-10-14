"""Descriptive cohorts and independent feature checks; runs after analyze.py."""
from pathlib import Path
import json,csv
import pandas as pd
R=Path(__file__).resolve().parents[1];D=R.parents[1]/'datasets'/'oulad'
rows=[];checks=[]
a=pd.read_csv(D/'assessments.csv');s=pd.read_csv(D/'studentAssessment.csv')
for c in [30,60,90]:
 f=pd.read_csv(R/'prepared'/f'features_day_{c}.csv')
 for (cohort,mod,outcome),g in f.groupby(['code_presentation','code_module','final_result']):
  rows.append(dict(cutoff=c,cohort=cohort,module=mod,outcome=outcome,n=len(g),due_n=int((g.due_count>0).sum()),missing_fraction=g.missing_fraction.mean(),ontime_fraction=g.ontime_fraction.mean(),mean_score=g.mean_score.mean()))
 # independent raw lookup of every primary test enrollment's due completion fraction
 test=pd.read_csv(R/'prepared'/'test_predictions.csv');test=test[test.cutoff==c]
 lookup={(int(x.id_assessment),int(x.id_student)):x for x in s.itertuples()}
 schedules={key:g for key,g in a[(a.assessment_type!='Exam')&(a.date>=0)&(a.date<=c)].groupby(['code_module','code_presentation'])}
 features=f.set_index(['code_module','code_presentation','id_student']);bad=0;examined=0
 for x in test.itertuples():
  key=(x.code_module,x.code_presentation,x.id_student);sched=schedules.get(key[:2]);ff=features.loc[key]
  count=0 if sched is None else len(sched)
  submitted=0
  if sched is not None:
   for ass in sched.itertuples():
    row=lookup.get((ass.id_assessment,x.id_student))
    submitted+=bool(row and row.is_banked==0 and row.date_submitted<=c)
  expected=1-submitted/count if count else float('nan')
  same=(pd.isna(expected) and pd.isna(ff.missing_fraction)) or abs(expected-ff.missing_fraction)<1e-12
  bad+=int(count!=ff.due_count or not same);examined+=1
 checks.append(dict(cutoff=c,check='independent raw opportunity and missing-fraction reconciliation',enrollments_examined=examined,mismatches=bad,status='PASS' if bad==0 else 'FAIL'))
pd.DataFrame(rows).to_csv(R/'results'/'cohort_behaviors.csv',index=False)
pd.DataFrame(checks).to_csv(R/'results'/'independent_checks.csv',index=False)
assert all(x['mismatches']==0 for x in checks)
print(json.dumps(checks,indent=2))

# Material unavailable evidence is recorded separately from numerical gate passes.
rows=[('Score release days','No score-release field in studentAssessment.csv','Observed score availability by warning cutoff','NOT VERIFIED','Score estimates conditional on +14/+28 day assumptions'),('Submission logging availability','Event day recorded; insertion/revision timestamps absent','Submission record actually visible by warning cutoff','NOT VERIFIED','Behavior warning conditional on timely logging; +7 day challenge'),('Historical label publication','Actual publication day absent; calendar bound assumes +60 days','Labels released before deployment','NOT VERIFIED','Temporal simulation conditional on publication assumption'),('Failure event timing','Final Fail category without event/release day','Actual warning-to-failure interval','NOT VERIFIED','Course-end proxy only'),('Individual assessment applicability','Schedules available; individual extensions/exemptions absent','Due denominator equals individual obligation','NOT VERIFIED','Absent due records remain proxy behavior'),('Stakeholder capacity','No supplied workload limit','Educator-approved review capacity','NOT VERIFIED','10/20/30 percent are proposed comparisons'),('Intervention effectiveness','No intervention implemented','Observed support effect','NOT APPLICABLE','No intervention-effect claim')]
pd.DataFrame(rows,columns=['check','observed','expected','status','consequence']).assign(method='Source schema/record and design review; REPORT.md timing/limits').to_csv(R/'results'/'availability_review.csv',index=False)
