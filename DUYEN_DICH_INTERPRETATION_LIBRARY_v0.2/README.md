# Duyên Dịch Interpretation Library v0.2

**Contract:** Duyên Dịch v3.1 (`contract_version=3.1.0`)  
**Layer position:**

```text
DETERMINISTIC KERNEL  →  CANONICAL OUTPUT  →  INTERPRETATION LIBRARY  →  OPERATIONS DECODER  →  LANGUAGE OUTPUT
```

This library does **not** modify Core Engine. It does **not** deploy.

## Principles

1. Structural facts only where source confirms them.
2. **Thể/Dụng is completely banned** (code, JSON, rules, examples, golden cases).
3. MSIE nodes `N1..N12` are addresses, not fixed real-world objects.
4. Applied images require Input + Context + Evidence; otherwise `UNSUPPORTED`.
5. S07 profile rules are recorded as `SOURCE_CONFIRMED` text; profile remains `CALIBRATION_REQUIRED`.
6. Missing traditional tables (hexagram names, elements, proper/improper positions) are **not invented** in CORE; external names live under `external_sources/` only.

## Layout

```text
DUYEN_DICH_INTERPRETATION_LIBRARY_v0.2/
  README.md
  REVIEW_REQUIRED.md
  structural/
  resolver/
  validation/
  external_sources/
```

See `external_sources/SOURCE_REGISTRY.md` and `REVIEW_REQUIRED.md`.
