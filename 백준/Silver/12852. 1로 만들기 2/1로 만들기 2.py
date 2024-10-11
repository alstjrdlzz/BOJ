import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
path = ["" for _ in range(N + 1)]
path[1] = "1"
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    p = i - 1
    
    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            p = i // 2
            
    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            p = i // 3
    
    path[i] = str(i) + " " + path[p]
        
print(dp[N])
print(path[N])
