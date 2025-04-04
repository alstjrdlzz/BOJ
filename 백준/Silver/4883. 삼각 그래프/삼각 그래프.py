import sys
input = sys.stdin.readline

k = 1
while 1:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[0] * 3 for _ in range(N)]
    # 0
    dp[0][1] = arr[0][1]
    dp[0][2] = dp[0][1] + arr[0][2]
    # 1
    dp[1][0] = dp[0][1] + arr[1][0]
    dp[1][1] = min(dp[0][1], dp[0][2], dp[1][0]) + arr[1][1]
    dp[1][2] = min(dp[0][1], dp[0][2], dp[1][1]) + arr[1][2]
    # 2 ~ N - 1
    for i in range(2, N):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][2], dp[i][1]) + arr[i][2]
        
    n = dp[N - 1][1]
    print(f"{k}. {n}")
    k += 1