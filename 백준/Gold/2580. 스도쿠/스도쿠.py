import sys
input = sys.stdin.readline

def promise(num, ci, cj):
    # 행 체크
    if num in arr[ci]:
        return 0
    
    # 열 체크
    if num in [arr[i][cj] for i in range(9)]:
        return 0
    
    # 3x3 체크
    si, sj = (ci // 3 * 3), (cj // 3 * 3)
    for i in range(si, si + 3):
        for j in range(sj, sj + 3):
            if num == arr[i][j]:
                return 0
    return 1

def dfs(n):
    if n == 81:
        for i in range(9):
            print(*arr[i])
        exit()
        return
    
    ci, cj = divmod(n, 9)
    if arr[ci][cj] == 0:
        for i in range(1, 10):
            if promise(i, ci, cj):
                arr[ci][cj] = i
                dfs(n + 1)
                arr[ci][cj] = 0
    else:
        dfs(n + 1)

arr = [list(map(int, input().split())) for _ in range(9)]

dfs(0)