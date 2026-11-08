"""Moved to the build-report skill: .agents/skills/build-report/scripts/page_budget.py (optimistic and pessimistic
page estimates per part, layout gaps, table share, --blocks, --budget). This wrapper keeps the commands recorded in
the logs of Milestones 1–3 runnable.

Usage (from the repository root): venv/bin/python reports/milestone-1/code/page_budget.py DOCX [--budget 10]
"""
import runpy
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[3] / ".agents" / "skills" / "build-report" / "scripts" / "page_budget.py"
sys.argv = [str(SCRIPT)] + sys.argv[1:]
runpy.run_path(str(SCRIPT), run_name="__main__")
