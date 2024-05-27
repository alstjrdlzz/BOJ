import sys
input = sys.stdin.readline

def dfs(ci, cj):
    if dp[ci][cj] == -1: # 첫 방문
        # 네 방향(더 높은 곳으로부터 낮은 곳 방문 시 경로 수 누적)
        dp[ci][cj] = 0
        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            pi, pj = ci + di, cj + dj # 이전좌표 계산
            if arr[pi][pj] > arr[ci][cj]: # 내리막길인 경우 처리
                dp[ci][cj] += dfs(pi, pj) # 조건에 맞는 네 방향 경로 수 ㄴ적
    return dp[ci][cj]


M, N = map(int, input().split())
# 범위체크를 생략하기 위해서 0으로 둘러쌈
arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(M)] + [[0] * (N + 2)]

# dp 테이블 생성 및 초기값 설정
dp = [[-1] * (N + 2) for _ in range(M + 2)]
dp[1][1] = 1

print(dfs(M, N))