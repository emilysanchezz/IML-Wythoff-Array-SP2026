# Lists the indices of the Wythoff pairs as they appear in the Wythoff array.

from lib import *

# number of rows
I = 10
# number of columns
J = I

for i in range(I):
    for j in range(J):
        x = unbeatty(phi, wythoff(i + 1, 2 * j + 1))
        print(x, end = "\t")
    print()
