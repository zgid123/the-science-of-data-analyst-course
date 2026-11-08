"""apply.py EDITFILE...: each EDITFILE is python defining FILE and PAIRS=[(old,new),...];
each old must occur exactly once in the twin, or the run aborts before writing."""
import sys, runpy, pathlib
root = pathlib.Path(__file__).resolve().parents[3] / "report"
for ef in sys.argv[1:]:
    ns = runpy.run_path(ef)
    p = root / ns["FILE"]
    text = p.read_text(encoding="utf-8")
    for old, new in ns["PAIRS"]:
        n = text.count(old)
        if n != 1:
            sys.exit(f"ABORT {p.name}: found {n}x: {old[:90]!r}")
        text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    print(f"{p.name}: {len(ns['PAIRS'])} edits applied")
