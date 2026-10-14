"""User-sampled EdNet KT1 within-user temporal proxy study; no course-failure claim."""
import sys,json,csv,io,zipfile,hashlib
from pathlib import Path
import numpy as np,pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score,roc_auc_score,brier_score_loss,confusion_matrix
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'_shared'))
from delivery import setup,save,check,evidence_gap,manifest
R,D=setup('ednet');SEED=20261013;checks=[];rng=np.random.default_rng(SEED)
q=pd.read_csv(D/'contents/questions.csv').set_index('question_id');check(checks,'question key duplicates',int(q.index.duplicated().sum()),'0',q.index.is_unique)
qmap=q[['correct_answer','part','bundle_id']].to_dict('index')
manifest(R,[D/'contents/questions.csv'])
rows=[];selection=[];badrows=0;unmatched=0;overlap=0;usersinvalid=0;rawrows=0;bundledata=[]
with zipfile.ZipFile(D/'ednet_kt1.zip') as z:
 frame=sorted([x for x in z.infolist() if x.filename.endswith('.csv')],key=lambda x:x.filename)
 selected=rng.choice(len(frame),min(50000,len(frame)),replace=False);infos=[frame[j] for j in selected]
 # Sample halves are randomly allocated before reading; user split fixed before eligibility.
 ids=np.arange(len(infos));trainidx,remain=train_test_split(ids,test_size=.3,random_state=SEED);valididx,testidx=train_test_split(remain,test_size=.5,random_state=SEED)
 split={int(j):'train' for j in trainidx};split.update({int(j):'validation' for j in valididx});split.update({int(j):'test' for j in testidx})
 mapping={x.filename:j for j,x in enumerate(infos)}
 metadata=dict(seed=SEED,frame_users=len(frame),sample_users=len(infos),sampling_fraction=len(infos)/len(frame),archive_uncompressed_bytes=sum(x.file_size for x in frame),frame_fingerprint=hashlib.sha256('\n'.join(f'{x.filename}|{x.CRC}|{x.file_size}' for x in frame).encode()).hexdigest(),archive_bytes=(D/'ednet_kt1.zip').stat().st_size,method='uniform users without replacement from complete local zip central directory; 70/15/15 fixed held-out users; sampled halves for stability',source='https://github.com/riiid/ednet')
 (R/'results/sampling.json').write_text(json.dumps(metadata,indent=2))
 for count,x in enumerate(sorted(infos,key=lambda x:x.header_offset)):
  j=mapping[x.filename];userid=Path(x.filename).stem;records=list(csv.DictReader(io.StringIO(z.read(x).decode())))
  rawrows+=len(records);selection.append(dict(file=x.filename,crc=x.CRC,bytes=x.file_size,split=split[j],half=j%2))
  valid=[];invalid=False
  for record in records:
   content=qmap.get(record['question_id'])
   if content is None:unmatched+=1;invalid=True;continue
   try:
    stamp=int(record['timestamp']);elapsed=int(record['elapsed_time']);sid=int(record['solving_id'])
    if elapsed<0 or record['user_answer'] not in 'abcd' or (content['part']==2 and record['user_answer']=='d'):badrows+=1;invalid=True;continue
   except (ValueError,KeyError):badrows+=1;invalid=True;continue
   valid.append(dict(sid=sid,stamp=stamp,end=stamp+elapsed,elapsed=elapsed,qid=record['question_id'],correct=int(record['user_answer']==content['correct_answer']),part=content['part'],bundle=content['bundle_id']))
  if invalid:usersinvalid+=1;continue # no silently shortened trajectory after invalid response
  if not valid:continue
  # Bundle sessions are observed solving_id groups; same question rows do not imply separate attempts.
  bundles={}
  for v in valid:bundles.setdefault(v['sid'],[]).append(v)
  ordered=sorted(bundles.values(),key=lambda a:min(v['stamp'] for v in a))
  # Record global frame coverage for each proposed observation point.
  for cut in [10,30,60]:
   if len(ordered)<cut+20:continue
   early=[v for b in ordered[:cut] for v in b];future=[v for b in ordered[cut:cut+20] for v in b]
   cutoff=max(v['end'] for v in early);first=min(v['stamp'] for v in future)
   if first<=cutoff:overlap+=1;continue
   durations=np.array([max(v['elapsed'] for v in b)/1000 for b in ordered[:cut]])
   starts=np.array([min(v['stamp'] for v in b) for b in ordered[:cut]])
   seen={v['qid'] for v in early};novel=[v for v in future if v['qid'] not in seen]
   accuracy=np.mean([v['correct'] for v in future]);parts=[v['part'] for v in future]
   rows.append(dict(user=userid,cutoff=cut,split=split[j],half=j%2,bundles_total=len(ordered),early_accuracy=np.mean([v['correct'] for v in early]),elapsed_median=np.median(durations),elapsed_iqr=np.quantile(durations,.75)-np.quantile(durations,.25),gap_median=np.median(np.diff(starts))/3600000,span_days=(cutoff-min(starts))/86400000,repeat_fraction=1-len(seen)/len(early),part7_share=np.mean([v['part']==7 for v in early]),future_accuracy=accuracy,risk=int(accuracy<.4),risk50=int(accuracy<.5),novel_future_accuracy=np.mean([v['correct'] for v in novel]) if len(novel)>=10 else np.nan,novel_future_n=len(novel),future_question_n=len(future),future_part=max(set(parts),key=parts.count),lead_first_hours=(first-cutoff)/3600000,lead_last_days=(max(v['end'] for v in future)-cutoff)/86400000,feature_end=cutoff,outcome_start=first))
  if (count+1)%5000==0:print('Read',count+1,'sample users; eligible snapshots',len(rows),flush=True)
pd.DataFrame(selection).to_csv(R/'prepared/sample_manifest.csv',index=False)
f=pd.DataFrame(rows);f.to_csv(R/'prepared/features.csv',index=False)
check(checks,'feature completion before future question presentation',int((f.feature_end>=f.outcome_start).sum()),'0 snapshots',bool((f.feature_end<f.outcome_start).all()))
check(checks,'unique user-cutoff rows',int(f.duplicated(['user','cutoff']).sum()),'0',not f.duplicated(['user','cutoff']).any())
check(checks,'one split per user across cutoffs',int((f.groupby('user').split.nunique()>1).sum()),'0',not (f.groupby('user').split.nunique()>1).any())
quality=[dict(issue='sample users',n=len(selection)),dict(issue='raw sampled response rows',n=rawrows),dict(issue='unmatched question rows',n=unmatched),dict(issue='invalid timestamp/elapsed/answer rows',n=badrows),dict(issue='users excluded for any invalid/unmatched row',n=usersinvalid),dict(issue='overlapping prefix/outcome windows excluded',n=overlap)]
save(R,'data_quality',quality)
BEH=['elapsed_median','elapsed_iqr','gap_median','span_days','repeat_fraction'];SCORE=['early_accuracy'];CONTEXT=['part7_share']
def fit(tr,cols,y='risk'):
 model=make_pipeline(SimpleImputer(strategy='median',add_indicator=True),StandardScaler(),LogisticRegression(C=1,max_iter=1000,random_state=SEED));model.fit(tr[cols],tr[y]);return model

def metric(y,p,t):
 pred=p>=t;tn,fp,fn,tp=confusion_matrix(y,pred,labels=[0,1]).ravel()
 return dict(n=len(y),prevalence=float(np.mean(y)),ap=average_precision_score(y,p) if sum(y) else np.nan,auc=roc_auc_score(y,p) if len(set(y))==2 else np.nan,brier=brier_score_loss(y,p),threshold=t,alerts=int(sum(pred)),alert_rate=float(np.mean(pred)),precision=tp/(tp+fp) if tp+fp else np.nan,recall=tp/(tp+fn) if tp+fn else np.nan,tp=int(tp),fp=int(fp),fn=int(fn),tn=int(tn))
metrics=[];assoc=[];coverage=[];leads=[];unc=[];sensitivity=[];errors=[];calibration=[];stability=[]
for cut,g in f.groupby('cutoff'):
 tr=g[g.split=='train'];va=g[g.split=='validation'];te=g[g.split=='test'].reset_index(drop=True)
 coverage.append(dict(cutoff=cut,sampled_users=len(selection),eligible_users=len(g),coverage=len(g)/len(selection),train_n=len(tr),validation_n=len(va),test_n=len(te),test_risk=te.risk.mean()))
 for name,pop in [('low prior accuracy',te[te.early_accuracy<.4]),('higher prior accuracy',te[te.early_accuracy>=.4])]:assoc.append(dict(cutoff=cut,group=name,n=len(pop),future_risk=pop.risk.mean(),future_accuracy=pop.future_accuracy.mean(),elapsed_median=pop.elapsed_median.median(),gap_median=pop.gap_median.median(),repeat_mean=pop.repeat_fraction.mean()))
 for risk,pop in te.groupby('risk'):assoc.append(dict(cutoff=cut,group='Later low accuracy' if risk else 'Later higher accuracy',n=len(pop),future_risk=pop.risk.mean(),future_accuracy=pop.future_accuracy.mean(),elapsed_median=pop.elapsed_median.median(),gap_median=pop.gap_median.median(),repeat_mean=pop.repeat_fraction.mean()))
 probs={};ths={}
 for name,cols in [('behavior',BEH+CONTEXT),('score',SCORE+CONTEXT),('combined',BEH+SCORE+CONTEXT)]:
  model=fit(tr,cols);pv=model.predict_proba(va[cols])[:,1];pt=model.predict_proba(te[cols])[:,1];probs[name]=pt
  for capacity in [.1,.2,.3]:
   t=float(np.quantile(pv,1-capacity,method='higher'));ths[(name,capacity)]=t
   for split,pop,p in [('validation',va,pv),('test',te,pt)]:metrics.append(dict(cutoff=cut,model=name,capacity=capacity,split=split,**metric(pop.risk.to_numpy(),p,t)))
 for name,p,t in [('prevalence',np.full(len(te),tr.risk.mean()),1.),('prior_accuracy_rule',(te.early_accuracy<.4).astype(float).to_numpy(),.5)]:metrics.append(dict(cutoff=cut,model=name,capacity=0,split='test',**metric(te.risk.to_numpy(),p,t)))
 y=te.risk.to_numpy();diff=[]
 rr=np.random.default_rng(SEED)
 for _ in range(500):
  ix=rr.integers(0,len(te),len(te));diff.append(average_precision_score(y[ix],probs['combined'][ix])-average_precision_score(y[ix],probs['score'][ix]))
 lo,hi=np.quantile(diff,[.025,.975]);unc.append(dict(cutoff=cut,comparison='combined minus score AP',estimate=average_precision_score(y,probs['combined'])-average_precision_score(y,probs['score']),lo=lo,hi=hi))
 pt=probs['combined'];t=ths[('combined',.2)];pred=pt>=t
 for name,mask in [('all eligible',np.ones(len(te),dtype=bool)),('flagged future low accuracy',pred&(y==1))]:
  pop=te[mask];leads.append(dict(cutoff=cut,group=name,n=len(pop),first_hours_median=pop.lead_first_hours.median(),first_hours_q25=pop.lead_first_hours.quantile(.25),first_hours_q75=pop.lead_first_hours.quantile(.75),last_days_median=pop.lead_last_days.median(),first_under_1hour_n=int((pop.lead_first_hours<1).sum())))
 for part,ix in te.groupby('future_part').indices.items():errors.append(dict(cutoff=cut,future_dominant_part=part,**metric(y[ix],pt[ix],t)))
 for half,ix in te.groupby('half').indices.items():stability.append(dict(cutoff=cut,half=half,**metric(y[ix],pt[ix],t)))
 for b in range(5):
  mask=(pt>=b*.2)&((pt<(b+1)*.2) if b<4 else pt<=1)
  if mask.any():calibration.append(dict(cutoff=cut,bin=f'{b*.2:.1f}–{(b+1)*.2:.1f}',n=int(mask.sum()),predicted=float(pt[mask].mean()),observed=float(y[mask].mean())))
 # Fixed alternate outcome and novel-item restriction, not candidate tuning.
 for setting,target in [('future_accuracy_below_50','risk50'),('novel_future_items','novel_future_accuracy')]:
  tra=tr.copy();vaa=va.copy();tea=te.copy()
  if target=='novel_future_accuracy':
   tra=tra[tra[target].notna()];vaa=vaa[vaa[target].notna()];tea=tea[tea[target].notna()]
   for d in [tra,vaa,tea]:d['alternate']=(d[target]<.4).astype(int)
  else:
   for d in [tra,vaa,tea]:d['alternate']=d[target]
  for name,cols in [('score',SCORE+CONTEXT),('combined',BEH+SCORE+CONTEXT)]:
   model=fit(tra,cols,'alternate');pv=model.predict_proba(vaa[cols])[:,1];pp=model.predict_proba(tea[cols])[:,1];tt=np.quantile(pv,.8,method='higher');sensitivity.append(dict(cutoff=cut,setting=setting,model=name,**metric(tea.alternate.to_numpy(),pp,tt)))
 check(checks,f'day-bundle cutoff {cut}: primary confusion total',int(sum(confusion_matrix(y,pred,labels=[0,1]).ravel())),f'{len(te)} held-out users',sum(confusion_matrix(y,pred,labels=[0,1]).ravel())==len(te))
for n,d in [('model_metrics',metrics),('behavior_comparisons',assoc),('coverage',coverage),('lead_time',leads),('uncertainty',unc),('sensitivity',sensitivity),('future_part_errors',errors),('calibration',calibration),('sampling_stability',stability)]:save(R,n,d)
evidence_gap(checks,'official academic adverse outcome','No course result or official TOEIC score in local files','Linked future academic result','Practice proxy only; course-risk claims unsupported')
evidence_gap(checks,'calendar temporal transport','Published timestamps shifted; no verified shared real calendar','Training labels known before a future-cohort deployment','Within-snapshot held-out-user estimate only')
evidence_gap(checks,'actual answer release and record availability','Question-presented timestamp and elapsed_time proxy','Actual completion/logging timestamp','Timing conditional on duration interpretation')
save(R,'verification',checks)
print(pd.DataFrame(metrics).query('split == "test" and (capacity == .2 or capacity == 0)').to_string(index=False),flush=True)
