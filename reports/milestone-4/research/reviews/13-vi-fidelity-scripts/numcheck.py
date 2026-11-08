"""numcheck.py STEM...: compare the numbers, citations and identifiers of each English unit with its Vietnamese unit
(units aligned by position, as in pairs.py), to catch an English edit the twin has not followed. Decimal commas and
thousands dots of the twin are normalised to the English form; numbers written as words are not compared.
Usage: venv/bin/python numcheck.py 01-01 10-01 10-04 10-06"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pairs import units, root  # noqa: E402


def tokens(s, vi):
    if vi:
        s = re.sub(r"(?<=\d)\.(?=\d{3}\b)", ",", s)          # 11.811 -> 11,811
        s = re.sub(r"(?<=\d),(?=\d{1,2}\b)", ".", s)          # 0,05 -> 0.05 (decimal comma)
        s = re.sub(r"(?<=\d),(?=\d{3}\b)", ",", s)
    nums = re.findall(r"\d[\d,]*(?:\.\d+)?", s)
    ids = re.findall(r"\b(?:AQ\d|C\d\d|D\d|S\d|R\d+|FR\d|[A-G]{3})\b", s)
    return sorted(nums + ids)


for stem in sys.argv[1:]:
    vi = next(root.glob(stem + "*.vi.md")); en = pathlib.Path(str(vi).replace(".vi.md", ".md"))
    U, E = units(vi), units(en)
    print(f"== {vi.name}: units vi={len(U)} en={len(E)}")
    for k, (u, e) in enumerate(zip(U, E)):
        a, b = tokens(e[2], False), tokens(u[2], True)
        if a != b:
            ma = [x for x in a if a.count(x) > b.count(x)]
            mb = [x for x in b if b.count(x) > a.count(x)]
            print(f"  unit {k} (vi line {u[0]}): only EN {sorted(set(ma))}  only VI {sorted(set(mb))}")
