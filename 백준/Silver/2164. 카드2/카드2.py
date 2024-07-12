import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])

n = 1
while n < N:
    q.popleft()
    q.append(q.popleft())
    n += 1
    
print(q[0])