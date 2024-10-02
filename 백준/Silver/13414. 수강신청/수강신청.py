import sys
input = sys.stdin.readline
from collections import defaultdict

K, L = map(int, input().split())

dic = defaultdict(int)
for i in range(L):
    uid = input().rstrip()
    dic[uid] = i

lst = sorted(dic.items(), key=lambda x: x[1])
    
if len(lst) < K:
    K = len(lst)
    
for i in range(K):
    print(lst[i][0])   