import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
queue = deque(list(range(1, N + 1)))

while len(queue) > 1:
    print(queue.popleft(), end = " ")
    
    tmp = queue.popleft()
    queue.append(tmp)
    
print(queue.popleft())