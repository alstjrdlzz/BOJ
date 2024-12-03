import sys
input = sys.stdin.readline
from collections import defaultdict

M, N = map(int, input().split())

dic = defaultdict(int)
for _ in range(M):
    lst = list(map(int, input().split()))
    
    sorted_set = sorted(set(lst))
    
    rank_dict = {sorted_set[i]: i for i in range(len(sorted_set))}
    
    k = tuple(list(rank_dict[kg] for kg in lst))
    
    dic[k] += 1
    
ans = 0
for v in dic.values():
    ans += (v * (v - 1)) // 2 # 지을 수 있는 쌍의 갯수
    
print(ans)