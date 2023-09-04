import sys
input = sys.stdin.readline


result = {-1: 0, 0: 0, 1: 0}

def nona_tree(x, y, size):
    start = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if start != board[i][j]:
                size = size // 3
                for a in range(3):
                    for b in range(3):
                        nona_tree(x + a * size, y + b * size, size)
                return
    result[start] += 1
    
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

nona_tree(0, 0, n)

for key in (-1, 0, 1):
    print(result[key])