import sys
input = sys.stdin.readline


white = 0
blue = 0

def quad_tree(x, y, size):
    global white, blue
    start = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if start != board[i][j]:
                size = size // 2
                quad_tree(x, y, size)
                quad_tree(x + size, y, size)
                quad_tree(x, y + size, size)
                quad_tree(x + size, y + size, size)
                return
            
    if start == 0:
        white += 1
    elif start == 1:
        blue += 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

quad_tree(0, 0, n)
print(white)
print(blue)