# Topic glossary: AutoDCWorkflow, LLM-generated data cleaning workflows and their benchmark

The vocabulary of one report: a critical review of the paper "AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation and Benchmark". It fixes the report's title and part titles, the names of the three agents, the benchmark's references and metrics, and the labels of the critical assessment. General data-cleaning terms (làm sạch dữ liệu, chiều chất lượng dữ liệu, thao tác, lịch sử thao tác, chèn lỗi …) come from the domain glossary `data-cleaning`; research terms (bình duyệt, phương pháp cơ sở, độ chính xác dương, độ phủ …) from the common layer. System, model, dataset and tool names (AutoDCWorkflow, OpenRefine, Llama 3.1-8B, Gemma 2-27B, CFI, PPP, Ollama, Pith, OpenReview) stay as written.

## Title and parts

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation and Benchmark | AutoDCWorkflow: Tự động sinh quy trình làm sạch dữ liệu dựa trên mô hình ngôn ngữ lớn và xây dựng bộ đánh giá chuẩn | Report title, sentence case; the title page sets it in capitals. The paper's own English title stays in English where the report cites it (paper details, references) | |
| AutoDCWorkflow (short title) | AutoDCWorkflow: Tự động sinh quy trình làm sạch dữ liệu | Running header | |

## Method and agents

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| three-stage LLM pipeline | pipeline LLM ba giai đoạn | | |
| Select Target Columns (agent) | Select Target Columns | Keep the agent name in English as a proper name; first use in a file "tác tử Select Target Columns (chọn cột đích)", later "tác tử Select Target Columns" or "tác tử chọn cột" | |
| Inspect Column Quality (agent) | Inspect Column Quality | First use "tác tử Inspect Column Quality (kiểm tra chất lượng cột)", later "tác tử Inspect Column Quality" or "tác tử kiểm tra" | |
| Generate Operation and Arguments (agent) | Generate Operation and Arguments | First use "tác tử Generate Operation and Arguments (sinh thao tác và đối số)", later "tác tử Generate Operation and Arguments" or "tác tử sinh thao tác" | |
| column-selection agent / inspection agent / operation agent | tác tử chọn cột / tác tử kiểm tra / tác tử sinh thao tác | Short descriptive forms used in running text | |
| Data Quality Report | Báo cáo chất lượng dữ liệu (Data Quality Report) | Proper name of the second agent's output; first use with English | |
| flag (True / False) | cờ (True / False) | True and False stay in English as the agent's output values | |
| vote (on whether a column is finished) | lượt bỏ phiếu | "ba lượt bỏ phiếu" | |
| operation toolkit | bộ thao tác | Also a section heading | hộp công cụ thao tác |
| few-shot example | ví dụ few-shot | "few-shot" stays English (common layer) | |
| Direct Prompting (DP) | prompt trực tiếp (Direct Prompting – DP) | Baseline name: first use "phương pháp cơ sở prompt trực tiếp (Direct Prompting – DP)", later "DP" | nhắc trực tiếp |
| raw-table baseline | phương pháp cơ sở bảng thô | "bảng thô không làm sạch" | |

## Benchmark and references

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| benchmark (AutoDCWorkflow's) | bộ đánh giá chuẩn | "bộ đánh giá chuẩn gồm 142 mục đích"; "benchmark" stays in names of other benchmarks (CDR-Bench, DataGovBench) | |
| purpose category | nhóm mục đích | | |
| Descriptive Statistics / Counting and Grouping / Category or Type Classification | Thống kê mô tả / Đếm và nhóm / Phân loại theo nhóm hoặc kiểu | Purpose category names | |
| Time-based Analysis / Correlations and Relationships / Filtering and Specific Queries | Phân tích theo thời gian / Tương quan và quan hệ / Lọc và truy vấn cụ thể | Purpose category names | |
| purpose complexity | độ phức tạp của mục đích | | |
| curated workflow / human-curated workflow | quy trình được xây dựng thủ công / quy trình do con người xây dựng | The benchmark's fifth element, the expert's workflow per purpose (the silver workflow); "hiệu chỉnh" (adjust) misreads it | quy trình được hiệu chỉnh |
| curated clean table | bảng sạch được hiệu chỉnh thủ công | Short "bảng sạch tham chiếu" | bảng sạch được tuyển chọn |
| silver workflow / silver-standard ground truth | quy trình chuẩn bạc (silver workflow) / nhãn chuẩn bạc | First use with English; "chuẩn bạc" against "chuẩn vàng" (gold standard) | quy trình bạc |
| gold-standard workflow | quy trình chuẩn vàng | | |
| expert (who wrote the silver workflows) | chuyên gia làm sạch dữ liệu | | |

## Evaluation

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| Purpose Answer (dimension) | Câu trả lời cho mục đích (Purpose Answer) | Dimension name; first use with English; table header "Câu trả lời" | |
| Column Value (dimension) | Giá trị cột (Column Value) | Dimension name; first use with English | |
| Workflow (dimension) / Workflow (Operation) | Quy trình (Workflow) / Quy trình (Thao tác) | Dimension name; RQ3 label "Quy trình (Thao tác)" | |
| RQ1, RQ2, RQ3 | RQ1, RQ2, RQ3 | Keep the paper's labels, defined in the abbreviation list as "câu hỏi nghiên cứu (RQ)"; not CH1–CH3, which name the report's own questions in other tasks | |
| column cleanness ratio / column ratio | tỷ lệ sạch theo cột / tỷ lệ cột | First use "tỷ lệ sạch theo cột (column cleanness ratio)", in result tables "tỷ lệ cột (column ratio)" | tỷ lệ độ sạch cột |
| accuracy (evaluation property of the Purpose Answer dimension) | tính chính xác | Same form as the quality dimension; with tính nhất quán and tính hợp lý names the three evaluation properties | |
| exact match | khớp chính xác | "tỷ lệ khớp chính xác"; table header "Khớp chính xác" | trùng khớp hoàn toàn |
| Similarity (metric) | Similarity | Keep the metric name in English; first use "chỉ số Similarity (độ tương đồng chuỗi)" | |
| F1 score / answer F1 / workflow F1 | điểm F1 / F1 câu trả lời / F1 quy trình | | |

## Critical assessment

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| meta-review | đánh giá tổng hợp (meta-review) | First use with English | |
| senior area chair / programme chair | chủ tịch lĩnh vực cấp cao / chủ tịch chương trình | ARR roles | |
| the group's own analysis / the group's reading | phân tích của nhóm / cách đọc của nhóm | Marks the report's own analysis; "theo phân tích của nhóm" | |
| critique-induced confusion | nhiễu loạn do phản biện (critique-induced confusion) | First use with English | |
| evidence-gated generation | sinh có kiểm soát bằng bằng chứng | | |
| curator copilot | trợ lý cho người hiệu chỉnh dữ liệu | | |
| drift between versions | sai lệch giữa các phiên bản | | |
| conditional (Pith rating) | "có điều kiện" (conditional) | Pith's verdict label: the central claim is sound but at least one issue must be addressed; not an acceptance decision | chấp nhận có điều kiện |
| workflow shape | cấu trúc của quy trình | Which operations a workflow uses and how long it is; also a section heading | hình dạng của quy trình |
| safeguard | biện pháp bảo vệ | This report keeps "biện pháp bảo vệ" where it first wrote "cơ chế bảo vệ" | cơ chế bảo vệ |
| graphics card / GPU | bộ xử lý đồ họa | This report keeps "bộ xử lý đồ họa" throughout | card đồ họa |
