import sys
input = sys.stdin.readline

def solve(sset, G):
    nunique = len(sset)
    nplayer_dic = {"Y": 1, "F": 2, "O": 3}
    
    return nunique // nplayer_dic[G]


N, G = input().split()
N = int(N)
sset = set(input().rstrip() for _ in range(N))

print(solve(sset, G))