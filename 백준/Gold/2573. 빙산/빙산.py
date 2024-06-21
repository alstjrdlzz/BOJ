# import sys
# input = sys.stdin.readline
from collections import deque

def count_zero(ci, cj):
    '''
    동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수 카운트
    '''
    cnt = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        # 범위, 0
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] <= 0:
            cnt += 1
    return cnt    

def melt():
    '''
    실제로는 모든 빙하가 동시에 녹는 것이므로 
    반목문 내에서 먼저 처리된 빙하의 결과에
    다음 빙하의 처리가 영향을 받으면 안 됨
    '''
    lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt = count_zero(i, j)
                if cnt > 0:
                    lst.append((i, j, cnt))
                
    for i, j, cnt in lst:
        arr[i][j] -= cnt        

def bfs(si, sj):
    q = deque([])
    q.append((si, sj))
    v[si][sj] = 1
    
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위, 방문x, 바다x
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni, nj))
                v[ni][nj] = 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    year += 1
    # 1년치 녹이기
    melt()
    # 덩어리 수 계산 (bfs)
    icnt = 0
    v = [[0] * (M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and v[i][j] == 0:
                bfs(i, j)
                icnt += 1
                
    if icnt > 1:         # 빙산이 2 덩어리로 분리 됨
        print(year)
        break
    if icnt == 0:        # 빙산이 다 녹을 때까지 분리되지 않음
        print(0)
        break