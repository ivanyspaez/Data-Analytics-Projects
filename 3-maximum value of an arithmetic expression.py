import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def MinAndMax(i, j, m, M, operation):
    minimum = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        a = ops[operation[k - 1]](M[i][k], M[k+1][j])
        b = ops[operation[k - 1]](M[i][k], m[k+1][j])
        c = ops[operation[k - 1]](m[i][k], M[k+1][j])
        d = ops[operation[k - 1]](m[i][k], m[k+1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum

def maxValue(digit, operation):
    n = len(digit)
    m = [[0] * n for _ in range(n)]
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = digit[i]
        M[i][i] = digit[i]
    for s in range(1, n):  # s is the step between i and j
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, operation)
    return M[0][n-1]

expression = input()
n = len(expression)
digit = [int(expression[i]) for i in range(0, n, 2)]
operation = [expression[i] for i in range(1, n, 2)]
print(maxValue(digit, operation))

