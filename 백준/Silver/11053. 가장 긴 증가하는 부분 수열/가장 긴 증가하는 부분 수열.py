n = int(input())
data = list(map(int, input().split()))

d = [0] * n
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            if d[i] < d[j]:
                d[i] = d[j]
    d[i] += 1

print(max(d))