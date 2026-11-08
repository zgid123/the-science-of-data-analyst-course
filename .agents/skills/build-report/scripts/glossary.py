"""Layered translation glossaries of a language pack: common → domains → topics.

Usage:
    glossary.py --lang vi [--task TASK | --names a,b] show            the merged glossary with each row's layer
    glossary.py --lang vi [--task TASK | --names a,b] lookup "term"   rows whose English or Vietnamese contains the term
    glossary.py --lang vi lint                                         check every glossary file of the pack
    glossary.py --lang vi --task TASK coverage --report DIR | --deck MODULE.py   term drift across a deliverable
    glossary.py --lang vi sizes                                        rows and sections of every glossary file
    glossary.py --lang vi split LAYER/FILE.md [--each]                 balanced files by ## section, tasks.toml updated
    glossary.py --lang vi snapshot save|compare FILE.json              the merged glossary of every task, kept equal

Layers (languages/<code>/glossaries/): every file in common/ applies to every report; a task adds the domain and topic
files it names in tasks.toml ([taskN.<code>] glossaries = ["domain-name", "topic-name"]), looked up in domains/ and
then topics/. When the same English term appears in several layers, the more specific layer wins (topic > domain >
common), which lets a field fix its own sense of a general word. Rows are table rows | English | Vietnamese | Usage |
Replaces |; Replaces lists variants (comma-separated) that the language checks report as errors with the preferred
form. lint reports: malformed rows, an English term repeated within one file or translated differently in two common
files, a variant claimed by two different preferred forms, and a variant that is itself a preferred form elsewhere.

Every file stays small enough for an agent to read in one pass: lint reports a file above ROW_BUDGET rows. split
turns such a file into focused files: consecutive ## sections grouped into the fewest files of about equal size, each
at most SPLIT_FILL of the budget (--each: one file per section); the first file keeps the name, each further one is
LAYER/<file>-<its first section>.md, all with the file's opening paragraph; it adds the new names after the old one in every tasks.toml glossaries list that names it,
and confirms with a snapshot that every task's merged glossary is unchanged; on any difference it restores the
files and stops. snapshot save/compare records and compares those merged glossaries around any manual
reorganisation (moving rows between files or to common/).

coverage measures term drift over a whole deliverable: for each domain and topic term (the task's own concepts), it
counts the English term in the source (a report's English files, or the keys of a deck's VI module) and the
glossary's form, or the English term kept, in the translation. A concept met at least --min times in the English
whose glossary form appears in fewer than --ratio of those places most likely travels under other names in the
translation, which a reader takes for different things (lessons.md S2). Counted over the whole deliverable, the
measure tolerates sentence-level rephrasing; it is a diagnosis for the reviewer and always exits 0.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from common import ROOT, language_packs, load_config, tasks, shown

LAYERS = ("common", "domains", "topics")
ROW_BUDGET = 150                                     # rows an agent reads comfortably in one pass of a file
SPLIT_FILL = 0.6                                     # a split leaves each file at about 60% of the budget, room to grow


def folder(pack: dict) -> Path:
    return pack["_dir"] / pack.get("translation", {}).get("glossaries", "glossaries")


def names_of(task: dict, code: str) -> list[str]:
    cfg = task.get(code, {}) if task else {}
    names = cfg.get("glossaries", cfg.get("glossary", []))
    return [names] if isinstance(names, str) else list(names)


def files_for(pack: dict, names: list[str]) -> list[tuple[str, Path]]:
    """(layer, path) in precedence order, lowest first: all common files, then each named domain or topic."""
    root = folder(pack)
    out = [("common", p) for p in sorted((root / "common").glob("*.md"))]
    for name in names:
        hit = next(((layer, root / layer / f"{name}.md") for layer in ("domains", "topics")
                    if (root / layer / f"{name}.md").exists()), None)
        if hit is None:
            raise SystemExit(f"glossary '{name}' not found in {shown(root)}/domains or topics")
        out.append(hit)
    return out


def rows_of(path: Path) -> list[dict]:
    rows = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] in ("English", "") or set("".join(cells)) <= set("-: "):
            continue
        cells += [""] * (4 - len(cells))
        rows.append(dict(en=cells[0], vi=cells[1], usage=cells[2], replaces=[v.strip() for v in cells[3].split(",") if v.strip()],
                         file=path.name, line=n, cells=len(cells)))
    return rows


def load(pack: dict, names: list[str]) -> list[dict]:
    """Merged rows: one per English term, from the most specific layer that defines it."""
    merged = {}
    for layer, path in files_for(pack, names):
        for r in rows_of(path):
            key = r["en"].lower()
            if key in merged and merged[key]["vi"] != r["vi"]:
                r["overrides"] = f"{merged[key]['layer']}/{merged[key]['file']}"
            merged[key] = {**r, "layer": layer}
    return list(merged.values())


def variants(rows: list[dict]) -> list[tuple[str, str]]:
    """(variant, preferred form) pairs for the language checks."""
    return [(v, r["vi"]) for r in rows for v in r["replaces"]]


def for_task(pack: dict, task: dict | None) -> list[tuple[str, str]]:
    if "translation" not in pack:
        return []
    return variants(load(pack, names_of(task, pack["code"])))


def _forms(cell: str, shortest: int) -> list[str]:
    """The alternatives of a glossary cell ("a / b (gloss)") without parenthesised glosses."""
    return [f.strip() for f in re.split(r"\s*/\s*", re.sub(r"\(.*?\)", "", cell)) if len(f.strip()) >= shortest]


def coverage(rows: list[dict], source: str, target: str, minimum: int = 3, ratio: float = 0.5) -> list[dict]:
    """Domain and topic terms whose glossary form covers fewer than `ratio` of the English term's occurrences."""
    out, low = [], target.lower()
    for r in rows:
        if r.get("layer") == "common":
            continue
        ens, vis = _forms(r["en"], 3), _forms(r["vi"], 1)
        if not ens or not vis:
            continue
        n_en = sum(len(re.findall(rf"\b{re.escape(e)}(?:s|es)?\b", source, re.I)) for e in ens)
        n_vi = sum(low.count(v.lower()) for v in vis) + sum(low.count(e.lower()) for e in ens)
        if n_en >= minimum and n_vi / n_en < ratio:
            out.append(dict(row=r, en=n_en, vi=n_vi, share=n_vi / n_en))
    return sorted(out, key=lambda d: d["share"])


def deliverable_text(pack: dict, report: str | None, deck: str | None) -> tuple[str, str]:
    """(English, translation) of a report folder (source files and their twins) or of a deck's VI module."""
    if deck:
        import importlib.util
        spec = importlib.util.spec_from_file_location("deck_vi", deck)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return "\n".join(mod.VI.keys()), "\n".join(mod.VI.values())
    folder_ = ROOT / report
    suffix = pack.get("suffix", f".{pack['code']}.md")
    src = [p for p in sorted(folder_.glob("*.md")) if not p.name.endswith(suffix) and ".vi." not in p.name]
    twins = [p.with_name(p.name[:-3] + suffix) for p in src]
    return ("\n".join(p.read_text(encoding="utf-8") for p in src),
            "\n".join(t.read_text(encoding="utf-8") for t in twins if t.exists()))


def lint(pack: dict) -> list[str]:
    errors = []
    root = folder(pack)
    paths = [p for layer in LAYERS for p in sorted((root / layer).glob("*.md"))]
    claimed = {}
    preferred = {}
    common = {}                                      # every common file is always loaded: one meaning per term
    for p in sorted((root / "common").glob("*.md")):
        for r in rows_of(p):
            key = r["en"].lower()
            if key in common and common[key][0] != r["vi"]:
                errors.append(f"common/{p.name}:{r['line']}: '{r['en']}' differs from {common[key][1]} ('{common[key][0]}')")
            common.setdefault(key, (r["vi"], f"common/{p.name}:{r['line']}"))
    for p in paths:
        seen = {}
        for r in rows_of(p):
            where = f"{p.relative_to(root)}:{r['line']}"
            if r["cells"] > 4 or not r["vi"]:
                errors.append(f"{where}: row needs | English | Vietnamese | Usage | Replaces | ('{r['en'][:40]}')")
            key = r["en"].lower()
            if key in seen:
                errors.append(f"{where}: '{r['en']}' already defined at line {seen[key]}")
            seen[key] = r["line"]
            for form in re.split(r"\s*/\s*|;\s*", r["vi"]):
                preferred.setdefault(form.strip(), where)
            for v in r["replaces"]:
                if v in claimed and claimed[v][0] != r["vi"]:
                    errors.append(f"{where}: variant '{v}' also replaced by '{claimed[v][0]}' at {claimed[v][1]}")
                claimed[v] = (r["vi"], where)
    for v, (vi, where) in claimed.items():
        if v in preferred:
            errors.append(f"{where}: variant '{v}' is a preferred form at {preferred[v]}")
    return errors


def sizes(pack: dict) -> list[tuple[str, int, int]]:
    """(layer/file, rows, ## sections) of every glossary file, largest first."""
    root = folder(pack)
    out = []
    for layer in LAYERS:
        for p in sorted((root / layer).glob("*.md")):
            text = p.read_text(encoding="utf-8")
            out.append((f"{layer}/{p.name}", len(rows_of(p)), len(re.findall(r"(?m)^## ", text))))
    return sorted(out, key=lambda x: -x[1])


def over_budget(pack: dict) -> list[str]:
    return [f"{name} holds {n} rows, above the budget of {ROW_BUDGET}: "
            + (f"group its {k} sections into balanced files with `glossary.py --lang {pack['code']} split {name}`" if k >= 2 else
               "group its rows under ## sections by concept, then split it with `glossary.py split`")
            for name, n, k in sizes(pack) if n > ROW_BUDGET]


def snapshot(pack: dict) -> dict:
    """Merged rows (English, Vietnamese, usage, replaces) of every task that uses this pack, by task."""
    out = {}
    for name, task in tasks(load_config()).items():
        if pack["code"] not in task:
            continue
        try:
            rows = load(pack, names_of(task, pack["code"]))
        except SystemExit:
            continue
        out[name] = sorted([r["en"].lower(), r["vi"], r["usage"], sorted(r["replaces"])] for r in rows)
    return out


def snapshot_diff(before: dict, after: dict) -> list[str]:
    import json
    diff = []
    for t in sorted(set(before) | set(after)):
        a = {json.dumps(r, ensure_ascii=False) for r in before.get(t, [])}
        b = {json.dumps(r, ensure_ascii=False) for r in after.get(t, [])}
        diff += [f"{t}: removed or changed {r}" for r in sorted(a - b)]
        diff += [f"{t}: added or changed {r}" for r in sorted(b - a)]
    return diff


def slug(text: str) -> str:
    words, out = re.sub(r"[^a-z0-9]+", " ", text.lower()).split(), ""
    for w in words:                                   # whole words up to 40 characters
        if len(out) + len(w) + 1 > 40:
            break
        out = f"{out}-{w}" if out else w
    return out or "section"


def group_sections(sections: list[str], each: bool = False) -> list[list[str]]:
    """Consecutive ## sections in the fewest files of about equal size, each at most SPLIT_FILL of the budget."""
    if each:
        return [[sec] for sec in sections]
    sizes_ = [len(re.findall(r"(?m)^\|", sec)) for sec in sections]   # table lines; headers count alike everywhere
    total = sum(sizes_)
    n = min(len(sections), max(2, -(-total // int(SPLIT_FILL * ROW_BUDGET))))
    groups, cum, k = [[]], 0, 1
    for sec, size in zip(sections, sizes_):
        if groups[-1] and k < n and cum + size / 2 > k * total / n:  # cut at the boundary nearest the next share
            groups.append([])
            k += 1
        groups[-1].append(sec)
        cum += size
    return groups


def split(pack: dict, rel: str, each: bool = False) -> list[str]:
    """Split LAYER/FILE.md by its ## sections into balanced files; keep every task's merged glossary unchanged."""
    root = folder(pack)
    path = root / rel
    layer, stem = path.parent.name, path.stem
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"(?m)^(?=## )", text)
    head, sections = parts[0], [x for x in parts[1:] if x.strip()]
    if len(sections) < 2:
        raise SystemExit(f"{rel} has {len(sections)} ## section(s); group its rows under sections first")
    title = (re.search(r"(?m)^# (.*)$", head) or [None, stem])[1]
    intro = re.sub(r"(?m)^# .*\n", "", head).strip()
    before = snapshot(pack)
    config_path = __import__("common").CONFIG
    config_text = config_path.read_text(encoding="utf-8")
    groups = group_sections(sections, each)
    written = {}
    for i, group in enumerate(groups):
        headings = [re.match(r"## (.*)", sec)[1].strip() for sec in group]
        name = stem if i == 0 else f"{stem}-{slug(headings[0])}"
        body = (f"# {title}: {'; '.join(headings)}\n\n" + (intro + "\n\n" if intro else "")
                + "\n\n".join(sec.strip() for sec in group) + "\n")
        written[name] = body
    new_names = [n for n in written if n != stem]
    clash = [n for n in new_names if (root / layer / f"{n}.md").exists()]
    if clash:
        raise SystemExit(f"files already exist: {', '.join(clash)}")
    for name, body in written.items():
        (root / layer / f"{name}.md").write_text(body, encoding="utf-8")
    if layer != "common":                             # common files load for every task; others are named per task
        quoted = f'"{stem}"'
        lines = []
        for line in config_text.split("\n"):
            if re.match(r"\s*glossar(y|ies)\s*=", line) and quoted in line:
                listed = ", ".join(f'"{n}"' for n in [stem] + new_names)
                line = (line.replace(quoted, listed, 1) if "[" in line else
                        re.sub(r"glossar(y|ies)\s*=\s*" + re.escape(quoted), f"glossaries = [{listed}]", line))
            lines.append(line)
        config_path.write_text("\n".join(lines), encoding="utf-8")
    diff = snapshot_diff(before, snapshot(pack))
    if diff:                                          # restore everything and stop
        path.write_text(text, encoding="utf-8")
        for n in new_names:
            (root / layer / f"{n}.md").unlink(missing_ok=True)
        config_path.write_text(config_text, encoding="utf-8")
        raise SystemExit("split changed a merged glossary, restored:\n" + "\n".join(diff[:20]))
    return [f"{layer}/{n}.md" for n in written]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["show", "lookup", "lint", "coverage", "sizes", "split", "snapshot"])
    ap.add_argument("term", nargs="?", help="lookup: the term; split: LAYER/FILE.md; snapshot: save or compare")
    ap.add_argument("file", nargs="?", help="snapshot: the JSON file")
    ap.add_argument("--each", action="store_true", help="split: one file per ## section instead of balanced groups")
    ap.add_argument("--lang", required=True)
    ap.add_argument("--task")
    ap.add_argument("--names", help="comma-separated domain/topic glossary names")
    ap.add_argument("--report", help="coverage: report folder (English files and their twins)")
    ap.add_argument("--deck", help="coverage: a deck's VI module (keys English, values translated)")
    ap.add_argument("--min", type=int, default=3, help="coverage: English occurrences a term needs to be judged")
    ap.add_argument("--ratio", type=float, default=0.5, help="coverage: share below which a term counts as drifted")
    args = ap.parse_args()
    pack = language_packs()[args.lang]
    if args.command == "lint":
        errors = lint(pack)
        files = [p for layer in LAYERS for p in (folder(pack) / layer).glob("*.md")]
        for e in errors:
            print("ERROR " + e)
        for w in over_budget(pack):
            print("WARN  " + w)
        print(f"Checked {len(files)} glossary files, {sum(len(rows_of(p)) for p in files)} terms: {len(errors)} errors")
        return 1 if errors else 0
    if args.command == "sizes":
        print(f"{'file':55} {'rows':>5} {'sections':>8}")
        for name, n, k in sizes(pack):
            mark = "  above budget" if n > ROW_BUDGET else ("  near budget" if n > 0.8 * ROW_BUDGET else "")
            print(f"{name:55} {n:5} {k:8}{mark}")
        print(f"budget: {ROW_BUDGET} rows per file")
        return 0
    if args.command == "split":
        if not args.term:
            raise SystemExit("split needs LAYER/FILE.md")
        for f in split(pack, args.term, args.each):
            print(f"wrote {f}")
        print("every task's merged glossary is unchanged; tasks.toml lists the new files after the old one")
        return 0
    if args.command == "snapshot":
        import json
        if args.term not in ("save", "compare") or not args.file:
            raise SystemExit("snapshot save|compare FILE.json")
        now = snapshot(pack)
        if args.term == "save":
            Path(args.file).write_text(json.dumps(now, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"saved {args.file}: " + ", ".join(f"{t} {len(r)} rows" for t, r in now.items()))
            return 0
        diff = snapshot_diff(json.loads(Path(args.file).read_text(encoding="utf-8")), now)
        for d in diff:
            print("DIFF  " + d)
        print(f"compared {len(now)} tasks: {len(diff)} differences")
        return 1 if diff else 0
    task = tasks(load_config()).get(args.task) if args.task else None
    names = args.names.split(",") if args.names else names_of(task, args.lang)
    rows = load(pack, names)
    if args.command == "coverage":
        if not (args.report or args.deck):
            raise SystemExit("coverage needs --report DIR or --deck MODULE.py")
        source, target = deliverable_text(pack, args.report, args.deck)
        drift = coverage(rows, source, target, args.min, args.ratio)
        for d in drift:
            r = d["row"]
            print(f"WARN  term drift: '{r['en']}' occurs {d['en']}× in the English, its form '{r['vi']}' "
                  f"{d['vi']}× in the translation ({d['share']:.0%}); the concept likely travels under other names "
                  f"– align them with the glossary ({r['layer']}/{r['file']})")
        print(f"Checked {sum(1 for r in rows if r.get('layer') != 'common')} task terms: {len(drift)} drifting")
        return 0
    if args.command == "lookup":
        t = (args.term or "").lower()
        rows = [r for r in rows if t in r["en"].lower() or t in r["vi"].lower()]
    for layer in LAYERS:
        part = [r for r in rows if r["layer"] == layer]
        if part and args.command == "show":
            print(f"===== {layer}: {len(part)} terms")
        for r in part:
            extra = (f"  [{r['usage']}]" if r["usage"] else "") + (f"  replaces: {', '.join(r['replaces'])}" if r["replaces"] else "")
            over = f"  (overrides {r['overrides']})" if r.get("overrides") else ""
            print(f"  {r['en']} → {r['vi']}{extra}{over}  ({layer}/{r['file']})")
    print(f"\n{len(rows)} terms from: {', '.join(['common'] + names)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
