# 효율 144편 전문 판정 근거 (2026-09-14, 판정: Claude, 규칙: RUBRIC.md)

## 2502.09838 — HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - PAR: HealthGPT-M3, with only 3.8B parameters … HealthGPT-L14 with a similar number of trainable parameters (experiments)
  - note: energy hits are LoRA weight-matrix W symbols; no hardware/time stated in body

## 2503.20047 — Med3DVLM: An Efficient Vision-Language Model for 3D Medical Image Analysis
- LAT N (infer N, train N) · HW Y · FLOP Y · MEM N · ENG N · THR N · PAR Y
  - HW: 8 NVIDIA A100 80GB GPUs (implementation details)
  - FLOP: vision backbone 87.4M params/253.23G FLOPs → 18.2M/21.59G FLOPs; Table 12 per-module FLOPs
  - PAR: Table 12 params
  - note: authors explicitly state they do NOT report inference time or memory

## 2405.10948 — Surgical-LVLM: Learning to Adapt Large Vision-Language Model for Grounded Visual Question Answering in Robotic Surgery
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: conducted on a server with NVIDIA A100 GPUs (implementation details)

## 2411.15232 — BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A100 GPU (40GB) (implementation details)
  - note: 40GB is GPU spec, not measured footprint → MEM N; energy hits are batch-size symbols

## 2410.15074 — LLaVA-Ultra: Large Chinese Language and Vision Assistant for Ultrasound
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: Trained in only 60 hours with 4 48GB A40s (training time, own model)
  - HW: 4 48GB NVIDIA A40s (experiment)
  - note: training time only; no inference latency

## 2401.02797 — PeFoMed: Parameter Efficient Fine-tuning of Multimodal Large Language Models for Medical Imaging
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: 4 NVIDIA Tesla A40 GPUs, 48GB each (implementation details)
  - PAR: trainable parameters 56.63M vs LLaVA-Med 7B (evaluation); Table with trainable-parameter column

## 2505.03981 — X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: SFT 8 hours on 8×A100; RLVR ~56 hours on 32×A100 (training time)
  - HW: 8 / 32 40GB A100 GPUs
  - PAR: model size limited to 7B parameters
  - note: training time only

## 2503.00908 — Patient-Level Anatomy Meets Scanning-Level Physics: Personalized Federated Low-Dose CT Denoising Empowered by Large Language Model
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: AMD Ryzen 7 5800X CPU and one NVIDIA GTX 3080 Ti GPU (experiments)
  - note: federated LDCT denoising; no timing

## 2406.13173 — Biomedical Visual Instruction Tuning with Clinician Preference Alignment
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 2 NVIDIA A100 GPUs (experiments)
  - note: energy hits are sample-weight symbol w

## 2412.13558 — Read Like a Radiologist: Efficient Vision-Language Model for 3D Medical Imaging Interpretation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: eight NVIDIA A100 (40GB) GPUs for CT-RATE; single A100 for rectal MRI (implementation details)
  - note: 'Efficient' in title refers to token/slice handling; no timing/memory numbers in body; fps hit is a generic video example

## 2403.06407 — Can LLMs' Tuning Methods Work in Medical Multimodal Domain?
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - PAR: can reduce the parameter count by 40% while maintaining performance (experiment)
  - note: relative parameter reduction only

## 2504.14692 — OmniV-Med: Scaling Medical Vision-Language Model for Universal Visual Understanding
- LAT N (infer N, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - HW: 8× RTX 3090 GPUs for training; 7B version supports inference on a single RTX 3090 (ablation)
  - MEM: Training the OmniV-Med-1.5B model requires less than 24GB of GPU memory (ablation)
  - PAR: OmniV-Med-1.5B / 7B
  - note: 'efficient long-video inference' claimed but no latency number

## 2409.00084 — Vision-Language and Large Language Model Performance in Gastroenterology: GPT, Claude, Llama, Phi, Mistral, Gemma, and Quantized Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - LAT: execution time measured from input to final token (time library); Supplementary Table S5 execution time and cost per execution
  - HW: laptop with RTX 3080 Ti (16 GB VRAM), Core i9-12900, 32 GB RAM
  - MEM: 13B/70B models demand approximately 52 GB and 280 GB of memory
  - PAR: 13B / 70B
  - note: energy mentioned only qualitatively ('reduces energy consumption' via quantization) → ENG N

## 2410.23822 — Parameter-Efficient Fine-Tuning Medical Multimodal Large Language Models for Medical Visual Grounding
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: four NVIDIA Tesla A40 GPUs (experiments)

## 2603.01143 — TC-SSA: Token Compression via Semantic Slot Aggregation for Gigapixel Pathology Reasoning
- LAT N (infer N, train N) · HW Y · FLOP Y · MEM N · ENG N · THR N · PAR N
  - HW: 2×A6000 GPUs instead of 8×A100 (experiments)
  - FLOP: Table 1: Flops column, SlideChat 133.3T vs token-compressed ~60× (own model)
  - note: FLOPs is the headline efficiency metric

## 2404.14755 — SkinGEN: an Explainable Dermatology Diagnosis-to-Generation Framework with Interactive Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: Intel Core i7 + NVIDIA 3090Ti for training; only one NVIDIA 3090 necessary for inference
  - note: no timing numbers

## 2406.02601 — Multimodal Deep Learning for Low-Resource Settings: A Vector Embedding Alignment Approach for Healthcare Applications
- LAT Y (infer Y, train Y) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR N
  - LAT: Table 3 training and inference times per epoch [s] across datasets (e.g., 1.54 / 0.40 s)
  - HW: Oracle Standard.E4.Flex, 2 CPU cores, 64GB each, no GPU (low-resource setting)
  - MEM: memory usage computed per batch/model; memory footprints compared across approaches
  - note: energy only qualitative ('minimizing the energy … requirements') → ENG N; CPU-only deployment study

## 2406.07146 — Argus: Benchmarking and Enhancing Vision-Language Models for 3D Radiology Report Generation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: eight A100-80G GPUs (appendix B)
  - PAR: 3B / 8B / 70B

## 2506.06600 — RARL: Improving Medical VLM Reasoning and Generalization with Reinforcement Learning and LoRA under Data and Hardware Constraints
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: single NVIDIA A100-PCIE-40GB GPU (training)
  - PAR: Qwen2-VL-2B; LoRA r=8
  - note: 'feasibility of deploying in constrained environments' claimed from single-GPU training only

## 2412.14424 — FedPIA -- Permuting and Integrating Adapters leveraging Wasserstein Barycenters for Finetuning Foundation Models in Multi-Modal Federated Learning
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: FedPIA: no hardware/time/memory numbers found in body; energy hits are weight symbols W

## 2603.25155 — Photon: Speedup Volume Understanding with Efficient Multimodal Large Language Models
- LAT Y (infer Y, train Y) · HW N · FLOP N · MEM Y · ENG N · THR Y · PAR Y
  - LAT: training time 21.5H → 4H, inference 2.8H → 1.5H (figure 1)
  - MEM: GPU memory 134.2GiB/128.9GiB → 34.8GiB (train), 26.0GiB → 9.2GiB (inference); Table 3 GiB column
  - THR: up to 4.12 tokens/s (Table 3)
  - PAR: Photon-3B / 32B
  - note: GPU model not named in extracted text → HW N (recheck if needed)

## 2508.10054 — SurgPub-Video: A Comprehensive Surgical Video Dataset for Enhanced Surgical Intelligence in Vision-Language Model
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: 4 NVIDIA A40 GPUs
  - PAR: SurgLLaVA-Video 3B

## 2506.23903 — Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: Table VII: 0.33 s per image vs BiomedParse 0.49 s, SAMUS 0.67 s, MedCLIP-SAM 3.05 s; runtimes on TITAN V
  - HW: RTX 4090 (24 GB) for training; NVIDIA Titan V (12 GB) for inference benchmark
  - PAR: ≈1.7% of trainable parameters (LoRA)
  - note: 12/24 GB are GPU specs, not measured footprint → MEM N

## 2604.08203 — MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: Table 8: average inference latency on OmniMedVQA profiled on H20 GPUs; zoom-in tool overhead 1.5% of total inference time
  - HW: 32 H20 GPUs (training); H20 for latency profiling
  - PAR: Qwen2.5-VL-7B

## 2505.05189 — Biomed-DPT: Dual Modality Prompt Tuning for Biomedical Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: three RTX 4090 GPUs (24 GB RAM each) (experiments)
  - note: energy hits are text-embedding symbol W

## 2507.07902 — MIRA: A Novel Framework for Fusing Modalities in Medical RAG
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: 9× faster inference than 72B models (contribution claim; no absolute number or table found)
  - HW: NVIDIA A100 GPUs (implementation details)
  - note: LAT is a relative speed-up claim only; borderline

## 2601.16549 — LLM is Not All You Need: A Systematic Evaluation of ML vs. Foundation Models for text and image based Medical Classification
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: states VLM 'latency and carbon cost … orders of magnitude higher' qualitatively; no measured value → all N. Closest any paper comes to energy

## 2509.01554 — Unified Supervision For Vision-Language Modeling in 3D Computed Tomography
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: most experiments were done in 24 hours (training time)
  - HW: single H100 GPU (appendix)
  - note: training time only

## 2502.14149 — PitVQA++: Vector Matrix-Low-Rank Adaptation for Open-Ended Visual Question Answering in Pituitary Surgery
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA RTX A6000 GPU
  - note: memory hit is QLoRA description (related work); fps hit is frame extraction rate

## 2501.19086 — Fairness Analysis of CLIP-Based Foundation Models for X-Ray Image Classification
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA GTX 1080Ti GPU
  - note: fairness study; no efficiency numbers

## 2507.14497 — Efficient Whole Slide Pathology VQA via Token Compression
- LAT N (infer N, train N) · HW Y · FLOP Y · MEM N · ENG N · THR Y · PAR N
  - HW: NVIDIA A6000 (48G) GPUs; throughput on a single A6000
  - FLOP: average 10.87 TFLOPS vs 2.35 TFLOPS for SlideChat (Tab. 2) — utilization, not model FLOPs
  - THR: Table: training throughput 179.46 vs 0.42 samples/sec; inference 3.33 vs 0.58 samples/sec
  - note: 'significantly lower training and inference times' stated but only throughput numbers given → LAT N, THR Y

## 2601.21617 — PathReasoner-R1: Instilling Structured Reasoning into Pathology Vision-Language Model via Knowledge-Guided Policy Optimization
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 8 × NVIDIA RTX 4090 48GB GPUs (appendix B.3)

## 2512.05391 — LoC-Path: Learning to Compress for Pathology Multimodal Large Language Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR N
  - LAT: Tab. 4(b): ms/step 1288 vs LLaVA 1520 / SlideChat 2546 on RTX A6000 Ada; Fig. 5 TTFT vs visual token length
  - HW: 4 Ada RTX A6000 GPUs; profiling on RTX A6000 Ada
  - MEM: peak reserved memory 19.36 GB vs 21.23 / 43.75 GB (Tab. 4b); prefill memory in Fig. 5
  - note: one of the most complete efficiency reports

## 2603.21010 — SkinCLIP-VL: Consistency-Aware Vision-Language Learning for Multimodal Skin Cancer Diagnosis
- LAT N (infer N, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - HW: single NVIDIA A100 (80GB)
  - MEM: reduce training memory requirements by 43% compared to full finetuning (relative only)
  - PAR: trainable parameters reduced ≈43%; 4.3B
  - note: MEM is relative reduction without absolute value; counted Y as own measurement

## 2511.07929 — Federated CLIP for Resource-Efficient Heterogeneous Medical Image Classification
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR N
  - LAT: 120× faster than FedAVG; FedAVG 95.58 min vs FedAPT 72.495 min vs ours 68.56 min (ISIC2019); BraTS 2.85 vs 3.36 min
  - HW: Intel 13900KF CPU, 128 GB RAM, RTX 4090 GPU
  - MEM: communication load 7.569 GB vs 0.063 GB; compressed model 1.36 MB
  - note: federated; 'resource cost' = time + communication volume

## 2509.09397 — Decoupling Clinical and Class-Agnostic Features for Reliable Few-Shot Adaptation under Shift
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A100 GPU

## 2501.15370 — Scaling Large Vision-Language Models for Enhanced Multimodal Comprehension In Biomedical Image Analysis
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: compute node with 4 A40G GPUs
  - note: 'significant runtime acceleration' and memory optimizations described without numbers

## 2601.20323 — ECG-Agent: On-Device Tool-Calling Agent for ECG Multi-Turn Dialogue
- LAT N (infer N, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - HW: RTX A6000s (1B/3B/8B), A100s (32B) — server GPUs, not the target smartphone
  - MEM: 4-bit quantized 3B model requires ≈2GB; 8B demands 5–6GB vs smartphone RAM 6–8GB
  - PAR: 1B/3B/8B/32B; on-device <4B
  - note: title says On-Device but no measured latency on a phone; memory figures are estimates

## 2604.09450 — ECHO: Efficient Chest X-ray Report Generation with One-step Block Diffusion
- LAT Y (infer Y, train N) · HW N · FLOP N · MEM N · ENG N · THR Y · PAR N
  - LAT: up to 8× theoretical and 5.1× practical inference speedup; 390% speedup at block size 8 (own experiments)
  - THR: Table 1 TPF/TPS columns (tokens per forward pass, tokens per second)
  - note: GPU model for TPS not found in extracted text → HW N; efficiency is the paper's headline

## 2601.10949 — MMedExpert-R1: Strengthening Multimodal Medical Reasoning via Domain-Specific Adaptation and Clinical Guideline Reinforcement
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: training on ~1,000 samples requires only ≈0.4 hours on a single A100 (deployment-feasibility estimate)
  - HW: single NVIDIA A100 GPU
  - PAR: 2B / 7B
  - note: training time only

## 2509.15482 — Comparing Computational Pathology Foundation Models using Representational Similarity Analysis
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: representational-similarity analysis; no hardware or efficiency numbers

## 2508.11673 — Contrastive Regularization over LoRA for Multimodal Biomedical Image Incremental Learning
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: each experiment roughly 20 GPU hours, ~500 GPU hours total (training)
  - HW: 8 A6000 GPUs (48GB each)
  - note: training compute only; energy hits are LoRA weight symbols

## 2507.22802 — Advancing Fetal Ultrasound Image Quality Assessment in Low-Resource Settings
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA RTX 4090 GPU
  - note: 'low-resource settings' in title refers to clinical setting, not compute

## 2505.16647 — Point, Detect, Count: Multi-Task Medical Image Understanding with Instruction-Tuned Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A100 80GB

## 2502.05928 — ClinKD: Cross-Modal Clinical Knowledge Distiller For Multi-Task Medical Images
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: distillation paper; no hardware/time/memory numbers found

## 2606.08641 — Learnable Token Sparsification for Efficient Gigapixel Whole Slide Image Reasoning
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: two NVIDIA A6000 GPUs
  - note: claims 'no extra computation'/'zero computational latency' qualitatively; token count 32 given but no time

## 2604.01310 — Sparse Spectral LoRA: Routed Experts for Medical VLMs
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - LAT: Table 6 Epoch Time 29h15min / 29h17min / 29h19min on one A100 (training)
  - HW: one A100 GPU
  - MEM: Table 6 Memory Usage 32.56 GB / 32.47 GB / 32.56 GB
  - PAR: Params(%) 0.96 / 0.84; 339× fewer trainable parameters
  - note: FLOPs discussed analytically (big-O) not measured → FLOP N

## 2603.00148 — Mechanistically Guided LoRA Improves Paraphrase Consistency in Medical Vision-Language Models
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - PAR: 4.38M trainable parameters ≈0.10% of full model
  - note: no hardware stated in extracted text

## 2512.18554 — Enhancing Medical Large Vision-Language Models via Alignment Distillation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: four NVIDIA A6000 GPUs
  - note: energy hits are rotation-matrix W

## 2512.13072 — Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 4-NVIDIA A6000 GPU workstation

## 2511.09540 — vMFCoOp: Towards Equilibrium on a Unified Hyperspherical Manifold for Prompting Biomedical VLMs
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: NVIDIA A100 GPU (80GB)

## 2503.19670 — fine-CLIP: Enhancing Zero-Shot Fine-Grained Surgical Action Recognition with Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: single NVIDIA A100 GPU
  - PAR: 3.019M trainable parameters

## 2411.19688 — SURE-VQA: Systematic Understanding of Robustness Evaluation in Medical VQA Tasks
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: robustness benchmark; no hardware/efficiency numbers

## 2507.21976 — Compression Strategies for Efficient Multimodal LLMs in Medical Contexts
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - LAT: Table 4 Latency (ms/token): 154 → 122; 4.2× inference speedup on NVIDIA T4
  - HW: Kaggle T4 GPUs
  - MEM: Table 4 VRAM (GB): 13.4 → 3.9; 70% reduction
  - PAR: 7.06B → 5.85B, bit width 16 → 4
  - note: most complete deployment-oriented report; no energy

## 2607.23794 — PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: no hardware or efficiency numbers in extracted text

## 2607.23631 — PathSelect: Sequential Token Selection for Whole Slide Pathology
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A6000 GPU

## 2607.16303 — Med-OPD: Improving Medical Vision-Language Models via Evidence-Aware On-Policy Distillation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: AMD server with four MI308 GPUs, 192GB each

## 2607.03647 — Do Medical Vision Language Models Actually See? A Counterfactual Grounding Framework and Hard-Negative Contrastive Training for Visually-Reliant Medical VLMs
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 4×80 GB H100s (training); H100 (evaluation)
  - note: steps given, no wall time

## 2604.04133 — Learning Robust Visual Features in Computed Tomography Enables Efficient Transfer Learning for Clinical Tasks
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: eight L40S GPUs (48GB)
  - note: 'largest feasible with our hardware' — memory as constraint, no measured footprint

## 2603.19957 — HiPath: Hierarchical Vision-Language Alignment for Structured Pathology Report Prediction
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: feature pre-extraction ∼120 GPU-h (H100); training ∼5.6 h on 4×H100
  - HW: 4×H100
  - PAR: 15.0 M trainable (HiPA 5.2 M, HiCL 4.1 M, Slot-MDP 5.7 M)
  - note: training time only

## 2603.17079 — ACE-LoRA: Graph-Attentive Context Enhancement for Parameter-Efficient Adaptation of Medical Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: three RTX 3090 GPUs
  - PAR: 0.95M trainable parameters (0.48% of full FT; backbone ~197M)

## 2602.22098 — Brain3D: Brain Report Automation via Inflated Vision Transformers in 3D
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A100 (64GB VRAM)

## 2601.16895 — Evaluating Large Vision-language Models for Surgical Tool Detection
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: NVIDIA A100 (40GB) GPU
  - PAR: 7B / 8B models evaluated
  - note: fps hit is frame extraction

## 2601.14406 — Large-Scale Label Quality Assessment for Medical Segmentation via a Vision-Language Judge and Synthetic Data
- LAT Y (infer Y, train Y) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR N
  - LAT: assesses a 3D label in 0.06 s on an RTX A6000; Table 3 Time [s/label]
  - HW: Intel Xeon Gold 5218R + 8 RTX A6000; single A6000 for timing
  - MEM: Table 3 RAM [GB] and Disk [GB] columns
  - note: efficiency table with time/RAM/disk

## 2601.03915 — HemBLIP: A Vision-Language Model for Interpretable Leukemia Cell Morphology Analysis
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: no hardware/efficiency numbers found (HemBLIP)

## 2512.03477 — Fairness-Aware Fine-Tuning of Vision-Language Models for Medical Glaucoma Diagnosis
- LAT Y (infer N, train Y) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: training completes in approximately 2.5 hours per method
  - PAR: ~20M trainable (0.24% of 8.3B; 415× reduction)
  - note: GPU not named; 'limited GPU infrastructure' deployment claim rests on training time

## 2510.15418 — Fine-Tuning MedGemma for Clinical Captioning to Enhance Multimodal RAG over Malaysia CPGs
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: Azure instance with NVIDIA A100 GPUs (80 GiB)

## 2508.20830 — Estimating 2D Keypoints of Surgical Tools Using Vision-Language Models with Low-Rank Adaptation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - PAR: baselines 26.4M / +1M; 'fewer trainable parameters' comparison
  - note: no hardware or timing

## 2508.04572 — Knowledge to Sight: Reasoning over Visual Attributes via Knowledge Decomposition for Abnormality Grounding
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: 4×A100 GPUs
  - PAR: compact models 0.23B and 2B

## 2506.14451 — Adapting Lightweight Vision Language Models for Radiological Visual Question Answering
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: fine-tuning ~3 days (ROCO/MedPix), ~6 days (PMC-VQA), <5 hours (SLAKE) on one H100
  - HW: single NVIDIA H100 GPU
  - note: training time only; 'lightweight' refers to model size

## 2504.16181 — CLIP-IT: CLIP-based Pairing for Histology Images Classification
- LAT Y (infer Y, train N) · HW Y · FLOP Y · MEM N · ENG N · THR N · PAR N
  - LAT: latency 33.3 ms (unimodal), 43.1 ms CLIP-IT (+29%), 158.5 ms CONCH (+376%) on RTX A6000, batch=1
  - HW: RTX A6000
  - FLOP: 17 GFLOPs baseline, +0.001 GFLOPs CLIP-IT, 505 GFLOPs CONCH per forward pass
  - note: clean inference-side report

## 2606.13572 — ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: NVIDIA A100 80GB PCIe GPU

## 2601.02443 — Evaluating the Diagnostic Classification Ability of Multimodal Large Language Models: Insights from the Osteoarthritis Initiative
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: NVIDIA A800 GPU (80 GB) + Intel Xeon Gold 6348

## 2512.10750 — LDP: Parameter-Efficient Fine-Tuning of Multimodal LLM for Medical Report Generation
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - LAT: training time 1.8 hours vs FFT ~48 hours (est.)
  - HW: 4× RTX 4090; fits on a single 24GB RTX 4090
  - MEM: GPU VRAM (train) 24 GB vs ~120 GB (est.)
  - PAR: 8.4M (0.12%) vs 7.0B; 833× reduction
  - note: training-side table; FFT baseline is estimated, not measured

## 2506.09634 — HSENet: Hybrid Spatial Encoding Network for 3D Medical Vision-Language Understanding
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 8 RTX 3090 GPUs
  - note: energy hits are width symbols W

## 2608.30352 — Co-Annotator: Expert-Distilled ViT and VLM for Visual and Documentation Guidance in Age-Related Macular Degeneration
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: user-study paper; 'Correct Dx/min' is clinician throughput, not model throughput → THR N

## 2608.17926 — PerFact: Perception-Derived Fact Prompting for 3D Brain MRI Report Generation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: single NVIDIA GH200 96GB GPU
  - PAR: 3B to 32B

## 2608.14015 — MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: agent harness with proprietary orchestrator; 'cost' refers to accuracy points, no compute numbers

## 2608.09302 — Bootstrapping Vision-Language Model for Hysteroscopic Surgical Scene Segmentation
- LAT Y (infer Y, train N) · HW Y · FLOP Y · MEM Y · ENG N · THR Y · PAR Y
  - LAT: Table 13 inference time (FPS) on single A40
  - HW: 4 NVIDIA A40 (train); single A40 (evaluation)
  - FLOP: Table 13 FLOPs column
  - MEM: Table 13 Memory(GB) column
  - THR: FPS
  - PAR: Table 13 Params(M)
  - note: full computational-cost table (Sec. 5.8)

## 2608.00232 — Real-Time Visual Obstruction Detection in Surgical Augmented Reality
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: average end-to-end latency 479 ms; 62.90% latency reduction vs cloud baseline
  - HW: workstation with two NVIDIA RTX A6000 GPUs (edge server)
  - note: energy cost mentioned only as future-work motivation, not measured → ENG N; closest AR/edge paper

## 2607.27122 — Towards Grounded GI Endoscopy VQA via Multi-Task Learning on Small VLMs
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: single NVIDIA RTX 3090 Ti
  - PAR: small VLMs vs ≥4B backbones

## 2607.26554 — MedARC: Training-Free Adaptive Redundancy Compression of Visual Tokens for 3D Medical Vision-Language Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: Table 1 Time column: average inference time in seconds (e.g., 1.25 → 0.90 s) with token retention rate
  - HW: four NVIDIA A100 GPUs
  - note: memory 'consumption' discussed qualitatively only

## 2607.15661 — Model Merging for Medical LVLMs: A Benchmark and a Winner-Take-All Approach
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: model-merging benchmark; no hardware or efficiency numbers in extracted text

## 2607.05625 — Cross-Contextual Vision-Language Adaptation with LoRA for Personalized Severe Adverse Event Detection in Clinical Wound Monitoring
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA L40 GPU

## 2607.04344 — IRIS: An Intelligent Vision-Language System for Ocular Surface Diseases via Topic Tree and Scene-Driven VQA Generation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: four A6000 GPUs
  - PAR: compact 4B vs up to 34B

## 2607.01908 — Towards Real-World Ultrasound Understanding: Large Vision-Language Models from Multi-Image Examinations with Long-Form Reports
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: 'on NVIDIA GPUs' without model; iterations given, no time → HW N

## 2607.01436 — Discrete Diffusion Language Models for Interactive Radiology Report Drafting
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR Y · PAR Y
  - LAT: Table 2 latency (s): 6.43 AR vs 1.46–1.84 diffusion; 3.5–4.4× faster
  - HW: one H100 (bf16)
  - THR: Table 2 throughput 24.6 vs 139.4–175.3 tok/s
  - PAR: 3.8B active / 26B
  - note: clean inference report

## 2606.31599 — Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning
- LAT Y (infer Y, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: Table 4: ≈4.5× speedup on Lingshu-7B, ≈3.4× on Lingshu-32B (vLLM); training 8 hours
  - HW: 8 NVIDIA H200 GPUs
  - note: relative speedup; absolute ms not in extracted text

## 2606.23487 — CADRE: Stable, Parameter Efficient Adaptation of Medical Vision Language Models with Bounded Forgetting and Prior Drift
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: one T4 GPU
  - note: explicitly states no runtime guardrail result

## 2606.21915 — GTA-Net: Cooperative Game Theory for Vision-Language Alignment in Chest X-Ray Report Generation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: NVIDIA H100/H200 GPUs (80GB)

## 2606.21194 — MEDLAYXPLAIN: Benchmarking the Expert-Lay Gap in Medical Vision-Language Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: Table H.3: ∼88× faster inference than 27B teacher, ∼34× faster than GREEN on a single B200
  - HW: 4×B200 (training); single B200 (cost comparison)
  - PAR: 3B evaluator vs 27B teacher
  - note: relative speed of the evaluation metric model

## 2606.15861 — Object Tokens as a Bridge Between Segmentation and Visual Question Answering in Robotic Surgery
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: no hardware/timing numbers in extracted text

## 2606.11106 — FADA: Accessible fetal ultrasound interpretation and annotation with a selectively distilled unified vision-language model
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - LAT: Table 4: ∼20–25 s (RTX 4090), ∼35–45 s (A10G), ∼70–140 s (T4), ∼59 s on-device (Honor 90); mobile latency measured, GPU latencies estimated from 14,004 s / 4,478 images
  - HW: RTX 4090, A10G, T4; Honor 90 (Snapdragon 7 Gen 1, 12 GB RAM)
  - MEM: GGUF Q4_K_M 516 MB + 195 MB = 712 MB; ~60% GPU memory reduction (training)
  - PAR: 4B and 0.8B; ~2% trainable
  - note: only paper with measured smartphone deployment; still no energy/battery measurement → ENG N

## 2608.18095 — Backdoor Learning in Language Models and Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP Y · MEM N · ENG N · THR Y · PAR N
  - HW: NVIDIA RTX A6000 (48GB); RTX A5000 (24GB)
  - FLOP: Table 5.2: 10.87 vs 2.35 TFLOPS (utilization)
  - THR: Table 5.2 samples/sec 179.46 vs 0.42 (training), 3.33 vs 0.58 (inference)
  - note: PhD dissertation (470k chars) that embeds the TCP-LLaVA chapter (same numbers as 2507.14497); efficiency part duplicates that paper

## 2606.04922 — Geometry-Aware Distillation for Prompt Tuning Biomedical Vision-Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A100 GPU (40 GB)
  - note: energy hits are class-graph W

## 2605.30716 — Simple Token-Efficient Vision-Language Model for Case-level Pathology Synoptic Report Generation
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR N
  - LAT: preprocessing 14.06 s and inference 2.4 s per case (5×); 196.84 s / 4.62 s at 20×; runtime tables 12–13
  - HW: half of an NVIDIA H100 (40 GB VRAM)
  - MEM: training fits in 40 GB VRAM (memory as constraint met); 'substantially more efficient in memory' with runtime figures
  - note: memory reported as fit-within-budget rather than measured peak; counted Y (borderline)

## 2605.29299 — Pocket-Dentist: On-Device Dental Image Understanding via Efficient Multimodal Large Language Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM Y · ENG N · THR Y · PAR Y
  - LAT: 4.31 s per sample on iPhone 17 Pro; 4.9× reduction vs 7B; Table 5 TTFT/OET/Total (s)
  - HW: iPhone 17 Pro (A19 Pro, 12 GB); NVIDIA H100 96 GB for training
  - MEM: 2.62 GB RAM (2B) vs 6.03 GB (7B); Table 5 RAM (GB), CPU (%)
  - THR: 30.6 vs 9.2 tokens/s; Table 5 ITPS/OTPS
  - PAR: 1B–32B evaluated; 2B deployed
  - note: most complete on-device report; explicitly states no thermal measurements → ENG N

## 2605.26292 — Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient and Generalizable Evidential Tuning
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: one NVIDIA A100 GPU (40GB)
  - PAR: 0.11% of parameters (221K)

## 2605.24792 — Parameter-Efficient VLMs for Gastrointestinal Endoscopy: Medical Image Generation and Clinical Visual Question Answering
- LAT Y (infer N, train Y) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: training time ~4–5 hours on 'standard GPU hardware'
  - PAR: 89.9% reduction in trainable parameters
  - note: GPU model not named for own runs (RTX 4090 refers to cited DermatoLlama)

## 2605.21421 — AIGaitor: Privacy-preserving and cloud-free motion analysis for everyone, using edge computing
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR Y · PAR Y
  - LAT: 8.3–100 ms/frame on iPhone 14; 77 s end-to-end for 10 s clip vs 94 s cloud (H200)
  - HW: iPhone 14 (A15 Bionic) vs NVIDIA H200 NVL 143 GB + Xeon 6731P
  - THR: ms/frame over 10-min 4K 60 fps stream
  - PAR: 24 M–632 M
  - note: mentions thermal throttling qualitatively; no energy/battery measurement → ENG N. Pose/gait pipeline with LLM summary stage

## 2605.18419 — Geometry-Aware Uncertainty Coresets for Robust Visual In-Context Learning in Histopathology
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: coreset selection; no hardware/efficiency numbers; 'high-throughput' is clinical context

## 2605.18313 — Wasserstein Equilibrium Decoding for Reliable Medical Visual Question Answering
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: single NVIDIA A100 80GB GPU
  - PAR: 2B / 8B
  - note: motivates on-device low latency but does not measure it; energy hits are Wasserstein W1

## 2605.15736 — BiomedAP: A Vision-Informed Dual-Anchor Framework with Gated Cross-Modal Fusion for Robust Medical Vision-Language Adaptation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single RTX 5090 (32GB)

## 2605.15561 — RoiMAM: Region-of-Interest Medical Attention Model for Efficient Vision-Language Understanding
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: NVIDIA A100 (40GB) + Intel Xeon Gold 5320
  - PAR: 1.7B vs 7–8.6B competitors (Table 1 parameter column)
  - note: 'Efficient' in title = parameter count only

## 2605.09384 — LiteMedCoT-VL: Parameter-Efficient Adaptation for Medical Visual Question Answering
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: NVIDIA GeForce RTX 5090 32 GB (appendix spec table)
  - PAR: 2B with LoRA vs 4B
  - note: explicitly: 'We have not measured latency, memory footprint, throughput, or energy consumption on representative portable hardware'

## 2605.09242 — Cross-Modal Semantic-Enhanced Diffusion Framework for Diabetic Retinopathy Grading
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA RTX 4090

## 2605.06173 — Retina-RAG: Retrieval-Augmented Vision-Language Modeling for Joint Retinal Diagnosis and Clinical Report Generation
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - LAT: training 367 minutes; cost < $0.0002 per report
  - HW: single RTX 1650 (4GB)
  - MEM: 10.5GB peak memory (training)
  - PAR: 1.23% (103M/8.4B)
  - note: cost per report as proxy; no inference latency

## 2604.19937 — Infection-Reasoner: A Compact Vision-Language Model for Wound Infection Classification with Evidence-Grounded Clinical Reasoning
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: NVIDIA H100 (80GB) ×1 / ×4 (training)
  - PAR: 4B
  - note: steps given, no wall time

## 2604.18444 — ProtoCLIP: Prototype-Aligned Latent Refinement for Robust Zero-Shot Chest X-Ray Classification
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA Tesla V100 (32GB)

## 2604.17629 — BioVLM: Routing Prompts, Not Parameters, for Cross-Modality Generalization in Biomedical VLMs
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: single NVIDIA A6000 GPU
  - PAR: Table 5 trainable-parameter comparison

## 2603.20985 — Consistent but Dangerous: Per-Sample Safety Classification Reveals False Reliability in Medical Vision-Language Models
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: safety classification study; no hardware/efficiency numbers

## 2603.11625 — MedPruner: Training-Free Hierarchical Token Pruning for Efficient 3D Medical Image Understanding in Vision-Language Models
- LAT Y (infer Y, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: Table 3: average inference time 9.2 s → 7.7 s
  - HW: 8 × NVIDIA H20 GPUs
  - note: 'Efficient' token pruning; inference time reported

## 2603.05421 — DARK: Diagonal-Anchored Repulsive Knowledge Distillation for Vision-Language Models under Extreme Compression
- LAT Y (infer Y, train N) · HW Y · FLOP Y · MEM N · ENG N · THR Y · PAR Y
  - LAT: visual encoder 1.6 ms on iPhone 16 Pro vs teacher 37.6 ms (CoreML fp16, batch 1); Table 3
  - HW: iPhone 16 Pro
  - FLOP: 32× fewer MACs; Table 3 GMACs
  - THR: >600 fps vs 30–60 fps ultrasound
  - PAR: 427M → 75M; 26× smaller encoder
  - note: on-device measured; no energy/battery → ENG N

## 2602.23817 — Footprint-Guided Exemplar-Free Continual Histopathology Report Generation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: continual learning; 'footprint' is a method name, not memory; no hardware numbers

## 2602.19178 — EMAD: Evidence-Centric Grounded Multimodal Diagnosis for Alzheimer's Disease
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: NVIDIA RTX 3090 GPUs

## 2602.06184 — PhenoLIP: Integrating Phenotype Ontology Knowledge into Medical Vision-Language Pretraining
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 8 NVIDIA A100 GPUs (appendix)
  - note: epochs given, no wall time

## 2602.00400 — KEPO: Knowledge-Enhanced Preference Optimization for Multimodal Reasoning with Applications to Medical VQA
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: each training run typically takes around 4 … (appendix B, training time)
  - HW: NVIDIA A100-SXM4-80GB server
  - note: training time only

## 2512.21508 — Fixed-Budget Parameter-Efficient Training with Frozen Encoders Improves Multimodal Chest X-Ray Classification
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - PAR: 2.37M (2.51%) vs 94.3M full FT; 40× reduction; budget-matched 1.06M
  - note: parameter budget is the efficiency axis; no hardware/time

## 2512.10316 — ConStruct: Structural Distillation of Foundation Models for Prototype-Based Weakly Supervised Histopathology Segmentation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR Y
  - PAR: 6.3M trainable (3.7%)
  - note: 'energy function' hit is CRF energy, not power

## 2512.02438 — Boosting Medical Vision-Language Pretraining via Momentum Self-Distillation under Limited Computing Resources
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM Y · ENG N · THR N · PAR N
  - LAT: Table: Epoch Time ~26 min / ~30 min (training)
  - HW: single RTX 4090 (24 GB); feasible on RTX 2080Ti (11 GB)
  - MEM: Peak VRAM ~22 GB vs ~9 GB; ≥32 GB per GPU for end-to-end baseline
  - note: training-side efficiency table

## 2512.00597 — Scaling Down to Scale Up: Towards Operationally-Efficient and Deployable Clinical Models via Cross-Modal Low-Rank Adaptation for Medical Vision-Language Models
- LAT N (infer N, train N) · HW N · FLOP N · MEM Y · ENG N · THR N · PAR Y
  - MEM: storage ∼500 MB per checkpoint (full FT) vs LoRA adapters (Table 3)
  - PAR: 1.67M trainable (0.38% of 440M)
  - note: 'operationally-efficient and deployable' in title; no hardware/latency numbers; MEM is storage size — borderline

## 2511.22739 — All Centers Are at most a Few Tokens Apart: Knowledge Distillation with Domain Invariant Prompt Tuning
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: no hardware/efficiency numbers

## 2510.02922 — Multimodal Carotid Risk Stratification with Large Vision-Language Models: Benchmarking, Fine-Tuning, and Clinical Insights
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: fps hit is ultrasound acquisition rate; no compute numbers

## 2508.09225 — AMRG: Extend Vision Language Models for Automatic Mammography Report Generation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: no hardware/efficiency numbers

## 2508.04101 — NEARL: Interacted Query Adaptation with Orthogonal Regularization for Medical Vision-Language Understanding
- LAT N (infer N, train N) · HW Y · FLOP Y · MEM N · ENG N · THR Y · PAR Y
  - HW: single NVIDIA RTX 3090
  - FLOP: 1170 GFLOPs per batch (batch 100)
  - THR: 500 FPS vs baselines 470–540 FPS
  - PAR: 1.46M trainable
  - note: 'real-time clinical application' section

## 2505.00275 — AdCare-VLM: Towards a Unified and Pre-aligned Latent Representation for Healthcare Video Understanding
- LAT Y (infer N, train Y) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - LAT: fine-tuning ~eight hours
  - HW: eight A5000 GPUs
  - PAR: 7B
  - note: training time only

## 2406.18054 — Leveraging Pre-trained Models for FF-to-FFPE Histopathological Image Translation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: image translation; no hardware/efficiency numbers

## 2608.26856 — From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: two NVIDIA 48G A6000 GPUs

## 2608.21445 — ViTexSZ: Heterogeneous Vision-Text Knowledge Distillation for EEG Seizure Detection
- LAT Y (infer Y, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - LAT: online inference ≈9.8 ms per window
  - note: hardware not named

## 2606.22442 — Efficient Multimodal Clinical Question Answering for Pulmonary Embolism Risk Assessment
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: 'Efficient' in title; no hardware/latency/memory numbers found in extracted text

## 2605.11208 — Hi-GaTA: Hierarchical Gated Temporal Aggregation Adapter for Surgical Video Report Generation
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single 40G NVIDIA A100

## 2605.09443 — Through the Lens of Character: Resolving Modality-Role Interference in Multimodal Role-Playing Agent
- LAT Y (infer Y, train N) · HW N · FLOP N · MEM Y · ENG N · THR Y · PAR N
  - LAT: Table 5 Sec./sample 27.28 (base) vs 59.11 (VCD) vs ours
  - MEM: Table 5 Peak CUDA GB 19.22 / 24.87 / …
  - THR: Table 5 Tok./s 13.77 / 6.03 / 11.44 …
  - note: 'single GPU' unnamed → HW N; role-play VLM, medical relevance marginal

## 2603.27737 — Synergizing Discriminative Exemplars and Self-Refined Experience for MLLM-based In-Context Learning in Medical Diagnosis
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single RTX 6000 GPU (vLLM)

## 2603.26008 — FairLLaVA: Fairness-Aware Parameter-Efficient Fine-Tuning for Large Vision-Language Assistants
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 8 NVIDIA RTX A6000 (or 2 A100 for baselines)
  - note: 'modest computational overhead' unquantified

## 2603.17746 — Concept-to-Pixel: Prompt-Free Universal Medical Image Segmentation
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: no hardware/efficiency numbers; energy hits are conv weights W

## 2603.16372 — InViC: Intent-aware Visual Cues for Medical Visual Question Answering
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 8 NVIDIA GeForce RTX 4090

## 2512.23304 — MedGemma vs GPT-4: Open-Source and Proprietary Zero-shot Medical Disease Classification from Images
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: NVIDIA A100 cluster (8 GPUs, 40GB)
  - note: 'GPU requirements by 3 times' is a cited LoRA claim, not measured

## 2510.04281 — RetiBridge: Bridging Quantitative Retinal Biomarkers and Qualitative Diagnosis with a Knowledge-Guided Multimodal Large Language Model
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA L40S (48 GB)

## 2510.03232 — LEAML: Label-Efficient Adaptation to Out-of-Distribution Visual Tasks for Multimodal Large Language Models
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 16 NVIDIA A100 80GB
  - note: 'label-efficient', not compute-efficient

## 2509.24888 — MMRQA: Signal-Enhanced Multimodal Large Language Models for MRI Quality Assessment
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: 2 NVIDIA A6000

## 2509.22261 — InfiMed-Foundation: Pioneering Advanced Multimodal Medical Models with Compute-Efficient Pre-Training and Multi-Stage Fine-Tuning
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR Y
  - HW: 32 NVIDIA H800 (80GB) pretraining; 16 GPUs SFT
  - PAR: one-fifth the parameter count of BioMediX2-8B
  - note: 'Compute-Efficient Pretraining' in title refers to data/curriculum strategy; no GPU-hour or time figure found

## 2508.02525 — Accurate and Interpretable Postmenstrual Age Prediction via Multimodal Large Language Model
- LAT N (infer N, train N) · HW Y · FLOP N · MEM N · ENG N · THR N · PAR N
  - HW: single NVIDIA A100
  - note: 'large memory footprint' qualitative

## 2608.04515 — CARVE: Cross-Slice Anisotropic Reallocation of Visual Evidence for Efficient 3D Medical Volume Understanding
- LAT Y (infer Y, train N) · HW N · FLOP Y · MEM Y · ENG N · THR N · PAR N
  - LAT: latency 6.10 s (CARVE) vs 9.21 s Full vs 13.04 s MMTok; Fig. 1/6 latency (ms) sweeps
  - FLOP: Fig. 2 FLOPs vs token count (curve, no table value)
  - MEM: ∆Mem in GB (3.79 Full → 2.84 …) in efficiency table
  - note: GPU model not found in extracted text → HW N; FLOP counted from figure axis (borderline)

## 2608.17151 — Lymphocyte Mimicry Correction via Region-Level Tissue Reasoning and Unbalanced Optimal Transport
- LAT N (infer N, train N) · HW N · FLOP N · MEM N · ENG N · THR N · PAR N
  - note: hardware hits are tissue-subtype codes T1/T3/T4, not GPUs; no efficiency numbers

