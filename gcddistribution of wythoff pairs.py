from math import floor, sqrt, gcd, pi 
from collections import Counter
from typing import Dict, List, Tuple

##golden ratio 
phi = (1 + sqrt(5)) / 2

"""
a(n) definiton 
as phi is irrational, the fractional parts of {n*phi} are uniformly distributed in [0,1)
"""
def a(n: int) -> int:
    return floor(n * phi)
"""
gcd function definition using the simplification of gcd(a(n), b(n)) = gcd(a(n), n), problem simplification via 
Bezout's Identity/Divisibility Arguments 
"""
def g(n: int) -> int:
    return gcd(a(n), n)

## list generation of [g(1), g(2), ... g(N)], finite sample size for approximating the asymptotic distribution 
def sample_gcds(N: int) -> List[int]:
    return [g(n) for n in range(1, N + 1)]
"""
theoretical values of the probability distribution of n = gcd(a(n),n), refer to notes 
i) floor(nphi) is asymptotically uniform mod m, divisibility behaves randomly
ii) P(d|n, d|a(n)) ~ 1/d^2
iii) By Mobius Inversion and Number Theory Thms, P(gcd(a(n),n) = d) ~ 6/(pi*d)^2 
"""
def theory_p_g_equals(d: int) -> float:
    return 6 / (pi * pi * d * d)

"""
{ d : (count, empirical probability)}
count = #{n<=N | g(n)=d}, empirical probability = count/N 
"""
def full_g_distribution(N: int) -> Dict[int, Tuple[int, float]]:
    values = sample_gcds(N)
    counts = Counter(values)
    return {d: (counts[d], counts[d] / N) for d in sorted(counts)}

##gives comparison of the empirical and theoretical distribution 
def compare_g_equals_theory(N: int, max_d: int = 30) -> None:
    dist = full_g_distribution(N)

    print(f"N={N}")
    print(" d    count     emp_P(g=d)     theory_P(g=d)     diff")

    for d in dist:
        if d > max_d:
            break
        count, emp = dist[d]
        theo = theory_p_g_equals(d)
        print(f"{d:2d}  {count:7d}   {emp:12.8f}   {theo:12.8f}   {emp-theo:+.2e}")

## compute probability for a single value of d 
def prob_g_equals_d(N: int, d: int) -> Tuple[int, float, float]:
    dist = full_g_distribution(N)
    count = dist.get(d, (0, 0.0))[0]
    emp = count / N
    theo = theory_p_g_equals(d)
    return count, emp, theo
"""
N = sample size 
as N increases, better approximation to the asymptotic distribution 
"""
if __name__ == "__main__":
    N = 200000

    max_d = 100
    compare_g_equals_theory(N, max_d=max_d)

    print("\nSingle value check:\n")
    for d in [1, 2, 3, 5, 10, 25, 50]:
        count, emp, theo = prob_g_equals_d(N, d)
        print(f"d={d:2d}  count={count:7d}  emp={emp:12.8f}  theory={theo:12.8f}  diff={emp-theo:+.2e}")
"""
Collective Output: gives d, empirical P(g=d), and compares this to the theoretical value up until our "max_d"
Single Value Check: can test particular values of d, compares using same structure 
"""
