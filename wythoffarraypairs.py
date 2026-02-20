import math
from decimal import Decimal

number = Decimal('132')
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')


n = 9999999
m = 2

wythoff = [[Decimal('0') for _ in range(m)] for _ in range(n)]
phi = (Decimal('1') + Decimal(str(math.sqrt(5)))) / Decimal('2')

for i in range(n):
    wythoff[i][0] = Decimal(str(math.floor(math.floor((Decimal(str(i)) + Decimal('1')) * phi) * phi)))
    wythoff[i][1] = Decimal(str(math.floor(math.floor((Decimal(str(i)) + Decimal('1')) * phi) * phi * phi)))

f = open("pairs.txt", "w")

for i in range(n):
    f.write(str(wythoff[i][0]) + "\n")
    f.write(str(wythoff[i][1]) + "\n")
f.close()
