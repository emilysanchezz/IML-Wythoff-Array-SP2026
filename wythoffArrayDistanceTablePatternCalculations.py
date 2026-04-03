"""
Wythoff array distance table pattern exploration
Code by Anthony Salemi
"""
import math
from decimal import Decimal

size = 500
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')


def criteria(x, y):
    return (math.floor((y - x) * phi) - x) == 0

n = size
m = 2

wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

loc = [[Decimal('0') for _ in range(2)] for _ in range(size + 1)]

f = open("pairs.txt", "r")
i = 0
for i in range(1, n):
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
    return abs(loc[x][0]-loc[y][0]) + abs(loc[x][1]-loc[y][1])
    #return math.sqrt((loc[x][0] - loc[y][0])**2 + (loc[x][1] - loc[y][1])**2)

distanceTable = [[Decimal('0') for _ in range(size+1)] for _ in range(size+1)] # 1-indexed

for i in range(1, size + 1): # tabulate distances for printing
    line = ""
    for j in range(1, i + 1):
        distance = dist(i, j)
        line += str(distance) + ","
        distanceTable[i][j] = distance # update distanceTable array (1-indexed)
    #print(line)

#print(loc) # location data of each element

pattern = []

# pattern analysis
for i in range(2, size): # calculate up/middle/down addition pattern at the boundary
    top = distanceTable[i][i-1]
    mid = distanceTable[i+1][i-1]
    bot = distanceTable[i+1][i]
    if (top + mid == bot):
        pattern.append("down")
    elif (top + bot == mid):
        pattern.append("middle")
    else:
        pattern.append("up")
print(pattern)

# check larger pattern of up/middle/down/down/down and up/middle/down
sequence = []

i = 4

while i < len(pattern) - 5:
    if (pattern[i] == "up" and pattern[i+1] == "middle" and pattern[i+2] == "down" and pattern[i+3] == "down" and pattern[i+4] == "down"):
        sequence.append(0)
        i += 5
    elif (pattern[i] == "up" and pattern[i+1] == "middle" and pattern[i+2] == "down"):
        sequence.append(1)
        i += 3
    else:
        i += 1
        sequence.append(-1)

print(sequence)

