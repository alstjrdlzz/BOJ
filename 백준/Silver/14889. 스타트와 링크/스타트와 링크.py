import sys
input = sys.stdin.readline

def cal(alst, blst):
    asm = bsm = 0
    for i in range(N//2):
        for j in range(N//2):
            asm += arr[alst[i]][alst[j]]
            bsm += arr[blst[i]][blst[j]]        
    return abs(asm - bsm)


def dfs(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            ans = min(ans, cal(alst, blst))
        return
    dfs(n + 1, alst + [n], blst)
    dfs(n + 1, alst, blst + [n])
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = int(1e9)
dfs(0, [], [])
print(ans)