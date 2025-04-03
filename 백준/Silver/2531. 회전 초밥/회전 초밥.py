import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst += lst[:-1]

start, end = 0, K
window = lst[start : end]
ans = len(set(window + [C]))
while start < N:
    window.pop(0)
    window += [lst[end]]
    ans = max(ans, len(set(window + [C])))
    start += 1
    end += 1
print(ans)