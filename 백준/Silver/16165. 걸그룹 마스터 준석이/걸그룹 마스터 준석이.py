import sys
input = sys.stdin.readline
from collections import defaultdict

N, M = map(int, input().split())

dic = defaultdict(set)
for _ in range(N):
    team = input().rstrip()
    n = int(input())
    members = set([input().rstrip() for _ in range(n)])
    dic[team] = members

for _ in range(M):
    query = input().rstrip()
    cate = int(input())
    
    if cate == 1:
        for team, members in dic.items():
            if query in members:
                print(team)
                break
    else:
        for team, members in dic.items():
            if query == team:
                for member in sorted(members):
                    print(member)
                break