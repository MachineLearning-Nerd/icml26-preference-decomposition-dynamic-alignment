# Claim 1 — preference decomposition

**Exact live claim:** Theorem 4.5 establishes that any preference function decomposes uniquely into an orthogonal transitive (scalar, potential-function) component and a cyclic (zero-marginal, vector) component (Section 4.1, Theorem 4.5).

**Outcome: toy.** This is an independently executed, exact-rational **finite** uniform-measure realization of the pinned construction. It is not a proof for arbitrary continuous preference functions.

## Protocol and source pin

The pinned source (`evidence/source/arxiv_source.tar.gz`, hash manifest `evidence/source/SHA256SUMS`) defines `f(v)=E_w phi(v,w)`, `phi_T=f(v)-f(w)`, and `phi_C=phi-phi_T`; see `evidence/claim1_source_locations.md`. We implement that construction on five independently seeded 7-strategy skew-symmetric games, using exact Python rational arithmetic and uniform discrete measure.

Run:

```bash
.venv/bin/python src/claim1_finite_decomposition.py \
  --out outputs/claim1_finite_decomposition --seeds 11 23 47 89 131
(cd outputs/claim1_finite_decomposition && sha256sum -c SHA256SUMS)
.venv/bin/python -m pytest -q
```

## Results and controls

For every one of five fixtures, reconstruction is exact, the cyclic residual has zero row marginal, and the Frobenius inner product `<phi_T,phi_C>` is exactly zero. Raw results/configuration/log/hash manifest are in `outputs/claim1_finite_decomposition/`.

**Negative control:** replacing the source-defined row-mean potential with a nonconstant arbitrary potential makes the residual fail the zero-marginal condition. This checks that the claimed construction, not merely an arbitrary split, is being tested.

## Limits

Finite discrete examples do not establish the theorem's universal functional claim or its embedding assumptions. This reduced finite experiment is therefore labeled **toy**, not verified or falsified.
