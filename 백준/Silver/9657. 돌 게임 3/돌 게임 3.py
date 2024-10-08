import sys
input = sys.stdin.readline

N = int(input())

dp = ["SK", "CY", "SK", "SK"]
for i in range(4, N):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY" or dp[i - 4] == "CY":
        dp.append("SK")
    else:
        dp.append("CY")
        
print(dp[N - 1])