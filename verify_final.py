#!/usr/bin/env python3
"""Fail-closed verification for the published partial preference audit."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = "MachineLearning-Nerd/icml26-preference-decomposition-dynamic-alignment"
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_COMMIT_COUNT = 9
EXPECTED_OVERALL_VERDICT = "PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_6_UNSTARTED"
EXPECTED_STATUSES = {
    "C1": "TOY_FINITE_AUDIT",
    "C2": "UNSTARTED",
    "C3": "UNSTARTED",
    "C4": "UNSTARTED",
    "C5": "UNSTARTED",
    "C6": "UNSTARTED",
}
EXPECTED_HASHES = {
    "README.md": "e2b4fc1d305e0c78042434e341dbb2c99f03a22a13fe3eb2a3ac410902c099d4",
    "STATUS.md": "bea8fcb5cbe37c077654fe933012f6174161226e1e8d759c055218e2956cbca2",
    "REPORT.md": "8089129f2cfc09e7e98ac48123838b609812210528b8edbbe733e98d7cdd6832",
    "claims.json": "3d2d9408e5ca0e0ed846628266739255b0c33a2b1cf10ea1aa7c0035258533c8",
    "reproduction_verdicts.json": "693a7f7875fc0620084f8bce22214b5b78618f77342187fa2e8558d0bc3c61d1",
    "AUTONOMOUS_STATE.json": "10915073f75ec9ff659b4a1566ff3179bf511cf3256d76c8e2a2cfea5ee72d68",
}


def command(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    failures: list[str] = []
    origin = command("git", "config", "--get", "remote.origin.url").strip()
    if EXPECTED_REPOSITORY not in origin:
        failures.append(f"unexpected origin: {origin}")

    local_branches = set(command("git", "for-each-ref", "--format=%(refname)", "refs/heads").splitlines())
    if local_branches != {"refs/heads/main"}:
        failures.append(f"local branches are {sorted(local_branches)}")
    remote_branches = set(command("git", "for-each-ref", "--format=%(refname)", "refs/remotes/origin").splitlines())
    if remote_branches - {"refs/remotes/origin/HEAD", "refs/remotes/origin/main"}:
        failures.append(f"unexpected remote branches: {sorted(remote_branches)}")
    backup_refs = command("git", "for-each-ref", "--format=%(refname)", "refs/original").splitlines()
    if backup_refs:
        failures.append(f"backup refs remain: {backup_refs}")

    commits = command("git", "rev-list", "main").splitlines()
    if len(commits) != EXPECTED_COMMIT_COUNT:
        failures.append(f"expected {EXPECTED_COMMIT_COUNT} commits, found {len(commits)}")
    if command("git", "rev-parse", "main") != command("git", "rev-parse", "origin/main"):
        failures.append("main and origin/main differ")
    for commit in commits:
        identity = command("git", "show", "-s", "--format=%an%n%ae%n%cn%n%ce", commit).splitlines()
        if identity != [CANONICAL_NAME, CANONICAL_EMAIL, CANONICAL_NAME, CANONICAL_EMAIL]:
            failures.append(f"non-canonical identity at {commit[:12]}")
            break
    if "co-authored-by:" in command("git", "log", "main", "--format=%B").lower():
        failures.append("co-author trailer found")

    manifest = json.loads((ROOT / "EVIDENCE_MANIFEST.json").read_text())
    if manifest.get("repository") != EXPECTED_REPOSITORY:
        failures.append("evidence manifest repository is not canonical")
    if manifest.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        failures.append("evidence manifest overall verdict is not canonical")
    for field in ("publication_allowed", "score_claim", "official_author_endorsement"):
        if manifest.get(field) is not False:
            failures.append(f"evidence manifest {field} boundary is not false")
    for relative in manifest["required_audit_files"]:
        if not (ROOT / relative).is_file():
            failures.append(f"missing audit file: {relative}")

    claims = json.loads((ROOT / "claims.json").read_text())
    if claims.get("repository") != EXPECTED_REPOSITORY:
        failures.append("claim ledger repository is not canonical")
    if claims.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        failures.append("claim ledger overall verdict is not canonical")
    for field in ("publication_allowed", "score_claim", "official_author_endorsement"):
        if claims.get(field) is not False:
            failures.append(f"claim ledger {field} boundary is not false")
    statuses = {claim["id"]: claim["status"] for claim in claims["claims"]}
    if statuses != EXPECTED_STATUSES:
        failures.append(f"unexpected claim statuses: {statuses}")
    if len(claims["claims"]) != 6:
        failures.append("claim ledger does not contain six claims")

    summary = json.loads((ROOT / "outputs/claim1_finite_decomposition/summary.json").read_text())
    if summary.get("verdict") != "toy":
        failures.append(f"unexpected Claim 1 verdict: {summary.get('verdict')}")
    with (ROOT / "outputs/claim1_finite_decomposition/results.csv").open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 5:
        failures.append(f"expected five Claim 1 rows, found {len(rows)}")
    for row in rows:
        if row.get("reconstruction_max_abs") != "0":
            failures.append("Claim 1 reconstruction is not exact")
        if row.get("cyclic_zero_marginal") != "True":
            failures.append("Claim 1 cyclic marginal is not zero")
        if row.get("orthogonality_inner_product") != "0":
            failures.append("Claim 1 orthogonality is not exact")
        if row.get("wrong_potential_zero_marginal") != "False":
            failures.append("Claim 1 wrong-potential control did not fail")

    for item in manifest["content_addressed_artifacts"]:
        path = ROOT / item["path"]
        if not path.is_file():
            failures.append(f"missing evidence artifact: {item['path']}")
        elif sha256(path) != item["sha256"]:
            failures.append(f"evidence hash mismatch: {item['path']}")
    manifest_hashes = {item["path"]: item["sha256"] for item in manifest["content_addressed_artifacts"]}
    for relative, expected in EXPECTED_HASHES.items():
        if manifest_hashes.get(relative) != expected:
            failures.append(f"manifest hash is not pinned: {relative}")
        elif sha256(ROOT / relative) != expected:
            failures.append(f"reader document hash mismatch: {relative}")

    source_sums = {}
    for line in (ROOT / "evidence/source/SHA256SUMS").read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        source_sums[relative] = expected
    for relative in ("arxiv_source.tar.gz", "paper.pdf"):
        path = ROOT / "evidence/source" / relative
        if source_sums.get(relative) != sha256(path):
            failures.append(f"source checksum mismatch: {relative}")

    readme = (ROOT / "README.md").read_text()
    for marker in [
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "BRANCH_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "reproduction_verdicts.json",
        "AUTONOMOUS_STATE.json",
        "verify_final.py",
        "publication_allowed",
        "score_claim",
        "official_author_endorsement",
    ]:
        if marker not in readme:
            failures.append(f"README missing dossier marker: {marker}")
    branch_audit = (ROOT / "BRANCH_AUDIT.md").read_text()
    if "| `main` |" not in branch_audit:
        failures.append("branch audit does not record main")
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    if "lab-klc/Hybrid-Reward-Cyclic" not in source_audit or "ce8b59f57854a40ebeb1609849b8455a1174dfa1" not in source_audit:
        failures.append("official implementation pin is missing")

    state = json.loads((ROOT / "AUTONOMOUS_STATE.json").read_text())
    if state.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        failures.append("autonomous state overall verdict is not canonical")
    for field in ("publication_allowed", "score_claim", "official_author_endorsement"):
        if state.get(field) is not False:
            failures.append(f"autonomous state {field} boundary is not false")
    if state.get("canonical_branch") != "main" or state.get("branch_count") != 1:
        failures.append("autonomous state branch metadata is not canonical")
    if state.get("canonical_identity", {}).get("email") != CANONICAL_EMAIL:
        failures.append("autonomous state does not record canonical email")
    if state.get("canonical_identity", {}).get("verified_reachable_commits") != 8:
        failures.append("autonomous state does not record the eight pre-dossier commits")

    reproduction = json.loads((ROOT / "reproduction_verdicts.json").read_text())
    if reproduction.get("repository") != EXPECTED_REPOSITORY:
        failures.append("reproduction verdict repository is not canonical")
    if reproduction.get("overall_verdict") != EXPECTED_OVERALL_VERDICT:
        failures.append("reproduction verdict is not canonical")
    for field in ("publication_allowed", "score_claim", "official_author_endorsement"):
        if reproduction.get(field) is not False:
            failures.append(f"reproduction verdict {field} boundary is not false")
    reproduction_statuses = {claim["id"]: claim["status"] for claim in reproduction["claims"]}
    if reproduction_statuses != EXPECTED_STATUSES:
        failures.append(f"unexpected reproduction verdict statuses: {reproduction_statuses}")

    result = {
        "passed": not failures,
        "failures": failures,
        "repository": EXPECTED_REPOSITORY,
        "commit_count": len(commits),
        "claim_statuses": statuses,
        "evidence_artifacts": len(manifest["content_addressed_artifacts"]),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
