# DUYÊN DỊCH v2.8.7+ REV.B — FULL LINEAGE CAPTURE

Source: `DUYEN_DICH_UNIFIED_MASTER_SPEC_2.8.7_REV.B.pdf` / equivalent DOCX (Library source captured 2026-08-21).

## Authority
DD-SPEC-2.8.7-UNIFIED / REV.B — MASTER RUNTIME SPEC.
Runtime mode: DETERMINISTIC_FORWARD_ONLY / CONTINUOUS_CONTEXT.
CORE_POLICY = FROZEN; RESEARCH_POLICY = EXPLICIT + CALIBRATED; KNOWLEDGE_POLICY = ADAPTER_ONLY; RESET_POLICY = INITIALIZATION_EVENT_ONLY; SEMANTIC_POLICY = DECODE_AFTER_S07.

## Purpose
Rev.B unifies 2.8.7+ Rev.A and the full specification into one runtime path, deduplicating conflicting rules. Research/BEC remains a layer over Frozen Core and is not automatically Core-validated.

## Context continuity
Observation/Evidence at later ticks continues the running case. A new Core State is created only by an explicit valid Initialization Event. GPS, timestamps, real-world feedback and order results do not silently recreate the original quẻ.

## Runtime contracts
Raw input → canonical state → graph → weights → field → kinematics → emergence → output → evidence.
Published historical Core State is never retrospectively mutated by Ground Truth. Calibration may produce parameters/profiles for subsequent ticks/cases.

## Precision / provenance
Core precision: 6 decimals. Research/BEC reporting: 4 decimals unless explicitly a core calculation. Canonical JSON uses sorted keys and SHA-256. Every quantitative output carries precision and calibration status.

## Research / BEC
BEC is disabled by default in the unified runtime unless enabled by profile. Research hypotheses require explicit status. They cannot silently become constants or mutate Frozen Core.

## Lineage role
Rev.B is preserved as the historical unified runtime authority for the 2.8.7 generation. No attempt is made here to merge its rules into v3.4; the purpose is to retain the source material for later comparison.
