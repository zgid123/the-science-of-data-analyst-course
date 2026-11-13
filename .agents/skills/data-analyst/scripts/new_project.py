"""Create the working folder of a substantial analysis, with the run tools wired in.

    python new_project.py <output-dir> [--title "Early warning for course completion"]

Creates   NOTES.md        brief, inherited project record, ten-stage lifecycle record, decisions, check ledger
          run_all.sh      every step in order, each run through tools/run_step.py
          tools/          copies of this skill's scripts, so the folder runs on its own when it is handed over
          requirements.txt   packages for the statistics, chart and profiling scripts (tools/setup_env.py installs them)
          code/ results/ figures/ logs/ data/
It never overwrites an existing NOTES.md or run_all.sh. Standard library only.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
TOOLS = ["run_step.py", "data_manifest.py", "holdout_guard.py", "report_tables.py", "check_report.py", "compare_results.py",
         "stats_helpers.py", "chart_style.py", "profile_data.py", "setup_env.py"]


def create(out: Path, title: str) -> list[str]:
    made = []
    for folder in ("code", "results", "figures", "logs", "data", "tools"):
        (out / folder).mkdir(parents=True, exist_ok=True)
    for name in TOOLS:
        shutil.copyfile(SKILL / "scripts" / name, out / "tools" / name)
    shutil.copyfile(SKILL / "requirements.txt", out / "requirements.txt")
    shutil.copyfile(SKILL / "assets" / "reviewer-brief.md", out / "tools" / "reviewer-brief.md")
    if not (out / "code" / "_tools.py").exists():
        (out / "code" / "_tools.py").write_text('"""Put ../tools on the import path: start every script in code/ with `import _tools`."""\n\nimport sys\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nsys.path.insert(0, str(ROOT / "tools"))\n')
    if not (out / ".gitignore").exists():
        (out / ".gitignore").write_text(".venv/\n__pycache__/\n")
    for target, template in (("NOTES.md", "notes-template.md"), ("run_all.sh", "run_all-template.sh")):
        if (out / target).exists():
            continue
        (out / target).write_text((SKILL / "assets" / template).read_text().replace("{title}", title))
        made.append(target)
    return made


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Create the working folder of an analysis.")
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", default="analysis")
    args = parser.parse_args(argv)
    made = create(args.output, args.title)
    print(f"{args.output}: folders and tools ready; written: {', '.join(made) or 'nothing new (files kept)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
