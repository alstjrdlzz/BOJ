import sys
input = sys.stdin.readline

def dfs(n, tst):
    global ans
    if n == len(T) - len(S):
        if tst == S:
            ans = 1
        return
    if tst[-1] == "A":
        dfs(n + 1, tst[:-1])
    if tst[0] == "B":
        dfs(n + 1, tst[::-1][:-1])
    
S = input().rstrip()
T = input().rstrip()

ans = 0
if S == T:
    print(ans)
else:
    dfs(0, T)
    print(ans)