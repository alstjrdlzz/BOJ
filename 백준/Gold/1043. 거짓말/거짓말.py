import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([])
    for s in K[1:]:
        q.append(s)
        v1[s] = 1
    
    while q:
        c = q.popleft()
        for i in range(M):
            if c in party[i]:
                v2[i] = 1
                for n in party[i] :
                    if v1[n] == 0 and n != c:
                        q.append(n)
                        v1[n] = 1

N, M = map(int, input().split())
K = list(map(int, input().split()))

party = []
for _ in range(M):
    lst = list(map(int, input().split()))
    party.append(lst[1:])
    
v1 = [0] * (N + 1)
v2 = [0] * M

bfs()
print(v2.count(0))
    