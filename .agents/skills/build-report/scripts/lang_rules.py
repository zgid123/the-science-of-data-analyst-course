"""Language conventions of a target-language pack, applied to any text (markdown sources, Word text, slides).

The rules come from the pack's [conventions] table, so a new language adds data, not code:
  decimal = "comma"          a decimal point is an error, except after reference words (Mục 3.5), in standard codes,
                             versions (v4.1, phiên bản 4.1), licences (CC BY-NC 4.0) and thousands groups (10.000)
  glossary = {regex = form}  a language-wide variant of a fixed term is an error that names the form to use; the
                             glossaries' Replaces columns (glossary.py) add the variants of the task's layers
  [[warn]] pattern/message   style warnings (for Vietnamese: modern tone placement); `only = "slides"` limits a
                             warning to slide decks, where presenters and the authors under review meet
  check_untranslated         a line dense with the source language's function words reads as untranslated
  source_references          "warn" or "error" for source-language references such as "Figure 2.1"
Every rule skips quotations ("…" of 8+ characters), inline code, math and snake_case identifiers.
"""

from __future__ import annotations

import re

QUOTE = re.compile(r'"[^"]{8,}?"|“[^”]{8,}?”')
CODE_SPAN = re.compile(r"`[^`]*`")
INLINE_MATH = re.compile(r"(?<!\$)\$(?![\s$])[^$\n]+?(?<!\s)\$(?![\d$])")    # pandoc rule: "$30 | $300" is not math
DISPLAY_MATH = re.compile(r"\$\$.+?\$\$", re.S)
IDENT = re.compile(r"\b\w*_\w+\b")
DECIMAL = re.compile(r"(?<![\w.,/\[-])\d+\.\d+(?![\w.]|-\d)")    # "Llama 3.1-8B" names a model, not a decimal
THOUSANDS = re.compile(r"\d{1,3}(?:\.\d{3})+")
REF_NUM = r"(?:\d+|[IVX]+|[A-Z])(?![A-Za-z])(?:\.\d+)*"   # "Phụ lục A", not the "G" of "mô hình Gemini 1.5"


class Rules:
    def __init__(self, pack: dict, source: dict, variants: list[tuple[str, str]] | None = None, scope: str = "report"):
        conv = pack.get("conventions", {})
        self.pack, self.conv = pack, conv
        self.decimal_comma = conv.get("decimal") == "comma"
        words = "|".join(map(re.escape, conv.get("reference_words", [])))
        versions = "|".join(map(re.escape, conv.get("version_words", ["version"])))
        joins = "|".join(map(re.escape, [c.strip() for c in pack.get("connectors", []) if c.strip() not in (",", "–")]))
        exempt = [r"(?:ISO/IEC|ISO|CEN/TS|IEC|IEEE)\s*[\d.:-]+", r"\bv\d[\d.]*", rf"(?i:{versions})\s+\d[\d.]*",
                  r"\bCC BY(?:-[A-Z]{2})*\s+\d[\d.]*",
                  r"\b10\.\d{4,9}/\S+",                          # DOIs: 10.18653/v1/…
                  r"(?i:arXiv)[:\s]*\d{4}\.\d{4,5}(?:v\d+)?",       # arXiv identifiers: arXiv 2412.06724
                  r"\b[A-Z][A-Za-z]*[a-z][A-Za-z]*\s+\d+(?:\.\d+)+\b"]  # product versions: Llama 3.3, OpenRefine 3.9
        if words:
            exempt.insert(0, rf"(?i:{words})\s+{REF_NUM}(?:(?:–|,\s*|\s+(?:{joins or 'và'})\s+)(?:(?i:{words})\s+)?{REF_NUM})*")
        self.exempt = re.compile("|".join(exempt))
        self.glossary = [(re.compile(k), v) for k, v in conv.get("glossary", {}).items()]
        self.glossary += [(re.compile(rf"(?<!\w){re.escape(v)}(?!\w)"), form) for v, form in (variants or [])]
        self.warn = [(re.compile(w["pattern"], re.I), w["message"]) for w in conv.get("warn", [])
                     if w.get("only", scope) == scope]
        # A source-language reference reads correctly in the source language itself, so only target languages check it.
        src_words = [] if source is pack else [w for k in ("figure", "table", "section", "appendix", "part") for w in source.get(k, [])]
        self.source_ref = re.compile(rf"\b({'|'.join(map(re.escape, src_words))})\s+[A-Z0-9IVX]+(\.\d+)*") if src_words else None
        self.ref_level = conv.get("source_references", "warn")
        fw = source.get("function_words", [])
        self.function = re.compile(rf"\b({'|'.join(map(re.escape, fw))})\b", re.I) if fw and conv.get("check_untranslated") else None

    @staticmethod
    def clean(text: str) -> str:
        """Text with code, math and identifiers blanked (quotations kept)."""
        text = CODE_SPAN.sub(" ", DISPLAY_MATH.sub(" ", text))
        return IDENT.sub(" ", INLINE_MATH.sub(" ", text))

    def check(self, text: str, heading: bool = False, ref_level: str | None = None) -> tuple[list[str], list[str]]:
        """Errors and warnings for one line or paragraph of target-language text."""
        errors, warns = [], []
        unquoted = QUOTE.sub(" ", self.clean(text))
        level = ref_level or self.ref_level
        if self.source_ref and not heading:
            for m in self.source_ref.finditer(unquoted):
                (errors if level == "error" else warns).append(
                    f"source-language reference '{m.group(0)}' (use {'/'.join(self.pack[k][0] for k in ('figure', 'table', 'section', 'appendix', 'part'))})")
        if self.decimal_comma and not heading:
            for m in DECIMAL.finditer(self.exempt.sub(" ", unquoted)):
                if not THOUSANDS.fullmatch(m.group(0)):
                    errors.append(f"decimal point '{m.group(0)}' (use a decimal comma)")
        for pattern, preferred in self.glossary:
            # a variant that is part of its own preferred form ("biến thể trùng" in "biến thể trùng lặp") is not an error
            spans = [(k.start(), k.end()) for k in re.finditer(re.escape(preferred), unquoted)] \
                if isinstance(preferred, str) and preferred else []
            for m in pattern.finditer(unquoted):
                if not any(a <= m.start() and m.end() <= b for a, b in spans):
                    errors.append(f"glossary '{m.group(0)}' -> '{preferred}'")
        for pattern, message in self.warn:
            for m in pattern.finditer(unquoted):
                warns.append(f"{message}: '{m.group(0)}'")
        if self.function and not heading:
            words = re.findall(r"[^\W\d_]+", unquoted)
            hits = len(self.function.findall(unquoted))
            if len(words) >= 8 and hits >= 4 and hits / len(words) > 0.12:
                warns.append(f"looks untranslated: '{unquoted.strip()[:70]}'")
        return errors, warns
