"""Check that people's names are spelled exactly as listed in tasks.toml, in the report and its slide deck.

Usage: python .claude/skills/build-report/scripts/check_names.py --task TASK

A task lists the names that must appear character for character (lecturers, supervisors, authors) without titles:

    [taskN]
    people = ["Phạm Thị Bạch Huệ", "Nguyễn Trần Minh Thư"]
    people_files = ["slides_taskN_vi.py"]        # optional: further files to scan

The check reads every section file of the report (all languages), every script in hooks.extras and the files in
people_files, and reports each run of words that resembles a listed name closely (a similarity of 0.85 or more)
without matching it, for example "Phạm Thị Bích Huệ" for "Phạm Thị Bạch Huệ". A wrong name on a title page or title
slide is a visible error that the other checks cannot see. Exit code 1 when a near-miss is found.
"""

import argparse
import difflib
import re
import sys
import tomllib
from pathlib import Path

from common import ROOT, shown

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def near_misses(text, name, threshold=0.85):
    """Runs of as many words as `name` that resemble it at `threshold` or more without being equal to it."""
    target = name.split()
    n = len(target)
    words = [(m.group(0), m.start()) for m in WORD.finditer(text)]
    found = []
    for i in range(len(words) - n + 1):
        cand = " ".join(w for w, _ in words[i:i + n])
        if cand == name:
            continue
        if cand[0].lower() != name[0].lower():
            continue                                    # a different person almost always starts differently
        ratio = difflib.SequenceMatcher(None, cand.lower(), name.lower()).ratio()
        if ratio >= threshold:
            line = text.count("\n", 0, words[i][1]) + 1
            found.append((line, cand, ratio))
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", required=True)
    ap.add_argument("--config", default=str(ROOT / "tasks.toml"))
    args = ap.parse_args()
    task = tomllib.loads(Path(args.config).read_text(encoding="utf-8")).get(args.task, {})
    people = task.get("people", [])
    files = sorted((ROOT / task.get("report", "")).glob("*.md")) if task.get("report") else []
    files += [ROOT / f for f in task.get("hooks", {}).get("extras", []) if (ROOT / f).exists()]
    files += [ROOT / f for f in task.get("people_files", []) if (ROOT / f).exists()]
    errors = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        for name in people:
            for line, cand, ratio in near_misses(text, name):
                errors += 1
                print(f"ERROR {shown(path)}:{line}: '{cand}' looks like '{name}' ({ratio:.2f}); "
                      f"copy the name from tasks.toml")
    print(f"Checked {len(files)} files for {len(people)} names: {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
