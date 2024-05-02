import sys
input = sys.stdin.readline
from collections import deque


N, K = map(int, input().split())

queue = deque(list(range(1, N + 1)))

print("<", end = "")
while len(queue) > 1:
    for _ in range(K - 1):
        tmp = queue.popleft()
        queue.append(tmp)
    print(queue.popleft(), end = ", ")
print(queue.popleft(), end = ">")