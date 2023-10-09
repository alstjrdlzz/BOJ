import sys
input = sys.stdin.readline


def my_lcs(s):
    _s = s[::-1]
    d = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == _s[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i][j - 1], d[i - 1][j])
    return d[n][n]


n = int(input())
s = list(map(int, input().split()))

ans = n - my_lcs(s)

print(ans)