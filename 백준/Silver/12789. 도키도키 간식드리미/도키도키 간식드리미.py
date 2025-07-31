import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))

trg = 1
stack = []
for x in lst:
    stack.append(x)
    while stack and stack[-1] == trg:
        stack.pop()
        trg += 1
    
    if len(stack) > 1 and stack[-1] > stack[-2]:
        break

if stack:
    print("Sad")
else:
    print("Nice")