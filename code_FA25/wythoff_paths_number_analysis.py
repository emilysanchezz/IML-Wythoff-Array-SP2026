import math
import numpy as np
import matplotlib.pyplot as plt

phi = (1 + math.sqrt(5)) / 2
def wythoff_pairs(N):
    A = [int(math.floor(n*phi)) for n in range(1, N+1)]
    B = [int(math.floor(n*phi**2)) for n in range(1, N+1)]
    return list(zip(A, B))

def nCr(n, r):
    from math import comb
    return comb(n, r)
# number of combinations n choose r

def paths_count_for_wythoff(N=200):
    data = []
    for i, (a, b) in enumerate(wythoff_pairs(N), start=1):
        cnt = nCr(a + b, a)        
        data.append((i, a, b, a + b, cnt, math.log(cnt)))
    return data
# We generate first 200 Wythoff pairs and compute the number of shortest L1 paths.

def log_nCr_stirling(n, r):
    def stirling_log_fact(k):
        if k == 0: return 0.0
        return k*math.log(k) - k + 0.5*math.log(2*math.pi*k)
    return stirling_log_fact(n) - stirling_log_fact(r) - stirling_log_fact(n-r)
# Stirling's approximation for log(n choose r)


N = 200
data = paths_count_for_wythoff(N)
n_vals = [row[0] for row in data]
l1_vals = [row[3] for row in data]
log_counts = [row[5] for row in data]
# Here, we extract n, L1 distance, and log(count) from the data.

plt.figure(figsize=(8,5))
plt.plot(n_vals, log_counts, label="log(#paths)")
plt.xlabel("n (index of Wythoff pair)")
plt.ylabel("log(number of shortest paths)")
plt.title("Log(number of shortest L1 paths) vs n")
plt.legend()
plt.tight_layout()
plt.show()
# Here, we plot log(count) vs n.

plt.figure(figsize=(8,5))
plt.plot(l1_vals, log_counts, label="log(#paths)")
plt.xlabel("L1 distance (a_n + b_n)")
plt.ylabel("log(number of shortest paths)")
plt.title("Log(number of shortest L1 paths) vs L1 distance")
plt.legend()
plt.tight_layout()
plt.show()
# Here, we plot log(count) vs L1 distance.

log_counts_stirling = [log_nCr_stirling(a+b, a) for (_,a,b,_,_,_) in data]

plt.figure(figsize=(8,5))
plt.plot(n_vals, log_counts, label="Actual log(#paths)")
plt.plot(n_vals, log_counts_stirling, '--', label="Stirling approx")
plt.xlabel("n (index of Wythoff pair)")
plt.ylabel("log(number of shortest paths)")
plt.title("Comparison: Actual vs Stirling approximation")
plt.legend()
plt.tight_layout()
plt.show()
# Here, we compare actual log(count) with Stirling's approximation.

# Conclusion:
# The number of shortest L1 paths to Wythoff pairs grows extremely fast, roughly exponentially.
# The Stirling's approximation closely matches the actual log(count), validating its accuracy for large values.
# The plots show that log(count) increases linearly with both n and L1 distance, indicating exponential growth in count.
# This reflects the combinatorial explosion in the number of shortest paths as the coordinates increase.