# Part 4 Claims

One row per claim. Claim IDs are C4-001, C4-002, … The quote anchor is one or more "…" quotes (at least 8 characters each) copied verbatim from the source's crawl.md. Avoid the | character inside cells (write \| if a quote contains one).

| Claim ID | Claim | Exact value or quote anchor | Source ID | Primary or secondary | Report file(s) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| C4-001 | GREEN: variables, population, time window and quality suffice for the claim; YELLOW: partial support; RED: key concept, variable, target or intervention missing. | "GREEN – Full support" "YELLOW – Partial support" "RED – Unsupported" | S001 | primary | 04-00-aq-data-fit.md |
| C4-002 | When data do not support an AQ, the priority is derive from real data, add compatible real data, narrow or rewrite, then defer or drop; synthetic data is not a step to save a question. | "thứ tự ưu tiên là: (1) kiểm chứng/derive hợp lệ từ real data" | S001 | primary | 04-00-aq-data-fit.md,04-02-gap-decisions.md |
| C4-003 | A missing variable or concept that the dataset never collected must not be imputed or generated as real data. | "Không được impute/sinh giả như dữ liệu thật." | S001 | primary | 04-02-gap-decisions.md |
| C4-004 | Small synthetic data for testing code, schema or ETL is allowed if labelled synthetic and kept out of conclusions. | "Dùng dữ liệu giả nhỏ để kiểm thử code, schema, ETL hoặc visualization." | S001 | primary | 04-02-gap-decisions.md |
