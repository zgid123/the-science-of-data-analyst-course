import sys, re, difflib, pathlib
rep = pathlib.Path(sys.argv[1]); diff = pathlib.Path(sys.argv[2]).read_text()
def units(path):
    out=[]; buf=[]; start=None
    lines=path.read_text().split('\n')
    def flush():
        nonlocal buf,start
        if buf: out.append((start,' '.join(x.strip() for x in buf)))
        buf=[];start=None
    for i,l in enumerate(lines,1):
        if not l.strip(): flush(); continue
        if l.lstrip().startswith('|'):
            flush(); out.append((i,l.strip())); continue
        if re.match(r'^(#|\s*[-*] |\s*\(\d+\) |\s*\d+\. )',l) and buf: flush()
        if start is None: start=i
        buf.append(l)
    flush(); return out
files={}; cur=None
for l in diff.split('\n'):
    if l.startswith('+++ after/'): cur=l[10:].strip(); files[cur]=[]
    elif cur and l.startswith('+') and not l.startswith('+++') and l[1:].strip(): files[cur].append(l[1:].strip())
n=0
for vi,plus in files.items():
    en=vi.replace('.vi.md','.md')
    U=units(rep/vi); E=units(rep/en)
    print(f'\n######## {vi}  units vi={len(U)} en={len(E)}')
    seen=set()
    for p in plus:
        best=max(range(len(U)),key=lambda k: difflib.SequenceMatcher(None,p[:300],U[k][1][:300]).ratio() if p[:40] in U[k][1] or True else 0)
        if best in seen: continue
        seen.add(best); n+=1
        r=difflib.SequenceMatcher(None,p,U[best][1]).ratio()
        print(f'\n--- [{n}] VI L{U[best][0]} (unit {best}, match {r:.2f})')
        print('EN:', E[best][1] if best<len(E) else '<<none>>')
        print('VI:', U[best][1])
print('\nTOTAL',n)
