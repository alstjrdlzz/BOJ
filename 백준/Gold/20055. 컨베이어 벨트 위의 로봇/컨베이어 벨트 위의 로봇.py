import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * N

ans = 0
while 1: # 내구도 체크
    ans += 1
    # [1]
    belt = [belt[-1]] + belt[:-1]      
    robot = [0] + robot[:-1]
    robot[N - 1] = 0
    # [2] 로봇 1칸 이동
    for i in range(N - 2, 0, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
            robot[i], robot[i + 1] = 0, 1 # 이동
            belt[i + 1] -= 1    
            
    if belt[0] >= 1:
        robot[0] = 1 # 이동
        belt[0] -= 1 # 내구도 감소
        
    if belt.count(0) >= K:
        break        
print(ans)