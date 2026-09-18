# -*- coding: utf-8 -*-
"""본문 텍스트에서 효율 수치 후보 문장을 항목별로 추출 → candidates.json
   항목: latency, hardware, flops, memory, energy, throughput, params(보조)
   각 후보 = {kind, sent, pos(문서 내 위치 비율), sec(추정 절)} — 관련연구/참고문헌 구간 표시.
   실행: python efficiency_audit/extract_candidates.py"""
import os, re, json, sys, csv
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.abspath(__file__))
rows = {r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "..", "healthcare_shortlist.csv"), encoding="utf-8-sig"))}

PAT = {
 "latency":    r"\b(latenc\w*|inference (?:time|speed)|(?:run|wall[- ]clock|execution|response|processing) ?time|(?:ms|milliseconds?|seconds?|sec|s)\s*(?:per|/)\s*(?:image|sample|query|case|token|slide|frame|volume|scan)|(?:\d+(?:\.\d+)?)\s*(?:ms|milliseconds)\b|time[- ]to[- ]first[- ]token|TTFT|tokens?\s*(?:per|/)\s*(?:second|sec|s)\b|\d+(?:\.\d+)?\s*×?\s*(?:faster|speed-?up))",
 "hardware":   r"\b(A100|A6000|A40|A10|H100|H800|V100|T4|L4|L40S?|RTX\s?\d{3,4}|GeForce|Tesla|Quadro|Jetson(?:\s+\w+)?|Orin|Xavier|Raspberry Pi|Snapdragon|Apple\s+M\d|iPhone|Android|TPU\s*v?\d?|NPU|FPGA|Intel\s+Xeon|Ryzen|CPU-only|on a single (?:GPU|CPU)|(?:\d+)\s*×?\s*(?:GPUs?|NVIDIA))",
 "flops":      r"\b(\d+(?:\.\d+)?\s*[GTP]?FLOPs?|FLOPs?\b|MACs?\b|multiply[- ]accumulate)",
 "memory":     r"\b(\d+(?:\.\d+)?\s*(?:GB|GiB|MB)\s*(?:of\s+)?(?:GPU\s+)?(?:memory|VRAM|RAM)?|(?:GPU |peak |memory )?(?:memory|VRAM) (?:usage|footprint|consumption|requirement)|KV[- ]cache (?:size|memory))",
 "energy":     r"\b(energy|power consumption|watt\w*|\bW\b(?=\s|$)|joule|\bJ\b\s*(?:per|/)|mWh|kWh|carbon|CO2|battery)",
 "throughput": r"\b(throughput|(?:images?|samples?|queries|slides?|frames?|cases?)\s*(?:per|/)\s*(?:second|sec|s|hour|minute)\b|QPS|\bfps\b)",
 "params":     r"\b(\d+(?:\.\d+)?\s*[BM]\s*(?:parameters|params)|(?:trainable|active|total)\s+parameters|parameter count)",
}
RX = {k: re.compile(v, re.I) for k, v in PAT.items()}
NUM = re.compile(r"\d")
SEC_HDR = re.compile(r"^\s*(?:\d+(?:\.\d+)*\.?\s+)?(related work|background|preliminar\w+|experiments?|experimental (?:setup|results)|implementation details|results|evaluation|efficiency|analysis|ablation|limitations?|conclusion|references|appendix|supplementary)\b", re.I | re.M)

def sentences(text):
    text = re.sub(r"-\n(?=[a-z])", "", text)          # 하이픈 줄바꿈 복원
    text = re.sub(r"\s*\n\s*", " ", text)
    return re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text)

out = {}
for aid in rows:
    fp = os.path.join(ROOT, "txt", aid + ".txt")
    if not os.path.exists(fp): continue
    raw = open(fp, encoding="utf-8").read()
    # 참고문헌 시작 위치(뒤에서 가장 먼저 나오는 References 헤더)
    refpos = None
    for m in re.finditer(r"\n\s*(?:\d+\s+)?References\s*\n", raw): refpos = m.start()
    body = raw[:refpos] if refpos else raw
    # 관련연구 구간
    rel = [(m.start(), m.group(1).lower()) for m in SEC_HDR.finditer(body)]
    def sec_at(pos):
        cur = "front"
        for p, name in rel:
            if p <= pos: cur = name
            else: break
        return cur
    sents = sentences(body); cands = []; off = 0
    joined = " ".join(sents)
    for s in sents:
        pos = joined.find(s, off); off = pos + len(s) if pos >= 0 else off
        for k, rx in RX.items():
            if rx.search(s) and (NUM.search(s) or k in ("energy",)):
                cands.append({"kind": k, "sent": s.strip()[:600], "pos": round(pos / max(1, len(joined)), 3), "sec": sec_at(pos)})
    out[aid] = {"title": rows[aid]["title"], "n_chars": len(body), "has_refs_cut": refpos is not None, "cands": cands}
json.dump(out, open(os.path.join(ROOT, "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
tot = sum(len(v["cands"]) for v in out.values())
print("papers with text:", len(out), "| candidate sentences:", tot)
from collections import Counter
print(Counter(c["kind"] for v in out.values() for c in v["cands"]))
print("papers with ≥1 energy candidate:", sum(1 for v in out.values() if any(c["kind"]=="energy" for c in v["cands"])))
