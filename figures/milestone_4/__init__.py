"""Figures of the Milestone 4 report (reports/milestone-4), drawn with the build-report visual kit.

Figure 2.1 maps each analytical question to its technical task, output and decision (Appendix I); Figure 4.1 shows
the validation and test protocol (Appendix IV, Table A.13), with the run counts of the prepared views.
Render: venv/bin/python .claude/skills/build-report/scripts/render_figures.py milestone-4
"""
from __future__ import annotations

import diagrams as dg
from c4kit import Canvas

T = {"vi": {
    "Descriptive": "Mô tả", "Diagnostic": "Chẩn đoán", "Predictive": "Dự báo", "Prescriptive": "Đề xuất",
    "Question": "Câu hỏi", "Technical task": "Bài toán kỹ thuật", "Output": "Đầu ra", "Decision": "Quyết định",
    "Outcome shares by module and run": "Tỷ lệ kết quả theo module và kỳ mở",
    "Signs by week 4 linked to non-completion": "Dấu hiệu đến tuần 4 gắn với không hoàn thành",
    "Non-completion estimated at day 13 and day 27": "Ước lượng không hoàn thành tại ngày 13 và ngày 27",
    "Who ranks first under capacity": "Ai xếp đầu trong giới hạn năng lực liên hệ",
    "Aggregation": "Tổng hợp", "Association within run": "Mối liên hệ trong từng kỳ mở",
    "Classification": "Phân loại", "Ranking at capacity": "Xếp hạng theo năng lực liên hệ",
    "Rates with 95% intervals": "Tỷ lệ kèm khoảng tin cậy 95%",
    "Risk differences and odds ratios": "Chênh lệch nguy cơ và tỉ số odds",
    "Risk score per enrolment": "Điểm nguy cơ cho mỗi lượt đăng ký học",
    "Ranked list with reasons": "Danh sách xếp hạng kèm lý do",
    "D2, D3: where to look, whether to extend": "D2, D3: tập trung vào đâu, có mở rộng không",
    "D2; reasons on the D1 list": "D2; lý do trong danh sách D1",
    "D1: who is listed": "D1: ai được đưa vào danh sách",
    "D1: tutor decides whom to contact": "D1: giảng viên quyết định liên hệ ai",
    "First freeze": "Chốt lần thứ nhất",
    "Questions, splits, metrics, baselines and success criteria fixed": "Cố định câu hỏi, cách chia dữ liệu, chỉ số, mốc so sánh và tiêu chí thành công",
    "Develop on 9 runs of 2013": "Phát triển trên 9 kỳ mở năm 2013",
    "Leave-one-run-out folds, students kept on one side, tuning nested": "Loại trừ từng kỳ mở, mỗi sinh viên chỉ ở một phía, tinh chỉnh lồng nhau",
    "Second freeze": "Chốt lần thứ hai",
    "Chosen model refitted on 2013, recorded with its hash": "Mô hình được chọn khớp lại trên 2013, ghi kèm mã băm",
    "Single test on 13 runs of 2014": "Kiểm tra một lần trên 13 kỳ mở năm 2014",
    "9 paired and 4 unpaired runs, scored once and logged": "9 lượt có cặp và 4 lượt không có cặp, chấm một lần và ghi nhật ký",
    "Report and replicate": "Báo cáo và lặp lại",
    "Pooled and per-run results; AQ2 replicated on 2014": "Kết quả gộp và theo kỳ mở; lặp lại AQ2 trên 2014",
}}


def _t(lang):
    return lambda s: T.get(lang, {}).get(s, s)


def aq_map(out, lang="en"):
    """Figure 2.1: each AQ, its technical task, its output and the decision it supports."""
    t = _t(lang)
    rows = [
        ("AQ1", "Descriptive", "Outcome shares by module and run", "Aggregation", "Rates with 95% intervals",
         "D2, D3: where to look, whether to extend"),
        ("AQ2", "Diagnostic", "Signs by week 4 linked to non-completion", "Association within run",
         "Risk differences and odds ratios", "D2; reasons on the D1 list"),
        ("AQ3", "Predictive", "Non-completion estimated at day 13 and day 27", "Classification",
         "Risk score per enrolment", "D1: who is listed"),
        ("AQ4", "Prescriptive", "Who ranks first under capacity", "Ranking at capacity", "Ranked list with reasons",
         "D1: tutor decides whom to contact"),
    ]
    w, h, gap_x, gap_y, head = 1.45, 0.8, 0.13, 0.12, 0.52
    total = head + 4 * h + 3 * gap_y + 0.1
    cv = Canvas(6.3, total + 0.1)
    xs = [0.05 + k * (w + gap_x) for k in range(4)]
    for x, lab in zip(xs, (t("Question"), t("Technical task"), t("Output"), t("Decision"))):
        cv.lane(x - 0.04, 0.05, w + 0.08, total, lab)
    roles = ["system", "external", "warehouse", "person"]
    for i, (aq, level, q, task, output, dec) in enumerate(rows):
        y = 0.05 + head + i * (h + gap_y)
        b = [cv.box(xs[0], y, w, h, f"{aq} – {t(level)}", desc=t(q), role=roles[0]),
             cv.box(xs[1], y, w, h, t(task), role=roles[1]),
             cv.box(xs[2], y, w, h, t(output), role=roles[2]),
             cv.box(xs[3], y, w, h, t(dec), role=roles[3])]
        for a, c in zip(b, b[1:]):
            cv.arrow(a, c)
    cv.trim()
    cv.save(out)


def validation(out, lang="en"):
    """Figure 4.1: from the first freeze to the single test on the 2014 runs."""
    t = _t(lang)
    dg.process([
        (t("First freeze"), t("Questions, splits, metrics, baselines and success criteria fixed"), "lock"),
        (t("Develop on 9 runs of 2013"), t("Leave-one-run-out folds, students kept on one side, tuning nested"),
         "gear"),
        (t("Second freeze"), t("Chosen model refitted on 2013, recorded with its hash"), "lock"),
        (t("Single test on 13 runs of 2014"), t("9 paired and 4 unpaired runs, scored once and logged"), "check"),
        (t("Report and replicate"), t("Pooled and per-run results; AQ2 replicated on 2014"), "search"),
    ]).save(out)


FIGURES = {"fig-2-1-aq-map": aq_map, "fig-4-1-validation": validation}
