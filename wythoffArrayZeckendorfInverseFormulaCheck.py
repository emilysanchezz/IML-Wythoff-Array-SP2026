"""
Wythoff array inverse test for closed form Zeckendorf formula
Code by Anthony Salemi
"""
import math
from decimal import Decimal

number = Decimal('99829')
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')


def criteria(x, y):
    return (math.floor((y - x) * phi) - x) == 0

n = 10000
m = 10000

wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

f = open("pairs.txt", "r")
for i in range(n):
    pair = f.readline()
    if not pair or pair == "":
        break
    wythoff[i][0] = Decimal(pair)
    wythoff[i][1] = Decimal(f.readline())
f.close()

fib = [0, 1]
while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])
print(fib)
fib = fib[2:]

for j in range(1, n): # verified to 508, socan start at for loop at 508 if you want
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
    
    #print(c)
    #print(z)
    c.reverse()
    for i in range(len(c)):
        if c[i] == 1:
            n = i+1
            break
    
    c.reverse()
    c = c[0:len(c) - n-1]

    #print(c)
    flag = False
    c.reverse()
    #for i in c:
    #    if i != 0:
    #        flag = True
    #if flag:
    k = 0
    for i in c:
        m += fib[k] * i
        k += 1

    tem = m
    m = n
    n = tem

    print(str(number) + " is at: " + str(n) + "x" + str(m))

    nextVal = Decimal('0')
    val1 = Decimal(str(math.floor(math.floor((Decimal(str(n))) * phi) * phi)))
    val2 = Decimal(str(math.floor(math.floor((Decimal(str(n))) * phi) * phi * phi)))

    if (m==1):
        nextVal = val1
    elif (m==2):
        nextVal = val2
    else:
        for i in range(2, m):
            nextVal = val2 + val1
            val1 = val2
            val2 = nextVal

    #print("\n" + str(n) + "x" + str(m) + " value is: " + str(nextVal))
    if number != nextVal:
        print("Error: " + str(n) + "x" + str(m) + " value is " + str(nextVal) + " not equal to " + str(number))
    else:
        print(str(number) + " check")
    n = 10000
    
