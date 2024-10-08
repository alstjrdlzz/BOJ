import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

p = [0]

tmp = 0
for x in lst:
    tmp += x
    p.append(tmp)
    
for _ in range(M):
    l, r = map(int, input().split())
    print(p[r] - p[l - 1])    