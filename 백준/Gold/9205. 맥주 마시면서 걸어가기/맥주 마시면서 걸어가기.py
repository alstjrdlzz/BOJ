import sys
input = sys.stdin.readline
from collections import deque

def bfs(sj, si, ej, ei):
    q = deque([])
    v = [0] * N
    
    q.append((sj, si))
    
    while q:
        cj, ci = q.popleft()
        if abs(cj - ej) + abs(ci - ei) <= 1000 :
            return "happy"
        
        for i in range(N):
            if v[i] == 0:
                nj, ni = lst[i]
                if abs(cj - nj) + abs(ci - ni) <= 1000:
                    q.append((nj, ni))
                    v[i] = 1
    return "sad"


TC = int(input())
for _ in range(TC):
    N = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(N):
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())
    ans = bfs(sj, si, ej, ei)
    print(ans)