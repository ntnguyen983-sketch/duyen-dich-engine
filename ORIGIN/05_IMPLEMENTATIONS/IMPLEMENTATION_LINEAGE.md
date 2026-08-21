# IMPLEMENTATION LINEAGE

## 1. v2.3.x
Early implementations encode Structural/SIE/Ngũ hành and localization concepts. They are useful as executable history and test material.

## 2. v2.8.x
The architecture separates frozen core from runtime extensions. Runtime may expand through adapters/plugins/APIs without silently changing core axioms.

## 3. v2.9.2 merged implementation
`duyen_dich_engine_v293_full.py` is a substantial reference implementation containing deterministic runtime, matrix core, DWL, DPKE, BEC observation, emergence, spacetime, ROM, warning, implication, forecast, recommendation and canonical JSON/hash pathways.

Its own header explicitly describes the design contract: Core is deterministic/forward-only; observation and interpretation do not mutate Core; BEC density and observation are separate; S00→S08 is preserved.

## 4. DD-3A v3.4 strict reference
The newer strict reference separates Entity from Space and refuses to invent unvalidated L4-derived values. Its role is reference architecture, not a claim that the code is already production-complete.

## 5. Production split
The production worker should be developed as a separate implementation branch. It must consume the Origin documents, not redefine them. A worker may optimize data structures, graph algorithms, parsers, APIs and UI while preserving the architectural contract.

## 6. No GEM hardcoding
External model/GEM knowledge must enter through an explicit adapter. It must not become an undocumented second Core or mutate canonical state.

## Worker deliverable
A production implementation should include:
1. canonical input schema;
2. validation;
3. deterministic structural engine;
4. dynamic event/flow/rhythm engine;
5. calibration/research boundary;
6. provenance + canonical JSON + hash;
7. regression vectors;
8. API contract;
9. UI adapter;
10. deployment/test automation.
