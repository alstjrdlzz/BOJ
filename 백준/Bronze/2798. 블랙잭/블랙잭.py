import sys
input = sys.stdin.readline

def dfs(n, cnt, tsm):
    global ans
    
    if cnt > 3 or tsm > M:
        return
    
    if n == N:
        if cnt == 3:
            ans = max(ans, tsm)
        return
    
    dfs(n + 1, cnt, tsm)
    dfs(n + 1, cnt + 1, tsm + lst[n])
    

N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
dfs(0, 0, 0)
print(ans)
