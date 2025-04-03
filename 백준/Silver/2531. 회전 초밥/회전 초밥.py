import sys
input = sys.stdin.readline
from collections import defaultdict

N, D, K, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst += lst[:-1]

window = defaultdict(int)
for i in range(K):
    window[lst[i]] += 1
window[C] += 1
    
ans = len(window)

start, end = 0, K
while start < N:
    window[lst[start]] -= 1
    if window[lst[start]] == 0:
        window.pop(lst[start])
    window[lst[end]] += 1
    ans = max(ans, len(window))
    start += 1
    end += 1
print(ans)