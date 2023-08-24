import sys
from collections import deque


input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
               
            
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    
    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
        
    answer = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1
    
    print(answer)