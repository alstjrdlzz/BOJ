import sys


input=sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(int(input()))

for x in sorted(data):
    print(x)