import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
sset = sorted(set(lst))
dic = {sset[i]: i for i in range(len(sset))}

for num in lst:
    print(dic[num], end=" ")