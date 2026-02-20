"""
Wythoff array inverse test
Code by Anthony Salemi
"""
import math
from decimal import Decimal

size = 50
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')


def criteria(x, y):
    return (math.floor((y - x) * phi) - x) == 0

n = 1000
m = 2

wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

loc = [[Decimal('0') for _ in range(2)] for _ in range(size + 1)]

f = open("pairs.txt", "r")
i = 0
for i in range(1, 1000):
    pair = f.readline()
    if not pair or pair == "":
        break
    wythoff[i][0] = Decimal(pair)
    wythoff[i][1] = Decimal(f.readline())
    i += 1
f.close()

for j in range(1, size + 1):
    number = j
    m = 1
    
    flag = True
    for i in range(len(wythoff)):
        if number in wythoff[i]:
            flag = False
            n = i + 1
            if number == wythoff[i][1]:
                m = 2
    if flag:
        m = 1
        num1 = number
        num2 = round(num1 / phi)
        m += 1
        flag = True

        while flag:
            if criteria(num2, num1):
                for i in range(n):
                    if num1 in wythoff[i]:
                        flag = False
                        n = i + 1
                        break
            if (flag):
                m += 1
                val = num1
                num1 = num2
                num2 = val - num2
    loc[j][0] = n-1
    loc[j][1] = m
    print(str(number) + " is at: " + str(n-1) + "x" + str(m))
    n = size


def dist(x, y):
    return abs((float(loc[x][0]) - float(loc[y][0])) + abs((float(loc[x][1]) - float(loc[y][1]))))
    
for i in range(1, size + 1):
    line = ""
    for j in range(1, i + 1):
        line += str(dist(i, j)) + ","
    print(line)

print(loc)
