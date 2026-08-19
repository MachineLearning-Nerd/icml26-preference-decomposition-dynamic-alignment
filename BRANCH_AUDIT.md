# Branch audit

The final public repository has one branch: `main`.

| Branch | Pre-dossier tip | Purpose and outcome | Disposition |
| --- | --- | --- | --- |
| `main` | `a853ee635daab208f65d6dcd9b7231009a3de27c` | Normalized source snapshot, finite Claim 1 audit, outputs, and saved state before this publication dossier. | Keep as canonical main |

There were no stale `master`, ORX, experiment, or unnamed branches. The local and remote ref layout is intentionally only `main`; `verify_final.py` fails if another branch appears.

All eight reachable pre-dossier commits use `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>` for both author and committer. A complete recovery bundle was created before history normalization; its SHA-256 is `f2bef96acbc8c1769b671a5b4688db4a11409fb5c3112d587868fa8b66cecf63`.
