---
name: presales-fit-gap-analysis-guide
keywords: [presales, fit-gap, fit gap analysis, requirements, scoping, moscow, workshop]
description: Phương pháp luận và template chuẩn cho buổi Fit-Gap Workshop - tài liệu quan trọng nhất khách hàng nhận được trước khi báo giá. Là input trực tiếp cho Proposal/SOW và Handoff sang đội Dev.
odoo_versions: [all]
related_skills: [odoo-app-feature-matrix, presales-discovery-questionnaire, presales-effort-estimation-guide, presales-proposal-sow-templates, presales-to-implementation-handoff-guide]
---

# Fit-Gap Analysis Guide (PreSale)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  FIT-GAP ANALYSIS                                                             ║
║  Discovery Notes → Bảng Fit-Gap → Proposal/SOW + Handoff cho Dev              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Fit-Gap Analysis là tài liệu **bản lề** giữa giai đoạn khảo sát và giai đoạn báo giá/triển khai: với mỗi yêu cầu của khách, xác định Odoo **đáp ứng sẵn (Fit)**, **đáp ứng một phần qua cấu hình (Partial)**, hay **cần customize/tích hợp (Gap)** — và từ đó mới ước lượng được effort, chi phí, timeline.

---

## 1. Khi nào chạy Fit-Gap Workshop

- **Sau khi** đã có Discovery Notes (`presales-discovery-questionnaire.md`) và demo sơ bộ (`presales-demo-environment-guide.md`).
- **Trước khi** gửi Commercial Proposal/SOW chính thức.
- Thời lượng: thường 0.5–2 ngày tùy quy mô, chia theo từng khối nghiệp vụ (Sales, Kho, Kế toán, HR...).
- Người tham gia:
  - Phía khách: trưởng phòng/người dùng chính của từng khối (process owner) — **không chỉ** ban giám đốc, vì họ mới biết chi tiết quy trình.
  - Phía PreSale: Solution Consultant chủ trì + (nếu có) Technical Lead để đánh giá nhanh độ khó của các Gap kỹ thuật.

---

## 2. Quy trình thực hiện

### Bước 1 — Chuẩn bị
- Tổng hợp danh sách yêu cầu từ Discovery Notes thành các dòng riêng lẻ (1 yêu cầu = 1 dòng trong bảng Fit-Gap).
- Với mỗi yêu cầu, tra trước trong `odoo-app-feature-matrix.md` xem có Fit/Partial sẵn không — chuẩn bị sẵn câu trả lời "Odoo làm được như thế nào" để workshop đi nhanh.
- Đánh dấu trước các dòng nghi ngờ là Gap dựa trên checklist Red Flags (`presales-discovery-questionnaire.md` Phần 3).

### Bước 2 — Trong workshop
- Với mỗi yêu cầu: trình bày ngắn gọn cách Odoo xử lý theo chuẩn (demo trực tiếp nếu có thể) → hỏi khách "quy trình của anh/chị có khác điểm này không, khác như thế nào, mức độ bắt buộc?".
- Ghi nhận ngay vào bảng Fit-Gap (xem template Mục 4) — **không tranh luận giải pháp kỹ thuật tại chỗ**, chỉ ghi nhận Gap và mức độ ưu tiên.
- Với mỗi Gap, hỏi thêm: "Nếu Odoo không làm đúng y hệt cách cũ, anh/chị có sẵn sàng đổi quy trình theo chuẩn Odoo không?" — đây là lựa chọn **Process Change**, thường rẻ hơn nhiều so với Customize.

### Bước 3 — Sau workshop
- PreSale + Technical Lead review lại từng dòng Gap → quyết định hướng xử lý (Mục 5) và ước lượng effort sơ bộ (`presales-effort-estimation-guide.md`).
- Hoàn thiện bảng Fit-Gap → gửi lại cho khách để xác nhận (sign-off) trước khi đưa vào Proposal.

---

## 3. Tiêu chí phân loại

| Nhãn | Định nghĩa | Ví dụ |
|---|---|---|
| ✅ **Fit** | Odoo chuẩn (out-of-the-box) đáp ứng đúng nhu cầu, không cần cấu hình đặc biệt | "Tạo báo giá, gửi email cho khách" → Sales app chuẩn |
| 🔧 **Partial Fit (Configuration)** | Odoo đáp ứng được nhưng cần **cấu hình** (không phải code): tạo thêm field qua Studio, thiết lập workflow/automation rules, tùy biến view | "Thêm trường 'Mã số thuế NCC' trên form Purchase Order" → field tùy chỉnh đơn giản |
| 🛠️ **Gap (Customize)** | Cần **viết code** — module mới, custom model/field/report/logic | "Tính hoa hồng đại lý theo công thức bậc thang riêng" |
| 🔌 **Gap (3rd-party / Integration)** | Cần tích hợp hệ thống ngoài (có thể có connector sẵn hoặc phải build mới) | "Đồng bộ đơn hàng 2 chiều với Shopee" |
| 🔄 **Process Change** | Gap nhưng khách đồng ý **đổi quy trình** theo chuẩn Odoo thay vì customize | "Bỏ bước duyệt giấy, chuyển sang duyệt trên hệ thống" |
| ⏸️ **Out of Scope / Phase 2** | Ghi nhận nhưng không nằm trong phạm vi triển khai lần này | "Tích hợp AI dự báo nhu cầu" — để Phase 2 |

---

## 4. Template bảng Fit-Gap

| Mã | Yêu cầu | Khối | Ưu tiên (MoSCoW) | Đánh giá | Giải pháp đề xuất | Effort (man-day) | Ghi chú |
|---|---|---|---|---|---|---|---|
| FG-001 | Tạo báo giá, in PDF gửi khách | Sales | Must | ✅ Fit | Sales app chuẩn | 0 (config) | — |
| FG-002 | Báo giá > 50tr cần Giám đốc duyệt | Sales | Must | 🔧 Partial | Approval workflow + automation rule | 0.5 | `workflow-state-patterns.md` |
| FG-003 | Hoa hồng đại lý theo bậc thang doanh số lũy kế quý | Sales | Must | 🛠️ Gap-Custom | Module tính hoa hồng riêng | 5–8 | Cần làm rõ công thức |
| FG-004 | Đồng bộ đơn hàng 2 chiều với Shopee | Sales | Should | 🔌 Gap-Integration | Tích hợp Shopee Open API | 8–12 | `vietnam-integration-landscape.md` |
| FG-005 | Phiếu xuất kho cần in theo mẫu công ty (logo, layout riêng) | Kho | Must | 🔧 Partial | Custom QWeb report | 1–2 | `report-patterns.md` |
| FG-006 | Bỏ bước "duyệt phiếu xuất kho bằng giấy" | Kho | Could | 🔄 Process Change | Duyệt trên hệ thống qua Approvals | 0 | Cần thuyết phục khách |
| FG-007 | Xuất hóa đơn điện tử qua MISA meInvoice | Kế toán | Must | 🔌 Gap-Integration | Tích hợp e-invoice | 10–15 | `l10n-vietnam-compliance-guide.md` |
| FG-008 | Dự báo nhu cầu bằng AI | Kho | Won't (Phase 2) | ⏸️ Out of scope | — | — | Đưa vào roadmap Phase 2 |

> **Cột "Effort"**: chỉ điền số sơ bộ (range) ở giai đoạn này, lấy từ benchmark trong `presales-effort-estimation-guide.md`. Con số chính xác sẽ được Technical Lead xác nhận trước khi đưa vào Proposal.

---

## 5. Hướng xử lý từng loại Gap

Khi gặp 🛠️/🔌 Gap, cân nhắc theo thứ tự ưu tiên (từ rẻ → đắt):

1. **Process Change** — Khách đổi quy trình theo chuẩn Odoo. Luôn hỏi lựa chọn này trước.
2. **Configuration nâng cao** — Dùng Studio (Enterprise), Automation Rules, Server Actions để giải quyết mà không cần code mới (nếu khách có Enterprise).
3. **Module có sẵn (OCA/Marketplace)** — Kiểm tra OCA (`https://github.com/OCA`) hoặc Odoo Apps Store trước khi quyết định code mới.
4. **Customize (code mới)** — Module riêng, theo `agents/odoo-planner.md` xử lý ở giai đoạn triển khai.
5. **Tích hợp 3rd-party** — Xác định bên thứ 3 đã có connector/API hay chưa (`vietnam-integration-landscape.md` cho các tích hợp phổ biến tại VN).
6. **Phase 2 / Out of scope** — Khi effort quá lớn so với giá trị, hoặc chưa cấp thiết — ghi rõ vào Proposal phần "Out of scope" để tránh hiểu nhầm scope creep sau này.

---

## 6. Ưu tiên hóa (MoSCoW)

| Mức | Ý nghĩa | Tác động đến Proposal |
|---|---|---|
| **Must have** | Bắt buộc phải có để go-live, thiếu thì không dùng được | Luôn nằm trong Phase 1 / scope chính |
| **Should have** | Quan trọng nhưng có thể go-live mà chưa cần | Có thể đưa vào Phase 1 nếu effort thấp, hoặc Phase 1.5 |
| **Could have** | "Nice to have", giá trị thấp hơn | Thường đưa vào Phase 2, hoặc bỏ nếu effort cao |
| **Won't have (this phase)** | Đã thống nhất KHÔNG làm ở phase này | Ghi rõ vào "Out of scope" trong SOW để tránh tranh chấp |

---

## 7. Output & bước tiếp theo

Bảng Fit-Gap hoàn chỉnh (đã sign-off với khách) là input trực tiếp cho:

- **`presales-effort-estimation-guide.md`** — quy đổi từng dòng Gap thành effort/chi phí
- **`presales-proposal-sow-templates.md`** — phần "Giải pháp đề xuất" và "Out of scope" của Proposal/SOW lấy thẳng từ bảng này
- **`presales-to-implementation-handoff-guide.md`** — khi deal chốt, mỗi dòng 🛠️/🔧 Gap trong bảng Fit-Gap được map sang 1 mục trong `REQUIREMENT_SPEC.md` cho `agents/odoo-planner.md`

---

## Liên kết

- Tra cứu Apps/tính năng chuẩn: `skills/odoo-app-feature-matrix.md`
- Nguồn input: `skills/presales-discovery-questionnaire.md`
- Bước kế tiếp: `skills/presales-effort-estimation-guide.md`, `skills/presales-proposal-sow-templates.md`
- Bàn giao Dev: `skills/presales-to-implementation-handoff-guide.md`
