import sys
input = sys.stdin.readline


def solution():
    d = [0] * 301
    d[1] = stairs[1]
    d[2] = stairs[1] + stairs[2]
    d[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    for i in range(4, n + 1):
        case1 = d[i - 3] + stairs[i - 1] + stairs[i]
        case2 = d[i - 2] + stairs[i]
        d[i] = max(case1, case2)
        
    return d[n]

    
n = int(input())
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

print(solution())