import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

ans = N + 1
flag, interval_sum, e = 0, 0, 0
for s in range(N):
    while interval_sum < S and e < N:
        interval_sum += lst[e]
        e += 1
        
    if interval_sum >= S:
        ans = min(ans, e - s)
        flag = 1
    
    interval_sum -= lst[s]
    
if flag == 0:
    print(0)
else:
    print(ans)