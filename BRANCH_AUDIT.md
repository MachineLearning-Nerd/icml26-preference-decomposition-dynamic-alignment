# Branch audit

The final public repository has one branch: `main`.

| Branch | Pre-dossier tip | Purpose and outcome | Disposition |
| --- | --- | --- | --- |
| `main` | `9271c858971bf6998fd664b87bfedbd0396504cd` | Canonical source snapshot, finite Claim 1 audit, outputs, and saved state. | Keep as canonical main |

There were no stale `master`, ORX, experiment, or unnamed branches. The local and remote ref layout is intentionally only `main`; `verify_final.py` fails if another branch appears.

All seven reachable pre-dossier commits use `MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>` for both author and committer. A complete recovery bundle was created before publication changes; its SHA-256 is `85675c5e80155836dfa01bc26a456029afe0486a32fca8b497aa265400b489f2`.
