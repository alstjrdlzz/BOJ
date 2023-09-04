import sys
from collections import deque
input = sys.stdin.readline


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        x, y, z = q.popleft()
        visited[x][y][z] = 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = 1
                graph[nx][ny][nz] = graph[x][y][z] + 1
                q.append((nx, ny, nz))


m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
                
q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

bfs()

flag = False
max_val = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = True
            max_val = max(max_val, graph[i][j][k])
            
if flag:
    print(-1)
else:
    print(max_val - 1)