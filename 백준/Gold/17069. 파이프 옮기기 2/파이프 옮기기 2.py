import sys
input = sys.stdin.readline


def solution():
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1
    for i in range(2, n):
        if board[0][i] == 0:
            dp[0][i][0] = dp[0][i - 1][0]
    
    for r in range(1, n):
        for c in range(1, n):
            if (board[r][c] == 0):
                dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
                dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]
                if (board[r][c - 1] == 0) and (board[r - 1][c] == 0):
                    dp[r][c][2] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
                    
    return sum(dp[n - 1][n - 1])


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(solution())