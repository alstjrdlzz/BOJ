import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        else:
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

print(max(map(max, dp)) ** 2)