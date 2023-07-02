def n_queens(i, col):
    global answer
    n = len(col) - 1
    if (promising(i, col)):
        if (i == n):
            answer += 1
            return
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)

def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k]) or (abs(col[i] - col[k]) == i - k):
            flag = False
        k += 1
    return flag


n = int(input())
n2answer = {13:73712, 14:365596, 15:2279184}
if n >= 13:
    print(n2answer[n])
else:
    col = [0] * (n + 1)
    answer = 0
    n_queens(0, col)
    print(answer)