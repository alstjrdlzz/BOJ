import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int, input().split()))

lo, hi = 1, 10 ** 5
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    sset = set()
    flag = 1
    for i in range(M):
        if i == 0:
            if 0 < lst[i] - mid:
                flag = 0
                break
                
        if i > 0:
            if lst[i - 1] + mid < lst[i] - mid:
                flag = 0
                break
                
        if i == M - 1:
            if lst[i] + mid < N:
                flag = 0
                break
        
    if flag == 1:
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1
        
print(ans)