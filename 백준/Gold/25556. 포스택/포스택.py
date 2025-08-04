import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int, input().split()))

stack = [[] for _ in range(4)]
for n in lst:
    match = 0
    for i in range(4):
        if stack[i]:
            if stack[i][-1] < n:
                stack[i].append(n)
                match = 1
                break
        else:
            stack[i].append(n)
            match = 1
            break
    if not match:
        print("NO")
        break
else:
    print("YES")