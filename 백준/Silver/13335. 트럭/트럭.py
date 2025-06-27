import sys
input = sys.stdin.readline
from collections import deque

N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

bridge = deque([0] * W)
time = 0
weight = 0

while bridge:
    time += 1
    top = bridge.popleft()
    weight -= top
    
    if trucks:
        if weight + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
            weight += truck
        else:
            bridge.append(0)
print(time)
            