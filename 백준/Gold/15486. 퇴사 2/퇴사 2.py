import sys
input = sys.stdin.readline

N = int(input())
T, P = [0] * N, [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if i + T[i] <= N:
        dp[i] = max(dp[i + T[i]] + P[i], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
        
print(dp[0])