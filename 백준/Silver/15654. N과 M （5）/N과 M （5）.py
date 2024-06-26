import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, lst + [ipt[j]])
            v[j] = 0

            
N, M = map(int, input().split())
ipt = sorted(list(map(int, input().split())))
ans = []
v = [0] * N
dfs(0, [])
for lst in ans:
    print(*lst)
