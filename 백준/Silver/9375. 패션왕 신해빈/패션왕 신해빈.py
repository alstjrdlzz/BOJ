import sys
input = sys.stdin.readline
from collections import defaultdict

TC = int(input())
for _ in range(TC):
    N = int(input())
    
    dic = defaultdict(list)
    for _ in range(N):
        v, k = input().split()
        dic[k].append(v)
    
    ans = 1
    for k, v in dic.items():
        ans *= (len(v) + 1)
        
    print(ans - 1)