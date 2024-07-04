import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

ans = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    ans.append(cnt + 1)
    
print(*ans)