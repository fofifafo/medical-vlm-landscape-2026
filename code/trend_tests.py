"""표 I 24개 가지에 대해 (1) 2024 vs 2026 Fisher(검증용), (2) 3년 Cochran–Armitage 추세 검정, (3) 2026을 1–6월로 제한한 민감도 분석.
   리뷰 대응 B8·B9 (9/18). 순수 파이썬(scipy 없음)."""
import re, sys, os, collections, math
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); os.chdir(os.path.dirname(os.path.abspath(__file__)))
_o = sys.stdout; sys.stdout = open(os.devnull, "w", encoding="utf-8")
import medical_taxonomy as mt
sys.stdout = _o
from strict_tags import STRICT, fisher_exact
med = mt.med
AX = {n: p for ax in mt.AXES.values() for n, p in ax}
ROWS = [  # (표 I 이름, 정규식)
 ("Pathology / WSI", AX["병리 — 조직/WSI"]), ("Chest X-ray", AX["방사선 — X-ray/CXR"]), ("CT / MRI", AX["방사선 — CT/MRI (3D)"]),
 ("Endoscopy / surgical video", AX["내시경·수술 영상"]), ("Ophthalmology", AX["안과 — 안저/OCT"]),
 ("VQA", AX["의료 VQA"]), ("Grounding vocabulary", AX["병변 탐지·그라운딩"]), ("Grounding as contribution", STRICT["grounding_contribution"]),
 ("Report generation", AX["판독문 생성"]), ("Clinical decision", AX["임상 의사결정·추론"]), ("Retrieval / RAG", AX["검색·RAG"]), ("Segmentation", AX["분할"]),
 ("Reasoning technique", AX["추론 기법 (CoT/RL/GRPO/DPO)"]), ("Reasoning any", AX["추론 언급 (bare, 어휘)"]), ("Efficiency concept", AX["경량화·효율"]),
 ("CLIP family", AX["도메인 사전학습 (CLIP계)"]), ("Agents", AX["에이전트·도구 사용"]), ("Instruction data", AX["명령어 튜닝·데이터 구축"]), ("LLaVA fine-tuning", AX["범용 VLM 파인튜닝 (LLaVA계)"]),
 ("Reliability vocabulary", AX["신뢰성 어휘 (넓게)"]), ("Hallucination explicit", AX["환각 (명시적)"]), ("Clinical-validation vocabulary", AX["임상 검증·실사용"]),
 ("Explainability", AX["설명가능성"]), ("Regulation / ethics", AX["규제·윤리"]),
]
def norm_sf(z):  # 표준정규 상단 꼬리
    return 0.5 * math.erfc(z / math.sqrt(2))
def cochran_armitage(counts, totals, scores=(0, 1, 2)):
    """양측 p. counts[i]=해당 연도 양성 수, totals[i]=연도 논문 수."""
    N = sum(totals); R = sum(counts)
    if R == 0 or R == N: return float("nan"), float("nan")
    t = sum(s * c for s, c in zip(scores, counts)); e = R * sum(s * n for s, n in zip(scores, totals)) / N
    sbar = sum(s * n for s, n in zip(scores, totals)) / N
    var = R * (N - R) / N * sum(n * (s - sbar) ** 2 for s, n in zip(scores, totals)) / (N - 1)
    z = (t - e) / math.sqrt(var); return z, 2 * norm_sf(abs(z))
yr = lambda p: p["date"][:4]
N = collections.Counter(yr(p) for p in med)
h1 = [p for p in med if not (p["date"].startswith("2026") and p["date"][5:7] > "06")]
N1 = collections.Counter(yr(p) for p in h1)
alpha = 0.05 / 24
print(f"N: 2024 {N['2024']}  2025 {N['2025']}  2026(1-8) {N['2026']}  2026(1-6) {N1['2026']}   Bonferroni α={alpha:.4f}\n")
print(f"{'branch':32} {'n':>4} {'Δ24-26':>7} {'p_Fisher':>9} {'CA_z':>6} {'p_trend':>9} | {'Δ(1-6)':>7} {'p(1-6)':>8}  keep?")
out = []
for name, pat in ROWS:
    r = re.compile(pat, re.I)
    c = collections.Counter(yr(p) for p in med if r.search(p["title"] + " " + p["abstract"]))
    c1 = collections.Counter(yr(p) for p in h1 if r.search(p["title"] + " " + p["abstract"]))
    a, b = c["2024"], c["2026"]; pf = fisher_exact([[a, N["2024"] - a], [b, N["2026"] - b]])[1]
    d = 100 * b / N["2026"] - 100 * a / N["2024"]
    z, pt = cochran_armitage([c["2024"], c["2025"], c["2026"]], [N["2024"], N["2025"], N["2026"]])
    b1 = c1["2026"]; pf1 = fisher_exact([[a, N["2024"] - a], [b1, N1["2026"] - b1]])[1]; d1 = 100 * b1 / N1["2026"] - 100 * a / N["2024"]
    sig, sig1, sigt = pf < alpha, pf1 < alpha, pt < alpha
    keep = ("**" if sig else "  ") + ("→**" if sig1 else "→  ") + (" T**" if sigt else " T  ")
    print(f"{name:32} {sum(c.values()):4d} {d:+7.1f} {pf:9.2e} {z:6.2f} {pt:9.2e} | {d1:+7.1f} {pf1:8.2e}  {keep}")
    out.append((name, sig, sig1, sigt, d, d1))
s = [o for o in out if o[1]]; s1 = [o for o in out if o[2]]; st = [o for o in out if o[3]]
print(f"\nBonferroni 유의: Fisher 2024-26 {len(s)}개 | 2026 1-6월 {len(s1)}개 | 추세검정 {len(st)}개")
print("Fisher 유의 6개가 1-6월에서도 유의?:", [(o[0], o[2]) for o in s])
print("추세검정 유의:", [o[0] for o in st])
print("Δ 부호 뒤집힘(1-8 vs 1-6):", [o[0] for o in out if (o[4] > 0) != (o[5] > 0) and abs(o[4]) > 1])
