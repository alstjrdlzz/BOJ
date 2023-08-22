import sys
from collections import deque
sys.setrecursionlimit(10**9)


input = sys.stdin.readline


def bfs(graph, v, visited):
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
queue = deque([1])
visited[1] = 1
bfs(graph, 1, visited)

answer = 0
for i in range(2, n + 1):
    if visited[i] == 1:
        answer += 1
        
print(answer)