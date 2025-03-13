import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0
    
for _ in range(M):
    a, b, t = map(int, input().split())
    dist[a][b] = t
    
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

K = int(input())
clst = list(map(int, input().split()))

mxlst = [INF] * (N + 1)
for x in range(1, N + 1):
    mx = 0
    for c in clst:
        mx = max(mx, dist[c][x] + dist[x][c])
    mxlst[x] = mx

min_val = min(mxlst)
ans = [idx for idx, val in enumerate(mxlst) if val == min_val]
print(*ans)