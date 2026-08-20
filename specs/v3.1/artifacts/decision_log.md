# Duyên Dịch v3.1 — Decision Log

## Phạm vi quyết định

Gemini được dùng để đề xuất và phản biện. Quyết định cuối cùng dưới đây được Manus đối chiếu với canonical governance và bằng chứng đã truy xuất trong repository.

| Decision ID | Chủ đề | Hành động | Classification | Căn cứ |
|---|---|---|---|---|
| `DD31-DEC-001` | Sáu mã S07 `SAT, TA, NHIEU, HY, DUONG, AN` | Giữ | `CORE` | Canonical governance; không có mã thứ bảy |
| `DD31-DEC-002` | Firewall giữa L3 và L4 | Giữ | `CORE` | Bảo vệ ranh giới compute–interpretation |
| `DD31-DEC-003` | Năm validation gates | Giữ | `CORE` | Contract và failure behavior có thể kiểm định |
| `DD31-DEC-004` | Determinism `S_(t+1)=K(S_t,I_t)` | Giữ ở mức contract | `CORE` | Snapshot/TickEngine và baseline test hiện hữu |
| `DD31-DEC-005` | `S07_CANONICAL_V31_DEFAULT` với threshold cụ thể | Loại | `RESEARCH` | Gemini Vòng 2 xác nhận không có provenance/calibration/hash/test vectors |
| `DD31-DEC-006` | Công thức BEC `I*F/(1+epsilon)` | Loại hoàn toàn | `PLACEHOLDER` | Đây là công thức suy đoán, không có phụ lục v2.8 |
| `DD31-DEC-007` | `safe_epsilon=1e-7` | Hạ cấp | `RESEARCH/CALIBRATION` | Safety parameter cần đăng ký; không phải invariant vật lý |
| `DD31-DEC-008` | Nhãn lịch sử trong canonical vocabulary | Loại khỏi canonical list | `COMPATIBILITY` | Chỉ decoder ngoài Kernel được đọc với provenance |
| `DD31-DEC-009` | Matrix/delay runtime v2.9.2 | Chưa khóa công thức | `RESEARCH` | Không có spec gốc trong các repository |
| `DD31-DEC-010` | `eval()` trong semantic evaluator | Loại khỏi thiết kế | `CORE security rule` | Chuyển sang declarative AST/whitelist; không thực thi chuỗi Python |
| `DD31-DEC-011` | Confidence | Tách khỏi lực | `CORE` | `f_net_out` không được là confidence |
| `DD31-DEC-012` | Profile thiếu/sai hash/ngoài domain | Trả unresolved | `CORE failure behavior` | Không ép vector 5D thành S07 |

## Gemini Vòng 1

Gemini đề xuất khung 6 lớp, 5 gates, data contract, profile S07 và pseudocode runtime. Một số phần hữu ích được giữ ở cấp contract. Tuy nhiên, Vòng 1 đã tự tạo threshold profile, công thức BEC và epsilon cố định; các điểm đó không được chấp nhận.

## Gemini Vòng 2

Gemini tự phản biện và xác định các lỗi chính: profile S07 chưa có evidence; công thức BEC là suy đoán; epsilon cụ thể không được nâng thành CORE; legacy không được đưa vào canonical vocabulary; L3 matrix/delay chưa đủ bằng chứng để gọi là CORE; và uncertainty variance không được gán cứng.

## Quyết định cuối

Bản v3.1 khóa **vocabulary, firewall, gate architecture, failure behavior, provenance contract và determinism contract**. Bản v3.1 không khóa **công thức SDE/Bellman, SL-DIF/BEC, matrix/delay v2.9.2, S07 thresholds hoặc calibration constants**. Những phần chưa đủ bằng chứng đã được ghi rõ trong các file `RESEARCH` và `PLACEHOLDER`, không bị che bằng dự đoán.

## Artifact review

| Artifact | Nội dung |
|---|---|
| `gemini_round1.json` | Prompt, model, thời điểm và đề xuất Vòng 1 |
| `gemini_round2.json` | Prompt, model, thời điểm và phản biện Vòng 2 |
| `SOURCE_INVENTORY.md` | Repository, commit và giới hạn bằng chứng |
| `DUYEN_DICH_v3.1.md` | Đặc tả hợp nhất đã viết lại |


## DD31-DEC-013 — Full rewrite from Drive source corpus

**Status:** ACCEPTED FOR RELEASE CANDIDATE
**Basis:** Corpus trích xuất từ Google Docs nguồn v2.5.3, v2.5.6, v2.8.6, BEC Unified v2.8.7, v2.9 overview, v2.9.1 NEW2, Py v2.9.3 và canonical v3.0.0.
**Decision:** Thay bản khung placeholder bằng đặc tả có công thức, pseudocode, profile, guard, gate, error behavior, provenance và test vectors. `CALIBRATION_REQUIRED` là trạng thái có behavior, không phải nội dung trống.
**Boundary:** Không nâng S07 activation, RGS normalization, BEC lambda/gamma, threshold profile, ΦSystem=60 ticks hoặc H1 Drain/Reserve thành CORE nếu chưa có approval/calibration độc lập.

## DD31-DEC-014 — Profile conflict isolation

**Status:** ACCEPTED
**Decision:** `DD-DELAY-2.9.2-TF1` và `DD-DELAY-REV-A` là named profiles không composable trong cùng execution. Runtime phải ghi profile selection và từ chối `PROFILE_SELECTION_CONFLICT` khi chọn đồng thời.

## DD31-DEC-015 — Gemini Round 2 required changes

**Status:** APPLIED
**Decision:** Đã thêm S07 boundary vectors và `rule_config_sha256`, guard `persistence_denominator_missing=QUARANTINE`, confidence tree audit với `f_net_out_found=false`, TV-017 overlap và TV-018 denominator missing. `ΦSystem=60` và H1 Drain/Reserve được hạ về `RESEARCH`.
