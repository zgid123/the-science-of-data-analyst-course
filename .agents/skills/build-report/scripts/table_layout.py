"""Printed text widths and line wrapping for report tables, shared by build_docx.py and check_docx.py.

Widths come from the fonts Word prints with, so a column is sized to what it holds: capitals, bold headers and
monospaced identifiers run wider than an average character. Where a font file is missing the width falls back to
an average per character, so the build still works; the columns are then only less exact.
"""
from __future__ import annotations

import math
import os
import re

from PIL import ImageFont

FONT_DIRS = ["/System/Library/Fonts/Supplemental", "/Library/Fonts", "/usr/share/fonts/truetype/msttcorefonts",
             "C:/Windows/Fonts"]
FONT_FILES = {"regular": ("Times New Roman.ttf", "times.ttf"), "bold": ("Times New Roman Bold.ttf", "timesbd.ttf"),
              "mono": ("Courier New.ttf", "cour.ttf")}
FALLBACK_EM = {"regular": 0.47, "bold": 0.52, "mono": 0.6}     # average character width where a font file is missing
LONG_WORD_PT = 104.0           # about 3.7 cm: a longer token (URL, hash) may wrap inside its cell rather than widen it
WRAP_GUARD = 0.97              # Word and this measurement drift a little, so lines count as slightly shorter
_FONTS: dict = {}
ZWSP = "\u200b"                # zero-width space: a break opportunity Word honours inside a long identifier
WORD_BREAK = re.compile(r"(?<=[^\W\d_][-–])(?=[^\W\d_])|(?<=\u200b)")   # after a hyphen between letters; after ZWSP
SOFT_POINT = re.compile(r"(?<=[./])(?=[^\s.,;:)\]/])")    # after a dot or slash inside a token
LINK_TOKEN = re.compile(r"^\W*(https?://|doi:|10\.\d{4,}/|www\.|[\w-]+(\.[\w-]+)+/|[\w-]+(\.[\w-]+)*\.(com|org|net|edu|io|ac\.uk|uk|cn)\b)")   # copied from the page, so no hidden characters
SOFT_UNDERSCORE = re.compile(r"(?<=_)(?=[^\s_.,;:)\]])")     # after an underscore, only in a part still too long


def _font(kind: str):
    if kind not in _FONTS:
        _FONTS[kind] = None
        for d in FONT_DIRS:
            for name in FONT_FILES[kind]:
                if os.path.exists(f"{d}/{name}"):
                    _FONTS[kind] = ImageFont.truetype(f"{d}/{name}", 200)
                    break
            if _FONTS[kind] is not None:
                break
    return _FONTS[kind]


def text_pt(text: str, size: float, bold: bool = False, mono: bool = False) -> float:
    """Printed width of one line of text, in points."""
    kind = "mono" if mono else "bold" if bold else "regular"
    font = _font(kind)
    return font.getlength(text) * size / 200 if font else len(text) * FALLBACK_EM[kind] * size


def soft_break(word: str, size: float, bold: bool = False, mono: bool = False) -> str:
    """A token longer than LONG_WORD_PT (a dotted or snake_case identifier, a path) with break points after its dots
    and slashes, and after the underscores of any part still longer than that, so Word breaks it at a name boundary
    instead of at an arbitrary letter. A URL or a DOI stays as it is: a reader copies it, and a zero-width space
    would travel with the copy and break the link."""
    if ZWSP in word or LINK_TOKEN.match(word) or text_pt(word, size, bold, mono) <= LONG_WORD_PT:
        return word
    parts = SOFT_POINT.sub(ZWSP, word).split(ZWSP)
    return ZWSP.join(SOFT_UNDERSCORE.sub(ZWSP, p) if text_pt(p, size, bold, mono) > LONG_WORD_PT else p for p in parts)


def unbroken(word: str) -> list[str]:
    """The parts of a word that Word keeps on one line."""
    return WORD_BREAK.split(word)


def word_widths(text: str, size: float, bold: bool = False, mono_words=frozenset()) -> list[list[float]]:
    """The width of each unbroken part of a word, paragraph by paragraph."""
    return [[text_pt(part, size, bold, w in mono_words) for w in para.split() for part in unbroken(w)]
            for para in text.split("\n")]


def count_lines(paras: list[list[float]], inner_pt: float, size: float) -> int:
    """Lines a cell takes at a text width of inner_pt, greedy like Word; a token wider than the cell breaks."""
    space, room, lines = 0.25 * size, max(1.0, inner_pt * WRAP_GUARD), 0
    for words in paras:
        used = None
        lines += 1
        for w in words:
            if w > room:
                lines += (0 if used is None else 1) + math.ceil(w / room) - 1
                used = w % room or room
            elif used is None:
                used = w
            elif used + space + w <= room:
                used += space + w
            else:
                lines += 1
                used = w
    return lines
