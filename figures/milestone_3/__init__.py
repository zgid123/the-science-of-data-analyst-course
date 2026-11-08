"""Figures of the Milestone 3 report (reports/milestone-3), drawn with the build-report visual kit.

Every number comes from the Prepared Data Package metadata (package/data/metadata/*.csv, written by
src/02_profile.py), so a rerun of the package and of render_figures.py redraws the figures from the same data.
Render: venv/bin/python .claude/skills/build-report/scripts/render_figures.py milestone-3
"""
from __future__ import annotations

import csv
from pathlib import Path

import charts as ch
import diagrams as dg
from c4kit import Canvas

META = Path(__file__).resolve().parents[2] / "reports" / "milestone-3" / "package" / "data" / "metadata"

T = {"vi": {
    "module run": "kỳ mở module", "assessment": "bài đánh giá", "learning resource": "tài nguyên học tập",
    "enrolment": "lượt đăng ký học", "registration days": "ngày đăng ký, rút", "submission": "bài nộp",
    "daily click record": "bản ghi lượt nhấp theo ngày", "1–N": "1–N", "1–1": "1–1", "rows": "dòng",
    "Distinction": "Xuất sắc", "Pass": "Đạt", "Fail": "Không đạt", "Withdrawn": "Rút học phần",
    "Clicks per enrolled student": "Lượt nhấp mỗi sinh viên", "Week of the module run": "Tuần của kỳ mở module",
    "Feb 2013": "Tháng 2/2013", "Oct 2013": "Tháng 10/2013", "Feb 2014": "Tháng 2/2014", "Oct 2014": "Tháng 10/2014",
    "cut-off day 13": "mốc ngày 13", "cut-off day 27": "mốc ngày 27", "no clicks logged": "không ghi nhận lượt nhấp",
    "Raw files": "Tệp gốc", "7 CSV tables, SHA-256 pinned, read-only": "7 bảng CSV, cố định SHA-256, chỉ đọc",
    "Understand and profile": "Hiểu và lập hồ sơ",
    "Understanding Map, profile, Data Quality Issue Log": "Bản đồ hiểu dữ liệu, hồ sơ, nhật ký vấn đề chất lượng",
    "Prepare": "Chuẩn bị", "Ten steps: population, standardise, keys, missing values, truncate, integrate, features":
        "Mười bước: tổng thể, chuẩn hoá, khoá, giá trị thiếu, cắt theo ngày rút, tích hợp, đặc trưng",
    "Fit on 2013 runs": "Khớp trên lượt 2013", "Encodings and scaling from training runs only":
        "Mã hoá và chuẩn hoá chỉ từ lượt huấn luyện",
    "Validate and package": "Kiểm định và đóng gói", "22 checks, dictionary, lineage, version manifest":
        "22 phép kiểm, từ điển, dòng dõi dữ liệu, bản kê phiên bản",
}}


def _t(lang):
    return lambda s: T.get(lang, {}).get(s, s)


def _rows(name):
    with (META / name).open() as f:
        return list(csv.DictReader(f))


def tables(out, lang="en"):
    """Figure 2.1: the seven tables, their grain, row counts and the keys that join them."""
    t = _t(lang)
    cv = Canvas(6.3, 3.9)
    w, h = 1.85, 0.72
    crs = cv.box(2.22, 0.1, w, h, "courses", tech=f"22 {t('rows')}", desc=t("module run"), role="external")
    asm = cv.box(0.05, 1.3, w, h, "assessments", tech=f"206 {t('rows')}", desc=t("assessment"), role="external")
    inf = cv.box(2.22, 1.3, w, h, "studentInfo", tech=f"32,593 {t('rows')}", desc=t("enrolment"), role="system")
    vle = cv.box(4.4, 1.3, w, h, "vle", tech=f"6,364 {t('rows')}", desc=t("learning resource"), role="external")
    sa = cv.box(0.05, 2.75, w, h, "studentAssessment", tech=f"173,912 {t('rows')}", desc=t("submission"),
                role="warehouse")
    reg = cv.box(2.22, 2.75, w, h, "studentRegistration", tech=f"32,593 {t('rows')}", desc=t("registration days"),
                 role="warehouse")
    sv = cv.box(4.4, 2.75, w, h, "studentVle", tech=f"10,655,280 {t('rows')}", desc=t("daily click record"),
                role="warehouse")
    cv.arrow(crs, asm, label=t("1–N"))
    cv.arrow(crs, inf, label=t("1–N"))
    cv.arrow(crs, vle, label=t("1–N"))
    cv.arrow(asm, sa, label=t("1–N"))
    cv.arrow(inf, reg, label=t("1–1"))
    gx_l, gx_r = 0.05 + w + (2.22 - 0.05 - w) / 2, 2.22 + w + (4.4 - 2.22 - w) / 2   # gaps between the columns
    cv.arrow(inf, sa, label=t("1–N"), sides=("w", "e"), via=[(gx_l, 1.3 + h / 2), (gx_l, 2.75 + h / 2)],
             label_at=0.5, label_w=0.45)
    cv.arrow(inf, sv, label=t("1–N"), sides=("e", "w"), via=[(gx_r, 1.3 + h / 2), (gx_r, 2.75 + h / 2)],
             label_at=0.5, label_w=0.45)
    cv.arrow(vle, sv, label=t("1–N"))
    cv.trim()
    cv.save(out)


def outcomes(out, lang="en"):
    """Figure 3.1: final result of every enrolment, by module run (100 % stacked)."""
    t = _t(lang)
    rows = sorted(_rows("fig_outcome_by_run.csv"), key=lambda r: (r["code_module"], r["code_presentation"]))
    cats = [f"{r['code_module']} {r['code_presentation']}" for r in rows]
    parts = {t(k): [int(r[k]) for r in rows] for k in ("Distinction", "Pass", "Fail", "Withdrawn")}
    fig, ax = ch.figure(6.3, 4.0, lang=lang)
    ch.stacked(ax, cats, parts, percent=True, horizontal=True, min_label=0.08)
    ch.save(fig, out)


def weekly(out, lang="en"):
    """Figure 3.2: weekly clicks per enrolled student by start month and year, with the cut-offs and the gap."""
    t = _t(lang)
    enrol = {}
    for r in _rows("fig_outcome_by_run.csv"):
        enrol[r["code_presentation"]] = enrol.get(r["code_presentation"], 0) + sum(
            int(r[k]) for k in ("Distinction", "Pass", "Fail", "Withdrawn"))
    clicks: dict[str, dict[int, int]] = {}
    for r in _rows("fig_weekly_activity.csv"):
        wk = int(r["week"]) + 1                          # file: floor(day / 7); report: week 1 = days 0-6
        clicks.setdefault(r["code_presentation"], {}).setdefault(wk, 0)
        clicks[r["code_presentation"]][wk] += int(r["clicks"])
    weeks = list(range(-3, 40))
    names = {"2013B": "Feb 2013", "2013J": "Oct 2013", "2014B": "Feb 2014", "2014J": "Oct 2014"}
    last = {p: max(clicks[p]) for p in names}           # each start month ends in its own week
    series = {t(names[p]): [clicks[p].get(w, 0) / enrol[p] if w <= last[p] else float("nan") for w in weeks]
              for p in names}
    fig, ax = ch.figure(6.3, 3.3, lang=lang)
    ch.lines(ax, weeks, series, markers=False, end_labels=False, show_legend=True,
             xlabel=t("Week of the module run"), ylabel=t("Clicks per enrolled student"))
    top = max(max(x for x in v if x == x) for v in series.values())
    plate = {"fc": "white", "ec": "none", "pad": 1.2}
    for x, lab, y in ((2.5, t("cut-off day 13"), 0.97), (4.5, t("cut-off day 27"), 0.84)):
        ax.axvline(x, color="#7A8290", lw=0.9, ls="--", zorder=1)
        ax.text(x + 0.4, top * y, lab, fontsize=7.5, color="#4A5260", va="top", bbox=plate, zorder=5)
    ch.save(fig, out)


def pipeline(out, lang="en"):
    """Figure 6.1: from the raw files to the prepared views."""
    t = _t(lang)
    dg.process([
        (t("Raw files"), t("7 CSV tables, SHA-256 pinned, read-only"), "database"),
        (t("Understand and profile"), t("Understanding Map, profile, Data Quality Issue Log"), "search"),
        (t("Prepare"), t("Ten steps: population, standardise, keys, missing values, truncate, integrate, features"),
         "gear"),
        (t("Fit on 2013 runs"), t("Encodings and scaling from training runs only"), "lock"),
        (t("Validate and package"), t("22 checks, dictionary, lineage, version manifest"), "check"),
    ]).save(out)


FIGURES = {"fig-2-1-tables": tables, "fig-3-1-outcomes": outcomes, "fig-3-2-weekly": weekly,
           "fig-6-1-pipeline": pipeline}
