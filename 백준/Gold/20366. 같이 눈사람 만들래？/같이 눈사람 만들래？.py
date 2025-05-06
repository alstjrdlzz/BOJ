import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
H.sort()

ans = 2 * (int(1e9) - 1)
for i in range(N - 3):
    for j in range(i + 3, N):
        target = H[i] + H[j]
        l = i + 1
        r = j - 1
        while l < r:
            x = H[l] + H[r]
            diff = abs(target - x)
            ans = min(ans, diff)
            if x >= target:
                if x == target:
                    print(0)
                    exit()
                r -= 1
            else:
                l += 1
                
print(ans)
