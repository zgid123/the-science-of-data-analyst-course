# Domain glossary: usage control (UCON)

The vocabulary of texts on usage control and attribute-based access control: the UCON_ABC model of Park and Sandhu, its decision phases and mutability, the components of a policy architecture (PDP, PEP, PIP, PAP), and the reliability terms used when such an engine is examined. General security terms (kiểm soát truy cập, xác thực, phân quyền, dấu vết kiểm toán, bề mặt tấn công, lỗ hổng) come from the common layer. Model labels (preA0, onB1, onC0), identifiers in code, finding IDs (AC-01, UC-07) and names of standards (XACML, NIST SP 800-162) stay as written.

## Model

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| usage control (UCON) | kiểm soát sử dụng (UCON) | First use with the abbreviation; "UCON" afterwards | |
| attribute-based access control (ABAC) | kiểm soát truy cập dựa trên thuộc tính (ABAC) | | |
| subject / object / right | chủ thể / đối tượng / quyền | | |
| attribute / mutable attribute | thuộc tính / thuộc tính khả biến | | |
| authorization (UCON A) / obligation (B) / condition (C) | cấp quyền / nghĩa vụ / điều kiện | The three decision factors of UCON_ABC | |
| pre phase / ongoing phase | giai đoạn trước khi sử dụng (pre) / giai đoạn trong khi sử dụng (on) | Short form "giai đoạn pre", "giai đoạn on" after first use | |
| continuity (of decisions) | tính liên tục | "tính liên tục của quyết định" | |
| mutability / pre-update / on-update / post-update | tính khả biến / cập nhật trước / cập nhật trong / cập nhật sau | Keep "pre-update", "post-update" when the text names the code concept | |
| usage session | phiên sử dụng | "phiên" alone after first use | |
| revocation / revoke | thu hồi / thu hồi quyền | | |
| grant (a request) / deny | cấp quyền / từ chối | | |
| policy / policy version | chính sách / phiên bản chính sách | | |
| safety (analysis) / undecidable | bài toán an toàn / không quyết định được | | |

## Architecture and assurance

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| reference monitor | bộ giám sát tham chiếu (reference monitor) | First use with English | |
| always invoked / tamper-proof / verifiable | luôn được gọi / chống can thiệp / kiểm chứng được | Anderson's three properties | |
| trusted computing base (TCB) | cơ sở tính toán tin cậy (TCB) | | |
| policy decision point (PDP) | điểm quyết định chính sách (PDP) | | |
| policy enforcement point (PEP) | điểm thực thi chính sách (PEP) | | |
| policy information point (PIP) | điểm cung cấp thông tin chính sách (PIP) | | |
| policy administration point (PAP) | điểm quản trị chính sách (PAP) | | |
| fail-safe defaults | nguyên tắc mặc định an toàn | | |
| fail open / fail closed | mở khi lỗi (fail-open) / đóng khi lỗi (fail-closed) | First use with English | |
| lease (time-bounded grant) | lease (quyền có thời hạn) | Keep "lease"; gloss at first use | |
| liveness signal / heartbeat | tín hiệu còn hoạt động / heartbeat | | |
| exactly-once / at-least-once / at-most-once | đúng một lần / ít nhất một lần / nhiều nhất một lần | Delivery and processing guarantees | |
| idempotency | tính lũy đẳng | | |
| separation of duty | phân tách nhiệm vụ | | |
| step-up authentication | xác thực tăng cường (step-up) | | |
| demo mode | chế độ demo | | |

## Examination

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| viva / defence | buổi bảo vệ | | |
| examiner | giám khảo | | |
| passing answer | câu trả lời đạt | | |
| finding (of a review) | phát hiện | "phát hiện AC-01" | |
| grading rubric | thang chấm điểm | | |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| attribute store | kho thuộc tính | | |
| derived attribute | thuộc tính dẫn xuất | | |
| update directive | chỉ thị cập nhật | | |
| policy snapshot | ảnh chụp chính sách (snapshot) | | |
| re-evaluation | đánh giá lại | | |
| combining rule / deny-overrides | quy tắc kết hợp / deny-overrides | Keep "deny-overrides" | |
| model conformance test | kiểm thử tính tuân thủ mô hình | | |
| advice (XACML) | khuyến nghị (advice) | | |
| target (of a policy) | phạm vi áp dụng (target) | First use with English | |
| decision log | nhật ký quyết định | | |
| XACML 3.0 | XACML phiên bản 3.0 | The decimal check reads "3.0" as a number | |
