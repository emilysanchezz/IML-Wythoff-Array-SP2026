"""
Wythoff array Zeckendorf Hamming distance table
Code by Anthony Salemi
"""

n = 100
m = 100

fib = [0, 1]
while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])
print(fib)
fib = fib[2:]

zeck = [[]]

for j in range(1, n):
    number = j
    m = 1

    # Determine Zeckendorf Representation
    z = []
    c = []
    num = j
    for f in reversed(fib):
        if f <= num:
            z.append(f)
            c.append(1)
            num -= f
        else:
            c.append(0)

    zeck.append(c)



def dist(x, y):
    d = 0
    if x > y:
        length = len(zeck[x])
    else:
        length = len(zeck[y])
    ytem = zeck[x][::-1]
    xtem = zeck[y][::-1]
    for i in range(length):
        ytem.append(0)
        xtem.append(0)
        if (xtem[i] != ytem[i]):
            d += 1
    return d


for i in range(1, n):
    line = ""
    for j in range(1, i + 1):
        line += str(dist(i, j)) + ","
    print(line)


    
