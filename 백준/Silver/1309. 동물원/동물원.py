import sys
input = sys.stdin.readline

N = int(input())

n0 = 1
n1 = 2
for _ in range(1, N):
    n0, n1 = (n0 + n1), (2 * n0 + n1)

ans = n0 + n1
print(ans%9901)