import sys
input = sys.stdin.readline


n, m = map(int, input().split())

site2password = {}
for _ in range(n):
    site, password = input().split()
    site2password[site] = password

for _ in range(m):
    site = input().rstrip()
    print(site2password[site])