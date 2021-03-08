def prefixSum1(X, n):
    S = [0 for i in range(n)]
    for i in range(0, n):
        S[i] = 0
        for j in range(0, i+1):
            S[i] += X[j]
    return S

def prefixSum2(X, n):
    S = [0 for i in range(n)]
    S[0] = X[0]
    for i in range(1, n):
        S[i] = S[i-1] + X[i]
    return S

X = [3, 1, -2, 6, 7]
result_1 = prefixSum1(X, len(X))
result_2 = prefixSum2(X, len(X))
print(result_1)
print(result_2)
