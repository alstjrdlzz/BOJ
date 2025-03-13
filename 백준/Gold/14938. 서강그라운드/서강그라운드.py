import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, R = map(int, input().split())
tlst = [0] + list(map(int, input().split()))
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            dist[i][j] = 0
            
for _ in range(R):
    a, b, l = map(int, input().split())
    dist[a][b] = l
    dist[b][a] = l

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            
ans = 0
for i in range(1, N + 1):
    tmp = 0
    for j in range(1, N + 1):
        if dist[i][j] <= M:
            tmp += tlst[j]
    ans = max(ans, tmp)
print(ans)