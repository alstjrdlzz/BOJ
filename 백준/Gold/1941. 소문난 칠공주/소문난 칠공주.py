import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    q = deque()
    vv = [[0] * 5 for _ in range(5)]
    
    q.append((si, sj))
    vv[si][sj] = 1
    cnt = 1
    
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and vv[ni][nj] == 0 and v[ni][nj] == 1:
                q.append((ni, nj))
                vv[ni][nj] = 1
                cnt += 1
                
    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)

def dfs(n, cnt, scnt):
    global ans
    if cnt > 7:
        return 
    
    if n == 25:
        if cnt == 7 and scnt >= 4: # 7명 그룹이고, 4명이상이 다솜파인 경우
            if check(): # 인접했는지 체크해서 모두 인접 시 정답 += 1
                ans += 1
        return
    # 포함하는 경우
    v[n // 5][n % 5] = 1
    dfs(n + 1, cnt + 1, scnt + int(arr[n // 5][n % 5] == "S"))
    v[n // 5][n % 5] = 0
    # 포함하지 않는 경우
    dfs(n + 1, cnt, scnt)

    
arr = [input() for _ in range(5)]
ans = 0
v = [[0] * 5 for _ in range(5)]
dfs(0, 0, 0)
print(ans)
