import sys
input = sys.stdin.readline

M, N = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 1, max(lst)
ans = 0
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(N):
        cnt += (lst[i] // mid)
        
    if cnt >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)               