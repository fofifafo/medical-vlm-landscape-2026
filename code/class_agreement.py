"""규칙(정규식) 판정 vs Claude 초록 판독 판정 비교: 태그별 P/R/F1/κ (150편)."""
import csv, json, os
ROOT=os.path.dirname(os.path.abspath(__file__))
J={}
for l in open(os.path.join(ROOT,"class_judgments_claude.txt"),encoding="utf-8"):
    if l.startswith("#") or not l.strip(): continue
    n,s=l.split(); assert len(s)==12, (n,s); J[int(n)]=s
rows=list(csv.DictReader(open(os.path.join(ROOT,"class_sample.csv"),encoding="utf-8-sig")))
assert len(rows)==150 and len(J)==150
tags=[k[3:] for k in rows[0].keys() if k.startswith("규칙 ")]
out=[]; tot=dict(tp=0,fp=0,fn=0,tn=0)
for j,t in enumerate(tags):
    tp=fp=fn=tn=0
    for r in rows:
        n=int(r["#"]); rule=r["규칙 "+t]=="O"; hum=J[n][j]=="O"
        if rule and hum: tp+=1
        elif rule and not hum: fp+=1
        elif hum and not rule: fn+=1
        else: tn+=1
    N=tp+fp+fn+tn; po=(tp+tn)/N; pe=((tp+fp)*(tp+fn)+(fn+tn)*(fp+tn))/N**2
    k=(po-pe)/(1-pe) if pe<1 else 1.0
    P=tp/(tp+fp) if tp+fp else float("nan"); R=tp/(tp+fn) if tp+fn else float("nan")
    F=2*P*R/(P+R) if (tp+fp and tp+fn and P+R) else float("nan")
    out.append(dict(tag=t,rule_pos=tp+fp,claude_pos=tp+fn,tp=tp,fp=fp,fn=fn,tn=tn,P=P,R=R,F1=F,kappa=k,agree=po))
    for kk,v in zip(("tp","fp","fn","tn"),(tp,fp,fn,tn)): tot[kk]+=v
N=sum(tot.values()); po=(tot["tp"]+tot["tn"])/N
pe=((tot["tp"]+tot["fp"])*(tot["tp"]+tot["fn"])+(tot["fn"]+tot["tn"])*(tot["fp"]+tot["tn"]))/N**2
Pm=tot["tp"]/(tot["tp"]+tot["fp"]); Rm=tot["tp"]/(tot["tp"]+tot["fn"])
print(f"{'tag':22s} rule  claude  TP  FP  FN   P     R     F1    kappa")
for o in out: print(f"{o['tag']:22s} {o['rule_pos']:4d} {o['claude_pos']:6d} {o['tp']:3d} {o['fp']:3d} {o['fn']:3d}  {o['P']:.2f}  {o['R']:.2f}  {o['F1']:.2f}  {o['kappa']:.2f}")
print(f"pooled (1800 decisions): agree={po:.3f} kappa={(po-pe)/(1-pe):.3f} microP={Pm:.3f} microR={Rm:.3f} microF1={2*Pm*Rm/(Pm+Rm):.3f}")
with open(os.path.join(ROOT,"class_agreement.csv"),"w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
# 불일치 목록
with open(os.path.join(ROOT,"class_disagreements.md"),"w",encoding="utf-8") as f:
    f.write("# 규칙 vs Claude 불일치 (150편 x 12태그)\n\n| # | arXiv | 태그 | 규칙 | Claude |\n|---|---|---|---|---|\n")
    for r in rows:
        n=int(r["#"])
        for j,t in enumerate(tags):
            rule=r["규칙 "+t]; hum=J[n][j]
            if rule!=hum: f.write(f"| {n} | {r['arXiv ID']} | {t} | {rule} | {hum} |\n")
