import sys
input = sys.stdin.readline


st = input().rstrip()

ans = ""
stack = []
for c in st:
    if c.isalpha():
        ans += c
    elif c == "(":
        stack.append(c)
    elif c == "*" or c == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            ans += stack.pop()
        stack.append(c)
    elif c == "+" or c == "-":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.append(c)
    elif c == ")":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
        
while stack:
    ans += stack.pop()
    
print(ans)