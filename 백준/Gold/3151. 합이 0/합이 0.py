import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

ans = 0
for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        sum_ = lst[i] + lst[left] + lst[right]
        if sum_ <= 0:
            if sum_ == 0:
                # 정답처리
                if lst[left] == lst[right]:
                    ans += right - left 
                else:
                    ans += right - bisect_left(lst, lst[right]) + 1
            left += 1
        else:
            right -= 1
print(ans)
            