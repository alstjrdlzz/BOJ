import sys
input = sys.stdin.readline

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()

ans = 0
s, e = lst[0]
for i in range(1, N):
    x, y = lst[i]
    if x <= e:        # 겹치는 경우
        e = max(e, y)
    else:             # 겹치지 않는 경우
        ans += e - s  # ans 갱신
        s, e = x, y   # s, e 초기화
        
ans += e - s
print(ans)