import sys
input = sys.stdin.readline


def matmul(a, b):
    mat = [[0] * len(a) for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                mat[i][j] += (a[i][k] * b[k][j]) % 1000
    return mat


def square(mat, n):
    if n == 1:
        return mat

    if n % 2 == 0:
        tmp = square(mat, n // 2)
        return matmul(tmp, tmp)
    else:
        return matmul(square(mat, n - 1), mat)


N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

ans = square(mat, B)
for i in range(N):
    for j in range(N):
        ans[i][j] %= 1000
        
for row in ans:
    print(*row)