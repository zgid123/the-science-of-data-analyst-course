"""Self-test of the research-report skill: gates on good and broken fixtures, fetch conversion, scaffold, ledger.

Usage: ./venv/bin/python .claude/skills/research-report/scripts/selftest.py [--online]
       (fixtures in build/.cache/research_selftest/; --online also walks the live fetch ladder on two known sources)
"""

import shutil
import subprocess
import sys
import zlib
from pathlib import Path

import fetch
from common import ROOT, SKILL

PY = str(ROOT / "venv" / "bin" / "python")
HERE = ROOT / "build" / ".cache" / "research_selftest"
SCRIPTS = SKILL / "scripts"
results = []

CRAWL = """---
id: S101
url: https://example.org/iso
fetched: 2026-10-02T10:00+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T05
part: 1
---
A presentation attack is the presentation to the biometric data capture subsystem with the goal of
interfering with the operation of the biometric system.
"""
COMP = """# S101 – Demo standard

## Summary in my own words
Defines presentation attacks.

## Key facts
- "presentation to the biometric data capture subsystem with the goal of interfering"

## Used in
01-01-1-x.md

## Against reference.md
Confirms.

## Reliability
Primary.

## Open questions
None.
"""
SOURCES = """# Source Register

| ID | Folder slug | Source | URL | Outline item | Primary/secondary | Status | APA 7 entry |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| S101 | demo | Demo standard | https://example.org/iso | 1 | primary | fetched | Demo, A. (2026). *Demo standard*. Example. |
"""
CLAIMS = """# Part 1 Claims

| Claim ID | Claim | Exact value or quote anchor | Source ID | Primary or secondary | Report file(s) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C1-001 | PA definition | "the goal of interfering with the operation of the biometric system" | S101 | primary | 01-01-1-x.md |
"""
LOG = """| # | Task | Date | Query | Kept | Dropped |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | T05 | 2026-10-02 | iso 30107 definition | S101 | none |
"""
BODY = ("### 1.1.1. X\n\nA presentation attack is meant to interfere with the operation of the biometric system "
        "at the capture device, which is why the definition centres on the presentation itself {cite}.\n")


def make(name, draft=True):
    base = HERE / name
    shutil.rmtree(base, ignore_errors=True)
    src = base / "research" / "sources" / "S101-demo"
    src.mkdir(parents=True)
    (src / "crawl.md").write_text(CRAWL)
    (src / "comprehension.md").write_text(COMP)
    (base / "research" / "sources.md").write_text(SOURCES + ("" if draft else "\n## Reference map\n\n| n | Source ID |\n| :---- | :---- |\n| 1 | S101 |\n"))
    (base / "research" / "part1-claims.md").write_text(CLAIMS)
    (base / "research" / "search-log.md").write_text(LOG)
    rep = base / "report"
    rep.mkdir()
    (rep / "01-01-1-x.md").write_text(BODY.format(cite="[S101]" if draft else "[1]"))
    (rep / "05-references.md").write_text("# References\n" if draft else "# References\n\n[1] Demo, A. (2026).\n")
    return base


def run(script, *args):
    r = subprocess.run([PY, str(SCRIPTS / script), *map(str, args)], capture_output=True, text=True, cwd=ROOT)
    return r.returncode, r.stdout + r.stderr


def expect(label, ok, detail=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {label}" + (f"  ({detail})" if detail else ""))


def gate(label, code_out, want_fail, needle=""):
    code, out = code_out
    first = next((ln for ln in out.splitlines() if ln.startswith(("ERROR", "WARN"))), "")
    expect(label, (code == 1) == want_fail and needle in out, first[:90] or f"exit {code}")


def minimal_pdf(text):
    content = zlib.compress(f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode())
    return (b"%PDF-1.4\n1 0 obj << /Length " + str(len(content)).encode() + b" /Filter /FlateDecode >>\nstream\n" + content
            + b"\nendstream\nendobj\ntrailer << >>\n%%EOF\n")


def main():
    online = "--online" in sys.argv
    print("== A. Trail gate (check_trail.py)")
    g = make("good")
    gate("good fixture: --task", run("check_trail.py", "--base", g, "--task", "T05"), False)
    gate("good fixture: --all", run("check_trail.py", "--base", g, "--all"), False)
    gate("good fixture: --part 1", run("check_trail.py", "--base", g, "--part", "1"), False)
    b = make("no_crawl"); (b / "research/sources/S101-demo/crawl.md").unlink()
    gate("missing crawl.md", run("check_trail.py", "--base", b, "--all"), True, "crawl.md missing")
    b = make("no_comp"); (b / "research/sources/S101-demo/comprehension.md").unlink()
    gate("missing comprehension.md", run("check_trail.py", "--base", b, "--all"), True, "comprehension.md missing")
    b = make("empty_heading"); p = b / "research/sources/S101-demo/comprehension.md"; p.write_text(p.read_text().replace("Primary.", ""))
    gate("empty comprehension heading", run("check_trail.py", "--base", b, "--all"), True, "'Reliability' missing or empty")
    b = make("bad_anchor"); p = b / "research/part1-claims.md"; p.write_text(p.read_text().replace("goal of interfering", "aim of disturbing"))
    gate("claim anchor not verbatim", run("check_trail.py", "--base", b, "--all"), True, "anchor not found verbatim")
    b = make("bad_quote"); p = b / "research/sources/S101-demo/comprehension.md"; p.write_text(p.read_text().replace("with the goal", "with the aim"))
    gate("comprehension quote not verbatim", run("check_trail.py", "--base", b, "--all"), True, "comprehension quote not found")
    b = make("orphan"); p = b / "research/part1-claims.md"; p.write_text(p.read_text().replace("| S101 | primary", "| S199 | primary"))
    gate("orphan claim", run("check_trail.py", "--base", b, "--part", "1"), True, "orphan claim")
    b = make("blocked"); p = b / "research/sources.md"; p.write_text(p.read_text().replace("| fetched |", "| blocked |"))
    gate("claim on a blocked source", run("check_trail.py", "--base", b, "--all"), True, "cannot support a claim")
    b = make("no_log"); (b / "research/search-log.md").write_text(LOG.replace("T05", "T07"))
    gate("task without search-log row", run("check_trail.py", "--base", b, "--task", "T05"), True, "no row for T05")
    b = make("status_mismatch"); p = b / "research/sources/S101-demo/crawl.md"; p.write_text(p.read_text().replace("status: ok", "status: partial"))
    gate("crawl/register status mismatch (warning)", run("check_trail.py", "--base", b, "--all"), False, "register status")
    b = make("escaped_pipe"); src = b / "research/sources/S101-demo/crawl.md"; src.write_text(src.read_text() + "| Motion | 50.2% | 47.9% |\n")
    p = b / "research/part1-claims.md"
    p.write_text(p.read_text().replace('"the goal of interfering with the operation of the biometric system"', '"\\| Motion \\| 50.2% \\| 47.9% \\|"'))
    gate("escaped pipe in an anchor matches", run("check_trail.py", "--base", b, "--all"), False)

    print("\n== B. Draft gate (check_drafts.py)")
    gate("good draft", run("check_drafts.py", "--base", g, "--words", "10-700"), False)
    b = make("unknown_s"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[S150]"))
    gate("unknown [Sxxx]", run("check_drafts.py", "--base", b), True, "not in sources.md")
    b = make("numeric"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[3]"))
    gate("numeric citation in a draft", run("check_drafts.py", "--base", b), True, "numeric citation")
    b = make("meta"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[S101]") + "\nIn this task we will explain the outline [S101].\n")
    gate("meta commentary", run("check_drafts.py", "--base", b), True, "meta commentary")
    gate("word count outside range (warning)", run("check_drafts.py", "--base", g, "--words", "200-700"), False, "words (expected")
    b = make("authors_merged"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[S101]")
        + "\n| Cue | Works |\n| :---- | :---- |\n| rPPG | Liu et al. 2016 and 2018 [S101] |\n")
    gate("one 'Surname et al.' over two years (warning)", run("check_drafts.py", "--base", b, "--words", "10-700"), False,
         "'Liu et al.' names works of 2016, 2018")
    b = make("authors_initials"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[S101]")
        + "\n| Cue | Works |\n| :---- | :---- |\n| rPPG | Liu S.-Q. et al. 2016; Liu Y. et al. 2018 [S101] |\n")
    code, out = run("check_drafts.py", "--base", b, "--words", "10-700")
    expect("authors with initials are told apart", code == 0 and "names works of" not in out)
    b = make("priority"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[S101]")
        + "\nThis is the first fully automated approach to cleaning tables for a purpose [S101].\n")
    gate("priority claim stated as the report's own (warning)", run("check_drafts.py", "--base", b, "--words", "10-700"),
         False, "priority claim")
    b = make("priority_attributed"); (b / "report/01-01-1-x.md").write_text(BODY.format(cite="[S101]")
        + "\nThe authors present it as the first fully automated approach, and the first agent selects columns [S101].\n")
    code, out = run("check_drafts.py", "--base", b, "--words", "10-700")
    expect("attributed priority claim and an ordinal 'first' pass quietly", code == 0 and "priority claim" not in out)
    b = make("own_material"); crawl = b / "research/sources/S101-demo/crawl.md"
    crawl.write_text(crawl.read_text().replace("tool:", "tool: local\nx-tool:", 1))
    gate("citing the authors' own material, fetched with fetch.py local (warning)",
         run("check_drafts.py", "--base", b, "--words", "10-700"), False, "authors' own material")

    print("\n== C. Finishing (finalize_refs.py, spot_check.py)")
    b = make("finalize")
    code, out = run("finalize_refs.py", "--base", b)
    body = (b / "report/01-01-1-x.md").read_text()
    refs = (b / "report/05-references.md").read_text()
    expect("finalize: [S101] → [1], reference list and map written",
           code == 0 and "[1]" in body and "[S101]" not in body and "[1] Demo, A." in refs
           and "| 1 | S101 |" in (b / "research/sources.md").read_text(), out.strip().splitlines()[-1][:90])
    gate("trail --all after finalize (reference map)", run("check_trail.py", "--base", b, "--all"), False)
    code, out = run("spot_check.py", "--base", b, "--n", "3", "--seed", "1")
    expect("spot-check traces [1] → S101 → C1-001 (found)", code == 0 and "S101" in out and "(found)" in out)
    b2 = make("finalize_missing_apa"); p = b2 / "research/sources.md"; p.write_text(p.read_text().replace("Demo, A. (2026). *Demo standard*. Example.", ""))
    code, out = run("finalize_refs.py", "--base", b2)
    expect("finalize refuses a source without APA entry", code != 0 and "without an APA entry" in out)

    print("\n== D. Fetch conversion and readability (offline)")
    prose = ("The presentation attack detection subsystem is evaluated with error rates that are reported for each "
             "attack instrument species, and the results of the evaluation are compared across datasets. ") * 25
    html = (f"<html><head><title>Demo paper</title><meta name='citation_doi' content='10.1/demo'>"
            f"<script>var x = 1;</script></head><body><nav>menu</nav><h1>Intro</h1><p>{prose}</p>"
            f"<ul><li>first</li></ul><table><tr><td>a</td><td>b</td></tr></table></body></html>").encode()
    text = fetch.html_to_text(html)
    expect("html: title, citation meta, heading kept; script and nav dropped",
           "title: Demo paper" in text and "citation_doi: 10.1/demo" in text and "# Intro" in text
           and "var x" not in text and "menu" not in text and "- first" in text)
    expect("readable prose → readable", fetch.readability(text)["verdict"] == "readable")
    expect("blocking page → blocked", fetch.readability("<title>Just a moment...</title> Checking your browser")["verdict"] == "blocked")
    expect("symbol soup → unreadable", fetch.readability("�'eCc�;� *fme̫ �k�!�ˢW ¤¥¦§¨©ª«¬ " * 40)["verdict"] == "unreadable")
    expect("short text → partial", fetch.readability(prose[:600])["verdict"] == "partial")
    lig = prose + " the classication of dierent eects and the rst denition " * 3
    expect("lost ligatures → partial", fetch.readability(lig)["verdict"] == "partial")
    pdf = HERE / "mini.pdf"
    pdf.write_bytes(minimal_pdf("Bona fide presentations are accepted"))
    expect("pdf-stdlib extracts a Flate text stream", "Bona fide presentations are accepted" in fetch.pdf_stdlib(pdf))
    meta = fetch.json_to_text(b'{"message": {"DOI": "10.1/x", "title": ["A Survey"], "author": [{"family": "Doe", "given": "J."}], '
                              b'"container-title": ["ACM CSUR"], "issued": {"date-parts": [[2024, 10, 7]]}, "is-referenced-by-count": 20}}')
    expect("crossref JSON → bibliographic record", "title: A Survey" in meta and "Doe, J." in meta and "ACM CSUR" in meta)
    lad = fetch.ladder(["arXiv:2406.03684"], alternates=False)
    expect("ladder: arXiv ID → html, pdf, abs", [u for _, u in lad][:3] == ["https://arxiv.org/html/2406.03684",
                                                                          "https://arxiv.org/pdf/2406.03684",
                                                                          "https://arxiv.org/abs/2406.03684"])
    lad = fetch.ladder(["https://example.org/page"], alternates=True)
    expect("ladder: URL → itself, then Wayback snapshot", [t for t, _ in lad] == ["L1", "L3"])

    print("\n== E. Scaffold and ledger")
    base = HERE / "task9"
    shutil.rmtree(base, ignore_errors=True)
    base.mkdir(parents=True)
    (base / "outline.md").write_text("# Topic\n\n## 1. Scope\n\nScope.\n\n## 2. Theory\n\n### 2.1 Definitions\n\nText.\n\n"
                                     "### 2.2 Metrics\n\nText.\n\n## 3. Policy\n\n### 3.1 Standards\n\nText.\n\n"
                                     "## 4. References\n\n1. Doe, J. (2024). *A Survey*. arXiv:2406.03684.\n")
    code, out = run("scaffold.py", "init", "--base", base, "--outline", base / "outline.md", "--title", "Demo Report")
    plan = (base / "plan.toml").read_text()
    expect("init: parts from the outline, scope and references skipped, seed from arXiv",
           code == 0 and "# 1. Theory" in plan and "## 1.2. Metrics" in plan and "# 2. Policy" in plan
           and not any("Scope" in ln for ln in plan.splitlines() if ln.startswith("heading")) and "https://arxiv.org/abs/2406.03684" in plan)
    import outline as ol
    tab = ["## References", "", "| Ref | Citation | Link | Status |", "| --- | --- | --- | --- |",
           "| R1 | Doe et al. A Survey. arXiv 2406.03684 | [arxiv.org/abs/2406.03684](https://arxiv.org/abs/2406.03684) | Live |",
           "| R2 | Roe. Data Page | [example.org](https://example.org/data) | Live |"]
    items = ol.references(tab, ol.sections(tab))
    expect("outline: a reference table gives one seed per row, with its URL",
           [it["item"] for it in items] == ["R1", "R2"] and items[0]["arxiv"] == "2406.03684"
           and items[1]["urls"] == ["https://example.org/data"] and "[" not in items[0]["text"])
    code, out = run("scaffold.py", "build", "--base", base)
    expect("build + check: 0 errors", code == 0 and "0 errors" in out, out.strip().splitlines()[-1])
    (base / "report" / "01-01-0-definitions.md").unlink()
    gate("check: missing planned file", run("scaffold.py", "check", "--base", base), True, "missing report file")
    code, out = run("progress.py", "--base", base, "set", "T01", "done", "--note", "scaffold ok")
    code2, out2 = run("progress.py", "--base", base, "next")
    expect("ledger: set T01 done, next is T02 with its card", code == 0 and out2.startswith("T02") and "scaffold ok" in out2)

    print("\n== F. Trail bookkeeping (trail.py) and the research prompt")
    b = make("bookkeeping")
    code, out = run("trail.py", "log-search", "--base", b, "--task", "T06", "--query", "pad survey", "--kept", "x → S102", "--dropped", "blog")
    log = (b / "research/search-log.md").read_text()
    expect("log-search: next row number and today's date", code == 0 and "| 2 | T06 |" in log)
    code, out = run("trail.py", "register", "--base", b, "--id", "S102", "--slug", "survey", "--source", "A survey | 2024",
                    "--url", "https://doi.org/10.1/x", "--status", "partial")
    reg = (b / "research/sources.md").read_text()
    expect("register: new row with 8 columns and escaped pipe", code == 0 and "| S102 | survey | A survey \\| 2024 |" in reg)
    code, out = run("trail.py", "register", "--base", b, "--id", "S102", "--status", "fetched")
    expect("register: update one field of an existing row", code == 0 and "| fetched |" in (b / "research/sources.md").read_text().split("S102")[1])
    folder = b / "research/sources/S102-survey"
    folder.mkdir(parents=True)
    (folder / "crawl.md").write_text(CRAWL.replace("S101", "S102") + "\nsource: Crossref\ntitle: A Survey of Liveness\n"
                                     "authors: Doe, Jane; Roe, Rick\ncontainer: ACM Computing Surveys\npublished: 2024-10-7\n"
                                     "volume: 57\nissue: 1\npages: 1-32\ndoi: 10.1145/3687264\ntype: journal-article\n")
    code, out = run("trail.py", "apa", "--base", b, "--id", "S102")
    expect("apa: APA 7 journal entry from the metadata", "Doe, J., & Roe, R. (2024). A Survey of Liveness. *ACM Computing Surveys*, *57*(1), 1–32. https://doi.org/10.1145/3687264" in out, out.strip()[:90])
    code, out = run("trail.py", "claim", "--base", b, "--part", "1", "--source", "S102", "--claim", "c",
                    "--anchor", '"interfering with the operation"', "--files", "01-01-1-x.md")
    expect("claim: next ID C1-002, anchor verified", code == 0 and "C1-002" in out)
    code, out = run("trail.py", "claim", "--base", b, "--part", "1", "--source", "S102", "--claim", "c", "--anchor", '"words that are absent here"')
    expect("claim: refused when the anchor is not in crawl.md", code == 1 and "not found verbatim" in out)
    code, out = run("trail.py", "comprehension", "--base", b, "--id", "S102")
    comp = (folder / "comprehension.md").read_text()
    expect("comprehension: skeleton with six headings and the crawl title",
           code == 0 and comp.startswith("# S102 – A Survey of Liveness") and comp.count("\n## ") == 6)
    code, out = run("progress.py", "--base", base, "prompt", "T05")
    expect("prompt: research task gets its outline lines, ID block and files",
           "sed -n '" in out and "S100–S199" in out and "01-02-0-metrics.md" in out, out.split("sed -n")[1][:20] if "sed -n" in out else "")

    print("\n== G. Local repository sources (fetch.py local)")
    repo = b / "repo"
    repo.mkdir()
    git = lambda *a: subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True)
    git("init", "-q")
    (repo / "pdp.go").write_text("// Decide applies deny-overrides to every policy in scope.\nfunc Decide() {}\n")
    git("add", "."); git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "v1")
    (repo / "pdp.go").write_text("// changed after the commit\n")
    rel = str(repo.relative_to(ROOT))
    run("trail.py", "register", "--base", b, "--id", "S901", "--slug", "pdp", "--source", "Engine PDP",
        "--url", "https://example.org/blob/abc/pdp.go", "--status", "to-fetch")
    code, out = run("fetch.py", "local", "--base", b, "--id", "S901", "--slug", "pdp", "--task", "T04", "--part", "3",
                    "--repo", rel, "--rev", "HEAD", "--url-prefix", "https://example.org/blob/abc", "pdp.go", "nope.go")
    crawl = (b / "research/sources/S901-pdp/crawl.md").read_text()
    expect("local: committed text copied verbatim, not the working tree",
           "applies deny-overrides to every policy" in crawl and "changed after" not in crawl)
    expect("local: a missing path gives status partial and exit 3", code == 3 and "status: partial" in crawl)
    expect("local: register row follows the crawl status",
           "| partial |" in (b / "research/sources.md").read_text().split("S901")[1].split("\n")[0])
    code, out = run("trail.py", "claim", "--base", b, "--part", "1", "--source", "S901", "--claim", "c",
                    "--anchor", '"Decide applies deny-overrides"')
    expect("local: a code fragment serves as a verified claim anchor", code == 0 and "C1-" in out, out.strip()[:80])
    run("trail.py", "register", "--base", b, "--id", "S902", "--slug", "pdp2", "--source", "Engine PDP, no prefix",
        "--url", "-", "--status", "to-fetch")
    run("fetch.py", "local", "--base", b, "--id", "S902", "--slug", "pdp2", "--task", "T04", "--part", "3",
        "--repo", rel, "--rev", "HEAD", "pdp.go")
    head2 = (b / "research/sources/S902-pdp2/crawl.md").read_text().split("---")[1]
    row2 = (b / "research/sources.md").read_text().split("| S902 |")[1].split("\n")[0]
    expect("local: without --url-prefix the URL is a project-relative path, not file:///…",
           f"url: {rel}/pdp.go" in head2 and "file://" not in head2 and f"{rel}/pdp.go" in row2 and "file://" not in row2,
           head2.strip()[:120])

    print("\n== H. Working-file layout (layout.py)")
    b = make("layout")
    (b / "plan.toml").write_text('[layout]\nnotes = [ { path = "fit/", purpose = "AQ-Data Fit log" } ]\n')
    (b / "research/fit").mkdir()
    (b / "research/fit/aq-data-fit.md").write_text("# Fit\n")
    (b / "research/README.md").write_text("# Research Trail\n")
    code, out = run("layout.py", "new-review", "--base", b, "--kind", "vi-native-review", "--scope", "g1")
    code2, out2 = run("layout.py", "new-review", "--base", b, "--kind", "vi-native-review", "--scope", "g2", "--same")
    code3, out3 = run("layout.py", "new-review", "--base", b, "--kind", "vi-consistency")
    expect("new-review: g1 and g2 share round 01, the next round is 02",
           out.strip().endswith("reviews/01-vi-native-review-g1.md") and out2.strip().endswith("01-vi-native-review-g2.md")
           and out3.strip().endswith("reviews/02-vi-consistency.md"), (out + out2 + out3).replace("\n", " ")[:120])
    gate("new-review: a kind outside the vocabulary is refused",
         run("layout.py", "new-review", "--base", b, "--kind", "review2"), True, "kind must be")
    run("layout.py", "index", "--base", b, "--write")
    gate("layout: declared notes, reviews and a current index pass", run("layout.py", "check", "--base", b), False)
    (b / "research/reviews/03-vi-rewrite.md").write_text("# Rewrite\n")
    gate("layout: a new file without a fresh index fails", run("layout.py", "check", "--base", b), True, "out of date")
    run("layout.py", "index", "--base", b, "--write")
    (b / "research/vi-review").mkdir()
    (b / "research/vi-review/review2-A.md").write_text("# x\n")
    gate("layout: an undeclared folder fails", run("layout.py", "check", "--base", b), True, "research/vi-review")
    shutil.rmtree(b / "research/vi-review")
    (b / "research/reviews/review2-A.md").write_text("# x\n")
    gate("layout: a free-form review name fails", run("layout.py", "check", "--base", b), True, "review2-A.md")
    (b / "research/reviews/review2-A.md").unlink()
    shutil.rmtree(b / "research/fit")
    gate("layout: a declared note that is missing fails", run("layout.py", "check", "--base", b), True, "missing")
    (b / "research/fit").mkdir()
    (b / "research/fit/aq-data-fit.md").write_text("# Fit\n")
    # move: files and a folder move with identical bytes; ledgers follow, records (review rounds) keep their wording
    (b / "research/old-review").mkdir()
    (b / "research/old-review/prompt.md").write_text("Write to research/old-review/out.md.\n")
    (b / "research/old-review/out.md").write_text("# Out\n")
    (b / "research/draft-copy").mkdir()
    (b / "research/draft-copy/01.md").write_text("# Draft\n")
    (b / "PROGRESS.md").write_text("| T1 | research/old-review/out.md. |\n")
    m = b / "moves.csv"
    m.write_text("old,new\nold-review/prompt.md,reviews/04-ai-critic-prompt.md\nold-review/out.md,reviews/04-ai-critic-output.md\n"
                 "draft-copy,snapshot\n")
    gate("move: a saved copy that is not identical in the commit is refused", run("layout.py", "move", "--base", b,
         "--map", m, "--apply"), True, "not identical")
    m.write_text("old,new\nold-review/prompt.md,reviews/04-ai-critic-prompt.md\nold-review/out.md,reviews/04-ai-critic-output.md\n")
    code, out = run("layout.py", "move", "--base", b, "--map", m, "--apply")
    expect("move: bytes verified, ledger path rewritten, record prompt kept",
           code == 0 and "2 of 2 moved files identical" in out
           and "research/reviews/04-ai-critic-output.md." in (b / "PROGRESS.md").read_text()
           and "research/old-review/out.md" in (b / "research/reviews/04-ai-critic-prompt.md").read_text()
           and not (b / "research/old-review").exists(), out.strip().splitlines()[-1][:90])

    if online:
        print("\n== F. Live fetch ladder (--online)")
        code, out = run("fetch.py", "probe", "arXiv:2406.03684")
        expect("arXiv ID → readable arXiv HTML", "best: readable https://arxiv.org/html/" in out)
        code, out = run("fetch.py", "probe", "10.1145/3038924")
        expect("blocked ACM DOI (403) → readable fallback", "best: readable" in out, out.strip().splitlines()[-1][:90])

    print(f"\n{sum(results)}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
