import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj, sk):
    q = deque([])
    q.append((si, sj, sk))
    v[si][sj][sk] = 1
    
    while q:
        ci, cj, ck = q.popleft()
        
        if (ci, cj) == (N, M):
                return v[ci][cj][ck] # 시작하는 칸도 포함
            
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni = ci + di
            nj = cj + dj
            
            if ni < 1 or ni > N or nj < 1 or nj > M:
                continue
            
            if graph[ni][nj] == 1 and ck == 0:
                q.append((ni, nj, 1))
                v[ni][nj][1] = v[ci][cj][ck] + 1
                
            elif graph[ni][nj] == 0 and v[ni][nj][ck] == 0:
                q.append((ni, nj, ck))
                v[ni][nj][ck] = v[ci][cj][ck] + 1
    return -1


N, M = map(int, input().split())
graph = [[0]*(M+2)]+[[0]+list(map(int, input().rstrip()))+[0] for _ in range(N)]+[[0]*(M+2)]

v = [[[0]*2 for _ in range(M+2)] for _ in range(N+2)]
print(bfs(1, 1, 0))
