"""Read and update the progress ledger (PROGRESS.md), so a session resumes from files, not from memory.

Usage:
    progress.py --base TASK status              current task, counts per status, blocked tasks, next task
    progress.py --base TASK next                the first task that is not done, with its card from EXECUTION_PLAN.md
    progress.py --base TASK card T05            print one task card (table row or **T05:** block)
    progress.py --base TASK prompt T05          the filled research-subagent prompt for task T05 (card, handoff,
                                                outline lines, ID block, claims and synthesis files, commands)
    progress.py --base TASK add T45 "Title"     append a task row (status todo) after the last task
    progress.py --base TASK set T05 in-progress set a status (todo, in-progress, blocked, done, skipped)
    progress.py --base TASK set T05 done --outputs "…" --verified "…" --note "…"   close a task with its handoff

The ledger table has the columns ID | Task | Status | Outputs | Verified by | Handoff note; "Current task:" on
line 3 is kept in step. Statuses are written with the date, for example "done (2026-10-03)".
"""

import argparse
import re
import sys
from datetime import date

from common import ROOT, SKILL, TEMPLATES, base_dir, load_plan, split_cells

STATUSES = ["todo", "in-progress", "blocked", "done", "skipped"]


def ledger(base):
    path = base / "PROGRESS.md"
    return path, path.read_text(encoding="utf-8").splitlines()


def rows(lines):
    for i, line in enumerate(lines):
        if re.match(r"^\| T\d{2,3} \|", line):
            yield i, split_cells(line)


def card(base, tid):
    text = (base / "EXECUTION_PLAN.md").read_text(encoding="utf-8")
    m = re.search(rf"^\*\*{tid}:.*?(?=^\*\*T\d{{2,3}}:|^#{{2,3}} |\Z)", text, re.M | re.S)
    if m:
        return m.group(0).strip()
    row = next((ln for ln in text.splitlines() if re.match(rf"^\| {tid} \|", ln)), None)
    return row or f"(no card for {tid} in EXECUTION_PLAN.md)"


def prompt(base, tid, table):
    """Fill templates/RESEARCH_TASK_PROMPT.md for one research task from the plan, ledger and outline."""
    plan = load_plan(base)
    task = next((t for t in plan.get("tasks", []) if t["id"] == tid), {"title": ""})
    m = re.search(r"(\d+)(?:\.(\d+))?", task["title"])
    part = int(m.group(1)) if m else 0
    number = m.group(0) if m else ""
    files = [f for f in plan.get("files", []) if number and re.match(rf"^#+ {re.escape(number)}[.\s]", f.get("heading", ""))
             or (number and "." in number and re.match(rf"^#+ {re.escape(number)}\.\d", f.get("heading", "")))]
    outline = plan.get("plan", {}).get("outline", "")
    lines = "see the card"
    sec = next((f.get("outline_section") for f in files if f.get("outline_section")), "")
    if sec and outline:
        sys.path.insert(0, str(SKILL / "scripts"))
        import outline as ol                                              # noqa: E402
        text = (ROOT / outline).read_text(encoding="utf-8").splitlines()
        hit = next((s for s in ol.sections(text) if s["number"] == sec), None)
        lines = f"{hit['start']},{hit['end']}" if hit else lines
    done = [c for _, c in table if c[2].startswith("done")]
    values = dict(task_id=tid, task=plan.get("plan", {}).get("task", base.name), root=ROOT, card=card(base, tid),
                  handoff=(f"{done[-1][0]}: {done[-1][5]}" if done else "none (first task)"), lines=lines, outline=outline,
                  id_block=f"S{part}00–S{part}99 (next free number)" if part else "see the brief", part=part or "N",
                  files=", ".join(f["name"] for f in files) or "the files named in the card",
                  skill=SKILL.relative_to(ROOT).as_posix())
    text = (TEMPLATES / "RESEARCH_TASK_PROMPT.md").read_text(encoding="utf-8")
    for k, v in values.items():
        text = text.replace("{{" + k + "}}", str(v))
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True)
    ap.add_argument("command", choices=["status", "next", "card", "set", "prompt", "add"])
    ap.add_argument("task", nargs="?")
    ap.add_argument("status", nargs="?", help="set: a status; add: the task title")
    ap.add_argument("--outputs")
    ap.add_argument("--verified")
    ap.add_argument("--note")
    args = ap.parse_args()
    base = base_dir(args.base)
    path, lines = ledger(base)
    table = list(rows(lines))
    state = lambda c: c[2].split(" ")[0]                                       # noqa: E731
    todo = [c for _, c in table if state(c) not in ("done", "skipped")]

    if args.command == "status":
        counts = {s: sum(state(c) == s for _, c in table) for s in STATUSES}
        print(lines[2] if len(lines) > 2 else "")
        print("  ".join(f"{s}: {n}" for s, n in counts.items() if n))
        for c in (c for _, c in table if state(c) == "blocked"):
            print(f"blocked: {c[0]} {c[1]} – {c[5][:120]}")
        print(f"next: {todo[0][0]} {todo[0][1]}" if todo else "next: none, every task is done")
        return 0
    if args.command == "next":
        if not todo:
            print("every task is done")
            return 0
        print(f"{todo[0][0]} {todo[0][1]} [{todo[0][2]}]\n")
        print(card(base, todo[0][0]))
        prev = [c for _, c in table if state(c) == "done"]
        if prev:
            print(f"\nhandoff from {prev[-1][0]}: {prev[-1][5]}")
        return 0
    if args.command == "card":
        print(card(base, args.task))
        return 0
    if args.command == "prompt":
        print(prompt(base, args.task, table))
        return 0

    if args.command == "add":
        if any(c[0] == args.task for _, c in table):
            sys.exit(f"{args.task} is already in the ledger")
        last = table[-1][0]
        lines.insert(last + 1, f"| {args.task} | {(args.status or '').replace('|', '/')} | todo |  |  |  |")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{args.task} added")
        return 0
    if args.status not in STATUSES:
        sys.exit(f"status must be one of {', '.join(STATUSES)}")
    idx = next((i for i, c in table if c[0] == args.task), None)
    if idx is None or not args.status:
        sys.exit(f"usage: set TASK STATUS (task {args.task} not in the ledger?)")
    cells = dict(table)[idx]
    cells[2] = args.status if args.status in ("todo", "in-progress") else f"{args.status} ({date.today()})"
    for col, val in ((3, args.outputs), (4, args.verified), (5, args.note)):
        if val:
            cells[col] = val.replace("|", "/")
    lines[idx] = "| " + " | ".join(cells) + " |"
    if len(lines) > 2 and lines[2].startswith("Current task:"):
        current = args.task if args.status in ("in-progress", "blocked") else (
            next((c[0] for i, c in rows(lines) if c[2].split(" ")[0] not in ("done", "skipped")), "none"))
        lines[2] = re.sub(r"^Current task: \S+", f"Current task: {current}", lines[2])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{args.task} → {cells[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
