import sys
input = sys.stdin.readline

stack = []

def solve(data):
    if len(data) == 2:
        operator = data[0]
        x = data[1]
    else:
        operator = data[0]
    
    if operator == 1:
        stack.append(x)
    
    elif operator == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif operator == 3:
        print(len(stack))
    
    elif operator == 4:
        if not stack:
            print(1)
        else:
            print(0)
            
    elif operator == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

            
n = int(input())

for _ in range(n):
    data = list(map(int, input().split()))
    solve(data)
