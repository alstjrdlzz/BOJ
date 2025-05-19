import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    q = deque([])
    v = [-1] * 100001
    
    q.append(s)
    v[s] = 0
    
    while q:
        c = q.popleft()
        if c == e:
            return v[c]
        
        for n in [2 * c, c - 1, c + 1]:
            if 0 <= n < 100001 and v[n] == -1:
                if n == 2 * c:
                    q.appendleft(n)
                    v[n] = v[c]
                else:
                    q.append(n)
                    v[n] = v[c] + 1
            
N, K = map(int, input().split())
print(bfs(N, K))