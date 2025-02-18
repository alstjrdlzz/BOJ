import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj, ei, ej):
    if si == ei and sj == ej:
        return 0
    q = deque([])
    q.append((si, sj))
    v[si][sj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                if ni == ei and nj == ej:
                    return v[ni][nj]           
            

TC = int(input())
for _ in range(TC):
    N = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    
    v = [[0] * N for _ in range(N)]
    ans = bfs(si, sj, ei, ej) - 1
    if ans == -1:
        print(0)
    else:
        print(ans)
