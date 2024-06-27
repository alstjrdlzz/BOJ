import sys
input = sys.stdin.readline

N = int(input())

lo = 1
ans = 1
while N > lo:
    lo += 6 * ans
    ans += 1
    
print(ans)