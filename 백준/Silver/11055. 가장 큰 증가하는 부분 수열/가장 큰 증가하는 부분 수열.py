import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N
dp[0] = lst[0]
for i in range(1, N):
  for j in range(i):
    if lst[j] < lst[i]:
        dp[i] = max(dp[i], dp[j] + lst[i])
    else:
        dp[i] = max(dp[i], lst[i])

print(max(dp))