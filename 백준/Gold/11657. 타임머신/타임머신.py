import sys
#input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            a, b, c = edge[j]
            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == n - 1:
                    return False
    return True

n, m = map(int, input().split())

edge = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))
    
if bellman_ford(1):
    for i in range(2, n + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
else:
    print(-1)
    