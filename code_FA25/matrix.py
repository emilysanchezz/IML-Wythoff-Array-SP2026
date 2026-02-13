def fibonacci_word_prefix(n: int) -> str:
    s = "A"
    while len(s) < n:
        s = "".join("AB" if c == "A" else "A" for c in s)
    return s[:n]
def generate_matrix(fib_n: int, size: int = 100):

    pattern = fibonacci_word_prefix(fib_n) 
    
   
    col_types = [pattern[j % fib_n] for j in range(size)]  
    
 
    M = [[0] * size for _ in range(size)]
    
   
    M[0][0] = 3
    for x in range(size - 1):  
        if col_types[x] == 'A':
            M[x + 1][x + 1] = M[x][x] + 6
        else:  # 'B'
            M[x + 1][x + 1] = M[x][x] + 4

    for i in range(size):
        for j in range(i + 1, size):
            m = j - 1  
            if col_types[m] == 'A':
                M[i][j] = M[i][j - 1] + 3
            else:  # 'B'
                M[i][j] = M[i][j - 1] + 2

    for i in range(size):
        for j in range(i):
            M[i][j] = M[j][i]
    
    return M

def constant_anti_diagonals(M):

    n = len(M)
    result = []


    for s in range(2 * n - 1):
        vals = []
        for i in range(n):
            j = s - i
            if 0 <= j < n:
                vals.append(M[i][j])

        if len(vals) >= 1 and all(v == vals[0] for v in vals):
            result.append(s + 1)  

    return result


if __name__ == "__main__":

    M2 = generate_matrix(2, size=100)
    diag2 = constant_anti_diagonals(M2)
    print("n=2 anti-diagonals:", diag2[:20])  


    M3 = generate_matrix(3, size=100)
    diag3 = constant_anti_diagonals(M3)
    print("n=3 anti-diagonals:", diag3[:20])

    M5 = generate_matrix(5, size=100)
    diag5 = constant_anti_diagonals(M5)
    print("n=5 anti-diagonals:", diag5[:20])

    M8 = generate_matrix(8, size=100)
    diag8 = constant_anti_diagonals(M8)
    print("n=8 anti-diagonals:", diag8[:20])