"""wdiff.py DIFF [STEM]: word-level view of each -/+ line pair in the rewrite diff, so the reviewer sees exactly what
the rewrite changed inside a long paragraph or table row: [-removed-] {+added+}. Usage:
  venv/bin/python wdiff.py ../rewrite-2-2026-11-08-scripts/twins.diff [04-02]"""
import sys, difflib, pathlib

text = pathlib.Path(sys.argv[1]).read_text().split("\n")
only = sys.argv[2] if len(sys.argv) > 2 else None
cur, minus, plus = None, [], []


def flush():
    global minus, plus
    if cur and (not only or cur.startswith(only)) and (minus or plus):
        a = " ".join(minus).split()
        b = " ".join(plus).split()
        out = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op == "equal":
                seg = a[i1:i2]
                out.append(" ".join(seg) if len(seg) < 12 else " ".join(seg[:5]) + " … " + " ".join(seg[-5:]))
            else:
                if i2 > i1:
                    out.append("[-" + " ".join(a[i1:i2]) + "-]")
                if j2 > j1:
                    out.append("{+" + " ".join(b[j1:j2]) + "+}")
        print(f"== {cur}\n" + " ".join(out) + "\n")
    minus, plus = [], []


for l in text:
    if l.startswith("+++ "):
        flush(); cur = pathlib.Path(l[4:].split("\t")[0]).name
    elif l.startswith("--- ") or l.startswith("diff "):
        flush()
    elif l.startswith("-"):
        if plus:
            flush()
        minus.append(l[1:])
    elif l.startswith("+"):
        plus.append(l[1:])
    else:
        flush()
flush()
