# 분류 검증 12개 태그 판정 안내

| 태그 | 판정 기준 | 규칙(정규식) |
|---|---|---|
| 흉부 X선 | 논문이 흉부 X선(CXR/radiograph)을 다루는가 | `chest x-?ray|\bCXR\b|radiograph|x-?ray` |
| CT/MRI (3D) | 논문이 CT 또는 MRI 볼륨을 다루는가 | `\bCT\b|\bMRI\b|volumetric|3D medical|computed tomography|magnetic resonance` |
| 병리/WSI | 병리 슬라이드·조직 영상을 다루는가 | `patholog|histolog|whole[- ]slide|\bWSI\b|biopsy` |
| 내시경·수술 영상 | 내시경 또는 수술 영상을 다루는가 | `endoscop|surgical (video|scene)|laparoscop|surgery video|colonoscop` |
| 판독문 생성 | 판독문(report) 생성이 과제인가 | `report generation|radiology report|generate (a |the )?report|report writing` |
| 그라운딩·병변 위치 | 병변 위치 추정/그라운딩이 실제 과제·기여인가 (단어만 나오면 X) | `lesion detection|grounding|localiz|bounding box|abnormality detection` |
| 임상 의사결정·추론 | 임상 의사결정 지원/감별진단이 과제인가 | `clinical (decision|reasoning)|differential diagnosis|treatment (plan|recommend)|triage` |
| 추론 기법 (CoT/RL) | CoT·강화학습·GRPO/DPO 같은 구체 추론 기법을 쓰는가 | `chain[- ]of[- ]thought|reinforcement learning|\bRL\b|\bGRPO\b|\bDPO\b|\bRLHF\b|R1[- ]style|reasoning (model|trace|chain)` |
| 에이전트·도구 사용 | 에이전트 설계 또는 도구 호출을 쓰는가 | `\bagent|tool[- ]use|tool[- ]calling|multi[- ]agent` |
| 효율 기법 | 경량화·양자화·LoRA 등 효율 기법을 실제로 쓰는가 (형용사 'efficient'만이면 X) | `efficien|lightweight|quantiz|distill|\bLoRA\b|parameter[- ]efficient|on[- ]device|token (prun|compress)` |
| 환각 명시 | 환각(hallucination)을 명시적으로 다루는가 | `hallucinat` |
| 임상 검증·실사용 | 임상의 평가·전향적 검증·실제 배포를 보고하는가 (희망 서술만이면 X) | `clinical (validation|trial|deployment|practice)|real[- ]world|prospective|reader study|radiologist(s)? (evaluat|rat|prefer)` |
