import re,sys,glob,os,collections
d=sys.argv[1]
en_pat=re.compile(r'\b(Sections?|Parts?|Tables?|Figures?|Appendix|Appendices)\s+((?:[IVX]+|\d+(?:\.\d+)*)(?:(?:,\s*|\s*(?:and|to|–|-)\s*|\s*,\s*and\s+)(?:[IVX]+|\d+(?:\.\d+)*))*)')
vi_pat=re.compile(r'(Mục|Phần|Bảng|Hình|Phụ lục)\s+((?:[IVX]+|\d+(?:\.\d+)*)(?:(?:,\s*|\s*(?:và|đến|–|-)\s*)(?:[IVX]+|\d+(?:\.\d+)*))*)')
m={'Section':'Mục','Sections':'Mục','Part':'Phần','Parts':'Phần','Table':'Bảng','Tables':'Bảng','Figure':'Hình','Figures':'Hình','Appendix':'Phụ lục','Appendices':'Phụ lục'}
num=re.compile(r'[IVX]+|\d+(?:\.\d+)*')
for vi in sorted(glob.glob(os.path.join(d,'*.vi.md'))):
    en=vi.replace('.vi.md','.md')
    E=collections.Counter(); V=collections.Counter()
    t=open(en).read()
    t=re.sub(r'\s+',' ',t)
    for k,v in en_pat.findall(t):
        for n in num.findall(v): E[(m[k],n)]+=1
    for k,v in vi_pat.findall(re.sub(r'\s+',' ',open(vi).read())):
        for n in num.findall(v): V[(k,n)]+=1
    if E!=V:
        print(os.path.basename(vi),'EN-only',dict(E-V),'VI-only',dict(V-E))
