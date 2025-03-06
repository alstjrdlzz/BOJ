import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, end):
    dist = [int(1e9)] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cur_weight, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_weight:
            continue
        for adj_node, adj_weight in graph[cur_node]:
            cost = cur_weight + adj_weight
            if dist[adj_node] > cost:
                dist[adj_node] = cost
                heapq.heappush(q, (cost, adj_node))
    return dist[end]

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V, W = map(int, input().split())
    graph[U].append((V, W))

ans = 0
for i in range(1, N + 1):
    ans = max(ans, dijkstra(i, X) + dijkstra(X, i))
print(ans)