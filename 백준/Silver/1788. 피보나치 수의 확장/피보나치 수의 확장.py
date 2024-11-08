import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (int(1e6) + 1)
dp[1] = 1
for i in range(2, abs(N) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % int(1e9)
    
if N > 0:
    print(1)
    print(dp[N])
elif N == 0:
    print(0)
    print(dp[N])
else:
    if -N % 2 == 1:
        print(1)
        print(dp[-N])
    else:
        print(-1)
        print(dp[-N])   