import sys
input = sys.stdin.readline

N, T, P = map(int, input().split())

if N == 0:
    print(1)
else:
    lst = list(map(int, input().split()))
    if N == P and T <= lst[-1]:
        print(-1)
    
    else:
        cnt = 0
        for score in lst:
            if score > T:
                cnt += 1
        print(cnt + 1)