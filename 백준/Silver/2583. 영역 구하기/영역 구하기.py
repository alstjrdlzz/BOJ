import sys
input = sys.stdin.readline
from collections import deque

def draw(x1, y1, x2, y2):
    for i in range(M - y2, M - y1):
        for j in range(x1, x2):
            arr[i][j] = 1
            
def bfs(i, j):
    q = deque([])
    q.append((i, j))
    arr[i][j] = 1
    cnt = 1
    
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[ni][nj] = 1
                cnt += 1
    return cnt
    

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    draw(x1, y1, x2, y2)

cnt = 0
lst = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            res = bfs(i, j)
            cnt += 1
            lst.append(res)
lst.sort()
print(cnt)
print(*lst)