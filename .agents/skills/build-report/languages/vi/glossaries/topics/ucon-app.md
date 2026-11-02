# Topic glossary: ucon-app, a UCON engine for a movie rental system

The vocabulary of one report: the technical report on the ucon-app, a UCONABC engine for a movie rental system. It fixes the report's title and chapter titles, the names of the system's components and mechanisms, the vocabulary of verification and measurement, and the labels of the design review. Model and architecture terms (kiểm soát sử dụng, phiên sử dụng, thu hồi, PDP, PEP, PIP, PAP, fail-closed, chế độ demo, phát hiện) come from the domain glossary `usage-control`. Component and file names in code (`ucond`, `usage_sessions`, `policy_revise`, `onA2_prepaid_minutes`), model labels (preA0, onB1), finding IDs (AC-01, UC-12), goal and requirement IDs (G1, FR5, C1) and product names (Gin, Next.js, PostgreSQL, TimescaleDB, CEL, Docker Compose, AuthzForce) stay as written.

## Title and chapters

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| UCON Engine for a Movie Rental System: Architecture and the Application of UCONABC | UCON Engine cho hệ thống thuê phim: kiến trúc và ứng dụng mô hình UCONABC | Report title (tasks.toml) | |
| Introduction / Requirements and Design Goals / System Architecture / Runtime Behaviour | Giới thiệu / Yêu cầu và mục tiêu thiết kế / Kiến trúc hệ thống / Hành vi khi vận hành | Chapter titles | |
| Implementation of UCONABC / Cross-Cutting Mechanisms | Hiện thực mô hình UCONABC / Các cơ chế xuyên suốt | Chapter titles | |
| Verification and Evaluation / Known Limitations / Conclusions and Future Work | Kiểm chứng và đánh giá / Các hạn chế đã biết / Kết luận và hướng phát triển | Chapter titles | |
| Reminder (theory note) | Nhắc lại | The italic label "*Reminder:*" becomes "*Nhắc lại:*" | |

## System and components

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| movie rental system | hệ thống thuê phim | | |
| usage control engine / engine | engine kiểm soát sử dụng / engine | Keep "engine", as Vietnamese engineers write it | bộ máy |
| enforcement service | dịch vụ thực thi | The PEP service (backend in Go) | |
| facade (engine facade) | lớp mặt tiền (facade) của engine | First use with English | |
| loader / reactor / scheduler / updater | bộ nạp chính sách (loader) / bộ phản ứng (reactor) / bộ lập lịch (scheduler) / bộ cập nhật (updater) | First use with English; the English name alone may follow | |
| deadline expression / deadline timer | biểu thức thời hạn / bộ hẹn giờ theo thời hạn | | |
| sweep (re-evaluation of many sessions) | lượt quét đánh giá lại | | |
| compensation (revoke phase) | cập nhật bù trừ | "giai đoạn revoke" | |
| demonstration panel | bảng điều khiển demo | | |
| demonstration account | tài khoản demo | | |
| licence (rental, subscription, offline download) | giấy phép (license) | "license" in identifiers stays | |
| rental / subscription / pay-per-view | thuê lẻ / gói thuê bao / trả tiền theo lượt xem | | |
| wallet | ví | | |
| prepaid quota | hạn mức trả trước | | |
| device limit | giới hạn số thiết bị | | |
| mid-roll advertisement | quảng cáo giữa phim | | |
| offline licence | giấy phép xem ngoại tuyến | | |
| curfew (time rule) | khung giờ cấm | | |

## Design, verification and review

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| local change / global change | thay đổi cục bộ / thay đổi toàn cục | | |

## Terms settled during translation (2026-10-22)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| handler / content handler | bộ xử lý (handler) / bộ xử lý nội dung | This report writes "bộ xử lý" where it first wrote "lớp xử lý" | lớp xử lý |
| SSE hub | bộ phân phối SSE (SSE hub) | | |
| trigger (what caused a re-evaluation) | tác nhân kích hoạt | The database object stays "trigger" | nguyên nhân kích hoạt |
| premium / basic (account, film) | cao cấp / cơ bản | The code values `premium`, `basic` stay in backticks | |
| qualification (of a result by a review finding) | điểm lưu ý | "điểm lưu ý UC-07" | điều kiện kèm theo |
| the group's draft report / knowledge base | bản thảo báo cáo của nhóm / cơ sở tri thức của nhóm | | |
| settlement (of played seconds) | quyết toán | | |
| playback segment | đoạn phát | | |
| re-evaluation trigger (component role) | bộ kích hoạt đánh giá lại | The component role; the cause of one re-evaluation is "tác nhân kích hoạt" | |
| viewing-hours rule (onC0) | quy tắc khung giờ xem | The curfew at 23:00 it enforces is "khung giờ cấm" | |
| pre-update / on-update / post-update | cập nhật trước khi sử dụng / cập nhật trong khi sử dụng / cập nhật sau khi sử dụng | Full forms in prose; the short forms "cập nhật trước/trong/sau" only in table cells and figure labels; "(pre-update)" may follow at first use | |
| dashboard (admin metrics page) | trang tổng quan | "bảng điều khiển demo" is the demo panel | |
| client (engine client, client library, browser client) | client | Keep English in this report: "thư viện client", "client của engine" | |
| versioning (of policies) | cơ chế quản lý phiên bản (versioning) | First use with English | |
| leader lock | khóa chọn engine chủ (leader lock) | | |
