n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

cnt = []
# 탐색범위: (0, 0) ~ (n-8, m-8)
for i in range(n-7):
    for j in range(m-7):
        # 탐색
        cnt_b = 0
        cnt_w = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        cnt_b += 1
                    if board[k][l] != 'B':
                        cnt_w += 1
                else:
                    if board[k][l] != 'B':
                        cnt_b += 1
                    if board[k][l] != 'W':
                        cnt_w += 1
        #최솟값 업데이트
        cnt.append(min(cnt_b, cnt_w))
            
print(min(cnt))