# Part 1 Claims

One row per claim. Claim IDs are C1-001, C1-002, … The quote anchor is one or more "…" quotes (at least 8 characters each) copied verbatim from the source's crawl.md. Avoid the | character inside cells (write \| if a quote contains one).

| Claim ID | Claim | Exact value or quote anchor | Source ID | Primary or secondary | Report file(s) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C1-001 | Requirements decide which data to find; data must not change project goals arbitrarily. | "Requirement quyết định dữ liệu cần tìm" | S001 | primary | 01-01-frozen-baseline.md |
| C1-002 | Milestone 2 must answer which data the committed AQs need and whether the collected open dataset provides them. | "Milestone 2 phải trả lời được hai câu hỏi" | S001 | primary | 01-00-baseline-scope.md,01-02-scope-change-log.md |
| C1-003 | No missing-value removal, imputation, normalisation, feature engineering, class balancing or model training in Milestone 2. | "Không xóa missing values, không impute, không chuẩn hóa, không feature engineering" | S001 | primary | 01-02-scope-change-log.md |
| C1-004 | Before searching, the team must freeze a baseline from the Milestone 1 proposal. | "Trước khi tìm dataset, nhóm phải" | S001 | primary | 01-01-frozen-baseline.md |
| C1-005 | The structural check is minimal and is not a full EDA. | "không phải EDA đầy đủ" | S001 | primary | 06-00-structural-verification.md |
| C1-006 | Raw data must be kept unchanged to ensure provenance and reproducibility. | "Raw data phải được giữ nguyên" | S001 | primary | 05-00-acquisition-provenance.md |
| C1-007 | The search must log queries, use official sources, read documentation and license, and trace re-uploads to the original. | "nếu phát hiện dataset qua blog/Kaggle/GitHub thì phải lần về nguồn gốc chính thức" | S001 | primary | 03-00-search-strategy.md |
| C1-008 | A high-scoring dataset can still be rejected if it lacks a required target, timing for predictive AQs or the right of use. | "Một dataset đạt tổng điểm cao nhưng thiếu target bắt buộc" | S001 | primary | 04-01-criteria-gates.md |
| C1-009 | The selection uses ten criteria scored 0, 1 or 2. | "0 = không đáp ứng, 1 = đáp ứng một phần, 2 = đáp ứng tốt" | S001 | primary | 04-01-criteria-gates.md |
| C1-010 | Partial coverage: keep or narrow the AQ and state what can and cannot be answered. | "Giữ hoặc thu hẹp AQ; ghi rõ phần nào có thể/không thể trả lời và vì sao" | S001 | primary | 07-02-gaps-revisions.md |
| C1-011 | AI must not create datasets, variables, licenses, statistics or download sources. | "AI không được phép" | S001 | primary | 09-00-genai-reflection.md |
| C1-012 | No synthetic evidence may fill a data gap. | "không tạo synthetic evidence" | S001 | primary | 09-00-genai-reflection.md |
