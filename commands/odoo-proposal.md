---
name: odoo-proposal
description: |
  MUST be invoked when user asks to "soạn proposal", "tạo báo giá", "draft SOW", "commercial proposal", "technical proposal" from a signed-off Fit-Gap table.
  Converts a Fit-Gap table into draft Technical Proposal, Commercial Proposal/Quotation, and/or SOW documents following presales-proposal-sow-templates.md.
arguments:
  - name: fitgap_file
    description: "Đường dẫn tới file Fit-Gap table đã sign-off (mặc định: fit-gap-table.md trong thư mục hiện tại)"
    required: false
  - name: sections
    description: "Phần cần tạo: technical, commercial, sow, all (mặc định: all)"
    required: false
input_examples:
  - description: "Tạo đầy đủ Technical Proposal + Commercial Proposal + SOW từ fit-gap-table.md"
    arguments: {}
  - description: "Chỉ tạo Commercial Proposal (báo giá)"
    arguments:
      sections: "commercial"
  - description: "Tạo Proposal từ file Fit-Gap cụ thể của khách hàng"
    arguments:
      fitgap_file: "presales/acme-corp/fit-gap-table.md"
---

# /odoo-proposal Command

Soạn Proposal/SOW từ bảng Fit-Gap đã sign-off — đây là **Phase 3** của `agents/odoo-presales-consultant.md`.

## Execution Flow

### Step 1: Load input & context

1. Read `fitgap_file` (nếu không tồn tại, hỏi người dùng paste bảng Fit-Gap). Nếu không có dấu hiệu đã sign-off, nhắc người dùng đây vẫn là **draft** — Proposal chính thức nên dựa trên bảng đã được khách xác nhận.
2. Read `skills/presales-proposal-sow-templates.md` — templates cho Technical Proposal / Commercial Proposal / SOW / ROI / hồ sơ đấu thầu.
3. Read `skills/presales-effort-estimation-guide.md` — để điền/kiểm tra lại các ô Effort còn `TBD` trong Fit-Gap, và áp dụng buffer/risk contingency.
4. Read `skills/odoo-licensing-deployment-guide.md` — cho phần license & phương án triển khai trong Commercial Proposal.
5. Nếu Fit-Gap có dòng liên quan migration dữ liệu, read thêm `skills/presales-data-migration-scoping-guide.md`.
6. Nếu khách đang dùng/so sánh với hệ thống khác (Misa/SAP B1/Fast/Bravo...), read `skills/presales-competitor-comparison-guide.md` để chuẩn bị phần "Tại sao chọn Odoo".

### Step 2: Xác định phạm vi output

- `sections=all` (mặc định): tạo cả Technical Proposal + Commercial Proposal + SOW.
- `sections=technical` / `commercial` / `sow`: chỉ tạo phần tương ứng.

### Step 3: Soạn nội dung

Theo `presales-proposal-sow-templates.md`:

- **Technical Proposal**: Executive Summary, Pain Points (từ Discovery Notes nếu có), giải pháp theo từng khối nghiệp vụ (map App + Edition từ các dòng Fit-Gap ✅/🔧), danh sách Customization (từ các dòng 🛠️/🔌), roadmap theo phase.
- **Commercial Proposal/Quotation**: License (theo `odoo-licensing-deployment-guide.md`), Implementation cost (Effort × rate card từ `presales-effort-estimation-guide.md`), Training, Support/Maintenance, Hosting, optional items, payment terms (gợi ý mẫu 30/40/30 hoặc theo milestone).
- **SOW**: Deliverables theo phase, Timeline/Milestones, RACI, Assumptions, **Out of Scope** (lấy trực tiếp từ các dòng Fit-Gap ⏸️), Change Request process, Acceptance Criteria theo milestone, Warranty/Support terms.
- Nếu khách có số liệu so sánh trước/sau, thêm mục ROI "before vs after" — **CHỈ dùng số liệu khách đã cung cấp trong Discovery, không tự bịa**.

### Step 4: Output

Tạo file `proposal-draft.md` (hoặc tách thành `technical-proposal.md` / `commercial-proposal.md` / `sow.md` nếu người dùng yêu cầu).

## Bước tiếp theo

Sau khi Proposal/SOW được khách **ký**, dùng `skills/presales-to-implementation-handoff-guide.md` (Phase 5 của `agents/odoo-presales-consultant.md`) để chuyển sang `REQUIREMENT_SPEC.md` cho Dev team.

## AI Agent Instructions

1. **LOAD**: bảng Fit-Gap (đã sign-off) + `presales-proposal-sow-templates.md` + `presales-effort-estimation-guide.md` + `odoo-licensing-deployment-guide.md`
2. **SCOPE**: theo `sections` argument
3. **DRAFT**: nội dung theo templates — KHÔNG bịa số liệu/tính năng ngoài những gì đã thống nhất trong Fit-Gap
4. **OUTPUT**: `proposal-draft.md`
5. **REMIND**: bước tiếp theo là Handoff (`presales-to-implementation-handoff-guide.md`) sau khi khách ký
