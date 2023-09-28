import sys
input = sys.stdin.readline


def solution(n):
    d = [0] * 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    for i in range(4, n + 1):
        d[i] = d[i - 3] + d[i - 2]
    return d[n]
        

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))
    