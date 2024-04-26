import sys
input = sys.stdin.readline

def sol(string):
    stack = []
    for ch in string:
        stack.append(ch)
        if stack[-4:] == ["P", "P", "A", "P"]:
            for _ in range(3):
                stack.pop()
    if stack == ["P", "P", "A", "P"] or stack == ["P"]:
        return "PPAP"
    return "NP"


string = input().rstrip()
print(sol(string))