# Test whether [i] + [j] > [i], for all i and j.

from lib import *

i = 1
while True:
    for j in range(1, i + 1):
        k = wythoff_add(i, j)
        if k <= i:
            print(f"addition is not increasing ([{i}] + [{j}] = [{k}])")
            exit()
    print(f"finished checking up to i = {i}")
    i += 1
