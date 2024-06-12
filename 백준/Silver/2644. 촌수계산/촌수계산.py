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
                
    return -1
    

N = int(input())
P, Q = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
v = [0] * (N + 1)
ans = bfs(P, Q)
print(ans)