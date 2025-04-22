import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

l, r = 0, 0
cnt = 0
ans = 0
while r < N:
    if cnt <= K:
        if lst[r] % 2 == 1:
            cnt += 1
        r += 1
    else:
        if lst[l] % 2 == 1:
            cnt -= 1
        l += 1
    ans = max(ans, r - l - cnt)
    
print(ans)