import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [0] * (N + 1)
mx = 0
for i in lst:
    dp[i] = dp[i - 1] + 1
    mx = max(dp[i], mx)
    
print(N - mx)