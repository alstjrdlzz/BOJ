import sys
input = sys.stdin.readline

def convert(i):
    if lst[i - 1] == 1:
        lst[i - 1] = 0
    else:
        lst[i - 1] = 1
        
def search(mid):
    tlst = [mid]
    lo, hi = mid - 1, mid + 1
    while lo >= 1 and hi <= N:
        if lst[lo - 1] != lst[hi - 1]:
            break
        else:
            tlst += [lo, hi]
            
        lo -= 1
        hi += 1
            
    for i in tlst:
        convert(i)
        

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    g, n = map(int, input().split())
    if g == 1:
        for i in range(1, N + 1):
            if i % n == 0:
                convert(i)
    else:
        for i in range(1, N + 1):
            if i == n:
                search(i)

for i in range(0, len(lst), 20):
    print(*lst[i:i+20])