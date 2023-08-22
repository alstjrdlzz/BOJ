import sys
from collections import deque
sys.setrecursionlimit(10**9)


input = sys.stdin.readline


def bfs(graph, v, visited):
    global cnt
    
    visited[v] = cnt

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)
          

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)
    
queue = deque([r])
visited[r] = cnt
bfs(graph, r, visited)
for i in range(1, n + 1):
    print(visited[i])