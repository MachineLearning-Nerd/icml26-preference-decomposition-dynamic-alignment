# Source and paper audit

## Paper identity

- Title: *Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment*
- Authors: Yucong Huang, Xiucheng Li, Kaiqi Zhao, and Jing Li
- arXiv: [2605.17342](https://arxiv.org/abs/2605.17342), version 1 submitted 2026-05-17
- OpenReview: [7H9HRTWady](https://openreview.net/forum?id=7H9HRTWady)
- Submission number: `14998`

The arXiv abstract describes a hybrid reward-cyclic model that separates transitive and cyclic preference structure, plus Dynamic Self-Play Preference Optimization (DSPPO) for time-varying game guidance. It reports synthetic, RewardBench 2, AlpacaEval 2.0, Arena-Hard-v0.1, and MT-Bench experiments. The current repository audits only a finite decomposition mechanism.

## Pinned source records

| Source | Record |
| --- | --- |
| Source archive | `evidence/source/arxiv_source.tar.gz` |
| Archive SHA-256 | `0a1dc570c7a3c47d3c3d15e94e1500f2c20603c88418e07aa95dc17b6bc31a3b` |
| PDF | `evidence/source/paper.pdf` |
| PDF SHA-256 | `921356c07b3a34bd5c29d88b51f34e55f27eb269fd6aca1d2670ad3d15d80c19` |
| Source/contract retrieval | `2026-08-01T20:30:38.200953+00:00` |
| Contract manifest | `contract/contract_manifest.json`, SHA-256 `1d3a3cd1de4b26cc96bb2f6819f770fcb0db667d6b0b41d61c1d6d7c6885b8f7` |

## Official implementation provenance

The paper's arXiv record links the public author repository [lab-klc/Hybrid-Reward-Cyclic](https://github.com/lab-klc/Hybrid-Reward-Cyclic). Its observed `main` tip on 2026-08-17 was `ce8b59f57854a40ebeb1609849b8455a1174dfa1`. The public repository currently contains only `README.md` and `LICENSE`; no executable training or evaluation code, dataset, checkpoint, or raw result artifact is available there.

This audit does not execute or modify the official repository. The current Claim 1 result is independent clean-room code. The absence of executable artifacts is recorded as a reproducibility limitation, not as evidence against the paper's scientific claims.

## Local implementation provenance

The source archive is retained for paper inspection. The local Claim 1 producer uses exact Python rational arithmetic on synthetic finite matrices and is not presented as author code.

## Version and claim boundaries

- Claim 1 is a finite proxy for the construction in Theorem 4.5, not a universal theorem proof.
- Claims 2–6 retain the live contract statements but have no current evidence.
- No RewardBench, LLM checkpoint, preference dataset, evaluator output, downstream policy checkpoint, or DSPPO convergence trace is silently substituted.
