import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    test = input().rstrip()
    stack = []
    flag = 1
    for x in test:
        if x == "(":
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                flag = 0
                print("NO")
                break
    if flag:
        if stack:
            print("NO")
        else:
            print("YES")     