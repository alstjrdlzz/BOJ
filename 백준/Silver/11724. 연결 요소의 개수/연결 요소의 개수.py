import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0] * (n + 1)

def bfs(x):
    queue = deque([x])
    visited[x] = 1
    while queue:
        x = queue.popleft()
        for v in graph[x]:
            if visited[v] == 0:
                visited[v] = 1
                queue.append(v)

answer = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        bfs(i)
        answer += 1
                
print(answer)