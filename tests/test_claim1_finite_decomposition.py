from fractions import Fraction
from src.claim1_finite_decomposition import fixture,decompose,add,inner,zero_marginal,skew

def test_exact_decomposition_properties():
 for seed in [11,23,47,89,131]:
  a=fixture(seed); _,t,c=decompose(a)
  assert skew(a) and skew(t) and skew(c)
  assert add(t,c)==a and zero_marginal(c)
  assert inner(t,c)==0

def test_nonconstant_potential_breaks_zero_marginal():
 a=fixture(11); n=len(a); q=[Fraction(i) for i in range(n)]
 c=[[a[i][j]-(q[i]-q[j]) for j in range(n)] for i in range(n)]
 assert not zero_marginal(c)
