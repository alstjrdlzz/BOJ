import sys
input = sys.stdin.readline


shapes = [
    [[1, 1],
     [1, 1]],
    
    [[1, 1, 1, 1]],

    [[1, 1, 1],
     [0, 1, 0]],
    
    [[1, 1, 0],
     [0, 1, 1]],

    [[1, 1, 1],
     [0, 0, 1]],
]


def place(s, i, j, A):
    h, w = len(s), len(s[0])
    val = 0
    for r in range(h):
        for c in range(w):
            val += s[r][c] * A[i + r][j + c]
    return val


def maximize(s, n, m, A):
    h, w = len(s), len(s[0])
    opt = 0
    for i in range(n - h + 1):
        for j in range(m - w + 1):
            opt = max(opt, place(s, i, j, A))
    return opt


def flip(s):
    h, w = len(s), len(s[0])
    shape = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            shape[i][j] = s[i][w - 1 - j]
    return shape


def rotate(s):
    h, w = len(s[0]), len(s)
    shape = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            shape[i][j] = s[w - 1 - j][i]
    return shape
            

def get_shape(k, s):
    if k == 0:
        return shapes[0]
    elif k == 1:
        return shapes[1]
    elif k == 3:
        return shapes[2]
    elif k == 7:
        return shapes[3]
    elif k == 11:
        return shapes[4]
    elif k in [9, 15]:
        return flip(s)
    else:
        return rotate(s)
    

def solve(n, m, A):
    opt = 0
    shape = []
    for i in range(19):
        shape = get_shape(i, shape)
        opt = max(opt, maximize(shape, n, m, A))
    return opt
    
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, m, A)) 