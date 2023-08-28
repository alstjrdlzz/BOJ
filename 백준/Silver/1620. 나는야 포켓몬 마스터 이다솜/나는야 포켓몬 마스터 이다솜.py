import sys
input = sys.stdin.readline


n, m = map(int, input().split())

id2name = {}
for i in range(1, n + 1):
    id2name[i] = input().rstrip()
    
name2id = {name: i for i, name in id2name.items()}

for _ in range(m):
    x = input().rstrip()
    if x.isalpha():
        print(name2id[x])
    else:
        print(id2name[int(x)])
