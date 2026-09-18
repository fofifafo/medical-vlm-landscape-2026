# Classification-validation criteria (12 tags)

A tag is credited only when the paper actually performs the activity; the loose regex used by the rule-based classifier is shown for comparison. Judged on title + abstract.

| Tag | Criterion (credit only if the paper does this) | Rule regex (case-insensitive) |
|---|---|---|
| chest_xray | the paper works on chest X-rays (CXR / radiographs) | `chest x-?ray|\bCXR\b|radiograph|x-?ray` |
| ct_mri_3d | the paper works on CT or MRI volumes | `\bCT\b|\bMRI\b|volumetric|3D medical|computed tomography|magnetic resonance` |
| pathology_wsi | the paper works on pathology slides / tissue images | `patholog|histolog|whole[- ]slide|\bWSI\b|biopsy` |
| endoscopy_surgical | the paper works on endoscopic or surgical video/images | `endoscop|surgical (video|scene)|laparoscop|surgery video|colonoscop` |
| report_generation | report generation is a task of the paper | `report generation|radiology report|generate (a |the )?report|report writing` |
| grounding_localization | lesion localization / grounding is an actual task or contribution (the word alone does not count) | `lesion detection|grounding|localiz|bounding box|abnormality detection` |
| clinical_decision | clinical decision support or differential diagnosis is a task of the paper | `clinical (decision|reasoning)|differential diagnosis|treatment (plan|recommend)|triage` |
| reasoning_technique | a concrete reasoning technique is used: CoT, reinforcement learning, GRPO/DPO | `chain[- ]of[- ]thought|reinforcement learning|\bRL\b|\bGRPO\b|\bDPO\b|\bRLHF\b|R1[- ]style|reasoning (model|trace|chain)` |
| agents_tool_use | an agent design or tool calling is used | `\bagent|tool[- ]use|tool[- ]calling|multi[- ]agent` |
| efficiency_technique | an efficiency technique (compression, quantization, LoRA, ...) is actually applied (the adjective 'efficient' alone does not count) | `efficien|lightweight|quantiz|distill|\bLoRA\b|parameter[- ]efficient|on[- ]device|token (prun|compress)` |
| hallucination_explicit | hallucination is addressed explicitly | `hallucinat` |
| clinical_validation | the paper reports a clinician evaluation, prospective validation, or real-world deployment (statements of intent do not count) | `clinical (validation|trial|deployment|practice)|real[- ]world|prospective|reader study|radiologist(s)? (evaluat|rat|prefer)` |

Key distinction: the presence of a word is not the same as doing the thing. 'grounded reasoning' without any localization → grounding X; 'efficient' without a compression technique → efficiency X; 'needed for real-world deployment' without an evaluation → clinical_validation X. A paper may carry several tags.
