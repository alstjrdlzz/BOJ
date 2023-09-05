import sys
input = sys.stdin.readline


shapes = [
    [1],
    [1, 1, 1, 1],

    [1, 1],

    [1, 1, 0],
    [0, 1],

    [0, 1, 1],
    [1, 0],

    [1, 1, 1],
    [1, 0],
    [0, 1, 0],
    [0, 1],

    [1, 1, 1],
    [1, 1],
    [1, 0, 0],
    [0, 2],

    [1, 1, 1],
    [2, 0],
    [0, 0, 1],
    [1, 1],
]


def get_shapes(p):
    if p == 1:
        return [shapes[0], shapes[1]]
    elif p == 2:
        return [shapes[2]]
    elif p == 3:
        return [shapes[3], shapes[4]]
    elif p == 4:
        return [shapes[5], shapes[6]]
    elif p == 5:
        return [shapes[7], shapes[8], shapes[9], shapes[10]]
    elif p == 6:
        return [shapes[11], shapes[12], shapes[13], shapes[14]]
    elif p == 7:
        return [shapes[15], shapes[16], shapes[17], shapes[18]]
    

def ok(i, shape):
    start = fields[i] + shape[0]
    for j in range(1, len(shape)):
        if start != (fields[i+j] + shape[j]):
            return False
        
    return True


def solve(c, p):
    answer = 0
    shapes = get_shapes(p)
    for shape in shapes:
        for i in range(c - len(shape) + 1):
            if ok(i, shape):
                answer += 1
    return answer


c, p = map(int, input().split())

fields = list(map(int, input().split()))

print(solve(c, p)) 