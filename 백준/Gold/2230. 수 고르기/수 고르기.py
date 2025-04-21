import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

l, r = 0, 0
ans = int(2e9)
while r < N:
    d = lst[r] - lst[l]
    if d < M:
        r += 1
    elif d == M:
        ans = M
        break
    else:
        ans = min(ans, d)
        l += 1
        
print(ans)