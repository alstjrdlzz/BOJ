import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
lst = [0] + list(map(int, input().split())) + [L]
lst.sort()

start, end = 1, L - 1
ans = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > mid:
            cnt += (lst[i] - lst[i - 1] - 1) // mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)
            