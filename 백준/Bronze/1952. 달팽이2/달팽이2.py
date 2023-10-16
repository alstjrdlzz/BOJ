import sys
input = sys.stdin.readline


def solution(k):
    dm, dn = m - k , n - k
    if (dm > 0):
        return 2 * (k - 1) + 1
    else:
        return 2 * (k - 1)

    
m, n = map(int, input().split())

k = min(m, n)

ans = solution(k)

print(ans)
