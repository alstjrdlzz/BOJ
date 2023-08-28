import sys
input = sys.stdin.readline


n, m = map(int, input().split())

s1 = set()
for _ in range(n):
    s1.add(input().rstrip())

s2 = set()
for _ in range(m):
    s2.add(input().rstrip())

inter = list(s1 & s2)
inter.sort()
l = len(inter)
print(l)
for i in range(l):
    print(inter[i])