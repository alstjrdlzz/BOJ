import sys
input = sys.stdin.readline


def solution():
    d = [[0] * 10 for _ in range(n + 1)]
    
    for j in range(1, 10):
        d[1][j] = 1
        
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i - 1][j + 1]
            elif j == 9:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1] 
    return sum(d[n]) % 1000000000

n = int(input())
print(solution())