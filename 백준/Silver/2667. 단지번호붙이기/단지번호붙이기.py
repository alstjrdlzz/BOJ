import sys
input = sys.stdin.readline
from collections import deque

def bfs(si, sj):
    q = deque([(si, sj)])    # 초기 데이터 삽입
    arr[si][sj] = 0          # 초기 데이터 방문 표시
    
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] == 1:      # 방문하지 않은 경우
                q.append((ni, nj))    # 큐에 삽입
                arr[ni][nj] = 0       # 방문 표시
                cnt += 1
    return cnt


N = int(input())
arr = [[0] * (N + 2)] + [[0] + list(map(int, input().strip())) + [0] for _ in range(N)] + [[0] * (N + 2)]

lst = []
for i in range(N + 2):
    for j in range(N + 2):
        if arr[i][j] == 1:
            lst.append(bfs(i, j))
            
lst.sort()        # 오름차순 정렬
print(len(lst))
for cnt in lst:
    print(cnt)