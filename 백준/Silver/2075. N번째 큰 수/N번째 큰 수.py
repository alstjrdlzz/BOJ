import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
for _ in range(N):
    lst = list(map(int, input().split()))
    for i in range(N):
        if len(heap) < N:
            heapq.heappush(heap, lst[i])
        else:
            if heap[0] < lst[i]:
                heapq.heapreplace(heap, lst[i])
print(heap[0])       