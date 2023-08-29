import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance[end]

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]


for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

answer = min(case1, case2)

if answer >= INF:
    print(-1)
else:
    print(answer)