# Corpus-inclusion validation (2026-09-18)

Sample: 100 papers included by the medical filter (33/33/34 by year) and 50 boundary exclusions (VLM-relevant records with exactly one clinical-term match in the abstract), seed 20260918. Question: "Is this a medical vision-language-model paper?" (O/X). Judged by the first author; disagreements with the rule were adjudicated against the written criterion (medical or clinical imaging/data as the main subject; papers that mention medicine only as one application domain are X). Final judgments: `inclusion_human_final.json`, `inclusion_sample_judgments.csv`.

Result: TP 99, FP 1, FN 5, TN 45. Inclusion precision 0.990, agreement 0.960, kappa 0.908.
False inclusion: #62 (2410.03551, constructive-apraxia analogy). Boundary exclusions judged medical: #18 IOSVLM, #60 CORE-Seg, #105 I2ddPCR, #121 CardiacCLIP, #142 disease-informed adaptation.
