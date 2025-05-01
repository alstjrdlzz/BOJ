import sys
input = sys.stdin.readline

def is_prime(n):
    arr = [i for i in range(n + 1)]
    end = int(n**1/2)
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n + 1, i):
            arr[j] = 0
    return [i for i in arr[2:] if arr[i]]


N = int(input())

if N == 1:
    print(0)
    exit()

arr = is_prime(N)

l, r = 0, 0
ans = 0
while r <= len(arr):
    tmp = sum(arr[l:r])
    if tmp <= N:
        if tmp == N:
            ans += 1
        r += 1
    else:
        l += 1
            
print(ans)