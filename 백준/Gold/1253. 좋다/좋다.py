import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

ans = 0
for i in range(N):
    L, R = 0, N - 1
    while L < R:
        sum_ = lst[L] + lst[R]
        if sum_ == lst[i]:
            if L != i and R != i:
                ans += 1
                break
            elif L == i:
                L += 1
            elif R == i:
                R -= 1
        elif sum_ < lst[i]:
            L += 1
        else:
            R -= 1
print(ans)