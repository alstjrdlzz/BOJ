import sys
input = sys.stdin.readline

N = 4
arr = [[0] * 8] + [list(map(int, input().rstrip())) for _ in range(N)]
K = int(input())
top = [0] * (N + 1)

for _ in range(K):
    idx, dr = map(int, input().split())
    tlst = [(idx, 0)]
    for i in range(idx + 1, N + 1):
        if arr[i - 1][(top[i - 1] + 2) % 8] != arr[i][(top[i] + 6) % 8]:
            tlst.append((i, (i - idx) % 2))
        else:
            break
    for i in range(idx - 1, 0, -1):
        if arr[i][(top[i] + 2) % 8] != arr[i + 1][(top[i + 1] + 6) % 8]:
            tlst.append((i, (idx - i) % 2))
        else:
            break
    for i, rot in tlst:
        if rot == 0:
            top[i] = (top[i] - dr + 8) % 8
        else:
            top[i] = (top[i] + dr + 8) % 8
ans = 0
tbl = [0, 1, 2, 4, 8]
for i in range(1, N + 1):
    ans += arr[i][top[i]] * tbl[i]
print(ans)