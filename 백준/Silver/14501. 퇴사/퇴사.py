import sys
input = sys.stdin.readline

def dfs(n, sm):
    global ans
    # 종료조건
    if n >= N:
        ans = max(ans, sm)
        return
    
    # 상담 O
    if n + T[n] <= N: # 퇴사일 이내에 완료 가능하면 상담 가능
        dfs(n + T[n], sm + P[n])
        
    # 상담 X
    dfs(n + 1, sm)
        

N = int(input())

T, P = [0]*  N, [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)