# S001 – MTH045 Milestone P3 brief: From understanding to preparation (2026)

## Summary in my own words

The instructor brief for Milestone 3 asks the team to check the fit and quality of the open dataset collected in Milestone 2, understand its structure, content and limits, and build a reproducible preparation pipeline that produces an analytic-ready dataset for modelling in Milestone 4. It fixes the required inputs from Milestone 2 and an entry gate, seven working principles, an eight-step process, eight tasks with their tables (Dataset Understanding Map, Data Quality Issue Log, GREEN/YELLOW/RED fit ratings, Preparation Decision Matrix, pipeline steps, leakage rules, Model Readiness Matrix, Data Lineage Table), a synthetic-data policy, the allowed roles of generative AI with an AI Decision Log, six deliverables, a ten-section report structure of 8–12 pages, a checklist and the conditions for moving to Milestone 4.

## Key facts

- Goal – "xây dựng một quy trình chuẩn bị dữ liệu có thể tái lập để tạo Analytic-ready Dataset làm đầu vào cho giai đoạn Modeling & Evaluation"
- Principle – "Mọi quyết định chuẩn bị dữ liệu phải có lý do gắn với Analytical Question"
- Raw immutable – "Không chỉnh sửa file trong data/raw. Mọi xử lý tạo file/version mới trong data/interim hoặc data/processed."
- No modelling – "Milestone này có thể chuẩn bị split/feature structure, nhưng chưa tối ưu mô hình"
- Fit ratings – "GREEN – Full support", "YELLOW – Partial support", "RED – Unsupported"
- Synthetic data – "synthetic data không được dùng để tạo bằng chứng thực nghiệm mà dữ liệu thật không có"
- Priority rule – "thứ tự ưu tiên là: (1) kiểm chứng/derive hợp lệ từ real data"
- Leakage rule – "Feature chỉ được dùng nếu tồn tại trước prediction point."
- Fitted transforms – "fit transform trên training và apply sang validation/test"
- Sensitive attributes – "có thể giữ để audit fairness nhưng hạn chế dùng làm predictor tùy bối cảnh và policy"
- AI is not a data source – "AI là partner cho reasoning/coding; evidence phải đến từ dữ liệu và nguồn chính thức."
- Deliverables – "báo cáo Milestone 3"
- Length – "Báo cáo nên khoảng 8–12 trang nội dung chính, không tính phụ lục, code và data files."
- Prescriptive limit – "chỉ giữ ở mức decision requirement/future work"

## Used in

Every part: Part 1 (inputs, entry gate), Part 2 (Task 1), Part 3 (Task 2), Part 4 (Task 3, sections 8.1–8.3), Part 5 (Task 4), Part 6 (Tasks 5–6), Part 7 (Task 8), Part 8 (Task 7), Part 10 (section 14).

## Against reference.md

The outline is derived from this brief; no conflict. The brief's recommended folder structure (section 10.1) is followed inside the task's `package/` folder.

## Reliability

Primary: the instructor's own brief for the course, verified Markdown copy of `milestone-3.pdf` in the repository.

## Open questions

The rubric (section 18) lists criteria without point values ("NA"); the report covers every criterion.
