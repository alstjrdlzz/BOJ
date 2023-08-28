import sys
input = sys.stdin.readline


n = int(input())

s = set()
for _ in range(n):
    x, operator = input().split()
    if operator == "enter":
        s.add(x)
    else:
        s.discard(x)

s_list = list(s)
s_list.sort(reverse=True)
for x in s_list:
    print(x)