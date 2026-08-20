# Duyên Dịch v3.1 — Release Handoff

**Release:** `3.1.0-full-rewrite`
**Ngày:** 2026-08-20
**Trạng thái:** Release candidate sau kiểm định nội bộ
**Repository:** `ntnguyen983-sketch/duyen-dich-engine`

## Tóm tắt

Đây là bản viết lại hoàn chỉnh của đặc tả Duyên Dịch v3.1. Bản này không còn dùng `PLACEHOLDER` như nội dung chính. Các mô-đun đã được viết bằng công thức, pseudocode, guards, error behavior, profile registry, provenance, JSON contract và test vectors. Trạng thái `CALIBRATION_REQUIRED` vẫn tồn tại nhưng có nghĩa kỹ thuật cụ thể: profile đã có định nghĩa, miền, hash, điều kiện kích hoạt, behavior khi chưa active và test bắt buộc.

## Nguồn đã tích hợp

| Lớp | Nguồn | Nội dung đã tích hợp | Phân loại |
|---|---|---|---|
| L1 | v2.5.3/v2.5.6 | Ψ, F0, ΔF, SDE/Bellman/MDP, 12 phase operators | `REFERENCE` |
| L2 | v2.8.6 Master/BEC Unified v2.8.7 | SL-DIF, SIE, M_POL, M_SIE, M_FLUX, DWL, Vector Khí, BEC, Frozen Core | `CORE_PROFILE` hoặc `CALIBRATION_REQUIRED` theo profile |
| L3 | v2.9/v2.9.1/Py v2.9.3 | topology, matrix lookup, force normalization, L2-RGS, DPKE, delay, tick/replay | `RUNTIME_EVIDENCE` |
| L4 | v2.9.1-NEW2/v3.0.0 | sáu predicate S07, overlap policy, legacy decoder | `CALIBRATION_REQUIRED` + `COMPATIBILITY` |
| L5 | v3.0.0/governance | vocabulary, schema, provenance, gates, errors, hashes | `CORE` |
| L6 | UI/Operations | output A/B và API/interface boundary | `INTERFACE_ONLY` |

## Các sửa bắt buộc sau Gemini Vòng 2

Gemini xác nhận bản thiết kế ở mức `PASS_WITH_REQUIRED_CHANGES`. Ba sửa bắt buộc đã được áp dụng. S07 registry hiện có sáu predicate, miền giá trị, chín boundary vectors, overlap `MAPPING_AMBIGUOUS`, no-match `MAPPING_UNRESOLVED`, `rule_config_sha256` và trạng thái `CALIBRATION_REQUIRED`. Guard `persistence_denominator_missing=QUARANTINE` đã được thêm vào DWL profile. Confidence contract hiện bắt buộc audit status, scanned paths và `f_net_out_found=false`; G7 phải quét cấu trúc input để chặn semantic leakage.

Chu kỳ `ΦSystem=60` ticks đã được hạ rõ ràng về `RESEARCH`; runtime chỉ phát `SYNC_RESONANCE` như derived schedule marker. H1 Drain/Reserve cũng là `RESEARCH` và không được mutate Frozen Core.

## Kiểm định

| Kiểm định | Kết quả |
|---|---:|
| Unit tests đặc tả v3.1 | **10/10 PASS** |
| JSON syntax: runtime profiles | **PASS** |
| JSON syntax: S07 mapping | **PASS** |
| JSON syntax: vocabulary | **PASS** |
| JSON syntax: canonical response schema | **PASS** |
| Profile hash cross-check | **PASS** |
| S07 overlap vector | **PASS** |
| DWL denominator guard | **PASS** |
| Confidence firewall metadata | **PASS** |

## Các điểm không được nâng thành CORE

S07 đã có rule đầy đủ nhưng vẫn cần calibration/approval trước khi được coi là active semantic profile. RGS normalization, BEC lambda/gamma và threshold profile vẫn ở `CALIBRATION_REQUIRED`. Chu kỳ đồng pha 60 ticks và H1 Drain/Reserve ở `RESEARCH`. Các causal claims, phase-shift interpretation và semantic action không nằm trong runtime contract.

## Hash release

Hash phải được tính lại sau khi mọi artifact cuối cùng đã ổn định. `canonical_vocabulary.json` trỏ đến hash của `runtime_profiles_v31.json`; S07 profile có `rule_config_sha256`; release manifest sẽ ghi SHA-256 từng artifact.

## Cách kiểm định lại

```bash
cd specs/v3.1
python3 -m unittest discover -s tests -v
python3 -m json.tool runtime_profiles_v31.json >/dev/null
python3 -m json.tool s07_mapping_profile_v31.json >/dev/null
python3 -m json.tool canonical_vocabulary.json >/dev/null
python3 -m json.tool schemas/canonical_response.schema.json >/dev/null
```

## Quyết định vận hành

Bản release này có thể dùng làm **canonical implementation contract** và test target. Không được dùng nó như bằng chứng dự đoán thực tại; mọi output semantic phải giữ provenance, uncertainty và gate result. Decoder chỉ đọc; không có write-back vào Kernel.
