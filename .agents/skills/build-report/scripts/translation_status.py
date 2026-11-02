"""Quick check of a report's translation into one language: which twins are missing or out of date.

Usage:
    translation_status.py --report DIR --lang vi [--all]                     list the files to translate, in order
    translation_status.py --report DIR --lang vi --mark FILE ...             record files whose parity check passes
    translation_status.py --report DIR --lang vi --mark-all                  record every existing pair as in sync

A twin is "missing" when it does not exist and "stale" when the source text changed after it was last recorded as
in sync. Sync points are content hashes in <report>/.<lang>-sync.json (written by --mark), so a file date alone
never marks a twin stale; without a recorded hash the file dates decide. Language-only pages (pack extra_files)
are listed separately and are never orphans. When work is pending, the output names the pack's guide and the
domain glossary to read first. Exit code 0 when every twin is up to date, 1 otherwise.
"""

import argparse
import hashlib
import json
import sys

import glossary
from check_parity import check_pair
from common import ROOT, is_extra, language_packs, section_files, source_language, task_for_report, twin, shown
from lang_rules import Rules


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True)
    ap.add_argument("--lang", required=True)
    ap.add_argument("--all", action="store_true", help="list every file, including those up to date")
    ap.add_argument("--mark", nargs="+", metavar="FILE")
    ap.add_argument("--mark-all", action="store_true")
    args = ap.parse_args()
    packs = language_packs()
    pack, source = packs[args.lang], packs[source_language(packs)]
    report = (ROOT / args.report).resolve()
    manifest_path = report / f".{args.lang}-sync.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    sources = section_files(report, source, packs)

    if args.mark or args.mark_all:
        targets = sources if args.mark_all else [report / f.split("/")[-1] for f in args.mark]
        done = 0
        rules = Rules(pack, source, glossary.for_task(pack, task_for_report(report)))
        for src in targets:
            if twin(src, pack).exists() and not args.mark_all:
                errors, _ = check_pair(src, twin(src, pack), pack, rules)
                if errors:
                    print(f"kept open {src.name}: {len(errors)} parity error(s), first: {errors[0][:90]}")
                    continue
            if twin(src, pack).exists():
                manifest[src.name] = digest(src)
                done += 1
            else:
                print(f"skip {src.name}: no {pack['name']} twin yet")
        manifest_path.write_text(json.dumps(dict(sorted(manifest.items())), indent=1) + "\n")
        print(f"recorded {done} file(s) in {shown(manifest_path)}")
        return 0

    pending = []
    for src in sources:
        tgt = twin(src, pack)
        if not tgt.exists():
            status = "missing"
        elif src.name in manifest:
            status = "ok" if manifest[src.name] == digest(src) else "stale"
        else:
            status = "stale" if src.stat().st_mtime > tgt.stat().st_mtime else "ok"
        if status != "ok":
            pending.append(src)
        if status != "ok" or args.all:
            print(f"{status:8s} {src.name}  ->  {tgt.name}")
    names = {s.name[:-3] for s in sources}
    targets = section_files(report, pack, packs)
    extras = [t.name for t in targets if is_extra(t.name, pack)]
    orphans = [t.name for t in targets if not is_extra(t.name, pack) and t.name[:-len(pack["suffix"])] not in names]
    for o in orphans:
        print(f"orphan   {o}  (no source file; delete or rename it)")
    if extras:
        print(f"{pack['name']}-only pages: {', '.join(extras)}")
    print(f"\n{len(sources)} sections, {len(pending)} need translation into {pack['name']} ({args.lang}), "
          f"{len(orphans)} orphaned files")
    if pending:
        guide = pack["_dir"] / pack.get("translation", {}).get("guide", "guide.md")
        names = glossary.names_of(task_for_report(report), args.lang)
        files = [str(shown(p)) for _, p in glossary.files_for(pack, names)]
        print(f"read first: {shown(guide)}; glossaries (common → domain → topic): {', '.join(files)}")
    return 1 if pending or orphans else 0


if __name__ == "__main__":
    sys.exit(main())
