import sys
input = sys.stdin.readline


n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

answer = 0
for i in range(n):
    q, r = divmod(k, coins[i])
    answer += q
    k = r

print(answer)