import sys
input = sys.stdin.readline


N, K = map(int, input().split())
sset = set(int(input()) for _ in range(N))

INF = K + 1
dp = [INF] * (K + 1)
dp[0] = 0

for coin in sset:
    for j in range(1, K + 1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j - coin] + 1)
            
ans = dp[K]
if ans == INF:
    ans = -1
print(ans)