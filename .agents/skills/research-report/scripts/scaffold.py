"""Plan and create the workspace of a research report task from its concise outline.

Usage:
    scaffold.py init     --base TASK --outline TASK/reference.md --title "Report Title"
        Stage 0: propose TASK/plan.toml (file map from the outline's sections, the standard task list, seeds from
        the outline's reference list) and TASK/EXECUTION_PLAN.md (the plan template). Both are drafts to refine
        and get approved before `build`; existing files are never overwritten.
    scaffold.py tasks    --base TASK          regenerate the [[tasks]] list from the current [[files]] map (prints it)
    scaffold.py build    --base TASK          create report/ skeleton, research/ trail, AGENT_BRIEF.md, PROGRESS.md
    scaffold.py check    --base TASK          verify skeleton, ledger and seeds against plan.toml (exit 1 on mismatch)
    scaffold.py register --base TASK          add the task to tasks.toml for the build-report skill (if absent)

plan.toml is the machine-readable half of the plan: [plan] (task folder, title, outline), [checks], [[files]]
(name and heading, in document order), [[tasks]] (id, kind, title) and [[seeds]] (outline references).
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

from common import ROOT, SKILL, TEMPLATES, base_dir, load_plan, table_rows

SKIP_SECTIONS = re.compile(r"reference|bibliograph|scope|objective|selection criteria|notes on sourcing", re.I)


def render(text: str, **values) -> str:
    for k, v in values.items():
        text = text.replace("{{" + k + "}}", str(v))
    return text


def write_new(path: Path, text: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return True


def slugify(text: str, n: int = 6) -> str:
    stop = {"the", "a", "an", "of", "and", "for", "in", "on", "to", "with", "how", "what", "is", "isn", "t", "s"}
    words = [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in stop]
    return "-".join(words[:n]) or "section"


def toml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


# ----------------------------------------------------------------------------- stage 0: proposal
def propose_files(outline: Path):
    sys.path.insert(0, str(SKILL / "scripts"))
    import outline as ol                                            # noqa: E402
    lines = outline.read_text(encoding="utf-8").splitlines()
    secs = ol.sections(lines)
    top = min((s["level"] for s in secs if s["number"]), default=2)
    files = [("00-0-title-page.md", "", ""), ("00-1-abbreviations.md", "# List of Abbreviations", ""),
             ("00-2-glossary.md", "# List of Terms", "")]
    part = 0
    for s in secs:
        if s["level"] != top or not s["number"] or SKIP_SECTIONS.search(s["title"]):
            continue
        part += 1
        title = re.sub(r"^[\dA-Za-z.]+\s+", "", s["title"]).replace("&", "and").replace("—", "–")
        files.append((f"{part:02d}-00-{slugify(title)}.md", f"# {part}. {title}", s["number"]))
        subs = [x for x in secs if x["level"] == top + 1 and s["start"] < x["start"] <= s["end"]]
        for k, sub in enumerate(subs, 1):
            t = re.sub(r"^[\dA-Za-z.]+\s+", "", sub["title"]).replace("&", "and").replace("—", "–")
            files.append((f"{part:02d}-{k:02d}-0-{slugify(t)}.md", f"## {part}.{k}. {t}", sub["number"]))
    files.append((f"{part + 1:02d}-references.md", "# References", ""))
    return files, ol.references(lines, secs), ol


def standard_tasks(files):
    tasks = [("S", "Scaffold workspace and register the task"), ("HC", "Scope inputs (title page, inclusions, language)")]
    parts = {}
    for name, heading, *_ in files:
        m = re.match(r"^(#{1,2}) (\d+)\.(\d+)?\.?\s*(.*)", heading)
        if m and m.group(1) == "##":
            parts.setdefault(int(m.group(2)), []).append((m.group(2) + "." + m.group(3), m.group(4)))
        elif m and m.group(1) == "#":
            parts.setdefault(int(m.group(2)), [])
    for p, secs in sorted(parts.items()):
        for num, title in secs:
            short = title[:40]
            tasks += [("R", f"R {num} {short}"), ("W", f"W {num} {short}")]
        tasks.append(("HC", f"Part {p} intro + review"))
    tasks += [("S", "Front matter"), ("S", "References"), ("S", "Full gates"), ("S", "Fact spot-check"),
              ("S", "Style read-through"), ("S", "Build and post-check the Word document"), ("HC", "Final review")]
    return [(f"T{i:02d}", k, t) for i, (k, t) in enumerate(tasks, 1)]


def plan_toml(base, outline, title, files, tasks, seeds):
    out = ["# Machine-readable half of EXECUTION_PLAN.md: edit both together, then run scaffold.py build.", "",
           "[plan]", f"task = {toml_str(base.relative_to(ROOT).as_posix())}", f"title = {toml_str(title)}",
           f"outline = {toml_str(outline.relative_to(ROOT).as_posix())}", f'created = "{date.today()}"', "",
           "[checks]", 'words = "150-700"                 # per section file (intro files: no minimum)', "",
           "[references]", 'heading = "# References"', ""]
    for name, heading, *src in files:
        out += ["[[files]]", f"name = {toml_str(name)}", f"heading = {toml_str(heading)}"]
        out += [f'outline_section = "{src[0]}"'] if src and src[0] else []
        out.append("")
    for tid, kind, t in tasks:
        out += ["[[tasks]]", f'id = "{tid}"', f'kind = "{kind}"', f"title = {toml_str(t)}", ""]
    for k, it in enumerate(seeds, 1):
        url = (f"https://arxiv.org/abs/{it['arxiv']}" if it["arxiv"] else
               f"https://doi.org/{it['doi']}" if it["doi"] else (it["urls"] or [""])[0])
        out += ["[[seeds]]", f'id = "S{k:03d}"', f"slug = {toml_str(slugify(it['short'], 5))}",
                f"source = {toml_str(it['short'])}", f"url = {toml_str(url)}", f'item = "{it["item"]}"',
                'type = "primary"', ""]
    return "\n".join(out)


# ----------------------------------------------------------------------------- build / check / register
def parts_of(plan):
    return sorted({int(f["name"][:2]) for f in plan.get("files", [])
                   if re.match(r"^# \d+\.", f.get("heading", ""))})


def build(base, plan):
    p = plan["plan"]
    values = dict(task=p["task"], title=p["title"], outline=p["outline"], outline_name=Path(p["outline"]).name,
                  date=date.today(), skill=SKILL.relative_to(ROOT).as_posix(),
                  blocks=", ".join(f"Part {n} S{n}00–S{n}99" for n in parts_of(plan)))
    report, research = base / "report", base / "research"
    created = 0
    (report / "assets" / "figures").mkdir(parents=True, exist_ok=True)
    logo = report / "assets" / "university-logo.png"
    if not logo.exists():
        logo.write_bytes((TEMPLATES / "report" / "university-logo.png").read_bytes())
    for f in plan["files"]:
        tpl = TEMPLATES / "report" / re.sub(r"^\d\d-\d-", "", f["name"]) if f["name"].startswith("00-") else None
        text = render(tpl.read_text(encoding="utf-8"), **values) if tpl and tpl.exists() else (
            f["heading"] + "\n" if f["heading"] else "")
        created += write_new(report / f["name"], text)
    for name in ("README.md", "search-log.md", "spot-check.md", "style-review.md"):
        created += write_new(research / name, render((TEMPLATES / "research" / name).read_text(encoding="utf-8"), **values))
    seeds = "".join(f"| {s['id']} | {s['slug']} | {s['source'].replace('|', '/')} | {s['url'] or '–'} | {s['item']} | "
                    f"{s.get('type', 'primary')} | to-fetch | – |\n" for s in plan.get("seeds", []))
    created += write_new(research / "sources.md",
                         render((TEMPLATES / "research" / "sources.md").read_text(encoding="utf-8"), **values) + seeds)
    for n in parts_of(plan):
        for kind in ("claims", "synthesis"):
            created += write_new(research / f"part{n}-{kind}.md", render(
                (TEMPLATES / "research" / f"{kind}.md").read_text(encoding="utf-8"), part=n, **values))
    for name in ("crawl.md", "comprehension.md"):
        created += write_new(research / "templates" / name,
                             render((TEMPLATES / "research" / name).read_text(encoding="utf-8"), **values))
    created += write_new(research / "AGENT_BRIEF.md", render((TEMPLATES / "AGENT_BRIEF.md").read_text(encoding="utf-8"), **values))
    rows = "".join(f"| {t['id']} | {t['title']} | todo |  |  |  |\n" for t in plan["tasks"])
    created += write_new(base / "PROGRESS.md", render((TEMPLATES / "PROGRESS.md").read_text(encoding="utf-8"), **values,
                                                     first=plan["tasks"][0]["id"]) + rows + "\n## Decisions\n\n- (none yet)\n\n## Blocked\n\n- (none)\n")
    print(f"created {created} files under {base.relative_to(ROOT)}/ (existing files kept)")


def check(base, plan):
    errors = []
    report = base / "report"
    names = [f["name"] for f in plan["files"]]
    if names != sorted(names):
        errors.append("plan [[files]] are not in lexical order (sorting the names must give document order)")
    for f in plan["files"]:
        path = report / f["name"]
        if not path.exists():
            errors.append(f"missing report file {f['name']}")
        elif f["heading"]:
            first = next((ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.startswith("#")), "")
            if first.strip() != f["heading"].strip():
                errors.append(f"{f['name']}: first heading '{first[:60]}' differs from the plan '{f['heading'][:60]}'")
    extra = sorted(p.name for p in report.glob("*.md") if not p.name.endswith(".vi.md") and p.name not in names)
    errors += [f"report file not in the plan: {n}" for n in extra]
    ledger = {r[0] for r in table_rows(base / "PROGRESS.md") if re.fullmatch(r"T\d{2,3}", r[0])}
    errors += [f"task {t['id']} missing from PROGRESS.md" for t in plan["tasks"] if t["id"] not in ledger]
    reg = {r[0] for r in table_rows(base / "research" / "sources.md")}
    errors += [f"seed {s['id']} missing from sources.md" for s in plan.get("seeds", []) if s["id"] not in reg]
    for n in parts_of(plan):
        for kind in ("claims", "synthesis"):
            if not (base / "research" / f"part{n}-{kind}.md").exists():
                errors.append(f"research/part{n}-{kind}.md missing")
    for e in errors:
        print("ERROR " + e)
    print(f"\nChecked {len(names)} planned files, {len(plan['tasks'])} tasks, {len(plan.get('seeds', []))} seeds: "
          f"{len(errors)} errors")
    return 1 if errors else 0


def register(base, plan):
    cfg = ROOT / "tasks.toml"
    name = base.name
    text = cfg.read_text(encoding="utf-8") if cfg.exists() else ""
    if re.search(rf"^\[{re.escape(name)}\]", text, re.M):
        print(f"[{name}] already in tasks.toml")
        return 0
    title = plan["plan"]["title"]
    block = f'''
# ---------------------------------------------------------------------------------------------------- {name}
[{name}]
name = {toml_str(title)}
report = "{base.relative_to(ROOT).as_posix()}/report"
build = "build/{name}"
author = "Group"

[{name}.en]
out = "Report_EN.docx"
title = {toml_str(title)}
short_title = {toml_str(title[:60])}
subject = "Research report"

[{name}.hooks]
checks = {{ research_trail = "{(SKILL / 'scripts' / 'check_trail.py').relative_to(ROOT).as_posix()} --base {base.relative_to(ROOT).as_posix()} --all", research_layout = "{(SKILL / 'scripts' / 'layout.py').relative_to(ROOT).as_posix()} check --base {base.relative_to(ROOT).as_posix()}" }}

[{name}.citations]
order = "first-citation"
draft_ids = 'S\\d{{3}}'
'''
    cfg.write_text(text.rstrip("\n") + "\n" + block, encoding="utf-8")
    print(f"added [{name}] to tasks.toml (edit author, short_title and subject; add [{name}.figures] when figures exist)")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["init", "tasks", "build", "check", "register"])
    ap.add_argument("--base", required=True)
    ap.add_argument("--outline")
    ap.add_argument("--title")
    args = ap.parse_args()
    base = base_dir(args.base)

    if args.command == "init":
        if not args.outline or not args.title:
            sys.exit("init needs --outline and --title")
        outline = base_dir(args.outline)
        files, seeds, _ = propose_files(outline)
        tasks = standard_tasks(files)
        wrote = write_new(base / "plan.toml", plan_toml(base, outline, args.title, files, tasks, seeds))
        plan_md = render((TEMPLATES / "EXECUTION_PLAN.md").read_text(encoding="utf-8"), task=base.relative_to(ROOT).as_posix(),
                         title=args.title, outline=outline.relative_to(ROOT).as_posix(), outline_name=outline.name,
                         date=date.today(), skill=SKILL.relative_to(ROOT).as_posix(),
                         blocks="Part 1 S100–S199, Part 2 S200–S299, …")
        wrote_md = write_new(base / "EXECUTION_PLAN.md", plan_md)
        print(f"plan.toml: {'written' if wrote else 'kept (exists)'} – {len(files)} files, {len(tasks)} tasks, "
              f"{len(seeds)} seeds proposed")
        print(f"EXECUTION_PLAN.md: {'written from the template' if wrote_md else 'kept (exists)'}")
        print("next: refine the file map and task cards with the user, then `scaffold.py build`")
        return 0
    plan = load_plan(base)
    if not plan:
        sys.exit(f"{base.relative_to(ROOT)}/plan.toml not found (run init first)")
    if args.command == "tasks":
        files = [(f["name"], f["heading"]) for f in plan["files"]]
        for tid, kind, t in standard_tasks(files):
            print(f'[[tasks]]\nid = "{tid}"\nkind = "{kind}"\ntitle = {toml_str(t)}\n')
        return 0
    if args.command == "build":
        build(base, plan)
        return check(base, plan)
    if args.command == "check":
        return check(base, plan)
    return register(base, plan)


if __name__ == "__main__":
    sys.exit(main())
