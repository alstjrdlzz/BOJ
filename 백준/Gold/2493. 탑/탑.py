import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans = [0] * N # 0 으로 초기화
stk = []
for i in range(N):
    while stk:
        top_i, top_h = stk[-1]
        if top_h >= lst[i]:
            ans[i] = top_i + 1
            break
        else:
            stk.pop() # 나(즉 lst[i])보다 작은 탑은 어차피 신호가 닿을 수 없음
            
    stk.append((i, lst[i]))
               
print(*ans)