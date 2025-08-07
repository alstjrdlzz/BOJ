import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    deg[b] += 1
    
q = deque([])
for i in range(1, N + 1):
    if deg[i] == 0:
        q.append(i)
        
ans = []
while q:
    c = q.popleft()
    for n in adj[c]:
        deg[n] -= 1
        if deg[n] == 0:
            q.append(n)
    ans.append(c)
    
print(*ans)