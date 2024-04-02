import sys
input = sys.stdin.readline

def dfs(n, s, tlst):
    if n == M:
        ans.append(tlst)
        return
    
    for j in range(s, N):
        dfs(n + 1, j, tlst + [lst[j]])
        
        
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []
dfs(0, 0, [])
for lst in ans:
    print(*lst)
