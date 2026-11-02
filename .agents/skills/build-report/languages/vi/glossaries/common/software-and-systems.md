# Common glossary: software and systems

Architecture, interfaces, operations and reliability of software systems. Loaded for every report.

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| system / subsystem | hệ thống / phân hệ | | |
| architecture | kiến trúc | | |
| hybrid architecture | kiến trúc lai (Hybrid) | | |
| component / module | thành phần / mô-đun | | |
| service / microservice | dịch vụ / vi dịch vụ (microservice) | | |
| interface / API | giao diện / API | Keep "API", "typed API", "Retrieval API" | |
| backend / frontend | backend / frontend | Keep English | |
| client / server | máy khách / máy chủ | | |
| request / response | yêu cầu / phản hồi | | |
| endpoint | điểm cuối (endpoint) | | |
| pipeline | pipeline | Keep English; "quy trình xử lý" when describing steps | |
| workflow | luồng công việc | | |
| orchestrator / orchestration | bộ điều phối (orchestrator) / điều phối | | |
| router / routing | bộ định tuyến (Router) / định tuyến | | |
| queue / review queue | hàng đợi / hàng đợi duyệt | | |
| cache | cache | Keep English | |
| latency | độ trễ | "độ trễ đầu-cuối", "độ trễ backend" | |
| throughput | thông lượng | | |
| scalability | khả năng mở rộng | | |
| availability / reliability | tính sẵn sàng / độ tin cậy | | |
| fault tolerance | khả năng chịu lỗi | | |
| failure / failure handling | lỗi / xử lý lỗi (failure handling) | | |
| fallback | phản hồi dự phòng (fallback) | | |
| retry / backoff | thử lại / giãn cách thử lại (backoff) | | |
| timeout | hết thời gian chờ (timeout) | | |
| idempotent | lũy đẳng (idempotent) | | |
| read-only | chỉ đọc (read-only) | | |
| side effect | tác dụng phụ | | |
| deduplication | chống trùng lặp | | |
| concurrency | xử lý đồng thời | | |
| deployment / production | triển khai / môi trường vận hành thực tế | "production-ready" → "sẵn sàng triển khai thực tế" | |
| blue-green deployment | triển khai blue-green | | |
| sandbox | sandbox | Keep English | |
| configuration | cấu hình | | |
| dependency / pinned version | phụ thuộc / phiên bản cố định | | |
| version / versioning | phiên bản / versioning | Keep "versioning" | |
| drift (version) | lệch phiên bản | | lệch version, trôi phiên bản |
| release | bản phát hành | | |
| snapshot / manifest / checksum | snapshot / manifest / checksum | Keep English | |
| log / logging / audit log | nhật ký / ghi nhật ký / nhật ký kiểm toán | | |
| monitoring | giám sát | | |
| maintenance effort | công sức vận hành | | |
| cost | chi phí | | |
| tool / tool call | công cụ / lời gọi công cụ | | |
| tool contract | hợp đồng công cụ (tool contract) | | |
| schema | schema | Keep English; "lược đồ" in prose about databases | |
| field / parameter | trường / tham số | Field names in backticks stay as written | |
| user / end user | người dùng / người dùng cuối | | |
| stakeholder | bên liên quan | | |
| use case | trường hợp sử dụng | | |
| C4 model: System Context | Ngữ cảnh hệ thống (System Context) | | |
| C4 model: Container | Container | Keep English | |
| C4 model: Component | Thành phần (Component) | | |
| C4 model: Code | Mã (Code) | | |
| C4 levels (Level 1 … Level 4) | Cấp 1 … Cấp 4 | | |
| system boundary | ranh giới hệ thống | | |
| zooms into | phóng to | | |
| refresh rate (display) | tần số quét | | tần số làm tươi |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| risk flag (rule-based) | cờ rủi ro (dựa trên quy tắc) | | |
| unit test / unit tester | kiểm thử đơn vị / bộ kiểm thử đơn vị | | |
| name clash | trùng tên | | |
| interactive use | sử dụng tương tác | | |
| iterative loop / iteration | vòng lặp / lặp | "quy trình lặp", "lượt lặp" for an iteration | |
| stopping rule | quy tắc dừng | | |
| graphics card / GPU | bộ xử lý đồ họa | "bốn bộ xử lý đồ họa NVIDIA A100"; "card đồ họa" for the physical card | |
| safeguard | biện pháp bảo vệ | Against error propagation, or for a practical use | |
| web client | ứng dụng web phía client | | |
| keyed lock | khóa theo định danh (keyed lock) | First use with English | khóa theo khóa |
| one-shot timer | bộ hẹn giờ một lần (one-shot timer) | First use with English | |
| seed data / seed policies | dữ liệu khởi tạo / chính sách khởi tạo | | |
| migration (database) | migration | Keep English: "migration 019" | |
| listener | bộ lắng nghe (listener) | | |
| route (HTTP) | route | Keep English | |
| control plane | mặt phẳng điều khiển | | |
| byte-range request | yêu cầu theo khoảng byte (byte-range) | | |
| functional requirement | yêu cầu chức năng | | |
| key architectural decision | quyết định kiến trúc then chốt | | |
| principal user flow | luồng người dùng chính | | |
| sequence (diagram) | sơ đồ tuần tự | | |
| reaction time | thời gian phản ứng | | |
| background load (idle) | tải nền | | |
| polling / poller | thăm dò định kỳ (polling) / bộ thăm dò | | |
| design review | bản đánh giá thiết kế | | |
| reverse geocoding | chuyển tọa độ thành địa chỉ (reverse geocoding) | | mã hóa địa lý ngược |
| metered billing / metered tier | tính phí theo mức sử dụng | | |
| static analyzer / analyzer | bộ phân tích tĩnh / bộ phân tích (analyzer) | | |
| atomic / mutual exclusion | nguyên tử / loại trừ tương hỗ | "thực hiện nguyên tử" | |
| open / fixed (finding) | chưa xử lý / đã khắc phục | | |
| race detector / race condition | bộ phát hiện tranh chấp dữ liệu (race detector) / tranh chấp thời điểm (race condition) | | |
| smoke test | kiểm thử nhanh (smoke test) | | |
| state machine | máy trạng thái | | |
| worker (parallel worker) | worker | Keep English: "8 worker" | |
| handler / content handler | bộ xử lý (handler) / bộ xử lý nội dung | First use with English | |
| event spine | trục sự kiện | First use "trục sự kiện (event spine)" | xương sống sự kiện, cột sống sự kiện |
| design principle | nguyên tắc thiết kế | | |
