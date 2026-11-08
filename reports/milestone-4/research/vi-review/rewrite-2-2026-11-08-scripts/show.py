"""show.py STEM LINE...: print the English and Vietnamese units (paragraph or table row) holding each Vietnamese line.
Units are aligned by position, as in fidelity-2026-11-08-scripts/pairs.py."""
import sys, re, pathlib
root = pathlib.Path(__file__).resolve().parents[3] / "report"
def units(path):
    out = []; buf = []; start = None
    def flush():
        nonlocal buf, start
        if buf: out.append((start, i_prev, " ".join(x.strip() for x in buf)))
        buf = []; start = None
    i_prev = 0
    for i, l in enumerate(path.read_text().split("\n"), 1):
        if not l.strip(): flush(); i_prev = i; continue
        if l.lstrip().startswith("|"):
            flush(); out.append((i, i, l.strip())); i_prev = i; continue
        if re.match(r"^(#|\s*[-*] |\s*\(\d+\) |\s*\d+\. )", l) and buf: flush()
        if start is None: start = i
        buf.append(l); i_prev = i
    flush(); return out
stem = sys.argv[1]
vi = next(root.glob(stem + "*.vi.md")); en = pathlib.Path(str(vi).replace(".vi.md", ".md"))
U = units(vi); E = units(en)
print(f"units vi={len(U)} en={len(E)}")
for a in sys.argv[2:]:
    ln = int(a)
    k = max(j for j, u in enumerate(U) if u[0] <= ln)
    print(f"== {vi.name}:{a} (unit {k})\nEN: {E[k][2] if k < len(E) else '<none>'}\nVI: {U[k][2]}\n")
