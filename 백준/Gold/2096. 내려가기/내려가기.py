import sys
input = sys.stdin.readline

N = int(input())
arr0 = list(map(int, input().split()))
mx = arr0
mn = arr0
for _ in range(N - 1):
    arr = list(map(int, input().split()))
    mx = [max(mx[0], mx[1]) + arr[0], max(mx) + arr[1],  max(mx[1], mx[2]) + arr[2]]
    mn = [min(mn[0], mn[1]) + arr[0], min(mn) + arr[1],  min(mn[1], mn[2]) + arr[2]]

print(max(mx), min(mn))