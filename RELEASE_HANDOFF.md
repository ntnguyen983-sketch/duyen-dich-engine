# Duyên Dịch v3.1 — Release Handoff

## Trạng thái phát hành

Bản hợp nhất v3.1 đã được commit và đẩy lên repository [ntnguyen983-sketch/duyen-dich-engine](https://github.com/ntnguyen983-sketch/duyen-dich-engine) tại commit [`1d1a4fd83528d98c8a74ee8760451fde737a9c42`](https://github.com/ntnguyen983-sketch/duyen-dich-engine/commit/1d1a4fd83528d98c8a74ee8760451fde737a9c42). Working tree cục bộ sạch và `origin/main` trùng commit này.

## Quyết định đã khóa

Bản v3.1 khóa sáu mã S07 `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`; firewall giữa L3 và L4; năm validation gates; behavior `MAPPING_UNRESOLVED` khi profile thiếu/sai; provenance; tách uncertainty khỏi confidence; cấm dùng `f_net_out` làm confidence; và determinism contract của Snapshot/TickEngine.

## Phần không được tự suy đoán

SDE/Bellman/12 phase operators của v2.5, SL-DIF/BEC của v2.8, matrix/delay v2.9.2, S07 threshold profile và các calibration constants chưa được nâng thành CORE vì không tìm thấy phụ lục gốc trong các repository đã chọn. Công thức BEC do Gemini đề xuất ở Vòng 1 đã bị Vòng 2 và Manus loại bỏ.

## Artifact chính

| Artifact | Mục đích |
|---|---|
| `specs/v3.1/DUYEN_DICH_v3.1.md` | Đặc tả hợp nhất duy nhất |
| `specs/v3.1/canonical_vocabulary.json` | Từ vựng canonical sáu mã |
| `specs/v3.1/s07_mapping_profile_v31.json` | Registry profile hiện ở `MAPPING_UNRESOLVED` |
| `specs/v3.1/compatibility/legacy_decoder.json` | Đọc dữ liệu lịch sử, không ép canonical |
| `specs/v3.1/schemas/canonical_response.schema.json` | Hợp đồng JSON L5 |
| `specs/v3.1/artifacts/decision_log.md` | Quyết định giữ/sửa/loại |
| `gemini_round1.json` | Đề xuất Gemini Vòng 1 |
| `gemini_round2.json` | Phản biện Gemini Vòng 2 |
| `SOURCE_INVENTORY.md` | Inventory repo và giới hạn bằng chứng |
| `specs/v3.1/artifacts/file_hashes.sha256` | Hash provenance |

## Kiểm thử

Bộ test đặc tả v3.1: **6/6 pass**. Baseline `dd_engine1`: **11/11 pass**. Các test đã kiểm tra enum canonical, loại nhãn legacy khỏi Kernel, unresolved mapping, confidence firewall, provenance boundary, firewall semantic và decision log.

## Bước tiếp theo có điều kiện

Để chuyển các phần `RESEARCH/PLACEHOLDER` thành runtime canonical, cần bổ sung phụ lục gốc hoặc artifact có hash cho v2.5, v2.8, v2.9.2 và profile S07. Sau đó phải chạy lại các gate liên quan, test vectors tại DPKE zero/small denominator, BEC boundary `R=0.30`/`R=0.10`, replay 60 ticks và hai vòng review Gemini; không được sửa trực tiếp Kernel bằng suy đoán.
