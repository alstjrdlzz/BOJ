import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
query = input().rstrip()
words = list(input().rstrip() for _ in range(N - 1))

cnt = 0
for word in words:
    if Counter(query) == Counter(word):
        cnt += 1
    elif len(query) >= len(word):
        if len(list((Counter(query) - Counter(word)).elements())) == 1:
            cnt += 1
    else:
        if len(list((Counter(word) - Counter(query)).elements())) == 1:
            cnt += 1
print(cnt)