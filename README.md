# The Changing Landscape of Medical Vision-Language Models — Supplementary Material

Supplementary material for: Youchan Jee, Woojae Kim, Hoyeon Ahn, "The Changing Landscape of Medical Vision-Language Models: A Quantitative Survey of 1,217 arXiv Papers, 2024–2026", ICT4sHealth 2026.

Repository: https://github.com/fofifafo/medical-vlm-landscape-2026

## Contents
- `Supplementary_Material.pdf` — S1 arXiv queries, S2 VLM screen, S3 medical filter, S4 taxonomy patterns, S5 strict definitions, S6 efficiency-oriented set, S7 judging model, S8 classification-validation criteria, S9 sampling, S10 efficiency-audit rubric, S11 judging procedure, S12 Table II partition.
- `code/` — `arxiv_scrape.py` (22 queries, controlled vocabulary), `medical_taxonomy.py` (medical filter, 39 tag patterns), `strict_tags.py` (strict definitions, Fisher exact test), `trend_tests.py` (Cochran–Armitage trend test, Jan–Jun 2026 sensitivity), `extract_candidates.py` / `summarize.py` (full-text efficiency audit), `class_agreement.py`, `validation_kappa.py`.
- `data/medical_vlm_corpus_1217.csv` — the 1,217 medical VLM papers (arXiv id, date, title) with one column per tag (1 = pattern matched title + abstract). Abstracts are not redistributed; fetch them by arXiv id.
- `validation/` — classification validation (`class_tags_guide.md` criteria, `class_sample.csv` 150-paper sample, `class_judgments_claude.txt` judgments, `class_agreement.csv`, `class_disagreements.md`); efficiency audit (`RUBRIC.md`, `audit.jsonl` one line per paper with evidence sentences, `audit.csv`, `evidence.md`); 30-paper verification (`validation_human.json`, `validation_kappa.json`); corpus-inclusion validation (`inclusion_sample_judgments.csv`, `inclusion_human_final.json`, `inclusion_validation_result.md`).

## Reproducing the counts
`python code/medical_taxonomy.py` prints the yearly tag counts behind Table I (requires the cached arXiv records produced by `arxiv_scrape.py`). `python code/strict_tags.py` and `python code/trend_tests.py` print the strict-tag counts, Fisher p-values, trend tests, and the sensitivity analysis.

## License
Code: MIT. Data and documents: CC BY 4.0. arXiv metadata is used under the arXiv API terms of use.
