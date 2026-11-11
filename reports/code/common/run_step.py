"""Run one step of the prototype and write its console output as a Markdown log.

    python common/run_step.py <aq-folder> <step-name> -- <command ...>

Writes  <aq-folder>/logs/<step-name>.md   UTC start and end, command, git commit, exit status, full output
appends logs/experiment-log.md            one row per run, in the order the steps were run

The command runs from the folder `reports/code`, with the repository's shared interpreter when it starts
with `python`.
"""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    args = sys.argv[1:]
    if "--" not in args or len(args) < 4:
        print(__doc__)
        return 2
    cut = args.index("--")
    folder, step = args[0], args[1]
    cmd = args[cut + 1:]
    shown = " ".join(cmd)
    if cmd[0] == "python":
        cmd[0] = sys.executable
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    start, t0 = now(), time.time()
    proc = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines = []
    for line in proc.stdout:
        sys.stdout.write(line)
        lines.append(line)
    status = proc.wait()
    secs = time.time() - t0
    log = (ROOT / "logs" if folder == "logs" else ROOT / folder / "logs") / f"{step}.md"     # top-level steps log to logs/
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(
        f"# Log: {folder} / {step}\n\n"
        f"| Field | Value |\n| :---- | :---- |\n"
        f"| Started (UTC) | {start} |\n| Finished (UTC) | {now()} |\n| Duration | {secs:.1f} s |\n"
        f"| Command | `{shown}` (run from `reports/code`) |\n| Git commit | `{commit}` (working tree may hold uncommitted files) |\n"
        f"| Exit status | {status} |\n\n"
        f"## Console output\n\n{''.join(lines)}\n"
    )
    exp = ROOT / "logs" / "experiment-log.md"
    exp.parent.mkdir(parents=True, exist_ok=True)
    if not exp.exists():
        exp.write_text(
            "# Experiment log\n\nOne row per executed step, appended by `common/run_step.py` in run order. "
            "Each row links to the step's full console log.\n\n"
            "| Started (UTC) | Folder | Step | Command | Exit | Seconds | Log |\n"
            "| :---- | :---- | :---- | :---- | :---- | :---- | :---- |\n"
        )
    link = f"{step}.md" if folder == "logs" else f"../{folder}/logs/{step}.md"
    with open(exp, "a") as fh:
        fh.write(f"| {start} | {folder} | {step} | `{shown}` | {status} | {secs:.1f} | [{step}.md]({link}) |\n")
    return status


if __name__ == "__main__":
    sys.exit(main())
