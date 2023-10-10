import sys
input = sys.stdin.readline


def lcs(s1, s2, n1, n2):
    d = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])
    return d[n1][n2]


s1 = input().strip()
s2 = input().strip()

n1 = len(s1)
n2 = len(s2)

print(lcs(s1, s2, n1, n2))