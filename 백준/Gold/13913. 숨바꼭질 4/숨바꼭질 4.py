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
        for n in [c * 2, c - 1, c + 1]:
            if 0 <= n < 100001 and v[n] == -1:
                q.append(n)
                v[n] = v[c] + 1
                memo[n] = c
                

N, K = map(int, input().split())
memo = [0] * 100001

ans = bfs(N, K)

path = []
point = K
for _ in range(ans + 1):
    path.append(point)
    point = memo[point]

print(ans)
print(*path[::-1])