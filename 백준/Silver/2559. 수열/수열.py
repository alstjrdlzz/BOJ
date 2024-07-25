import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))


interval_sum = sum(lst[:K])
ans = interval_sum

s = 0
while s < N - K:
    interval_sum -= lst[s]
    interval_sum += lst[s+K]
    s += 1
    ans = max(ans, interval_sum)
    
print(ans)