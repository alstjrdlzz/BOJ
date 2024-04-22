import sys
input = sys.stdin.readline


def dfs(n, cnt):
    global ans
    
    if n == N:
        ans = max(ans, cnt)
        return
    
    if cracked[n] == 1: # 손에 든 계란이 없는 경우
        dfs(n + 1, cnt)
        
    else:
        flag = False
        for i in range(N):
            if i == n or cracked[i] == 1:
                continue
            
            flag = True
            sw_list[i][0] -= sw_list[n][1]
            sw_list[n][0] -= sw_list[i][1]

            if sw_list[i][0] <= 0 and sw_list[n][0] <= 0:
                cracked[i], cracked[n] = 1, 1
                dfs(n + 1, cnt + 2)
                cracked[i], cracked[n] = 0, 0

            elif sw_list[i][0] <= 0:
                cracked[i] = 1
                dfs(n + 1, cnt + 1)
                cracked[i] = 0

            elif sw_list[n][0] <= 0:
                cracked[n] = 1
                dfs(n + 1, cnt + 1)
                cracked[n] = 0

            else:
                dfs(n + 1, cnt)

            sw_list[i][0] += sw_list[n][1]
            sw_list[n][0] += sw_list[i][1]

        if flag == False: # 깨지지 않은 다른 계란이 없는 경우
            dfs(n + 1, cnt)

N = int(input())
sw_list = [list(map(int, input().split())) for _ in range(N)]

ans = 0
cracked = [0] * N
dfs(0, 0)
print(ans)
