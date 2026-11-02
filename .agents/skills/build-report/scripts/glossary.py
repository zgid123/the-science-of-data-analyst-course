"""Layered translation glossaries of a language pack: common → domains → topics.

Usage:
    glossary.py --lang vi [--task TASK | --names a,b] show            the merged glossary with each row's layer
    glossary.py --lang vi [--task TASK | --names a,b] lookup "term"   rows whose English or Vietnamese contains the term
    glossary.py --lang vi lint                                         check every glossary file of the pack
    glossary.py --lang vi --task TASK coverage --report DIR | --deck MODULE.py   term drift across a deliverable

Layers (languages/<code>/glossaries/): every file in common/ applies to every report; a task adds the domain and topic
files it names in tasks.toml ([taskN.<code>] glossaries = ["domain-name", "topic-name"]), looked up in domains/ and
then topics/. When the same English term appears in several layers, the more specific layer wins (topic > domain >
common), which lets a field fix its own sense of a general word. Rows are table rows | English | Vietnamese | Usage |
Replaces |; Replaces lists variants (comma-separated) that the language checks report as errors with the preferred
form. lint reports: malformed rows, an English term repeated within one file or translated differently in two common
files, a variant claimed by two different preferred forms, and a variant that is itself a preferred form elsewhere.

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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["show", "lookup", "lint", "coverage"])
    ap.add_argument("term", nargs="?")
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
        print(f"Checked {len(files)} glossary files, {sum(len(rows_of(p)) for p in files)} terms: {len(errors)} errors")
        return 1 if errors else 0
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
