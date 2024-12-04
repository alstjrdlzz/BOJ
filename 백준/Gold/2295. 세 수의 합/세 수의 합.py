import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

# x + y 배열 만들기
xy_lst = []
for x in range(N):
    for y in range(x, N):
        xy_lst.append(lst[x] + lst[y])
xy_lst.sort()

# x + y = k - z를 만족하는 경우 찾기
ans = 0
for z in range(N):
    for k in range(z, N):
        kz = lst[k] - lst[z]
        start, end = 0, len(xy_lst) - 1
        while start <= end:
            mid = (start + end) // 2 # x + y
            xy = xy_lst[mid]
            if kz == xy:
                ans = max(ans, lst[k])
                break
            elif kz > xy:   # kz 보다 값이 작으면 x + y 를 증가 시키기
                start = mid + 1
            else:         # kz 보다 값이 크면 x + y 를 감소 시키기
                end = mid - 1
print(ans)