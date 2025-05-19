import sys
input = sys.stdin.readline
from collections import deque

def bfs(s, e):
    q = deque()
    q.append((s, 1))

    while q:
        c, cnt = q.popleft()
        if c > e:
            continue
        if c == e:
            return cnt
        q.append((c * 2, cnt + 1))
        q.append((c * 10 + 1, cnt + 1))    
    return 0
    

A, B = map(int, input().split())

ans = bfs(A, B)

if not ans:
    print(-1)
else:
    print(ans)