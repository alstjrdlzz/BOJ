import sys


input = sys.stdin.readline

def dfs(depth):
    if depth == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            dfs(depth + 1)
            visited[i] = False
            answer.pop()
            
n, m = map(int, input().split())
answer = []
visited = [False] * (n + 1)

dfs(0)