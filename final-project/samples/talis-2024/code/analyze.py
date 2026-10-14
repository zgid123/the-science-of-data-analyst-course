"""Assessment-practice survey context; level extracts used once, with Fay-BRR uncertainty."""
import sys,json,zipfile,zlib
from pathlib import Path
import numpy as np,pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'_shared'))
from delivery import setup,save,check,evidence_gap,manifest
from survey import estimate,coded
R,D=setup('talis-2024');checks=[]
ITEMS={'TT4G53A':'End-unit assessment','TT4G53C':'Improvement feedback','TT4G53D':'Student self-assessment','TT4G53E':'Immediate task feedback','TT4G53F':'Check material learned','TT4G24D':'Need: assessment practices','TT4G24M':'Need: analysis/use of assessments','TT4G52C':'Digital feedback','TT4G52I':'Digital assessment'}
reps=[f'TRWGT{i}' for i in range(1,101)];keys=['IDCNTPOP','IDSCHOOL','IDTEACH'];cols=['CNTRY','IDCNTRY','IDCNTPOP','IDSCHOOL','IDTEACH','IDPOP','IDTQUEST','ADJRT24','TCHWGT']+list(ITEMS)+reps
frames=[];archive=[];paths=[]
with zipfile.ZipFile(D/'TALIS2024_teachers_NoESE_CSV.zip') as z:
 for name in ['atgintt4.csv','btgintt4.csv','ctgintt4.csv']:
  p=D/name;g=pd.read_csv(p,sep=';',usecols=cols);g['source']=name;frames.append(g);paths.append(p)
  check(checks,name+' unique teacher-population keys',int(g.duplicated(keys).sum()),'0 duplicate keys',not g.duplicated(keys).any())
  crc=0
  with p.open('rb') as f:
   for b in iter(lambda:f.read(1024*1024),b''):crc=zlib.crc32(b,crc)
  info=z.getinfo(name);archive.append(dict(file=name,rows=len(g),extracted_crc=crc,archive_crc=info.CRC,bytes=p.stat().st_size))
  check(checks,name+' extracted bytes match supplied zip member CRC',crc,f'{info.CRC}',crc==info.CRC)
  print(name,'teachers',len(g),flush=True)
f=pd.concat(frames,ignore_index=True);check(checks,'combined analytic level rows',len(f),f'{sum(len(x) for x in frames)} sum of three extracts',len(f)==sum(len(x) for x in frames))
# Combined export contains the same respondents and must not be appended as a new sample.
combined=pd.read_csv(D/'ttgintt4.csv',sep=';',usecols=keys+['IDPOP']+list(ITEMS))
check(checks,'combined export unique respondent keys',int(combined.duplicated(keys).sum()),'0',not combined.duplicated(keys).any())
left=f[keys+['IDPOP']+list(ITEMS)].sort_values(keys).reset_index(drop=True);right=combined[left.columns].sort_values(keys).reset_index(drop=True)
check(checks,'combined export equals level extracts on keys, levels and selected items',int((left.fillna(-999)!=right.fillna(-999)).any(axis=1).sum()) if left.shape==right.shape else -1,'0 mismatched respondent rows',left.shape==right.shape and (left.fillna(-999)==right.fillna(-999)).all().all())
save(R,'archive_overlap',archive);save(R,'population_coverage',f.groupby(['CNTRY','IDCNTPOP','IDPOP']).agg(teachers=('IDTEACH','size'),schools=('IDSCHOOL','nunique'),adjudication=('ADJRT24','min')).reset_index())
quality=[];out=[];forms=[]
for item,label in ITEMS.items():
 success=[3,4] # need items mean moderate/high need; practice means frequent/always
 for (country,level),g in f.groupby(['CNTRY','IDPOP']):
  vals=coded(g[item],[1,2,3,4],success);m=estimate(g,vals,'TCHWGT',reps)
  out.append(dict(country=country,level=level,item=item,meaning=label,adjudication=int(g.ADJRT24.min()),**m))
 for (level,form),g in f.groupby(['IDPOP','IDTQUEST']):forms.append(dict(level=level,form=form,item=item,rows=len(g),valid_n=int(g[item].isin([1,2,3,4]).sum()),valid_fraction=g[item].isin([1,2,3,4]).mean()))
 for token,n in f.loc[~f[item].isin([1,2,3,4]),item].value_counts(dropna=False).items():quality.append(dict(item=item,nonvalid_code=str(token),rows=n))
save(R,'practice_estimates',out);save(R,'form_coverage',forms);save(R,'missing_codes',quality)
paired=[];association=[]
for (country,level),g in f.groupby(['CNTRY','IDPOP']):
 a=coded(g.TT4G53E,[1,2,3,4],[3,4]);b=coded(g.TT4G53C,[1,2,3,4],[3,4]);valid=np.isfinite(a)&np.isfinite(b)
 m=estimate(g,np.where(valid,a-b,np.nan),'TCHWGT',reps);paired.append(dict(country=country,level=level,comparison='Immediate minus improvement feedback',**m))
 # Joint practice/training-need association is conditional on rotated form overlap, never imputed.
 for need,name in [('TT4G24D','assessment practices'),('TT4G24M','analysis/use of assessments')]:
  v=coded(g[need],[1,2,3,4],[3,4]);feedback=coded(g.TT4G53C,[1,2,3,4],[3,4]);
  for status in [0,1]:
   values=np.where(feedback==status,v,np.nan);m=estimate(g,values,'TCHWGT',reps);association.append(dict(country=country,level=level,need_item=need,need_meaning=name,feedback_group='frequent/always' if status else 'never/occasionally',**m))
save(R,'paired_feedback',paired);save(R,'need_feedback_association',association)
check(checks,'primary valid survey weights',int((~np.isfinite(f.TCHWGT)|(f.TCHWGT<=0)).sum()),'0 teachers',bool((np.isfinite(f.TCHWGT)&(f.TCHWGT>0)).all()))
# Independent vector-free country/level check, using valid response and positive final weights.
first=next(x for x in out if x['valid_n']>0);g=f[(f.CNTRY==first['country'])&(f.IDPOP==first['level'])&f[first['item']].isin([1,2,3,4])]
manual=sum(float(w)*int(v>=3) for w,v in zip(g.TCHWGT,g[first['item']]))/sum(g.TCHWGT)
check(checks,'independent weighted proportion',manual,f"{first['weighted']} within 1e-12",abs(manual-first['weighted'])<1e-12)
evidence_gap(checks,'student future risk linkage','Teachers/principals surveyed once, no student event/outcome linkage','Student assessment records linked to later academic outcomes','No student early-warning model or causal practice effect supported')
evidence_gap(checks,'absence versus form-assigned missingness','Questionnaire form IDs and nonvalid codes retained; full routing not reconstructed','Complete item-specific routing metadata for each respondent','Nonresponse/by-design missingness not equated; complete-case conditional estimates')
principal_scope=[]
for name in ['acgintt4.csv','bcgintt4.csv','ccgintt4.csv']:
 h=pd.read_csv(D/name,sep=';',nrows=0);gg=pd.read_csv(D/name,sep=';',usecols=['IDCNTPOP','IDSCHOOL']);principal_scope.append(dict(file=name,rows=len(gg),fields=len(h.columns),country_populations=gg.IDCNTPOP.nunique(),duplicate_school_keys=int(gg.duplicated(['IDCNTPOP','IDSCHOOL']).sum())))
save(R,'principal_scope',principal_scope)
save(R,'verification',checks);manifest(R,paths+[D/'ttgintt4.csv'])
(R/'results/metadata.json').write_text(json.dumps(dict(source='OECD TALIS 2024 local CSVs',levels=[1,2,3],rows=len(f),combined_rows=len(combined),replicates=100,fay=.5,variance='4/100 * sum((replicate estimate - full estimate)^2)',questionnaire='https://www.oecd.org/content/dam/oecd/en/about/programmes/edu/talis/talis2024questionnaires/TALIS2024TeacherQuestionnaireISCED1-2-3.pdf',variance_source='https://one.oecd.org/document/EDU/TALIS/GB%282025%299/en/pdf'),indent=2))
print('Country-level practice estimates',len(out));print('Rows',len(f),'same as combined',len(combined));print('Training/feedback common response valid total',sum(x['valid_n'] for x in association))
