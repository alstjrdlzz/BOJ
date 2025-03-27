import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sset = set(int(input()) for _ in range(M))
    
K = int((2 * N) ** 0.5) + 1

dp = [[10001] * (K + 1) for _ in range(N + 1)]
dp[1][0] = 0
for i in range(2, N + 1):
    if i in sset:
        continue
    for j in range(1, K):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
        
ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)