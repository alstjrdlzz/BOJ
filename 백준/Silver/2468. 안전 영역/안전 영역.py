import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj, h):
    q = deque([])
    q.append((si, sj))
    v[si][sj] = 1
    
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] > h:
                q.append((ni, nj))
                v[ni][nj] = 1
    return 1    
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


h_min, h_max = 1, 1
for i in range(N):
    for j in range(N):
        h_min = min(h_min, arr[i][j])
        h_max = max(h_max, arr[i][j])

ans = 0
for h in range(h_min, h_max):
    v = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] > h:
                cnt += bfs(i, j, h)        
    ans = max(ans, cnt)
    
if ans == 0:
    print(1)
else:
    print(ans)