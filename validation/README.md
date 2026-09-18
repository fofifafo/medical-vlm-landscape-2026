# Validation files

| File | What it is |
|---|---|
| `class_tags_guide.md` | Criteria for the 12 validated tags and the loose regex of the rule-based classifier |
| `class_sample_judgments.csv` | 150-paper stratified sample (50 per year, seed 20260915): rule tags and criterion-based (Claude Opus 5) judgments per tag |
| `class_judgments_claude.txt` | The same criterion-based judgments as 12-character O/X strings |
| `class_agreement.csv`, `class_disagreements.md` | Per-tag precision/recall/kappa of the rule against the criterion-based reading, and the 130 disagreeing cells |
| `RUBRIC.md` | Full-text efficiency-audit rubric (six quantities; only the authors' own measurements count) |
| `audit.jsonl`, `audit.csv`, `evidence.md` | Per-paper audit results for the 144 efficiency-oriented papers with supporting sentences |
| `validation_human.json`, `validation_kappa.json` | First-author check of all 180 judgments in a 30-paper stratified sample against the stored sentences (a verification of the recorded evidence, not an independent blind rating; no judgment was overturned) |
| `inclusion_sample_judgments.csv`, `inclusion_human_final.json`, `inclusion_validation_result.md` | Corpus-inclusion validation: 100 included + 50 boundary-excluded papers judged by the first author |
