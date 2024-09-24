import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
        
lst.sort()

cnt = 0
old = (3, 1)
while lst:
    if (12, 1) <= old or old < (lst[0][0], lst[0][1]):
        break
    # old와 겹치면서 더 늦게 지는 꽃 찾기
    mx = (-1, -1)
    for _ in range(len(lst)):
        # 안 겹
        if old < (lst[0][0], lst[0][1]):
            break # 더 탐색할 필요 없음
        # 겹
        else:
            # mx 업데이트
            if mx <= (lst[0][2], lst[0][3]):
                mx = (lst[0][2], lst[0][3])
            lst.pop(0) # 탐색한 꽃 리스트에서 제거 
            
    # 카운트
    cnt += 1
    old = mx

if old < (12, 1):
    print(0)
else:
    print(cnt)