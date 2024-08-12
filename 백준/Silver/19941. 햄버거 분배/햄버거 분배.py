import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(input().rstrip())

ans = 0
for i in range(len(lst)):
    if lst[i] == "P":
        start = max(0, i - K)
        end = min(N - 1, i + K)
        for j in range(start, end + 1):
            if lst[j] == "H":
                lst[j] = "-"
                ans += 1
                break
print(ans)