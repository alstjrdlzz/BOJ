import sys
input = sys.stdin.readline

def update(cross):
    x, y, s = cross
    visited[x][y] = 0
    for i in range(1, s + 1):
        visited[x - i][y] = 0
        visited[x + i][y] = 0
        visited[x][y - i] = 0
        visited[x][y + i] = 0
    

def cross_ok(x, y, s):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + s * dx[i]
        ny = y + s * dy[i]
        if board[nx][ny] != "*":
            return False
    return True


def ok(visited):
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                return False
    return True


def search(x, y):
    ans = []
    max_size = min(x, n - 1 - x, y, m - 1 - y)
    for s in range(1, max_size + 1):
        if not cross_ok(x, y, s):
            return ans
        ans.append((x, y, s))
    return ans
               
                
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 방문 배열 초기화
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == "*":
            visited[i][j] = 1

# 탐색
res = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "*":
            crosses = search(i, j)
            if crosses:
                biggest_cross = crosses[-1]
                res.append(biggest_cross)
                # 탐색 성공한 십자가를 방문 배열에 표시
                update(biggest_cross)            

if ok(visited):
    print(len(res))
    for x, y, s in res:
        print(x + 1, y + 1, s, sep=" ")
else:
    print(-1)