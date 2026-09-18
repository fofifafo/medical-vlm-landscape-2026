# -*- coding: utf-8 -*-
"""audit.jsonl → audit.csv, evidence.md, summary(표 II 본문 열), 검증 표본 30편(validation_sample.csv).
   LAT 세분: 근거 문장에 'training'/'hours'/'GPU-h'/'epoch'만 있으면 학습 시간(LAT_train), 아니면 추론 지연(LAT_infer)."""
import json, csv, re, random, sys, os
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.abspath(__file__))
rows = [json.loads(l) for l in open(os.path.join(ROOT, "audit.jsonl"), encoding="utf-8")]
meta = {r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "..", "healthcare_shortlist.csv"), encoding="utf-8-sig"))}
# 초록 기준(기존 표 II) 재현용: 초록 텍스트에 같은 패턴
ABS = {
 "LAT": re.compile(r"latenc|inference (?:time|speed)|\bms\b|milliseconds|seconds? per|(?:×|x)\s*(?:faster|speed-?up)|speed-?up", re.I),
 "HW":  re.compile(r"A100|A6000|A40|H100|H20|V100|T4|RTX|Jetson|iPhone|Snapdragon|smartphone|GPU\b", re.I),
 "FLOP":re.compile(r"FLOPs?|MACs?\b|GMACs", re.I),
 "MEM": re.compile(r"\bGB\b|VRAM|memory (?:usage|footprint)|RAM\b", re.I),
 "ENG": re.compile(r"energy|watt|joule|power consumption|mWh|carbon", re.I),
 "THR": re.compile(r"throughput|tokens?/s|fps\b|samples?/s", re.I),
}
TRAIN = re.compile(r"train|hours|GPU-h|epoch|fine-tun|SFT|RLVR|minutes per method|367 minutes", re.I)
INFER = re.compile(r"infer|latency|per (?:image|sample|case|window|frame)|ms\b|tokens?/s|speedup|faster|fps|end-to-end|TTFT|ms/token|ms/step|s per", re.I)
out = []
for r in rows:
    aid = r["id"]; ab = meta[aid]["abstract"]
    lat_ev = r["ev"].get("LAT", "")
    lat_infer = "Y" if r["LAT"] == "Y" and INFER.search(lat_ev) and not (TRAIN.search(lat_ev) and not re.search(r"infer|latency|ms/token|tokens?/s|fps|per (?:image|sample|case|window|frame)|end-to-end|TTFT|ms/step|speedup|faster", lat_ev, re.I)) else "N"
    lat_train = "Y" if r["LAT"] == "Y" and lat_infer == "N" else ("Y" if r["LAT"] == "Y" and TRAIN.search(lat_ev) else "N")
    # 수동 교정(근거 문장 재검토): 추론 지연이 분명한 3편
    if aid in ("2409.00084", "2601.14406", "2605.09443"): lat_infer, lat_train = "Y", ("Y" if aid == "2601.14406" else "N")
    rec = {"id": aid, "date": meta[aid]["date"], "title": meta[aid]["title"], "tag": meta[aid].get("효율키워드") or list(meta[aid].values())[7],
           **{k: r[k] for k in ["LAT", "HW", "FLOP", "MEM", "ENG", "THR", "PAR"]},
           "LAT_infer": lat_infer, "LAT_train": lat_train,
           **{"abs_" + k: ("Y" if rx.search(ab) else "N") for k, rx in ABS.items()},
           "note": r["note"]}
    out.append(rec)
K = ["LAT", "HW", "FLOP", "MEM", "ENG", "THR"]
with open(os.path.join(ROOT, "audit.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
n = len(out)
def cnt(key, val="Y"): return sum(1 for o in out if o[key] == val)
print(f"{'quantity':28s} {'abstract':>9s} {'full text':>10s}")
for k, lab in [("LAT", "Latency / time (any)"), ("LAT_infer", "  inference-side latency"), ("LAT_train", "  training time only"), ("HW", "Named hardware"), ("FLOP", "FLOPs / MACs"), ("MEM", "Memory footprint"), ("ENG", "Energy or power"), ("THR", "Throughput")]:
    a = cnt("abs_" + k) if ("abs_" + k) in out[0] else None
    print(f"{lab:28s} {('%3d (%4.1f%%)' % (a, 100*a/n)) if a is not None else '':>12s} {cnt(k):3d} ({100*cnt(k)/n:4.1f}%)")
meas = [o for o in out if any(o[k] == "Y" for k in ["LAT_infer", "FLOP", "MEM", "ENG", "THR"])]
print("≥1 inference-relevant measured quantity (infer-latency/FLOPs/memory/energy/throughput):", len(meas), f"({100*len(meas)/n:.1f}%)")
none6 = [o for o in out if not any(o[k] == "Y" for k in K)]; print("none of six in full text:", len(none6))
hwonly = [o for o in out if o["HW"] == "Y" and not any(o[k] == "Y" for k in ["LAT", "FLOP", "MEM", "ENG", "THR"])]; print("hardware named but no quantity:", len(hwonly))
absnone = [o for o in out if not any(o["abs_" + k] == "Y" for k in K)]; print("none of six in abstract (recomputed):", len(absnone))
gain = [o for o in absnone if any(o[k] == "Y" for k in ["LAT_infer", "FLOP", "MEM", "ENG", "THR"])]; print("abstract-silent but body reports an inference-relevant quantity:", len(gain))
ondev = [o for o in out if re.search(r"iPhone|Snapdragon|Honor|smartphone|Android|Jetson", json.dumps(next(r for r in rows if r['id']==o['id'])["ev"]))]; print("measured on a phone/edge device:", len(ondev), [o["id"] for o in ondev])
# 검증 표본 30편: 층화(측정 있음 15 / 없음 15)
random.seed(20260914)
yes = [o for o in out if any(o[k] == "Y" for k in ["LAT", "FLOP", "MEM", "ENG", "THR"])]; no = [o for o in out if o not in yes]
samp = random.sample(yes, 15) + random.sample(no, 15); random.shuffle(samp)
ev = {r["id"]: r["ev"] for r in rows}
with open(os.path.join(ROOT, "validation_sample.csv"), "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(["#", "id", "title", "Claude LAT", "Claude HW", "Claude FLOP", "Claude MEM", "Claude ENG", "Claude THR", "근거 발췌", "지유찬 LAT", "지유찬 HW", "지유찬 FLOP", "지유찬 MEM", "지유찬 ENG", "지유찬 THR", "메모"])
    for i, o in enumerate(samp, 1):
        w.writerow([i, o["id"], o["title"], o["LAT"], o["HW"], o["FLOP"], o["MEM"], o["ENG"], o["THR"], " | ".join(f"{k}: {v}" for k, v in ev[o["id"]].items()), "", "", "", "", "", "", ""])
with open(os.path.join(ROOT, "evidence.md"), "w", encoding="utf-8") as f:
    f.write("# 효율 144편 전문 판정 근거 (2026-09-14, 판정: Claude, 규칙: RUBRIC.md)\n\n")
    for o in out:
        f.write(f"## {o['id']} — {o['title']}\n- LAT {o['LAT']} (infer {o['LAT_infer']}, train {o['LAT_train']}) · HW {o['HW']} · FLOP {o['FLOP']} · MEM {o['MEM']} · ENG {o['ENG']} · THR {o['THR']} · PAR {o['PAR']}\n")
        for k, v in ev[o["id"]].items(): f.write(f"  - {k}: {v}\n")
        if o["note"]: f.write(f"  - note: {o['note']}\n")
        f.write("\n")
print("wrote audit.csv, evidence.md, validation_sample.csv (30)")
