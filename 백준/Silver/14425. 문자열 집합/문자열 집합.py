import sys
input = sys.stdin.readline


n, m = map(int, input().split())
s = set()
for _ in range(n):
    x = input()
    s.add(x)

answer = 0
for _ in range(m):
    x = input()
    if x in s:
        answer += 1

print(answer)