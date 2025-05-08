import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [0] * 1000001
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e):
        arr[i] += 1
    
flag = 0
l, r = 0, 0
x = 0
while l <= r < 1000001:
    if x == K:
        flag = 1
        break
    if x < K:
        x += arr[r]
        r += 1
    else:
        x -= arr[l]
        l += 1

if flag:
    print(l, r)
else:
    print(0, 0)