from collections import Counter


s = input()
q = int(input())
for _ in range(q):
    alpha, l, r = input().split()
    print(Counter(s[int(l):int(r)+1])[alpha])