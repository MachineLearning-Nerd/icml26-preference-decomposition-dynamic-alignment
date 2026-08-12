# Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment

Independent, claim-by-claim reproduction and audit record for the ICML 2026 paper by Yucong Huang, Xiucheng Li, Kaiqi Zhao, and Jing Li.

Current status: **partial audit**. Claim 1 has a finite exact-rational toy audit. Claims 2–6 remain unstarted. Nothing in this repository should be read as a verified reproduction of the paper's universal theorem, model training, or benchmark results.

## Paper and provenance

| Field | Record |
| --- | --- |
| Paper | Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment |
| Authors | Yucong Huang; Xiucheng Li; Kaiqi Zhao; Jing Li |
| arXiv | [2605.17342](https://arxiv.org/abs/2605.17342) |
| OpenReview | [7H9HRTWady](https://openreview.net/forum?id=7H9HRTWady), submission 14998 |
| Paper source pin | arxiv_source.tar.gz SHA-256: 0a1dc5707c3a47d3c3d15e94e1500f2c20603c88418e07aa95dc17b6bc31a3b |
| Paper PDF pin | paper.pdf SHA-256: 921356c07b3a34bd5c29d88b51f34e55f27eb269fd6aca1d2670ad3d15d80c19 |
| Collection | ICML 2026 reproduction collection |
| Former repository | icml26-repro-7H9HRTWady-preference-decomposition-dynamic-alignment |
| Current repository | [MachineLearning-Nerd/icml26-preference-decomposition-dynamic-alignment](https://github.com/MachineLearning-Nerd/icml26-preference-decomposition-dynamic-alignment) |
| Canonical branch | main |

The six live claims are preserved in contract/live_claims.json. The contract manifest is pinned by SHA-256 in contract/contract_manifest.json.

## What the paper is doing

The paper argues that pairwise preferences are not always well represented by one scalar reward. It separates preference structure into:

1. A transitive component represented by a scalar potential difference, f(v) - f(w).
2. A cyclic component with zero marginal under the paper's uniform-measure construction.
3. A Hybrid Reward Cyclic (HRC) model that combines a Bradley-Terry scalar reward with a GPM-style skew-symmetric bilinear component.
4. Dynamic Score Preference Policy Optimization (DSPPO), which changes the score guidance from transitive to cyclic during training and analyzes its convergence toward a Nash equilibrium.

The paper reports synthetic experiments, RewardBench 2 results for Gemma-2B-it and Llama-3.1-8B, and downstream AlpacaEval 2.0, Arena-Hard-v0.1, and MT-Bench evaluations.

## Claim ledger

The status labels below describe this audit only. An unstarted claim is not a falsification; it has not yet been independently executed.

| Claim | Paper target | How the claim must be produced | Audit status |
| --- | --- | --- | --- |
| 1 | Theorem 4.5: unique orthogonal transitive-plus-cyclic decomposition | Construct preference functions on a finite uniform measure; compute the row-mean potential; form the potential difference and residual; check exact reconstruction, zero cyclic marginal, orthogonality, and a wrong-potential negative control. Then extend beyond finite fixtures before calling the universal theorem reproduced. | **TOY_FINITE_AUDIT** — outputs/claim1_finite_decomposition/ |
| 2 | Theorem 4.6, source label thm:decomposition_instantiation: HRC combines Bradley-Terry and GPM-style skew-symmetric terms | Pin the data and embedding construction; verify zero-mean embeddings; fit or load the scalar reward and skew-symmetric bilinear form; check score decomposition and the stated constraints on held-out pairwise preferences. | **UNSTARTED** |
| 3 | RewardBench 2: Gemma-2B-it HRC 57.63%, BT 55.93%, GPM 56.40% | Pin RewardBench 2 version, prompt/template, model checkpoint, training data, objective, seeds, evaluation code, and every task-level result before comparing the reported averages. | **UNSTARTED** |
| 4 | RewardBench 2: Llama-3.1-8B HRC 70.95%, 0.85 percentage points over BT | Reproduce the same protocol as Claim 3 with the Llama-3.1-8B checkpoint and report task-level metrics, aggregation, uncertainty, and baseline configuration. | **UNSTARTED** |
| 5 | HRC+DSPPO: Gemma-2B-it 44.75% length-controlled AlpacaEval 2.0 win rate and 46.8% Arena-Hard-v0.1 win rate | Pin policy checkpoints, preference data, DSPPO schedule, decoding, reference models, evaluator models, prompts, length-control implementation, and benchmark versions; preserve raw judged outputs. | **UNSTARTED** |
| 6 | Theorem 5.3, source label thm:dsppo: DSPPO reaches an O(1/sqrt(T)) duality-gap rate under its assumptions | Implement the time-varying score schedule and dynamic game; verify realizability, bounded scores, score-approximation error, step-size choices, and measure the average-policy duality gap over T. | **UNSTARTED** |

## Claim 1: current finite audit

The pinned paper source states the construction in main.tex lines 267–280 and develops it in lines 725–782. For each finite fixture, this audit:

1. Generates a skew-symmetric preference matrix under a uniform discrete measure.
2. Computes the source-defined potential as the row mean, f_i = average_j phi(i,j).
3. Forms the transitive matrix T_ij = f_i - f_j.
4. Forms the cyclic residual C = phi - T.
5. Checks exact reconstruction, zero row marginal, and zero Frobenius inner product using rational arithmetic.
6. Replaces the source-defined potential with a nonconstant wrong potential as a negative control.

Five independently seeded seven-strategy fixtures were run with seeds 11, 23, 47, 89, and 131. Every fixture produced:

- exact reconstruction maximum absolute error 0;
- zero cyclic row marginal;
- zero transitive/cyclic inner product;
- failure of the zero-marginal check for the wrong potential.

The result is deliberately labeled **toy**. It covers finite skew-symmetric games with a uniform discrete measure; it does not prove the theorem for arbitrary preference functions, continuous measures, or the paper's embedding assumptions.

Evidence and code:

- Source locations: evidence/claim1_source_locations.md
- Exact theorem excerpt: evidence/source/theorem45_excerpt.tex
- Reproduction script: src/claim1_finite_decomposition.py
- Source audit: src/claim1_source_audit.py
- Results, configuration, log, and checksums: outputs/claim1_finite_decomposition/
- Claim log: logbook/claim-1.md

To rerun the current local audit:

    .venv/bin/python src/claim1_finite_decomposition.py --out outputs/claim1_finite_decomposition --seeds 11 23 47 89 131
    (cd outputs/claim1_finite_decomposition && sha256sum -c SHA256SUMS)

The environment used for the recorded run is captured in outputs/claim1_finite_decomposition/summary.json. The repository does not claim that a full test suite has been rerun for every future change.

## Official implementation status

The paper names [lab-klc/Hybrid-Reward-Cyclic](https://github.com/lab-klc/Hybrid-Reward-Cyclic) as its public code repository. At the time of this audit, the public repository exposed only LICENSE and README.md and no executable training, evaluation, data, or model-release artifacts. Therefore this reproduction cannot pin an official implementation or checkpoint. This is a reproducibility limitation, not evidence that the paper's method is incorrect.

## Repository and branch map

The canonical repository has one branch: main. No experiment, ORX, master, or other stale branch is part of the published state.

- README.md — paper overview, claim ledger, current verdict, and reproduction instructions.
- STATUS.md — compact machine-readable audit status for this repository.
- AUTONOMOUS_STATE.json — durable continuation state.
- branch-audit.md — branch inventory and attribution audit.
- contract/ — pinned challenge metadata and six live claims.
- evidence/source/ — pinned paper source, PDF, theorem excerpt, and checksums.
- evidence/ — source locations and claim-specific evidence notes.
- src/ — the finite Claim 1 audit scripts.
- outputs/ — auditable JSON, CSV, logs, and checksum manifests.
- logbook/ — claim-level reasoning and scope notes.
- tests/ — contract and Claim 1 checks.

Branch policy: use main for the canonical audit record. A temporary local branch may be used for development, but it must be merged or removed before publication. Branch names must describe work; names such as orx, experiment, or unnamed checkpoints are not canonical.

## Reproduction policy

The repository is designed for transparent local work:

- local CPU or locally available GPU only;
- no Hugging Face CPU upgrades, Hugging Face Jobs, paid remote compute, or untracked external runners;
- every source, contract, output, and checkpoint used for a claim must be hashed or linked;
- benchmark claims require raw outputs, exact evaluator configuration, and model/data pins;
- a small toy result is reported as toy and never promoted to verified without matching the paper's scope.

## Citation

    @article{huang2026transitivity,
      title   = {Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment},
      author  = {Huang, Yucong and Li, Xiucheng and Zhao, Kaiqi and Li, Jing},
      journal = {arXiv preprint arXiv:2605.17342},
      year    = {2026},
      doi     = {10.48550/arXiv.2605.17342}
    }

Please cite the original paper when using this audit record. The paper and its authors remain the source of the scientific claims documented here.

## Thank-you note

Thank you to Yucong Huang, Xiucheng Li, Kaiqi Zhao, and Jing Li for making a difficult alignment question concrete: how to represent preferences that contain both transitive and genuinely cyclic structure. The theorem statements, decomposition viewpoint, HRC model, and DSPPO analysis provide a useful target for careful reproduction. This repository is intended as a respectful, transparent audit of that target, with uncertainty and missing artifacts recorded instead of hidden.

## Limitations and next actions

The current record is not publication-ready. The next scoped work is an independent review of the finite Claim 1 audit followed by the direct HRC instantiation in Claim 2. Claims 3–5 require model, data, evaluator, and compute artifacts that are not present in the named author repository. Claim 6 requires a separate dynamic-game implementation and convergence audit.
