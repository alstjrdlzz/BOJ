import sys
input = sys.stdin.readline
import heapq
from collections import deque

N, M = map(int, input().split())
arr = [deque(sorted(list(map(int, input().split())))) for _ in range(N)]

# 초기화
hq = []
mx, mn = 0, int(1e9)
for i in range(N):
    v = arr[i].popleft()
    mx = max(mx, v)
    mn = min(mn, v)
    heapq.heappush(hq, (v, i))

ans = mx - mn
while 1:
    _, i = heapq.heappop(hq)
    if not arr[i]:
        break
    v = arr[i].popleft()
    heapq.heappush(hq, (v, i))
    mx = max(mx, v)
    mn = hq[0][0]
    ans = min(ans, mx - mn)

print(ans)