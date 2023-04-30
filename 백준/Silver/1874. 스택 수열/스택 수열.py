n = int(input())
stack = []
answer = []
now = 0
for i in range(n):
    x = int(input())
    while now < x:
        now += 1
        stack.append(now)
        answer.append('+')
    temp = stack.pop()
    if temp == x:
        answer.append('-')
    else:
        stack.append(temp)
        print('NO')
        break
else:      
    for operator in answer:
        print(operator)