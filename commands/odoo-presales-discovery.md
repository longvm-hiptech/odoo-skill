---
name: odoo-presales-discovery
description: |
  MUST be invoked when user asks to "khảo sát khách hàng", "discovery workshop", "bộ câu hỏi khảo sát Odoo", "presales discovery questionnaire".
  Generates a tailored Odoo presales discovery questionnaire, optionally focused on one industry blueprint, specific business blocks, and Vietnam-specific questions.
arguments:
  - name: industry
    description: "Ngành của khách hàng (vd: distribution, manufacturing, retail, construction, services, logistics) - dùng để load thêm blueprint phù hợp từ presales-industry-solution-templates.md"
    required: false
  - name: blocks
    description: "Các khối nghiệp vụ cần khảo sát, phân tách bằng dấu phẩy (vd: sales,purchase,inventory,accounting,hr,project). Mặc định: hỏi người dùng hoặc suy luận từ context"
    required: false
  - name: vietnam
    description: "true/false - khách có phải doanh nghiệp Việt Nam không (bổ sung câu hỏi về kế toán/hoá đơn điện tử/tích hợp VN)"
    required: false
input_examples:
  - description: "Khảo sát khách phân phối tại VN, chưa rõ khối nào ưu tiên"
    arguments:
      industry: "distribution"
      vietnam: "true"
  - description: "Khảo sát tổng quát, chưa biết ngành"
    arguments: {}
  - description: "Khảo sát riêng khối Kế toán + Kho cho khách sản xuất"
    arguments:
      industry: "manufacturing"
      blocks: "accounting,inventory"
---

# /odoo-presales-discovery Command

Sinh bộ câu hỏi khảo sát (Discovery Questionnaire) cho 1 buổi Discovery Workshop với khách hàng — đây là **Phase 1** của `agents/odoo-presales-consultant.md`.

## Execution Flow

### Step 1: Load context

1. Read `skills/presales-discovery-questionnaire.md` — bộ câu hỏi gốc:
   - Phần 1: hồ sơ chung (quy mô, hệ thống đang dùng, pain points)
   - Phần 2: câu hỏi theo từng khối nghiệp vụ
   - Phần 3: checklist Red Flags
   - Phần 4: template "Discovery Notes" output
2. Nếu có `industry` argument, read `skills/presales-industry-solution-templates.md` và lấy đúng phần ngành tương ứng (Combo Apps + Quy trình mẫu) — dùng để chuẩn bị thêm câu hỏi xác nhận "quy trình của anh/chị có giống mô tả này không, khác ở đâu?".
3. Nếu `vietnam=true` (hoặc rõ ràng khách là DN Việt Nam), read thêm:
   - `skills/l10n-vietnam-compliance-guide.md` — mục FAQ và hoá đơn điện tử
   - `skills/vietnam-integration-landscape.md` — mục "Bảng tổng hợp ưu tiên khảo sát"

### Step 2: Xác định scope khảo sát

- Nếu `blocks` được chỉ định, chỉ lấy các khối tương ứng từ Phần 2 của discovery questionnaire.
- Nếu không, hỏi người dùng 1 câu ngắn gọn về các khối khách quan tâm — hoặc tự suy luận nếu context đã đủ rõ (vd "khách bán buôn, cần Sales+Kho+Kế toán" → 3 khối).

### Step 3: Sinh bộ câu hỏi

Tổng hợp thành 1 bộ câu hỏi hoàn chỉnh:

1. **Phần 1** — Hồ sơ chung (luôn bao gồm đầy đủ)
2. **Phần 2** — Câu hỏi theo từng khối đã xác định ở Step 2
3. *(Nếu có industry)* — 3-5 câu hỏi xác nhận quy trình theo blueprint ngành tương ứng
4. *(Nếu vietnam=true)* — câu hỏi bổ sung về kế toán/hoá đơn điện tử/tích hợp VN
5. **Checklist Red Flags** (Phần 3) — để team note lại trong lúc khảo sát

### Step 4: Output

Tạo file `discovery-notes.md` (hoặc `presales/{ten-khach-hang}/discovery-notes.md` nếu đã biết tên khách) theo đúng template Phần 4 của `presales-discovery-questionnaire.md`, đã điền sẵn câu hỏi (phần trả lời để trống) — sẵn sàng dùng trực tiếp trong buổi workshop.

## Bước tiếp theo

Sau khi điền xong Discovery Notes từ buổi workshop, dùng `/odoo-fit-gap` để chuyển sang Phase 2 (Solution Mapping & Fit-Gap).

## AI Agent Instructions

1. **LOAD**: `skills/presales-discovery-questionnaire.md` (luôn) + `presales-industry-solution-templates.md` (nếu có `industry`) + nhóm Localization VN (nếu `vietnam=true`)
2. **SCOPE**: xác định các khối nghiệp vụ cần khảo sát (từ `blocks` hoặc hỏi 1 câu)
3. **GENERATE**: bộ câu hỏi tổng hợp theo Step 3
4. **OUTPUT**: file `discovery-notes.md` theo template chuẩn, sẵn sàng điền trong workshop
5. **REMIND**: bước tiếp theo là `/odoo-fit-gap`
