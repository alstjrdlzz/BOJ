import sys
input = sys.stdin.readline


n = int(input())
s = set(list(map(int, input().split())))

m = int(input())
data = list(map(int, input().split()))
for x in data:
    if x in s:
        print(1, end=" ")
    else:
        print(0, end=" ")
