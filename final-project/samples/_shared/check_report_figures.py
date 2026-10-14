"""Check figure-source lineage, rendered assets, export links and mobile layout."""
from pathlib import Path
import sys,json,hashlib
import pandas as pd
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
NAMES=['fff','ednet','mooccubex','college-scorecard','pisa-2022','talis-2024']
with sync_playwright() as p:
 exe=next(Path('/root/.cache/ms-playwright').glob('chromium-*/chrome-linux-*/chrome'));b=p.chromium.launch(executable_path=str(exe),headless=True)
 for name in sys.argv[1:] or NAMES:
  r=R/name;checks=[]
  def record(check,observed,expected,ok):
   checks.append(dict(check=check,observed=observed,expected=expected,status='PASS' if ok else 'FAIL'));assert ok,checks[-1]
  ledger=json.loads((r/'evidence/report-figures.json').read_text());record('Finding-specific chart count',len(ledger),'2',len(ledger)==2)
  for row in ledger:
   for src in row['sources']:
    digest=hashlib.sha256((r/src['file']).read_bytes()).hexdigest();record(row['figure']+' source fingerprint '+src['file'],digest,src['sha256'],digest==src['sha256'])
   frame=pd.read_csv(r/row['plotted_data']);record(row['figure']+' exported plotted rows',len(frame),row['plotted_rows'],len(frame)==row['plotted_rows'])
   for f in ['png','svg','plotted_data']:record(row['figure']+' '+f,(r/row[f]).stat().st_size,'positive bytes',(r/row[f]).stat().st_size>0)
  page=b.new_page(viewport={'width':1440,'height':1000});page.goto((r/'report.html').as_uri());page.wait_for_function('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)')
  record('Report charts render',page.locator('img').count(),len(ledger),page.locator('img').count()==len(ledger))
  for index,img in enumerate(page.locator('img').all()):
   record('Chart '+str(index+1)+' caption/alt present',img.get_attribute('alt'),'population and limitation caption',len(img.get_attribute('alt') or '')>60);img.screenshot(path=str(r/'evidence'/f'report-chart-{index+1}.png'))
  for a in page.locator('a').all():
   href=a.get_attribute('href') or ''
   if href and not href.startswith(('https:','http:','#')):record('Local report link '+href,(r/href).resolve().is_file(),True,(r/href).resolve().is_file())
  page.screenshot(path=str(r/'evidence/report-with-charts-desktop.png'))
  page.set_viewport_size({'width':390,'height':844});page.locator('img').first.scroll_into_view_if_needed();page.screenshot(path=str(r/'evidence/report-with-charts-mobile.png'));okay=page.evaluate('document.documentElement.scrollWidth<=innerWidth');record('Mobile page stays within viewport',okay,True,okay)
  width=page.locator('.report-figure img').first.evaluate('(el)=>el.getBoundingClientRect().width');record('Mobile figure preserves readable plotting width',width,'at least 900 CSS pixels',width>=900)
  offset=page.locator('.report-figure').first.evaluate('(el)=>{el.scrollLeft=el.scrollWidth;return el.scrollLeft}');record('Mobile figure can scroll horizontally',offset,'positive offset',offset>0)
  page.close();(r/'evidence/report-chart-review.json').write_text(json.dumps(checks,indent=2));print(name,len(checks),'figure/render/link checks passed',flush=True)
 b.close()
