# Partial reproduction report

## Conclusion

The current evidence supports one narrow result: the row-mean potential construction from Theorem 4.5 exactly decomposes five finite seven-strategy skew-symmetric preference matrices into a transitive difference and a cyclic zero-marginal residual, with exact orthogonality. The result is labeled `TOY_FINITE_AUDIT`.

Claims 2–6 are not reproduced. The repository does not claim the HRC instantiation, RewardBench 2 scores, downstream LLM alignment scores, or DSPPO convergence rate.

## What the current evidence shows

- Five independently seeded finite fixtures were checked.
- Reconstruction maximum absolute error is 0 in every fixture.
- Cyclic row marginal and transitive/cyclic inner product are 0 in every fixture.
- A nonconstant wrong-potential control fails the zero-marginal condition in every fixture.

## Boundaries

- Finite uniform discrete matrices do not establish the theorem for arbitrary preference functions, continuous measures, or embedding assumptions.
- The official author repository currently contains only README.md and LICENSE; no training, evaluation, data, checkpoint, or raw benchmark result is pinned.
- No RewardBench, AlpacaEval, Arena-Hard, MT-Bench, or DSPPO run is claimed.
- Collection cleanup preserves the partial status and does not substitute model, data, evaluator, or remote compute artifacts.
