import sys
input = sys.stdin.readline


def dfs(cn, cd):
    global fn
    global fd
    
    if cd > fd:
        fn = cn
        fd = cd
        
    for nn, nd in graph[cn]:
        if v[nn] == 0:
            v[nn] = 1
            dfs(nn, cd + nd)
            v[nn] = 0
            

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N):
    lst = list(map(int, input().split()))
    for idx in range(1, len(lst) - 2, 2):
        graph[lst[0]].append((lst[idx], lst[idx + 1]))
        
fn = 0
fd = 0
v = [0] * (N + 1)

v[1] = 1
dfs(1, 0)
v[1] = 0

fd = 0
v[fn] = 1
dfs(fn, 0)
v[fn] = 0

print(fd)