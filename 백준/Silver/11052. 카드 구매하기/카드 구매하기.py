import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int , input().split()))

dp = [0] * (N + 1)

dp[1] = lst[1]
for i in range(2, N + 1):
    # 카드 i개를 갖기 위해 지불해야 하는 금액의 최댓값
    mx = lst[i]
    for j in range(1, i):
        mx = max(mx, dp[j] + lst[i - j])
    dp[i] = mx
    
print(dp[N])