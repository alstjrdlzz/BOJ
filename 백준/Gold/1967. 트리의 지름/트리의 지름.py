import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n, tmp):
    for i, w in graph[n]:
        if v[i] == -1:
            v[i] = tmp + w
            dfs(i, tmp + w)
            

V = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
    
v = [-1] * (V + 1)
v[1] = 0
dfs(1, 0)
start = v.index(max(v))

v = [-1] * (V + 1)
v[start] = 0
dfs(start, 0)

print(max(v))