"""Pre-check, build and post-check the reports of a project, driven by tasks.toml and the language packs.

Usage (from the project root):
    python .claude/skills/build-report/scripts/report.py init      TASK [--title TEXT] [--author TEXT]
    python .claude/skills/build-report/scripts/report.py list
    python .claude/skills/build-report/scripts/report.py translate TASK|all [--lang CODE] [--add-extra NAME]
    python .claude/skills/build-report/scripts/report.py precheck  TASK|all
    python .claude/skills/build-report/scripts/report.py build     TASK|all [--lang CODE] [--no-figures]
    python .claude/skills/build-report/scripts/report.py postcheck TASK|all [--lang CODE]
    python .claude/skills/build-report/scripts/report.py all       TASK|all [--lang CODE] [--force]
    python .claude/skills/build-report/scripts/report.py test

init       set up a project or a new task: tasks.toml (from templates/tasks.toml, every field documented), the
           Makefile and TASK/report/ from templates/starter/, a small report that passes every check. Existing files
           are kept; a task already in tasks.toml is left as it is.
translate  quick check of every target language: the files to translate or refresh, in report order, with the
           language guide, the domain glossary and the language-only pages the pack offers. Exit 1 while work is open.
precheck   the markdown sources: format, structure, abbreviations, citations (every language), hooks.checks; then
           for each target language its translation status and parity with the source (structure + conventions).
build      the task's figures ([TASK.figures]), one Word document per language, then hooks.extras (a slide deck …).
           A target language whose translation is incomplete is held back with a pointer to `translate`.
postcheck  every built document (check_docx.py, with the language's conventions), then hooks.extra_checks.
all        precheck → build → postcheck. The general checks gate every language; a target language's own
           translation and parity checks gate only that language. --force builds anyway (for inspecting drafts).
test       the skill's self-test, then the project tests listed in [project] tests.
Each step prints one summary line (PASS/FAIL, step, result, seconds) and its details when it fails; the exit code
is 1 when any step fails.
"""

import argparse
import re
import shutil
import shlex
import subprocess
import sys
import time

import glossary
from common import PYTHON, ROOT, SKILL, language_packs, load_config, resolve, task_languages, tasks, shown

PY = PYTHON
SCRIPTS = SKILL / "scripts"
results = []


def command(spec, **values):
    """A hook string or list → argv; .py scripts run with the project's interpreter, {placeholders} are filled in."""
    argv = shlex.split(spec.format(**values)) if isinstance(spec, str) else [str(a) for a in spec]
    return [PY, *argv] if argv[0].endswith(".py") else argv


def step(label, argv, show=False):
    start = time.time()
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    lines = [ln for ln in (proc.stdout + proc.stderr).splitlines() if ln.strip()]
    heads = [ln.strip("= ") for ln in lines if ln.startswith("=====")]
    tally = lines[-1] if lines and re.match(r"^\d+/\d+ ", lines[-1]) else ""        # "39/39 checks passed"
    summary = "; ".join(heads) or tally or next((ln for ln in reversed(lines) if "→" in ln), lines[-1] if lines else "")
    ok = proc.returncode == 0
    results.append((label, ok))
    print(f"{'PASS' if ok else 'FAIL'}  {label:<30} {summary[:120]}  ({time.time() - start:.0f} s)")
    if show or not ok:
        print("\n".join("      " + ln for ln in lines[-30:]))
    return ok


def status_argv(task, code):
    return [PY, SCRIPTS / "translation_status.py", "--report", task["report"], "--lang", code]


def pending(task, code, packs):
    """Files of the source language whose twin in `code` is missing or stale (quick, silent)."""
    proc = subprocess.run(status_argv(task, code), cwd=ROOT, capture_output=True, text=True)
    return [ln.split()[1] for ln in proc.stdout.splitlines() if ln.startswith(("missing", "stale"))]


def precheck(name, task, packs, langs):
    """General checks (all languages), then per target language: translation status, parity, pack checks.
    Returns {"general": bool, "<code>": bool, …}."""
    report = task["report"]
    ok = step(f"{name} format", [PY, SCRIPTS / "check_format.py", "--report", report])
    for check in ("structure", "style", "abbreviations", "citations"):
        ok &= step(f"{name} {check}", [PY, SCRIPTS / f"check_{check}.py", "--report", report])
    if task.get("people"):                                  # names spelled exactly as listed in tasks.toml
        ok &= step(f"{name} names", [PY, SCRIPTS / "check_names.py", "--task", name])
    for check, spec in task.get("hooks", {}).get("checks", {}).items():
        ok &= step(f"{name} {check}", command(spec, report=report, task=name))
    gates = {"general": ok}
    for code in langs:
        if "translation" not in packs[code]:
            gates[code] = True
            continue
        lang_ok = step(f"{name} translation {code}", status_argv(task, code))
        lang_ok &= step(f"{name} parity {code}", [PY, SCRIPTS / "check_parity.py", "--report", report, "--lang", code])
        for check, spec in packs[code].get("checks", {}).items():
            lang_ok &= step(f"{name} {check}", command(spec, report=report, skill=packs[code]["_dir"], task=name))
        gates[code] = lang_ok
    return gates


def translate(name, task, packs, langs, add_extra=None):
    """Print the translation work of each target language and how to do it; optionally add a language-only page."""
    for code in langs:
        pack = packs[code]
        if "translation" not in pack:
            continue
        if add_extra:
            src = pack["_dir"] / pack["translation"].get("extras", "templates") / add_extra
            dst = ROOT / task["report"] / add_extra
            if src.exists() and not dst.exists():
                dst.write_bytes(src.read_bytes())
                print(f"added {shown(dst)} from the {pack['name']} templates; fill in its placeholders with the user")
            elif src.exists():
                print(f"{shown(dst)} already exists; kept")
        step(f"{name} translation {code}", status_argv(task, code), show=True)
        todo = pending(task, code, packs)
        tr = pack["translation"]
        extras = sorted((pack["_dir"] / tr.get("extras", "templates")).glob("*.md"))
        missing_extras = [e.name for e in extras if not (ROOT / task["report"] / e.name).exists()]
        print(f"      guide     {shown((pack['_dir'] / tr.get('guide', 'guide.md')))}")
        if (pack["_dir"] / tr.get("review", "review.md")).exists():
            print(f"      review    {shown((pack['_dir'] / tr.get('review', 'review.md')))} "
                  f"(native review after translation; stages in reference.md section 4.3)")
        if (pack["_dir"] / tr.get("lessons", "lessons.md")).exists():
            print(f"      lessons   {shown((pack['_dir'] / tr.get('lessons', 'lessons.md')))} "
                  f"(what human reviewers changed; read before translating)")
        voice_line = pack.get("style", {}).get("voice", {}).get(task.get("voice", ""), "")
        if voice_line:
            print(f"      voice     {voice_line} (task voice = {task['voice']}; put this line into every translator's and reviewer's prompt)")
        names = glossary.names_of(task, code)
        print(f"      glossary  common/* + {', '.join(names) or '(no domain or topic selected)'} "
              f"(see: glossary.py --lang {code} --task {name} show)")
        if missing_extras:
            print(f"      optional  {pack['name']}-only pages to offer the user: {', '.join(missing_extras)} "
                  f"(add one with: report.py translate {name} --lang {code} --add-extra NAME)")
        if todo:
            print(f"      next      translate {len(todo)} file(s) in this order, check each pair with check_parity.py "
                  f"--lang {code}, record it with translation_status.py --mark, then build: report.py all {name}")


def google_docs_path(task, cfg):
    """The portrait-only copy for Google Docs, next to the Word file: Report_EN.docx → Report_EN_GoogleDocs.docx."""
    stem, _, ext = cfg["out"].rpartition(".")
    return f"{task['build']}/{stem}_GoogleDocs.{ext}"


def build(name, task, langs, figures=True):
    hooks = task.get("hooks", {})
    ok = True
    if figures and "figures" in task:
        ok &= step(f"{name} figures", [PY, SCRIPTS / "render_figures.py", name])
    for code in langs:
        cfg = task[code]
        args = [PY, SCRIPTS / "build_docx.py", "--src", task["report"], "--lang", code,
                "--title", cfg["title"], "--short-title", cfg["short_title"],
                "--author", cfg.get("author", task.get("author", "")), "--subject", cfg.get("subject", ""),
                "--figure-lang", cfg.get("figure_lang", code)]
        layout = task.get("layout", {})
        if layout.get("compact"):                           # a short document: no part page breaks, no contents
            args.append("--compact")
            if layout.get("landscape_tables"):              # wide or text-heavy tables still get landscape pages
                args.append("--landscape-tables")
        elif layout.get("part_breaks") is False:            # contents kept; parts run on, all pages portrait
            args.append("--run-on-parts")
            if layout.get("landscape_appendices"):          # appendices sit outside the page budget and start a new page
                args.append("--landscape-appendices")
        for key in ("body_size", "line_spacing"):           # the task's page budget overrides the language pack
            if key in layout:
                args += [f"--{key.replace('_', '-')}", str(layout[key])]
        main_args = args + (["--vector"] if layout.get("vector_figures") else [])   # SVG figures, PNG fallback
        ok &= step(f"{name} build {code}", main_args + ["--out", f"{task['build']}/{cfg['out']}"])
        if task.get("google_docs"):
            ok &= step(f"{name} build {code} (Google Docs)", args + ["--out", google_docs_path(task, cfg), "--portrait"])
    for spec in hooks.get("extras", []):
        ok &= step(f"{name} {spec.split()[0].removesuffix('.py')}", command(spec, task=name))
    return ok


def postcheck(name, task, langs):
    ok = True
    for code in langs:
        ok &= step(f"{name} docx {code}", [PY, SCRIPTS / "check_docx.py", "--task", name, "--lang", code])
        if task.get("google_docs"):
            ok &= step(f"{name} docx {code} (Google Docs)", [PY, SCRIPTS / "check_docx.py", "--task", name, "--lang", code,
                                                            "--docx", google_docs_path(task, task[code])])
    for check, spec in task.get("hooks", {}).get("extra_checks", {}).items():
        ok &= step(f"{name} {check}", command(spec, task=name))
    return ok


def toml_str(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def init(name, title, author):
    """Install tasks.toml, the Makefile and a starter report for task `name`; keep whatever already exists."""
    templates = SKILL / "templates"
    text = (templates / "tasks.toml").read_text(encoding="utf-8")
    text = (text.replace('"Report Title"', toml_str(title)).replace('"Group N"', toml_str(author))
            .replace("taskN", name))
    cfg = ROOT / "tasks.toml"
    if not cfg.exists():
        cfg.write_text(text, encoding="utf-8")
        print(f"created  {shown(cfg)} with task [{name}] (every field documented there)")
    elif re.search(rf"^\[{re.escape(name)}\]", cfg.read_text(encoding="utf-8"), re.M):
        print(f"kept     {shown(cfg)}: task [{name}] is already there")
    else:
        block = text[text.index("# ----"):]                  # the task part of the template
        cfg.write_text(cfg.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + block, encoding="utf-8")
        print(f"added    task [{name}] to {shown(cfg)}")
    make = ROOT / "Makefile"
    if not make.exists():
        shutil.copy(templates / "Makefile", make)
        print(f"created  {shown(make)}")
    report = ROOT / name / "report"
    if report.exists():
        print(f"kept     {shown(report)}: the folder exists")
    else:
        shutil.copytree(templates / "starter" / "report", report)
        page = report / "00-0-title-page.md"
        page.write_text(page.read_text(encoding="utf-8").replace("{{TITLE}}", title.upper())
                        .replace("{{AUTHOR}}", author), encoding="utf-8")
        print(f"created  {shown(report)}/ (starter report: title page, abbreviations, two parts, references)")
    print(f"next     python {shown(SKILL / 'scripts' / 'report.py')} all {name}   (or: make all TASK={name})")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["init", "list", "translate", "precheck", "build", "postcheck", "all", "test"])
    ap.add_argument("task", nargs="?", default="all")
    ap.add_argument("--lang", default="all", help="language pack code, or all languages of the task")
    ap.add_argument("--no-figures", action="store_true", help="reuse the rendered figures")
    ap.add_argument("--add-extra", help="translate: copy this language-only page template into the report")
    ap.add_argument("--title", default="Report Title", help="init: the report title")
    ap.add_argument("--author", default="Group N", help="init: the default author")
    ap.add_argument("--force", action="store_true", help="build even when prechecks or translations are incomplete")
    args = ap.parse_args()
    if args.command == "init":
        if args.task == "all" or not re.fullmatch(r"[A-Za-z][\w-]*", args.task):
            raise SystemExit("init needs a task name such as task8 (letters, digits, - and _)")
        return init(args.task, args.title, args.author)
    config, packs = load_config(), language_packs()
    all_tasks = tasks(config)

    if args.command == "list":
        for name, t in all_tasks.items():
            langs = task_languages(t, packs)
            print(f"{name}: {t.get('name', '')}\n  report   {t['report']}\n  outputs  "
                  + ", ".join(f"{t['build']}/{t[c]['out']}" for c in langs)
                  + "".join(f"\n  hook     {k}: {v}" for k, v in t.get("hooks", {}).items()))
        print(f"language packs: {', '.join(f'{c} ({shown(p['_dir'])})' for c, p in packs.items())}")
        return 0
    if args.command == "test":
        step("test build-report skill", [PY, SCRIPTS / "selftest.py"])
        for test in config.get("project", {}).get("tests", []):
            parts = test.split("/")
            label = f"{parts[2]} skill" if parts[:2] == [".claude", "skills"] else test.removesuffix(".py")
            step(f"test {label}", command(test))
    else:
        for name in resolve(args.task, config):
            task = all_tasks[name]
            if not (ROOT / task["report"]).is_dir():             # e.g. a fresh clone without that task's folder
                hint = f"report folder {task['report']} not found; start it with: report.py init {name}"
                if args.task == "all":
                    print(f"skip  {name}: {hint}")
                else:
                    results.append((f"{name} report", False))
                    print(f"FAIL  {name} report{'':<17} {hint}")
                continue
            langs = task_languages(task, packs) if args.lang == "all" else [args.lang]
            if args.command == "translate":
                translate(name, task, packs, langs, args.add_extra)
                continue
            build_langs = langs
            if args.command in ("precheck", "all"):
                gates = precheck(name, task, packs, langs)
                if args.command == "all" and not args.force:
                    if not gates["general"]:
                        print(f"skip  {name}: the general prechecks failed, so no document is built (fix the sources or use --force)")
                        continue
                    held = [c for c in langs if not gates[c]]
                    for c in held:
                        print(f"skip  {name} {c}: translation or parity is not complete; run: report.py translate {name} --lang {c}")
                    build_langs = [c for c in langs if gates[c]]
            elif args.command == "build" and not args.force:
                for c in [c for c in langs if "translation" in packs[c] and pending(task, c, packs)]:
                    results.append((f"{name} build {c}", False))
                    print(f"FAIL  {name} build {c:<23} {len(pending(task, c, packs))} file(s) still to translate; "
                          f"run: report.py translate {name} --lang {c}")
                    build_langs = [x for x in build_langs if x != c]
            if args.command in ("build", "all"):
                build(name, task, build_langs, figures=not args.no_figures)
            if args.command in ("postcheck", "all"):
                postcheck(name, task, build_langs)

    failed = [label for label, ok in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} steps passed" + (f"; failed: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
