import sys
input = sys.stdin.readline


def solve(a, b):
    if b == 1:
        return a % c
    else:
        q, r = divmod(b, 2)
        temp = solve(a, q)
        if r == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c

a, b, c = map(int, input().split())

print(solve(a, b))