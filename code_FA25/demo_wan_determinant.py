from lib import *

N = 10

# an implementation of the determinant
def det(A):
    if len(A) == 1:
        if len(A[0]) == 1:
            return A[0][0]
        else:
            raise ValueError("matrix is not of square shape")
    total = 0
    for i in range(len(A)):
        B = [A[k][1:] for k in range(len(A)) if k != i] # rowwise minor
        total += (-1)**i * A[i][0] * det(B)
    return total

for n in range(1, N + 1):
    A = [[wan(i, j) for j in range(1, n + 1)] for i in range(1, n + 1)]
    d = det(A)
    print(f"n = {n}, det = {d}")
