import sys
sys.setrecursionlimit(10**9)
from collections import deque


input = sys.stdin.readline


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort()

visited = [0] * (n + 1)
dfs(r)
print()
visited = [0] * (n + 1)
bfs(r)