import sys


input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
        
        
n = int(input())
m = int(input())
parent = [i for i in range(n)]
for i in range(n):
    link = list(map(int, input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i, j)
            
plan = list(map(int, input().split()))

if len(set([find(x - 1) for x in plan])) == 1:
    print("YES")
else:
    print("NO")