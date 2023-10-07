import sys
input = sys.stdin.readline


def solution():
    for i in range(1, n):
        m = len(d[i])
        for j in range(m):
            if j == 0:
                d[i][j] = d[i - 1][j] + d[i][j]
            elif j == m - 1:
                d[i][j] = d[i - 1][j - 1] + d[i][j]
            else:
                d[i][j] = max(d[i - 1][j - 1], d[i - 1][j]) + d[i][j]
    return max(d[n - 1])


n = int(input())
d = []
for _ in range(n):
    d.append(list(map(int, input().split())))
    
print(solution())
            