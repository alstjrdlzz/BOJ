import sys
input = sys.stdin.readline

dp = [0] * 12
dp[1:4] = [1, 2, 4]

TC = int(input())
for _ in range(TC):
    N = int(input())
    for i in range(4, 12):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[N])