import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())

dist = [[INF] * (N + 1) for _ in range(N + 1)]

while 1:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    dist[a][b] = 1
    dist[b][a] = 1
    
for i in range(1, N + 1):
    dist[i][i] = 0
    
for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

lst = []
for i in range(1, N + 1):
    lst.append(max(dist[i][1:]))

min_val = min(lst)
print(min_val, lst.count(min_val))

for i, v in enumerate(lst):
    if v == min_val:
        print(i + 1, end=" ")