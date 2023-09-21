import sys
input = sys.stdin.readline


def solution(n):
    if n == 0:
        ans = 0
        
    res = []
    for i in range(n + 1):
        for j in range(n + 1 - i):
            for k in range(n + 1 - i - j):
                l = n - i - j - k
                tmp = i + 5 * j + 10 * k + 50 * l
                res.append(tmp)
                
    ans = len(set(res))
    return ans


n = int(input())
print(solution(n))