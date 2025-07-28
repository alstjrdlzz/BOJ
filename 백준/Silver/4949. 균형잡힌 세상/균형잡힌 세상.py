import sys
input = sys.stdin.readline


while 1:
    st = input().rstrip()
    if st == ".":
        break
    
    stack = []
    for s in st:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(s)
                break
        else:
            continue
            
    if stack:
        print("no")
    else:
        print("yes")
