n = int(input())
a = set(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

for x in data:
    if x in a:
        print(1)
    else:
        print(0)