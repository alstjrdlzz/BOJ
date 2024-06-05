import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]

dp[1] = [1, 2]
for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % 9901            # 안 놓는 경우
    dp[i][1] = (2 * dp[i - 1][0] + dp[i - 1][1]) % 9901        # 한 마리 놓는 경우
    
print(sum(dp[N]) % 9901)