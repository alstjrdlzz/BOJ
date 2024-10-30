import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = [int(input()) for _ in range(M)]

dp = [1] * (42)
dp[2] = 2
for i in range(3, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

if M > 0:
    ans, start = 1, 0
    for end in lst:
        ans *= dp[end - start - 1]
        start = end
    ans *= dp[N - start]
else:
    ans = dp[N]
    
print(ans)