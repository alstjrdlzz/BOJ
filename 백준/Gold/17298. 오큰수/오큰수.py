import sys
input = sys.stdin.readline


def sol():
    stack = [0]
    for j in range(1, N):
        while stack and A[stack[-1]] < A[j]:
            ans[stack.pop()] = A[j]
            
        if j != N - 1:
            stack.append(j)
            
N = int(input())
A = list(map(int, input().split()))

ans = [-1] * N
sol()
print(*ans)