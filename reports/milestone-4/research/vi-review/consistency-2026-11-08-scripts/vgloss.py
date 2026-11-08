import re,glob,os,sys,collections
d=sys.argv[1]
files=[f for f in sorted(glob.glob(os.path.join(d,'*.vi.md'))) if not os.path.basename(f).startswith(('00-1','00-2','09-'))]
occ=collections.defaultdict(list)
for f in files:
    for i,l in enumerate(open(f),1):
        if l.startswith('>'): continue
        for m in re.finditer(r'(\S+(?: \S+){0,3}) \(([^()]{6,120})\)',l):
            g=m.group(2)
            if re.search(r'Mục|Bảng|Hình|Phụ lục|Phần|^C\d|\d{4}|^\[',g): continue
            if re.fullmatch(r'[A-Za-z][A-Za-z \-/–’\']+',g): continue
            occ[g].append((os.path.basename(f)[:5],i,m.group(1)))
for g,v in occ.items():
    if len(v)>1: print(repr(g),v)
