n = int(input())

for i in range(n):
    data = input()
    
    score, cnt = 0, 0
    for d in data:
        if d == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)