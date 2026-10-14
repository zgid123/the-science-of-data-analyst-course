"""Assessment-practice context from verified SPSS labels; no student early-risk model."""
import sys,json
from pathlib import Path
import pandas as pd,numpy as np,pyreadstat
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'_shared'))
from delivery import setup,save,check,evidence_gap,manifest
from survey import estimate,coded
R,D=setup('pisa-2022');checks=[]
rep=[f'W_FTCHRWT{i}' for i in range(1,81)]
T={'TC054Q01NA':('Develop own assessment',[1,2,3,4],[3,4]),'TC054Q04NA':('Written feedback beyond marks',[1,2,3,4],[3,4]),'TC054Q06NA':('Immediate task feedback',[1,2,3,4],[3,4]),'TC185Q04HA':('Moderate/high assessment training need',[1,2,3,4],[3,4])}
S={'SC034Q03TA':('Teacher-developed tests monthly or more',[1,2,3,4,5],[4,5]),'SC037Q06NA':('Systematic recording of results',[1,2,3],[1,2]),'SC035Q01NB':('Teacher tests guide learning',[1,2],[1]),'SC035Q09NB':('Teacher tests adapt instruction',[1,2],[1])}
t,tm=pyreadstat.read_sav(D/'CY08MSP_TCH_QQQ.SAV',usecols=['CNT','CNTSCHID','CNTTCHID','TCHTYPE','W_FTCHWT']+list(T)+rep,user_missing=True)
s,sm=pyreadstat.read_sav(D/'CY08MSP_SCH_QQQ.SAV',usecols=['CNT','CNTSCHID','W_SCHGRNRABWT']+list(S),user_missing=True)
labels=[]
for metadata,items,source in [(tm,T,'teacher'),(sm,S,'school')]:
 for item in items:labels.append(dict(source=source,field=item,label=metadata.column_names_to_labels[item],codes=json.dumps(metadata.variable_value_labels.get(item,{}),ensure_ascii=False)))
save(R,'verified_codebook',labels)
check(checks,'unique country-school questionnaire keys',int(s.duplicated(['CNT','CNTSCHID']).sum()),'0',not s.duplicated(['CNT','CNTSCHID']).any())
check(checks,'unique teacher keys',int(t.duplicated(['CNT','CNTTCHID']).sum()),'0',not t.duplicated(['CNT','CNTTCHID']).any())
# Mathematics and general-teacher sampling domains remain separate.
rows=[];missing=[];coverage=[]
for source,d,items,weight,reps in [('teacher',t,T,'W_FTCHWT',rep),('school',s,S,'W_SCHGRNRABWT',None)]:
 groupcols=['CNT','TCHTYPE'] if source=='teacher' else ['CNT']
 for key,g in d.groupby(groupcols):
  country=key[0] if isinstance(key,tuple) else key;typ=key[1] if isinstance(key,tuple) and len(key)>1 else 0
  coverage.append(dict(source=source,country=country,teacher_type=typ,respondents=len(g),positive_weight_n=int((g[weight]>0).sum()),schools=g.CNTSCHID.nunique()))
  for item,(meaning,valid,success) in items.items():
   vals=coded(g[item],valid,success);m=estimate(g,vals,weight,reps)
   rows.append(dict(source=source,country=country,teacher_type=typ,item=item,meaning=meaning,uncertainty='80 Fay-BRR replicates' if reps else 'No school replicate weights supplied; descriptive only',**m))
 for item,(_,valid,_) in items.items():
  for token,n in d.loc[~d[item].isin(valid),item].value_counts(dropna=False).items():missing.append(dict(source=source,item=item,nonvalid_code=str(token),rows=n))
save(R,'practice_estimates',rows);save(R,'coverage',coverage);save(R,'missing_codes',missing)
paired=[];need=[]
for (country,typ),g in t.groupby(['CNT','TCHTYPE']):
 written=coded(g.TC054Q04NA,[1,2,3,4],[3,4]);immediate=coded(g.TC054Q06NA,[1,2,3,4],[3,4]);both=np.isfinite(written)&np.isfinite(immediate)
 paired.append(dict(country=country,teacher_type=typ,comparison='Immediate minus written feedback',**estimate(g,np.where(both,immediate-written,np.nan),'W_FTCHWT',rep)))
 needs=coded(g.TC185Q04HA,[1,2,3,4],[3,4])
 for status in [0,1]:need.append(dict(country=country,teacher_type=typ,written_feedback='most/every lesson' if status else 'less often',**estimate(g,np.where(written==status,needs,np.nan),'W_FTCHWT',rep)))
save(R,'paired_feedback',paired);save(R,'training_need_context',need)
# The ESCS export is not a 2022 student-outcome file. Stream all rows to validate cycles/coverage.
trend=[];total=0;cyclecounts={};countries={}
for ch in pd.read_csv(D/'escs_trend.csv',chunksize=100000,usecols=['cycle','cnt','escs_trend']):
 total+=len(ch)
 for (cycle,country),g in ch.groupby(['cycle','cnt']):
  key=(int(cycle),country)
  if key not in countries:countries[key]=[0,0]
  countries[key][0]+=len(g);countries[key][1]+=int(g.escs_trend.notna().sum())
for (cycle,country),(n,valid) in countries.items():trend.append(dict(cycle=cycle,year={5:2012,6:2015,7:2018}.get(cycle,'unknown'),country=country,rows=n,escs_valid_n=valid))
save(R,'trend_export_coverage',trend)
check(checks,'trend export contains only documented earlier cycles',sorted({x['cycle'] for x in trend}),'[5,6,7]',{x['cycle'] for x in trend}=={5,6,7})
# No school/teacher to historical student join is attempted across incompatible populations/years.
check(checks,'teacher respondent accounting',sum(x['respondents'] for x in coverage if x['source']=='teacher'),f'{len(t)} source teacher rows',sum(x['respondents'] for x in coverage if x['source']=='teacher')==len(t))
first=next(x for x in rows if x['source']=='teacher' and x['valid_n']>0);g=t[(t.CNT==first['country'])&(t.TCHTYPE==first['teacher_type'])&t[first['item']].isin(T[first['item']][1])&(t.W_FTCHWT>0)]
manual=sum(float(w)*int(v in T[first['item']][2]) for w,v in zip(g.W_FTCHWT,g[first['item']]))/sum(g.W_FTCHWT)
check(checks,'independent teacher weighted rate',manual,f"{first['weighted']} within 1e-12",abs(manual-first['weighted'])<1e-12)
evidence_gap(checks,'student assessment trajectory and future outcome','No linked student submission/deadline/outcome table in local snapshot','Individual timed assessment records linked to later academic outcome','Context-only; no academic-risk model')
evidence_gap(checks,'school design-based uncertainty','No school replicate weights in supplied school file','School variance replicates/design variables','School weighted points are descriptive; no fabricated CI')
save(R,'verification',checks);manifest(R,[D/'CY08MSP_TCH_QQQ.SAV',D/'CY08MSP_SCH_QQQ.SAV',D/'escs_trend.csv',D/'ReadMe.txt'])
(R/'results/metadata.json').write_text(json.dumps(dict(teacher_rows=len(t),school_rows=len(s),trend_rows=total,teacher_types=tm.variable_value_labels['TCHTYPE'],teacher_replicates=80,fay=.5,school_weight=sm.column_names_to_labels['W_SCHGRNRABWT'],source='https://www.oecd.org/en/data/datasets/pisa-2022-database.html',variance_source='https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/03/pisa-2022-technical-report_599753f0/01820d6d-en.pdf'),indent=2))
print('Teachers',len(t),'schools',len(s),'trend rows',total);print('Country/domain estimates',len(rows));print(pd.DataFrame(paired).head().to_string(index=False))
