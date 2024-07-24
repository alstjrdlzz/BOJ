import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0]
for i in A:
    sum_value += i
    prefix_sum.append(sum_value)

cnt = 0
s, e = 0, 0
while e < N:
    # 구간 합 계산
    interval_sum = prefix_sum[e + 1] - prefix_sum[s]
    
    if interval_sum < M:
        e += 1  
    elif interval_sum == M:
        cnt += 1
        s += 1
    else:
        s += 1
print(cnt)