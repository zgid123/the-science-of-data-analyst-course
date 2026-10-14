"""Observed browser, metric display, source preservation and reader-path checks."""
from pathlib import Path
import json,hashlib,sys,zipfile
import pandas as pd
from playwright.sync_api import sync_playwright
from delivery import BASE
NAMES=['fff','ednet','mooccubex','college-scorecard','pisa-2022','talis-2024']
def review(name,browser):
 r=BASE/'samples'/name;records=[]
 def check(n,observed,expected,ok):
  records.append(dict(check=n,observed=observed,expected=expected,status='PASS' if ok else 'FAIL'));assert ok,records[-1]
 for x in pd.read_csv(r/'results/source_manifest.csv').itertuples():
  p=BASE/x.file if str(x.file).startswith('datasets/') else BASE/'datasets'/name/x.file
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
  check('source unchanged '+p.name,h.hexdigest(),x.sha256,h.hexdigest()==x.sha256)
 if name=='ednet':
  meta=json.loads((r/'results/sampling.json').read_text())
  with zipfile.ZipFile(BASE/'datasets/ednet/ednet_kt1.zip') as z:
   frame=sorted([x for x in z.infolist() if x.filename.endswith('.csv')],key=lambda x:x.filename);digest=hashlib.sha256('\n'.join(f'{x.filename}|{x.CRC}|{x.file_size}' for x in frame).encode()).hexdigest()
  check('archive complete user-frame fingerprint unchanged',digest,meta['frame_fingerprint'],digest==meta['frame_fingerprint'])
 page=browser.new_page(viewport={'width':1440,'height':1000});errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
 page.goto((r/'dashboard/index.html').as_uri());page.wait_for_timeout(200)
 check('dashboard title',page.title(),'dataset-specific rendered title',len(page.title())>10)
 page.screenshot(path=str(r/'evidence/dashboard-desktop.png'))
 if name in ['fff','ednet']:
  mm=pd.read_csv(r/'results/model_metrics.csv');cuts=[30,60,90] if name=='fff' else [10,30,60]
  for cut in cuts:
   page.select_option('#cut',str(cut))
   for cap in [.1,.2,.3]:
    page.select_option('#cap',str(cap));row=mm[(mm.cutoff==cut)&(mm.capacity==cap)&(mm.model=='combined')&(mm.split=='test')].iloc[0];text=page.locator('#stats').inner_text()
    ok=f'{int(row.n):,}' in text and f'{int(row.alerts):,}' in text;check(f'display n/alerts reconcile: cutoff {cut}, capacity {cap}',text.replace('\n',' | '),'saved combined test n and alerts',ok)
    expected=len(mm[(mm.cutoff==cut)&(mm.split=='test')&((mm.capacity==cap)|(mm.capacity==0))]);check('model rows at selected cutoff/capacity',page.locator('#metricRows tbody tr').count(),expected,page.locator('#metricRows tbody tr').count()==expected)
  if name=='fff':
   for value in ['disability','age_band','final_result','behavior_group']:
    page.select_option('#auditGroup',value);check('audit filter '+value,page.locator('#auditRows tbody tr').count(),'at least two groups',page.locator('#auditRows tbody tr').count()>=2)
 elif name=='mooccubex':
  data=pd.read_csv(r/'results/field_context.csv')
  for minimum in [5,10,30,50]:
   page.select_option('#minCourses',str(minimum));n=int((data.courses>=minimum).sum());check('field course-count filter '+str(minimum),page.locator('#fieldRows tbody tr').count(),n,page.locator('#fieldRows tbody tr').count()==n)
  check('resource count reconciles',page.locator('#distribution').inner_text(),'67,325 exercise containers','67,325' in page.locator('#distribution').inner_text())
 elif name=='college-scorecard':
  data=pd.read_csv(r/'results/outcome_definitions.csv')
  for family in ['Four-year metric','Less-than-four-year metric']:
   page.select_option('#family',family)
   for sector in ['All reported sectors','Public','Private nonprofit','Private for-profit']:
    page.select_option('#sector',sector);x=data[(data.family==family)&(data.sector==sector)&(data.measure=='150% completion')].iloc[0];text=page.locator('#weightRows').inner_text();check(f'completion display {family}/{sector}',text[:180],'saved institution/cohort weighted means',f'{100*x.unweighted_mean:.1f}%' in text and f'{100*x.weighted_mean:.1f}%' in text)
 else:
  data=pd.read_csv(r/'results/practice_estimates.csv');countrycol='country';control='level' if name=='talis-2024' else 'type';vals=[1,2,3] if name=='talis-2024' else [1,2]
  for country in ['AUS','BRA']:
   if country not in data.country.unique():continue
   page.select_option('#country',country)
   for val in vals:
    page.select_option('#'+control,str(val));expected=data[(data.country==country)&(data.level==val)] if name=='talis-2024' else data[(data.country==country)&(data.source=='teacher')&(data.teacher_type==val)];id='practiceRows' if name=='talis-2024' else 'teacherRows';nr=page.locator('#'+id+' tbody tr').count();check(f'survey domain {country}/{val} row count',nr,len(expected),nr==len(expected))
    if len(expected):
     row=expected.iloc[0];text=page.locator('#'+id).inner_text();check('survey weighted share and valid n reconcile',text[:180],'CSV weighted proportion/valid denominator',f'{100*row.weighted:.1f}%' in text and f'{int(row.valid_n):,}' in text)
    else:check('unavailable domain explicitly undefined',page.locator('#'+id).inner_text(),'No observations / undefined','undefined' in page.locator('#'+id).inner_text())
 if name=='pisa-2022':
  optional=set(data[data.source=='school'].country)-set(data[data.source=='teacher'].country)
  if optional:
   absent=sorted(optional)[0];page.select_option('#country',absent);check('actual absent optional teacher domain '+absent,page.locator('#teacherRows').inner_text(),'explicit undefined state','undefined' in page.locator('#teacherRows').inner_text())
 page.click('#reset')
 # Actual reader paths: inspect every question section, supporting comparisons and scope notes.
 for index,section in enumerate(page.locator('main > section').all()):
  ident=section.get_attribute('id')
  if not ident:continue
  text=section.inner_text();check('reader path '+ident,text[:220],'readable question, evidence and limitation',len(text)>200)
  if index in [1,2,3]:section.screenshot(path=str(r/'evidence'/f'dashboard-{ident}.png'))
 for summary in page.locator('main > details > summary').all():summary.click()
 for a in page.locator('a').all():
  href=a.get_attribute('href') or ''
  if href and not href.startswith(('http:','https:','#')):
   exists=(r/'dashboard'/href.split('#')[0]).resolve().exists();check('dashboard local link '+href,exists,True,exists)
 check('reset retains rendered populated default',page.locator('main table').count(),'at least four evidence tables',page.locator('main table').count()>=4)
 # Test empty helper explicitly even where all exposed combinations have evidence.
 id='metricRows' if name in ['fff','ednet'] else ('fieldRows' if name=='mooccubex' else 'weightRows' if name=='college-scorecard' else 'practiceRows' if name=='talis-2024' else 'teacherRows')
 page.evaluate(f"tbl('{id}',[],[['n','n']])");check('empty helper does not fabricate zero',page.locator('#'+id).inner_text(),'undefined rates', 'undefined' in page.locator('#'+id).inner_text());page.click('#reset')
 forbidden=page.evaluate("Object.values(D).some(rows=>rows.some(r=>['id_student','user','IDTEACH','CNTTCHID'].some(k=>k in r)))");check('no individual identifiers in public embedded tables',forbidden,False,not forbidden)
 page.set_viewport_size({'width':390,'height':844});page.goto((r/'dashboard/index.html').as_uri());page.screenshot(path=str(r/'evidence/dashboard-mobile.png'));overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth');check('dashboard mobile page overflow',overflow,False,not overflow)
 page.set_viewport_size({'width':1440,'height':1000});page.goto((r/'report.html').as_uri());check('report rendered evidence tables',page.locator('table').count(),'at least four',page.locator('table').count()>=4);page.screenshot(path=str(r/'evidence/report-desktop.png'))
 for a in page.locator('a').all():
  href=a.get_attribute('href') or ''
  if href and not href.startswith(('http:','https:','#')):
   exists=(r/href.split('#')[0]).resolve().exists();check('report local link '+href,exists,True,exists)
 page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(r/'evidence/report-mobile.png'));overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth');check('report mobile page overflow',overflow,False,not overflow)
 check('JavaScript errors',errors,[],not errors)
 page.close();(r/'evidence/browser-review.json').write_text(json.dumps(records,indent=2));print(name,len(records),'checks passed',flush=True)

if __name__=='__main__':
 with sync_playwright() as p:
  candidates=list(Path('/root/.cache/ms-playwright').glob('chromium-*/chrome-linux-*/chrome'))
  browser=p.chromium.launch(executable_path=str(candidates[0]) if candidates else p.chromium.executable_path,headless=True)
  for name in sys.argv[1:] or NAMES:review(name,browser)
  browser.close()
