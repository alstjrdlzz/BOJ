import sys
input = sys.stdin.readline


s = input().rstrip()
n = len(s)

result = set()
for i in range(n):
    for j in range(n):
        result.add(s[j:j+i+1])

print(len(result))