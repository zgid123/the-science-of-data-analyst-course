"""Render the code-first figures of one or more tasks at 300 DPI.

Usage: python .claude/skills/build-report/scripts/render_figures.py [TASK|all] [name-filter]
       ... render_figures.py                 # every task with a [TASK.figures] table in tasks.toml
       ... render_figures.py taskN timeline  # the task's figures whose name contains "timeline"

A task declares its figures in tasks.toml as [TASK.figures] package = "figures.taskN": a Python package of the
project whose __init__.py lists FIGURES (output name -> builder taking the output path). The PNGs are written to
the assets/figures/ folder of the task's report. Builders draw with this skill's kit (figures.md): c4kit.py
(`from c4kit import Canvas`) for boxes, people, arrows and C4 diagrams, diagrams.py for ready-made diagram types,
charts.py for charts and icons.py for pictograms, all in the colours of palette.py. A builder that takes a `lang`
argument also writes <name>.<code>.png for every other language of the task, and the build of that language uses it.

Every figure saved while rendering passes the layout check (figqa.py: overlapping, cut-off or crossed labels, text
past its box, text below 6.5 pt, empty margins), however the builder saves it; each finding prints as a WARN line,
and the last line counts them. With [TASK.layout] vector_figures = true, each PNG also gets an SVG twin (text kept
as text), which the Word build attaches as the vector version of the figure.
"""

import importlib
import inspect
import sys

from matplotlib.figure import Figure

from common import ROOT, language_packs, load_config, resolve, source_language, tasks, shown

sys.path.insert(0, str(ROOT))                   # the project's figure packages (figures.taskN, …)


VECTOR = {"on": False}


def _checked_savefig(original):
    """Figure.savefig that runs the layout check once per figure written to an image file."""
    def savefig(self, fname, *args, **kwargs):
        result = original(self, fname, *args, **kwargs)
        if VECTOR["on"] and str(fname).endswith(".png"):       # the SVG twin, text kept as text
            import matplotlib
            with matplotlib.rc_context({"svg.fonttype": "none"}):
                original(self, str(fname)[:-4] + ".svg", format="svg", **{k: v for k, v in kwargs.items()
                                                                          if k in ("facecolor", "transparent")})
        if isinstance(fname, (str, bytes)) or hasattr(fname, "__fspath__"):
            import figqa
            if not getattr(self, "_figqa_done", False):
                self._figqa_done = True
                figqa.report(self, shown(fname))
        return result
    return savefig


def render(name, task, flt="", quiet=False):
    import figqa
    before = len(figqa.LOG)
    VECTOR["on"] = bool(task.get("layout", {}).get("vector_figures"))
    figures = importlib.import_module(task["figures"]["package"]).FIGURES
    out = ROOT / task["report"] / "assets" / "figures"
    out.mkdir(parents=True, exist_ok=True)
    langs = [k for k in task if isinstance(task[k], dict) and k in language_packs() and k != source_language(language_packs())]
    for fig, fn in figures.items():
        if flt in fig:
            fn(out / f"{fig}.png")
            if "lang" in inspect.signature(fn).parameters:      # a builder that draws its labels in each language
                for code in langs:
                    fn(out / f"{fig}.{code}.png", lang=code)
            if not quiet:
                print("rendered", fig)
    if not quiet:
        print(f"{name}: {sum(flt in f for f in figures)} figures → {shown(out)}, {len(figqa.LOG) - before} layout findings")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    Figure.savefig = _checked_savefig(Figure.savefig)
    config = load_config()
    all_tasks = tasks(config)
    for name in resolve(argv[0] if argv else "all", config):
        if "figures" in all_tasks[name]:
            render(name, all_tasks[name], argv[1] if len(argv) > 1 else "")


if __name__ == "__main__":
    main()
