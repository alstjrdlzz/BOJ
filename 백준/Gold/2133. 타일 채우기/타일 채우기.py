import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (31)
dp[2] = 3

for i in range(4, N + 2, 2):
    dp[i] += (3 * dp[i - 2] + 2)
    for j in range(4, i + 2, 2):
        dp[i] += 2 * dp[i - j]

print(dp[N])