import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]

# 심장 위치
flag = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "*":
            heart = (i + 1, j)
            flag = 1
            break
    if flag == 1:
        break

# 왼팔, 오른팔 길이
flag = 0
tot = 0
for j in range(N):
    if arr[heart[0]][j] == "*" and flag == 0:
        tot += 1
        s = j
        flag = 1
    elif arr[heart[0]][j] == "*" and flag == 1:
        tot += 1
        
left_arm = heart[1] - s
right_arm = tot - left_arm - 1

# 허리 길이
waist = 0
for i in range(heart[0] + 1, N):
    if arr[i][heart[1]] == "*":
        waist += 1
    if arr[i][heart[1]] == "_":
        hip = (i, heart[1])
        break
        
# 왼다리 길이
left_leg = 0
for i in range(hip[0], N):
    if arr[i][hip[1] - 1] == "*":
        left_leg += 1
        
# 오른다리 길이
right_leg = 0
for i in range(hip[0], N):
    if arr[i][hip[1] + 1] == "*":
        right_leg += 1

print(heart[0] + 1, heart[1] + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)