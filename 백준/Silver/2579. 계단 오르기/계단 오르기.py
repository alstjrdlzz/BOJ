import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 301
for i in range(N):
    lst[i + 1] = int(input())

dp = [0] * 301

dp[1] = lst[1]
dp[2] = lst[1] + lst[2]
dp[3] = max(lst[1], lst[2]) + lst[3]
for i in range(4, 301):
    dp[i] = max(dp[i - 3] + lst[i - 1], dp[i - 2]) + lst[i]

print(dp[N])