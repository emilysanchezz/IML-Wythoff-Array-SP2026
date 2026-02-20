"""
Wythoff array inverse test
Code by Anthony Salemi
"""
import math
from decimal import Decimal

number = Decimal('99829')
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')


def criteria(x, y):
    return (math.floor((y - x) * phi) - x) == 0

n = 9999999
m = 2

"""
CAN RUN A LOT FASTER IF ONE USES LESS PRIMITIVE PAIRS
"""

wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

f = open("pairs.txt", "r")
i = 0
while True:
    pair = f.readline()
    if not pair or pair == "":
        break
    wythoff[i][0] = Decimal(pair)
    wythoff[i][1] = Decimal(f.readline())
    i += 1
f.close()

for j in range(1, n): # verified to 508, socan start at for loop at 508 if you want
    number = j
    m = 1

    flag = True
    for i in range(n):
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

        #print(str(number) + " is at: " + str(n) + "x" + str(m))

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
    n = 9999999
    

