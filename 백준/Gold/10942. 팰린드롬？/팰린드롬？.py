import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]
# 길이 1
for i in range(1, N + 1):
    dp[i][i] = 1
    
# 길이 2
for i in range(1, N):
    if lst[i] == lst[i + 1]:
        dp[i][i + 1] = 1
        
# 길이 3이상
for mid in range(1, N - 1):
    for i in range(1, N - mid):
        if lst[i] == lst[i + mid + 1] and dp[i + 1][i + mid] == 1:
            dp[i][i + mid + 1] = 1

# 출력
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if dp[S][E] == 1:
        print(1)
    else:
        print(0)