import sys
from collections import deque


#input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a, b):
    queue = deque([(a, b)])
    graph[a][b] = 0
    
    cnt = 1
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

    
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(i, j))

print(len(answer))

answer.sort()
for cnt in answer:
    print(cnt)