import sys
input = sys.stdin.readline
from collections import deque

def bfs1():
    q = deque([])
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if arr[i][j] == "*":
                q.append((i, j))
                v1[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if v1[ni][nj] == 0:
                if arr[ni][nj] == "." or arr[ni][nj] == "@":
                    q.append((ni, nj))
                    v1[ni][nj] = v1[ci][cj] + 1
                
def bfs2(i, j):
    q = deque([])
    q.append((i, j))
    v2[i][j] = 1
    
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if v2[ni][nj] == 0:
                if arr[ni][nj] == "$":
                    return v2[ci][cj]
                elif arr[ni][nj] == ".":
                    if v2[ci][cj] + 1 < v1[ni][nj] or v1[ni][nj] == 0:
                        q.append((ni, nj))
                        v2[ni][nj] = v2[ci][cj] + 1
                else:
                    continue
    return "IMPOSSIBLE"
                

TC = int(input())
for _ in range(TC):
    W, H = map(int, input().split())
    arr = [["$"] * (W + 2)] + [["$"] + list(input().rstrip()) + ["$"] for _ in range(H)] + [["$"] * (W + 2)]
    v1 = [[0] * (W + 2) for _ in range(H + 2)]
    bfs1()
    v2 = [[0] * (W + 2) for _ in range(H + 2)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if arr[i][j] == "@":
                print(bfs2(i, j))
                break