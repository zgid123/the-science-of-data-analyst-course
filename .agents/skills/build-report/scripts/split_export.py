"""Split a single-file Markdown export of a report (for example a human-reviewed Google Docs version) back into the
report's section files, so it can be compared side by side with the sources it was built from.

Usage: python .claude/skills/build-report/scripts/split_export.py --export FILE --report DIR --lang CODE
                                                                              --out DIR [--force]

The report folder supplies the layout: every source file of the language starts with one numbered heading (or, for
front matter, a heading text such as "Danh mục từ viết tắt"), and the export section with the same number or text is
written to the OUT folder under the same file name. Nothing in the report folder is changed.

Normalisation, so that differences in the comparison are differences of content:
  - headings: Google Docs bold markers, "\\." escapes and {#anchor} suffixes are removed ("# 1. Title");
  - Markdown escapes of punctuation outside formulas and code are undone (\\[6\\] → [6], \\- → -); formulas
    ($…$, $$…$$) stay character for character, and "\\|" in tables stays;
  - table separator rows take the house form "| :---- |", trailing spaces and repeated blank lines are removed;
  - figures written as ![caption][imageN] get the path of the same figure number in the report's sources, and every
    embedded image is also saved to OUT/assets/export-images/imageN.png;
  - the table of contents and the lists of figures and tables (Word fields in the built document) are dropped;
  - what the export loses is restored from the report's own file: list items "1)" become "(1)", a formula that the
    export rewrote but that equals the source's formula apart from spacing and braces ({L}_{1} for L_1) takes the
    source's form, a code block whose lines arrive without fences gets its fences back (without the export's
    backslash escapes), a caption repeated in italics under its image is dropped, and figures keep the source's
    width attribute.

--repair: apply only that restoring step to the files already in OUT (for a split folder that was edited since),
leaving every other change in place.

OUT/_split-report.md lists every file with its status (matched, new in the export, missing from the export) and a
similarity ratio to the report's own file, so the review can start with the files that changed most.
Exit code 1 when a section of the export matches no source file (it is still written, as unmatched-NN.md).
"""

from __future__ import annotations

import argparse
import base64
import difflib
import os
import re
import sys
from pathlib import Path

from common import ROOT, language_packs, shown

HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
NUMBER = re.compile(r"^((?:\d+|[A-Z])(?:\.\d+)*)\.?\s+(.*)$")
IMAGE_DEF = re.compile(r"^\[(image\d+)\]:\s*<data:image/(\w+);base64,([A-Za-z0-9+/=]+)>\s*$")
IMAGE_REF = re.compile(r"!\[((?:[^\]\\]|\\.)*)\]\[(image\d+)\]")
FIGURE_LINE = re.compile(r"^!\[(.*)\]\(([^()\s]+)\)(\{[^}]*\})?")          # captions may hold [n] citations
PROTECT = re.compile(r"\$\$.+?\$\$|(?<!\$)\$(?!\s)[^$\n]+?\$|`[^`]*`", re.S)
ESCAPE = re.compile(r"\\([\[\]:.\-_()=&#+!~<>{}'\"%/,;?@^$])")


def unescape(text: str) -> str:
    """Undo punctuation escapes outside formulas and code spans."""
    out, last = [], 0
    for m in PROTECT.finditer(text):
        out.append(ESCAPE.sub(r"\1", text[last:m.start()]))
        out.append(m.group(0))
        last = m.end()
    out.append(ESCAPE.sub(r"\1", text[last:]))
    return "".join(out)


def clean_heading(text: str) -> str:
    text = re.sub(r"\s*\{#[^}]*\}\s*$", "", text)
    text = text.replace("**", "").replace("__", "")
    return re.sub(r"\s+", " ", unescape(text)).strip()


def key_of(heading: str) -> str:
    m = NUMBER.match(heading)
    return m.group(1) if m else heading.lower()


def first_heading(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEAD.match(line)
        if m:
            return clean_heading(m.group(2))
    return None


def tidy(body: str, figures: dict[str, str]) -> str:
    """Normalise one section's body text."""
    def figure(m):
        caption = unescape(m.group(1)).strip()
        num = re.search(r"(\d+\.\d+)", caption)
        path, attrs = figures.get(num.group(1), (None, None)) if num else (None, None)
        return f"![{caption}]({path or f'assets/export-images/{m.group(2)}.png'}){attrs or '{width=100%}'}"

    lines = []
    for line in body.split("\n"):
        line = IMAGE_REF.sub(figure, line).rstrip()
        if re.match(r"^\|(\s*:?-{3,}:?\s*\|)+$", line):          # table separator row in house form
            line = "|" + " :---- |" * (line.count("|") - 1)
        elif not line.startswith("!["):
            line = unescape(line)
        lines.append(line)
    text = "\n".join(lines).strip("\n")
    return re.sub(r"\n{3,}", "\n\n", text)


FENCED = re.compile(r"^(```[^\n]*)\n(.*?)\n```", re.M | re.S)


def formula_key(f: str) -> str:
    return re.sub(r"[\s{}]", "", f)


def restore(text: str, source: str) -> tuple[str, int]:
    """Restore list numbering, formulas and code fences that the export lost, using the report's own file."""
    count = 0
    text, n = re.subn(r"(?m)^(\d+)\) ", r"(\1) ", text)
    count += n
    forms = {formula_key(m.group(0)): m.group(0) for m in PROTECT.finditer(source) if m.group(0).startswith("$")}

    def formula(m):
        nonlocal count
        f = m.group(0)
        if f.startswith("$") and forms.get(formula_key(f), f) != f:
            count += 1
            return forms[formula_key(f)]
        return f
    text = PROTECT.sub(formula, text)
    text, n = re.subn(r"(?m)^(!\[(.+?)\]\([^)]*\)\{[^}]*\})\n\n\*\2\*\n", r"\1\n", text)   # caption repeated in italics
    count += n
    widths = {m.group(2): m.group(3) for m in map(FIGURE_LINE.match, source.splitlines()) if m and m.group(3)}

    def width(m):
        nonlocal count
        if widths.get(m.group(2), m.group(3)) != m.group(3):
            count += 1
            return m.group(0).replace(m.group(3), widths[m.group(2)], 1)
        return m.group(0)
    text = "\n".join(FIGURE_LINE.sub(width, x) for x in text.split("\n"))
    for fence, body in FENCED.findall(source):
        block = body.split("\n")
        lines = text.split("\n")
        first = block[0].strip()
        for i, line in enumerate(lines):
            window = lines[i:i + len(block)]
            if (line.strip() == first and (i == 0 or not lines[i - 1].startswith("```")) and len(window) == len(block)
                    and difflib.SequenceMatcher(None, [x.strip() for x in window], [x.strip() for x in block]).ratio() >= 0.6):
                window = [re.sub(r"\\([*_#\[\]])", r"\1", x) for x in window]      # export escapes inside code
                text = "\n".join(lines[:i] + [fence] + window + ["```"] + lines[i + len(block):])
                count += 1
                break
    return text, count


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--export", type=Path, help="the single-file export (not needed with --repair)")
    ap.add_argument("--report", required=True, type=Path)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--force", action="store_true", help="overwrite files already in OUT")
    ap.add_argument("--repair", action="store_true", help="only restore lists, formulas and code fences in OUT")
    a = ap.parse_args(argv)
    packs = language_packs()
    pack = packs[a.lang]
    suffix = pack.get("suffix", ".md")
    report, out = (ROOT / a.report).resolve(), (ROOT / a.out).resolve()
    if out == report:
        sys.exit("OUT must differ from the report folder: the split is for comparison, the sources stay untouched")

    # 1. The layout of the report: file name per heading key, figure paths per figure number.
    sources = sorted(p for p in report.glob(f"*{suffix}") if suffix != ".md" or not any(
        p.name.endswith(q["suffix"]) for q in packs.values() if q.get("suffix", ".md") != ".md"))
    by_key, figures, title_page = {}, {}, None
    for p in sources:
        h = first_heading(p)
        if h is None:
            title_page = title_page or p
        else:
            by_key[key_of(h)] = p
        for line in p.read_text(encoding="utf-8").splitlines():
            m = FIGURE_LINE.match(line)
            num = re.search(r"(\d+\.\d+)", m.group(1)) if m else None
            if m and num:
                figures[num.group(1)] = (m.group(2), m.group(3))
    logo = next((m.group(2) for m in (FIGURE_LINE.match(x) for x in title_page.read_text(encoding="utf-8")
                 .splitlines()) if m), None) if title_page else None

    if a.repair:
        total = 0
        for p in sources:
            target = out / p.name
            if target.exists():
                new, n = restore(target.read_text(encoding="utf-8"), p.read_text(encoding="utf-8"))
                if n:
                    target.write_text(new, encoding="utf-8")
                    print(f"repaired {target.name}: {n}")
                    total += n
        print(f"{total} repairs in {shown(out)}")
        return 0

    # 2. The export: embedded images out, then front matter and body sections.
    text = a.export.read_text(encoding="utf-8")
    images, kept = {}, []
    for line in text.split("\n"):
        m = IMAGE_DEF.match(line)
        if m:
            images[m.group(1)] = (m.group(2), base64.b64decode(m.group(3)))
        else:
            kept.append(line)
    lines = kept
    body_start = next((i for i, x in enumerate(lines) if HEAD.match(x)), len(lines))
    skip = {w.lower() for w in (pack.get("contents"), pack.get("lof"), pack.get("lot")) if w}
    front_titles = {key_of(first_heading(p)): p for p in sources if p.name.startswith("00-") and first_heading(p)}

    sections: list[tuple[str, str, list[str]]] = []      # (key, heading line, body lines)
    current = ("__title__", "", [])
    for line in lines[:body_start]:
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line.strip())
        title = clean_heading(m.group(1)).lower() if m else None
        if title in skip:
            sections.append(current)
            current = ("__skip__", "", [])
        elif title in front_titles:
            sections.append(current)
            current = (title, "# " + first_heading(front_titles[title]), [])
        else:
            current[2].append(line)
    for line in lines[body_start:]:
        m = HEAD.match(line)
        if m:
            sections.append(current)
            h = clean_heading(m.group(2))
            current = (key_of(h), f"{m.group(1)} {h}", [])
        else:
            current[2].append(line)
    sections.append(current)
    sections = [s for s in sections if s[0] != "__skip__"]
    seen, written = set(), []

    # 3. Write every section under the report's file name.
    out.mkdir(parents=True, exist_ok=True)
    (out / "assets" / "export-images").mkdir(parents=True, exist_ok=True)
    for name, (ext, data) in images.items():
        (out / "assets" / "export-images" / f"{name}.{ext}").write_bytes(data)
    for src in ("figures", Path(logo).name if logo else None):           # previews show the report's images
        if src and (report / "assets" / src).exists() and not (out / "assets" / src).exists():
            os.symlink(os.path.relpath(report / "assets" / src, out / "assets"), out / "assets" / src)

    unmatched = 0
    for key, heading, body in sections:
        if key == "__title__":
            if not "".join(body).strip() or title_page is None:
                continue
            target = out / title_page.name
            content = tidy("\n".join(body), figures)
            if logo:
                content = IMAGE_REF.sub(lambda m: f"![{m.group(1)}]({logo})", content)
                content = re.sub(r"!\[\]\(assets/export-images/image\d+\.png\)\{width=100%\}", f"![]({logo})", content)
            src = title_page
        else:
            src = by_key.get(key)
            if src is None:
                unmatched += 1
                target = out / f"unmatched-{unmatched:02d}{suffix}"
            else:
                target = out / src.name
            content = heading + "\n\n" + tidy("\n".join(body), figures)
            if src is not None:
                content = restore(content, src.read_text(encoding="utf-8"))[0]
        if target.exists() and not a.force and target.name not in seen:
            sys.exit(f"{shown(target)} exists; pass --force to overwrite")
        seen.add(target.name)
        target.write_text(content.rstrip("\n") + "\n", encoding="utf-8")
        written.append((target, src))

    # 4. The comparison index.
    rows = []
    for target, src in written:
        new = target.read_text(encoding="utf-8")
        if src is None:
            rows.append((target.name, "new in the export", "–", "–", len(new.split())))
            continue
        old = src.read_text(encoding="utf-8")
        ratio = difflib.SequenceMatcher(None, old.split(), new.split(), autojunk=False).ratio()
        rows.append((target.name, "matched", f"{ratio:.2f}", len(old.split()), len(new.split())))
    names = {t.name for t, _ in written}
    for p in sources:
        if p.name not in names:
            rows.append((p.name, "missing from the export", "–", len(p.read_text(encoding="utf-8").split()), "–"))
    rows.sort(key=lambda r: r[0])
    changed = sorted((r for r in rows if r[1] == "matched" and float(r[2]) < 1), key=lambda r: float(r[2]))
    index = [f"# Split of {a.export.name}", "",
             f"Export split into the file layout of `{a.report}` ({a.lang}); similarity is the word-level ratio between "
             f"the report's file and the export's section (1.00 = identical).", "",
             "| File | Status | Similarity | Words in report | Words in export |", "| :---- | :---- | :---- | :---- | :---- |"]
    index += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |" for r in rows]
    index += ["", f"Most changed: {', '.join(f'{r[0]} ({r[2]})' for r in changed[:10]) or 'none'}", ""]
    (out / "_split-report.md").write_text("\n".join(index), encoding="utf-8")
    counts = {s: sum(r[1] == s for r in rows) for s in ("matched", "new in the export", "missing from the export")}
    print(f"{len(written)} files → {shown(out)} ({counts['matched']} matched, "
          f"{counts['new in the export']} new, {counts['missing from the export']} missing); "
          f"{len(images)} images saved; index: {shown((out / '_split-report.md'))}")
    return 1 if unmatched else 0


if __name__ == "__main__":
    sys.exit(main())
