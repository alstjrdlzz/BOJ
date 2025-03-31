import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

counter = [0] * (max(lst) + 1)
i, j = 0, 0
ans = 0
while j < N:
    if counter[lst[j]] < K:
        counter[lst[j]] += 1
        j += 1
    else:
        counter[lst[i]] -= 1
        i += 1
    ans = max(ans, j - i)
print(ans)