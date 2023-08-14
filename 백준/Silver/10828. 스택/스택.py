import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    query = list(input().split())
    
    if query[0] == "push":
        stack.append(query[1])
    elif query[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif query[0] == "size":
        print(len(stack))
    elif query[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif query[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)