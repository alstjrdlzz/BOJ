n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

item = [[0, 0]]
for _ in range(n):
    item.append(list(map(int, input().split())))
    
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = item[i][0]
        v = item[i][1]
        
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])
            
print(dp[n][k])