import sys
input = sys.stdin.readline

N = int(input())

ans, interval_sum, e = 0, 0, 1
for s in range(1, N + 1):
    while interval_sum < N and e <= N:
        interval_sum += e
        e += 1
    if interval_sum == N:
        ans += 1
    interval_sum -= s
    
print(ans)