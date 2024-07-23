import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sset = set(input().rstrip() for _ in range(N))

for _ in range(M):
    sset -= set(input().rstrip().split(","))
    print(len(sset))