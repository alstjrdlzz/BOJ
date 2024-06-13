import sys
input = sys.stdin.readline
from collections import deque

def fn1(x):
    return x - 1

def fn2(x):
    return x + 1

def fn3(x):
    return x * 2

fns = [fn1, fn2, fn3]

def bfs(s, e):
    v = [0] * (10 ** 5 + 1)
    q = deque([])
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.popleft()
        if c == e:
            return v[e] - 1
        for fn in fns:
            n = fn(c)
            if 0 <= n < 10 ** 5 + 1:
                if not v[n]:
                    q.append(n)
                    v[n] += v[c] + 1
                

N, K = map(int, input().split())

ans = bfs(N, K)
print(ans)