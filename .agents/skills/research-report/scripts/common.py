"""Shared helpers of the research-report skill: project paths, the task plan and markdown table parsing.

A research task lives in one folder (for example task3/) holding plan.toml, EXECUTION_PLAN.md, PROGRESS.md,
report/ (the numbered section files) and research/ (the trail). Every script takes --base TASK_DIR.
"""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[4]
TEMPLATES = SKILL / "templates"

SOURCE_ID = re.compile(r"S\d{3}")
CLAIM_ID = re.compile(r"C\d+-\d{3}")
USABLE = {"fetched", "partial"}                    # statuses that may support claims
SAVED = USABLE | {"blocked", "error"}              # statuses that must have a folder on disk
QUOTE = re.compile(r"[\"“]([^\"“”]{8,}?)[\"”]")


def base_dir(arg: str) -> Path:
    p = Path(arg)
    return (p if p.is_absolute() else ROOT / p).resolve()


def load_plan(base: Path) -> dict:
    path = base / "plan.toml"
    return tomllib.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def norm(s: str) -> str:
    """Collapse whitespace and straighten typographic quotes, so verbatim matching ignores layout."""
    s = s.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'").replace("­", "")
    return re.sub(r"\s+", " ", s).strip()


def split_cells(line: str) -> list[str]:
    """Cells of one markdown table row; "\\|" is an escaped pipe inside a cell."""
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def table_rows(path: Path) -> list[list[str]]:
    """Data rows of every markdown table in a file (separator rows skipped)."""
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = split_cells(line)
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    return rows


def load_register(base: Path) -> tuple[dict, dict]:
    """sources.md → ({Sxxx: {slug, status, apa, url}}, reference map {n: Sxxx})."""
    reg, refmap = {}, {}
    for r in table_rows(base / "research" / "sources.md"):
        if SOURCE_ID.fullmatch(r[0]) and len(r) >= 7:
            reg[r[0]] = dict(slug=r[1], source=r[2], url=r[3], status=r[6].lower(), apa=r[7] if len(r) > 7 else "")
        elif len(r) >= 2 and r[0].isdigit() and SOURCE_ID.fullmatch(r[1]):
            refmap[int(r[0])] = r[1]
    return reg, refmap


def claim_files(base: Path) -> list[Path]:
    return sorted((base / "research").glob("part*-claims.md"), key=lambda p: int(re.sub(r"\D", "", p.name) or 0))


def load_claims(base: Path) -> list[dict]:
    claims = []
    for path in claim_files(base):
        part = int(re.sub(r"\D", "", path.name))
        for r in table_rows(path):
            if len(r) >= 6 and CLAIM_ID.fullmatch(r[0]):
                claims.append(dict(id=r[0], claim=r[1], anchor=r[2], source=r[3], kind=r[4], files=r[5], part=part))
    return claims


def source_folder(base: Path, sid: str, slug: str) -> Path:
    return base / "research" / "sources" / f"{sid}-{slug}"


def read_crawl(folder: Path) -> tuple[dict | None, str]:
    """Front-matter header (dict) and body of crawl.md."""
    text = (folder / "crawl.md").read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return None, text
    header = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            header[k.strip()] = v.split(" #")[0].strip().strip('"')
    return header, m.group(2)


def report_dir(base: Path) -> Path:
    return base / "report"


def references_file(report: Path) -> Path | None:
    named = [p for p in sorted(report.glob("[0-9][0-9]-references.md"))]           # NN-references.md
    if named:
        return named[-1]
    return next((p for p in sorted(report.glob("*.md")) if not p.name.endswith(".vi.md")          # or H1 "References"
                 and p.read_text(encoding="utf-8").lstrip().startswith("# References")), None)


def body_files(report: Path) -> list[Path]:
    """English section files outside the front matter (00-*) and the reference list."""
    refs = references_file(report)
    return [p for p in sorted(report.glob("*.md"))
            if not p.name.endswith(".vi.md") and not p.name.startswith("00-") and p != refs]


def body_paragraphs(path: Path):
    """(line_no, paragraph) of running text: no headings, images, captions, display math, code or tables."""
    para, start, in_code = [], 0, False
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines() + [""], 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if (not line.strip() or line.startswith(("#", "![", "$$"))
                or re.match(r"^\*\*(Table|Figure) [A-Z0-9]", line)):
            if para:
                yield start, " ".join(para)
            para = []
            continue
        if not para:
            start = n
        para.append(re.sub(r"`[^`]*`|\$[^$]+\$", " ", line))
