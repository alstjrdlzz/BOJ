import sys
input = sys.stdin.readline

def dfs(n):
		global ans
		if n == N: # 종료조건
				ans += 1 # 정답처리: 경우의수 + 1
				return
		# 하부단계 호출
		for j in range(N):
				if v1[j] ==  v2[n + j] == v3[n - j] == 0:
						v1[j] = v2[n + j] = v3[n - j] = 1
						dfs(n + 1)
						v1[j] = v2[n + j] = v3[n - j] = 0
						
						
N = int(input())
ans = 0
v1 = [0] * N
v2 = [0] * (2 * N)
v3 = [0] * (2 * N)
dfs(0)
print(ans)