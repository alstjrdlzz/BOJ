import sys
input = sys.stdin.readline

T, W = map(int, input().split())
lst = [0] + [int(input()) for _ in range(T)]

dp = [[0] * (W + 2) for _ in range(T + 1)]
for i in range(1, T + 1):
    for j in range(W + 1):    
        # 먹
        if (lst[i] == 1 and j % 2 == 0) or (lst[i] == 2 and j % 2 == 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1
        # 못 먹
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
            
print(max(dp[T]))