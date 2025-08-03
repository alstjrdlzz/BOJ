import sys
input = sys.stdin.readline


lst = list(input().rstrip())

ans = 0
stack = []
for i, c in enumerate(lst):
    if c == "(":
        stack.append((i, c))
    else:
        i_, c_ = stack.pop()
        if i - i_ == 1:
            ans += len(stack)
        else:
            ans += 1
print(ans)