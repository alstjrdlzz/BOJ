import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans = [0] * N
tlst = list(range(N))
for i in range(N):
    ans[tlst[lst[i]]] = i + 1
    tlst.pop(lst[i])
    
print(*ans)