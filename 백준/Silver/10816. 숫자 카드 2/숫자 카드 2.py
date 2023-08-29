import sys
from collections import Counter
input = sys.stdin.readline


n = int(input())
cnt_dic = Counter(list(map(int, input().split())))

m = int(input())
query = list(map(int, input().split()))

for i in range(m):
    print(cnt_dic[query[i]], end=" ")
