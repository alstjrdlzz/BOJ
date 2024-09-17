import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    tmp = int(input())
    if tmp == 0:
        lst.pop()
    else:
        lst.append(tmp)
        
ans = sum(lst)
print(ans)