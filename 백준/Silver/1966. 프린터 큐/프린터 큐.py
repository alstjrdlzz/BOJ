import sys
from collections import deque
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    queue = deque([(idx, val) for idx, val in enumerate(data)])
    answer = 0
    while True:
        if queue[0][1] == max(queue, key=lambda x: x[1])[1]:
            answer += 1
            if queue[0][0] == m:
                print(answer)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())