import sys
input = sys.stdin.readline


lstack = list(input().rstrip())
rstack = []

M = int(input())
for _ in range(M):
    cmd = input().split()
    
    if cmd[0] == "L" and lstack:
        rstack.append(lstack.pop())
    elif cmd[0] == "D" and rstack:
        lstack.append(rstack.pop())
    elif cmd[0] == "B" and lstack:
        lstack.pop()
    elif cmd[0] == "P":
        lstack.append(cmd[1])

print("".join(lstack + rstack[::-1]))