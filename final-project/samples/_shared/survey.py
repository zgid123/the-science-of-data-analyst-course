"""Fay-BRR ratio estimates and paired contrasts; no country pooling by default."""
import numpy as np,pandas as pd
def estimate(g,values,weight,reps=None):
 v=np.asarray(values,dtype=float);w=pd.to_numeric(g[weight],errors='coerce').to_numpy();valid=np.isfinite(v)&np.isfinite(w)&(w>0)
 if not valid.any():return dict(n=len(g),valid_n=0,weighted=np.nan,unweighted=np.nan,se=np.nan,lo=np.nan,hi=np.nan,weight_sum=0)
 v=v[valid];w=w[valid];p=np.average(v,weights=w);se=np.nan
 if reps:
  rw=g.loc[valid,reps].apply(pd.to_numeric,errors='coerce').to_numpy();tot=np.nansum(rw,axis=0);rep=np.nansum(rw*v[:,None],axis=0)/tot
  se=np.sqrt(4/len(reps)*np.sum((rep-p)**2)) if np.isfinite(rep).all() else np.nan
 return dict(n=len(g),valid_n=int(valid.sum()),weighted=p,unweighted=v.mean(),se=se,lo=p-1.96*se,hi=p+1.96*se,weight_sum=w.sum())
def coded(series,valid,success):
 x=pd.to_numeric(series,errors='coerce');return np.where(x.isin(valid),x.isin(success).astype(float),np.nan)
