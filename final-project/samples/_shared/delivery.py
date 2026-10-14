"""Shared portable presentation helpers; analytical layouts are study-specific."""
from pathlib import Path
import json,html,hashlib,re
import numpy as np,pandas as pd,markdown
BASE=Path(__file__).resolve().parents[2]
CSS='''body{background:#f5f6f8;color:#192b3b;font:16px/1.65 system-ui,sans-serif;margin:0}main{max-width:1180px;margin:auto;padding:32px}h1{font-size:34px;line-height:1.2;max-width:1000px}h2{font-size:24px;margin-top:34px}h3{font-size:19px}a{color:#126b70}section,.panel{padding:24px;background:white;border:1px solid #dbe1e7;border-radius:10px;margin:22px 0}.note{border-left:4px solid #b77632;background:#fff5e8;padding:16px}.muted{color:#52647a}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:13px;white-space:nowrap}th,td{padding:9px 12px;text-align:left;border-bottom:1px solid #dde2e7}th{background:#edf1f4}tr:hover{background:#f1f6f6}select,button{font:inherit;background:white;border:1px solid #a9b6c4;border-radius:5px;padding:7px}label{display:inline-block;margin:10px 20px 10px 0}nav{display:flex;flex-wrap:wrap;gap:20px}svg,img{max-width:100%;height:auto}.report-figure{overflow:auto;max-width:100%}.report-figure img{display:block;width:100%;max-width:none;min-width:900px}.figure-hint{display:none;font-size:13px;color:#52647a}.stats{display:flex;gap:24px;flex-wrap:wrap}.stat{border-top:3px solid #126b70;padding:12px;flex:1;min-width:180px}.stat strong{font-size:28px;display:block}details{margin:12px 0}@media(max-width:650px){.figure-hint{display:block}main{padding:16px}section,.panel{padding:16px}h1{font-size:27px}label{display:block}}'''
JS='''const $=id=>document.getElementById(id),esc=x=>String(x??'—').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])),pc=x=>x==null?'—':(x*100).toFixed(1)+'%',dec=x=>x==null?'—':Number(x).toFixed(3),num=x=>x==null?'—':Number(x).toLocaleString('en-US',{maximumFractionDigits:0});
function tbl(id,rows,cols){$(id).innerHTML=rows.length?'<div class="scroll"><table><thead><tr>'+cols.map(c=>'<th>'+esc(c[1])+'</th>').join('')+'</tr></thead><tbody>'+rows.map(r=>'<tr>'+cols.map(c=>'<td>'+esc((c[2]||String)(r[c[0]]))+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>':'<p>No observations for this selection. Rates are undefined.</p>';}
function bars(id,rows,key,label,fmt=pc){let h=rows.length*40+35;$(id).innerHTML='<svg viewBox="0 0 960 '+h+'" role="img" aria-label="'+esc(label)+'">'+rows.map((r,i)=>'<text x="0" y="'+(i*40+24)+'" font-size="13">'+esc(r.label)+'</text><rect x="340" y="'+(i*40+7)+'" width="'+(Math.max(0,r[key]??0)*450)+'" height="23" fill="#126b70"/><text x="'+(350+Math.max(0,r[key]??0)*450)+'" y="'+(i*40+24)+'" font-size="13">'+fmt(r[key])+'</text>').join('')+'<text x="340" y="'+(h-2)+'" font-size="12">'+fmt(0)+'</text><text x="790" y="'+(h-2)+'" font-size="12">'+fmt(1)+'</text></svg>';}
'''
def setup(name):
 r=BASE/'samples'/name
 for x in ['code','results','evidence','prepared','dashboard','figures']:(r/x).mkdir(parents=True,exist_ok=True)
 (r/'.gitignore').write_text('prepared/\n__pycache__/\n')
 return r,BASE/'datasets'/name

def save(r,n,d):
 d=d if isinstance(d,pd.DataFrame) else pd.DataFrame(d);d.to_csv(r/'results'/(n+'.csv'),index=False);return d

def mdtable(d):
 d=d.copy()
 for c in d:
  if pd.api.types.is_float_dtype(d[c]):d[c]=d[c].map(lambda x:'—' if pd.isna(x) else f'{x:.3f}')
 d=d.fillna('—').astype(str)
 return '| '+' | '.join(d.columns)+' |\n|'+'|'.join(['---']*len(d.columns))+'|\n'+'\n'.join('| '+' | '.join(row)+' |' for row in d.values)

def manifest(r,paths):
 rows=[]
 for p in paths:
  h=hashlib.sha256()
  with p.open('rb') as f:
   for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
  rows.append(dict(file=str(p.relative_to(BASE)),bytes=p.stat().st_size,sha256=h.hexdigest()))
 return save(r,'source_manifest',rows)

def report(r,text):
 from report_figures import add_report_figures
 text=add_report_figures(r,text)
 (r/'REPORT.md').write_text(text)
 content=markdown.markdown(text,extensions=['tables','fenced_code','toc']).replace('<table>','<div class="scroll"><table>').replace('</table>','</table></div>')
 content=re.sub(r'(<p><img\b[^>]*></p>)',r'<div class="report-figure">\1</div><p class="figure-hint">Scroll sideways to read the chart.</p>',content)
 (r/'report.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(r.name)+' research report</title><style>'+CSS+'</style><main><nav><a href="dashboard/index.html">Dashboard</a><a href="README.md">Reproduce</a></nav>'+content+'</main></html>')

def dashboard(r,title,scope,body,script,tables):
 data={n:pd.read_csv(r/'results'/(n+'.csv')).replace({np.nan:None}).to_dict('records') for n in tables}
 text='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+CSS+'</style><main><p class="muted">'+html.escape(r.name)+' · Local analysis snapshot · 13 October 2026</p><h1>'+html.escape(title)+'</h1><p class="note">'+scope+'</p><nav><a href="../report.html">Read the report</a><a href="../README.md">Reproduce and open</a><a href="../QUALITY_REVIEW.md">Verification and review</a></nav>'+body+'</main><script>const D='+json.dumps(data,allow_nan=False)+';'+JS+script+'</script></html>'
 (r/'dashboard'/'index.html').write_text(text)

def check(rows,name,observed,expected,ok=True,consequence='Numerical gate passes'):
 rows.append(dict(check=name,observed=observed,expected=expected,status='PASS' if ok else 'FAIL',method='Executed code/analyze.py or named companion script',consequence=consequence));assert ok,rows[-1]

def evidence_gap(rows,name,observed,expected,consequence):
 rows.append(dict(check=name,observed=observed,expected=expected,status='NOT VERIFIED',method='Actual source schema and documented coverage review',consequence=consequence))
