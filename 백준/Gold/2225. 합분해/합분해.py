import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[1] * (K + 1) for _ in range(N + 1)]

dp[1] = [j for j in range(K+1)]

for i in range(2, N + 1):
    for j in range(2, K + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[N][K] % 10**9)