import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [[num] for num in lst]
for i in range(1, N):
    idx = 0
    flag = 0
    for j in range(i):
        if lst[j] < lst[i]:                 # (조건 1) 증가하는 수열인가?
            if len(dp[j]) >= len(dp[idx]):  # (조건 2) 가장 긴 수열인가?
                idx = j
                flag = 1
    if flag:
        dp[i] = dp[idx] + [lst[i]]         # 이전의 LIS에 lst[i] 붙여서 업데이트

print(len(max(dp, key=len)))
print(*max(dp, key=len))