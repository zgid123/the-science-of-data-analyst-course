# Domain glossary: text-to-SQL

The vocabulary of reports on translating natural-language questions into SQL with language models: benchmarks and their metrics, the stages of a generate-and-select pipeline, test-time scaling and deployment safety. General database terms (cơ sở dữ liệu, truy vấn, bảng, chỉ mục, schema/lược đồ) and research terms (phương pháp cơ sở, đánh giá chuẩn, thí nghiệm loại bỏ thành phần, zero-shot/few-shot) come from the common layer. Benchmark, system and model names (BIRD, Spider, Spider 2.0, BIRD-Interact, LiveSQLBench, GPT-4o, Gemini 1.5 Pro) stay as written.

## Task and evaluation

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| text-to-SQL | chuyển đổi văn bản sang SQL (text-to-SQL) | First use with English; later "chuyển đổi văn bản sang SQL" or "text-to-SQL" in compound names ("hệ thống text-to-SQL") | dịch văn bản sang SQL |
| natural-language question | câu hỏi bằng ngôn ngữ tự nhiên | | |
| execution accuracy (EX) | độ chính xác thực thi (EX) | Keep "EX" after first use | |
| gold query / ground-truth SQL | truy vấn chuẩn / SQL chuẩn | "truy vấn chuẩn sai" for a wrong gold query | truy vấn vàng, SQL vàng |
| predicted query | truy vấn dự đoán | | |
| result set / execution result | tập kết quả / kết quả thực thi | | |
| valid efficiency score (VES) | điểm hiệu quả hợp lệ (VES) | | |
| reward-based VES (R-VES) | VES dựa trên phần thưởng (R-VES) | | |
| development set / test set / training set | tập phát triển / tập kiểm thử / tập huấn luyện | "tập kiểm thử ẩn" for the hidden test set | tập dev |
| leaderboard | bảng xếp hạng | | |
| evidence sentence / hint (BIRD) | câu gợi ý (evidence) / gợi ý | The external-knowledge sentence of a BIRD question; not "bằng chứng" | |
| dirty value | giá trị bẩn | | |
| annotation error / label noise | lỗi chú thích / nhiễu nhãn | | |
| cross-domain | liên miền | | |
| SQL dialect | phương ngữ SQL | | |
| enterprise workflow | quy trình nghiệp vụ doanh nghiệp | | |

## Generation and selection

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| candidate / candidate query | ứng viên / truy vấn ứng viên | | |
| candidate pool | tập ứng viên | | |
| candidate generator | bộ sinh ứng viên | | |
| selection agent / selector | tác tử lựa chọn / bộ chọn | "bộ chọn" as the short form | |
| query fixer | bộ sửa truy vấn | | |
| value retrieval | truy xuất giá trị | | |
| keyword extraction | trích xuất từ khóa | | |
| schema linking | liên kết lược đồ (schema linking) | First use with English | |
| locality-sensitive hashing (LSH) | băm nhạy cục bộ (LSH) | | |
| edit distance | khoảng cách chỉnh sửa | | |
| embedding similarity | độ tương đồng embedding | | |
| chain-of-thought (CoT) | chuỗi suy luận (chain-of-thought – CoT) | Keep "CoT" after first use | chuỗi suy nghĩ |
| divide-and-conquer | chia để trị | | |
| query plan / execution plan | kế hoạch truy vấn / kế hoạch thực thi | | |
| demonstration / few-shot example | ví dụ minh họa | "ví dụ minh họa few-shot" when the setting matters | |
| synthetic example | ví dụ tổng hợp | | |
| self-consistency | tự nhất quán (self-consistency) | First use with English | tự đồng nhất |
| majority voting | bỏ phiếu đa số | | |
| sampling temperature | nhiệt độ lấy mẫu | | |
| upper bound / lower bound | cận trên / cận dưới | | |
| oracle (selector) | bộ chọn lý tưởng (oracle) | First use with English | |
| adversary (selector) | bộ chọn bất lợi | | |
| pairwise comparison | so sánh từng cặp | | so sánh cặp đôi |
| round-robin tournament | giải đấu vòng tròn | | |
| binary classification | phân loại nhị phân | | |
| listwise ranking / ranker | xếp hạng theo danh sách / bộ xếp hạng | | |
| verifier | bộ kiểm chứng (verifier) | First use with English | |
| self-correction / self-reflection | tự sửa lỗi / tự phản tư | | |
| judge / referee (pairwise) | bộ đánh giá theo cặp / trọng tài | | |
| fuzzy retrieval | truy xuất gần đúng | | |
| common table expression | biểu thức bảng chung (common table expression) | First use with English | |
| many-shot in-context learning | học trong ngữ cảnh với nhiều ví dụ (many-shot) | | |

## Scaling and deployment

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| test-time compute | tính toán khi suy luận (test-time compute) | First use with English | |
| test-time scaling | mở rộng tính toán khi suy luận | | |
| parallel / sequential / internal scaling | mở rộng song song / tuần tự / nội tại | | |
| reinforcement learning (RL) | học tăng cường (RL) | | |
| reward / partial reward | phần thưởng / phần thưởng từng phần | | |
| complexity-aware routing | định tuyến theo độ phức tạp | | |
| clarifying question | câu hỏi làm rõ | | |
| prompt injection / SQL injection | tấn công chèn prompt / tấn công chèn SQL (SQL injection) | | |
| read-only role / SELECT-only role | vai trò chỉ đọc / vai trò chỉ được SELECT | | |
| sandbox / sandboxed execution | môi trường cô lập (sandbox) / thực thi trong môi trường cô lập | | |
| timeout | giới hạn thời gian chạy (timeout) | First use with English | |
| contamination-free | không bị rò rỉ dữ liệu kiểm thử | | |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| schema union | hợp lược đồ | | |
| vague question / ambiguous question | câu hỏi mơ hồ | | |
| token elasticity of performance (TEP) | độ co giãn hiệu năng theo token (TEP) | | |
| undisclosed method (leaderboard) | phương pháp không công khai | A leaderboard entry without a paper or code | |
| ensemble (of generators) | tập hợp bộ sinh | "tập hợp mô hình" when models are meant | tổ hợp bộ sinh |
| challenging (BIRD difficulty) | thử thách | "câu hỏi thử thách"; simple / moderate: "đơn giản" / "trung bình" | |
| generator mix | cách kết hợp các bộ sinh | | |
| cluster of candidates (by execution result) | cụm ứng viên / cụm | "cụm lớn nhất", "cụm đúng", "cụm đa số"; "nhóm" is kept for people ("nhóm tác giả") | |
