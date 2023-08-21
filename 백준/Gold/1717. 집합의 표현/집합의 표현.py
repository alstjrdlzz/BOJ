import sys
sys.setrecursionlimit(1000000)


input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

    
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    operator, a, b = map(int, input().split())
    if operator == 0:
        union(a, b)
    elif operator == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
