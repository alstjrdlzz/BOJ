import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cw, cn = heapq.heappop(q)
        if distance[cn] < cw:
            continue
        for nn, nw in graph[cn]:
            if distance[nn] > cw + nw:
                distance[nn] = cw + nw
                prev[nn] = cn
                heapq.heappush(q, (cw + nw, nn))
    

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
start, end = map(int, input().split())

distance = [INF] * (N + 1)
prev = [0] * (N + 1)

dijkstra(start)

path = [end]
cur = end
while cur != start:
    cur = prev[cur]
    path.append(cur)
    
print(distance[end])
print(len(path))
print(*path[::-1])