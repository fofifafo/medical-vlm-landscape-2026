"""30편 검증 표본: Claude 판정(audit.jsonl) vs 사람 판정(validation_human.json) → 항목별·합산 일치율, Cohen's κ, 불일치 목록."""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.abspath(__file__))
A = {}
for l in open(os.path.join(ROOT, "audit.jsonl"), encoding="utf-8"):
    if l.strip(): a = json.loads(l); A[a["id"]] = a
H = json.load(open(os.path.join(ROOT, "validation_human.json"), encoding="utf-8"))
K = ["LAT", "HW", "FLOP", "MEM", "ENG", "THR"]
KO = {"LAT": "지연", "HW": "하드웨어", "FLOP": "FLOPs", "MEM": "메모리", "ENG": "에너지", "THR": "처리량"}
def kappa(a, b, c, d):
    n = a + b + c + d; po = (a + d) / n; pe = ((a + b) * (a + c) + (c + d) * (b + d)) / n ** 2
    return po, (1.0 if pe >= 1 else (po - pe) / (1 - pe))
tot = [0, 0, 0, 0]; dis = []
print(f"{'항목':6} 둘다Y  C만Y  사람만O  둘다N   일치율    κ")
for k in K:
    cell = [0, 0, 0, 0]
    for h in H:
        c = A[h["id"]][k] == "Y"; m = h["judgment"].get(k) == "O"
        i = 0 if (c and m) else 1 if c else 2 if m else 3
        cell[i] += 1; tot[i] += 1
        if i in (1, 2): dis.append((h["n"], h["id"], KO[k], "Claude Y / 사람 X" if i == 1 else "Claude N / 사람 O", h["note"]))
    po, kp = kappa(*cell)
    print(f"{KO[k]:6} {cell[0]:5} {cell[1]:5} {cell[2]:7} {cell[3]:6}    {po:.2f}   {kp:.2f}" + ("  (κ 정의 불가: 둘 다 전부 N)" if cell[0] + cell[1] + cell[2] == 0 else ""))
po, kp = kappa(*tot)
print(f"합산   {tot[0]:5} {tot[1]:5} {tot[2]:7} {tot[3]:6}    {po:.3f}  {kp:.3f}   (판정 {sum(tot)}개)")
print("\n불일치", len(dis))
for d in dis: print(" ", d)
json.dump({"pooled": {"agree": round(po, 4), "kappa": round(kp, 4), "cells": tot}, "disagreements": dis}, open(os.path.join(ROOT, "validation_kappa.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
