import sys
from collections import deque


input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) 
            
            
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

bfs(0, 0)
print(graph[n-1][m-1])