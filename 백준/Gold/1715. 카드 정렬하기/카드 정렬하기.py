import sys
input = sys.stdin.readline
import heapq

N = int(input())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(input()))

ans = 0
while len(hq) > 1:
    d = heapq.heappop(hq) + heapq.heappop(hq)
    ans += d
    heapq.heappush(hq, d)
    
print(ans)