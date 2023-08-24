import sys
from collections import deque


input = sys.stdin.readline

def fn1(x):
    return x - 1


def fn2(x):
    return x + 1


def fn3(x):
    return x * 2

idx2fn = {0: fn1, 1: fn2, 2: fn3}

def bfs(start): 
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[x]
        for i in range(3):
            nx = idx2fn[i](x)
            if nx < 0 or nx > 10 ** 5:
                continue
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                queue.append(nx)

n, k = map(int, input().split())
graph = [0] * (10 ** 5 + 1)

print(bfs(n))