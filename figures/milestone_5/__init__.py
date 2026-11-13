"""Figures of the Milestone 5 report (reports/milestone-5), drawn with the build-report visual kit.

Figure A.1 (Appendix I) shows the project's logic chain from the stakeholder problem to decision support, with the milestone that
produced each link and one concrete item per link (items from research/baseline/m5-baseline.md and results/).
Figure 11.1 shows AQ1, the non-completion rate per module in 2013 and in 2014 with its 95% Wilson interval, students
still registered at day 14, and the pooled rate of the 22 runs (results/2013/aq1_rates.csv, results/2014/aq1_rates.csv,
results/all_runs/aq1_rates.csv). Figure 11.2 shows AQ2, the mutually adjusted risk difference of each early sign in
2013 and in 2014 with 95% intervals (results/compare/aq2_year_comparison.csv, refitted to four decimals). Both charts
read their CSV.
Render: venv/bin/python .claude/skills/build-report/scripts/render_figures.py milestone-5
"""
from __future__ import annotations

import csv
from pathlib import Path

import charts as ch
import palette as P
from c4kit import Canvas

RESULTS = Path(__file__).resolve().parents[2] / "reports" / "milestone-5" / "results"

T = {"vi": {
    # Figure A.1
    "M1": "M1", "M2": "M2", "M3": "M3", "M4": "M4", "M5": "M5",
    "Stakeholder problem": "Vấn đề của các bên liên quan",
    "Students who stop taking part are found too late for support within the semester":
        "Sinh viên giảm tham gia được phát hiện quá muộn để hỗ trợ ngay trong học kỳ",
    "Measurable goal": "Mục tiêu đo lường được",
    "Completion after add-drop from an assumed 70% to 75% by 2027–2028":
        "Tỷ lệ hoàn thành sau điều chỉnh đăng ký từ 70% (giả định) lên 75% vào 2027–2028",
    "Analytical questions": "Câu hỏi phân tích",
    "AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive (ranking)":
        "AQ1 mô tả, AQ2 chẩn đoán, AQ3 dự báo, AQ4 đề xuất (xếp hạng)",
    "Required data": "Dữ liệu cần có",
    "Dated outcome, tasks and activity; three or more runs; open licence; persistent IDs (gates G1–G5)":
        "Kết quả, bài đánh giá và hoạt động có ngày; ít nhất ba kỳ mở; giấy phép mở; mã định danh bền vững (G1–G5)",
    "Selected open dataset": "Bộ dữ liệu mở được chọn",
    "OULAD, 22 runs of 7 modules in 2013–2014; licence CC BY 4.0":
        "OULAD, 22 kỳ mở của 7 module năm 2013–2014; giấy phép CC BY 4.0",
    "Actual data fit and gaps": "Mức phù hợp thực tế và khoảng trống",
    "AQ1–AQ3 yellow, AQ4 red; no attendance, contacts or year of study":
        "AQ1–AQ3 vàng, AQ4 đỏ; không có điểm danh, liên hệ hay năm học",
    "Prepared data": "Dữ liệu đã chuẩn bị",
    "OULAD-N04-prepared-1.0; 22 of 22 validation checks pass":
        "OULAD-N04-prepared-1.0; đạt 22 trên 22 phép kiểm tra",
    "Candidate methods": "Phương pháp ứng viên",
    "Grouped rates; logistic regression within run; penalised logistic model; top-k ranking":
        "Tỷ lệ theo nhóm; hồi quy logistic trong từng kỳ mở; logistic có phạt; xếp hạng top-k",
    "Evaluation design": "Thiết kế đánh giá",
    "One Evaluation Design Card per AQ; develop on 2013, single test on 2014":
        "Một Evaluation Design Card cho mỗi AQ; phát triển trên 2013, kiểm tra một lần trên 2014",
    "Findings and limitations": "Kết quả và giới hạn",
    "AQ1–AQ2 answered on the 2013 and 2014 runs; AQ3–AQ4 proposed":
        "AQ1–AQ2 được trả lời trên các kỳ mở năm 2013 và 2014; AQ3–AQ4 ở mức đề xuất",
    "Educational decision support": "Hỗ trợ quyết định giáo dục",
    "D1 whom to contact, D2 where to place support time, D3 whether to extend":
        "D1 liên hệ ai, D2 phân bổ thời gian hỗ trợ ở đâu, D3 có mở rộng không",
    # Figure 11.1
    "Non-completion rate, students registered at day 14 (%)":
        "Tỷ lệ không hoàn thành, sinh viên còn đăng ký tại ngày 14 (%)",
    "Rate with 95% Wilson interval": "Tỷ lệ kèm khoảng Wilson 95%",
    "Pooled rate, 22 runs": "Tỷ lệ gộp 22 kỳ mở",
    "2013 (9 runs)": "Năm 2013 (9 kỳ mở)",
    "2014 (13 runs)": "Năm 2014 (13 kỳ mở)",
    "All runs": "Tất cả kỳ mở",
    "no 2013 run": "không mở năm 2013",
    # Figure 11.2
    "Risk difference in non-completion, with sign minus without (percentage points)":
        "Chênh lệch nguy cơ không hoàn thành, có dấu hiệu trừ không có (điểm phần trăm)",
    "Mutually adjusted risk difference in non-completion, with sign minus without (percentage points)":
        "Chênh lệch nguy cơ không hoàn thành đã điều chỉnh đồng thời, có dấu hiệu trừ không có (điểm phần trăm)",
    "Dot: estimate; line: 95% interval": "Chấm: ước lượng; đoạn: khoảng tin cậy 95%",
    "missed_task": "Bài đến hạn tính đến hết ngày 27 chưa nộp",
    "late_tma": "Nộp TMA trễ tính đến hết ngày 27",
    "inactive_last7": "Không có lượt nhấp ngày 21–27",
    "low_relative_activity": "Lượt nhấp ngày 0–27 thấp hơn trung vị kỳ mở",
    "no_pre_start_activity": "Không có lượt nhấp trước ngày 0",
    "runs": "kỳ mở",
}}

SIGN_EN = {
    "missed_task": "Task due by day 27 not submitted",
    "late_tma": "TMA submitted late by day 27",
    "inactive_last7": "No click on days 21–27",
    "low_relative_activity": "Clicks on days 0–27 below run median",
    "no_pre_start_activity": "No click before day 0",
}


def _t(lang):
    return lambda s: T.get(lang, {}).get(s, s)


def _read(name):
    with open(RESULTS / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ----------------------------------------------------------------------------- Figure A.1
CHAIN = [  # (milestone, link, concrete item, role)
    ("M1", [("Stakeholder problem", "Students who stop taking part are found too late for support within the semester"),
            ("Measurable goal", "Completion after add-drop from an assumed 70% to 75% by 2027–2028"),
            ("Analytical questions", "AQ1 descriptive, AQ2 diagnostic, AQ3 predictive, AQ4 prescriptive (ranking)")],
     "person"),
    ("M2", [("Required data",
             "Dated outcome, tasks and activity; three or more runs; open licence; persistent IDs (gates G1–G5)"),
            ("Selected open dataset", "OULAD, 22 runs of 7 modules in 2013–2014; licence CC BY 4.0")], "system"),
    ("M3", [("Actual data fit and gaps", "AQ1–AQ3 yellow, AQ4 red; no attendance, contacts or year of study"),
            ("Prepared data", "OULAD-N04-prepared-1.0; 22 of 22 validation checks pass")], "review"),
    ("M4", [("Candidate methods",
             "Grouped rates; logistic regression within run; penalised logistic model; top-k ranking"),
            ("Evaluation design", "One Evaluation Design Card per AQ; develop on 2013, single test on 2014")],
     "ingest"),
    ("M5", [("Findings and limitations", "AQ1–AQ2 answered on the 2013 and 2014 runs; AQ3–AQ4 proposed"),
            ("Educational decision support",
             "D1 whom to contact, D2 where to place support time, D3 whether to extend")], "agent"),
]


def project_chain(out, lang="en"):
    """Figure A.1: the logic chain of the project, one band per milestone, links numbered in order."""
    t = _t(lang)
    W, label_w, x0, gap_x, gap_y = 6.3, 0.42, 0.05, 0.28, 0.3
    inner = W - x0 - label_w - 0.1 - 0.05
    heights = [0.9 if len(links) == 3 else 0.68 for _, links, _ in CHAIN]
    if lang != "en":
        heights = [h + 0.16 for h in heights]
    total = sum(heights) + gap_y * (len(CHAIN) - 1) + 0.1
    cv = Canvas(W, total)
    y, k, prev = 0.05, 1, None
    for (ms, links, role), h in zip(CHAIN, heights):
        cv.band(x0, y - 0.04, W - 2 * x0, h + 0.08, t(ms))
        n = len(links)
        w = (inner - gap_x * (n - 1)) / n
        nodes = []
        for i, (name, item) in enumerate(links):
            x = x0 + label_w + 0.1 + i * (w + gap_x)
            nodes.append(cv.box(x, y, w, h, f"{k}. {t(name)}", desc=t(item), role=role, light=True,
                                name_fs=9, desc_fs=8))
            k += 1
        for a, b in zip(nodes, nodes[1:]):
            cv.arrow(a, b, sides=("e", "w"), dashed=False)
        if prev is not None:
            mid = prev.y + prev.h + gap_y / 2
            cv.arrow(prev, nodes[0], sides=("s", "n"), dashed=False,
                     via=[(prev.cx, mid), (nodes[0].cx, mid)])
        prev = nodes[-1]
        y += h + gap_y
    cv.trim()
    cv.save(out)


# ----------------------------------------------------------------------------- Figure 11.1
def _wilson(x, n, z=1.959963984540054):
    """Proportion with its 95% Wilson score interval, from the counts (the CSV rates are rounded to 4 decimals)."""
    p = x / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / (1 + z * z / n)
    return p, c - h, c + h



YEARS = [("2013 (9 runs)", "2013/", P.BLUE, -0.17), ("2014 (13 runs)", "2014/", P.ORANGE, 0.17)]


def aq1_rates(out, lang="en"):
    """Figure 11.1: non-completion per module and year, students registered at day 14, 95% Wilson intervals."""
    t = _t(lang)

    def rows(prefix):
        return [r for r in _read(f"{prefix}aq1_rates.csv")
                if r["denominator"] == "day14_registered" and r["measure"] == "non_completion"]

    pooled = next(r for r in rows("all_runs/") if r["level"] == "overall")
    pr = 100 * int(pooled["events"]) / int(pooled["n"])
    groups = ["all 9 runs of 2013"] + ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
    fig, ax = ch.figure(6.3, 3.6, lang=lang)
    labels = []
    for i, g in enumerate(groups):
        if i:
            ax.axhline(i - 0.5, color=P.GRID, lw=0.6, zorder=1)
        labels.append(t("All runs") if i == 0 else g)
        for name, prefix, color, dy in YEARS:
            level = "overall" if i == 0 else "module"
            r = next((x for x in rows(prefix) if x["level"] == level and (i == 0 or x["group"] == g)), None)
            if r is None:
                ax.annotate(t("no 2013 run"), (17, i + dy), ha="left", va="center", fontsize=ch.size("value"),
                            color=P.MUTED, zorder=4)
                continue
            v, lo, hi = (100 * x for x in _wilson(int(r["events"]), int(r["n"])))   # exact, not the stored rate
            ax.plot([lo, hi], [i + dy, i + dy], color=color, lw=ch.size("lw"), solid_capstyle="round", zorder=2)
            ax.plot(v, i + dy, "o", ms=ch.size("marker") * 1.2, color=color, mec=P.SURFACE, mew=1.1, zorder=3)
            ax.annotate(f"{ch.num(v, 1, True)} (n = {ch.num(int(r['n']), 0)})", (hi, i + dy), xytext=(5, 0),
                        textcoords="offset points", ha="left", va="center", fontsize=ch.size("value"),
                        color=P.INK, bbox=ch.PLATE, zorder=4)
    ax.axvline(pr, color=P.MUTED, lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.set_yticks(range(len(groups)), labels)
    ax.set_ylim(len(groups) - 0.5, -0.5)
    ax.set_xlim(15, 75)
    ax.set_xlabel(t("Non-completion rate, students registered at day 14 (%)") + "\n"
                  + t("Dot: estimate; line: 95% interval"), fontsize=ch.size("small"))
    ch.ticks(ax.xaxis)
    ch.legend(ax, [(t(nm), c, "-") for nm, _, c, _ in YEARS]
              + [(f"{t('Pooled rate, 22 runs')} {ch.num(pr, 1, True)}", P.MUTED, (0, (3, 2)))], kind="line")
    ch.save(fig, out)


# ----------------------------------------------------------------------------- Figure 11.2
def aq2_associations(out, lang="en"):
    """Figure 11.2: mutually adjusted risk difference (pp) per early sign in 2013 and 2014, 95% intervals."""
    t = _t(lang)
    comp = {r["sign"]: r for r in _read("compare/aq2_year_comparison.csv")}   # four decimals, refitted
    data = {name: {s: {"rd_adj_mutual_pp": comp[s][f"rd_{y}_pp"], "rd_adj_mutual_ci_low": comp[s][f"ci_low_{y}"],
                       "rd_adj_mutual_ci_high": comp[s][f"ci_high_{y}"]} for s in comp}
            for (name, _, _, _), y in zip(YEARS, ("2013", "2014"))}
    signs = list(SIGN_EN)
    fig, ax = ch.figure(6.3, 3.3, lang=lang)
    labels = []
    for i, s in enumerate(signs):
        labels.append(SIGN_EN[s] if lang == "en" else t(s))
        if i:
            ax.axhline(i - 0.5, color=P.GRID, lw=0.6, zorder=1)
        for name, _, color, dy in YEARS:
            r = data[name][s]
            v, lo, hi = (float(r[f"rd_adj_mutual_{k}"]) for k in ("pp", "ci_low", "ci_high"))
            ax.plot([lo, hi], [i + dy, i + dy], color=color, lw=ch.size("lw"), solid_capstyle="round", zorder=2)
            ax.plot(v, i + dy, "o", ms=ch.size("marker") * 1.2, color=color, mec=P.SURFACE, mew=1.1, zorder=3)
            ax.annotate(f"{ch.num(v, 1)} ({ch.num(lo, 1)}–{ch.num(hi, 1)})", (hi, i + dy), xytext=(5, 0),
                        textcoords="offset points", ha="left", va="center", fontsize=ch.size("value"),
                        color=P.INK, zorder=4)
    ax.axvline(0, color=P.MUTED, lw=1.0, zorder=1)
    ax.set_yticks(range(len(signs)), labels)
    ax.set_ylim(len(signs) - 0.5, -0.5)
    ax.set_xlim(-2, 60)
    ax.set_xticks(range(0, 51, 10))
    ax.set_xlabel(t("Mutually adjusted risk difference in non-completion, with sign minus without (percentage points)")
                  + "\n" + t("Dot: estimate; line: 95% interval"), fontsize=ch.size("small"))
    ch.ticks(ax.xaxis)
    ch.legend(ax, [(t(nm), c, "-") for nm, _, c, _ in YEARS], kind="line")
    ch.save(fig, out)


FIGURES = {
    "fig-1-1-project-chain": project_chain,
    "fig-11-1-aq1-rates": aq1_rates,
    "fig-11-2-aq2-associations": aq2_associations,
}
