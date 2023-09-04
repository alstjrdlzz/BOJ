import sys
from collections import defaultdict
input = sys.stdin.readline


result = defaultdict(int)


def divide(x, y, size, k):
    size = size // k
    for a in range(k):
        for b in range(k):
            nona_tree(x + a * size, y + b * size, size)

def nona_tree(x, y, size):
    start = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if start != board[i][j]:
                divide(x, y, size, 3)
                return
            
    result[start] += 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

nona_tree(0, 0, n)

for key in (-1, 0, 1):
    print(result[key])