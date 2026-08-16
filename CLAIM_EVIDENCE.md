# Claim-to-evidence ledger

This repository is a deliberately partial audit. Claim 1 has a reduced exact-rational finite result labeled `TOY_FINITE_AUDIT`; Claims 2–6 have no reproduction result and remain `UNSTARTED`.

## Claim 1 — Theorem 4.5 — TOY_FINITE_AUDIT

- Contract: a preference function decomposes into a transitive scalar-potential component and an orthogonal cyclic zero-marginal component.
- Producer: `src/claim1_finite_decomposition.py`.
- Evidence: `outputs/claim1_finite_decomposition/summary.json`, `results.csv`, `config.json`, and `SHA256SUMS`.
- Method: five independently seeded seven-strategy skew-symmetric preference matrices under a uniform discrete measure; exact Python rational arithmetic computes the row-mean potential, potential difference, residual, reconstruction, marginal, and inner product.
- Positive result: every fixture has reconstruction error 0, cyclic row marginal 0, and transitive/cyclic inner product 0.
- Negative control: a nonconstant wrong potential makes the residual fail the zero-marginal condition in all five fixtures.
- Boundary: finite discrete examples do not prove the theorem for arbitrary preference functions, continuous measures, or the paper's embedding assumptions.

## Claim 2 — Theorem 4.6 — UNSTARTED

- Contract: the Hybrid Reward Cyclic model combines a Bradley-Terry scalar reward with a GPM-style skew-symmetric bilinear component.
- Intended producer: pin the data and embedding construction, fit or load both components, and check score decomposition and constraints on held-out pairwise preferences.
- Current evidence: none. The finite decomposition fixture does not instantiate HRC.

## Claim 3 — RewardBench 2, Gemma-2B-it — UNSTARTED

- Contract: HRC reaches 57.63% average accuracy, above BT at 55.93% and GPM at 56.40%.
- Intended producer: pin RewardBench 2, prompt/template, model checkpoint, training data, objective, seeds, evaluation code, task-level results, and aggregation.
- Current evidence: none. No model or benchmark artifact is available in this workspace.

## Claim 4 — RewardBench 2, Llama-3.1-8B — UNSTARTED

- Contract: HRC reaches 70.95% average accuracy and improves over the BT baseline by 0.85 percentage points.
- Intended producer: reproduce Claim 3's protocol with the Llama-3.1-8B checkpoint and disclose task-level uncertainty and baselines.
- Current evidence: none.

## Claim 5 — HRC plus DSPPO downstream evaluations — UNSTARTED

- Contract: HRC plus DSPPO reaches the reported length-controlled AlpacaEval 2.0 and Arena-Hard-v0.1 win rates.
- Intended producer: pin policy checkpoints, preference data, schedule, decoding, reference models, evaluator models, prompts, length control, and benchmark versions; retain raw judged outputs.
- Current evidence: none. No downstream training or evaluator run is claimed.

## Claim 6 — Theorem 5.3 — UNSTARTED

- Contract: the time-varying DSPPO score schedule reaches a Nash equilibrium with an O(1/sqrt(T)) duality-gap rate under the theorem's assumptions.
- Intended producer: implement the dynamic game, verify realizability and bounded-score assumptions, pin step sizes and approximation errors, and measure average-policy duality gaps over T.
- Current evidence: none. No convergence theorem or rate audit is claimed.

## Aggregate verdict

The only supported result is the reduced finite Claim 1 fixture. The repository must not be described as a complete reproduction until Claims 2–6 receive evidence at their stated scope, exact source and artifact pins, and explicit controls.
