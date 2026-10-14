"""Feasibility and assessment-content investigation of the actual local MOOCCubeX subset."""
import sys,json,collections
from pathlib import Path
import pandas as pd,numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'_shared'))
from delivery import setup,save,manifest,check,evidence_gap
R,D=setup('mooccubex');checks=[];courses=[];resources=[]
for line in (D/'data/entities/course.json').open():
 x=json.loads(line);res=x.get('resource',[])
 courses.append(dict(course=x['id'],resources=len(res),exercises=sum(str(z.get('resource_id','')).startswith('Ex_') for z in res),videos=sum(str(z.get('resource_id','')).startswith('V_') for z in res),other=sum(not str(z.get('resource_id','')).startswith(('Ex_','V_')) for z in res),field_labels=len(x.get('field',[]))))
 resources.extend(dict(course=x['id'],resource=z.get('resource_id'),chapter=z.get('chapter')) for z in res)
c=pd.DataFrame(courses);rr=pd.DataFrame(resources)
check(checks,'unique course ids',int(c.course.duplicated().sum()),'0',c.course.is_unique)
check(checks,'course resource decomposition',int((c.resources!=c.exercises+c.videos+c.other).sum()),'0 course count discrepancies',bool((c.resources==c.exercises+c.videos+c.other).all()))
save(R,'course_summary',c.drop(columns='course')) # aggregate-ish per anonymous course row, no personal text
summary=[]
for col in ['resources','exercises','videos']:
 summary.append(dict(measure=col,courses=len(c),zero_n=int((c[col]==0).sum()),mean=c[col].mean(),q25=c[col].quantile(.25),median=c[col].median(),q75=c[col].quantile(.75),p95=c[col].quantile(.95),max=c[col].max(),total=c[col].sum()))
save(R,'opportunity_distribution',summary)
rel=[];sets={}
for name in ['concept-problem','concept-course','course-teacher','user-reply','comment-reply']:
 p=D/'data/relations'/f'{name}.txt';pairs=[];malformed=0
 for line in p.open():
  bits=line.rstrip('\r\n').split('\t')
  if len(bits)!=2:malformed+=1;continue
  pairs.append(tuple(bits))
 unique=set(pairs);sets[name]=unique
 rel.append(dict(relation=name,raw_rows=len(pairs),unique_pairs=len(unique),duplicate_rows=len(pairs)-len(unique),duplicate_fraction=(len(pairs)-len(unique))/len(pairs) if pairs else np.nan,left_entities=len({x[0] for x in unique}),right_entities=len({x[1] for x in unique}),malformed_rows=malformed))
 check(checks,name+' malformed relation rows',malformed,'0',malformed==0)
save(R,'relation_quality',rel)
cp=sets['concept-problem'];cc=sets['concept-course'];pconcept={x[0] for x in cp};cconcept={x[0] for x in cc};linkedcourses={x[1] for x in cc};localcourses=set(c.course)
# Concept overlap is semantic context, never a direct exercise-to-problem mapping.
linkage=[dict(check='courses with concept-course edge',numerator=len(localcourses&linkedcourses),denominator=len(localcourses)),dict(check='concept-course target courses present locally',numerator=len(linkedcourses&localcourses),denominator=len(linkedcourses)),dict(check='problem concepts also linked to courses',numerator=len(pconcept&cconcept),denominator=len(pconcept)),dict(check='distinct course exercise ids',numerator=rr[rr.resource.str.startswith('Ex_',na=False)].resource.nunique(),denominator=rr[rr.resource.str.startswith('Ex_',na=False)].shape[0]),dict(check='course-resource duplicate memberships',numerator=int(rr.duplicated(['course','resource']).sum()),denominator=len(rr))]
for row in linkage:row['fraction']=row['numerator']/row['denominator'] if row['denominator'] else np.nan
save(R,'content_linkage',linkage)
fields=[];manual=[]
for line in (D/'data/relations/course-field.json').open():
 x=json.loads(line);cid='C_'+str(x['course_id']);manual.append(cid)
 for field in x.get('field',[]):fields.append(dict(course=cid,field=field))
f=pd.DataFrame(fields).drop_duplicates();joined=f.merge(c,on='course',how='left',validate='many_to_one');save(R,'field_join_coverage',[dict(field_memberships=len(f),matched_memberships=int(joined.resources.notna().sum()),unmatched_memberships=int(joined.resources.isna().sum()),manual_courses=f.course.nunique(),matched_courses=joined[joined.resources.notna()].course.nunique(),unmatched_courses=joined[joined.resources.isna()].course.nunique())]);check(checks,'field join retains exactly one row per unique membership',len(joined),f'{len(f)} memberships',len(joined)==len(f));joined=joined[joined.resources.notna()].copy()
byfield=joined.groupby('field').agg(courses=('course','nunique'),mean_exercises=('exercises','mean'),median_exercises=('exercises','median'),zero_exercise_courses=('exercises',lambda x:int((x==0).sum())),median_videos=('videos','median')).reset_index();byfield['exercise_coverage']=1-byfield.zero_exercise_courses/byfield.courses;save(R,'field_context',byfield)
for label,mask in [('Manual field label',c.course.isin(manual)),('No manual field label',~c.course.isin(manual))]:
 pop=c[mask];savepath=None
 # Stash explicitly comparable coverage instead of equating manual/machine field labels.
 rel.append({}) if False else None
save(R,'manual_label_sensitivity',[dict(group=label,n=int(mask.sum()),mean_exercises=c.loc[mask,'exercises'].mean(),median_exercises=c.loc[mask,'exercises'].median(),exercise_coverage=(c.loc[mask,'exercises']>0).mean()) for label,mask in [('Manual field label',c.course.isin(manual)),('No manual field label',~c.course.isin(manual))]])
queries=[]
for line in (D/'data/relations/user-xiaomu.json').open():
 x=json.loads(line);queries.append((x.get('user_id'),x.get('question_type'),x.get('question')))
x=pd.DataFrame(queries,columns=['user','type','question']);save(R,'help_query_types',x.groupby('type').agg(rows=('user','size'),users=('user','nunique'),distinct_questions=('question','nunique')).reset_index())
requirements=[]
for file,meaning in [('entities/user.json','enrollment and timing'),('relations/user-problem.json','student submission time, correctness and score'),('relations/exercise-problem.json','exercise-container to problem linkage (documented JSON location)'),('relations/exercise-problem.txt','exercise-container to problem linkage (documented TXT variant)'),('entities/problem.json','problem identifiers, content and scores'),('entities/reply.json','reply text and creation time')]:
 present=(D/'data'/file).exists();requirements.append(dict(required_file=file,present=present,needed_for=meaning))
save(R,'evidence_requirements',requirements)
for name,obs in [('student assessment trajectories','No local user-problem event file'),('later academic adverse outcomes','No local linked outcome table'),('assessment deadline obligations','Course resource chapter labels are not due dates'),('exercise to problem linkage','Neither documented exercise-problem file variant is present')]:evidence_gap(checks,name,obs,'Verified linked student/course/time/outcome evidence','Blocks student-level early-warning inference')
save(R,'verification',checks)
paths=[D/'data/entities/course.json',D/'data/relations/course-field.json',D/'data/relations/concept-problem.txt',D/'data/relations/concept-course.txt',D/'data/relations/user-xiaomu.json',D/'docs/course-en.md',D/'docs/user-en.md']
manifest(R,paths)
print(pd.DataFrame(summary).to_string(index=False));print(pd.DataFrame(rel).to_string(index=False));print(pd.DataFrame(linkage).to_string(index=False));print('All full relevant tables inspected; source data preserved.')
