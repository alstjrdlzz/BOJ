import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            
for i in range(n):
    for j in range(m):
        print(visited[i][j], end=" ")
    print()