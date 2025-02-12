import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    arr[x][y] = 0
    width = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0
                width += 1
    return width
                

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            ans = max(ans, bfs(i, j))
print(cnt)
print(ans)