"""
Wythoff array and element generation
Code by Anthony Salemi
"""

import math
from decimal import Decimal

"""
This section prints the full nxm Wythoff array, edit the n and m values below.
It seems to work well with printing on the order of 100x100, after that at least
my setup starts to run into issues with printing that many characers.
"""

n = 1000 # rows
m = 1000 # columns

if (n < 1):
    n = 1
if (m < 2):
    m = 2


wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

for i in range(n):
    wythoff[i][0] = Decimal(str(math.floor(math.floor((Decimal(str(i)) + Decimal('1')) * phi) * phi)))
    wythoff[i][1] = Decimal(str(math.floor(math.floor((Decimal(str(i)) + Decimal('1')) * phi) * phi * phi)))


def printWythoff():
    for i in range(n):
        stringToPrint = ""
        for j in range(m):
            stringToPrint += str(wythoff[i][j]) + ", "
        print(stringToPrint)


def fib(x, y):
    return wythoff[x][y-1] + wythoff[x][y-2]


for i in range(2, m):
    wythoff[0][i] = fib(0, i)

for i in range(1, n): # across rows
    for j in range(2, m): # across columns
        wythoff[i][j] = fib(i, j)
        

printWythoff()


"""
This section prints a specific value of the Wythoff array without computing other rows.
Edit the n and m values below to specify the desired element.
My setup does not overflow until on the order of 10000000x10000000.
"""

n = 1000000 # row
m = 1000000 # column

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

print("\n" + str(n) + "x" + str(m) + " value is: " + str(nextVal))


