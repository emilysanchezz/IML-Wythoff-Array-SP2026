from math import *

# Calculate the n-th term of the Beatty sequence of r.
def beatty(r, n):
    return floor(n * r) # it's just that simple

# Determine the indices, if any, at which x appears in the Beatty sequence
# of r.
def unbeatty(r, x):
    if abs(r) < 1: # guarantees that the result will be unique
        raise ValueError("r passed to unbeatty must have magnitude at least 1")
    lower_bound = ceil(x / r)
    upper_bound = floor((x + 1) / r)
    if lower_bound == upper_bound:
        return lower_bound
    else:
        return None
