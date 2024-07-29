import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans, s, e = 0, 0, N - 1
while s < e:
    tmp = lst[s] + lst[e]
    if tmp == M:
        s += 1
        e -= 1
        ans += 1
    elif tmp < M:
        s += 1
    else:
        e -= 1

print(ans)