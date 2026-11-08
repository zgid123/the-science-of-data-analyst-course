#!/usr/bin/env python3
r"""Working-file layout of a task's research/ folder: one place and one name pattern for every kind of file.

Usage:
    layout.py check      --base TASK              # ERROR on a file outside the layout or a stale index
    layout.py index      --base TASK [--write]    # print (or write into research/README.md) the file index
    layout.py new-review --base TASK --kind KIND [--scope S] [--same] [--title TEXT]
                                                  # create the next review file and print its path
    layout.py move       --base TASK --map CSV [--apply] [--commit REV]
                                                  # move or retire files by a mapping table, then verify

Layout of TASK/research/ (reference.md section 2.1):
    core trail      README.md, AGENT_BRIEF.md, search-log.md, sources.md, partN-claims.md, partN-synthesis.md,
                    spot-check.md, style-review.md, .trail.lock, templates/, sources/
    baseline/       frozen inputs from earlier milestones: mN-baseline*.md
    notes           task notes, each declared with its purpose in plan.toml [layout] notes = [{path, purpose}]
    reviews/        one numbered round per review, in the order they ran:
                      NN-ai-<role>-prompt.md | -output.md | -decisions.md     (AI critic roles of the brief)
                      NN-<lang>-<step>[-<scope>].md, step in native-review, consistency, reader-test, rewrite,
                      fidelity, reread                                          (translation review, e.g. vi)
                      NN-slides-<review|rewrite>[-<scope>].md                   (deck review)
                      NN-<same name>-scripts/                                   (the round's scripts and logs)
    revisions/      NN-<label>.md and NN-<label>-scripts/ (revision records, in order), snapshots.md (each saved
                    state of the report as a git commit and path, never a copied folder), layout-moves.csv

check   ERROR  a file or folder under research/ that matches no rule above; a declared note path that is missing;
               research/README.md whose generated index (between the layout markers) differs from `index`.
move    CSV columns: old,new  (paths relative to research/; new = "snapshot" retires a saved copy of the report,
        allowed only when every file under it is tracked and identical to --commit). Tracked files move with
        git mv, untracked and ignored files with a plain rename; each file's sha256 is compared before and after.
        Then `research/<old>` is rewritten to `research/<new>` in the task's working files (PROGRESS.md,
        EXECUTION_PLAN.md, README.md, plan.toml, code/, research/ notes and revision records); records keep their
        wording: logs/, report/, package/, build/, baseline/, review rounds (prompts, outputs, scripts that ran) and
        revision scripts. layout-moves.csv maps every old path to its new one. --refs-only repeats only that rewrite.
Exit code 1 on any ERROR.
"""

import argparse
import csv
import hashlib
import os
import re
import subprocess
import sys
from pathlib import Path

from common import ROOT, base_dir, load_plan

CORE_FILES = {"README.md", "AGENT_BRIEF.md", "search-log.md", "sources.md", "spot-check.md", "style-review.md",
              ".trail.lock"}
CORE_FILE_RE = re.compile(r"part\d+-(claims|synthesis)\.md$")
CORE_DIRS = {"templates", "sources", "__pycache__"}
BASELINE_RE = re.compile(r"m\d+-baseline[a-z0-9-]*\.md$")
STEPS = "native-review|consistency|reader-test|rewrite|fidelity|reread"
REVIEW_STEM = rf"\d{{2}}-(ai-[a-z0-9]+(?:-[a-z0-9]+)*-(?:prompt|output|decisions)|[a-z]{{2}}-(?:{STEPS})(?:-[a-z0-9]+)*" \
              rf"|slides-(?:review|rewrite)(?:-[a-z0-9]+)*)"
REVIEW_FILE_RE = re.compile(REVIEW_STEM + r"\.md$")
REVIEW_DIR_RE = re.compile(r"\d{2}-[a-z0-9-]+-scripts$")
REVISION_FILE_RE = re.compile(r"(\d{2}-[a-z0-9-]+\.md|snapshots\.md|layout-moves\.csv)$")
REVISION_DIR_RE = re.compile(r"\d{2}-[a-z0-9-]+-scripts$")
START, END = "<!-- layout:index:start -->", "<!-- layout:index:end -->"
KIND_WORDS = {"native-review": "native review", "consistency": "consistency read", "reader-test": "reader test",
              "rewrite": "rewrite", "fidelity": "fidelity review", "reread": "reread of fixed passages"}


def notes(base: Path) -> list[dict]:
    return load_plan(base).get("layout", {}).get("notes", [])


def first_line(p: Path) -> str:
    try:
        for line in p.read_text(encoding="utf-8").splitlines():
            s = line.strip().lstrip("#").strip()
            if s:
                return re.sub(r"\s+", " ", s)[:140].replace("|", "\\|")
    except (UnicodeDecodeError, OSError):
        pass
    return ""


def check(base: Path) -> list[str]:
    rd = base / "research"
    errors = []
    declared = {n["path"].rstrip("/"): n for n in notes(base)}
    for n in declared:
        if not (rd / n).exists():
            errors.append(f"note declared in plan.toml [layout] is missing: research/{n}")
    for entry in sorted(rd.iterdir()):
        name = entry.name
        if name in declared:
            continue
        if entry.is_file() and (name in CORE_FILES or CORE_FILE_RE.match(name)):
            continue
        if entry.is_dir() and name in CORE_DIRS:
            continue
        if entry.is_dir() and name == "baseline":
            errors += [f"research/baseline/{f.name}: not a baseline name (mN-baseline*.md)"
                       for f in sorted(entry.iterdir()) if not (f.is_file() and BASELINE_RE.match(f.name))]
            continue
        if entry.is_dir() and name in ("reviews", "revisions"):
            frx, drx = (REVIEW_FILE_RE, REVIEW_DIR_RE) if name == "reviews" else (REVISION_FILE_RE, REVISION_DIR_RE)
            for f in sorted(entry.iterdir()):
                ok = (f.is_file() and frx.match(f.name)) or (f.is_dir() and drx.match(f.name))
                if not ok:
                    errors.append(f"research/{name}/{f.name}: name outside the layout (see layout.py --help); "
                                  f"create review files with `layout.py new-review`")
            continue
        errors.append(f"research/{name}: not part of the layout; move it to reviews/ or revisions/, or declare it "
                      f"as a note in plan.toml [layout] notes = [{{path, purpose}}]")
    readme = rd / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if START not in text:
            errors.append("research/README.md: no generated index; run `layout.py index --write`")
        elif text.split(START)[1].split(END)[0].strip() != index_text(base).strip():
            errors.append("research/README.md: the file index is out of date; run `layout.py index --write`")
    return errors


def rows_for(folder: Path, rel: str) -> list[str]:
    out = []
    for f in sorted(folder.iterdir()):
        if f.name == "__pycache__":
            continue
        if f.is_dir():
            n = sum(1 for x in f.rglob("*") if x.is_file() and "__pycache__" not in x.parts)
            out.append(f"| `{rel}{f.name}/` | scripts and logs of round {f.name[:2]} ({n} files) |")
        else:
            out.append(f"| `{rel}{f.name}` | {first_line(f)} |")
    return out


def index_text(base: Path) -> str:
    rd = base / "research"
    lines = ["Generated by `layout.py index --write` from the files on disk; `layout.py check` fails when it is "
             "out of date.", ""]
    if notes(base):
        lines += ["**Task notes** (declared in `plan.toml` [layout]):", "", "| Path | Purpose |", "| :---- | :---- |"]
        lines += [f"| `{n['path']}` | {n['purpose']} |" for n in notes(base)]
        lines.append("")
    for name, title in (("baseline", "**Baseline**: frozen inputs from earlier milestones"),
                        ("reviews", "**Reviews**: one numbered round per review, in the order they ran"),
                        ("revisions", "**Revisions**: revision records in order, saved report states, layout moves")):
        if (rd / name).is_dir():
            lines += [title, "", "| File | First line |", "| :---- | :---- |"] + rows_for(rd / name, f"{name}/") + [""]
    return "\n".join(lines).rstrip() + "\n"


def write_index(base: Path) -> None:
    readme = base / "research" / "README.md"
    text = readme.read_text(encoding="utf-8") if readme.exists() else "# Research Trail\n"
    block = f"{START}\n{index_text(base)}{END}"
    if START in text:
        text = text.split(START)[0] + block + text.split(END, 1)[1]
    else:
        text = text.rstrip() + "\n\n## Working files\n\n" + block + "\n"
    readme.write_text(text, encoding="utf-8")


def new_review(base: Path, kind: str, scope: str | None, same: bool, title: str | None) -> Path:
    folder = base / "research" / "reviews"
    folder.mkdir(parents=True, exist_ok=True)
    nums = [int(f.name[:2]) for f in folder.iterdir() if f.name[:2].isdigit()]
    nn = (max(nums) if nums and same else max(nums, default=0) + 1)
    name = f"{nn:02d}-{kind}" + (f"-{scope}" if scope else "") + ".md"
    if not REVIEW_FILE_RE.match(name):
        sys.exit(f"ERROR {name}: kind must be ai-<role>-prompt|output|decisions, <lang>-<{STEPS}> or "
                 f"slides-review|rewrite; scope in lower case with hyphens")
    path = folder / name
    if path.exists():
        sys.exit(f"ERROR {path} exists")
    path.write_text(f"# {title or name[3:-3]}\n", encoding="utf-8")
    return path


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git(*args: str, check: bool = True) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=check).stdout


def tracked(p: Path) -> bool:
    return bool(git("ls-files", "--error-unmatch", str(p.relative_to(ROOT)), check=False).strip())


WORKING_GLOBS = ["PROGRESS.md", "EXECUTION_PLAN.md", "README.md", "plan.toml", "code/**/*.py", "code/**/*.sh",
                 "research/**/*.md", "research/**/*.py", "research/**/*.sh", "research/**/*.json"]


def working_files(base: Path) -> list[Path]:
    seen = set()
    for g in WORKING_GLOBS:
        for p in base.glob(g):
            rel = p.relative_to(base).parts
            record = rel[:2] == ("research", "reviews") or (rel[:2] == ("research", "revisions") and len(rel) > 3)
            if p.is_file() and not record and not ({"baseline", "sources", "__pycache__"} & set(rel)) and p not in seen:
                seen.add(p)
    return sorted(seen)


def rewrite_refs(base: Path, rows: list[dict]) -> int:
    """Rewrite research/<old> to research/<new> in the task's working files, longest old path first."""
    pairs = sorted(((f"research/{r['old']}".rstrip("/"), f"research/{r['new']}".rstrip("/"))
                    for r in rows if r["new"] != "snapshot"), key=lambda x: -len(x[0]))
    if not pairs:
        return 0
    pat = re.compile("|".join(re.escape(o) + r"(?![A-Za-z0-9_-]|\.[A-Za-z0-9])" for o, _ in pairs))
    lookup = dict(pairs)
    total = 0
    for p in working_files(base):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new_text, n = pat.subn(lambda m: lookup[m.group(0)], text)
        if n:
            p.write_text(new_text, encoding="utf-8")
            total += n
            print(f"  references: {p.relative_to(base)}: {n}")
    print(f"references rewritten: {total}")
    return total


def move(base: Path, mapfile: Path, apply: bool, commit: str, refs_only: bool = False) -> int:
    rd = base / "research"
    rows = list(csv.DictReader(mapfile.open(encoding="utf-8")))
    if refs_only:
        rewrite_refs(base, rows)
        return 0
    errors, moved, retired = [], [], []
    news = [r["new"] for r in rows if r["new"] != "snapshot"]
    if len(news) != len(set(news)):
        errors.append("two rows share one new path")
    for r in rows:
        old = rd / r["old"]
        if not old.exists():
            errors.append(f"missing: research/{r['old']}")
            continue
        files = [old] if old.is_file() else sorted(x for x in old.rglob("*") if x.is_file())
        if r["new"] == "snapshot":
            for f in files:
                rel = f.relative_to(ROOT).as_posix()
                blob = git("rev-parse", "-q", "--verify", f"{commit}:{rel}", check=False).strip()
                if blob != git("hash-object", str(f)).strip():
                    errors.append(f"snapshot file not identical in {commit}: {rel}")
            retired.append((r["old"], len(files)))
            continue
        new = rd / r["new"]
        if new.exists():
            errors.append(f"target exists: research/{r['new']}")
        for f in files:
            moved.append((f, new if old.is_file() else new / f.relative_to(old)))
    if errors:
        print("\n".join("ERROR " + e for e in errors))
        return 1
    print(f"plan: {len(moved)} files to move, {len(retired)} saved copies to retire "
          f"({sum(n for _, n in retired)} files, kept in git at {commit})")
    if not apply:
        for a, b in moved:
            print(f"  {a.relative_to(rd)} -> {b.relative_to(rd)}")
        return 0
    before = {b: sha(a) for a, b in moved}
    for a, b in moved:
        b.parent.mkdir(parents=True, exist_ok=True)
        if tracked(a):
            git("mv", str(a.relative_to(ROOT)), str(b.relative_to(ROOT)))
        else:
            os.rename(a, b)
    for old, _ in retired:
        git("rm", "-r", "-q", str((rd / old).relative_to(ROOT)))
    for r in rows:                                   # drop folders left empty (ignored caches included)
        old = rd / r["old"]
        if old.is_dir():
            for d in sorted((x for x in old.rglob("*") if x.is_dir()), reverse=True) + [old]:
                for c in d.glob("*.pyc"):
                    c.unlink()
                if d.exists() and not any(d.iterdir()):
                    d.rmdir()
    for d in sorted((x for x in rd.rglob("*") if x.is_dir()), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()
    bad = [b for b, h in before.items() if not b.exists() or sha(b) != h]
    print(f"verify: {len(before) - len(bad)} of {len(before)} moved files identical after the move")
    for b in bad:
        print(f"ERROR changed or missing after move: {b}")
    rewrite_refs(base, rows)
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["check", "index", "new-review", "move"])
    ap.add_argument("--base", required=True)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--kind")
    ap.add_argument("--scope")
    ap.add_argument("--same", action="store_true", help="new-review: join the latest round (parallel groups)")
    ap.add_argument("--title")
    ap.add_argument("--map")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--commit", default="HEAD")
    ap.add_argument("--refs-only", action="store_true", help="move: only rewrite references (after a move)")
    a = ap.parse_args()
    base = base_dir(a.base)
    if a.cmd == "check":
        errors = check(base)
        print("\n".join("ERROR " + e for e in errors) or f"PASS layout: {base.relative_to(ROOT)}/research")
        return 1 if errors else 0
    if a.cmd == "index":
        if a.write:
            write_index(base)
            print(f"wrote index into {(base / 'research' / 'README.md').relative_to(ROOT)}")
        else:
            print(index_text(base))
        return 0
    if a.cmd == "new-review":
        if not a.kind:
            sys.exit("ERROR --kind is required")
        print(new_review(base, a.kind, a.scope, a.same, a.title).relative_to(ROOT))
        return 0
    if not a.map:
        sys.exit("ERROR --map is required")
    return move(base, Path(a.map), a.apply, a.commit, a.refs_only)


if __name__ == "__main__":
    sys.exit(main())
