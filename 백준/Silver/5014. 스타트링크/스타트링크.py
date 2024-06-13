import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    q = deque([])
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.popleft()
        if c == e:
            return v[e] - 1
        
        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] += v[c] + 1
                
    return "use the stairs"
                

F, S, G, U, D = map(int, input().split())
adj = [[] for _ in range(F + 1)]
for i in range(1, F + 1):
    if i + U <= F:
        adj[i].append(i + U)
    if i - D >= 1:
        adj[i].append(i - D)

v = [0] * (F + 1)
ans = bfs(S, G)
print(ans)