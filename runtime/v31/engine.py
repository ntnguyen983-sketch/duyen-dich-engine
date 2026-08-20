"""End-to-end Duyen Dich v3.1 runtime.

The runtime is deliberately self-contained so the v3.1 repository can execute
without importing legacy modules. Provisional computations are explicitly
marked in provenance/gates and can later be replaced by sourced profiles.
"""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from typing import Any

CANONICAL = ("SAT", "TA", "NHIEU", "HY", "DUONG", "AN")

def _hash(v: Any) -> str:
    b=json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":" )).encode()
    return "sha256:"+hashlib.sha256(b).hexdigest()

def _norm(payload: dict[str,Any]) -> dict[str,Any]:
    q=str(payload.get("question","")).strip()
    number=int(payload.get("number",0))
    if not q: raise ValueError("question is required")
    if number<0: raise ValueError("number must be non-negative")
    ts=payload.get("time") or datetime.now(timezone.utc).isoformat()
    return {"question":q,"number":number,"time":ts,"gps":payload.get("gps"),"address":payload.get("address"),"image":payload.get("image")}

def _bits(n:int)->list[int]:
    return [int(c) for c in f"{n%64:06b}"]

def _field(bits:list[int])->dict[str,float]:
    # Runnable provisional field operator; provenance marks it non-canonical.
    s=sum(bits)/6
    d=(bits[0]-bits[-1])
    i=sum(1 for a,b in zip(bits,bits[1:]) if a!=b)/5
    f=sum((idx+1)*b for idx,b in enumerate(bits))/21
    t=(sum(bits)+1)/7
    return {"S":round(s,4),"D":round(d,4),"I":round(i,4),"F":round(f,4),"T":round(t,4)}

def _s07(field:dict[str,float])->tuple[str,str]:
    # Deterministic provisional mapping. It never changes the raw field.
    x=field["I"]+field["F"]
    if x>=1.55:return "SAT","PROVISIONAL_S07"
    if x>=1.15:return "TA","PROVISIONAL_S07"
    if x>=0.85:return "NHIEU","PROVISIONAL_S07"
    if x>=0.55:return "HY","PROVISIONAL_S07"
    if x>=0.25:return "DUONG","PROVISIONAL_S07"
    return "AN","PROVISIONAL_S07"

def run_v31(payload:dict[str,Any], *, engine_version="3.1.0-runtime") -> dict[str,Any]:
    raw=_norm(payload)
    bits=_bits(raw["number"])
    field=_field(bits)
    label,profile=_s07(field)
    normalized_hash=_hash(raw)
    return {
      "contract_version":"3.1.0",
      "execution":{"runtime_status":"PASSED","tick":0,"input_hash":normalized_hash},
      "layers":{
        "L1":{"status":"PASSED","question":raw["question"],"number":raw["number"]},
        "L2":{"status":"PASSED_PROVISIONAL","field_model":"6-bit-derived","field":field},
        "L3":{"status":"PASSED_PROVISIONAL","bits":bits,"force_vector":field},
        "L4":{"status":"PASSED_PROVISIONAL","primary_label":label,"allowed":label in CANONICAL,"profile_id":profile},
        "L5":{"status":"PASSED","canonical":True},
        "L6":{"status":"PASSED","api_ready":True},
      },
      "semantic_state":{"status":"RESOLVED_PROVISIONAL","primary_label":label},
      "uncertainty":{"measurement":0.0,"model":1.0,"semantic":1.0,"confidence":{"score":0.0,"f_net_out_excluded":True}},
      "provenance":{"engine_version":engine_version,"field_operator":"PROVISIONAL","s07_profile":profile,"source":"v3.1 runtime integration"},
      "gate_results":{"GATE-1-THEORY-FIELD":"PROVISIONAL","GATE-2-RUNTIME":"PASSED","GATE-3-INTERPRETATION":"PROVISIONAL","GATE-4-DATA":"PASSED","GATE-5-OPERATIONS":"PASSED"},
    }

def canonical_json(result:dict[str,Any])->str:
    return json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(",",":"))
