import sys
input = sys.stdin.readline
INF = 1e10

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for k in range(3):
        dp[0][j][k] = arr[0][j]

for i in range(1, N):
    for j in range(M):
        if j == 0:
            dp[i][j][0] = INF
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + arr[i][j]
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + arr[i][j]
        elif j == M - 1:
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + arr[i][j]
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + arr[i][j]
            dp[i][j][2] = INF
        else:
            dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + arr[i][j]
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + arr[i][j]
            dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + arr[i][j]
            
ans = INF
for j in range(M):
    for k in range(3):
        ans = min(ans, dp[N - 1][j][k])
        
print(ans)                