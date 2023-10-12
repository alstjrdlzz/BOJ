import sys
input = sys.stdin.readline
INF = 2 ** 31


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0
    
for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
        dist = j - i
        for k in range(dist):
            dp[i][j] = min(
                dp[i][j],
                dp[i][i + k] + dp[i + k + 1][j] + s[i][0] * s[i + k][1] * s[j][1]
            )
            
print(dp[0][-1])