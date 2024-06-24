import sys
input = sys.stdin.readline

def dfs(cj, ci):
    global ans
    if abs(cj - ej) + abs(ci - ei) <= 1000:
        ans = "happy"
        return
        
    for i in range(N):
        if v[i] == 0:
            nj, ni = lst[i]
            if abs(cj - nj) + abs(ci - ni) <= 1000:
                v[i] = 1
                dfs(nj, ni)

TC = int(input())
for _ in range(TC):
    N = int(input())
    sj, si = map(int, input().split())
    lst = []
    for _ in range(N):
        tj, ti = map(int, input().split())
        lst.append((tj, ti))
    ej, ei = map(int, input().split())
    
    v = [0] * N
    ans = "sad"
    dfs(sj, si)
    print(ans)