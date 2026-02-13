from .beatty import *
from .fibonacci import *
import math

# Calculate the n-th Wythoff pair.
def wythoff_pair(n):
    a = beatty(phi, n)
    return (a, a + n)

# Determine whether (a, b) is a Wythoff pair.
# If it is, return the index of that pair; if not, return None.
def wythoff_pair_index(a, b):
    n = unbeatty(phi, a)
    if n != None and b == a + n:
        return n
    else:
        return None

# Calculate the n-th primitive Wythoff pair.
def primitive_wythoff_pair(n):
    return wythoff_pair(beatty(phi, n))

# Determine the primitive Wythoff pair which generates the Wythoff pair (a, b).
def primitivize(a, b):
    if wythoff_pair_index(a, b) is None:
        raise ValueError("(a, b) passed to primitivize must be a Wythoff pair")
    def _primitivize(a, b):
        d = b - a
        c = a - d
        if wythoff_pair_index(c, d) is None:
            return (a, b)
        else:
            return _primitivize(c, d)
    return _primitivize(a, b)

# Determine whether (a, b) is a primitive Wythoff pair.
# If it is, return the index of that pair; if not, return none.
#
# (Note that this index is as a *primitive* Wythoff pair!
# For example, (4, 7) is the second primitive Wythoff pair, so even though
# it is the third Wythoff pair, primitive_wythoff_pair_index(4, 7) = 2.)
def primitive_wythoff_pair_index(a, b):
    n = wythoff_pair_index(a, b)
    if n is None:
        return None
    return unbeatty(phi, n)

# Calculate the element of the Wythoff array in the i-th row and the
# j-th column (where i and j start from 1).
_wythoff_cache = {}
def wythoff(i, j):
    if i <= 0:
        raise ValueError("i passed to wythoff must be positive")
    if j <= 0:
        raise ValueError("j passed to wythoff must be positive")
    def _wythoff(i, j):
        if j == 1:
            return beatty(phi, beatty(phi, i))
        elif j == 2:
            return beatty(phi**2, beatty(phi, i))
        else:
            return wythoff(i, j - 1) + wythoff(i, j - 2)
    if (i, j) not in _wythoff_cache:
        _wythoff_cache[(i, j)] = _wythoff(i, j)
    return _wythoff_cache[(i, j)]

# Returns a function representing the sequence that is the i-th row of the
# Wythoff array.
def wythoff_row(i):
    return lambda j: wythoff(i, j)

# Let seq be a Fibonacci sequence (represented by a function
# from integers to integers), which is assumed to be indexed from 1.
# Determine the index of the row of the Wythoff array which is equivalent to seq
# (in the sense of differing in only finitely many terms, up to shifting).
def equivalent_wythoff_row(seq, debug = False):
    i = 1 # the current position in seq
    while True:
        (a, b) = (seq(i), seq(i + 1))
        if wythoff_pair_index(a, b) != None:
            # likely not necessary, since we reach the primitive first anyway
            (c, d) = primitivize(a, b)
            result = primitive_wythoff_pair_index(c, d)
            assert result != None
            if debug:
                print(f"pair ({a}, {b}), starting at index {i}, is a Wythoff pair")
                print(f"its primitivization is ({c}, {d})")
            return result
        else:
            i += 2

# Determine the index of the row of the Wythoff array which is equivalent to the
# sum of the (i1)-th and the (i2)-th rows of the Wythoff array.
def wythoff_add(i1, i2, debug = False):
    seq = lambda j: (wythoff(i1, j) + wythoff(i2, j))
    return equivalent_wythoff_row(seq, debug)

# The "Wythoff annihilator function".
def wan(x, y):
    return beatty(phi, y - x) - x

# Checks if sum of two rows converges at the second pair of a different row
# match returns true or false
def convergence_at_secondpair(i1, i2, length=10):
    target_row = wythoff_add(i1, i2)
    sum_seq = [wythoff(i1, j) + wythoff(i2, j) for j in range(1, length+1)]
    target_seq = [wythoff(target_row, j) for j in range(1, length+1)]
    
    match = sum_seq[2:][:2] == target_seq[:2]
    #comparing second pair

    # print(f"Row {i1} + Row {i2} converges to Row {target_row}")
    # print(f"Sum sequence: {sum_seq}")
    # print(f"Target row sequence: {target_seq}")
    # print(f"Match for second pair {match}")
    
    return match

# Checks if sum of two rows converges at the first pair of a different row
# match returns true or false
def convergence_at_firstpair(i1, i2, length=10):
    target_row = wythoff_add(i1, i2)
    sum_seq = [wythoff(i1, j) + wythoff(i2, j) for j in range(1, length+1)]
    target_seq = [wythoff(target_row, j) for j in range(1, length+1)]

    match = sum_seq[:2] == target_seq[:2]
    #comparing first pair

    # print(f"Row {i1} + Row {i2} converges to Row {target_row}")
    # print(f"Sum sequence: {sum_seq}")
    # print(f"Target row sequence: {target_seq}")
    # print(f"Match for first pair {match}")

    return match

# Runs on infinite loop until find ONE contradiction to idea
def find_until_contradiction(length=100):
    i1, i2 = 1, 1
    while True: # run until don't find a sum of two rows converging to first or second pair
        if not (convergence_at_secondpair(i1, i2, length) or 
                convergence_at_firstpair(i1, i2, length)):
            print(f"Contradiction found at ({i1}, {i2})")
            return (i1, i2)

        i2 += 1
        if i2 > i1:
            print(i1)
            i1 += 1
            i2 = 1
        # print(i1,i2) # tried and went up to 1k, but i stopped

def recurrence_relation(row):
    f_n_2 = wythoff_row(row)(2)
    f_n_1 = wythoff_row(row)(1)
    f_n_3 = wythoff_row(row)(3)
    list_of_c = []

    for c in range(0,100):
        formula = (f_n_2**2 + (c * -1))/f_n_1
        if f_n_3 == formula:
            list_of_c.append(c)
        else:
            continue
    return list_of_c

#print(recurrence_relation(2))

# Dr.Stolarsky was correct about c = F_2**2 - F_1*F_3
def verify_equation(row):
    c_value = recurrence_relation(row)
    f_n_2 = wythoff_row(row)(2)
    f_n_1 = wythoff_row(row)(1)
    f_n_3 = wythoff_row(row)(3)
    equation = f_n_2**2 - (f_n_1 * f_n_3)
    return equation == c_value[0]

#print(verify_equation(1))

#gives an estimation of our 4th element (3rd index)
#close to our 4th column, but off by one, not exact
def three_recurrence_relation(row):
    f_n_1 = wythoff_row(row)(2)
    f_n = wythoff_row(row)(1)
    f_n_2 = wythoff_row(row)(3)
    a_n,b_n = wythoff_pair(row)
    f_n_3 = wythoff_row(row)(4)

    formula = math.ceil(((f_n_2 * b_n * (f_n_1 + 1) - f_n) / (a_n * (f_n_1 + 1))))
    no_cel_formula = (((f_n_2 * b_n * (f_n_1 + 1) - f_n) / (a_n * (f_n_1 + 1))))
    return formula, no_cel_formula

#print(three_recurrence_relation(3))

#Agrees with Table 1 in notes
def k_n_table_creator(period, N=10):   
    curr = "1"
    prev = "0"
    final_sequence = [prev, curr] #initial

    for i in range(2, N):
        next = curr + prev

        if len(next) >= period:
            k_n = next[:period]
        else:
            k_n = next

        final_sequence.append(k_n)
        curr, prev = next, curr

    return final_sequence
print(k_n_table_creator(10))
# Array shows when the sequences converges/freezes


