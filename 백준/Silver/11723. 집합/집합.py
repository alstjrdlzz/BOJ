import sys
input = sys.stdin.readline


m = int(input())

s = set()
for _ in range(m):
    data = input().split()
    operator = data[0]
    if len(data) > 1:
        x = int(data[1])
    
    if operator == "add":
        s.add(x)
        
    elif operator == "remove":
        s.discard(x)
        
    elif operator == "toggle":
        if x in s:
            s.discard(x)
        else:
            s.add(x)
            
    elif operator == "check":
        if x in s:
            print(1)
        else:
            print(0)
            
    elif operator == "all":
        s = set([i for i in range(1, 21)])
        
    elif operator == "empty":
        s = set()