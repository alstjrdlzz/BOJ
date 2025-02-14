import sys
input = sys.stdin.readline
from collections import deque

def bfs1(i, j):
    q = deque([])
    q.append((i, j))
    v1[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ci][cj] == arr[ni][nj] and v1[ni][nj] == 0:
                q.append((ni, nj))
                v1[ni][nj] = 1
    return 1

def bfs2(i, j):
    q = deque([])
    q.append((i, j))
    v2[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v2[ni][nj] == 0:
                if (arr[ci][cj] in ["R", "G"] and arr[ni][nj] in ["R", "G"]) or (arr[ci][cj] == "B" and arr[ni][nj] == "B"):
                    q.append((ni, nj))
                    v2[ni][nj] = 1
    return 1

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

v1 = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if v1[i][j] == 0:
            cnt1 += bfs1(i, j)

v2 = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if v2[i][j] == 0:
            cnt2 += bfs2(i, j)

print(f"{cnt1} {cnt2}")