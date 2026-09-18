# Full-text efficiency audit rubric (144 efficiency-oriented papers, 2026-09-14)

Purpose: extend Table II from the abstract level to the full-text level. For each paper and each quantity, judge only whether the body (tables, figures, sentences) reports a value that **the authors measured for their own system**.

## Quantities
| Code | Quantity | Counts as Y | Does not count |
|---|---|---|---|
| LAT | Latency / time | inference or training time of the authors' own model (ms or s per image, speed-up factors from their own experiments) | values cited from other papers; adjectives such as "real-time"; number of training epochs |
| HW | Target hardware | GPU/CPU/edge device used in the authors' experiments | devices mentioned in related work |
| FLOP | Compute | FLOPs or MACs of the authors' own model | the concept only |
| MEM | Memory | GPU memory / VRAM / footprint of the authors' own model | dataset size; model file size (bit-width alone counts as MEM only if a footprint is given) |
| ENG | Energy / power | measured W, J, mWh, power or carbon of the authors' own system | "energy-efficient" as an adjective; battery mentioned only |
| THR | Throughput | samples/s, QPS, fps of the authors' own model | — |
| PAR | (auxiliary) Parameters | total / active / trainable parameter counts | — |

## Values
- `Y` the body reports the authors' own measurement (supporting sentence required)
- `A` reported in the abstract only, nothing further in the body (same as the abstract-level audit)
- `N` not reported
- `?` unreadable (PDF conversion failure, number only inside a figure) → resolved to Y/N after checking the page

## Section rules
- Ignore everything after References. Sentences in Related Work / Background describe other papers and do **not** count, unless the subject is "we"/"our" and the authors' own model is named.
- Numbers in tables are assigned by caption and column name (e.g., a "Time (s)" column → LAT).

## Outputs
- `audit.csv`: id, title, LAT, HW, FLOP, MEM, ENG, THR, PAR, any_Y, note (plus LAT_infer, the inference-side split)
- `audit.jsonl`: one line per paper with the supporting sentence for each Y
- Verification sample: 30 papers stratified by any_Y (15 with / 15 without), all 180 judgments checked by the first author against the stored sentences (`validation_human.json`, `validation_kappa.json`)
