import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

dist = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for i in range(1, N + 1):
    dist[i][i] = 0
    
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

lst = []
for i in range(1, N + 1):
    lst.append(sum(dist[i]))
    
print(lst.index(min(lst)) + 1)