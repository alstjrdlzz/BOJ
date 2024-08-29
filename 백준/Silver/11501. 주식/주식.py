import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    
    ans = 0
    mx = 0
    for i in range(N - 1, -1, -1):
        if lst[i] > mx:
            mx = lst[i]
        else:
            ans += mx - lst[i] # 차익실현
    print(ans)