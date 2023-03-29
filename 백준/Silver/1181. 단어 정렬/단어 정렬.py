n = int(input())

data = []
for _ in range(n):
    data.append(input())

data = list(set(data))

answer = []
for x in data:
    answer.append((len(x), x))
    
answer = sorted(answer)

for length, x in answer:
    print(x)