"""Ready-made diagram types, each sized from its measured text so nothing overflows and no space is wasted. Every
function returns a Scene (scene.py), which renders either as an image or as native PowerPoint shapes:

    import diagrams as dg
    sc = dg.process([("Profile", "Inspect the input", "search"), ("Plan", "Choose one step", "agent")])
    sc.save(out)                                          # a report figure (PNG), checked
    sc = dg.process(steps, width=12.7, medium="slide")    # slide type sizes
    sc.to_slide(slide, x=0.3, y=1.5)                      # native, editable shapes

| Function | Shows | Use it for |
| :---- | :---- | :---- |
| sequence | messages between participants over time, numbered | a request flow, a protocol |
| timeline | dated events on one axis, cards above and below | history, a roadmap, a policy chronology |
| state_machine | states on a grid and the transitions between them | a life cycle, a session, a payment |
| process | numbered steps in a row, each with an icon | a method, a pipeline, a procedure |
| cycle | steps around a loop | an iterative method, a feedback loop |
| matrix | support or ratings of items against criteria | a comparison of methods, tools or standards |
| layers | a stack of layers with their components | an architecture, a protocol stack |
| compare | two contrasting panels with an arrow between | before and after, problem and solution |
| screenshot | an image with numbered markers and their notes | a user interface, a photo, a scanned page |

Type sizes follow the medium (scene.TYPE): in a report names 9.5 pt bold, text 8 pt, small 7.5 pt (never below 6 pt
printed); on a slide 16, 14 and 12 pt. Spacing scales with the type. Text arguments arrive already in the build
language; icons are names from icons.py; roles are palette.ROLES keys.
"""

from __future__ import annotations

import math

import palette as P
from palette import LIGHT, ROLES
from scene import Scene, edge_point

WIDTH = {"report": 6.3, "slide": 12.7}
MAX_H = 19 / 2.54 - 0.05                                # the tallest figure a portrait page prints at full size


def _scale(medium):
    """Spacing unit: 1 in a report, larger on a slide in step with the type."""
    return 1.0 if medium == "report" else 1.6


def _width(width, medium):
    return width or WIDTH[medium]


# ----------------------------------------------------------------------------- sequence
KINDS = {"call": (P.CONNECTOR, False), "reply": (P.CONNECTOR, True), "event": (P.ORANGE, True)}


def _sequence_rows(sc, steps, xs, pitch, width, m, head_h, gap, u):
    rows, y = [], head_h + 0.22 * u
    num_ = 0
    for st in steps:
        kind = st[0]
        if kind in KINDS:
            a, b, text = st[1], st[2], st[3]
            span = abs(xs[a] - xs[b])
            lw_ = max(span - 0.3 * u, min(1.7 * u, width / 3))
            th = sc.text_h(text, lw_, "small")
            num_ += 1
            rows.append((kind, a, b, text, lw_, y, y + th + 0.14 * u, num_))   # room for the badge under the label
            y += th + gap
        elif kind == "self":
            a, text = st[1], st[2]
            right = width - xs[a] - 0.5 * u >= min(1.7 * u, sc.width_of(text, "small") + 0.1)
            room = (width - xs[a] - 0.5 * u) if right else (xs[a] - 0.5 * u)
            lw_ = max(0.9 * u, min(1.7 * u, room))
            th = sc.text_h(text, lw_, "small")
            num_ += 1
            rows.append((kind, a, 1 if right else -1, text, lw_, y, y, num_))
            y += max(th, 0.22 * u) + gap - 0.06 * u
        elif kind == "note":
            a, b, text = st[1], st[2], st[3]
            x0 = max(min(xs[a], xs[b]) - pitch * 0.42, m)
            x1 = min(max(xs[a], xs[b]) + pitch * 0.42, width - m)
            th = sc.text_h(text, x1 - x0 - 0.16 * u, "small")
            rows.append((kind, x0, x1, text, x1 - x0, y, y + th + 0.12 * u, None))
            y += th + 0.28 * u
        elif kind == "divider":
            rows.append((kind, None, None, st[1], width, y, y, None))
            y += 0.32 * u
    return rows, y


def sequence(participants, steps, width=None, legend=None, number=True, medium="report"):
    """Participants are (name, role) or (name, role, icon); steps are tuples:
    ("call" | "reply" | "event", a, b, text) for a message from participant a to b (indices),
    ("self", a, text) for work a participant does on itself, ("note", a, b, text) for a note over a..b,
    ("divider", text) for a phase label across the diagram. Messages are numbered in order (number=False to omit);
    labels wrap to the span of their arrow and sit on a plate, so lifelines never run through them. `legend` maps
    a used kind to its word, e.g. {"call": "call", "reply": "reply", "event": "notification"}. In a report, the row
    spacing tightens when the diagram would be taller than a portrait page."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    n = len(participants)
    m = 0.1 * u
    pitch = (width - 2 * m) / n
    xs = [m + pitch * (k + 0.5) for k in range(n)]
    hw = pitch - 0.1 * u
    has_icon = any(len(p) > 2 and p[2] for p in participants)
    isz = 0.26 * u
    head_h = max(probe.text_h(p[0], hw - 0.12 * u, "name", True) for p in participants) + 0.2 * u + \
        (isz + 0.04 * u if has_icon else 0)
    leg_h = 0.32 * u if legend else 0
    for gap in ((0.30, 0.27) if medium == "report" else (0.32 * u,)):
        rows, y = _sequence_rows(probe, steps, xs, pitch, width, m, head_h, gap, u)
        if y + 0.08 * u + leg_h <= MAX_H or medium != "report":
            break
    used = [k for k in KINDS if any(r[0] == k for r in rows)]
    total = y + 0.08 * u + leg_h
    sc = Scene(width, total, medium)
    for k, p in enumerate(participants):
        fill, txt = ROLES[p[1]]
        sc.rect(xs[k] - hw / 2, 0.05, hw, head_h - 0.05, fill=fill, r=0.06 * u, z=5)
        ty = 0.05 + 0.1 * u
        if has_icon and len(p) > 2 and p[2]:
            sc.icon(p[2], xs[k] - isz / 2, ty, isz, color=txt, bg=fill)
        if has_icon:
            ty += isz + 0.04 * u
        sc.text(xs[k], ty, p[0], hw - 0.12 * u, "name", True, txt, align="center", z=6)
        sc.line([(xs[k], head_h), (xs[k], y)], color=P.GRID, lw=1.0, dashed=True, z=1)
    br = sc.pt("badge") * 0.92 / 72
    for kind, a, b, text, lw_, top, ay, nr in rows:
        if kind in KINDS:
            color, dashed = KINDS[kind]
            d = 1 if xs[b] > xs[a] else -1
            x0 = xs[a] + ((2 * br) * d if number else 0)
            sc.line([(x0, ay), (xs[b] - 0.02 * d, ay)], color, 1.2, dashed, head=True, z=4)
            if number:
                sc.badge(xs[a] + br * d, ay, nr)
            sc.text((xs[a] + xs[b]) / 2, top, text, lw_, "small", align="center", plate=P.SURFACE, z=6)
        elif kind == "self":
            x, d = xs[a], b
            lo = 0.3 * u
            sc.line([(x, top + 0.02), (x + lo * d, top + 0.02), (x + lo * d, top + 0.2 * u),
                     (x + 0.02 * d, top + 0.2 * u)], P.CONNECTOR, 1.2, head=True, z=4)
            if number:
                sc.badge(x, top + 0.02, nr)
            if d > 0:
                sc.text(x + lo + 0.08 * u, top, text, lw_, "small", plate=P.SURFACE, z=6)
            else:
                sc.text(x - lo - 0.08 * u, top, text, lw_, "small", align="right", plate=P.SURFACE, z=6)
        elif kind == "note":
            sc.rect(a, top, lw_, ay - top, fill=P.SOFT, edge=P.LINE, r=0.05 * u, lw=0.8, z=5)
            sc.text(a + 0.08 * u, top + 0.06 * u, text, lw_ - 0.16 * u, "small", z=6)
        elif kind == "divider":
            sc.line([(m, top + 0.12 * u), (width - m, top + 0.12 * u)], P.LINE, 1.0, dashed=True, z=2)
            sc.text(width / 2, top + 0.03 * u, text, width * 0.6, "small", True, P.MUTED, align="center",
                    plate=P.SURFACE, z=6)
    if legend:
        x, ly = m, total - 0.18 * u
        for k in used:
            if k not in legend:
                continue
            color, dashed = KINDS[k]
            sc.line([(x, ly), (x + 0.4 * u, ly)], color, 1.2, dashed)
            sc.text(x + 0.48 * u, ly - sc.text_h("x", 1, "small") / 2, legend[k], 3 * u, "small")
            x += 0.6 * u + sc.width_of(legend[k], "small") + 0.25 * u
    return sc


# ----------------------------------------------------------------------------- timeline
def timeline(events, width=None, color=P.BLUE, medium="report"):
    """events: (when, title) or (when, title, text) or (when, title, text, color), in order. The cards alternate
    above and below the axis, so each may be twice as wide as the spacing between events."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    n = len(events)
    g = 0.14 * u
    pitch = (width + g - 0.1) / (n + 1)
    cw = 2 * pitch - g
    m = (cw - pitch) / 2 + 0.05
    xs = [m + pitch * (k + 0.5) for k in range(n)]
    pad = 0.08 * u
    hs = []
    for ev in events:
        h = 0.1 * u + probe.text_h(ev[0], cw - 2 * pad, "small", True) + 0.02 * u + \
            probe.text_h(ev[1], cw - 2 * pad, "text", True)
        if len(ev) > 2 and ev[2]:
            h += 0.04 * u + probe.text_h(ev[2], cw - 2 * pad, "small")
        hs.append(h + 0.1 * u)
    above = max([hs[k] for k in range(0, n, 2)] or [0])
    below = max([hs[k] for k in range(1, n, 2)] or [0])
    stem = 0.22 * u
    axis_y = 0.05 + above + stem
    sc = Scene(width, axis_y + stem + below + 0.08, medium)
    sc.line([(0.05, axis_y), (width - 0.05, axis_y)], P.LINE, 2.2 * u, z=2)
    for k, ev in enumerate(events):
        c = ev[3] if len(ev) > 3 and ev[3] else color
        x = xs[k]
        up = k % 2 == 0
        top = axis_y - stem - hs[k] if up else axis_y + stem
        left = x - cw / 2
        sc.line([(x, axis_y), (x, top + hs[k] if up else top)], c, 1.0, z=2)
        sc.ellipse(x, axis_y, 0.14 * u, 0.14 * u, fill=c, edge=P.SURFACE, lw=1.4, z=4)
        sc.rect(left, top, cw, hs[k], fill=P.tint(c, 0.9), edge=P.tint(c, 0.55), r=0.06 * u, lw=0.8, z=3)
        y = top + 0.1 * u
        y += sc.text(left + pad, y, ev[0], cw - 2 * pad, "small", True, P.shade(c, 0.25)) + 0.02 * u
        y += sc.text(left + pad, y, ev[1], cw - 2 * pad, "text", True) + 0.04 * u
        if len(ev) > 2 and ev[2]:
            sc.text(left + pad, y, ev[2], cw - 2 * pad, "small", color=P.MUTED)
    return sc


# ----------------------------------------------------------------------------- state machine
def state_machine(states, transitions, width=None, start=None, ends=(), cell_h=None, roles=None, medium="report"):
    """states: {name: (col, row)} on a grid; transitions: (from, to, label); `start` gets an initial dot and `ends`
    a double border; roles maps a state to a palette role (default: light system). Two transitions between the same
    pair run side by side; a transition from a state to itself loops above it."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    cell_h = cell_h or 1.15 * u
    cols = max(c for c, _ in states.values()) + 1
    rows_n = max(r for _, r in states.values()) + 1
    lead = 0.45 * u if start else 0.1
    cell_w = (width - lead - 0.1) / cols
    bw = min(cell_w * 0.5, 1.6 * u)
    bh = max(probe.text_h(s, bw - 0.16 * u, "text", True) for s in states) + 0.24 * u
    loops = any(a == b for a, b, _ in transitions)
    top_pad = 0.62 * u if loops else 0.12
    sc = Scene(width, top_pad + rows_n * cell_h - (cell_h - bh) + 0.15, medium)
    centre = {s: (lead + cell_w * (c + 0.5), top_pad + bh / 2 + r * cell_h) for s, (c, r) in states.items()}
    for s, (x, y) in centre.items():
        fill, txt, edge = LIGHT[(roles or {}).get(s, "system")]
        sc.rect(x - bw / 2, y - bh / 2, bw, bh, fill=fill, edge=edge, r=0.12 * u, lw=1.3, z=4)
        if s in ends:
            d = 0.05 * u
            sc.rect(x - bw / 2 + d, y - bh / 2 + d, bw - 2 * d, bh - 2 * d, edge=edge, r=0.09 * u, lw=0.9, z=5)
        th = sc.text_h(s, bw - 0.16 * u, "text", True)
        sc.text(x, y - th / 2, s, bw - 0.16 * u, "text", True, txt, align="center", z=6)
    if start:
        x, y = centre[start]
        sc.ellipse(x - bw / 2 - 0.32 * u, y, 0.14 * u, 0.14 * u, fill=P.INK, z=4)
        sc.line([(x - bw / 2 - 0.25 * u, y), (x - bw / 2, y)], head=True, z=4)
    pairs = {(a, b) for a, b, _ in transitions}
    for a, b, label in transitions:
        if a == b:
            x, y = centre[a]
            top, rise = y - bh / 2, 0.26 * u                 # a three-sided loop above the box
            sc.line([(x - 0.2 * u, top), (x - 0.2 * u, top - rise), (x + 0.2 * u, top - rise), (x + 0.2 * u, top)],
                    head=True, z=4)
            lh = sc.text_h(label, 1.4 * u, "small")
            sc.text(x, top - rise - 0.06 * u - lh, label, 1.4 * u, "small", align="center", plate=P.SURFACE, z=7)
            continue
        ca, cb = centre[a], centre[b]
        paired = (b, a) in pairs
        dx, dy = cb[0] - ca[0], cb[1] - ca[1]
        L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        off = 0.09 * u if paired else 0.0
        sa, sb = (ca[0] + nx * off, ca[1] + ny * off), (cb[0] + nx * off, cb[1] + ny * off)
        pa = edge_point(sa, bw / 2, bh / 2, sb)
        pb = edge_point(sb, bw / 2, bh / 2, sa)
        sc.line([pa, pb], head=True, z=4)
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
        free = math.hypot(pb[0] - pa[0], pb[1] - pa[1])
        if abs(dx) >= abs(dy):
            lw_ = max(0.9 * u, min(1.6 * u, free - 0.1))
            lh = sc.text_h(label, lw_, "small")
            above = ny < 0 if paired else True
            sc.text(mx, my - 0.05 * u - lh if above else my + 0.05 * u, label, lw_, "small", align="center",
                    plate=P.SURFACE, z=7)
        else:
            lw_ = max(0.8 * u, min(1.4 * u, cell_w - bw / 2 - 0.2))
            lh = sc.text_h(label, lw_, "small")
            right = nx < 0 if paired else True
            if right:
                sc.text(mx + 0.08 * u, my - lh / 2, label, lw_, "small", plate=P.SURFACE, z=7)
            else:
                sc.text(mx - 0.08 * u, my - lh / 2, label, lw_, "small", align="right", plate=P.SURFACE, z=7)
    return sc


# ----------------------------------------------------------------------------- process and cycle
def process(steps, width=None, role="system", arrows=True, medium="report"):
    """steps: (title, text) or (title, text, icon): numbered cards in a row joined by arrows."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    n = len(steps)
    gap = (0.26 if arrows else 0.12) * u
    cw = (width - 0.1 - gap * (n - 1)) / n
    fill, txt, edge = LIGHT[role]
    has_icon = any(len(s) > 2 and s[2] for s in steps)
    isz = 0.3 * u
    ih = isz + 0.06 * u if has_icon else 0
    inner = cw - 0.16 * u
    h = max(0.22 * u + ih + probe.text_h(s[0], inner, "text", True) + 0.05 * u +
            probe.text_h(s[1] if len(s) > 1 else "", inner, "small") for s in steps) + 0.12 * u
    top = 0.12 * u
    sc = Scene(width, h + top + 0.08, medium)
    for k, s in enumerate(steps):
        x = 0.05 + k * (cw + gap)
        sc.rect(x, top, cw, h, fill=fill, edge=edge, r=0.08 * u, lw=1.1, z=3)
        sc.badge(x + 0.04 * u, top + 0.04 * u, k + 1, edge)
        y = top + 0.18 * u
        if has_icon and len(s) > 2 and s[2]:
            sc.icon(s[2], x + cw / 2 - isz / 2, y, isz, color=edge, bg=fill)
        y += ih
        y += sc.text(x + cw / 2, y, s[0], inner, "text", True, txt, align="center") + 0.05 * u
        if len(s) > 1 and s[1]:
            sc.text(x + cw / 2, y, s[1], inner, "small", align="center")
        if arrows and k + 1 < n:
            sc.line([(x + cw + 0.03 * u, top + h / 2), (x + cw + gap - 0.03 * u, top + h / 2)], head=True, z=4)
    return sc


def cycle(steps, width=None, centre=None, role="agent", medium="report"):
    """steps: (title, text) placed clockwise around a loop from the top, joined by curved arrows; `centre` is an
    optional label in the middle (what the loop achieves)."""
    width = width or (4.6 if medium == "report" else 7.0)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    n = len(steps)
    fill, txt, edge = LIGHT[role]
    bw = min(1.55 * u, width * 0.36)
    inner = bw - 0.14 * u
    bh = max(probe.text_h(s[0], inner, "text", True) +
             (0.04 * u + probe.text_h(s[1], inner, "small") if len(s) > 1 and s[1] else 0) for s in steps) + 0.2 * u
    R = max(0.85 * u, (bw * 0.9) / (2 * math.sin(math.pi / n)) if n > 2 else u)
    if centre:
        R = max(R, bw / 2 + probe.width_of(centre, "text", True) / 2 + 0.25 * u)
    height = 2 * R + bh + 0.3 * u
    sc = Scene(width, height, medium)
    cx, cy = width / 2, height / 2
    pts = [(cx + R * math.sin(2 * math.pi * k / n), cy - R * math.cos(2 * math.pi * k / n)) for k in range(n)]
    for k in range(n):
        a, b = pts[k], pts[(k + 1) % n]
        pa = edge_point(a, bw / 2 + 0.04 * u, bh / 2 + 0.04 * u, b)
        pb = edge_point(b, bw / 2 + 0.04 * u, bh / 2 + 0.04 * u, a)
        sc.curve(pa, pb, bend=-0.28, color=edge, lw=1.4, head=True, z=2)
    for (x, y), s in zip(pts, steps):
        sc.rect(x - bw / 2, y - bh / 2, bw, bh, fill=fill, edge=edge, r=0.1 * u, lw=1.2, z=4)
        yy = y - bh / 2 + 0.1 * u
        yy += sc.text(x, yy, s[0], inner, "text", True, txt, align="center") + 0.04 * u
        if len(s) > 1 and s[1]:
            sc.text(x, yy, s[1], inner, "small", align="center")
    if centre:
        th = sc.text_h(centre, R * 0.9, "text", True)
        sc.text(cx, cy - th / 2, centre, R * 0.9, "text", True, P.MUTED, align="center")
    return sc


# ----------------------------------------------------------------------------- matrix
MARKS = {True: ("check", P.GOOD), False: ("cross", P.CRITICAL), "partial": ("warning", P.WARNING)}


def matrix(rows, cols, cells, width=None, legend=None, first_w=None, medium="report"):
    """rows × cols cells, each True (supported), False (not), "partial", None (not applicable) or a short text.
    Marks are icons whose shape carries the meaning (check, cross, warning) in the state colours; `legend` maps
    True / False / "partial" to their words, shown under the table."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    first_w = first_w or min(2.2 * u, max(1.0 * u, max(probe.width_of(r, "text") for r in rows) + 0.2 * u))
    cw = (width - first_w - 0.1) / len(cols)
    head_h = max(probe.text_h(c, cw - 0.1 * u, "small", True) for c in cols) + 0.14 * u
    row_h = [max([probe.text_h(r, first_w - 0.14 * u, "text")] +
                 [probe.text_h(v, cw - 0.12 * u, "small") for v in cells[i] if isinstance(v, str) and v != "partial"])
             + 0.16 * u for i, r in enumerate(rows)]
    row_h = [max(h, 0.3 * u) for h in row_h]
    leg = 0.3 * u if legend else 0
    sc = Scene(width, 0.05 + head_h + sum(row_h) + leg + 0.08, medium)
    x0, y = 0.05, 0.05
    for j, c in enumerate(cols):
        sc.text(x0 + first_w + cw * (j + 0.5), y + 0.06 * u, c, cw - 0.1 * u, "small", True, align="center")
    sc.line([(x0, y + head_h), (width - 0.05, y + head_h)], P.INK, 1.0, z=3)
    y += head_h
    s = 0.2 * u
    for i, r in enumerate(rows):
        band = P.SOFT if i % 2 == 1 else P.SURFACE
        if i % 2 == 1:
            sc.rect(x0, y, width - 0.1, row_h[i], fill=P.SOFT, z=0)
        sc.text(x0 + 0.07 * u, y + (row_h[i] - sc.text_h(r, first_w - 0.14 * u, "text")) / 2, r, first_w - 0.14 * u)
        for j, v in enumerate(cells[i]):
            cx = x0 + first_w + cw * (j + 0.5)
            if v is True or v is False or v == "partial":
                name, color = MARKS[v]
                sc.icon(name, cx - s / 2, y + (row_h[i] - s) / 2, s, color=color, bg=band)
            elif v is None:
                sc.text(cx, y + (row_h[i] - sc.text_h("–", 1, "text")) / 2, "–", 1, "text", color=P.MUTED,
                        align="center")
            else:
                sc.text(cx, y + (row_h[i] - sc.text_h(v, cw - 0.12 * u, "small")) / 2, v, cw - 0.12 * u, "small",
                        align="center")
        y += row_h[i]
    sc.line([(x0, y), (width - 0.05, y)], P.LINE, 0.8, z=3)
    if legend:
        x, ly = x0, y + 0.12 * u
        for key in (True, "partial", False):
            if key in legend:
                name, color = MARKS[key]
                sc.icon(name, x, ly, 0.16 * u, color=color)
                sc.text(x + 0.22 * u, ly + 0.08 * u - sc.text_h("x", 1, "small") / 2, legend[key], 3 * u, "small")
                x += 0.45 * u + sc.width_of(legend[key], "small")
    return sc


# ----------------------------------------------------------------------------- layers
def layers(stack, width=None, label_w=None, medium="report"):
    """stack: (layer name, [components], role) from top to bottom; components sit as chips in their band and wrap
    to further rows when the band is full."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    label_w = label_w or 1.35 * u
    inner = width - label_w - 0.2 * u
    chip_h, row_step = 0.28 * u, 0.36 * u
    bands = []
    for name, comps, role in stack:
        rows_, row, used = [], [], 0.0
        for c in comps:
            w = min(inner, max(0.8 * u, probe.width_of(c, "text") + 0.3 * u))
            if row and used + w + 0.1 * u > inner:
                rows_.append(row)
                row, used = [], 0.0
            row.append((c, w))
            used += w + 0.1 * u
        if row:
            rows_.append(row)
        bh = max(0.5 * u, len(rows_) * row_step + 0.16 * u,
                 probe.text_h(name, label_w - 0.16 * u, "text", True) + 0.2 * u)
        bands.append((name, rows_, role, bh))
    sc = Scene(width, sum(b[3] for b in bands) + 0.06 * u * (len(bands) - 1) + 0.1, medium)
    y = 0.05
    for name, rows_, role, bh in bands:
        fill, txt, edge = LIGHT[role]
        solid, solid_txt = ROLES[role]
        sc.rect(0.05, y, width - 0.1, bh, fill=fill, edge=edge, r=0.07 * u, lw=0.9, z=2)
        sc.rect(0.05, y, label_w, bh, fill=solid, r=0.07 * u, z=3)
        th = sc.text_h(name, label_w - 0.16 * u, "text", True)
        sc.text(0.05 + label_w / 2, y + (bh - th) / 2, name, label_w - 0.16 * u, "text", True, solid_txt,
                align="center")
        ry = y + (bh - len(rows_) * row_step + (row_step - chip_h)) / 2
        for row in rows_:
            used = sum(w for _, w in row) + 0.1 * u * (len(row) - 1)
            x = 0.05 + label_w + 0.1 * u + (inner - used) / 2
            for c, w in row:
                sc.rect(x, ry, w, chip_h, fill=P.SURFACE, edge=edge, r=0.05 * u, lw=0.8, z=4)
                th = sc.text_h(c, w, "text")
                sc.text(x + w / 2, ry + (chip_h - th) / 2, c, w, "text", color=txt, align="center", z=5)
                x += w + 0.1 * u
            ry += row_step
        y += bh + 0.06 * u
    return sc


# ----------------------------------------------------------------------------- compare
def compare(left, right, width=None, tones=("critical", "good"), arrow_label=None, medium="report"):
    """Two panels, left (title, [points]) and right (title, [points]); each point carries the panel's state icon
    (cross / check by default), and an arrow between the panels reads as "becomes"."""
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    gap = max(0.5 * u, probe.width_of(arrow_label, "small") + 0.3 * u) if arrow_label else 0.5 * u
    pw = (width - 0.1 - gap) / 2
    isz = 0.15 * u
    heads = [probe.text_h(p[0], pw - 0.3 * u, "name", True) for p in (left, right)]
    bodies = [sum(probe.text_h(t, pw - 0.5 * u, "text") + 0.08 * u for t in p[1]) for p in (left, right)]
    h = max(hd + bd for hd, bd in zip(heads, bodies)) + 0.36 * u
    sc = Scene(width, h + 0.1, medium)
    for k, (panel, tone) in enumerate(zip((left, right), tones)):
        color = P.STATUS.get(tone, tone)
        bg = P.tint(color, 0.92)
        x = 0.05 + k * (pw + gap)
        sc.rect(x, 0.05, pw, h, fill=bg, edge=P.tint(color, 0.5), r=0.08 * u, lw=1.0, z=2)
        sc.rect(x, 0.05, 0.07 * u, h, fill=color, z=3)
        y = 0.05 + 0.14 * u
        y += sc.text(x + 0.2 * u, y, panel[0], pw - 0.3 * u, "name", True, P.shade(color, 0.3)) + 0.1 * u
        for pt in panel[1]:
            sc.icon(P.STATUS_ICON.get(tone, "info"), x + 0.2 * u, y + 0.01, isz, color=color, bg=bg)
            y += sc.text(x + 0.42 * u, y, pt, pw - 0.5 * u, "text") + 0.08 * u
    mx = 0.05 + pw + gap / 2
    sc.line([(mx - gap / 2 + 0.08 * u, 0.05 + h / 2), (mx + gap / 2 - 0.08 * u, 0.05 + h / 2)], lw=2.0, head=True)
    if arrow_label:
        sc.text(mx, 0.05 + h / 2 - 0.26 * u, arrow_label, gap - 0.1 * u, "small", color=P.MUTED, align="center")
    return sc


# ----------------------------------------------------------------------------- screenshot
def screenshot(image, callouts, width=None, image_share=0.62, medium="report"):
    """An image (path) with numbered markers at (fx, fy) fractions of its width and height (from the top-left), and
    the notes beside it: callouts are (fx, fy, text)."""
    from PIL import Image
    width = _width(width, medium)
    u = _scale(medium)
    probe = Scene(width, 1, medium)
    with Image.open(image) as im:
        iw_px, ih_px = im.size
    iw = width * image_share
    ih = iw * ih_px / iw_px
    nw = width - iw - 0.3 * u
    notes_h = sum(probe.text_h(t, nw - 0.3 * u, "text") + 0.12 * u for _, _, t in callouts)
    sc = Scene(width, max(ih, notes_h) + 0.1, medium)
    sc.image(image, 0.05, 0.05, iw, ih, z=0)
    sc.rect(0.05, 0.05, iw, ih, edge=P.LINE, lw=0.8, z=1)
    y = 0.05 + max(0.0, (ih - notes_h) / 2)
    for k, (fx, fy, text) in enumerate(callouts, start=1):
        sc.badge(0.05 + fx * iw, 0.05 + fy * ih, k, P.ORANGE)
        sc.badge(iw + 0.3 * u, y + 0.08 * u, k, P.ORANGE)
        y += sc.text(iw + 0.45 * u, y, text, nw - 0.3 * u, "text") + 0.12 * u
    return sc


# ============================================================================= structures
def _node(sc, x, y, w, h, head, body, role, u, light=True, icon=None, align="center"):
    """A measured node: rounded box in the role's light (or solid) tone with a bold head and a body."""
    if light:
        fill, txt, edge = LIGHT[role]
    else:
        fill, txt = ROLES[role]
        edge = fill
    sc.rect(x, y, w, h, fill=fill, edge=edge, r=0.08 * u, lw=1.1, z=3)
    inner = w - 0.16 * u
    content = sc.text_h(head, inner, "text", True) + (0.04 * u + sc.text_h(body, inner, "small") if body else 0)
    isz = 0.28 * u if icon else 0
    yy = y + (h - content - (isz + 0.05 * u if icon else 0)) / 2
    cx = x + w / 2 if align == "center" else x + 0.08 * u
    if icon:
        sc.icon(icon, x + w / 2 - isz / 2, yy, isz, color=edge if light else txt, bg=fill)
        yy += isz + 0.05 * u
    yy += sc.text(cx, yy, head, inner, "text", True, txt, align=align, z=5) + 0.04 * u
    if body:
        sc.text(cx, yy, body, inner, "small", color=P.INK if light else txt, align=align, z=5)


def _node_h(sc, w, head, body, u, icon=False):
    inner = w - 0.16 * u
    return sc.text_h(head, inner, "text", True) + (0.04 * u + sc.text_h(body, inner, "small") if body else 0) + \
        0.24 * u + (0.33 * u if icon else 0)


def _elbow(sc, p0, p1, color=P.CONNECTOR, dashed=False, head=True, mid=None):
    """A vertical elbow from p0 down (or up) to p1: vertical, horizontal at `mid`, vertical."""
    (x0, y0), (x1, y1) = p0, p1
    if abs(x0 - x1) < 1e-6:
        sc.line([p0, p1], color, 1.2, dashed, head=head, z=2)
        return
    my = mid if mid is not None else (y0 + y1) / 2
    sc.line([p0, (x0, my), (x1, my), p1], color, 1.2, dashed, head=head, z=2)


def tree(root, groups, width=None, medium="report"):
    """A root above groups above leaves: root (head, body, role), groups [(label, role, [(head, body)])]. Leaves are
    measured and share the width; each group spans exactly its leaves and the root is centred over the groups."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    leaves = [lf for _, _, ls in groups for lf in ls]
    gap, ggap = 0.12 * u, 0.3 * u
    lw = (width - 0.1 - gap * (len(leaves) - len(groups)) - ggap * (len(groups) - 1)) / len(leaves)
    leaf_h = max(_node_h(sc0, lw, h, b, u) for h, b in leaves)
    group_h = max(sc0.text_h(g[0], 2.5 * u, "text", True) for g in groups) + 0.24 * u
    root_w = min(width * 0.4, max(1.6 * u, sc0.width_of(root[0], "text", True) + 0.5 * u))
    root_h = _node_h(sc0, root_w, root[0], root[1], u)
    v = 0.35 * u
    sc = Scene(width, 0.05 + root_h + v + group_h + v + leaf_h + 0.08, medium)
    x = 0.05
    gy, ly = 0.05 + root_h + v, 0.05 + root_h + v + group_h + v
    centres = []
    for label, role, ls in groups:
        gw = len(ls) * lw + (len(ls) - 1) * gap
        fill, txt = ROLES[role]
        sc.rect(x, gy, gw, group_h, fill=fill, r=0.07 * u, z=3)
        th = sc.text_h(label, gw - 0.16 * u, "text", True)
        sc.text(x + gw / 2, gy + (group_h - th) / 2, label, gw - 0.16 * u, "text", True, txt, align="center")
        for k, (h, b) in enumerate(ls):
            lx = x + k * (lw + gap)
            _node(sc, lx, ly, lw, leaf_h, h, b, role, u)
            _elbow(sc, (x + gw / 2, gy + group_h), (lx + lw / 2, ly), mid=gy + group_h + v / 2)
        centres.append(x + gw / 2)
        x += gw + ggap
    rx = (centres[0] + centres[-1]) / 2
    _node(sc, rx - root_w / 2, 0.05, root_w, root_h, root[0], root[1], root[2], u, light=False)
    for cx in centres:
        _elbow(sc, (rx, 0.05 + root_h), (cx, gy), mid=0.05 + root_h + v / 2)
    return sc


def _separate(spans, lo, hi, gap):
    """Shift (centre, width) spans of one row apart so neighbours keep `gap`, within [lo, hi]."""
    order = sorted(range(len(spans)), key=lambda i: spans[i][0])
    xs = [spans[i][0] - spans[i][1] / 2 for i in order]
    ws = [spans[i][1] for i in order]
    for _ in range(4):
        for k in range(1, len(xs)):
            xs[k] = max(xs[k], xs[k - 1] + ws[k - 1] + gap)
        xs[-1] = min(xs[-1], hi - ws[-1]) if xs else 0
        for k in range(len(xs) - 2, -1, -1):
            xs[k] = min(xs[k], xs[k + 1] - ws[k] - gap)
        xs[0] = max(xs[0], lo) if xs else 0
    out = [0.0] * len(spans)
    for k, i in enumerate(order):
        out[i] = xs[k]
    return out


def branches(main, above=(), below=(), width=None, medium="report"):
    """A main flow across the width, with nodes entering it from above and outcomes leaving it below.
    main: [(head, body, role)] or with an icon as 4th item; above / below: [(index, head, body, role, edge label,
    dashed)]: the node sits over (under) main node `index`, joined by a labelled vertical arrow; neighbours are
    pushed apart so they never overlap."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    n = len(main)
    gap = 0.3 * u
    mw = (width - 0.1 - gap * (n - 1)) / n
    mh = max(_node_h(sc0, mw, m[0], m[1], u, icon=len(m) > 3 and m[3]) for m in main)
    side_w = min(mw * 1.15, 2.4 * u)
    ah = max([_node_h(sc0, side_w, a[1], a[2], u) for a in above] or [0])
    bh = max([_node_h(sc0, side_w, b[1], b[2], u) for b in below] or [0])
    lab = max([sc0.text_h(e[4], side_w, "small") for e in list(above) + list(below) if e[4]] or [0])
    v = 0.3 * u + lab
    top = 0.05 + (ah + v if above else 0)
    sc = Scene(width, top + mh + (v + bh if below else 0) + 0.08, medium)
    xs = [0.05 + k * (mw + gap) for k in range(n)]
    for k, m in enumerate(main):
        _node(sc, xs[k], top, mw, mh, m[0], m[1], m[2], u, light=False, icon=m[3] if len(m) > 3 else None)
        if k + 1 < n:
            sc.line([(xs[k] + mw + 0.03 * u, top + mh / 2), (xs[k + 1] - 0.03 * u, top + mh / 2)], head=True, z=4)
    for items, is_above in ((above, True), (below, False)):
        if not items:
            continue
        lefts = _separate([(xs[i] + mw / 2, side_w) for i, *_ in items], 0.05, width - 0.05, 0.12 * u)
        h_ = ah if is_above else bh
        y = 0.05 if is_above else top + mh + v
        for (i, head, body, role, label, dashed), lx in zip(items, lefts):
            _node(sc, lx, y, side_w, h_, head, body, role, u)
            cx = min(max(lx + side_w / 2, xs[i] + 0.15 * u), xs[i] + mw - 0.15 * u)
            if is_above:
                p0, p1 = (lx + side_w / 2, y + h_), (cx, top)
            else:
                p0, p1 = (cx, top + mh), (lx + side_w / 2, y)
            _elbow(sc, p0, p1, dashed=dashed)
            if label:
                ly = (p0[1] + p1[1]) / 2 - sc.text_h(label, side_w, "small") / 2
                sc.text(p1[0] + 0.06 * u if is_above else p0[0] + 0.06 * u, ly, label, side_w, "small",
                        plate=P.SURFACE, z=6)
    return sc


def loop_flow(steps, back=None, exit=None, width=None, medium="report"):
    """A row of steps (head, body, role) with a back edge drawn over the row (back=(from, to, label)) and an exit
    drawn under it to an outcome (exit=(from, head, body, role, label))."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    n = len(steps)
    gap = 0.4 * u
    w = (width - 0.1 - gap * (n - 1)) / n
    h = max(_node_h(sc0, w, s[0], s[1], u) for s in steps)
    lab = sc0.text_h(back[2], width / 2, "small") if back else 0
    top = 0.05 + (lab + 0.3 * u if back else 0)
    oh = _node_h(sc0, w * 1.4, exit[1], exit[2], u) if exit else 0
    elab = sc0.text_h(exit[4], 2.5 * u, "small") if exit and exit[4] else 0
    sc = Scene(width, top + h + (0.3 * u + elab + 0.15 * u + oh if exit else 0) + 0.08, medium)
    xs = [0.05 + k * (w + gap) for k in range(n)]
    for k, s in enumerate(steps):
        _node(sc, xs[k], top, w, h, s[0], s[1], s[2], u)
        if k + 1 < n:
            sc.line([(xs[k] + w + 0.03 * u, top + h / 2), (xs[k + 1] - 0.03 * u, top + h / 2)], head=True, z=4)
    if back:
        a, b, label = back
        ly = top - 0.15 * u
        sc.line([(xs[a] + w / 2, top), (xs[a] + w / 2, ly), (xs[b] + w / 2, ly), (xs[b] + w / 2, top)], head=True, z=4)
        sc.text((xs[a] + xs[b] + w) / 2, ly - lab - 0.03 * u, label, width / 2, "small", align="center",
                plate=P.SURFACE, z=6)
    if exit:
        a, head, body, role, label = exit
        oy = top + h + 0.3 * u + elab + 0.15 * u
        ow = w * 1.4
        ox = min(max(xs[a] + w / 2 - ow / 2, 0.05), width - 0.05 - ow)
        sc.line([(xs[a] + w / 2, top + h), (xs[a] + w / 2, oy)], head=True, z=4)
        if label:
            sc.text(xs[a] + w / 2 + 0.08 * u, top + h + 0.12 * u, label, 2.5 * u, "small", plate=P.SURFACE, z=6)
        _node(sc, ox, oy, ow, oh, head, body, role, u, light=False)
    return sc


def decision_ladder(start, questions, final, width=None, medium="report", yes="yes", no="no"):
    """A column of questions: each `yes` leads right to its action, each `no` down to the next question, the last
    `no` to `final`. start: (head, role); questions: [(question, action, role)]; final: (head, body, role)."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    dw = min(2.4 * u, width * 0.42)
    aw = width - dw - 1.0 * u
    dh = [max(0.55 * u, sc0.text_h(q, dw * 0.62, "small", True) + 0.3 * u) for q, _, _ in questions]
    ah = [_node_h(sc0, aw, a, None, u) for _, a, _ in questions]
    rows = [max(d, a_) for d, a_ in zip(dh, ah)]
    sh = _node_h(sc0, dw, start[0], None, u)
    fh = _node_h(sc0, dw, final[0], final[1], u)
    v = 0.32 * u
    sc = Scene(width, 0.05 + sh + v + sum(rows) + v * len(rows) + fh + 0.08, medium)
    cx = 0.05 + dw / 2
    _node(sc, 0.05, 0.05, dw, sh, start[0], None, start[1], u, light=False)
    y = 0.05 + sh
    for (q, a, role), rh, d, a_h in zip(questions, rows, dh, ah):
        sc.line([(cx, y), (cx, y + v + (rh - d) / 2)], head=True, z=2)
        ty = y + v + (rh - d) / 2
        sc.poly([(cx, ty), (cx + dw / 2, ty + d / 2), (cx, ty + d), (cx - dw / 2, ty + d / 2)],
                fill=P.tint(P.GOLD, 0.88), edge=P.GOLD, lw=1.1, z=3)
        th = sc.text_h(q, dw * 0.62, "small", True)
        sc.text(cx, ty + (d - th) / 2, q, dw * 0.62, "small", True, align="center", z=5)
        ax_ = 0.05 + dw + 0.9 * u
        _node(sc, ax_, y + v + (rh - a_h) / 2, aw, a_h, a, None, role, u)
        sc.line([(cx + dw / 2, ty + d / 2), (ax_, ty + d / 2)], head=True, z=2)
        sc.text(cx + dw / 2 + 0.08 * u, ty + d / 2 - sc.text_h(yes, 1, "small") - 0.02, yes, 0.8 * u, "small",
                color=P.GOOD, bold=True)
        sc.text(cx + 0.08 * u, ty + d + 0.02, no, 0.8 * u, "small", color=P.CRITICAL, bold=True)
        y = ty + d + (rh - d) / 2
    sc.line([(cx, y), (cx, y + v)], head=True, z=2)
    _node(sc, 0.05, y + v, dw, fh, final[0], final[1], final[2], u, light=False)
    return sc


# ============================================================================= time
def era_timeline(t0, t1, eras=(), above=(), below=(), width=None, medium="report", fmt=str, ticks=None):
    """Events on a true time scale from t0 to t1: eras [(a, b, label, color)] as bands on the axis, events above
    and below [(t, label)] in cards on stems, lifted to a second or third level when they would overlap."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    m = 0.1
    X = lambda t: m + (width - 2 * m) * (t - t0) / (t1 - t0)          # noqa: E731
    card_w = min(1.8 * u, (width - 2 * m) / 3)

    def place(events):
        levels, out = [], []
        for t, label in sorted(events):
            w = min(card_w, sc0.width_of(label, "small") + 0.2 * u)
            x = min(max(X(t) - w / 2, 0.02), width - w - 0.02)
            h = sc0.text_h(label, w - 0.12 * u, "small") + 0.12 * u
            lv = next((k for k, end in enumerate(levels) if x > end + 0.06 * u), len(levels))
            if lv == len(levels):
                levels.append(0)
            levels[lv] = x + w
            out.append((t, label, x, w, h, lv))
        return out, len(levels)

    up, nu = place(above)
    dn, nd = place(below)
    lh = max([e[4] for e in up + dn] or [0.3 * u]) + 0.12 * u
    band = 0.32 * u
    axis_y = 0.05 + nu * lh + 0.15 * u
    sc = Scene(width, axis_y + band + 0.25 * u + nd * lh + 0.1, medium)
    for a, b, label, c in eras:
        xa, xb = X(a), X(b)
        sc.rect(xa, axis_y, xb - xa, band, fill=P.tint(c, 0.75), edge=P.tint(c, 0.4), lw=0.6, z=1)
        sc.text((xa + xb) / 2, axis_y + (band - sc0.text_h(label, xb - xa - 0.1, "small", True)) / 2, label,
                max(0.4, xb - xa - 0.1), "small", True, P.shade(c, 0.35), align="center", z=2)
    sc.line([(m, axis_y + band), (width - m, axis_y + band)], P.MUTED, 1.2, z=2)
    for t in (ticks or []):
        sc.line([(X(t), axis_y + band), (X(t), axis_y + band + 0.06 * u)], P.MUTED, 1.0, z=2)
        half = sc0.width_of(fmt(t), "small") / 2
        align = "left" if X(t) - half < 0.02 else "right" if X(t) + half > width - 0.02 else "center"
        sc.text(X(t), axis_y + band + 0.08 * u, fmt(t), 1.0 * u, "small", color=P.MUTED, align=align)
    for items, is_up in ((up, True), (dn, False)):
        for t, label, x, w, h, lv in items:
            if is_up:
                cy = axis_y - 0.12 * u - lv * lh - h
                sc.line([(X(t), cy + h), (X(t), axis_y)], P.MUTED, 0.8, z=1)
            else:
                cy = axis_y + band + 0.25 * u + (0.2 * u if ticks else 0) + lv * lh
                sc.line([(X(t), axis_y + band), (X(t), cy)], P.MUTED, 0.8, z=1)
            sc.ellipse(X(t), axis_y + (0 if is_up else band), 0.1 * u, 0.1 * u, fill=P.INK, z=3)
            sc.rect(x, cy, w, h, fill=P.SURFACE, edge=P.LINE, r=0.05 * u, lw=0.8, z=3)
            sc.text(x + 0.06 * u, cy + 0.06 * u, label, w - 0.12 * u, "small", z=4)
    if ticks:
        sc.h += 0.2 * u
    return sc


def lane_timeline(lanes, t0, t1, height=None, width=None, medium="report", fmt=str, ticks=None):
    """Lanes side by side (institutions, components), time running down on one scale; each event is a dot on its
    lane's spine with its label beside it, pushed down when it would overlap the one above (a leader keeps it tied
    to its dot). lanes: [(name, role, [(t, label)])]."""
    width = _width(width, medium)
    u = _scale(medium)
    height = height or (5.0 if medium == "report" else 5.4)
    sc = Scene(width, height, medium)
    axis_w = 0.55 * u
    lw = (width - axis_w - 0.1) / len(lanes)
    head_h = max(sc.text_h(n, lw - 0.16 * u, "text", True) for n, _, _ in lanes) + 0.2 * u
    top, bottom = 0.05 + head_h + 0.2 * u, height - 0.15
    Y = lambda t: top + (bottom - top) * (t - t0) / (t1 - t0)          # noqa: E731
    for t in (ticks or []):
        sc.line([(axis_w, Y(t)), (width - 0.05, Y(t))], P.GRID, 0.6, dashed=True, z=0)
        sc.text(axis_w - 0.08 * u, Y(t) - sc.text_h(fmt(t), 1, "small") / 2, fmt(t), axis_w, "small", color=P.MUTED,
                align="right")
    for k, (name, role, events) in enumerate(lanes):
        x = axis_w + k * lw
        fill, txt = ROLES[role]
        sc.rect(x + 0.04, 0.05, lw - 0.08, head_h, fill=fill, r=0.06 * u, z=3)
        th = sc.text_h(name, lw - 0.16 * u, "text", True)
        sc.text(x + lw / 2, 0.05 + (head_h - th) / 2, name, lw - 0.16 * u, "text", True, txt, align="center")
        spine = x + 0.2 * u
        sc.line([(spine, top - 0.1 * u), (spine, bottom)], fill, 2.0, z=1)
        tw = lw - 0.45 * u
        next_free = top - 1
        for t, label in sorted(events):
            h = sc.text_h(label, tw, "small")
            ly = max(Y(t) - h / 2, next_free)
            sc.ellipse(spine, Y(t), 0.12 * u, 0.12 * u, fill=fill, edge=P.SURFACE, lw=1.0, z=3)
            sc.line([(spine + 0.06 * u, Y(t)), (spine + 0.16 * u, ly + min(h / 2, 0.08 * u))], P.MUTED, 0.6, z=2)
            sc.text(spine + 0.2 * u, ly, label, tw, "small", plate=P.SURFACE, z=4)
            next_free = ly + h + 0.05 * u
    return sc


def gantt(lanes, t0, t1, width=None, medium="report", kinds=None, fmt=str, ticks=None):
    """Spans on lanes over time, e.g. requests waiting for and holding a lock: lanes [(name, [(a, b, label, kind)],
    outcome)], kinds {kind: (fill, dashed)}; outcome is None, "good" or "critical" (a check or a cross at the end)."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    kinds = kinds or {"wait": (P.tint(P.MUTED, 0.75), True), "hold": (P.BLUE, False), "done": (P.TEAL, False)}
    name_w = max(sc0.width_of(n, "text") for n, _, _ in lanes) + 0.2 * u
    end_w = 0.35 * u
    X = lambda t: name_w + (width - name_w - end_w - 0.05) * (t - t0) / (t1 - t0)   # noqa: E731
    row = max(0.34 * u, sc0.text_h("x", 1, "small") + 0.16 * u)
    sc = Scene(width, 0.05 + row * len(lanes) + (0.3 * u if ticks else 0) + 0.08, medium)
    for i, (name, spans, outcome) in enumerate(lanes):
        y = 0.05 + i * row
        sc.text(0.05, y + (row - sc.text_h(name, name_w, "text")) / 2, name, name_w, "text")
        sc.line([(name_w, y + row / 2), (X(t1), y + row / 2)], P.GRID, 0.6, z=0)
        for a, b, label, kind in spans:
            fill, dashed = kinds[kind]
            sc.rect(X(a), y + row * 0.18, X(b) - X(a), row * 0.64, fill=fill, edge=P.shade(fill, 0.2) if dashed else None,
                    r=0.04 * u, lw=0.8, dashed=dashed, z=2)
            if label and sc.width_of(label, "small") < X(b) - X(a) - 0.08:
                sc.text((X(a) + X(b)) / 2, y + (row - sc.text_h(label, 3, "small")) / 2, label, X(b) - X(a), "small",
                        color=P.text_on(fill), align="center", z=3)
        if outcome:
            end = max(b for _, b, _, _ in spans)
            s = row * 0.6
            sc.icon(P.STATUS_ICON[outcome], X(end) + 0.06 * u, y + (row - s) / 2, s, color=P.STATUS[outcome])
    if ticks:
        base = 0.05 + row * len(lanes)
        for t in ticks:
            sc.line([(X(t), base), (X(t), base + 0.05 * u)], P.MUTED, 0.8)
            sc.text(X(t), base + 0.07 * u, fmt(t), 1 * u, "small", color=P.MUTED, align="center")
    return sc


# ============================================================================= grids
CELL = {"plain": (P.SURFACE, P.LINE, P.INK), "mask": (P.tint(P.MUTED, 0.6), P.MUTED, P.INK),
        "new": (P.tint(P.ORANGE, 0.8), P.ORANGE, P.shade(P.ORANGE, 0.4)),
        "ok": (P.tint(P.GOOD, 0.85), P.GOOD, P.shade(P.GOOD, 0.3)),
        "bad": (P.tint(P.CRITICAL, 0.85), P.CRITICAL, P.shade(P.CRITICAL, 0.3)),
        "ref": (P.tint(P.BLUE, 0.85), P.BLUE, P.shade(P.BLUE, 0.35))}


def token_strip(rows, width=None, medium="report", label_w=None, cell_h=None):
    """Rows of cells (tokens, ids, values): rows [(label, [(text, style)], marks)] with styles from CELL (plain,
    mask, new, ok, bad, ref); marks are ("brace", i0, i1, text) for a bracket under cells i0..i1 and ("window", i0,
    i1) for a tinted window behind them. Cells take the width of their text."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    label_w = label_w if label_w is not None else (max(sc0.width_of(r[0], "text", True) for r in rows) + 0.2 * u
                                                  if any(r[0] for r in rows) else 0)
    ch = cell_h or sc0.text_h("Xg", 1, "text") + 0.16 * u
    g = 0.05 * u
    heights = []
    for _, cells, marks in rows:
        brace = max([sc0.text_h(mk[3], width / 2, "small") + 0.14 * u for mk in marks if mk[0] == "brace"] or [0])
        heights.append(ch + brace + 0.18 * u)
    sc = Scene(width, 0.05 + sum(heights) + 0.05, medium)
    y = 0.05
    for (label, cells, marks), rh in zip(rows, heights):
        if label:
            sc.text(0.05, y + (ch - sc.text_h(label, label_w, "text", True)) / 2, label, label_w, "text", True)
        xs, x = [], 0.05 + label_w
        for text, style in cells:
            w = max(ch, sc0.width_of(text, "text") + 0.16 * u)
            xs.append((x, w))
            x += w + g
        for mk in marks:
            if mk[0] == "window":
                a, b = xs[mk[1]], xs[mk[2]]
                sc.rect(a[0] - 0.05 * u, y - 0.05 * u, b[0] + b[1] - a[0] + 0.1 * u, ch + 0.1 * u,
                        fill=P.tint(P.GOLD, 0.82), edge=P.GOLD, r=0.05 * u, lw=1.0, dashed=True, z=0)
        for (text, style), (cx, w) in zip(cells, xs):
            fill, edge, ink = CELL[style]
            sc.rect(cx, y, w, ch, fill=fill, edge=edge, r=0.04 * u, lw=0.8, z=2)
            sc.text(cx + w / 2, y + (ch - sc.text_h(text, w, "text")) / 2, text, w + 0.2, "text", color=ink,
                    align="center", z=3)
        for mk in marks:
            if mk[0] == "brace":
                a, b = xs[mk[1]], xs[mk[2]]
                x0, x1, by = a[0], b[0] + b[1], y + ch + 0.08 * u
                sc.line([(x0, by - 0.05 * u), (x0, by), (x1, by), (x1, by - 0.05 * u)], P.MUTED, 1.0, z=2)
                sc.text((x0 + x1) / 2, by + 0.04 * u, mk[3], max(x1 - x0, 1.2 * u), "small", color=P.MUTED,
                        align="center")
        y += rh
    return sc


def pair_matrix(items, cell, width=None, medium="report", styles=None, totals=True, legend=None, totals_label=None,
                highlight=None, cell_size=None):
    """Every item against every other: cell(i, j) returns (text, style) or (text, style, winner) for row i, column j
    (not called on the diagonal); styles map a style to (fill, edge); totals adds a column with each item's points:
    the cells it won (the explicit winner index, else the cells whose text is the item). `highlight` marks one
    item's total (the overall winner); `legend` maps styles to their words, one per line under the grid."""
    u = _scale(medium)
    sc0 = Scene(1, 1, medium)
    styles = styles or {"win": (P.tint(P.GOOD, 0.85), P.GOOD), "lose": (P.SURFACE, P.LINE),
                        "tie": (P.tint(P.GOLD, 0.85), P.GOLD)}
    n = len(items)
    cells = {(i, j): cell(i, j) for i in range(n) for j in range(n) if i != j}
    cs = cell_size or max(0.42 * u, max(sc0.width_of(c[0], "small") for c in cells.values()) + 0.16 * u)
    head = max(cs * 0.8, max(sc0.text_h(it, cs, "small", True) for it in items) + 0.12 * u)
    row_w = max(sc0.width_of(it, "small", True) for it in items) + 0.2 * u
    tw = max(cs, sc0.width_of(totals_label, "small", True) + 0.12 * u) if totals_label else cs
    w = 0.05 + row_w + n * cs + (tw + 0.1 * u if totals else 0) + 0.1
    keys = [(style, word, 0.28 * u + sc0.width_of(word, "small") + 0.25 * u) for style, word in (legend or {}).items()]
    lines, cur, used = [], [], 0.0                         # legend keys flow left to right and wrap at the width
    for key in keys:
        if cur and used + key[2] > w - 0.1:
            lines.append(cur)
            cur, used = [], 0.0
        cur.append(key)
        used += key[2]
    if cur:
        lines.append(cur)
    w = max(w, max([sum(k[2] for k in ln) for ln in lines] or [0]) + 0.1)
    leg = (0.12 * u + 0.26 * u * len(lines)) if legend else 0
    sc = Scene(width or w, 0.05 + head + n * cs + leg + 0.1, medium)
    x0, y0 = 0.05 + row_w, 0.05 + head
    score = [0] * n
    for j, it in enumerate(items):
        sc.text(x0 + j * cs + cs / 2, 0.05 + (head - sc.text_h(it, cs, "small", True)) / 2, it, cs, "small", True,
                align="center")
    for i, it in enumerate(items):
        sc.text(0.05 + row_w / 2, y0 + i * cs + (cs - sc.text_h(it, row_w, "small", True)) / 2, it, row_w, "small",
                True, align="center")
        for j in range(n):
            x, y = x0 + j * cs, y0 + i * cs
            if i == j:
                sc.rect(x + 0.02, y + 0.02, cs - 0.04, cs - 0.04, fill=P.SOFT, r=0.04 * u, z=1)
                continue
            got = cells[(i, j)]
            text, style = got[0], got[1]
            fill, edge = styles[style]
            sc.rect(x + 0.02, y + 0.02, cs - 0.04, cs - 0.04, fill=fill, edge=edge, r=0.04 * u, lw=0.8, z=1)
            sc.text(x + cs / 2, y + (cs - sc.text_h(text, cs, "small")) / 2, text, cs, "small", align="center", z=2)
            winner = got[2] if len(got) > 2 else (i if text == it else None)
            if winner is not None:
                score[winner] += 1
    if totals:
        tx = x0 + n * cs + 0.1 * u
        if totals_label:
            sc.text(tx + tw / 2, 0.05 + (head - sc.text_h(totals_label, tw, "small", True)) / 2, totals_label, tw,
                    "small", True, P.MUTED, align="center")
        for i in range(n):
            y = y0 + i * cs
            sc.rect(tx, y + 0.02, tw, cs - 0.04, fill=P.GOOD if highlight == i else P.NAVY, r=0.04 * u, z=1)
            sc.text(tx + tw / 2, y + (cs - sc.text_h(str(score[i]), tw, "text", True)) / 2, str(score[i]), tw, "text",
                    True, P.SURFACE, align="center", z=2)
    if legend:
        ly = y0 + n * cs + 0.12 * u
        for ln in lines:
            x = 0.05
            for style, word, kw in ln:
                fill, edge = styles[style]
                sc.rect(x, ly, 0.2 * u, 0.16 * u, fill=fill, edge=edge, r=0.03 * u, lw=0.8)
                sc.text(x + 0.28 * u, ly + 0.08 * u - sc.text_h(word, 3, "small") / 2, word, kw, "small")
                x += kw
            ly += 0.26 * u
    return sc


def unit_rows(groups, width=None, medium="report", per_row=None, size=None):
    """Counts as rows of squares, one square per unit: groups [(label, n, color)] or [(label, [color per unit])];
    a color of None draws an empty (outlined) square. Small counts read at a glance, without an axis."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    label_w = max(sc0.width_of(g[0], "text") for g in groups) + 0.2 * u
    s = size or 0.2 * u
    g_ = s * 0.3
    per_row = per_row or max(1, int((width - label_w - 0.1) / (s + g_)))
    rows = []
    for gr in groups:
        units = gr[1] if isinstance(gr[1], list) else [gr[2]] * gr[1]
        rows.append((gr[0], units, max(1, math.ceil(len(units) / per_row))))
    sc = Scene(width, 0.05 + sum(r[2] * (s + g_) + 0.12 * u for r in rows) + 0.05, medium)
    y = 0.05
    for label, units, nr in rows:
        bh = nr * (s + g_)
        sc.text(0.05, y + (min(bh, s + g_) - sc.text_h(label, label_w, "text")) / 2, label, label_w, "text")
        for k, c in enumerate(units):
            x = 0.05 + label_w + (k % per_row) * (s + g_)
            yy = y + (k // per_row) * (s + g_)
            sc.rect(x, yy, s, s, fill=c, edge=c or P.MUTED, r=s * 0.18, lw=0.8, z=2)
        y += bh + 0.12 * u
    return sc


def risk_matrix(rows, cols, items, width=None, medium="report", row_title=None, col_title=None):
    """A likelihood × impact style grid: rows top (highest) to bottom, cols left (lowest) to right; items maps
    (row, col) to a list of short labels shown as chips; cells warm up toward the top-right."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    lw = max(sc0.width_of(r, "small", True) for r in rows) + 0.2 * u + (0.25 * u if row_title else 0)
    cw = (width - lw - 0.1) / len(cols)
    chip_h = sc0.text_h("x", 1, "small") + 0.08 * u
    rh = [max(0.5 * u, max([len(items.get((i, j), [])) for j in range(len(cols))] or [0]) * (chip_h + 0.05 * u)
              + 0.12 * u) for i in range(len(rows))]
    head = sc0.text_h("x", 1, "small", True) + 0.14 * u
    sc = Scene(width, 0.05 + sum(rh) + head + (0.3 * u if col_title else 0) + 0.05, medium)
    levels = len(rows) + len(cols) - 1
    y = 0.05
    for i, r in enumerate(rows):
        sc.text(lw - 0.1 * u, y + (rh[i] - sc.text_h(r, lw, "small", True)) / 2, r, lw, "small", True, align="right")
        for j in range(len(cols)):
            x = lw + j * cw
            level = ((len(rows) - 1 - i) + j) / max(1, levels - 1)      # 0 at the bottom-left, 1 at the top-right
            fill = P.blend(P.blend(P.GOLD, P.SURFACE, 0.88), P.blend(P.CRITICAL, P.SURFACE, 0.55), level)
            sc.rect(x + 0.02, y + 0.02, cw - 0.04, rh[i] - 0.04, fill=fill, r=0.04 * u, z=1)
            n_ = len(items.get((i, j), []))
            cy = y + (rh[i] - n_ * (chip_h + 0.05 * u) + 0.05 * u) / 2
            for lab in items.get((i, j), []):
                w = min(cw - 0.16 * u, sc0.width_of(lab, "small") + 0.14 * u)
                sc.rect(x + (cw - w) / 2, cy, w, chip_h, fill=P.SURFACE, edge=P.LINE, r=0.04 * u, lw=0.6, z=2)
                sc.text(x + cw / 2, cy + 0.04 * u, lab, w, "small", align="center", z=3)
                cy += chip_h + 0.05 * u
        y += rh[i]
    for j, c in enumerate(cols):
        sc.text(lw + j * cw + cw / 2, y + 0.06 * u, c, cw, "small", True, align="center")
    if col_title:
        sc.text(lw + (width - lw) / 2, y + head, col_title, width - lw, "small", color=P.MUTED, align="center")
    return sc


# ============================================================================= cards
def stripe_cards(items, cols=2, width=None, medium="report", centre_last=False):
    """Verdict or finding cards in a grid: items [(tag, head, body, color)] or with an icon as 5th item; a coloured
    stripe on the left and the tag above the head (e.g. "1 · FIRM"). Each row of cards takes its tallest card."""
    width = _width(width, medium)
    u = _scale(medium)
    sc0 = Scene(width, 1, medium)
    gap = 0.18 * u
    cw = (width - 0.1 - gap * (cols - 1)) / cols
    inner = cw - 0.36 * u
    isz = 0.24 * u
    head_w = lambda it: inner - (isz + 0.1 * u if len(it) > 4 and it[4] else 0)      # noqa: E731  (beside the icon)
    hs = [sc0.text_h(it[0], head_w(it), "small", True) + 0.04 * u + sc0.text_h(it[1], head_w(it), "name", True) +
          0.05 * u + sc0.text_h(it[2], inner, "text") + 0.26 * u for it in items]
    rows = [max(hs[k:k + cols]) for k in range(0, len(items), cols)]
    sc = Scene(width, 0.05 + sum(rows) + gap * (len(rows) - 1) + 0.05, medium)
    y = 0.05
    for r, rh in enumerate(rows):
        for c in range(cols):
            k = r * cols + c
            if k >= len(items):
                break
            tag, head, body, color = items[k][:4]
            short = len(items) - r * cols if r == len(rows) - 1 else cols
            shift = (cols - short) * (cw + gap) / 2 if centre_last and short < cols else 0
            x = 0.05 + c * (cw + gap) + shift
            sc.rect(x, y, cw, rh, fill=P.SOFT, edge=P.LINE, r=0.06 * u, lw=0.8, z=1)
            sc.rect(x, y, 0.07 * u, rh, fill=color, z=2)
            yy = y + 0.13 * u
            tx = x + 0.22 * u
            if len(items[k]) > 4 and items[k][4]:
                sc.icon(items[k][4], x + cw - isz - 0.12 * u, yy, isz, color=color, bg=P.SOFT)
            yy += sc.text(tx, yy, tag, head_w(items[k]), "small", True, color) + 0.04 * u
            yy += sc.text(tx, yy, head, head_w(items[k]), "name", True) + 0.05 * u
            sc.text(tx, yy, body, inner, "text")
        y += rh + gap
    return sc
