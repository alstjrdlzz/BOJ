import sys
input = sys.stdin.readline


N = int(input())

ans = N
for _ in range(N):
    st = input().rstrip()
    
    stack = []
    for c in st:
        stack.append(c)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                for _ in range(2):
                    stack.pop()
    if stack:
        ans -= 1

print(ans)