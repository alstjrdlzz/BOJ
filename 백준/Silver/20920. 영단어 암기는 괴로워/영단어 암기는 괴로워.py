import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = dict()
for i in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue
    
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
        
lst = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in lst:
    print(word) 