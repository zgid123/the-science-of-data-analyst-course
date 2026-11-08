# Review 2 – group B (06-00 to 11-04), second native read after the rewrite

Date: 2026-11-05. Reviewer: a second agent, not the translator. Inputs: review.md, guide.md, lessons.md (T1–T6), merged
glossary (`glossary.py --lang vi --task milestone-1 show`), reader-test.md findings #57–#73, rewrite-B.md.

Coverage before the passes (`glossary.py … coverage --report reports/milestone-1/report`): 5 drifting concepts, report-wide –
AI interviewer, candidate technique family, programmed decision, enrolment, capacity. In this group every occurrence
already uses the glossary form or, for capacity and enrolment, the actor-phrased sentence the glossary's Usage asks for
(06-01, 06-02, 08-00, 09-00, 11-02, 11-04); the remaining drift lies in other groups' files.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 06-01 | 16 | 3.1 named actor | nhóm có thể thử hướng tiếp cận này | nhóm phân tích dữ liệu có thể thử hướng tiếp cận này |
| 2 | 06-01 | 17 | 3.6 meaning ("one possible source"; fit assessed later) | Một nguồn phù hợp là | Một nguồn có thể dùng là |
| 3 | 06-02 | 4 | 3.6 meaning (reason the English does not give; reader-test #59) | một vài học phần mà giảng viên đồng ý thiết lập trên LMS theo cùng một cách. Việc liên kết dữ liệu thường xuyên | một vài học phần có cách thiết lập trên LMS giống nhau. Liên kết dữ liệu định kỳ |
| 4 | 06-02 | 16 | 3.6 changed English (Table 6.2 row) | Nhóm sinh viên quá nhỏ: tỷ lệ dễ dao động và sinh viên dễ bị nhận ra \| AQ3 | Nhóm nhỏ cho tỷ lệ không ổn định và có thể làm lộ danh tính sinh viên \| Các phép so sánh giữa nhóm trong AQ2 và AQ3 |
| 5 | 06-02 | 23 | 3.6 changed English (rule 2) | coi sinh viên là người cùng tham gia vào hoạt động phân tích này | hỏi ý kiến sinh viên về cách sử dụng dữ liệu cá nhân |
| 6 | 07-00 | 22 | 3.5 head noun | nên cần những vấn đề lặp lại qua nhiều học kỳ | nên cần bằng chứng về vấn đề lặp lại qua nhiều học kỳ |
| 7 | 08-00 | 17 | 3.6 changed English ("the risk table (Table 6.2)") | mâu thuẫn với Bảng 6.2 | mâu thuẫn với bảng rủi ro dữ liệu (Bảng 6.2) |
| 8 | 08-00 | 22 | 3.6 meaning ("suitable goal"); 3.5 no empty "một" | ví dụ về một mục tiêu tốt | ví dụ về mục tiêu phù hợp |
| 9 | 11-01 | 11 | 3.3 plain word (cohort) | một khóa | một khóa sinh viên |
| 10 | 11-01 | 13 | 3.6 meaning ("which would you make differently") | anh/chị sẽ quyết định khác đi ở những điểm nào? | anh/chị sẽ đưa ra quyết định nào khác đi? |
| 11 | 11-01 | 14 | 3.6 hedge ("realistically") | anh/chị có thể điều chuyển | anh/chị thực sự có thể điều chuyển |
| 12 | 11-02 | 13 | 3.3 one term per concept (cohort, as 11-01) | mỗi năm xem khóa một lần | mỗi năm xem khóa sinh viên một lần |
| 13 | 11-02 | 41 | 3.6 meaning ("capacity constraint"); 3.1 one breath | Phòng hỗ trợ sinh viên chỉ liên hệ được ít sinh viên mỗi tuần (con số do persona, tức vai bên liên quan do AI đóng, đưa ra) | Giới hạn về số sinh viên phòng hỗ trợ sinh viên liên hệ được (con số do persona đưa ra; persona là vai bên liên quan do AI đóng) |
| 14 | 11-03 | 59 | 3.6 meaning (VDO4, same as #3) | một vài học phần mà giảng viên đồng ý thiết lập trên LMS theo cùng một cách | một vài học phần có cách thiết lập trên LMS giống nhau |
| 15 | 11-04 | 13 | 3.1 one breath; 3.4 clear share (lesson T2) | cứ 100 sinh viên có thêm năm sinh viên đạt học phần, nghĩa là trong 30 sinh viên không hoàn thành học phần, cứ sáu sinh viên thì giúp được một sinh viên đạt | cứ 100 sinh viên thì có thêm năm sinh viên đạt học phần, nghĩa là giúp được một phần sáu trong số 30 sinh viên không hoàn thành học phần |

Reader-test passages #57–#73 re-read with the English closed: all read at first sight after the rewrite; #59 was fixed
again (#3) because the rewrite added a lecturer-consent condition the English does not state. #62 keeps the bridging
sentence "Mỗi tên trong danh sách vì thế là một sinh viên mà trường phải liên hệ", which restates the English obligation.

Terms for the glossary to settle: "cohort" (khóa sinh viên, not a bare "khóa"); "consistent setup" of pilot courses
(học phần có cách thiết lập trên LMS giống nhau).

Per file (`check_parity.py --report reports/milestone-1/report --lang vi FILE`; then `translation_status.py --mark`, 11 recorded):

- 06-00: reviewed, 0 findings, parity 0 errors 0 warnings.
- 06-01: reviewed, 2 fixed, parity 0 errors 0 warnings.
- 06-02: reviewed, 3 fixed, parity 0 errors 0 warnings.
- 07-00: reviewed, 1 fixed, parity 0 errors 0 warnings.
- 08-00: reviewed, 2 fixed, parity 0 errors 0 warnings.
- 09-00: reviewed, 0 findings, parity 0 errors 0 warnings.
- 11-00: reviewed, 0 findings, parity 0 errors 0 warnings.
- 11-01: reviewed, 3 fixed, parity 0 errors 0 warnings.
- 11-02: reviewed, 2 fixed, parity 0 errors 0 warnings.
- 11-03: reviewed, 1 fixed, parity 0 errors 0 warnings.
- 11-04: reviewed, 1 fixed, parity 0 errors 0 warnings.
