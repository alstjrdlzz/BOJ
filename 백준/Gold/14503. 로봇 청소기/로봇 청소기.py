import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solve(ci, cj, cd):
    cnt = 0
    while 1:
        # [1]
        arr[ci][cj] = 2
        cnt += 1
        
        # [2]
        flag = 1
        while flag == 1:
            for nd in ((cd + 3) % 4, (cd + 2) % 4, (cd + 1) % 4, cd % 4):
                ni, nj = ci + di[nd], cj + dj[nd]
                if arr[ni][nj] == 0:
                    ci, cj, cd = ni, nj, nd
                    flag = 0
                    break
            else: #4방향 모두 미청소 영역 없음 ==> 후진
                bi, bj = ci - di[cd], cj - dj[cd]
                if arr[bi][bj] == 1:
                    return cnt
                else:
                    ci, cj = bi, bj
                
                        
N, M = map(int, input().split())
si, sj, sd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve(si, sj, sd)
print(ans)