import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
lst = list(map(int, input().split()))
heapq.heapify(lst)

for _ in range(M):
    min1 = heapq.heappop(lst)
    min2 = heapq.heappop(lst)
    
    heapq.heappush(lst, min1 + min2)
    heapq.heappush(lst, min1 + min2)
    
print(sum(lst))