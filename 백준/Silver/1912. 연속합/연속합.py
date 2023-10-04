import sys
input = sys.stdin.readline
INF = float("-inf")


def solution(n, s):
    d = [INF] * (n + 1)
    d[0] = s[0]
    for i in range(1, n):
        d[i] = max(s[i], d[i-1] + s[i])
    return max(d)


n = int(input())
s = list(map(int, input().split()))

print(solution(n, s))