n = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

i = 0
j = n-1
answer = 0
while i < j:
    if a[i] + a[j] < x:
        i += 1
    elif a[i] + a[j] > x:
        j -= 1
    else:
        answer += 1
        i += 1
        j -= 1
        
print(answer)