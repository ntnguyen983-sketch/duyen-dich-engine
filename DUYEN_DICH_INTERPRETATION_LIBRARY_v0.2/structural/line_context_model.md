# Line Context Model — v0.2

**Classification:** DERIVED_FROM_SOURCE (structural) + PROVISIONAL (application context slots)  
**Contract version:** 3.1.0  
**Banned:** Thể/Dụng in any form.

## 1. Structural meaning (SOURCE_CONFIRMED / DERIVED)

From `specs/v3.1/DUYEN_DICH_v3.1.md` §6 and `runtime/v31/engine.py`:

| Concept | Definition |
|---|---|
| Line index | Integer `1..6` |
| Bit | `{0,1}` at that line for a given `root_code` |
| MSIE node (root) | `Hào k → Nk` |
| MSIE node (transformed pair) | `N(k+6)` when transformed state exists |
| Line zones (for Vector Khí S component in **spec** text) | lines 1–2 / 3–4 / 5–6 |
| Structural operators | `M_k` (flip), `P` (reverse), `C` (complement), `H` (nuclear) — structural only, no semantic label |
| Topology profile | `TOPOLOGY-MCHI-2.9.3`, `node_count=12` |

Structural meaning answers only: *which bit, which node, which zone, which operator path*.

It does **not** answer: *what object in the world the line “is”*.

## 2. MSIE is an application domain, not a fixed ontology

Spec: *“Mapping 6-line→12-node is `topology_profile_id`”*.  
Task constraint: MSIE is miền ứng; context decides concrete image.

Therefore:

- `N1..N6` / `N7..N12` are **node addresses**, not people, vehicles, weather, or institutions.
- Binding a node to a concrete image requires **Input + Context + Evidence**.
- Default binding without evidence is **forbidden** (anti-hallucination).

## 3. Context layer (PROVISIONAL application slots)

The seven context ids below are **library application slots** requested for Operations Decoder.  
They are **not** defined as CORE enums in `canonical_vocabulary.json` or the engine.

| Context id | Slot purpose (operations only) |
|---|---|
| `RELATIONSHIP` | interpersonal question framing |
| `WORK` | work / role framing |
| `MONEY` | resource / exchange framing |
| `MOVEMENT` | travel / relocation framing |
| `DECISION` | choice / branch framing |
| `INTENT` | stated intention framing |
| `FORECAST` | time-forward question framing |

Pipeline:

```text
STRUCTURAL MEANING  →  CONTEXT MAPPING  →  APPLIED IMAGE
     (bits/nodes)         (slot only)      (requires evidence)
```

If evidence is missing → Applied Image = `UNSUPPORTED` / `EVIDENCE_REQUIRED`.

## 4. Explicit non-bindings

The library must **not** hard-code, for example:

- N2 = vehicle  
- N4 = authority figure  
- N6 = weather  

unless the current Input/Context/Evidence record supplies that binding with provenance.

## 5. Traceability

Every applied image output should carry:

- `hexagram_id`, `line_index`, `msie_node`
- `context_id`
- `evidence_refs[]` (may be empty)
- `gate_result` from Evidence Gates
- `classification`: `SOURCE_CONFIRMED` | `DERIVED_FROM_SOURCE` | `PROVISIONAL` | `MISSING_SOURCE`
