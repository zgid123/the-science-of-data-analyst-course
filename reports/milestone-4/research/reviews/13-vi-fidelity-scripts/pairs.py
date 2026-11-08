"""pairs.py DIFF [STEM]: for every unit (paragraph or table row) that the rewrite diff changed, print the current
English unit and the current Vietnamese unit side by side. Changed lines are taken from the '+' lines of the diff
and located in the current twin by their after-hunk line number; units are aligned by position, as in
rewrite-2-2026-11-08-scripts/show.py. Usage:
  venv/bin/python pairs.py ../rewrite-2-2026-11-08-scripts/twins.diff [01-01]"""
import sys, re, pathlib

root = pathlib.Path(__file__).resolve().parents[3] / "report"


def units(path):
    out, buf, start = [], [], None
    lines = path.read_text().split("\n")
    def flush(end):
        nonlocal buf, start
        if buf:
            out.append((start, end, " ".join(x.strip() for x in buf)))
        buf, start = [], None
    prev = 0
    for i, l in enumerate(lines, 1):
        if not l.strip():
            flush(prev); prev = i; continue
        if l.lstrip().startswith("|"):
            flush(prev); out.append((i, i, l.strip())); prev = i; continue
        if re.match(r"^(#|\s*[-*] |\s*\(\d+\) |\s*\d+\. )", l) and buf:
            flush(prev)
        if start is None:
            start = i
        buf.append(l); prev = i
    flush(prev)
    return out


def changed_lines(diff_text):
    res, cur, ln = {}, None, 0
    for l in diff_text.split("\n"):
        if l.startswith("+++ "):
            cur = pathlib.Path(l[4:].split("\t")[0]).name; res[cur] = []
        elif l.startswith("@@"):
            ln = int(re.search(r"\+(\d+)", l).group(1))
        elif cur and l.startswith("+"):
            res[cur].append(ln); ln += 1
        elif cur and l.startswith(" "):
            ln += 1
    return res


def main():
    diff = pathlib.Path(sys.argv[1]).read_text()
    only = sys.argv[2] if len(sys.argv) > 2 else None
    total = 0
    for name, lns in changed_lines(diff).items():
        if only and not name.startswith(only):
            continue
        vi = root / name
        en = root / name.replace(".vi.md", ".md")
        U, E = units(vi), units(en)
        if len(U) != len(E):
            print(f"!! unit count differs {name}: vi={len(U)} en={len(E)}")
        ks = sorted({max(j for j, u in enumerate(U) if u[0] <= ln) for ln in lns})
        for k in ks:
            total += 1
            print(f"== {name} unit {k} (vi line {U[k][0]})")
            print("EN:", E[k][2] if k < len(E) else "<none>")
            print("VI:", U[k][2])
            print()
    print(f"changed units: {total}")


if __name__ == "__main__":
    main()
