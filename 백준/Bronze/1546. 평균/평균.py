import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans = 0
mx = max(lst)
for score in lst:
    ans += ((score/mx)*100)/N
print(ans)