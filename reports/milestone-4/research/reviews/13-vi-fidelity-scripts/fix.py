"""fix.py: apply the fidelity-2 corrections to the Vietnamese twins of Milestone 4.
Each before-string must occur exactly once in its twin, or the run aborts before writing anything.
Usage: venv/bin/python reports/milestone-4/research/vi-review/fidelity-2-2026-11-08-scripts/fix.py"""
import pathlib, sys

root = pathlib.Path(__file__).resolve().parents[3] / "report"

EDITS = [
    # 1. 01-01: the English names both questions with their Change Log entries (C10, C13), "as described below"
    ("01-01-goal-decisions-aqs.vi.md",
     "Đồng thời, các thay đổi này điều chỉnh cách đo của hai câu hỏi AQ3 và AQ4, qua hai định nghĩa trình bày ở cuối mục này.",
     "Đồng thời, các thay đổi này xác định lại cách đo của hai câu hỏi, AQ3 (C10) và AQ4 (C13), như trình bày dưới đây."),
    # 2. 03-03: start month has two levels and enters as one dummy; state the coding the code uses
    ("03-03-predictive.vi.md",
     "Module và tháng bắt đầu là biến phân loại, nên mỗi biến đi vào mô hình dưới dạng nhiều số hạng (biến giả); vì vậy, 19 biến dự báo tương ứng với tổng cộng 23 tham số.",
     "Module và tháng bắt đầu là biến phân loại nên được đưa vào mô hình dưới dạng biến giả, mỗi mức (trừ một mức tham chiếu) là một số hạng; vì vậy, 19 biến dự báo tương ứng với tổng cộng 23 tham số."),
    # 3. 04-01: "first missed task by week" read as "the first task was missed"
    ("04-01-evaluation-cards.vi.md",
     "| Chỉ số phụ | Tỷ lệ cộng dồn các lượt đăng ký học đã bỏ lỡ bài được chấm điểm đầu tiên, tính đến từng tuần và tách theo kết quả cuối cùng |",
     "| Chỉ số phụ | Tỷ lệ cộng dồn các lượt đăng ký học đã lần đầu bỏ lỡ một bài được chấm điểm, tính đến từng tuần và tách theo kết quả cuối cùng |"),
    # 4. 04-01: the English term is "confirmatory check"
    ("04-01-evaluation-cards.vi.md",
     "Kiểm định khẳng định (confirmatory test), tức kiểm định chính thức",
     "Kiểm định khẳng định (confirmatory check), tức kiểm định chính thức"),
    # 5. 04-02: resample is "mẫu lấy lại" (glossary, paired two-level bootstrap)
    ("04-02-validation-strategy.vi.md",
     "được tính trên cùng mẫu lặp đó.",
     "được tính trên cùng mẫu lấy lại đó."),
    # 6. 04-02: Riley criterion (iii) is the overall risk of the development data
    ("04-02-validation-strategy.vi.md",
     "nguy cơ chung, tức tỷ lệ không hoàn thành tính trên toàn bộ dữ liệu, được",
     "nguy cơ chung, tức tỷ lệ không hoàn thành tính trên toàn bộ dữ liệu phát triển, được"),
    # 7. 04-03: "context" for net benefit, same words as 04-01 ("chỉ dùng để tham khảo")
    ("04-03-metrics-success.vi.md",
     "lợi ích ròng chỉ là thông tin bối cảnh chứ không phải tiêu chí.",
     "lợi ích ròng chỉ dùng để tham khảo chứ không phải tiêu chí."),
    # 8. 06-00: role glosses restated the role name; say what each role does, as the English does
    ("06-00-genai-usage.vi.md",
     "AI phản biện lựa chọn mô hình (model-selection critic), tức một AI đóng vai người phản biện, dùng để chất vấn các AQ Modeling Brief",
     "AI phản biện lựa chọn mô hình (model-selection critic), là vai trò trong đó AI chất vấn các AQ Modeling Brief"),
    ("06-00-genai-usage.vi.md",
     "AI rà soát thiết kế đánh giá (evaluation reviewer), tức một AI đóng vai người rà soát, dùng để phản biện các Evaluation Design Card",
     "AI rà soát thiết kế đánh giá (evaluation reviewer), là vai trò trong đó AI phản biện các Evaluation Design Card"),
    # 9. 06-00: a reason the English does not give (the critique was that 2013 holds 6 modules, not 7)
    ("06-00-genai-usage.vi.md",
     "lấy từ 6 module của các kỳ mở huấn luyện, để không dùng đến dữ liệu của tập kiểm thử;",
     "lấy từ 6 module của các kỳ mở huấn luyện;"),
    # 10. 10-06 row 6: English now "on a run after the 2014 test runs"
    ("10-06-ai-critiques.vi.md",
     "chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở diễn ra sau |",
     "chỉ hiệu chuẩn lại trong giai đoạn phát triển hoặc trên một kỳ mở diễn ra sau các kỳ mở năm 2014 của tập kiểm thử |"),
]

texts = {}
for name, before, after in EDITS:
    t = texts.setdefault(name, (root / name).read_text())
    n = t.count(before)
    if n != 1:
        sys.exit(f"ABORT {name}: before-string found {n} times: {before[:80]}")
    texts[name] = t.replace(before, after)
for name, t in texts.items():
    (root / name).write_text(t)
print(f"applied {len(EDITS)} edits to {len(texts)} twins: {', '.join(sorted(texts))}")
