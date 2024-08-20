import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
q = deque(lst)

ans = 0
while q:
    num = q.popleft()
    ans = max(ans, num * (len(q) + 1))
     
print(ans)