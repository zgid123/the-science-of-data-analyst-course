"""Self-test of the build-report skill: clean runs and fault injection for every pre-check and the post-check.

Usage: python .claude/skills/build-report/scripts/selftest.py   (about 10 s)

A copy of the skill's own test report (tests/fixture/report: a two-language report on presentation attack
detection, with Vietnamese twins) is written to build/.cache/buildtest/ in the project, with its own tasks.toml
(citation order first-citation); its figures are drawn as plain placeholders of the sizes and resolutions listed in
tests/fixture/figures.json, which is all the checks and the builder read from them. The untouched copy must pass every check with 0 errors; then each injected fault,
applied to the copy and reverted afterwards, must be reported by its check with the expected message. Word faults
are injected into a copy of the document built from the clean sources.
"""

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from pptx.util import Inches, Pt

from common import PYTHON, ROOT, SKILL

PY = PYTHON
SCRIPTS = SKILL / "scripts"
BASE = ROOT / "build" / ".cache" / "buildtest"
REP = BASE / "report"
FIXTURE = SKILL / "tests" / "fixture"
DOCX = BASE / "out" / "Test_EN.docx"
CONFIG = BASE / "tasks.toml"
results = []


def setup():
    shutil.rmtree(BASE, ignore_errors=True)
    REP.mkdir(parents=True)
    for p in (FIXTURE / "report").glob("*.md"):                # English sources and their Vietnamese twins
        shutil.copy(p, REP / p.name)
    for rel, spec in json.loads((FIXTURE / "figures.json").read_text(encoding="utf-8")).items():
        path = REP / rel                                        # a plain image of the original's size and resolution
        path.parent.mkdir(parents=True, exist_ok=True)
        img = Image.new(spec["mode"], tuple(spec["size"]), "white")
        img.save(path, dpi=tuple(spec["dpi"])) if spec["dpi"] else img.save(path)
    CONFIG.write_text(f'''[selftest]
name = "Self-test copy of the fixture report"
report = "{REP.relative_to(ROOT)}"
build = "{DOCX.parent.relative_to(ROOT)}"
author = "Test Group"

[selftest.en]
out = "{DOCX.name}"
title = "Test Report"
short_title = "Test Report"
subject = "Testing"

[selftest.vi]
out = "Test_VI.docx"
title = "Báo cáo thử nghiệm"
short_title = "Báo cáo thử nghiệm"
author = "Nhóm thử nghiệm"
glossaries = ["biometrics-and-pad", "digital-banking-vn"]

[selftest.abbreviations.titles]
en = ["Presentation Attack Detection Act"]

[selftest.citations]
order = "first-citation"
draft_ids = 'S\\d{{3}}'
''', encoding="utf-8")


def run(script, *args):
    env = {**os.environ, "BUILD_REPORT_CONFIG": str(CONFIG)}
    r = subprocess.run([PY, str(SCRIPTS / script), *map(str, args)], cwd=ROOT, capture_output=True, text=True, env=env)
    return r.returncode, r.stdout + r.stderr


def _rows(path):
    import glossary
    return glossary.rows_of(path)


def expect(label, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"  ({detail})" if detail else ""))


CHECKS = {"format": ("check_format.py", "--report", REP.relative_to(ROOT)),
          "structure": ("check_structure.py", "--report", REP.relative_to(ROOT)),
          "abbreviations": ("check_abbreviations.py", "--report", REP.relative_to(ROOT)),
          "citations": ("check_citations.py", "--report", REP.relative_to(ROOT)),
          "style": ("check_style.py", "--report", REP.relative_to(ROOT)),
          "docx": ("check_docx.py", "--task", "selftest", "--lang", "en", "--docx", DOCX.relative_to(ROOT)),
          "parity": ("check_parity.py", "--report", REP.relative_to(ROOT), "--lang", "vi"),
          "translation": ("translation_status.py", "--report", REP.relative_to(ROOT), "--lang", "vi")}


BASELINE = {}


def baseline(check):
    """Exit code of a check on the untouched copy: the fixture is a real report, so its own state is the reference."""
    if check not in BASELINE:
        BASELINE[check] = run(*CHECKS[check])[0]
    return BASELINE[check]


def md_fault(check, label, file, mutate, needle, want="error"):
    base = baseline(check) if want == "none" else 0
    path = REP / file
    original = path.read_text(encoding="utf-8")
    changed = mutate(original)
    assert changed != original, f"mutation did not apply: {label}"
    path.write_text(changed, encoding="utf-8")
    code, out = run(*CHECKS[check])
    path.write_text(original, encoding="utf-8")
    hit = needle in out
    ok = {"error": code == 1 and hit, "warn": hit, "none": code == base and not hit}[want]
    expect(f"{check}: {label}", ok, needle if want != "none" else f"'{needle}' not reported")


def docx_fault(label, mutate, needle, want="error"):
    shutil.copy(BASE / "clean.docx", DOCX)
    doc = Document(str(DOCX))
    mutate(doc)
    doc.save(str(DOCX))
    code, out = run(*CHECKS["docx"])
    hit = needle in out
    expect(f"docx: {label}", (code == 1 and hit) if want == "error" else hit, needle)


def body_para(doc, style="BodyText"):
    return next(p for p in doc.paragraphs if p.style.style_id == style and len(p.text) > 40)


def main():
    setup()
    print("== Clean copy")
    for check in ("format", "structure", "style", "abbreviations", "citations"):
        code, out = run(*CHECKS[check])
        expect(f"{check}: clean sources pass", code == 0, [ln for ln in out.splitlines() if ln.strip()][-1][:90])
    code, out = run("build_docx.py", "--src", REP.relative_to(ROOT), "--lang", "en", "--out", DOCX.relative_to(ROOT),
                    "--title", "Test Report", "--short-title", "Test Report", "--author", "Test Group")
    expect("build: clean sources build", code == 0, out.strip().splitlines()[-1][:90] if out.strip() else "")
    shutil.copy(DOCX, BASE / "clean.docx")
    code, out = run(*CHECKS["docx"])
    expect("docx: clean document passes", code == 0, out.splitlines()[0][:90])

    print("== Title page layouts (names side by side; one label/value table)")

    def title_facts(path):
        d = Document(str(path))
        big = [p.text for p in d.paragraphs[:12] if any(r.font.size and r.font.size.pt == 22 for r in p.runs)]
        t = d.tables[0]._tbl
        cols = [int(g.get(qn("w:w"))) / 567 for g in t.iter(qn("w:gridCol"))]
        tblw = t.tblPr.find(qn("w:tblW"))
        gap = t.find(".//" + qn("w:tcMar"))
        return big, cols, tblw.get(qn("w:type")) if tblw is not None else None, gap is not None
    big, cols, wtype, _ = title_facts(DOCX)
    expect("title page: the title in capitals after the logo takes the title size",
           len(big) == 1 and big[0].startswith("PRESENTATION ATTACKS"), str(big)[:90])
    expect("title page: names side by side keep two wide columns in a fixed-width table",
           len(cols) == 2 and min(cols) >= 6 and wtype == "dxa", f"{[round(c, 1) for c in cols]} cm, tblW {wtype}")
    page = REP / "00-0-title-page.md"
    original = page.read_text(encoding="utf-8")
    page.write_text("**UNIVERSITY OF SCIENCE**\n\n**FACULTY OF INFORMATION TECHNOLOGY**\n\n"
                    "![University logo](assets/university-logo.png)\n\n**Course name**\n\n"
                    "**A Report Title in Sentence Case**\n\n| **Group information** | **Content** |\n| :---- | :---- |\n"
                    "| Lecturers | Dr. Nguyễn Văn A |\n|  | MSc. Trần Thị B |\n| Simulated stakeholders | Program "
                    "Manager, Course Lecturer, Academic Advisor, Student (played by generative AI) |\n"
                    "| Submission date | 14 November 2026 |\n\nHo Chi Minh City, 2026\n", encoding="utf-8")
    label_docx = BASE / "out" / "Test_EN_labels.docx"
    code, out = run("build_docx.py", "--src", REP.relative_to(ROOT), "--lang", "en", "--out",
                    label_docx.relative_to(ROOT), "--title", "Test Report", "--short-title", "Test Report",
                    "--author", "Test Group")
    page.write_text(original, encoding="utf-8")
    big, cols, wtype, gap = title_facts(label_docx)
    expect("title page: a sentence-case title is found, not the faculty line above the logo",
           code == 0 and big == ["A Report Title in Sentence Case"], str(big)[:90])
    expect("title page: a label column fits its longest label, the values take the rest, with a gap after the labels",
           len(cols) == 2 and 22 * 0.21 <= cols[0] <= 7.5 and abs(sum(cols) - 15) < 0.1 and gap,
           f"{[round(c, 1) for c in cols]} cm, gap {gap}")

    print("== Vector figures ([TASK.layout] vector_figures = true)")
    figs = sorted((REP / "assets" / "figures").glob("*.png"))
    twin = figs[0].with_suffix(".svg")
    twin.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="50"><text x="5" y="30">A</text></svg>',
                    encoding="utf-8")
    vec_docx = BASE / "out" / "Test_EN_vector.docx"
    code, out = run("build_docx.py", "--src", REP.relative_to(ROOT), "--lang", "en", "--out", vec_docx.relative_to(ROOT),
                    "--title", "Test Report", "--short-title", "Test Report", "--author", "Test Group", "--vector")
    twin.unlink()
    import zipfile
    with zipfile.ZipFile(vec_docx) as z:
        svg_parts = [n for n in z.namelist() if n.endswith(".svg")]
        refs = z.read("word/document.xml").decode().count("svgBlip")
    expect("vector: a figure with an SVG twin goes in as SVG, its PNG kept as fallback",
           code == 0 and len(svg_parts) == 1 and refs >= 1 and len(Document(str(vec_docx)).inline_shapes) > 0,
           f"{len(svg_parts)} svg parts, {refs} refs")

    print("== Compact layout ([TASK.layout] compact = true)")
    compact_docx = BASE / "out" / "Test_EN_compact.docx"
    code, out = run("build_docx.py", "--src", REP.relative_to(ROOT), "--lang", "en", "--out",
                    compact_docx.relative_to(ROOT), "--title", "Test Report", "--short-title", "Test Report",
                    "--author", "Test Group", "--compact", "--body-size", "11", "--line-spacing", "1.15")
    expect("compact: builds", code == 0, out.strip().splitlines()[-1][:90] if out.strip() else "")
    cdoc = Document(str(compact_docx))
    instr = " ".join(t.text or "" for t in cdoc.element.body.iter(qn("w:instrText")))
    expect("compact: no contents or list fields", "TOC" not in instr)
    size = cdoc.styles["Body Text"].font.size
    expect("layout: --body-size reaches the body style", size is not None and size.pt == 11, f"{size.pt if size else None} pt")
    h1 = cdoc.styles["Heading 1"].paragraph_format.page_break_before
    expect("compact: parts start without a page break", not h1, f"page_break_before={h1}")
    fmt = cdoc.sections[1]._sectPr.find(qn("w:pgNumType"))
    expect("compact: the page after the title page is 1 (arabic)",
           fmt is not None and fmt.get(qn("w:fmt")) == "decimal" and fmt.get(qn("w:start")) == "1")
    compact_cfg = BASE / "tasks_compact.toml"
    compact_cfg.write_text(CONFIG.read_text(encoding="utf-8") + "\n[selftest.layout]\ncompact = true\n", encoding="utf-8")
    r = subprocess.run([PY, str(SCRIPTS / "check_docx.py"), "--task", "selftest", "--lang", "en", "--docx",
                        str(compact_docx.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True,
                       env={**os.environ, "BUILD_REPORT_CONFIG": str(compact_cfg)})
    expect("compact: post-check passes for a compact task", r.returncode == 0, (r.stdout + r.stderr).splitlines()[0][:90])
    r = subprocess.run([PY, str(SCRIPTS / "check_docx.py"), "--task", "selftest", "--lang", "en", "--docx",
                        str(compact_docx.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True,
                       env={**os.environ, "BUILD_REPORT_CONFIG": str(CONFIG)})
    expect("compact: a regular task still requires the contents", r.returncode == 1 and "table of contents" in r.stdout)

    print("== Title page height")
    from docx.shared import Pt
    tall_docx = BASE / "out" / "Test_EN_tall_title.docx"
    base_docx = DOCX if DOCX.exists() else compact_docx
    tdoc = Document(str(base_docx))
    first = next(p for p in tdoc.paragraphs if p.text.strip())
    first.paragraph_format.space_before = Pt(800)                       # pushes the title page past one page
    tdoc.save(str(tall_docx))
    r = subprocess.run([PY, str(SCRIPTS / "check_docx.py"), "--task", "selftest", "--lang", "en", "--docx",
                        str(tall_docx.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True,
                       env={**os.environ, "BUILD_REPORT_CONFIG": str(CONFIG)})
    expect("title page: a title page taller than its text area fails the post-check",
           r.returncode == 1 and "title page is estimated" in r.stdout, (r.stdout + r.stderr).splitlines()[0][:90])

    print("== Pessimistic page layout (paginate.py)")
    sys.path.insert(0, str(SCRIPTS))
    import estimate_pages
    import paginate
    parts_p, pages_p = paginate.paginate(str(base_docx), paginate.PESSIMISTIC)
    parts_o, pages_o = paginate.paginate(str(base_docx), paginate.OPTIMISTIC)
    flow = estimate_pages.estimate(str(base_docx))
    expect("paginate: the pessimistic layout is never shorter than the optimistic layout or the continuous flow",
           parts_p[-1][2] >= parts_o[-1][2] and parts_p[-1][2] >= flow["body"] + flow["references"],
           f"pessimistic {parts_p[-1][2]:.2f}, optimistic {parts_o[-1][2]:.2f}, flow {flow['body'] + flow['references']:.2f}")
    brk_docx = BASE / "out" / "Test_EN_page_break.docx"
    small = Document()
    for _ in range(6):
        small.add_paragraph("A short paragraph of body text that fills part of one page. " * 3)
    small.save(str(brk_docx))
    _, pages_one = paginate.paginate(str(brk_docx), paginate.PESSIMISTIC)
    small.paragraphs[3].paragraph_format.page_break_before = True       # one forced break mid-page
    small.save(str(brk_docx))
    _, pages_two = paginate.paginate(str(brk_docx), paginate.PESSIMISTIC)
    expect("paginate: a forced page break on a one-page document adds exactly one page",
           pages_one == 1 and pages_two == 2, f"{pages_one} page(s) before, {pages_two} after the break")

    r = subprocess.run([PY, str(SCRIPTS / "page_budget.py"), str(base_docx), "--budget", "10"], cwd=ROOT,
                       capture_output=True, text=True)
    expect("page_budget: reports optimistic and pessimistic main content, the budget and the last-page fill",
           r.returncode == 0 and "pessimistic" in r.stdout and "budget 10 pages" in r.stdout
           and "last main-text page" in r.stdout, (r.stdout + r.stderr).strip().splitlines()[-1][:90])

    print("== Lists of figures and tables, table fit")
    from docx.oxml.ns import qn as _qn
    def post_check(path):
        return subprocess.run([PY, str(SCRIPTS / "check_docx.py"), "--task", "selftest", "--lang", "en", "--docx",
                               str(path.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True,
                              env={**os.environ, "BUILD_REPORT_CONFIG": str(CONFIG)})
    bad_docx = BASE / "out" / "Test_EN_faults.docx"
    fdoc = Document(str(base_docx))
    for cap in [p for p in fdoc.paragraphs if p.style.style_id == "ImageCaption"]:
        cap.style = fdoc.styles["Normal"]
    grid = next(t for t in fdoc.tables[1:] if len(t.columns) > 1)._tbl.find(_qn("w:tblGrid"))     # after the title page
    grid.findall(_qn("w:gridCol"))[0].set(_qn("w:w"), "200")     # a 10 pt column
    fdoc.save(str(bad_docx))
    r = post_check(bad_docx)
    expect("lists: a list of figures with no figure captions fails the post-check", r.returncode == 1 and "an empty page" in r.stdout, r.stdout[:120])
    expect("tables: a column too narrow for its words fails the post-check", "breaks the word" in r.stdout, r.stdout[:120])

    print("== Run-on parts ([TASK.layout] part_breaks = false)")
    runon_docx = BASE / "out" / "Test_EN_runon.docx"
    code, out = run("build_docx.py", "--src", REP.relative_to(ROOT), "--lang", "en", "--out",
                    runon_docx.relative_to(ROOT), "--title", "Test Report", "--short-title", "Test Report",
                    "--author", "Test Group", "--run-on-parts")
    rdoc = Document(str(runon_docx))
    instr = " ".join(t.text or "" for t in rdoc.element.body.iter(qn("w:instrText")))
    h1 = rdoc.styles["Heading 1"].paragraph_format.page_break_before
    refs_break = [p for p in rdoc.paragraphs if p.style.name == "Heading 1" and p.text.strip() == "References"
                  and p._p.find(qn("w:pPr") + "/" + qn("w:pageBreakBefore")) is not None]
    part_break = [p for p in rdoc.paragraphs if p.style.name == "Heading 1" and p.text[:1].isdigit()
                  and p._p.find(qn("w:pPr") + "/" + qn("w:pageBreakBefore")) is not None]
    land = sum(1 for s in rdoc.sections if s.orientation == WD_ORIENT.LANDSCAPE)
    expect("run-on: builds with the contents and the lists kept", code == 0 and 'TOC \\o "1-3"' in instr)
    expect("run-on: numbered parts start without a page break, the references on a new page",
           not h1 and not part_break and len(refs_break) == 1, f"style break={h1}, refs={len(refs_break)}")
    expect("run-on: every page stays portrait", land == 0, f"{land} landscape sections")
    r = subprocess.run([PY, str(SCRIPTS / "check_docx.py"), "--task", "selftest", "--lang", "en", "--docx",
                        str(runon_docx.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True,
                       env={**os.environ, "BUILD_REPORT_CONFIG": str(CONFIG)})
    expect("run-on: post-check passes for a regular task", r.returncode == 0, (r.stdout + r.stderr).splitlines()[0][:90])

    m, f = "01-01-2-evaluation-metrics.md", "01-02-3-pad-in-the-biometric-pipeline.md"
    refs = next(p.name for p in sorted(REP.glob("[0-9][0-9]-references.md")))   # the reference list, whatever its number
    cap = "**Table 1.2. PAD evaluation metrics**"
    print("\n== Format faults")
    md_fault("format", "em dash", m, lambda t: t + "\nA — B.\n", "em dash")
    md_fault("format", "list numbered 1.", m, lambda t: t + "\n1. Item\n", "numbered list item")
    md_fault("format", "bulleted list (warning)", m, lambda t: t + "\n- item\n", "bulleted list item", want="warn")
    md_fault("format", "display formula wider than the page (warning)", m,
             lambda t: t + "\n$$P = \\frac{\\text{correct operations}}{\\text{generated unique operations}}, \\qquad "
                           "R = \\frac{\\text{correct operations}}{\\text{operations in the silver workflow}}$$\n",
             "display formula about", want="warn")
    md_fault("format", "heading glued to paragraph", m, lambda t: t + "\nText line\n## Heading\n", "heading without a blank line")
    md_fault("format", "list glued to paragraph", m, lambda t: t + "\nText line\n- item\n", "list starts without a blank line")
    md_fault("format", "table glued to caption", m, lambda t: t.replace(cap + "\n\n|", cap + "\n|"), "table without a blank line")
    md_fault("format", "table row with extra cell", m, lambda t: t.replace("| APCER |", "| APCER | extra |", 1), "cells, header has")
    md_fault("format", "table without separator", m, lambda t: re.sub(r"(?m)^\| :-.*\n", "", t, count=1), "separator row")
    md_fault("format", "image glued to text", f, lambda t: t.replace("\n\n![Figure 1.1", "\nText\n![Figure 1.1"), "image not alone")
    md_fault("format", "unclosed code fence", m, lambda t: t + "\n```\ncode\n", "unclosed code fence")

    print("\n== Structure faults")
    md_fault("structure", "heading number skipped", m, lambda t: t.replace("### 1.1.2.", "### 1.1.5.", 1), "breaks the sequence")
    md_fault("structure", "caption number skipped", m, lambda t: t.replace("**Table 1.2.", "**Table 1.7."), "Table 1.7 breaks the sequence")
    md_fault("structure", "caption in wrong part", m, lambda t: t.replace("**Table 1.2.", "**Table 2.2."), "is not in Part")
    md_fault("structure", "caption without table", m, lambda t: t.replace(cap + "\n\n", cap + "\n\nSome text.\n\n"), "not directly followed by a table")
    md_fault("structure", "cross-reference to nothing", m, lambda t: t + "\nSee Section 9.9 for details.\n", "'Section 9.9' refers to nothing")
    md_fault("structure", "missing image file", f, lambda t: t.replace("task2-1-1-pad-pipeline.png", "missing.png"), "does not exist")
    md_fault("structure", "undefined footnote", m, lambda t: t + "\nText[^nope].\n", "has no definition")
    md_fault("structure", "table never referred to (warning)", m, lambda t: t.replace("Table 1.2 summarises the four metrics.", "The four metrics follow."),
             "Table 1.2 is never referred to", want="warn")

    print("\n== Style faults")
    md_fault("style", "meta commentary about the report", m, lambda t: t + "\nThis report will now explain the metrics.\n", "meta commentary 'This report will'")
    md_fault("style", "pending benchmark result", m, lambda t: t + "\nThe planned run covers all datasets.\n", "meta commentary 'planned run'")
    md_fault("style", "US spelling (warning)", m, lambda t: t + "\nThe methods generalize poorly.\n", "US spelling", want="warn")
    md_fault("style", "quoted source keeps its spelling", m, lambda t: t + '\nThe authors wrote "methods that generalize poorly across datasets".\n', "US spelling", want="none")

    print("\n== Abbreviation faults")
    md_fault("abbreviations", "full form repeated", m, lambda t: t + "\nThe presentation attack detection field grows.\n", "REPEAT  PAD")
    md_fault("abbreviations", "official title holding a full form is not a repeat", m,
             lambda t: t + "\nThe Presentation Attack Detection Act applies.\n", "REPEAT  PAD", want="none")
    md_fault("abbreviations", "first use without definition", "01-00-theory-and-taxonomy.md",
             lambda t: t.replace("presentation attack detection (PAD)", "PAD", 1), "DEFINE  PAD")

    print("\n== Citation faults")
    md_fault("citations", "citation without entry", m, lambda t: t + "\nClaim [999].\n", "[999] has no entry")
    md_fault("citations", "first citation out of order", "01-00-theory-and-taxonomy.md",
             lambda t: t.replace("\n\n", "\n\nEarly mention [50].\n\n", 1), "is cited before")
    md_fault("citations", "entry never cited", refs, lambda t: t + "\n[112] Extra entry.\n", "[112] is never cited")
    md_fault("citations", "entry listed twice", refs, lambda t: t + "\n[111] Duplicate.\n", "listed more than once")
    md_fault("citations", "draft source ID left", m, lambda t: t + "\nClaim [S101, S102].\n", "draft citation [S101, S102]")

    print("\n== Word document faults")

    def drop_table_caption(doc):
        p = next(p for p in doc.paragraphs if p.style.style_id == "TableCaption")
        p._p.getparent().remove(p._p)

    def widen_image(doc):
        ext = max(doc.element.body.iter(qn("wp:extent")), key=lambda e: int(e.get("cx")))   # a figure, not the logo
        ext.set("cx", str(int(ext.get("cx")) * 2))

    def drop_toc(doc):
        for it in doc.element.body.iter(qn("w:instrText")):
            if it.text and "TOC \\o" in it.text:
                it.text = " HYPERLINK x "

    def drop_header_row(doc):
        tr = list(doc.element.body.iter(qn("w:tbl")))[-1].find(qn("w:tr"))
        for el in tr.iter(qn("w:tblHeader")):
            el.getparent().remove(el)

    def rename_heading(doc):
        h = next(p for p in doc.paragraphs if p.style.style_id == "Heading2")
        h.runs[-1].text += " changed"

    docx_fault("table caption missing", drop_table_caption, "captions: Word has")
    docx_fault("markdown leftover", lambda d: body_para(d).add_run(" **bold**"), "markdown leftover '**'")
    docx_fault("image wider than the page", widen_image, "text area")
    docx_fault("contents field missing", drop_toc, "table of contents field")
    docx_fault("table without repeating header", drop_header_row, "no repeating header row")
    docx_fault("wrong title metadata", lambda d: setattr(d.core_properties, "title", "Other"), "core property title")
    docx_fault("em dash", lambda d: body_para(d).add_run(" a — b"), "em dash in")
    docx_fault("citation beyond the list", lambda d: body_para(d).add_run(" [999]"), "beyond the")
    docx_fault("heading text changed", rename_heading, "text differs")
    docx_fault("placeholder (warning)", lambda d: body_para(d).add_run(" [Course name]"), "placeholder to fill", want="warn")

    print("\n== Translation: quick check, sync and gating")
    code, out = run("translation_status.py", "--report", REP.relative_to(ROOT), "--lang", "vi", "--mark-all")
    code, out = run(*CHECKS["translation"])
    expect("all twins present and recorded in sync", code == 0 and " 0 need translation" in out, out.strip().splitlines()[-1][:90])
    target = REP / "04-02-2-masking-that-teaches-structure.md"
    original = target.read_text(encoding="utf-8")
    target.touch()
    code, out = run(*CHECKS["translation"])
    expect("a newer file date alone keeps the twin in sync (content hash)", f"stale    {target.name}" not in out)
    target.write_text(original + "\nAn added sentence.\n", encoding="utf-8")
    code, out = run(*CHECKS["translation"])
    expect("changed source text marks the twin stale", code == 1 and f"stale    {target.name}" in out)
    target.write_text(original, encoding="utf-8")
    twin = REP / "04-03-how-fsfm-is-judged.vi.md"
    kept = twin.read_text(encoding="utf-8")
    twin.unlink()
    code, out = run("report.py", "translate", "selftest", "--lang", "vi")
    expect("translate lists the missing twin with the guide and glossary", code == 1 and "missing  04-03-how-fsfm-is-judged.md" in out
           and "guide.md" in out and "biometrics-and-pad.md" in out and "common/report-writing.md" in out)
    code, out = run("report.py", "build", "selftest", "--lang", "vi", "--no-figures")
    expect("build holds back a language with untranslated files", code == 1 and "still to translate" in out
           and not (DOCX.parent / "Test_VI.docx").exists())
    twin.write_text(kept, encoding="utf-8")
    extra = REP / "00-0a-loi-cam-on.vi.md"
    shutil.copy(SKILL / "languages" / "vi" / "templates" / extra.name, extra)
    base2 = baseline("parity")
    code, out = run(*CHECKS["translation"])
    code2, out2 = run(*CHECKS["parity"])
    expect("a Vietnamese-only page is neither an orphan nor a parity error", code == 0 and "only pages: 00-0a" in out
           and code2 == base2 and "only pages skipped" in out2 and extra.name not in out2.replace("only pages skipped", ""))
    extra.unlink()

    target_vi = REP / "04-03-how-fsfm-is-judged.vi.md"
    kept = target_vi.read_text(encoding="utf-8")
    target_vi.write_text(kept.replace("[102]", "[103]", 1), encoding="utf-8")
    code, out = run("translation_status.py", "--report", REP.relative_to(ROOT), "--lang", "vi", "--mark", "04-03-how-fsfm-is-judged.md")
    expect("--mark keeps a file open while its parity check fails", "kept open 04-03-how-fsfm-is-judged.md" in out)
    target_vi.write_text(kept, encoding="utf-8")
    code, out = run("report.py", "translate", "selftest", "--lang", "vi", "--add-extra", "00-0b-loi-cam-doan.vi.md")
    expect("--add-extra copies a Vietnamese-only page template", (REP / "00-0b-loi-cam-doan.vi.md").exists() and "added" in out)
    (REP / "00-0b-loi-cam-doan.vi.md").unlink()
    # split_export.py: a Google-Docs-style single-file export goes back into the report's file layout
    import re as _re
    parts = []
    for f in sorted(REP.glob("*.vi.md")):
        t = f.read_text(encoding="utf-8")
        t = _re.sub(r"^(#{1,6}) (\d+(?:\.\d+)*)\. (.*)$", lambda m: f"{m.group(1)} **{m.group(2).replace('.', chr(92) + '.')}. {m.group(3)}**", t, flags=_re.M)
        parts.append(_re.sub(r"\[(\d+)\]", lambda m: chr(92) + "[" + m.group(1) + chr(92) + "]", t))
    export = BASE / "export.vi.md"
    export.write_text("\n\n".join(parts), encoding="utf-8")
    split_out = BASE / "split"
    code, out = run("split_export.py", "--export", export.relative_to(ROOT), "--report", REP.relative_to(ROOT),
                    "--lang", "vi", "--out", split_out.relative_to(ROOT), "--force")
    n = len(list(REP.glob("*.vi.md")))                               # the title page comes from the text before the first heading
    expect("split_export: every section of an export finds its report file", code == 0 and f"{n} matched, 0 new" in out, out[-200:])
    sample = next(f for f in sorted(REP.glob("0[1-9]-*.vi.md")) if "[" in f.read_text(encoding="utf-8"))
    expect("split_export: headings and citations come back in source form",
           (split_out / sample.name).read_text(encoding="utf-8").split("\n")[0] == sample.read_text(encoding="utf-8").split("\n")[0]
           and chr(92) + "[" not in (split_out / sample.name).read_text(encoding="utf-8"))
    code, out = run("check_abbreviations.py", "--report", REP.relative_to(ROOT), "--lang", "en", "--candidates")
    expect("--candidates lists abbreviation-like tokens missing from the table", "not in table  FSFM" in out)

    # split_export.restore: what a Google Docs export loses comes back from the report's own file
    from split_export import restore
    for name in ("04-02-3-two-learning-signals.vi.md", "04-04-limitations-and-open-questions.vi.md"):
        src = (REP / name).read_text(encoding="utf-8")
        broken = _re.sub(r"```[^\n]*\n(.*?)\n```", r"\1", src, flags=_re.S)              # fences lost
        broken = _re.sub(r"(?m)^\((\d+)\) ", r"\1) ", broken)                            # "(1)" exported as "1)"
        broken = _re.sub(r"\b([LS])_(\d)", r"{\1}_{\2}", broken).replace(" \\cdot ", "\\cdot ")   # equation editor form
        expect(f"split_export: restores fences, list numbers and formulas ({name[:7]})",
               broken != src and restore(broken, src)[0] == src)

    fig_src = "Intro.\n\n![Hình 4.3. Mặt nạ](assets/figures/x.png){width=80%}\n\nNext.\n"
    fig_bad = fig_src.replace("80%", "100%").replace("\n\nNext", "\n\n*Hình 4.3. Mặt nạ*\n\nNext")
    expect("split_export: drops a caption repeated in italics and restores the figure width", restore(fig_bad, fig_src)[0] == fig_src)

    # build_docx table sizing: columns follow their content, not the page width
    from build_docx import TEXT_W_PORTRAIT, column_widths, is_landscape_table
    short = [["Method", "Train CASIA-FASD, test Replay-Attack", "Train Replay-Attack, test CASIA-FASD"],
             ["Motion", "50.2%", "47.9%"], ["LBP", "55.9%", "57.6%"], ["LBP-TOP", "49.7%", "60.6%"]]
    w = column_widths(short, TEXT_W_PORTRAIT, 9.5)
    expect("tables: a short table takes its natural width, not the page width", sum(w) < 0.8 * TEXT_W_PORTRAIT and w[1] == w[2] >= w[0])
    scores = [["Method", "Year and venue", "O&C&I→M", "O&M&I→C", "O&C&M→I", "I&C&M→O", "Average"],
              ["MADDG [53]", "CVPR 2019", "17.69", "24.50", "22.19", "27.98", "23.09 (computed)"],
              ["SSDG-R [74], [51]", "CVPR 2020", "7.38", "10.44", "11.71", "15.61", "11.28"]]
    class _T:                                                     # the cell texts are all is_landscape_table reads
        def __init__(self, rows): self.rows = [type("R", (), {"cells": [type("C", (), {"text": c, "paragraphs": []}) for c in r]}) for r in rows]
    w = column_widths(scores, TEXT_W_PORTRAIT, 9.5)
    expect("tables: seven short columns stay on a portrait page with readable number columns",
           not is_landscape_table(_T(scores)) and min(w[2:6]) > 0.1 * TEXT_W_PORTRAIT and max(w) < 0.25 * TEXT_W_PORTRAIT)

    url = "https://research.example.edu/groups/data-mining/resources/open-datasets/index.aspx"
    prose = "A long reason that needs a real column to stay readable, with several clauses in it."
    log = [["Date", "Source", "URL", "Reason", "Result"]] + [["2026-11-06", "Search engine", url, prose, prose]] * 6
    w = column_widths(log, TEXT_W_PORTRAIT, 8.5)
    expect("tables: a long URL wraps in its cell and leaves the width to the text columns",
           w[3] > 0.2 * TEXT_W_PORTRAIT and w[4] > 0.2 * TEXT_W_PORTRAIT and w[2] < 0.4 * TEXT_W_PORTRAIT, str(w))
    from table_layout import text_pt
    caps = [["ID", "A long heading for the text column"], *[["AQ1", "word " * 60]] * 3]
    expect("tables: a column of capitals fits its printed width, wider than an average character",
           column_widths(caps, TEXT_W_PORTRAIT, 9.5)[0] / 12700 - 8 > text_pt("AQ1", 9.5))

    from table_layout import ZWSP, soft_break
    links = ["https://research.example.ac.uk/groups/data-mining/resources/open-datasets/index.aspx",
             "doi:10.34740/kaggle/dsv/15256262/and/some/more/path/to/make/it/long/enough/for/the/check",
             "core.ac.uk/download/1534442540000000000000000000000000000000000000000000.pdf",
             "data-mining.a-very-long-example-domain-name-for-the-check-of-bare-domains.com"]
    expect("tables: a URL or a DOI keeps no hidden characters, so a copied link works",
           not any(ZWSP in soft_break(u, 8.5) for u in links))
    expect("tables: a long identifier still gets break points",
           ZWSP in soft_break("studentRegistration_table.date_registration_of_the_student_record_field", 8.5))

    # apply_fixes.py: FIND/REPLACE blocks apply exactly once or not at all
    target = REP / "01-01-2-evaluation-metrics.vi.md"
    saved_t = target.read_text(encoding="utf-8")
    fixes = BASE / "fixes.md"
    first_line = next(x for x in saved_t.splitlines() if x.startswith("#"))
    fixes.write_text(f"### Fix X1 – {target.name}\nFIND: {first_line}\nREPLACE: {first_line} (sửa)\n\n"
                     f"### Fix X2 – {target.name}\nFIND: chuỗi không có trong tệp\nREPLACE: x\n", encoding="utf-8")
    code, out = run("apply_fixes.py", "--report", REP.relative_to(ROOT), "--fixes", fixes.relative_to(ROOT), "--write")
    changed = target.read_text(encoding="utf-8")
    target.write_text(saved_t, encoding="utf-8")
    expect("apply_fixes: a matching block applies, a missing FIND fails the run",
           code == 1 and "ok    X1" in out and "FIND occurs 0 times" in out and f"{first_line} (sửa)" in changed)

    # renumber_refs.py: a reference cited out of order (a reviewer's new source cited early) is renumbered
    saved = {p: p.read_text(encoding="utf-8") for p in REP.glob("*.vi.md")}
    first = next(p for p in sorted(REP.glob("01-*.vi.md")) if "[1]" in saved[p])
    last = max(int(x) for x in _re.findall(r"(?m)^\[(\d+)\]", next(t for p, t in saved.items() if "references" in p.name)))
    first.write_text(saved[first].replace("[1]", f"[{last}] [1]", 1), encoding="utf-8")
    code, out = run("check_citations.py", "--report", REP.relative_to(ROOT), "--lang", "vi")
    expect("citations: a new source cited early breaks first-citation order", code == 1 and f"[{last}] is cited before" in out)
    code, out = run("renumber_refs.py", "--report", REP.relative_to(ROOT), "--lang", "vi", "--write")
    code2, out2 = run("check_citations.py", "--report", REP.relative_to(ROOT), "--lang", "vi")
    for p, t in saved.items():
        p.write_text(t, encoding="utf-8")
    expect("renumber_refs: renumbers by first citation and the order check passes",
           code == 0 and f"[{last}] → [1]" in out and code2 == 0 and f"{last} references" in out2, out2.strip()[:90])

    print("\n== Translation: parity and Vietnamese conventions")
    mim, crfr, circ = "04-02-3-two-learning-signals.vi.md", "04-04-limitations-and-open-questions.vi.md", "03-04-1-banking-circulars.vi.md"
    md_fault("parity", "dropped citation", mim, lambda t: re.sub(r"\s?\[\d+\]", "", t, count=1), "citation sequence differs")
    md_fault("parity", "reordered citations", mim, lambda t: t.replace("[102]", "[103]", 1), "citation sequence differs")
    md_fault("parity", "altered formula", mim, lambda t: t.replace("0.007 \\cdot L_2", "0,007 \\cdot L_2", 1), "math differs")
    md_fault("parity", "dropped list item", crfr, lambda t: re.sub(r"(?m)^\(\d+\) .*\n", "", t, count=1), "list item count differ")
    md_fault("parity", "list written '1.'", crfr, lambda t: t.replace("(1) **Phép", "1. **Phép"), "ordered list written '1.'")
    md_fault("parity", "dropped table row", circ, lambda t: re.sub(r"(?m)^\| Thông tư 18/2024.*\n", "", t), "table shapes")
    md_fault("parity", "changed heading number", mim, lambda t: t.replace("### 4.2.3.", "### 4.2.5.", 1), "heading number differs")
    md_fault("parity", "em dash", mim, lambda t: t.replace(". ", " — ", 1), "em dash")
    md_fault("parity", "decimal point in prose", crfr, lambda t: t + "\nNgưỡng tin cậy là 0.85 trong thử nghiệm.\n", "decimal point '0.85'")
    md_fault("parity", "decimal point in a table", crfr, lambda t: t.replace("| Cách học |", "| Cách học 74.19 |"), "decimal point '74.19'")
    md_fault("parity", "glossary variant", circ, lambda t: t + "\nĐây là một tấn công thuyết trình điển hình.\n", "glossary 'tấn công thuyết trình'")
    md_fault("parity", "common-layer variant (glossary Replaces)", circ, lambda t: t + "\nĐây là điểm yếu của phương pháp.\n", "glossary 'điểm yếu'")
    code, out = run("glossary.py", "--lang", "vi", "lint")
    expect("glossary lint: every layer consistent", code == 0, out.strip().splitlines()[-1])
    gdir = SKILL / "languages" / "vi" / "glossaries" / "topics"
    bad = gdir / "zz-selftest.md"
    bad.write_text("# t\n\n| English | Vietnamese | Usage | Replaces |\n| --- | --- | --- | --- |\n| weakness | điểm yếu | | điểm hạn chế |\n")
    code, out = run("glossary.py", "--lang", "vi", "lint")
    bad.unlink()
    expect("glossary lint: a variant that is a preferred form elsewhere", code == 1 and "is a preferred form" in out)
    big = gdir / "zz-selftest-big.md"                       # size budget: an overgrown file is split by its sections
    rows = lambda tag, n: "".join(f"| {tag} term {i} | thuật ngữ {tag} {i} | | |\n" for i in range(n))
    head = "| English | Vietnamese | Usage | Replaces |\n| --- | --- | --- | --- |\n"
    big.write_text("# Big\n\nTerms of the self-test.\n\n## Alpha\n\n" + head + rows("alpha", 90)
                   + "\n## Beta\n\n" + head + rows("beta", 90), encoding="utf-8")
    cfg_text = CONFIG.read_text(encoding="utf-8")
    CONFIG.write_text(cfg_text.replace('glossaries = ["biometrics-and-pad", "digital-banking-vn"]',
                                       'glossaries = ["biometrics-and-pad", "digital-banking-vn", "zz-selftest-big"]'),
                      encoding="utf-8")
    snap = BASE / "glossary-snapshot.json"
    try:
        code, out = run("glossary.py", "--lang", "vi", "lint")
        expect("glossary lint: a file above the row budget gets a split suggestion",
               code == 0 and "WARN  topics/zz-selftest-big.md holds 180 rows" in out and "split topics/zz-selftest-big.md" in out)
        code, out = run("glossary.py", "--lang", "vi", "sizes")
        expect("glossary sizes: lists rows and sections per file", "topics/zz-selftest-big.md" in out and "above budget" in out)
        run("glossary.py", "--lang", "vi", "snapshot", "save", str(snap))
        code, out = run("glossary.py", "--lang", "vi", "split", "topics/zz-selftest-big.md")
        part = gdir / "zz-selftest-big-beta.md"
        expect("glossary split: one file per section, tasks.toml lists both, merged glossary unchanged",
               code == 0 and part.exists() and len(_rows(big)) == 90 and len(_rows(part)) == 90
               and '"zz-selftest-big", "zz-selftest-big-beta"' in CONFIG.read_text(encoding="utf-8"), out[-200:])
        code, out = run("glossary.py", "--lang", "vi", "snapshot", "compare", str(snap))
        expect("glossary snapshot: unchanged after the split", code == 0 and "0 differences" in out, out[-120:])
        part.write_text(part.read_text(encoding="utf-8").replace("thuật ngữ beta 3 |", "thuật ngữ khác |"), encoding="utf-8")
        code, out = run("glossary.py", "--lang", "vi", "snapshot", "compare", str(snap))
        expect("glossary snapshot: a changed row is reported", code == 1 and "thuật ngữ khác" in out, out[-120:])
        big.write_text("# One\n\n" + head + rows("solo", 3), encoding="utf-8")
        code, out = run("glossary.py", "--lang", "vi", "split", "topics/zz-selftest-big.md")
        expect("glossary split: a file without sections is left as it is", code != 0 and "group its rows under sections" in out)
    finally:
        for f in gdir.glob("zz-selftest-big*.md"):
            f.unlink()
        CONFIG.write_text(cfg_text, encoding="utf-8")
    md_fault("parity", "old tone placement (warning)", circ, lambda t: t + "\nQuá trình chuẩn hoá dữ liệu.\n", "old-style tone placement", want="warn")
    md_fault("parity", "two plural markers (warning)", circ, lambda t: t + "\nCác những tổ chức tín dụng tham gia.\n", "two plural markers", want="warn")
    md_fault("parity", "calque 'đóng một vai trò' (warning)", circ, lambda t: t + "\nNgân hàng đóng một vai trò quan trọng.\n", "calque", want="warn")
    md_fault("parity", "spoken sentence opener (warning)", circ, lambda t: t + "\nHệ thống chạy ổn định. Nhưng chi phí cao.\n", "spoken sentence opener", want="warn")
    md_fault("parity", "three stacked passives (warning)", circ, lambda t: t + "\nDữ liệu được thu thập, được làm sạch và được lưu trữ.\n", "three 'được'", want="warn")
    md_fault("parity", "comma before 'và' (warning, human review)", circ, lambda t: t + "\nNgân hàng kiểm tra hồ sơ, và hệ thống ghi nhận kết quả.\n", "comma before 'và'", want="warn")
    md_fault("parity", "possessive pronoun (warning, human review)", circ, lambda t: t + "\nPhạm vi của nó gồm ba phần.\n", "possessive pronoun", want="warn")
    md_fault("parity", "English loanword (warning, human review)", circ, lambda t: t + "\nMô hình được huấn luyện trên một dataset lớn.\n", "English loanword", want="warn")
    md_fault("parity", "one-digit date (warning, human review)", circ, lambda t: t + "\nTiêu chuẩn được công bố ngày 2/10/2026.\n", "one-digit day or month", want="warn")
    gl, gl_en = REP / "00-2-glossary.vi.md", REP / "00-2-glossary.md"
    original = gl.read_text(encoding="utf-8")
    code, out = run("check_parity.py", "--report", REP.relative_to(ROOT), "--lang", "vi", gl_en)
    expect("parity: terms page row opening with the Vietnamese name (warning, human review)", "terms page row 1:" in out)
    gl.write_text(original.replace("| Tiềm năng tấn công (attack potential) |", "| Attack potential – Tiềm năng tấn công |"),
                  encoding="utf-8")
    code, out = run("check_parity.py", "--report", REP.relative_to(ROOT), "--lang", "vi", gl_en)
    gl.write_text(original, encoding="utf-8")
    expect("parity: terms page row 'English term – Vietnamese name' passes", "terms page row 1:" not in out)
    md_fault("parity", "label starting with 'là' (warning)", circ, lambda t: t + "\nlà mức giảm số vụ lừa đảo.\n",
             "line starts with 'là'", want="warn")
    from pptx import Presentation as _Deck                  # slide text written as '·'-joined fragments
    deck = _Deck()
    slide = deck.slides.add_slide(deck.slide_layouts[6])
    box = slide.shapes.add_textbox(0, 0, 3000000, 600000)
    box.text_frame.text = "Ảnh từ camera thông thường · không cần phần cứng mới · tổng quát hóa kém"
    deck_path = BASE / "fragments.pptx"
    deck.save(str(deck_path))
    code, out = run("check_slides.py", deck_path.relative_to(ROOT), "--lang", "vi")
    expect("slides: '·'-joined fragments (warning)", "keyword fragments joined with" in out)
    narrow = _Deck()
    tb = narrow.slides.add_slide(narrow.slide_layouts[6]).shapes.add_textbox(Inches(1), Inches(1), Inches(0.45), Inches(0.4))
    tb.text_frame.word_wrap = True
    tb.text_frame.margin_left = tb.text_frame.margin_right = Inches(0.05)
    tb.text_frame.text = "2002"
    tb.text_frame.paragraphs[0].runs[0].font.size = Pt(14)
    narrow_path = BASE / "narrow.pptx"
    narrow.save(str(narrow_path))
    code, out = run("check_slides.py", narrow_path.relative_to(ROOT), "--lang", "vi")
    expect("slides: a word wider than its box is reported (warning)", "word wider than its box" in out)
    numbered = _Deck()
    nb = numbered.slides.add_slide(numbered.slide_layouts[6]).shapes.add_textbox(Inches(9), Inches(7), Inches(1), Inches(0.28))
    nb.text_frame.text = "12"
    nb.text_frame.paragraphs[0].runs[0].font.size = Pt(10)
    from docx.oxml.ns import qn as _qn                          # same namespace map for DrawingML
    r = nb.text_frame.paragraphs[0]._p.find(_qn("a:r"))
    fld = r.makeelement(_qn("a:fld"), {"id": "{00000000-0000-0000-0000-000000000001}", "type": "slidenum"})
    for child in list(r):
        fld.append(child)
    r.addprevious(fld); r.getparent().remove(r)
    numbered_path = BASE / "numbered.pptx"
    numbered.save(str(numbered_path))
    code, out = run("check_slides.py", numbered_path.relative_to(ROOT), "--lang", "vi")
    expect("slides: a slide-number field is read at its own size", "taller than its box" not in out, out.strip()[-80:])
    md_fault("parity", "kept English quotation is not flagged", crfr,
             lambda t: t + '\nNhóm tác giả viết "the masked patches of the covered region are reconstructed from the rest of the face".\n',
             "looks untranslated", want="none")
    md_fault("parity", "untranslated sentence outside quotes (warning)", crfr,
             lambda t: t + "\nThe authors argue that the masked region is reconstructed from the rest of the face and that this is useful.\n",
             "looks untranslated", want="warn")
    md_fault("parity", "version, standard and section numbers keep their dots", crfr,
             lambda t: t + "\nTheo ISO/IEC 30107-3:2023, phiên bản 4.1 và Mục 3.1 đến 3.3, giấy phép CC BY-NC 4.0.\n",
             "decimal point", want="none")
    md_fault("parity", "model names, product versions, DOIs and arXiv IDs keep their dots", crfr,
             lambda t: t + "\nMô hình Llama 3.1-8B và Llama 3.3 chạy trên OpenRefine 3.9, DOI 10.18653/v1/2025.x, arXiv 2412.06724.\n",
             "decimal point", want="none")

    kitdir = BASE / "kitdeck"                               # the slide kit: a small deck in both languages
    kitdir.mkdir()
    (kitdir / "kit_deck_vi.py").write_text('VI = {"Kit Test Footer": "Chân trang thử", "Part 1 · Method": '
                                           '"Phần 1 · Phương pháp", "The Loop": "Vòng lặp", "(~30 seconds) Notes.": '
                                           '"(~30 giây) Ghi chú.", "The loop runs one step at a time": '
                                           '"Vòng lặp chạy từng bước một", "Input": "Đầu vào", "Agent": "Tác tử", '
                                           '"plans a step": "lập kế hoạch một bước", "Result": "Kết quả", '
                                           '"Score": "Điểm", "Source: test data.": "Nguồn: dữ liệu thử."}\n',
                                           encoding="utf-8")
    (kitdir / "kit_deck.py").write_text(f'''import sys
sys.path.insert(0, {str(SCRIPTS)!r})
import slidekit as kit
from slidekit import T, D, lead, flow_row, chart, clean_axes, foot, cards_at, PT
kit.use_strings("kit_deck_vi")
OUT = {{"en": {str(kitdir / "en.pptx")!r}, "vi": {str(kitdir / "vi.pptx")!r}}}
FULL = len(sys.argv) > 1 and sys.argv[1] == "overflow"

def s_loop(prs):
    s = kit.base(prs, T("Part 1 · Method"), T("The Loop"), T("(~30 seconds) Notes."))
    y = lead(s, T("The loop runs one step at a time"))
    flow_row(s, y, 1.4, [(T("Input"), None, "input"), (T("Agent"), T("plans a step"), "agent"),
                         (T("Result"), None, "out")])
    def draw(fig):
        ax = fig.add_axes([0.05, 0.2, 0.9, 0.7])
        ax.bar([0, 1], [0.5, 0.75])
        ax.set_xticks([0, 1], [T("Score"), D(0.75)])
        clean_axes(ax)
    chart(s, "kit", 0.5, y + 1.7, 4, 2.5, draw)
    if FULL:
        cards_at(s, [(T("Score"), T("Source: test data.") * 30)] * 6, 3, y + 1.7, bottom=y + 2.0)
    foot(s, T("Source: test data."))

SLIDES = [s_loop]

def build(lang):
    kit.build_deck(lang, SLIDES, OUT[lang], "Kit Test Footer", cache={str(kitdir)!r})

if __name__ == "__main__":
    for code in ("en", "vi"):
        build(code)
''', encoding="utf-8")
    proc = subprocess.run([PY, str(kitdir / "kit_deck.py")], cwd=ROOT, capture_output=True, text=True)
    built = (kitdir / "en.pptx").exists() and (kitdir / "vi.pptx").exists()
    expect("slidekit: a deck builds in English and Vietnamese with no missing strings",
           proc.returncode == 0 and built and "without a Vietnamese form" not in proc.stdout, proc.stderr[-200:])
    if built:
        from pptx import Presentation as _P
        vi = _P(str(kitdir / "vi.pptx")).slides[0]
        texts = [sh.text_frame.text for sh in vi.shapes if sh.has_text_frame]
        expect("slidekit: Vietnamese text, footer and slide-number field are in place",
               "Vòng lặp" in texts and "Chân trang thử" in texts and (kitdir / "kit-vi.png").exists())
        code, out = run("check_slides.py", (kitdir / "vi.pptx").relative_to(ROOT), "--lang", "vi")
        expect("slidekit: the built Vietnamese deck passes check_slides", code == 0 and "0 errors" in out, out[-200:])
        code, out = run("slidekit.py", "text", (kitdir / "vi.pptx").relative_to(ROOT))
        expect("slidekit text: slides and notes as plain text", "=== Slide 1" in out and "(~30 giây) Ghi chú." in out)
        code, out = run("slidekit.py", "text", (kitdir / "vi.pptx").relative_to(ROOT), "--slides-only")
        expect("slidekit text --slides-only: the slide text without the notes (the slide-only reading pass)",
               "=== Slide 1" in out and "Ghi chú." not in out and "[Notes]" not in out)
    vi_mod = kitdir / "kit_deck_vi.py"
    vi_src = vi_mod.read_text(encoding="utf-8")
    vi_mod.write_text(vi_src.replace('"Agent": "Tác tử", ', ""), encoding="utf-8")
    code, out = run("slidekit.py", "strings", (kitdir / "kit_deck.py").relative_to(ROOT))
    vi_mod.write_text(vi_src, encoding="utf-8")
    expect("slidekit strings: lists exactly the English string without a Vietnamese form", '"Agent"' in out
           and out.count('\n "') == 1, out[-200:])
    proc = subprocess.run([PY, str(kitdir / "kit_deck.py"), "overflow"], cwd=ROOT, capture_output=True, text=True)
    expect("slidekit: content that does not fit at the fixed type scale is reported", "! en cards: needs" in proc.stderr)
    deck_src = (kitdir / "kit_deck.py").read_text(encoding="utf-8")       # sync: an English string changes
    (kitdir / "kit_deck.py").write_text(deck_src.replace('T("The loop runs one step at a time")',
                                                         'T("The loop runs one small step at a time")'), encoding="utf-8")
    code, out = run("slidekit.py", "sync", (kitdir / "kit_deck.py").relative_to(ROOT))
    expect("slidekit sync: a changed English string is paired with the key it replaces", "RENAME" in out
           and "one small step" in out, out[-160:])
    code, out = run("slidekit.py", "sync", (kitdir / "kit_deck.py").relative_to(ROOT), "--write")
    renamed = "one small step at a time" in vi_mod.read_text(encoding="utf-8")
    code, out = run("slidekit.py", "strings", (kitdir / "kit_deck.py").relative_to(ROOT))
    expect("slidekit sync --write: the key is renamed and its value kept", renamed and out.strip() == "[]", out[-120:])
    (kitdir / "kit_deck.py").write_text(deck_src, encoding="utf-8")
    vi_mod.write_text(vi_src, encoding="utf-8")
    if built:
        code, out = run("slidekit.py", "diff", (kitdir / "en.pptx").relative_to(ROOT), (kitdir / "en.pptx").relative_to(ROOT))
        same = code == 0 and "0 differ" in out
        code, out = run("slidekit.py", "diff", (kitdir / "en.pptx").relative_to(ROOT), (kitdir / "vi.pptx").relative_to(ROOT))
        expect("slidekit diff: equal decks pass, different decks fail", same and code == 1)
    code, out = run("slidekit.py", "prompt", "translate", (kitdir / "kit_deck.py").relative_to(ROOT), "--task", "selftest",
                    "--voice", "group", "--scratch", (kitdir / "prompt").relative_to(ROOT))
    expect("slidekit prompt: translator prompt filled with the voice, the strings file and the pack's language",
           code == 0 and "nhóm chúng em" in out and "strings.json" in out and "Vietnamese" in out
           and not re.search(r"\{[a-z_]{2,}\}", out), out[-160:])
    example = BASE / "example"                               # the example deck of slides.md section 6
    proc = subprocess.run([PY, str(SKILL / "templates" / "deck" / "example_deck.py"), "--out", str(example)],
                          cwd=ROOT, capture_output=True, text=True)
    code, out = run("check_slides.py", example / "Example_EN.pptx", "--lang", "en")
    expect("example deck: builds on the current kit and passes check_slides with 0 warnings",
           proc.returncode == 0 and code == 0 and "0 errors, 0 warnings" in out, (proc.stderr + out)[-200:])
    gal = subprocess.run([PY, str(SCRIPTS / "gallery.py"), str(BASE / "gallery")], cwd=ROOT, capture_output=True,
                         text=True)                          # the visual kit: every visual draws cleanly
    expect("visual kit: the gallery draws every chart, diagram and icon with 0 layout findings",
           gal.returncode == 0 and "0 layout findings" in gal.stdout and (BASE / "gallery" / "gallery.png").exists(),
           (gal.stdout + gal.stderr)[-300:])
    native = BASE / "gallery" / "gallery-native.pptx"
    code, out = run("check_slides.py", native, "--lang", "en")
    code2, text_out = run("slidekit.py", "text", native)
    expect("visual kit: diagrams drawn natively pass check_slides, and their grouped text is visible to the checks",
           code == 0 and "0 errors, 0 warnings" in out and "Artefact" in text_out and "Look-alike" in text_out,
           out[-160:])
    import charts as ch_
    import figqa as qa_
    import palette as pal_
    import matplotlib.pyplot as plt_

    def lum(c):
        ch = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        ch = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
    expect("palette: every series and state colour reaches 3:1 on white; white text is chosen on a series fill",
           all(1.05 / (lum(c) + 0.05) >= 3 for c in pal_.SERIES + list(pal_.STATUS.values()))
           and pal_.text_on(pal_.ORANGE) == "#FFFFFF" and pal_.text_on(pal_.tint(pal_.BLUE)) == pal_.INK)
    ch_.use("report", "vi")
    vi_nums = (ch_.num(0.75), ch_.num(1250), ch_.num(4.81, pct=True))
    ch_.use("report", "en")
    expect("charts: numbers follow the language (0,75 / 1.250 / 4,81% in Vietnamese)",
           vi_nums == ("0,75", "1.250", "4,81%") and ch_.num(1250) == "1,250", str(vi_nums))
    faults = {}
    for kind in ("overlap", "crossed", "small", "cut off"):
        f = plt_.figure(figsize=(4, 2))
        ax = f.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 2)
        ax.axis("off")
        if kind == "overlap":
            ax.text(1, 1, "first label", fontsize=9)
            ax.text(1.1, 1.02, "second label", fontsize=9)
        elif kind == "crossed":
            ax.plot([0.5, 3.5], [1.05, 1.05], color="k")
            ax.text(1.5, 1, "label on a line", fontsize=9, va="bottom")
            ax.text(1.5, 1.1, "x", fontsize=1)
        elif kind == "small":
            ax.text(1, 1, "tiny text", fontsize=4)
        else:
            ax.text(3.7, 1, "runs past the edge", fontsize=9)
        ax.text(0.05, 0.1, ".", fontsize=8)
        ax.text(3.9, 1.9, ".", fontsize=8)
        faults[kind] = any(i.startswith(kind) for i in qa_.check(f))
        plt_.close(f)
    expect("figqa: overlapping, crossed, small and cut-off labels are each reported", all(faults.values()), str(faults))
    fresh = BASE / "fresh"                                   # init: a new project builds its starter report
    fresh.mkdir()
    env = {**os.environ, "BUILD_REPORT_ROOT": str(fresh)}
    env.pop("BUILD_REPORT_CONFIG", None)
    report_py = [PY, str(SCRIPTS / "report.py")]
    first = subprocess.run(report_py + ["init", "demo", "--title", "Demo Report"], cwd=fresh, capture_output=True,
                           text=True, env=env)
    again = subprocess.run(report_py + ["init", "demo"], cwd=fresh, capture_output=True, text=True, env=env)
    built = subprocess.run(report_py + ["all", "demo"], cwd=fresh, capture_output=True, text=True, env=env)
    expect("init: tasks.toml, Makefile and starter report; a second init keeps them; the task passes every step",
           first.returncode == 0 and (fresh / "Makefile").exists() and "kept" in again.stdout
           and built.returncode == 0 and (fresh / "build" / "demo" / "Report_EN.docx").exists(),
           (first.stdout + built.stdout)[-300:])
    voice = _Deck()                                        # who speaks: a slides-only warning
    vb = voice.slides.add_slide(voice.slide_layouts[6]).shapes.add_textbox(Inches(1), Inches(1), Inches(8), Inches(1))
    vb.text_frame.text = "Theo nhóm, đây là yếu tố quan trọng nhất."
    voice.slides[0].notes_slide.notes_text_frame.text = "Theo nhóm chúng em, nhóm tác giả đánh giá quá cao kết quả."
    voice_path = BASE / "voice.pptx"
    voice.save(str(voice_path))
    code, out = run("check_slides.py", voice_path.relative_to(ROOT), "--lang", "vi")
    expect("slides: a bare 'nhóm' as speaker warns once; 'nhóm chúng em' and 'nhóm tác giả' pass",
           out.count("bare 'nhóm'") == 1, out[-160:])
    md_fault("parity", "a bare 'nhóm' in a report is left to the writers (slides-only warning)", circ,
             lambda t: t + "\nTheo nhóm, đây là yếu tố quan trọng nhất.\n", "bare 'nhóm'", want="none")
    names_dir = BASE / "names"                               # names: a near-miss of a listed name is an error
    names_dir.mkdir()
    names_cfg = BASE / "names.toml"
    names_cfg.write_text(f'[selftest]\nreport = "{names_dir.relative_to(ROOT)}"\npeople = ["Phạm Thị Bạch Huệ"]\n',
                         encoding="utf-8")
    page = names_dir / "00-0-title-page.vi.md"
    page_src = "Giảng viên giảng dạy và hướng dẫn:\n"
    page.write_text(page_src + "\nTS. Phạm Thị Bạch Huệ\n", encoding="utf-8")
    code, out = run("check_names.py", "--task", "selftest", "--config", names_cfg)
    exact = code == 0
    page.write_text(page_src + "\nTS. Phạm Thị Bích Huệ\n", encoding="utf-8")
    code, out = run("check_names.py", "--task", "selftest", "--config", names_cfg)
    page.write_text(page_src, encoding="utf-8")
    expect("names: the exact name passes, a near-miss ('Bích' for 'Bạch') is an error", exact and code == 1
           and "looks like 'Phạm Thị Bạch Huệ'" in out, out[-160:])

    import glossary as _g                                   # coverage: one concept under several names is found
    rows = [dict(en="selector / judge", vi="bộ chọn", layer="topics", file="t.md")]
    english = "The selector compares two queries. The judge is fine-tuned. The judge returns A or B."
    drifted = _g.coverage(rows, english, "Bộ đánh giá so sánh hai truy vấn. Bộ đánh giá được tinh chỉnh. Bộ đánh giá trả về A.")
    aligned = _g.coverage(rows, english, "Bộ chọn so sánh hai truy vấn. Bộ chọn được tinh chỉnh. Bộ chọn trả về A hoặc B.")
    expect("glossary coverage: a concept under another name drifts, the glossary's one term passes",
           len(drifted) == 1 and drifted[0]["en"] == 3 and not aligned)
    code, out = run("glossary.py", "--lang", "vi", "--names", "biometrics-and-pad,digital-banking-vn", "coverage",
                    "--report", REP.relative_to(ROOT))
    expect("glossary coverage: runs over a report and reports its count", code == 0 and "task terms:" in out, out[-120:])

    import build_docx                                       # the pack's [docx] layout reaches the Word styles
    import pypandoc
    ref = BASE / "layout-ref.docx"
    build_docx.build_reference(ref, pypandoc.get_pandoc_path(), "vi-VN", {"body_size": 13, "line_spacing": 1.4})
    st = Document(str(ref)).styles["Body Text"]
    expect("pack [docx] layout: 13 pt body, 1.4 line spacing", st.font.size.pt == 13 and st.paragraph_format.line_spacing == 1.4)

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
