def sol(string):
    stack = []
    for ch in string:
        stack.append(ch)
        if stack[-4:] == ["P", "P", "A", "P"]:
            for _ in range(4):
                stack.pop()
            stack.append("P")
    if stack == ["P", "P", "A", "P"] or stack == ["P"]:
        return "PPAP"
    return "NP"


string = input()
print(sol(string))