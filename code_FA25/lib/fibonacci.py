from math import *

# The golden ratio.
phi = (1 + sqrt(5)) / 2

# Calculate the n-th Fibonacci number, starting from 0, using Binet's formula.
def fibonacci(n):
    return round((phi**n - (1 - phi)**n) / sqrt(5))
