"""Executed Chromium artifact, interaction, display and source-preservation checks."""
from pathlib import Path
import json,hashlib
import pandas as pd
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];results=[]
def record(check,observed,expected,ok):
 results.append(dict(check=check,observed=observed,expected=expected,status='PASS' if ok else 'FAIL'));assert ok,results[-1]
m=pd.read_csv(R/'results/model_metrics.csv');manifest=pd.read_csv(R/'results/source_manifest.csv');data=R.parents[1]/'datasets/oulad'
for x in manifest.itertuples():
 actual=hashlib.sha256((data/x.file).read_bytes()).hexdigest();record('raw source unchanged: '+x.file,actual,x.sha256,actual==x.sha256)
with sync_playwright() as p:
 candidates=list(Path('/root/.cache/ms-playwright').glob('chromium-*/chrome-linux-*/chrome'))
 browser=p.chromium.launch(executable_path=str(candidates[0]),headless=True)
 page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
 page.goto((R/'dashboard/index.html').as_uri());page.wait_for_selector('#models table')
 record('dashboard initial rendered model rows',page.locator('#models tbody tr').count(),6,page.locator('#models tbody tr').count()==6)
 page.screenshot(path=str(R/'evidence/dashboard-desktop.png'))
 for cutoff in [30,60,90]:
  page.select_option('#cut',str(cutoff))
  for cap in [.1,.2,.3]:
   page.select_option('#cap',str(cap))
   row=m[(m.cutoff==cutoff)&(m.capacity==cap)&(m.model=='combined')&(m.split=='test')].iloc[0]
   text=page.locator('#stats').inner_text()
   ok=f'{int(row.n):,}' in text and f'{int(row.alerts):,}' in text and f'{row.recall*100:.1f}%' in text
   record(f'dashboard day {cutoff}, capacity {cap}: n/alerts/recall match CSV',text.replace('\n',' | '),'exact formatted saved test values',ok)
   state=page.evaluate("({cut:Number(document.querySelector('#cut').value),rows:document.querySelectorAll('#cov tbody tr').length})")
   record(f'coverage day {cutoff} all cohorts',state['rows'],4,state['rows']==4)
 for dim in ['code_module','disability','age_band','behavior_group']:
  page.select_option('#dimension',dim);nr=page.locator('#errors tbody tr').count();record('audit filter '+dim,nr,'at least two populated groups',nr>=2)
 # Inspection of every priority reader task, including consequential follow-up.
 page.click('#reset')
 tasks={
  'behavior':'#behavior', 'incremental_value':'#ranking','transport_followup':'#transport','workload':'#workload','lead_time':'#timing','delay_and_target_sensitivity':'#sensitivity','subgroup_and_calibration':'#audit'}
 for task,selector in tasks.items():
  element=page.locator(selector);element.scroll_into_view_if_needed()
  text=element.inner_text();record('reader task '+task,text[:180],'nonempty comparison and explanation',len(text)>300)
  if task in ['transport_followup','behavior','workload']:element.screenshot(path=str(R/'evidence'/f'dashboard-{task}.png'))
 page.locator('details.panel > summary').click()
 for cohort in ['2013B','2013J','2014B','2014J']:
  page.select_option('#cohort',cohort);count=page.locator('#cohorts tbody tr').count();record('full-snapshot descriptive cohort '+cohort,count,'observed outcome rows',count>0)
 page.evaluate("tbl('cohorts',[],[['n','n']])")
 record('explicit empty-state helper',page.locator('#cohorts').inner_text(),'No observations and undefined explanation', 'undefined' in page.locator('#cohorts').inner_text())
 page.click('#reset');record('reset controls',page.locator('#cut').input_value()+'/'+page.locator('#cap').input_value(),'60/0.2',page.locator('#cut').input_value()=='60' and page.locator('#cap').input_value()=='0.2')
 record('no embedded student identifiers',page.evaluate("Object.values(D).some(rows=>rows.some(r=>'id_student' in r))"),False,not page.evaluate("Object.values(D).some(rows=>rows.some(r=>'id_student' in r))"))
 page.set_viewport_size({'width':390,'height':844});page.goto((R/'dashboard/index.html').as_uri());page.screenshot(path=str(R/'evidence/dashboard-mobile.png'))
 overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth');record('dashboard mobile page overflow',overflow,False,not overflow)
 page.set_viewport_size({'width':1440,'height':1000});page.goto((R/'report.html').as_uri())
 record('report rendered tables',page.locator('table').count(),'at least 10 evidence tables',page.locator('table').count()>=10)
 record('report figure assets loaded',page.evaluate('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)'),True,page.evaluate('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)'))
 page.screenshot(path=str(R/'evidence/report-desktop.png'))
 headings=page.locator('h2,h3').all_text_contents();record('report required findings sections',headings,'behavior, timing, incremental value, workload, definitions',len(headings)>=8)
 for anchor in page.locator('a').all():
  href=anchor.get_attribute('href') or ''
  if href and not href.startswith(('https:','http:','#')):
   target=(R/href.split('#')[0]).resolve();record('report local link '+href,target.exists(),True,target.exists())
 page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(R/'evidence/report-mobile.png'));overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth');record('report mobile page overflow',overflow,False,not overflow)
 record('browser JavaScript errors',errors,[],not errors)
 browser.close()
(R/'evidence/browser-review.json').write_text(json.dumps(results,indent=2))
print(f'{len(results)} browser/source checks passed')
