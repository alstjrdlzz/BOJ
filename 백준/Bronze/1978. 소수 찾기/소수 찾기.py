import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ans = 0

for x in lst:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        ans += 1
      break

print(ans)