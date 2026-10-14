"""Independent source-window checks and direct average-precision reconciliation."""
from pathlib import Path
import zipfile,json
import pandas as pd,numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
R=Path(__file__).resolve().parents[1];D=R.parents[1]/'datasets/ednet';SEED=20261013
f=pd.read_csv(R/'prepared/features.csv');q=pd.read_csv(D/'contents/questions.csv').set_index('question_id');metrics=pd.read_csv(R/'results/model_metrics.csv');checks=[];rng=np.random.default_rng(SEED)
with zipfile.ZipFile(D/'ednet_kt1.zip') as z:
 for cutoff in [10,30,60]:
  te=f[(f.cutoff==cutoff)&(f.split=='test')].reset_index(drop=True);chosen=rng.choice(len(te),min(100,len(te)),replace=False);bad=0
  for ix in chosen:
   row=te.iloc[ix];raw=pd.read_csv(z.open('KT1/'+row.user+'.csv'));order=raw.groupby('solving_id',sort=False).timestamp.min().sort_values(kind='stable').index.tolist();early=raw[raw.solving_id.isin(order[:cutoff])];future=raw[raw.solving_id.isin(order[cutoff:cutoff+20])]
   ea=(early.user_answer.to_numpy()==q.loc[early.question_id,'correct_answer'].to_numpy()).mean();fa=(future.user_answer.to_numpy()==q.loc[future.question_id,'correct_answer'].to_numpy()).mean();end=int((early.timestamp+early.elapsed_time).max());start=int(future.timestamp.min())
   bad+=int(abs(ea-row.early_accuracy)>1e-12 or abs(fa-row.future_accuracy)>1e-12 or end!=row.feature_end or start!=row.outcome_start or end>=start)
  checks.append(dict(check=f'cutoff {cutoff}: independent raw prefix/target/timing',examined=len(chosen),mismatches=bad,status='PASS' if not bad else 'FAIL',method='100 seeded random held-out users; raw ZIP re-read; pandas grouping and direct answer-key comparison'));assert bad==0
  for name,cols in [('score',['early_accuracy','part7_share']),('combined',['elapsed_median','elapsed_iqr','gap_median','span_days','repeat_fraction','early_accuracy','part7_share'])]:
   tr=f[(f.cutoff==cutoff)&(f.split=='train')];model=make_pipeline(SimpleImputer(strategy='median',add_indicator=True),StandardScaler(),LogisticRegression(C=1,max_iter=1000,random_state=SEED));model.fit(tr[cols],tr.risk);p=model.predict_proba(te[cols])[:,1];y=te.risk.to_numpy();order=np.argsort(-p,kind='stable');scores=p[order];yy=y[order];ends=np.r_[np.flatnonzero(np.diff(scores)!=0),len(scores)-1];cumulative=np.cumsum(yy)[ends];increments=np.diff(np.r_[0,cumulative]);ap=float(np.sum(increments*cumulative/(ends+1))/sum(y));expected=metrics[(metrics.cutoff==cutoff)&(metrics.model==name)&(metrics.split=='test')&(metrics.capacity==.2)].iloc[0].ap
   checks.append(dict(check=f'cutoff {cutoff}: direct AP for {name}',examined=len(te),mismatches=int(abs(ap-expected)>1e-12),observed=ap,expected=expected,status='PASS' if abs(ap-expected)<1e-12 else 'FAIL',method='Sort scores, combine ties, sum precision at positive increments; independent of sklearn metric'));assert abs(ap-expected)<1e-12
pd.DataFrame(checks).to_csv(R/'results/independent_checks.csv',index=False);print(json.dumps(checks,indent=2))
