# Environment and run provenance

## Claim 1 command

    .venv/bin/python src/claim1_finite_decomposition.py --out outputs/claim1_finite_decomposition --seeds 11 23 47 89 131
    (cd outputs/claim1_finite_decomposition && sha256sum -c SHA256SUMS)

The cleanup verifier does not rerun this command or the full test suite.

## Recorded run

| Field | Value |
| --- | --- |
| Scope | Local CPU clean-room exact-rational finite preference decomposition |
| Seeds | `11`, `23`, `47`, `89`, `131` |
| Fixture size | 7 strategies per skew-symmetric preference matrix |
| Measure | Uniform discrete |
| Arithmetic | Exact Python rational arithmetic |
| Recorded Python | `3.14.5` |
| Recorded platform | Linux x86_64 with glibc 2.43 |
| Remote/paid compute | none |
| Claim 1 verdict | `TOY_FINITE_AUDIT` |

The cleanup verifier does not rerun the scientific command; it checks the retained outputs, manifests, and source pins.

## Evidence paths

- Source pin: `evidence/source/`
- Claim context: `evidence/claim1_source_locations.md`
- Exact theorem excerpt: `evidence/source/theorem45_excerpt.tex`
- Human-readable result: `logbook/claim-1.md`
- Raw outputs: `outputs/claim1_finite_decomposition/`
- Contract: `contract/live_claims.json` and `contract/contract_manifest.json`
- Standardized ledger: `claims.json`
- Selected hash record: `EVIDENCE_MANIFEST.json`

Claims 2–6 remain unstarted. No remote, paid, or benchmark-scale run was authorized for this documentation cleanup.
