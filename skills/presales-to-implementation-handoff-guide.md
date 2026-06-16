---
name: presales-to-implementation-handoff-guide
keywords: [presales, handoff, ban giao, requirement spec, kickoff, odoo-planner, du an]
description: Hướng dẫn chuyển hoá Fit-Gap + Proposal/SOW đã ký thành REQUIREMENT_SPEC.md chuẩn cho agents/odoo-planner.md, đảm bảo không thất thoát thông tin giữa đội PreSale và đội triển khai
odoo_versions: [all]
related_skills: [presales-fit-gap-analysis-guide, presales-proposal-sow-templates, presales-effort-estimation-guide]
---

# Presales-to-Implementation Handoff Guide

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  HANDOFF GUIDE                                                                ║
║  Fit-Gap (sign-off) + Proposal/SOW (đã ký) → REQUIREMENT_SPEC.md → odoo-planner ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Đây là tài liệu **bản lề cuối cùng** giữa giai đoạn PreSale và giai đoạn triển khai: khi deal đã chốt (hợp đồng ký), mọi cam kết trong Fit-Gap/Proposal/SOW phải được "dịch" sang `REQUIREMENT_SPEC.md` — định dạng đầu vào chuẩn mà `agents/odoo-planner.md` dùng để tạo `PLAN.md` và bắt đầu code. Thiếu bước này, đội Dev sẽ phải tự đọc lại toàn bộ Proposal/SOW (vốn viết bằng ngôn ngữ kinh doanh) và tự suy diễn ra spec kỹ thuật — rủi ro hiểu sai rất cao.

---

## 1. Tại sao cần Handoff Guide

Vấn đề thường gặp khi không có quy trình bàn giao chuẩn:

- **PreSale "hứa" 1 cách**: viết trong Technical Proposal/SOW bằng ngôn ngữ kinh doanh — "hệ thống sẽ tự động tính hoa hồng đại lý theo doanh số luỹ kế quý".
- **Dev "hiểu" theo cách khác**: đọc câu trên, tự chọn cách implement (vd: field tính tay, hoặc cron chạy hàng ngày, hoặc compute field on-the-fly) — mỗi cách cho ra hành vi khác nhau (thời điểm cập nhật số liệu, hiệu năng, khả năng truy vết lịch sử).
- **Khách "nhận" ra sự khác biệt khi UAT**: số hoa hồng hiển thị không đúng như khách hình dung lúc ký Proposal → phát sinh tranh cãi "đây có phải lỗi không hay là yêu cầu mới?" → Change Request hoặc tệ hơn là tranh chấp hợp đồng.

**Gốc rễ**: thông tin bị "tam sao thất bản" qua nhiều lần truyền miệng/đọc tài liệu khác định dạng, không ai chịu trách nhiệm "dịch" đầy đủ và có cấu trúc.

Handoff Guide giải quyết vấn đề này bằng cách đảm bảo:

- Mọi cam kết trong Proposal/SOW đã ký đều được **dịch đầy đủ** sang `REQUIREMENT_SPEC.md` — không bỏ sót dòng Fit-Gap nào.
- Việc dịch tuân theo **bảng mapping rõ ràng** (Mục 3) — không phụ thuộc vào cách hiểu cá nhân của người dịch.
- Có **buổi Handoff Meeting** (Mục 6) để Technical Lead phản biện/làm rõ trước khi Dev bắt đầu code — tránh việc PLAN.md được tạo dựa trên giả định sai.
- PreSale **không biến mất** sau khi ký hợp đồng (Mục 7) — vẫn là nguồn tham chiếu khi Dev cần hiểu "tại sao".

---

## 2. Input cho Handoff

Trước khi bắt đầu dịch sang `REQUIREMENT_SPEC.md`, phải có đủ 3 input sau — thiếu bất kỳ input nào, **dừng lại** và yêu cầu PreSale bổ sung trước khi Dev bắt đầu:

| # | Input | Nguồn | Vai trò trong Handoff |
|---|---|---|---|
| 1 | **Bảng Fit-Gap đã sign-off** | `presales-fit-gap-analysis-guide.md` (Mục 4 — bảng FG-001...FG-0xx) | Nguồn chính cho Mục 3 — mỗi dòng Fit-Gap map sang 1 phần của REQUIREMENT_SPEC.md |
| 2 | **Proposal/SOW đã ký**, đặc biệt phần Scope, Deliverables, Out of Scope, Assumptions | `presales-proposal-sow-templates.md` (Technical Proposal Mục 5, SOW Mục 1/4/5) | Xác nhận lại ranh giới scope chính thức (có giá trị pháp lý) — nếu có khác biệt với bảng Fit-Gap gốc (vd khách thương lượng bớt 1 hạng mục), **SOW là bản cuối cùng có hiệu lực** |
| 3 | **Discovery Notes gốc** | `presales-discovery-questionnaire.md` | Giúp Dev hiểu **"tại sao"** — bối cảnh nghiệp vụ, pain point gốc — không chỉ "làm gì". Nếu thiếu phần này, Dev dễ implement đúng "chữ" của spec nhưng sai "tinh thần" (vd: làm đúng công thức nhưng UX không phù hợp với cách đại lý thực tế thao tác) |

> ⚠️ **Nguyên tắc**: nếu Fit-Gap và SOW có mâu thuẫn (vd Fit-Gap ghi 1 hạng mục là Must-have nhưng SOW final lại đưa vào Out of Scope do thương lượng giá), **SOW đã ký luôn thắng** — vì đây là văn bản ràng buộc pháp lý (xem `presales-proposal-sow-templates.md` Mục 4). Người dịch REQUIREMENT_SPEC.md phải đối chiếu cả 2 và ghi chú rõ trường hợp lệch này trong buổi Handoff Meeting (Mục 6).

---

## 3. Mapping Bảng Fit-Gap → REQUIREMENT_SPEC.md

Đây là phần **CỐT LÕI** của tài liệu này. Mỗi dòng trong bảng Fit-Gap (đã sign-off) được map sang đúng 1 vị trí trong `REQUIREMENT_SPEC.md` theo bảng dưới đây — **không có ngoại lệ, không có dòng "bỏ qua vì nghĩ không quan trọng"**.

| Loại dòng Fit-Gap | Map sang phần nào trong REQUIREMENT_SPEC.md | Ghi chú |
|---|---|---|
| ✅ **Fit** | **Không** cần đưa vào REQUIREMENT_SPEC.md (Odoo chuẩn — Dev không cần làm gì thêm) | Có thể ghi chú trong `## Business Context` hoặc `Assumptions` để Dev biết rõ là **đã xác nhận** không cần touch phần này — tránh Dev mất thời gian "double check" lại những gì PreSale đã demo |
| 🔧 **Partial Fit (Configuration)** | Mục mới **`## Configuration Notes`** (bổ sung vào REQUIREMENT_SPEC.md ngoài 6 mục chuẩn) — liệt kê các cấu hình/Studio field/automation rule cần làm, KHÔNG phải code | Dev cần biết để **verify đã cấu hình đúng** khi UAT — nếu Dev không biết hạng mục này tồn tại, có thể bỏ sót khi review trước UAT và khách phát hiện thiếu |
| 🛠️ **Gap (Customize)** | `## Models`, `## Fields per Model`, `## Workflows` — mỗi dòng Gap-Custom trở thành 1 hoặc nhiều model/field/workflow cụ thể | Đây là phần Dev sẽ **code nhiều nhất** — cần dịch chi tiết nhất (xem ví dụ FG-003 ở Mục 4) |
| 🔌 **Gap (3rd-party/Integration)** | `## Reports / Views` (nếu chỉ là export/báo cáo) hoặc mục mới **`## Integrations`** (nếu là kết nối 2 chiều với hệ thống ngoài) — ghi rõ endpoint, format dữ liệu, tần suất đồng bộ, xác thực (auth) | Cross-ref `vietnam-integration-landscape.md` nếu là tích hợp đặc thù VN (e-invoice, Zalo, sàn TMĐT, ngân hàng...) |
| 🔄 **Process Change** | Ghi vào `Assumptions` (trong `## Business Context` hoặc mục riêng) — đây là thay đổi quy trình khách **đã đồng ý** | Dev không code gì cho mục này, nhưng cần biết để khi training/hướng dẫn user, Dev không vô tình hướng dẫn theo quy trình cũ |
| ⏸️ **Out of Scope/Phase 2** | Mục mới **`## Out of Scope`** (mirror từ SOW Mục 5) — liệt kê RÕ ràng | **Quan trọng nhất để kiểm soát scope creep**: Dev KHÔNG được tự ý "tiện làm luôn" các hạng mục này dù có vẻ liên quan/dễ làm ("gold-plating") — mọi yêu cầu thêm phải qua Change Request (xem Mục 7) |

### Quy tắc bổ sung khi dịch

1. **1 dòng Fit-Gap có thể map sang nhiều phần** — vd FG-003 (🛠️ Gap-Custom) vừa cần 1 model mới (`## Models`), vừa cần field mới trên model có sẵn (`## Fields per Model`), vừa cần 1 workflow tính toán (`## Workflows`).
2. **Giữ mã Fit-Gap (FG-xxx) trong REQUIREMENT_SPEC.md** — ghi vào cột "Notes"/"Ghi chú" của từng bảng để có thể truy vết ngược lại Proposal/SOW khi cần (vd khi giải quyết tranh chấp scope).
3. **Không thêm mới hạng mục nào không có trong Fit-Gap/SOW** — nếu Technical Lead phát hiện thiếu sót khi dịch (vd 1 model cần thêm field phụ trợ để implement đúng), ghi rõ đây là **bổ sung kỹ thuật** (technical necessity) trong buổi Handoff Meeting để cả 2 bên cùng biết, không lặng lẽ thêm vào.

---

## 4. REQUIREMENT_SPEC.md — Template đầy đủ + Ví dụ điền

### 4.1. Template gốc (từ `SKILL.md` — KHÔNG được thay đổi cấu trúc 6 mục chuẩn)

Đây là cấu trúc chính xác mà `agents/odoo-planner.md` mong đợi nhận được. Khi dịch từ Fit-Gap, **giữ nguyên 6 heading `##` này** (Module, Models, Fields per Model, Workflows, Security, Reports / Views) — đây là "hợp đồng" (contract) giữa PreSale và Dev team:

```markdown
# Requirement Specification

## Module
- **Name**: {technical_name}
- **Description**: {purpose}

## Models
| Model | Inherits | Description |
|-------|----------|-------------|
| model.name | res.partner | Business object |

## Fields per Model
### model.name
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| name | Char | Yes | Display name |
| partner_id | Many2one(res.partner) | Yes | Link to partner |
| state | Selection | No | Workflow state |
| total | Float(compute) | No | Sum of lines |

## Workflows
- model.name: draft → confirm → approve → done

## Security
- group_user: read/create/write own
- group_manager: full access

## Reports / Views
- List view of model.name
- Form view with chatter
- PDF report
```

### 4.2. Mục mở rộng dành riêng cho input từ PreSale

3 mục dưới đây **KHÔNG có trong template gốc của odoo-planner**, nhưng PHẢI thêm vào cuối `REQUIREMENT_SPEC.md` khi handoff — vì đây là context PreSale nắm giữ mà nếu không ghi lại, sẽ mất hoàn toàn khi sang tay Dev:

```markdown
## Business Context

{Tóm tắt ngắn gọn (3-5 câu) TẠI SAO khách cần module/tính năng này — lấy từ
Discovery Notes. Mục đích: giúp Dev hiểu MỤC ĐÍCH thay vì chỉ làm theo spec
máy móc — khi gặp tình huống spec không cover hết (edge case), Dev có thể
tự quyết định hướng xử lý phù hợp với "tinh thần" của yêu cầu.}

**Assumptions (từ Fit-Gap 🔄 Process Change + SOW Mục 4):**
- {Quy trình đã thay đổi mà khách đồng ý — Dev cần biết để không hướng dẫn
  user theo quy trình cũ}
- {Giả định khác về dữ liệu/môi trường ảnh hưởng đến cách implement}

## Out of Scope

{Mirror TRỰC TIẾP từ SOW Mục 5 + các dòng ⏸️ trong Fit-Gap. Liệt kê RÕ để
Dev KHÔNG tự ý làm thêm ("gold-plating") — mọi mở rộng phải qua Change
Request.}

| Mã (Fit-Gap) | Hạng mục | Lý do |
|---|---|---|
| FG-0xx | {Tên hạng mục} | {Để Phase 2 / chưa cấp thiết / ...} |

## Configuration Notes

{Từ Fit-Gap 🔧 Partial Fit (Configuration). Liệt kê các cấu hình/Studio
field/automation rule cần làm — KHÔNG phải code, nhưng Dev cần biết để
verify đã cấu hình đúng khi UAT.}

| Mã (Fit-Gap) | Cấu hình cần làm | Module/App liên quan |
|---|---|---|
| FG-0xx | {Mô tả cấu hình} | {App} |
```

> **Vị trí trong file**: 3 mục mở rộng này đặt **sau** `## Reports / Views` (mục cuối cùng của template gốc), theo thứ tự: `## Business Context` → `## Out of Scope` → `## Configuration Notes`. `agents/odoo-planner.md` sẽ đọc 6 mục chuẩn để lập Component Map/Task List như bình thường, đồng thời tham khảo 3 mục mở rộng này khi cần hiểu context hoặc khi Technical Lead review PLAN.md.

### 4.3. Ví dụ điền cụ thể — dòng FG-003

Lấy nguyên dòng FG-003 từ `presales-fit-gap-analysis-guide.md`:

> | FG-003 | Hoa hồng đại lý theo bậc thang doanh số lũy kế quý | Sales | Must | 🛠️ Gap-Custom | Module tính hoa hồng riêng | 5–8 | Cần làm rõ công thức |

Áp dụng bảng mapping Mục 3 (🛠️ Gap-Custom → `## Models` + `## Fields per Model` + `## Workflows`), ví dụ bản dịch (rút gọn, chỉ minh hoạ nguyên tắc — KHÔNG phải spec đầy đủ):

```markdown
## Models
| Model | Inherits | Description |
|-------|----------|-------------|
| agent.commission.tier | (mới) | Bậc thang hoa hồng theo doanh số lũy kế quý — mỗi record là 1 bậc (vd 0-100tr: 1%, 100-300tr: 1.5%, >300tr: 2%) |
| agent.commission.report | (mới) | Bảng tổng hợp hoa hồng đã tính cho từng đại lý theo từng quý — lưu lịch sử để truy xuất, không tính lại mỗi lần xem |

## Fields per Model

### agent.commission.tier
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| name | Char | Yes | Tên bậc, vd "Bậc 1: 0-100tr" |
| amount_from | Monetary | Yes | Mốc doanh số bắt đầu áp dụng bậc này |
| amount_to | Monetary | No | Mốc kết thúc (để trống = không giới hạn trên) |
| commission_percent | Float | Yes | % hoa hồng áp dụng cho phần doanh số trong khoảng [amount_from, amount_to) |
| company_id | Many2one(res.company) | Yes | Multi-company — FG-003 không nêu rõ, cần hỏi lại trong Handoff Meeting (Mục 6) |

### res.partner (kế thừa — _inherit)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| is_commission_agent | Boolean | No | Đánh dấu đại lý thuộc diện tính hoa hồng — cần để lọc khi cron chạy |
| commission_tier_set_id | Many2one(agent.commission.tier.set) | No | (nếu có nhiều bộ bậc thang khác nhau cho từng nhóm đại lý — cần làm rõ trong Handoff Meeting có cần hay 1 bộ bậc thang dùng chung cho tất cả) |

### agent.commission.report
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| partner_id | Many2one(res.partner) | Yes | Đại lý được tính hoa hồng |
| period_start / period_end | Date | Yes | Khoảng thời gian quý áp dụng |
| total_revenue | Monetary(compute, store=True) | No | Doanh số lũy kế quý — tổng `amount_total` của `sale.order` đã confirm trong kỳ |
| commission_amount | Monetary(compute, store=True) | No | Số tiền hoa hồng tính theo bậc thang áp dụng trên `total_revenue` |
| state | Selection | No | draft → confirmed → paid |

## Workflows
- agent.commission.report: draft → confirmed → paid
  - **draft**: cron hàng quý (Scheduled Action) tự động tạo record `agent.commission.report` cho mỗi đại lý `is_commission_agent = True`, tính `total_revenue` và `commission_amount` theo bậc thang trong `agent.commission.tier`
  - **confirmed**: Kế toán/Sales Manager review số liệu, xác nhận đúng → khoá `total_revenue`/`commission_amount` (không tự tính lại)
  - **paid**: đánh dấu đã chi trả hoa hồng (thủ công, hoặc link sang phiếu chi/hoá đơn — **cần làm rõ**: FG-003 ghi "Cần làm rõ công thức", trong Handoff Meeting cần hỏi thêm có cần tự động tạo bút toán kế toán không hay chỉ dừng ở mức "đánh dấu đã trả")

## Security
- group_sales_user: xem được report hoa hồng của chính mình (nếu đại lý có user login) — **cần làm rõ**: đại lý có phải là user trong hệ thống không, hay chỉ là `res.partner` thuần và Sales Admin xem hộ?
- group_sales_manager: full access agent.commission.tier + agent.commission.report (tạo/sửa bậc thang, confirm/pay report)

## Reports / Views
- List + Form view: agent.commission.tier (cấu hình bậc thang)
- List + Form view: agent.commission.report (xem/confirm/pay từng kỳ)
- PDF report: "Bảng kê hoa hồng đại lý theo quý" (gửi cho đại lý)
```

```markdown
## Business Context

Khách hàng (công ty phân phối) hiện tính hoa hồng đại lý thủ công trên Excel
cuối mỗi quý — mất nhiều thời gian, dễ sai sót khi đại lý nằm ở nhiều bậc
doanh số khác nhau trong cùng 1 quý (tính lũy kế). Mục tiêu: tự động hoá
hoàn toàn việc tính toán, đảm bảo minh bạch (đại lý có thể tự xem báo cáo
hoa hồng của mình), giảm tranh cãi giữa đại lý và phòng kế toán.

**Assumptions:**
- Công thức bậc thang áp dụng theo **doanh số lũy kế của TỪNG quý riêng biệt**
  (không cộng dồn qua các quý) — *giả định này cần Technical Lead xác nhận lại
  với khách trong Handoff Meeting, vì FG-003 ghi "Cần làm rõ công thức"*.
- Doanh số tính trên `sale.order` ở trạng thái `state = 'sale'` (đã confirm),
  không tính `quotation`/`draft`.

## Out of Scope
| Mã (Fit-Gap) | Hạng mục | Lý do |
|---|---|---|
| FG-008 | Dự báo nhu cầu bằng AI | Phase 2 — không liên quan trực tiếp FG-003 nhưng nằm chung Sprint Sales, ghi để Dev không nhầm lẫn phạm vi |

## Configuration Notes
*(Không có Configuration Notes nào liên quan trực tiếp đến FG-003 — phần này
chỉ áp dụng nếu cùng đợt handoff có các dòng 🔧 Partial Fit khác trong khối Sales)*
```

> **Lưu ý**: ví dụ trên chỉ minh hoạ **nguyên tắc mapping** (1 dòng Fit-Gap "Hoa hồng đại lý theo bậc thang..." → 3 model + fields cụ thể + 1 workflow cron/computed field), không phải spec hoàn chỉnh để code ngay. Các điểm đánh dấu "**cần làm rõ**" PHẢI được giải quyết trong buổi Handoff Meeting (Mục 6) trước khi `agents/odoo-planner.md` tạo `PLAN.md` — nếu không, Technical Verification (Phase 2.2 của `agents/odoo-planner.md`) sẽ phải tự đoán và có thể đoán sai.

---

## 5. Checklist bàn giao

| Hạng mục | Ai chuẩn bị | Ai sign-off / lưu trữ |
|---|---|---|
| Bảng Fit-Gap đã sign-off | PreSale (Solution Consultant) | Khách (process owner từng khối) + Technical Lead |
| Proposal/SOW đã ký (bản scan/PDF hợp đồng) | PreSale | Lưu trữ tại PreSale, bản copy gửi PM dự án |
| Discovery Notes gốc | PreSale | Bàn giao cho Technical Lead (không cần sign-off riêng, đính kèm cùng bộ hồ sơ) |
| `REQUIREMENT_SPEC.md` (theo Mục 4) | PreSale + Technical Lead **cùng hoàn thiện** | Technical Lead xác nhận "đủ để bắt đầu PLAN.md" |
| Danh sách license/edition đã chốt (Community/Enterprise, số user) | PreSale | Link `odoo-licensing-deployment-guide.md` — Technical Lead xác nhận môi trường dev khớp với edition đã bán |
| Thông tin môi trường (database demo đã dùng, hosting đã chọn) | PreSale | Link `odoo-licensing-deployment-guide.md` — IT/Technical Lead xác nhận access |
| Đầu mối liên hệ phía khách cho từng khối nghiệp vụ (process owner) | PreSale | PM dự án lưu vào danh bạ dự án — để Dev liên hệ trực tiếp khi cần làm rõ |

> Nếu bất kỳ hạng mục nào trong checklist trên **chưa sẵn sàng**, buổi Handoff Meeting (Mục 6) nên **dời lại** — bắt đầu Handoff Meeting khi thiếu input chỉ tạo thêm 1 vòng làm rõ nữa, lãng phí thời gian của cả 2 đội.

---

## 6. Mẫu Agenda "Handoff Meeting" PreSale ↔ Dev (60-90 phút)

| Thời gian | Nội dung | Người chủ trì |
|---|---|---|
| 0–10p | **Tổng quan dự án** — bối cảnh khách hàng, lý do chọn Odoo, mục tiêu kinh doanh (`## Business Context`) | PreSale (Solution Consultant) |
| 10–30p | **Đi qua từng dòng Fit-Gap 🛠️/🔌/🔧** — PreSale giải thích ý nghĩa nghiệp vụ của từng dòng, Technical Lead hỏi làm rõ (đặc biệt các dòng có ghi "Cần làm rõ..." trong cột Ghi chú), ghi nhận câu hỏi mở | PreSale trình bày, Technical Lead hỏi |
| 30–50p | **Review `REQUIREMENT_SPEC.md` draft** — Technical Lead phản hồi tính khả thi của từng model/field/workflow đã dịch, ước lượng lại effort nếu cần (so với effort ban đầu trong Fit-Gap/`presales-effort-estimation-guide.md`) | Technical Lead |
| 50–65p | **Review `## Out of Scope` & `Assumptions`** — đảm bảo Dev hiểu rõ ranh giới, không có hạng mục nào bị hiểu nhầm là "trong phạm vi" | PreSale + Technical Lead |
| 65–80p | **Timeline/Milestones từ SOW** — đối chiếu với kế hoạch sprint của Dev team, xác nhận mốc UAT/go-live khả thi | PM dự án |
| 80–90p | **Phân công đầu mối liên hệ**, thống nhất kênh trao đổi (Slack/email/...), bước tiếp theo: `agents/odoo-planner.md` tạo `PLAN.md` dựa trên `REQUIREMENT_SPEC.md` đã chốt | PM dự án |

**Đầu ra của buổi Handoff Meeting**:
- `REQUIREMENT_SPEC.md` phiên bản **final** (mọi điểm "cần làm rõ" đã được giải quyết và cập nhật vào file).
- Danh sách câu hỏi mở (nếu còn) — kèm người chịu trách nhiệm trả lời và deadline.
- Xác nhận Technical Lead **sẵn sàng** giao cho `agents/odoo-planner.md` bắt đầu Phase 1 (Gather Context) của quy trình lập `PLAN.md`.

---

## 7. Vai trò của PreSale sau Handoff

PreSale **KHÔNG "biến mất" hoàn toàn** sau buổi Handoff Meeting:

- **Vẫn là đầu mối quan hệ khách hàng** — đặc biệt với các stakeholder cấp cao (Ban Giám đốc, CFO) mà Dev team thường không tiếp xúc trực tiếp.
- **Tham gia UAT review** — PreSale có context "đã hứa gì với khách" nên có thể nhận ra sớm khi 1 tính năng đang implement đi lệch khỏi kỳ vọng ban đầu (trước khi khách phát hiện).
- **Hỗ trợ giải thích lại bối cảnh kinh doanh** khi Dev có câu hỏi phát sinh ngoài `## Business Context` đã ghi — đặc biệt với các yêu cầu phức tạp như FG-003 (công thức hoa hồng) nơi nhiều chi tiết chỉ tồn tại trong trí nhớ của người tham gia Discovery/Fit-Gap workshop.
- **Theo dõi Change Request** — nếu phát sinh yêu cầu mới ngoài `REQUIREMENT_SPEC.md` (đặc biệt là yêu cầu chạm vào `## Out of Scope`), PreSale **tham gia đánh giá** xem yêu cầu này có thực sự nằm trong "Out of Scope" đã thống nhất hay không, theo đúng Quy trình Change Request (`presales-proposal-sow-templates.md` SOW Mục 6) — **tránh để Dev tự quyết định mở rộng phạm vi** một mình, vì Dev không có đủ context về điều khoản hợp đồng/giá đã thương lượng.

---

## Liên kết

- Nguồn bảng Fit-Gap: `presales-fit-gap-analysis-guide.md`
- Nguồn Proposal/SOW đã ký (Scope, Out of Scope, Assumptions, Deliverables): `presales-proposal-sow-templates.md`
- Đối chiếu lại effort khi review REQUIREMENT_SPEC.md trong Handoff Meeting: `presales-effort-estimation-guide.md`
- Template `REQUIREMENT_SPEC.md` gốc + quy trình Phase 1 (Parse Requirements): root `SKILL.md`
- Bên nhận bàn giao, tạo `PLAN.md` từ `REQUIREMENT_SPEC.md`: `agents/odoo-planner.md`
- Thông tin license/edition/môi trường cần xác nhận trong checklist bàn giao: `odoo-licensing-deployment-guide.md`
- Tích hợp đặc thù VN (nếu Fit-Gap có dòng 🔌 liên quan e-invoice/Zalo/sàn TMĐT): `vietnam-integration-landscape.md`
