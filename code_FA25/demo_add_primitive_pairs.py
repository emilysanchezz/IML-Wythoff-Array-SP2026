from lib import *

i = 1
s = set()
while True:
    (a1, b1) = primitive_wythoff_pair(i)
    for j in range(1, i + 1):
        (a2, b2) = primitive_wythoff_pair(j)
        (c, d) = (a1 + a2, b1 + b2)
        (f, g) = (c + d, c + 2 * d)
        k = primitive_wythoff_pair_index(c, d)
        l = primitive_wythoff_pair_index(f, g)
        if k != None:
            s.add(i)
            s.add(j)
            print(f"{i}, {j}, {k}")
    # print(f"checked i = {i}")
    i += 1
    if i == 101:
        print(s)
        break
