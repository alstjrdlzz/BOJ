import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    q = deque([])
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.popleft()
        for n in graph[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
v = [0] * (N + 1)
bfs(1)

ans = 0
for i in range(2, N + 1):
    if 0 < v[i] <= 3:
        ans += 1
print(ans)