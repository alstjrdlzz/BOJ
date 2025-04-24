import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

l, r = 0, 0
ans = 0
sset = set()
while l < N and r < N:
    if lst[r] not in sset:
        sset.add(lst[r])
        ans += r - l + 1
        r += 1
    else:
        while lst[r] in sset:
            sset.remove(lst[l])
            l += 1
print(ans)