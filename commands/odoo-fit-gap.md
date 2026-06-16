---
name: odoo-fit-gap
description: |
  MUST be invoked when user asks to "tạo bảng fit-gap", "fit-gap analysis", "phân tích fit gap", "đánh giá fit gap" from Discovery Notes hoặc danh sách yêu cầu khách hàng.
  Converts Discovery Notes into a structured Fit-Gap table following presales-fit-gap-analysis-guide.md format and classification (Fit / Partial Fit / Gap-Custom / Gap-Integration / Process Change / Out of scope).
arguments:
  - name: discovery_file
    description: "Đường dẫn tới file Discovery Notes (mặc định: discovery-notes.md trong thư mục hiện tại, hoặc presales/{khách}/discovery-notes.md)"
    required: false
input_examples:
  - description: "Tạo Fit-Gap từ discovery-notes.md mặc định"
    arguments: {}
  - description: "Tạo Fit-Gap từ file khảo sát cụ thể"
    arguments:
      discovery_file: "presales/acme-corp/discovery-notes.md"
---

# /odoo-fit-gap Command

Chuyển Discovery Notes thành bảng Fit-Gap chuẩn — đây là **Phase 2** của `agents/odoo-presales-consultant.md`.

## Execution Flow

### Step 1: Load input & context

1. Read `discovery_file` (nếu không tồn tại, hỏi người dùng paste nội dung Discovery Notes hoặc danh sách yêu cầu trực tiếp).
2. Read `skills/odoo-app-feature-matrix.md` — đặc biệt mục "Mapping ngược: Khách nói X → Odoo App nào?".
3. Read `skills/presales-fit-gap-analysis-guide.md` — format bảng Fit-Gap, 6 nhãn phân loại, và thứ tự xử lý Gap.

### Step 2: Phân tích từng yêu cầu

Với mỗi yêu cầu trong Discovery Notes (mỗi yêu cầu = 1 dòng trong bảng kết quả):

1. Tra `odoo-app-feature-matrix.md` để xác định Odoo App/Edition (Community/Enterprise) đáp ứng.
2. Phân loại theo 6 nhãn chuẩn:
   - ✅ Fit · 🔧 Partial Fit (Configuration) · 🛠️ Gap (Customize) · 🔌 Gap (3rd-party/Integration) · 🔄 Process Change · ⏸️ Out of Scope/Phase 2
3. Nếu là 🔌 Gap-Integration và liên quan VN (hoá đơn điện tử, ngân hàng, vận chuyển, thanh toán, social commerce), tra `skills/vietnam-integration-landscape.md` để biết mức độ sẵn có/độ phức tạp tham khảo trước khi xếp loại.
4. Với mỗi Gap, áp dụng thứ tự ưu tiên xử lý ở `presales-fit-gap-analysis-guide.md` mục 5 (Process Change → Configuration nâng cao/Studio → OCA module → Customize → Tích hợp 3rd-party → Phase 2) để đề xuất cột "Giải pháp đề xuất".
5. Gán mã `FG-XXX` tăng dần. Gán Ưu tiên (MoSCoW) — nếu Discovery Notes chưa nêu rõ, đặt `TBD` và nhắc xác nhận với khách sau.
6. Cột "Effort (man-day)" — nếu có thể tra nhanh benchmark từ `skills/presales-effort-estimation-guide.md` thì điền sơ bộ (range), nếu không để `TBD` (sẽ chốt ở `/odoo-proposal`).

### Step 3: Output

Tạo file `fit-gap-table.md` theo đúng format của `presales-fit-gap-analysis-guide.md` mục 4:

```
| Mã | Yêu cầu | Khối | Ưu tiên (MoSCoW) | Đánh giá | Giải pháp đề xuất | Effort (man-day) | Ghi chú |
```

## Bước tiếp theo

- Bảng Fit-Gap cần được gửi lại cho khách để **sign-off** trước khi dùng `/odoo-proposal`.
- Nếu có yêu cầu liên quan di chuyển dữ liệu từ hệ thống cũ, gợi ý dùng `skills/presales-data-migration-scoping-guide.md` để scoping riêng trước khi chốt effort.

## AI Agent Instructions

1. **LOAD**: Discovery Notes (file hoặc nội dung user cung cấp) + `odoo-app-feature-matrix.md` + `presales-fit-gap-analysis-guide.md`
2. **CLASSIFY**: từng yêu cầu theo 6 nhãn, áp dụng thứ tự ưu tiên xử lý Gap để gợi ý giải pháp
3. **CROSS-CHECK VN**: nếu Gap-Integration liên quan VN, tra `vietnam-integration-landscape.md`
4. **OUTPUT**: `fit-gap-table.md` theo format chuẩn
5. **REMIND**: cần sign-off với khách trước khi chạy `/odoo-proposal`
