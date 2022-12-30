def kron_delta(i,j):
    if i == j:
        return 1
    else:
        return 0

def Fdcoeff(stenc,d):
    N = len(stenc)
    A = np.zeros((N,N))
    B = np.zeros(N)
    for a in range(N):
        A[a] = stenc**a
        B[a] = kron_delta(a,d)*math.factorial(d)
    return linalg.solve(A,B)
