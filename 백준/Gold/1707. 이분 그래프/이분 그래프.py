import sys
input = sys.stdin.readline
from collections import deque

def color_in(x):
    return 1 if x == -1 else -1

def bfs(s):
    q = deque([])
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.popleft()
        for n in graph[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = color_in(v[c])
            elif v[n] == v[c]:
                return 0 
            else:
                continue
    return 1
    

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    v = [0] * (V + 1)
    
    lst = []
    for i in range(1, V + 1):
        if v[i] == 0:
            lst.append(bfs(i))
            
    if all(lst):
        print("YES")
    else:
        print("NO")
        