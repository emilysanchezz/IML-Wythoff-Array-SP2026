# Shows how the numbers obtained in `demo_array_pair_indices.py` are
# given by bisections of generalized Fibonacci sequences.
# (The parenthesized terms are the ones that appear as indices.)

from lib import *

# number of rows
I = 10
# number of columns
J = I

for i in range(I):
    x = unbeatty(phi, wythoff(i + 1, 1)) # index of first pair in row
    y = unbeatty(phi, wythoff(i + 1, 3)) # index of second pair in row
    v = y - 2 * x # interpolate the term before x dropped in the bisection
    u = x - v     # interpolate the term before v
    print(f"row {i}: ({u}, {v}) =>", end = "\t")
    for j in range(J):
        (u, v) = (v, u + v) # evolve the generalized Fibonacci sequence forward
        if j % 2 == 0:
            print(f"({v})", end = "\t")
        else:
            print(f"{v}", end = "\t")
    print()
