"""Stage 7 - report: REPORT.md rendered as report.html, with the charts of charts.py inserted after the
paragraphs they support, task-list checkboxes and appendices generated from results/*.json.

Single source of text: the narrative comes from REPORT.md. The page is self-contained (inline CSS, inline
SVG, a small inline script for hover tooltips) and opens offline.

Run from the repository root, after stages 1-4: venv/bin/python datasets/oulad/exploration/code/07_build_report.py
"""

from __future__ import annotations

import html
import json
import re

import markdown

from charts import (
    INK,
    INK2,
    SURFACE,
    clicks_range,
    duplicates,
    esc,
    first_assessment,
    fmt,
    gender_simpson,
    imd_gradient,
    missingness,
    outcome_by_module,
    survival_curves,
    signal_ranking,
    trajectory_clusters,
    table,
    weekly_clicks,
    yoy_withdrawal,
)
from common import HERE, OUTCOMES, RESULTS


def appendix_columns(cols: list[dict]) -> str:
    rows = []
    for c in cols:
        stats = (f'{c["min"]:g} / {c["p50"]:g} / {c["max"]:g}' if "p50" in c and c.get("min") is not None else "")
        top = ", ".join(f"{v} ({n:,})" for v, n in (c.get("top_values") or [])[:4])
        rows.append([c["table"], c["column"], c["role"], fmt(c["missing"]), f'{c["missing_rate"]:.2%}',
                     fmt(c["distinct"]), stats, top])
    return table(["Table", "Column", "Role", "Missing", "Rate", "Distinct", "Min / median / max", "Top values"],
                 rows, f"All {len(cols)} columns: role, missingness, cardinality, range and top values")


def appendix_checks(checks: list[dict]) -> str:
    rows = [[c["status"], c["check"], json.dumps(c["observed"]) if isinstance(c["observed"], list) else c["observed"],
             c["expected"], c["note"]] for c in checks]
    passed = sum(c["status"] == "PASS" for c in checks)
    return table(["Status", "Check", "Observed", "Expected", "Note"], rows,
                 f"All {len(checks)} integrity and business-rule checks ({passed} pass, {len(checks) - passed} flagged)")


def appendix_presentations(seg: dict) -> str:
    rows = [[r["code_presentation"]] + [fmt(r[o]) for o in OUTCOMES]
            + [f'{r["Withdrawn"] / sum(r[o] for o in OUTCOMES):.1%}'] for r in seg["final_result_by_presentation"]]
    return table(["Presentation"] + OUTCOMES + ["Withdrawn %"], rows, "Outcome counts by presentation period")


# Page tokens (design-notes.md); chart inks in charts.py use the same values
PAPER, RAIL, RULE, MARKER = SURFACE, "#f3f5f8", "#dfe3ea", "#1d6b47"
SERIF = 'Charter, "Bitstream Charter", "Sitka Text", Cambria, serif'
SANS = '"Avenir Next", "Segoe UI", "Helvetica Neue", Arial, sans-serif'
MONO = 'ui-monospace, "SF Mono", Menlo, Consolas, monospace'

CSS = f"""
:root{{color-scheme:light;--paper:{PAPER};--rail:{RAIL};--ink:{INK};--ink-2:{INK2};--rule:{RULE};--marker:{MARKER}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 {SANS};font-variant-numeric:tabular-nums;
  -webkit-font-smoothing:antialiased}}
@media (prefers-reduced-motion:no-preference){{html{{scroll-behavior:smooth}}}}
.page{{display:grid;grid-template-columns:272px minmax(0,1fr)}}

/* navigation rail */
.rail{{background:var(--rail);border-right:1px solid var(--rule);position:sticky;top:0;height:100vh;overflow-y:auto;
  font-size:14px;line-height:1.45}}
.rail-in{{padding:28px 20px 40px}}
.rail a{{color:var(--ink);text-decoration:none}}
.rail a:hover{{text-decoration:underline;text-decoration-color:var(--marker)}}
.rail-title{{display:block;font:700 19px/1.25 {SERIF}}}
.rail-meta{{color:var(--ink-2);margin:4px 0 22px}}
.rail-h{{font-weight:600;color:var(--ink-2);margin:22px 0 8px;font-size:13.5px}}
.toc summary{{font-weight:600;color:var(--ink-2);cursor:pointer;font-size:13.5px}}
.toc ol,ol.issues,ul.files{{list-style:none;margin:6px 0 0;padding:0}}
.toc li{{margin:2px 0}} .toc ol ol{{padding-left:14px;margin:2px 0 4px}}
.toc a{{display:block;padding:2px 8px;border-left:2px solid transparent}}
.toc a[aria-current="true"]{{border-left-color:var(--marker);color:var(--marker);font-weight:600}}
.issues li{{margin:0 0 7px}} .issues a{{display:grid;grid-template-columns:22px 1fr;gap:2px 6px;align-items:baseline}}
.issues .n{{color:var(--ink-2);text-align:right}} .issues .sev{{grid-column:2;justify-self:start;margin-top:2px}}
.files li{{margin:3px 0}} .files code{{font-size:12.5px}}

/* document */
main{{padding:40px 48px 96px;max-width:1060px;min-width:0}}
h1,h2,h3,figcaption strong{{font-family:{SERIF};color:var(--ink)}}
h1{{font-size:36px;line-height:1.15;font-weight:700;margin:0 0 18px;letter-spacing:-.01em}}
h2{{font-size:24px;line-height:1.25;margin:56px 0 12px;padding-top:18px;border-top:1px solid var(--rule)}}
h3{{font-size:19px;line-height:1.3;margin:34px 0 8px}}
h2,h3{{scroll-margin-top:16px}}
p{{margin:0 0 14px}}  /* prose uses the full content column, like tables and figures */
a{{color:var(--marker);text-decoration-thickness:1px;text-underline-offset:2px}} a[href^="#"],.nw{{white-space:nowrap}} .rail a[href]{{white-space:normal}}
code{{font:.86em/1.4 {MONO};background:#eef1f5;padding:1px 5px;border-radius:3px}}
a.file code{{background:#e6f0ea;color:var(--marker)}}
pre{{background:#eef1f5;padding:14px 16px;border-radius:4px;overflow-x:auto;max-width:100%}} pre code{{background:none;padding:0}}
:focus-visible{{outline:2px solid var(--marker);outline-offset:2px}}
.facts{{list-style:none;padding:0;margin:0 0 22px;display:grid;gap:4px}}
.facts li{{display:grid;grid-template-columns:9.5em 1fr;max-width:none}} .facts strong{{font-weight:600;color:var(--ink-2)}}
.status{{border-left:3px solid var(--marker);padding:2px 0 2px 16px}}

/* tables */
.scroll{{overflow-x:auto;margin:16px 0 22px}}
table{{border-collapse:collapse;width:100%;font-size:14px;line-height:1.45}}
th,td{{text-align:left;padding:8px 12px 8px 0;border-bottom:1px solid var(--rule);vertical-align:top}}
th{{font-weight:600;color:var(--ink-2);border-bottom:1.5px solid var(--ink-2);white-space:nowrap}}
th.num,td.num{{text-align:right;padding-left:12px}}
tr:target td{{background:#e6f0ea}}
.issue-table td:nth-child(2){{min-width:11em}} .issue-table td:nth-child(4){{min-width:7.5em}}
.sev{{display:inline-block;font-size:12px;line-height:18px;font-weight:600;padding:0 6px;border-radius:3px;border:1px solid var(--ink);
  white-space:nowrap}}
.sev-high{{background:var(--ink);color:#fff}} .sev-medium{{color:var(--ink)}}
.sev-low{{border-color:transparent;color:var(--ink-2);padding-left:0;font-weight:500}}

/* figures */
.chart{{margin:28px 0 30px;padding-top:14px;border-top:1px solid var(--rule)}}
.chart figcaption{{display:grid;gap:3px;margin-bottom:10px}}
.chart .fig-n{{font-size:13px;color:var(--ink-2);font-weight:600}}
.chart figcaption strong{{font-size:19px;line-height:1.3}}
.chart .sub{{color:var(--ink-2);font-size:14px}}
.chart svg{{width:100%;height:auto;display:block}}
.legend{{display:flex;gap:18px;flex-wrap:wrap;font-size:13px;color:var(--ink-2);margin:4px 0 6px}}
.key{{display:inline-flex;align-items:center;gap:6px}} .swatch{{width:11px;height:11px;border-radius:2px;display:inline-block}}
.tableview summary{{cursor:pointer;color:var(--marker);font-size:13.5px;margin-top:8px;width:max-content}}
.tableview .scroll{{margin-top:8px}}
.mark:focus{{outline:2px solid var(--marker);outline-offset:1px}}
#tip{{position:fixed;pointer-events:none;background:#fff;border:1px solid var(--rule);border-radius:4px;
  box-shadow:0 2px 8px rgba(29,36,51,.12);padding:7px 10px;font-size:13px;line-height:1.45;display:none;max-width:320px;z-index:9}}
#tip div:first-child{{font-weight:600}}
ul.tasks{{list-style:none;padding-left:0}} li.task{{display:grid;grid-template-columns:24px 1fr}}
.box{{font-weight:700;line-height:1.6}} .box.done{{color:var(--marker)}} .box.open{{color:var(--ink-2)}}

@media (max-width:900px){{
  .page{{grid-template-columns:1fr}}
  .rail{{position:static;height:auto;border-right:0;border-bottom:1px solid var(--rule)}}
  main{{padding:28px 18px 64px}} h1{{font-size:28px}} .facts li{{grid-template-columns:1fr}}
}}
@media print{{.rail{{display:none}} .page{{display:block}} .chart{{break-inside:avoid}} details{{display:block}}}}
"""

JS = """
const tip=document.getElementById('tip');
function show(e,el){tip.replaceChildren(...el.dataset.tip.split(' | ').map(t=>{const d=document.createElement('div');d.textContent=t;return d}));
 tip.style.display='block';const r=tip.getBoundingClientRect();let x=e.clientX+14,y=e.clientY+14;
 if(x+r.width>innerWidth-8)x=e.clientX-r.width-14;if(y+r.height>innerHeight-8)y=e.clientY-r.height-14;tip.style.left=x+'px';tip.style.top=y+'px';
 const svg=el.ownerSVGElement,ch=svg&&svg.querySelector('.crosshair');if(ch&&el.dataset.x){ch.setAttribute('x1',el.dataset.x);ch.setAttribute('x2',el.dataset.x);ch.setAttribute('visibility','visible')}}
function hide(el){tip.style.display='none';const ch=el.ownerSVGElement&&el.ownerSVGElement.querySelector('.crosshair');if(ch)ch.setAttribute('visibility','hidden')}
document.querySelectorAll('.mark').forEach(el=>{el.addEventListener('pointermove',e=>show(e,el));el.addEventListener('pointerleave',()=>hide(el));
 el.addEventListener('focus',()=>{const b=el.getBoundingClientRect();show({clientX:b.right,clientY:b.top},el)});el.addEventListener('blur',()=>hide(el))});
// current section in the rail
const links=new Map([...document.querySelectorAll('.toc a')].map(a=>[a.getAttribute('href').slice(1),a]));
const heads=[...document.querySelectorAll('main h2[id],main h3[id]')].filter(h=>links.has(h.id));
function mark(){let cur=heads[0];for(const h of heads){if(h.getBoundingClientRect().top<120)cur=h;else break}
 links.forEach(a=>a.removeAttribute('aria-current'));if(cur)links.get(cur.id).setAttribute('aria-current','true')}
addEventListener('scroll',mark,{passive:true});mark();
if(matchMedia('(max-width:900px)').matches)document.querySelector('.toc').open=false;
"""

NUMERIC = re.compile(r"^[−+-]?[\d,]*\.?\d+%?$")
FILE_PATH = re.compile(r"^(?:(?:results|code|evidence|logs)/[\w./-]+|REPORT\.md|README\.md|design-notes\.md)$")


def plain(fragment: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def slug(text: str) -> str:
    s = re.sub(r"[^\w\s-]", "", plain(text).lower())
    return re.sub(r"\s+", "-", s.strip())


def add_heading_ids(body: str) -> tuple[str, list[tuple[int, str, str]]]:
    toc = []

    def sub(m):
        level, inner = int(m.group(1)), m.group(2)
        hid = slug(inner)
        toc.append((level, hid, plain(inner)))
        return f'<h{level} id="{hid}">{inner}</h{level}>'
    return re.sub(r"<h([23])>(.*?)</h\1>", sub, body, flags=re.S), toc


def link_text(body: str, toc: list[tuple[int, str, str]]) -> str:
    """Outside links, code and headings: 'Section 5.2' -> link to that section."""
    by_number = {}
    for _, hid, text in toc:
        m = re.match(r"(\d+(?:\.\d+)?)\.?\s", text)
        if m:
            by_number[m.group(1)] = hid
    out, skip = [], 0
    for part in re.split(r"(<[^>]+>)", body):
        if part.startswith("<"):
            tag = re.match(r"</?(\w+)", part)
            if tag and tag.group(1) in ("a", "code", "h1", "h2", "h3", "svg", "script", "summary"):
                skip += -1 if part.startswith("</") else 1
            out.append(part)
        elif skip:
            out.append(part)
        else:
            out.append(re.sub(r"Section (\d+(?:\.\d+)?)(?![\d–])",
                              lambda m: f'<a href="#{by_number[m.group(1)]}">Section {m.group(1)}</a>'
                              if m.group(1) in by_number else m.group(0), part))
    return "".join(out)


def link_files(body: str) -> str:
    """Every <code>path</code> naming an existing file of this folder becomes a link to it."""
    def sub(m):
        path = html.unescape(m.group(1))
        return (f'<a class="file" href="{esc(path)}"><code>{m.group(1)}</code></a>'
                if FILE_PATH.match(path) and (HERE / path).exists() else m.group(0))
    return re.sub(r"(?<!\">)<code>([^<]+)</code>", sub, body)


def style_tables(body: str) -> str:
    """Right-align all-numeric columns; severity words become badges."""
    def table_sub(m):
        t = m.group(0)
        rows = re.findall(r"<tr>(.*?)</tr>", t, re.S)
        cells = [re.findall(r"<(t[hd])([^>]*)>(.*?)</\1>", r, re.S) for r in rows]
        width = max((len(c) for c in cells), default=0)
        numeric = [all(NUMERIC.match(plain(r[i][2])) for r in cells if len(r) > i and r[i][0] == "td" and plain(r[i][2]))
                   and any(len(r) > i and r[i][0] == "td" and plain(r[i][2]) for r in cells) for i in range(width)]
        def row_sub(rm):
            def cell_sub(cm, idx=[0]):
                i = idx[0]; idx[0] += 1
                cls = ' class="num"' if i < width and numeric[i] else ""
                return f"<{cm.group(1)}{cls}{cm.group(2)}>{cm.group(3)}</{cm.group(1)}>"
            return "<tr>" + re.sub(r"<(t[hd])([^>]*)>(.*?)</\1>", cell_sub, rm.group(1), flags=re.S) + "</tr>"
        return re.sub(r"<tr>(.*?)</tr>", row_sub, t, flags=re.S)
    body = re.sub(r"<table>.*?</table>", table_sub, body, flags=re.S)
    body = re.sub(r"(\d[\d.,]*%? \(\d[\d.,]*–\d[\d.,]*\))", r'<span class="nw">\1</span>', body)
    return re.sub(r"<td>(High|Medium|Low)\b", lambda m: f'<td><span class="sev sev-{m.group(1).lower()}">{m.group(1)}</span>', body)


def issues_from(body: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Give each row of the Section 3 issue table an id and collect (number, name, severity) for the rail."""
    start = body.index('<h2 id="3-data-quality')
    end = body.index("</table>", start)
    part, issues = body[start:end], []
    part = part.replace("<table>", '<table class="issue-table">', 1)

    def sub(m):
        n, name, sev = m.group(1), plain(m.group(2)), re.search(r"sev-(\w+)", m.group(3)).group(1)
        issues.append((n, re.split(r" \(|: ", name)[0], sev))
        return f'<tr id="issue-{n}">' + m.group(0)[4:]
    part = re.sub(r"<tr>\s*<td[^>]*>(\d+)</td>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>.*?</td>\s*<td[^>]*>(.*?)</td>", sub, part, flags=re.S)
    return body[:start] + part + body[end:], issues


def rail(toc: list[tuple[int, str, str]], issues: list[tuple[str, str, str]]) -> str:
    items, open_sub = [], False
    for level, hid, text in toc:
        if level == 2:
            if open_sub:
                items.append("</ol></li>"); open_sub = False
            items.append(f'<li><a href="#{hid}">{esc(text)}</a>')
            items.append("</li>")
        else:
            if not open_sub:
                items.pop(); items.append("<ol>"); open_sub = True
            items.append(f'<li><a href="#{hid}">{esc(text)}</a></li>')
    if open_sub:
        items.append("</ol></li>")
    iss = "".join(f'<li><a href="#issue-{n}"><span class="n">{n}</span><span>{esc(name)}</span>'
                  f'<span class="sev sev-{sev}">{sev.capitalize()}</span></a></li>' for n, name, sev in issues)
    files = "".join(f'<li><a class="file" href="{p}"><code>{p}</code></a></li>' for p in
                    ("results/descriptive.json", "results/multivariate.json", "results/checks.json",
                     "results/enrolment_features.csv", "code/run_all.sh", "README.md", "REPORT.md") if (HERE / p).exists())
    return (f'<aside class="rail" aria-label="Report navigation"><div class="rail-in">'
            f'<a class="rail-title" href="#top">OULAD exploration</a><p class="rail-meta">Snapshot 1 November 2026</p>'
            f'<details class="toc" open><summary>Contents</summary><ol>{"".join(items)}</ol></details>'
            f'<p class="rail-h">Data issues</p><ol class="issues">{iss}</ol>'
            f'<p class="rail-h">Evidence files</p><ul class="files">{files}</ul></div></aside>')


def main() -> None:
    seg = json.loads((RESULTS / "segments.json").read_text())
    cols = json.loads((RESULTS / "columns.json").read_text())
    checks = json.loads((RESULTS / "checks.json").read_text())
    md = (HERE / "REPORT.md").read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["tables", "fenced_code"])
    body = re.sub(r"<table>", '<div class="scroll"><table>', body).replace("</table>", "</table></div>")
    # task-list items ("- [x]" / "- [ ]"), which python-markdown leaves as literal text
    body = re.sub(r"<li>\[([ x])\]\s*", lambda m: '<li class="task">' + (
        '<span class="box done" role="img" aria-label="done">✓</span>' if m.group(1) == "x"
        else '<span class="box open" role="img" aria-label="to do">○</span>') + "<span>", body)
    body = re.sub(r'(<li class="task">.*?)</li>', r"\1</span></li>", body, flags=re.S)
    body = re.sub(r"<ul>(\s*<li class=\"task\">)", r'<ul class="tasks">\1', body)
    # header: dataset facts list and status paragraph
    body = re.sub(r"(</h1>\s*)<ul>", r'\1<ul class="facts">', body, count=1)
    body = body.replace("<p><strong>Status:", '<p class="status"><strong>Status:', 1)

    def after_heading(text: str, block: str) -> None:
        nonlocal body
        m = re.search(rf"(<h2>{re.escape(text)}[^<]*</h2>)", body)
        assert m, text
        # insert before the next h2 (end of that section)
        nxt = body.find("<h2>", m.end())
        pos = nxt if nxt != -1 else len(body)
        body = body[:pos] + block + body[pos:]

    after_heading("1. Dataset map", outcome_by_module(seg))
    after_heading("3. Data quality issues", duplicates(seg) + missingness(cols))
    after_heading("4. Column profile highlights", clicks_range(seg) + weekly_clicks(seg))
    desc = json.loads((RESULTS / "descriptive.json").read_text())

    def after_paragraph(snippet: str, block: str) -> None:
        nonlocal body
        i = body.find(snippet)
        assert i != -1, snippet
        end = body.find("</p>", i) + len("</p>")
        body = body[:end] + block + body[end:]

    after_paragraph("which makes <code>imd_band</code> usable", imd_gradient(desc))
    after_paragraph("repeat against first attempt", gender_simpson(desc))
    after_paragraph("A clean early-warning", first_assessment(desc))
    after_paragraph("Retention at day 60 ranges", survival_curves(desc))
    after_paragraph("Withdrawal rose from 2013 to 2014", yoy_withdrawal(desc))
    multi = json.loads((RESULTS / "multivariate.json").read_text())
    after_paragraph("ranks the measures by how strongly", signal_ranking(desc))
    after_paragraph("sustained high-activity group", trajectory_clusters(multi))

    appendix = ("<h2>Appendix: everything the exploration produced</h2>"
                "<p>Generated from <code>results/checks.json</code> and <code>results/columns.json</code>; "
                "open a table to read it.</p>"
                + appendix_checks(checks) + appendix_columns(cols) + appendix_presentations(seg))
    body = body.replace("<h2>Reproduce</h2>", appendix + "<h2>Reproduce</h2>")

    # numbered figures, ids, links, table styling, issue anchors
    count = iter(range(1, 100))
    body = re.sub(r'<figure class="chart"><figcaption>',
                  lambda m: (lambda n: f'<figure class="chart" id="figure-{n}"><figcaption><span class="fig-n">Figure {n}</span>')(next(count)), body)
    body, toc = add_heading_ids(body)
    body = style_tables(link_files(link_text(body, toc)))
    body, issues = issues_from(body)
    body = body.replace("<h1>", '<h1 id="top">', 1)

    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<title>OULAD exploration report</title><style>{CSS}</style></head>"
            f'<body><div class="page">{rail(toc, issues)}<main>{body}</main></div>'
            f'<div id="tip" role="tooltip"></div><script>{JS}</script></body></html>')
    (HERE / "report.html").write_text(page, encoding="utf-8")
    print(f"wrote {HERE / 'report.html'} ({len(page) / 1024:.0f} KB): {next(count) - 1} figures, "
          f"{len(toc)} headings, {len(issues)} issues, {page.count('class=\"file\"')} file links, "
          f"{page.count('href=\"#')} in-page links")


if __name__ == "__main__":
    main()
