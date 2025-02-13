import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([])
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
            elif arr[i][j] == 0:
                cnt += 1
                
    if cnt == 0:
        return 0
    
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                q.append((ni, nj))
                arr[ni][nj] = arr[ci][cj] + 1
                cnt -= 1
    if cnt == 0:
        return arr[ci][cj] - 1
    else:
        return -1
            

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = bfs()
print(ans)