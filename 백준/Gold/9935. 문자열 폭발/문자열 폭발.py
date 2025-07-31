import sys
input = sys.stdin.readline


st = input().rstrip()
trg = input().rstrip()
L = len(trg)

stack = []
for c in st:
    stack.append(c)
    if len(stack) >= L:
        match = True
        for i in range(L):
            if stack[-L + i] != trg[i]:
                match = False
                break
        if match:
            for _ in range(L):
                stack.pop()
            
if stack:
    print("".join(stack))
else:
    print("FRULA")