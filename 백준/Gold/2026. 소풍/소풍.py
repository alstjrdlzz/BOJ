import sys
input = sys.stdin.readline

def check(j, tlst):
    for i in tlst:
        if graph[i][j] == 0:
            return False
    return True


def dfs(n, s, tlst):
    global ans
    if ans:
        return
    
    if len(tlst) == K:
        ans = tlst
        return
    
    for j in range(s, N + 1):
        if visited[j] == 0 and check(j, tlst) and degree[j] >= (K - 1):
            visited[j] = 1
            dfs(n + 1, j + 1, tlst + [j])
            visited[j] = 0
    

K, N, F = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(F):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1
    
degree = [sum(lst) for lst in graph]
    
ans = []
visited = [0] * (N + 1)
dfs(0, 1, [])

if not ans:
    print(-1)
else:
    for num in ans:
        print(num)