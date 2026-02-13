import math
import numpy as np
import matplotlib.pyplot as plt

g = (1 + math.sqrt(5)) / 2 
# Here, we define our golden ratio

def wythoff_pairs(N: int):
    """Return first N Wythoff pairs (a_n, b_n)"""
    A = [int(math.floor(n * g)) for n in range(1, N + 1)]
    B = [int(math.floor(n * g ** 2)) for n in range(1, N + 1)]
    return list(zip(A, B))
#Here, we define our an and bn, and return the first N pairs.

def l1_origin_dist(p):
    """Taxicab/L1 distance to origin"""
    x, y = p
    return abs(x) + abs(y)
# Here, we define the L1 distance to origin.

N = 5000
# We want to analyze the first 5000 Wythoff pairs.
pairs = wythoff_pairs(N)
l1_vals = np.array([l1_origin_dist(p) for p in pairs], dtype=float)
n_index = np.arange(1, N + 1, dtype=float)
theory = (2 * g + 1) * n_index
errors = l1_vals - theory
# Here, we calculate the actual L1 distances, theoretical values, and errors.

avg_err = float(np.mean(errors))
err_min = float(np.min(errors))
err_max = float(np.max(errors))
# Here, we compute the average, minimum, and maximum errors.

print(f"Average error: {avg_err:.6f}")
print(f"Error range: [{err_min:.6f}, {err_max:.6f}]")
# Here, we print the error statistics.

plt.figure(figsize=(8, 5))
plt.plot(n_index, l1_vals, label="Actual L1 distance a_n + b_n")
plt.plot(n_index, theory, label="Theoretical (2φ + 1)·n")
plt.xlabel("n")
plt.ylabel("Distance")
plt.title("L1 distance of Wythoff pairs vs. theory")
plt.legend()
plt.tight_layout()
plt.show()
# Here, we plot the actual L1 distances and theoretical values.

plt.figure(figsize=(8, 5))
plt.hist(errors, bins=60)
plt.xlabel("Error (actual - theory)")
plt.ylabel("Frequency")
plt.title("Error distribution histogram (bounded oscillation)")
plt.tight_layout()
plt.show()
# Here, we plot the histogram of errors.

plt.figure(figsize=(8, 4.8))
plt.plot(n_index, errors)
plt.xlabel("n")
plt.ylabel("Error")
plt.title("Error variation with n (bounded)")
plt.tight_layout()
plt.show()
# Here, we plot the error variation with n.


# Conclusion:
# For graph 1, the blue curve and the orange curve are very close. We can conlude that the L1 distance of Wythoff pairs grows approximately as (2φ + 1)·n.
# For graph 2, the error is between -2 and 0. And the distribution is relatively uniform, with the center around -1. We can conclude that the error is bounded.
# For graph 3, The error curve is like a sawtooth, fluctuating between -2 and 0, without a trend drift. we can conclude that the error term is -2{nφ}, So it is always controlled by the decimal part of the multiples of the golden ratio.
# Overall, we can conclude that the L1 distance of Wythoff pairs grows approximately as (2φ + 1)·n, with a bounded oscillating error term.
