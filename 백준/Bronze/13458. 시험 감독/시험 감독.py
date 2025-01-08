import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N 
for n in lst:
    if n - B > 0:
        ans += (n - B + C - 1) // C
print(ans)