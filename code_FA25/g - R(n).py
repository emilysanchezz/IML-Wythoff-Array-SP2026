import numpy as np
import math
import matplotlib.pyplot as plt
phi = (1 + 5**0.5) / 2
def wythoff_pair(n):
    A = math.floor(n * phi)
    B = A + n  
    return A, B
N = 500
ns = np.arange(1, N+1)
A = np.array([wythoff_pair(n)[0] for n in ns], dtype=float)
B = A + ns
R = B / A
err = phi - R  
# A(n) = floor(phi * n)
t = np.floor(phi * ns)
lower = -1.0 / (phi * (phi - 1.0 / t) * t)
upper = -(2 - phi) / (phi * (phi - (2 - phi) / t) * t)

plt.figure(figsize=(8,5))
plt.plot(ns, err, label="g - R(n)", color="orange")
plt.plot(ns, lower, linestyle='--', label="lower bound")
plt.plot(ns, upper, linestyle='--', label="upper bound")
plt.xlabel("n")
plt.ylabel("g - R(n)")
plt.title("Error g - R(n) with bounds")
plt.legend()
plt.tight_layout()
plt.show()

