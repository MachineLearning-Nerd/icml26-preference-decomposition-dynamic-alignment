"""Finite, exact-rational audit of the Theorem 4.5 uniform-measure decomposition.

For a skew-symmetric payoff matrix A on n equally-weighted strategies, the
paper's potential is p_i = mean_j A_ij.  We compute T_ij=p_i-p_j and C=A-T.
"""
from fractions import Fraction
from pathlib import Path
import argparse, csv, hashlib, json, platform, sys


def mat(n): return [[Fraction(0) for _ in range(n)] for _ in range(n)]
def row_means(a):
    n=len(a); return [sum(r, Fraction(0))/n for r in a]
def decompose(a):
    n=len(a); p=row_means(a)
    t=[[p[i]-p[j] for j in range(n)] for i in range(n)]
    c=[[a[i][j]-t[i][j] for j in range(n)] for i in range(n)]
    return p,t,c
def inner(a,b): return sum((a[i][j]*b[i][j] for i in range(len(a)) for j in range(len(a))), Fraction(0))
def maxabs(a): return max(abs(x) for r in a for x in r)
def skew(a): return all(a[i][j] == -a[j][i] for i in range(len(a)) for j in range(len(a)))
def zero_marginal(a): return all(sum(r, Fraction(0)) == 0 for r in a)
def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a))] for i in range(len(a))]
def fixture(seed,n=7):
    # deterministic integer edge weights; each seed is an independent finite game
    a=mat(n)
    for i in range(n):
      for j in range(i+1,n):
        v=Fraction(((seed+3)*(i+1)*(j+2)+7*i-5*j) % 19 - 9)
        if v == 0: v=Fraction(i+j+1)
        a[i][j]=v; a[j][i]=-v
    return a

def enc(x): return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'
def main(out, seeds):
    out=Path(out); out.mkdir(parents=True, exist_ok=True)
    rows=[]
    for seed in seeds:
      a=fixture(seed); p,t,c=decompose(a)
      assert skew(a) and skew(t) and skew(c) and zero_marginal(c)
      assert add(t,c)==a and inner(t,c)==0
      # uniqueness control: perturbing a potential by a nonconstant vector makes residual nonzero-marginal.
      q=[Fraction(i) for i in range(len(a))]
      badt=[[q[i]-q[j] for j in range(len(a))] for i in range(len(a))]
      badc=[[a[i][j]-badt[i][j] for j in range(len(a))] for i in range(len(a))]
      assert not zero_marginal(badc)
      rows.append({'seed':seed,'n':len(a),'skew_symmetric':skew(a),'cyclic_zero_marginal':zero_marginal(c),'reconstruction_max_abs':enc(maxabs([[a[i][j]-t[i][j]-c[i][j] for j in range(len(a))] for i in range(len(a))])),'orthogonality_inner_product':enc(inner(t,c)),'wrong_potential_zero_marginal':zero_marginal(badc),'potential':[enc(v) for v in p]})
    with (out/'results.csv').open('w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    summary={'method':'exact rational finite uniform-measure decomposition per pinned Theorem 4.5 proof','seeds':seeds,'rows':rows,'environment':{'python':sys.version,'platform':platform.platform()},'verdict':'toy','scope':'finite skew-symmetric games; not a proof for arbitrary preference functions'}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    (out/'config.json').write_text(json.dumps({'seeds':seeds,'n':7,'measure':'uniform discrete'},indent=2)+'\n')
    (out/'run.log').write_text('exact-rational finite decomposition completed\n')
    files=['config.json','results.csv','run.log','summary.json']
    (out/'SHA256SUMS').write_text(''.join(f'{hashlib.sha256((out/x).read_bytes()).hexdigest()}  {x}\n' for x in files))
if __name__=='__main__':
 p=argparse.ArgumentParser(); p.add_argument('--out',default='outputs/claim1_finite_decomposition'); p.add_argument('--seeds',nargs='+',type=int,default=[11,23,47,89,131]); a=p.parse_args(); main(a.out,a.seeds)
