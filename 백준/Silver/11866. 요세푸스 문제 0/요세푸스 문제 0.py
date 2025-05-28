import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque([str(i) for i in range(1, N + 1)])

ans = []
while q:
    for _ in range(K - 1):
        q.append(q.popleft())
    ans.append(q.popleft())
    
print(f"<{', '.join(ans)}>")