"""Check that report text addresses the reader with information only, in each language's style.

Usage: python .claude/skills/build-report/scripts/check_style.py --report DIR [--lang CODE|all]

ERROR  meta commentary: a phrase from the pack's [style] meta_phrases (talk about the report, the reader, the
       outline or the writing process; planned runs or pending results in benchmark material).
WARN   the pack's [[style.warn]] patterns (for English: US spelling in an en-GB report).
ERROR  in a part whose H1 contains a [style.conclusion] heading word: narration about the report itself ("the report",
       "each part"), because a conclusion states what is now known about the subject.
WARN   in the same part: a sentence whose subject is a part or section ("Part 1 fixed…"); cross-reference pointers such
       as "(Section 3.5.8)" or "the analysis in Part 3" stay fine.
ERROR  voice: when the task sets `voice` ("group" or "solo") in tasks.toml, the writers name themselves in the first
       person, so a pack [style.voice] `self` pattern ("the team", "nhóm tác giả") in a sentence without a `cited`
       marker (a [n] citation, "et al", "cộng sự") is reported with the pack's voice line.
Body sections only; headings, quotations ("…" of 8+ characters), code, math, front matter and the reference list
are exempt, so quoted sources keep their own wording. Exit code 1 when any ERROR is found.
"""

import argparse
import re
import sys

from common import ROOT, language_packs, load_config, load_report, mask, task_languages, tasks, text_lines


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--report", required=True)
    ap.add_argument("--lang", default="all")
    args = ap.parse_args()
    packs = language_packs()
    folder = (ROOT / args.report).resolve()
    task = next((t for t in tasks(load_config()).values() if (ROOT / t["report"]).resolve() == folder), {})
    codes = (task_languages(task, packs) if task else list(packs)) if args.lang == "all" else [args.lang]
    failed = False
    for code in codes:
        pack = packs[code]
        style = pack.get("style", {})
        rep = load_report(folder, pack, packs)
        if not rep.files:
            continue
        meta = [re.compile(rf"(?<!\w){re.escape(p)}(?!\w)", re.I) for p in style.get("meta_phrases", [])]
        warn = [(re.compile(w["pattern"]), w["message"]) for w in style.get("warn", [])]
        errors, warns = [], []
        concl = style.get("conclusion", {})
        concl_parts = {h.file[:2] for h in rep.headings if h.level == 1
                       and any(w.lower() in h.text.lower() for w in concl.get("headings", []))}
        concl_meta = [re.compile(rf"(?<!\w){re.escape(p)}(?!\w)", re.I) for p in concl.get("phrases", [])]
        concl_subject = re.compile(concl["subject"]) if concl.get("subject") else None
        voice = style.get("voice", {})
        voice_line = voice.get(task.get("voice", ""), "")
        self_refs = [re.compile(x) for x in voice.get("self", [])] if voice_line else []
        cited = re.compile(voice["cited"]) if self_refs and voice.get("cited") else None
        for p in rep.body_files():
            in_conclusion = p.name[:2] in concl_parts
            for n, line, code_line in text_lines(p.read_text(encoding="utf-8")):
                if code_line or line.startswith(("#", "![")) or re.match(r"^\[\d+\]\s", line):
                    continue
                text = mask(line)
                for pat in meta:
                    for m in pat.finditer(text):
                        errors.append(f"{p.name}:{n}: meta commentary '{m.group(0)}': …{text[max(0, m.start() - 50):m.end() + 40].strip()}…")
                units = [] if not self_refs or line.lstrip().startswith(">") else (   # a blockquote quotes its source
                    [text] if text.lstrip().startswith("|") else re.split(r"(?<=[.!?;])\s+", text))  # a table row is one item
                for sentence in units:
                    if cited and cited.search(sentence):
                        continue
                    for pat in self_refs:
                        for m in pat.finditer(sentence):
                            errors.append(f"{p.name}:{n}: voice '{m.group(0)}' names the writers in the third person: "
                                          f"{voice_line} …{sentence[max(0, m.start() - 40):m.end() + 40].strip()}…")
                for pat, message in warn:
                    for m in pat.finditer(text):
                        warns.append(f"{p.name}:{n}: {message}: '{m.group(0)}'")
                if in_conclusion:
                    for pat in concl_meta:
                        for m in pat.finditer(text):
                            errors.append(f"{p.name}:{n}: conclusion narrates the report '{m.group(0)}': state what is known "
                                          f"about the subject: …{text[max(0, m.start() - 40):m.end() + 40].strip()}…")
                    for m in (concl_subject.finditer(text) if concl_subject else []):
                        warns.append(f"{p.name}:{n}: conclusion sentence led by '{m.group(0).strip(' .;:!?')}': lead with "
                                     f"the finding, cite the section as a pointer")
        print(f"===== {code.upper()}: {len(rep.body_files())} body files: {len(errors)} errors, {len(warns)} warnings")
        for e in errors:
            print("  ERROR " + e)
        for w in warns:
            print("  WARN  " + w)
        failed |= bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
