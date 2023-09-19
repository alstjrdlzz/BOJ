import sys
input = sys.stdin.readline


def solution(a, b, c, x, y):
    ans = a * x + b * y
    if 2 * c < a + b:
        if x >= y:
            tmp = a
        else:
            tmp = b
        if 2 * c < tmp:
            ans = 2 * c * max(x, y)
        else:
            ans = 2 * c * min(x, y) + tmp * (max(x, y) - min(x, y))
    return ans
        
        
a, b, c, x, y = map(int, input().split())

print(solution(a, b, c, x, y))