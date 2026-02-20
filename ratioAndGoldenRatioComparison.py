"""
Wythoff array element ratio and golden ratio comparison
Code by Anthony Salemi
"""

import math
from decimal import Decimal
#import wythoffArrayGeneration as w

n = 517 # rows 
m = 8 # columns 
"""
verified to:
952 rows, 61 columns, bigger columns are difficult because of floating point
9999999 rows, 3 columns
as far as i could on 99999999 rows, 3 columns before running out of memory
"""

wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

for i in range(n):
    wythoff[i][0] = Decimal(str(math.floor(math.floor((Decimal(str(i)) + Decimal('1')) * phi) * phi)))
    wythoff[i][1] = Decimal(str(math.floor(math.floor((Decimal(str(i)) + Decimal('1')) * phi) * phi * phi)))

def fib(x, y):
    return wythoff[x][y-1] + wythoff[x][y-2]


for i in range(2, m):
    wythoff[0][i] = fib(0, i)

for i in range(1, n): # across rows
    for j in range(2, m): # across columns
        wythoff[i][j] = fib(i, j)

flag = False
for i in range(1, n): # across rows
    for j in range(1, m): # across columns
        dif = abs(wythoff[i][j]/phi - wythoff[i][j-1])
        if (dif > Decimal('0.5')):
            print("Error at " + str(i + 1) + " " + str(j + 1))
            print(dif)            
            flag = True

if (not(flag)):
    print("No errors")

