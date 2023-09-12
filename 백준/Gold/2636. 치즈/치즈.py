from collections import deque
import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    temp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    temp.append((nx, ny))
                    
    for x, y in temp:
        graph[x][y] = 0
        
    return len(temp)

                
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

result = []
while True:
    cnt = bfs()
    if cnt == 0:
        break
    else:
        result.append(cnt)
        
print(len(result))
print(result[-1])