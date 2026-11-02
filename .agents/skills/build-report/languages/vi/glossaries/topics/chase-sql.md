# Topic glossary: CHASE-SQL, generate-and-select text-to-SQL

The vocabulary of one report: a critical review of the paper "CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL". It fixes the report's title and part titles, the names of the three generators, the selection-agent vocabulary and the labels of the critical assessment. Domain terms (truy vấn chuẩn, tập ứng viên, bộ sửa truy vấn, tự nhất quán, cận trên …) come from the domain glossary `text-to-sql`. System, model and benchmark names (CHASE-SQL, CHESS, MCS-SQL, XiYan-SQL, Reasoning-SQL, Agentar-Scale-SQL, EllieSQL, BIRD, Spider, Gemini 1.5 Pro, Claude 3.5 Sonnet, Mistral Large, Qwen2.5-Coder) stay as written.

## Title and parts

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL | CHASE-SQL: Suy luận đa hướng và lựa chọn ứng viên tối ưu theo ưu tiên trong chuyển đổi văn bản sang SQL | Report title; the paper's own English title stays in English where the report cites it (paper details, references) | |

## Generators and selection

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| divide-and-conquer chain-of-thought (DC) | CoT chia để trị (DC) | Generator name; "bộ sinh DC" after first use | |
| query-plan chain-of-thought (QP) | CoT theo kế hoạch truy vấn (QP) | Generator name; "bộ sinh QP" after first use | |
| online synthetic example (OS) | ví dụ tổng hợp trực tuyến (OS) | Generator name; "bộ sinh OS" after first use | |
| selection gap | khoảng cách lựa chọn | 13.95 points between self-consistency and the oracle upper bound | |
| execution-equal shortcut | quy tắc trùng kết quả | Credits a candidate without a model call when two results are equal | |
| unique solve | câu hỏi chỉ một bộ sinh giải được | | |
| wrong pick | chọn sai | Selector error category | |
| guideline (R_f, R_t) | hướng dẫn sinh ví dụ | "hướng dẫn theo đặc trưng SQL ($R_f$)", "hướng dẫn theo lược đồ đã lọc ($R_t$)" | |
| refiner | bộ tinh lọc truy vấn | The rejected merging model; not "bộ sửa truy vấn" (query fixer) | |
| multi-path generation | sinh đa hướng | One of the two key contributions the authors claim | |
| multi-task selector | bộ chọn đa nhiệm | | |
| one-way comparison | so sánh một chiều | | |
| set of synthetic examples / guideline set | bộ ví dụ / bộ hướng dẫn | Deck wording; the report keeps its reviewed "nhóm hướng dẫn" | |
| judge / referee (pairwise) | bộ chọn | In CHASE-SQL the pairwise judge is the selection agent: "tác tử lựa chọn (bộ chọn)" at first use, then "bộ chọn"; one component keeps one name, whatever English word the source uses | |
| reviewer (peer review) | người bình duyệt | This report settles "người bình duyệt" for every reviewer | người phản biện |
