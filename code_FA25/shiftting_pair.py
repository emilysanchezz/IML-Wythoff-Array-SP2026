from lib import wythoff, wythoff_add

def get_row_prefix(i, m):
    return [wythoff(i, j) for j in range(1, m + 1)]

def converges_with_pair_shift(i1, i2, length=12, debug=False, cache=None):
    if cache is None:
        cache = {}

    need = length + 2  

    if (i1, need) not in cache:
        cache[(i1, need)] = get_row_prefix(i1, need)
    if (i2, need) not in cache:
        cache[(i2, need)] = get_row_prefix(i2, need)

    row_i1 = cache[(i1, need)]
    row_i2 = cache[(i2, need)]


    sum_seq = [row_i1[k] + row_i2[k] for k in range(need)]

    z = wythoff_add(i1, i2)
    if (z, need) not in cache:
        cache[(z, need)] = get_row_prefix(z, need)
    row_z = cache[(z, need)]

    # No shift
    if sum_seq[:length] == row_z[:length]:
        if debug:
            print(f"({i1},{i2}) -> Row {z}  [0 pair shift]")
        return True, z, 0

    # Shift 1
    if sum_seq[2:2 + length] == row_z[:length]:
        if debug:
            print(f"({i1},{i2}) -> Row {z}  [+1 pair shift on SUM]")
        return True, z, ("sum", 1)

    if debug:
        print(f"❌ Contradiction at ({i1},{i2}) → expect Row {z}")
        print("sum_seq        :", sum_seq[:length + 2])
        print("target (z=...) :", row_z[:length + 2])

    return False, None, None

def check_all_pairs(limit=1000, length=12, progress_every=100):

    cache = {}
    total = 0
    for i in range(1, limit + 1):
        for j in range(1, i + 1):
            total += 1
            ok, z, shift = converges_with_pair_shift(i, j, length=length, cache=cache)
            if not ok:
                print(f"❌ Contradiction found at ({i}, {j})")
                return (i, j)
        if progress_every and (i % progress_every == 0):
            print(f"✅ Checked up to Row {i}")
    print(f"\n✅ All {total} pairs (1 ≤ i,j ≤ {limit}) converge with ≤1 Wythoff pair shift.")
    return None

if __name__ == "__main__":

    check_all_pairs(limit=100, length=12)