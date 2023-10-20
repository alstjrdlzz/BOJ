import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

_dp = [1] * n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j]:
            _dp[i] = max(_dp[i], _dp[j] + 1)

res = []
for i in range(n):
    res.append(dp[i] + _dp[i] - 1 )

print(max(res))