"""Independent scalar-loop weighted and Fay-BRR rate check for the reference domain."""
import sys
from pathlib import Path
import pandas as pd,numpy as np,pyreadstat
from delivery import BASE,save

def verify(name):
 r=BASE/'samples'/name;d=BASE/'datasets'/name;results=[]
 if name=='talis-2024':
  reps=[f'TRWGT{i}' for i in range(1,101)];item='TT4G53C';w='TCHWGT';raw=pd.read_csv(d/'btgintt4.csv',sep=';',usecols=['CNTRY',item,w]+reps);g=raw[(raw.CNTRY=='AUS')&raw[item].isin([1,2,3,4])&(raw[w]>0)];target=pd.read_csv(r/'results/practice_estimates.csv').query('country == "AUS" and level == 2 and item == "TT4G53C"').iloc[0]
 else:
  reps=[f'W_FTCHRWT{i}' for i in range(1,81)];item='TC054Q04NA';w='W_FTCHWT';raw,_=pyreadstat.read_sav(d/'CY08MSP_TCH_QQQ.SAV',usecols=['CNT','TCHTYPE',item,w]+reps,user_missing=True);g=raw[(raw.CNT=='AUS')&(raw.TCHTYPE==1)&raw[item].isin([1,2,3,4])&(raw[w]>0)];target=pd.read_csv(r/'results/practice_estimates.csv').query('country == "AUS" and source == "teacher" and teacher_type == 1 and item == "TC054Q04NA"').iloc[0]
 values=[int(x>=3) for x in g[item]];base=sum(float(ww)*v for ww,v in zip(g[w],values))/sum(g[w]);repvals=[]
 for col in reps:repvals.append(sum(float(ww)*v for ww,v in zip(g[col],values))/sum(g[col]))
 se=(4/len(reps)*sum((x-base)**2 for x in repvals))**.5
 for title,observed,expected in [('Reference weighted rate scalar recomputation',base,target.weighted),('Reference Fay-BRR SE scalar recomputation',se,target.se)]:
  okay=abs(observed-expected)<1e-12;results.append(dict(check=title,source_respondents=len(g),replicates=len(reps),observed=observed,expected=expected,tolerance=1e-12,status='PASS' if okay else 'FAIL',method='Independent Python scalar weighted sums for each replicate'));assert okay
 # Replicate completeness checks cover every local respondent for the reference file, not only the example item.
 bad=int((~np.isfinite(raw[reps].to_numpy())|(raw[reps].to_numpy()<0)).sum());results.append(dict(check='Nonfinite/negative supplied replicate weights',source_respondents=len(raw),replicates=len(reps),observed=bad,expected=0,status='PASS' if bad==0 else 'FAIL',method='All replicate cells in supplied reference-level file'));assert bad==0
 save(r,'independent_checks',results);print(name,results)
if __name__=='__main__':verify(sys.argv[1])
