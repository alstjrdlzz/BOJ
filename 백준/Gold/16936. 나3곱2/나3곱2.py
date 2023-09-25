import sys
input = sys.stdin.readline


def dfs(x, a, depth):
    if depth == n - 1:
        return a
    
    if x in b:
        if x % 3 == 0:
            if (x // 3) in b:
                return dfs(x // 3, a + [x // 3], depth + 1)
        if (x * 2) in b:
            return dfs(x * 2, a + [x * 2], depth + 1)
        

n = int(input())
b = list(map(int, input().split()))

for x in b:
    a = dfs(x, [x], 0)
    if a:
        print(" ".join(map(str, a)))
        break
        