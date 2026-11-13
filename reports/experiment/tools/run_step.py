"""Run one step of an analysis and keep its console output as a Markdown log.

    python run_step.py <step-name> -- <command ...>
    python run_step.py <step-name> --logs <dir> -- <command ...>
    python run_step.py --new-run [--logs <dir>]            mark the start of a full run in the experiment log

Writes   <logs>/<step-name>.md       start and end (UTC), command, exit status, full console output
Appends  <logs>/experiment-log.md    one row per executed step, in run order

A command that starts with the word `python` runs under the interpreter that runs this script; any other command
runs as written. The command runs in the current directory and its exit status is returned, so a failing step stops a shell
script that uses `set -e`. Every number in a report should come from a step run this way: the log is the
evidence that the number was produced by code, when, and by which command. The experiment log is a record: steps that failed
while the work was being written stay in it. Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
import time
from pathlib import Path


HEADER = ("# Experiment log\n\nOne row per executed step, appended by `run_step.py` in run order. A **new run** row marks the start of "
          "each full run; the rows after the last one are the run that produced the delivered results.\n\n"
          "| Started (UTC) | Step | Command | Exit | Seconds | Log |\n| :---- | :---- | :---- | :---- | :---- | :---- |\n")


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def run_step(step: str, command: list[str], logs: Path = Path("logs")) -> int:
    shown = " ".join(command)
    command = [sys.executable if command[0] == "python" else command[0], *command[1:]]
    start, t0 = now(), time.time()
    lines = []
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as proc:
        for line in proc.stdout:
            sys.stdout.write(line)
            lines.append(line)
        status = proc.wait()
    seconds = time.time() - t0
    logs.mkdir(parents=True, exist_ok=True)
    (logs / f"{step}.md").write_text(
        f"# Log: {step}\n\n| Field | Value |\n| :---- | :---- |\n"
        f"| Started (UTC) | {start} |\n| Finished (UTC) | {now()} |\n| Duration | {seconds:.1f} s |\n"
        f"| Command | `{shown}` |\n| Exit status | {status} |\n\n## Console output\n\n```text\n{''.join(lines)}```\n"
    )
    index = logs / "experiment-log.md"
    if not index.exists():
        index.write_text(HEADER)
    with open(index, "a") as fh:
        fh.write(f"| {start} | {step} | `{shown}` | {status} | {seconds:.1f} | [{step}.md]({step}.md) |\n")
    return status


def new_run(logs: Path = Path("logs")) -> None:
    logs.mkdir(parents=True, exist_ok=True)
    index = logs / "experiment-log.md"
    if not index.exists():
        index.write_text(HEADER)
    with open(index, "a") as fh:
        fh.write(f"| {now()} | **new run** | – | – | – | – |\n")


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if "--new-run" in argv:
        new_run(Path(argv[argv.index("--logs") + 1]) if "--logs" in argv else Path("logs"))
        return 0
    if "--" not in argv:
        print(__doc__)
        return 2
    cut = argv.index("--")
    parser = argparse.ArgumentParser(description="Run one analysis step and log it.")
    parser.add_argument("step")
    parser.add_argument("--logs", default="logs", type=Path)
    args = parser.parse_args(argv[:cut])
    command = argv[cut + 1:]
    if not command:
        print(__doc__)
        return 2
    return run_step(args.step, command, args.logs)


if __name__ == "__main__":
    sys.exit(main())
