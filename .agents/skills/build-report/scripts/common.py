"""Shared helpers of the build-report skill: project configuration, language packs and a small markdown model.

Project root: the folder holding tasks.toml – BUILD_REPORT_ROOT when set, else the current folder when it holds
tasks.toml, else four levels above this file (a project-level skill in <project>/.claude/skills/build-report/).
Interpreter for hooks and helper scripts: the project's venv/bin/python when it exists, else the running one. Language packs: languages/*.toml in this
skill, plus .claude/skills/*/report-language-<code>.toml contributed by other skills. The markdown model reads the
house conventions described in reference.md (numbered section files, numbered headings, "Figure P.n." captions in
image alt text, bold "**Table P.n. …**" lines above tables, [n] citations, [^label] footnotes).
"""

from __future__ import annotations

import fnmatch
import os
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]


def _project_root() -> Path:
    if os.environ.get("BUILD_REPORT_ROOT"):
        return Path(os.environ["BUILD_REPORT_ROOT"]).resolve()
    if (Path.cwd() / "tasks.toml").exists():
        return Path.cwd().resolve()
    return Path(__file__).resolve().parents[4]


ROOT = _project_root()
PYTHON = str(ROOT / "venv" / "bin" / "python") if (ROOT / "venv" / "bin" / "python").exists() else sys.executable


def shown(path) -> Path:
    """A path for messages: relative to the project when it lies inside it, else absolute (the skill itself may be
    installed outside the project)."""
    path = Path(path).resolve()
    return path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
CONFIG = Path(os.environ.get("BUILD_REPORT_CONFIG", ROOT / "tasks.toml"))   # the self-test points it elsewhere


# ----------------------------------------------------------------------------- configuration
def load_config(path: Path | None = None) -> dict:
    return tomllib.loads((path or CONFIG).read_text(encoding="utf-8"))


def language_packs() -> dict[str, dict]:
    """Language packs: languages/<code>/pack.toml in this skill, plus report-language-<code>.toml in other skills."""
    packs = {}
    files = sorted((SKILL / "languages").glob("*/pack.toml")) + sorted(ROOT.glob(".claude/skills/*/report-language-*.toml"))
    for f in files:
        pack = tomllib.loads(f.read_text(encoding="utf-8"))
        pack["_dir"] = f.parent
        packs[pack["code"]] = pack
    return packs


def tasks(config: dict) -> dict[str, dict]:
    return {k: v for k, v in config.items() if k != "project" and isinstance(v, dict) and "report" in v}


def source_language(packs: dict) -> str:
    """The language every other pack translates from (the pack without a [translation] table)."""
    return next((c for c, p in packs.items() if "translation" not in p), "en")


def is_extra(name: str, pack: dict) -> bool:
    """A page that only this language carries (pack [translation] extra_files), outside sync and parity."""
    return any(fnmatch.fnmatch(name, pat) for pat in pack.get("translation", {}).get("extra_files", []))


def twin(path: Path, pack: dict) -> Path:
    """The target-language twin of a source file: NN-slug.md → NN-slug<suffix>."""
    return path.with_name(path.name[:-3] + pack["suffix"])


def task_languages(task: dict, packs: dict) -> list[str]:
    """Languages a task builds: the [task.<code>] tables that match a language pack, English first."""
    codes = [c for c in packs if isinstance(task.get(c), dict)]
    return sorted(codes, key=lambda c: (c != "en", c))


def resolve(task_name: str | None, config: dict) -> list[str]:
    names = list(tasks(config))
    if task_name in (None, "all"):
        return names
    if task_name not in names:
        raise SystemExit(f"unknown task '{task_name}'; known: {', '.join(names)} or all")
    return [task_name]


# ----------------------------------------------------------------------------- section files
def section_files(report: Path, pack: dict, packs: dict) -> list[Path]:
    """Section files of one language in report order (lexical order of NN-SS-slug names)."""
    other = [p["suffix"] for c, p in packs.items() if p["suffix"] != ".md" and p["suffix"] != pack["suffix"]]
    out = []
    for p in sorted(report.glob("*.md")):
        if pack["suffix"] != ".md":
            if p.name.endswith(pack["suffix"]):
                out.append(p)
        elif not any(p.name.endswith(s) for s in other):
            out.append(p)
    return out


def text_lines(text: str):
    """(line_no, line, in_code) for every line; fence lines themselves count as code."""
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            in_code = not in_code
            yield n, line, True
            continue
        yield n, line, in_code


QUOTE = re.compile(r'"[^"]{8,}?"|“[^”]{8,}?”')
CODE_SPAN = re.compile(r"`[^`]*`")
MATH = re.compile(r"\$\$.+?\$\$|(?<!\$)\$(?![\s$])[^$\n]+?(?<!\s)\$(?![\d$])")


def mask(line: str, quotes=True) -> str:
    """Blank out inline code, math and (optionally) verbatim quotations, keeping character positions."""
    line = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), line)
    line = MATH.sub(lambda m: " " * len(m.group(0)), line)
    return QUOTE.sub(lambda m: " " * len(m.group(0)), line) if quotes else line


# ----------------------------------------------------------------------------- report model
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
NUM = r"(?:\d+|[A-Z])(?:\.\d+)*"


@dataclass
class Heading:
    file: str
    line: int
    level: int
    text: str
    number: str = ""          # "3.5.3" for "3.5.3. Title"; "" when unnumbered
    appendix: str = ""        # "I" for "Appendix I – …"


@dataclass
class Caption:
    kind: str                 # "figure" or "table"
    file: str
    line: int
    number: str               # "2.1", "A.4"
    text: str
    target: str = ""          # image path (figures)
    followed_by_table: bool = True


@dataclass
class Report:
    folder: Path
    pack: dict
    files: list[Path]
    headings: list[Heading] = field(default_factory=list)
    captions: list[Caption] = field(default_factory=list)
    references_file: Path | None = None

    def body_files(self):
        """Files outside the front matter (00-*) and the reference list."""
        return [p for p in self.files if not p.name.startswith("00-") and p != self.references_file]


def h1_of(path: Path) -> str:
    for _, line, code in text_lines(path.read_text(encoding="utf-8")):
        m = HEADING.match(line)
        if not code and m and len(m.group(1)) == 1:
            return m.group(2)
    return ""


def load_report(folder: Path, pack: dict, packs: dict) -> Report:
    rep = Report(folder, pack, section_files(folder, pack, packs))
    fig_words = "|".join(map(re.escape, pack["figure"]))
    tab_words = "|".join(map(re.escape, pack["table"]))
    app_words = "|".join(map(re.escape, pack["appendix"]))
    fig_cap = re.compile(rf"^!\[(?:{fig_words})\s+({NUM})\.\s*(.*?)\]\(([^)\s]+)")
    tab_cap = re.compile(rf"^\*\*(?:{tab_words})\s+({NUM})\.\s*(.*?)\*\*\s*$")
    for p in rep.files:
        if h1_of(p) in pack["references"]:
            rep.references_file = p
        lines = p.read_text(encoding="utf-8").splitlines()
        for n, line, code in text_lines("\n".join(lines)):
            if code:
                continue
            m = HEADING.match(line)
            if m:
                text = m.group(2)
                num = re.match(r"^(\d+(?:\.\d+)*)\.\s", text)
                app = re.match(rf"^(?:{app_words})\s+([IVXLC]+)\b", text)
                rep.headings.append(Heading(p.name, n, len(m.group(1)), text, num.group(1) if num else "",
                                            app.group(1) if app else ""))
                continue
            m = fig_cap.match(line)
            if m:
                rep.captions.append(Caption("figure", p.name, n, m.group(1), m.group(2), m.group(3)))
                continue
            m = tab_cap.match(line)
            if m:
                rest = [x for x in lines[n:n + 3] if x.strip()]
                rep.captions.append(Caption("table", p.name, n, m.group(1), m.group(2),
                                            followed_by_table=bool(rest) and rest[0].startswith("|")))
    return rep


def roman(n: int) -> str:
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out, n = out + s, n - v
    return out


def task_for_report(folder: Path) -> dict:
    """The tasks.toml entry whose report folder is `folder` ({} when none)."""
    folder = folder.resolve()
    return next((t for t in tasks(load_config()).values() if (ROOT / t["report"]).resolve() == folder), {})
