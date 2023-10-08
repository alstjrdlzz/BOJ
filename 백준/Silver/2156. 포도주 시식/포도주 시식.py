import sys
input = sys.stdin.readline


def solution():
    d = [-1] * 100001
    d[1] = s[1]
    d[2] = s[1] + s[2]
    d[3] = max(s[1] + s[3], s[2] + s[3], s[1] + s[2])
    for i in range(4, n + 1):
        case1 = d[i - 3] + s[i - 1] + s[i]
        case2 = d[i - 2] + s[i]
        case3 = d[i - 1]
        d[i] = max(case1, case2, case3)
    return d[n]

n = int(input())
s = [-1] * 100001
for i in range(1, n + 1):
    s[i] = int(input())
    
print(solution())
