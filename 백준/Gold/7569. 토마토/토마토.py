import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([])
    for i in range(1, H + 1):
        for j in range(1, N + 1):
            for k in range(1, M + 1):
                if arr[i][j][k] == 1: 
                    q.append((i, j, k))
    
    while q:
        ci, cj, ck = q.popleft()
        for di, dj, dk in ((0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0)):
            ni, nj, nk = ci + di, cj + dj, ck + dk
            if arr[ni][nj][nk] == 0:
                q.append((ni, nj, nk))
                arr[ni][nj][nk] = arr[ci][cj][ck] + 1   

def check():
    mx = 0
    for i in range(1, H + 1):
        for j in range(1, N + 1):
            for k in range(1, M + 1):
                if arr[i][j][k] == 0:
                    return -1
                mx = max(mx, arr[i][j][k])
    return mx - 1


M, N, H = map(int, input().split())

arr = [[[-1] * (M + 2) for _ in range(N + 2)]] + [[[-1] * (M + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (M + 2)] for _ in range(H)] + [[[-1] * (M + 2) for _ in range(N + 2)]]
bfs()               
print(check())