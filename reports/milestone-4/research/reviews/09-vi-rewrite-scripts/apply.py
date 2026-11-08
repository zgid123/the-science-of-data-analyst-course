"""apply.py EDITFILE: EDITFILE is python defining FILE and PAIRS=[(old,new),...]; each old must occur exactly once."""
import sys, runpy, pathlib
ns = runpy.run_path(sys.argv[1])
root = pathlib.Path("/Users/ptkhanh/Documents/master/milestone-da/reports/milestone-4/report")
p = root / ns["FILE"]
text = p.read_text(encoding="utf-8")
for old, new in ns["PAIRS"]:
    n = text.count(old)
    if n != 1:
        sys.exit(f"ABORT {p.name}: found {n}x: {old[:90]!r}")
    text = text.replace(old, new)
p.write_text(text, encoding="utf-8")
print(f"{p.name}: {len(ns['PAIRS'])} edits applied")
