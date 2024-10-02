import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

ans = 0
stk = []
for i in range(N):
    while stk:
        if stk[-1] <= lst[i]:
            stk.pop()
        else:
            break
            
    ans += len(stk)
    
    stk.append(lst[i])
    
print(ans)