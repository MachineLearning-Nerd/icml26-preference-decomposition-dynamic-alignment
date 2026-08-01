import json, hashlib
from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_contract():
 m=json.loads((ROOT/'contract/contract_manifest.json').read_text()); c=json.loads((ROOT/'contract/live_claims.json').read_text()); assert len(c)==m['claim_count']==6 and m['max_points']==12
def test_source_manifest():
 for line in (ROOT/'evidence/source/SHA256SUMS').read_text().splitlines():
  h,n=line.split()[:2]; assert hashlib.sha256((ROOT/'evidence/source'/n).read_bytes()).hexdigest()==h
