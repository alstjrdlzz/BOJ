import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst = lst[::-1]

ans = 0
old = lst[0]
for i in range(1, N):
    # 현재 점수가 이전 점수보다 감소하지않으면
    if lst[i] >= old:
        diff = lst[i] - (old - 1) # 이전 점수보다 -1 만큼 감소하도록 수정
        lst[i] -= diff            # 수정
        ans += diff               # 수정한 부분을 정답에 반영
    old = lst[i]                  # 이전 점수 재설정 (if문과 상관없이 항상 재설정)
        
print(ans)