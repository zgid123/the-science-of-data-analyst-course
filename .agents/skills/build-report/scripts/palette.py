"""One colour set for every report figure, chart and slide (c4kit, diagrams, charts, icons, slidekit).

Colours are hex strings ("#2A6FBB"). Each colour does one job:

- text and structure: INK (text), MUTED (secondary text), GRID, LINE (borders), SOFT (panels), SURFACE (page);
- series identity (categorical): SERIES, six hues in a fixed order, assigned in sequence and never cycled. The order
  passes the colour-vision checks of a categorical palette on a white page: every slot inside the lightness band,
  chroma at least 0.10, adjacent pairs at least 11.8 apart (OKLab x 100) under simulated protanopia and deuteranopia
  and 19.7 with normal vision, and every slot at 3:1 or more against white, so white text on a slot fill reads at
  4:1 or more. Any three of the first three slots may sit side by side in any arrangement (scatter, Venn), since
  they pass the all-pairs check too. A seventh series folds into "Other" (OTHER) or a second chart;
- magnitude: sequential(n) steps of one hue, light to dark; polarity: diverging(n), two hues around a grey midpoint;
- state: STATUS good / warning / critical, reserved for state and always paired with an icon and a word, because
  red and green alone part only for readers with full colour vision;
- diagram roles: ROLES (fill, text) and LIGHT (fill, text, edge) for C4 boxes and slide nodes; a role keeps its
  colour in every figure of a report and on its slides.

Re-validate after changing a slot with a categorical palette validator (lightness band, chroma floor, adjacent
colour-vision separation, normal-vision floor, contrast against white).
"""

from __future__ import annotations

# ----------------------------------------------------------------------------- text and structure
INK = "#2B2F36"          # body text, values, labels
MUTED = "#5F6670"        # secondary text, axis ticks, captions
GRID = "#D9DDE3"         # gridlines and baselines
LINE = "#C9CED6"         # borders of labels and light boxes
SOFT = "#F4F6F9"         # panel backgrounds
SURFACE = "#FFFFFF"      # the page
NAVY = "#1F3864"         # titles and emphasis blocks (slide titles, take-home boxes)
CONNECTOR = "#4A5260"    # arrows and connectors

# ----------------------------------------------------------------------------- series identity (fixed order)
BLUE = "#2A6FBB"         # slot 1: the baseline, a system
ORANGE = "#C65F17"       # slot 2: the method under study, an agent
TEAL = "#0E8F78"         # slot 3
VIOLET = "#7458C2"       # slot 4
GOLD = "#A37200"         # slot 5
MAGENTA = "#C5457E"      # slot 6
SERIES = [BLUE, ORANGE, TEAL, VIOLET, GOLD, MAGENTA]
OTHER = "#9AA1AA"        # "Other", a reference or a context series (always labelled)

# ----------------------------------------------------------------------------- state (reserved)
GOOD = "#2E7D4F"
WARNING = "#C98500"       # a brighter amber than GOLD, so state never reads as series 5
CRITICAL = "#B23A48"
STATUS = {"good": GOOD, "warning": WARNING, "critical": CRITICAL}
STATUS_ICON = {"good": "check", "warning": "warning", "critical": "cross"}

# ----------------------------------------------------------------------------- diagram roles
PERSON = "#0B3D6B"
SYSTEM_DARK = "#1F5FAD"
EXTERNAL = "#7D838C"
STORE = "#5A6B7D"

ROLES = {                # role: (fill, text) for solid boxes
    "person": (PERSON, "white"),
    "system": (SYSTEM_DARK, "white"),
    "external": (EXTERNAL, "white"),
    "warehouse": (BLUE, "white"),
    "lake": (GOOD, "white"),
    "agent": (ORANGE, "white"),
    "ingest": (VIOLET, "white"),
    "review": (TEAL, "white"),
    "store": (STORE, "white"),
    "critical": (CRITICAL, "white"),
}


def mix(a: str, b: str, t: float) -> str:
    """The colour t of the way from a to b (0 gives a, 1 gives b), mixed in sRGB."""
    pa = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    pb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(pa, pb))


def _to_oklab(c):
    r, g, b = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in (r, g, b)]
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def _from_oklab(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb_ = (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)
    out = []
    for x in rgb_:
        x = min(max(x, 0.0), 1.0)
        out.append(12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055)
    return "#" + "".join(f"{round(x * 255):02X}" for x in out)


def blend(a: str, b: str, t: float) -> str:
    """The colour t of the way from a to b mixed perceptually (OKLab), so ramps keep their hue and stay even."""
    A, B = _to_oklab(a), _to_oklab(b)
    return _from_oklab(*(x + (y - x) * t for x, y in zip(A, B)))


def tint(c: str, t: float = 0.85) -> str:
    """A light tint of c for fills behind dark text (t = share of white)."""
    return mix(c, SURFACE, t)


def shade(c: str, t: float = 0.45) -> str:
    """A dark shade of c for text on its tint (t = share of black)."""
    return mix(c, "#000000", t)


LIGHT = {role: (tint(fill), shade(fill, 0.5), fill) for role, (fill, _) in ROLES.items()}   # (fill, text, edge)


def series(n: int) -> list[str]:
    """The first n series colours in their fixed order; more than six series fold into "Other" or a second chart."""
    if n > len(SERIES):
        raise ValueError(f"{n} series: fold the smallest into 'Other' (OTHER) or split the chart; six is the limit")
    return SERIES[:n]


def sequential(n: int, hue: str = BLUE) -> list[str]:
    """n steps of one hue from light to dark (magnitude), the lightest still visible on white."""
    if n == 1:
        return [hue]
    return [blend(blend(hue, SURFACE, 0.86), blend(hue, "#000000", 0.38), k / (n - 1)) for k in range(n)]


def diverging(n: int, low: str = ORANGE, high: str = BLUE, mid: str = "#E4E6EA") -> list[str]:
    """n steps (odd n has a grey midpoint) from `low` through a neutral grey to `high` (polarity around a baseline)."""
    half = n // 2
    lo = [blend(blend(low, "#000000", 0.15), mid, k / half) for k in range(half)]
    hi = [blend(mid, blend(high, "#000000", 0.15), (k + 1) / half) for k in range(half)]
    return lo + ([mid] if n % 2 else []) + hi


def cmap(colors: list[str], name: str = "kit"):
    """A matplotlib colormap through the given colours (e.g. sequential(7) for a heatmap)."""
    from matplotlib.colors import LinearSegmentedColormap
    return LinearSegmentedColormap.from_list(name, colors)


def rgb(c: str):
    """python-pptx RGBColor of a hex colour."""
    from pptx.dml.color import RGBColor
    return RGBColor.from_string(c.lstrip("#").upper())


def text_on(fill: str) -> str:
    """INK or white, whichever reads better on `fill` (WCAG relative luminance)."""
    def lum(c):
        ch = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        ch = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in ch]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
    on_white = (1.05) / (lum(fill) + 0.05)
    on_ink = (lum(fill) + 0.05) / (lum(INK) + 0.05)
    return "#FFFFFF" if on_white >= on_ink else INK
