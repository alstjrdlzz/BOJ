import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] *  2 for _ in range(N + 1)]
dp[0] = [1, 0]
for i in range(1, N + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

print(*dp[N])