import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())

ans1 = 0
for x in lst:
    if x == 0:
        continue
    elif x <= T:
        ans1 += 1
    else:
        q, r = divmod(x, T)
        if r == 0:
            ans1 += q
        else:
            ans1 += (q + 1)
            
ans2, ans3 = divmod(N, P)

print(ans1)
print(ans2, ans3)