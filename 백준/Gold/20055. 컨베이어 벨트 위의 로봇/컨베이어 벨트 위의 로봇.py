import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * N

cnt = 0
ans = 0
while 1:
    ans += 1
    # [1]
    belt.insert(0, belt.pop())     
    robot.pop()
    robot.insert(0, 0)
    robot[N - 1] = 0
    # [2]
    for i in range(N - 2, 0, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
            robot[i], robot[i + 1] = 0, 1 # 이동
            belt[i + 1] -= 1    
            if belt[i + 1] == 0:
                cnt += 1
    # [3]       
    if belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    # [4]
    if cnt >= K:
        break        
print(ans)