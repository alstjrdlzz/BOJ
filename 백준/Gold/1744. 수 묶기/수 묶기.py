import sys
input = sys.stdin.readline

def sol(arr):
    ret = 0
    while arr:
        if len(arr) >= 2:
            ret += arr.pop() * arr.pop()
        else:
            ret += arr.pop()   
    return ret


N = int(input())
ans, neg, pos = 0, [], []
for _ in range(N):
    z = int(input())
    if z <= 0:
        neg.append(z)
    elif z == 1:
        ans += z
    else:
        pos.append(z)
        
pos.sort(reverse=False) # 양수는 오름차순 정렬
neg.sort(reverse=True)  # 음수는 내림차순 정렬

ans += sol(pos) + sol(neg)

print(ans)