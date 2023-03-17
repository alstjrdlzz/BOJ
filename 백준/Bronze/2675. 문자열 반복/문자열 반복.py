n = int(input())

for _ in range(n):
    r, s = input().split()
    
    result = ""
    for x in s:
        result += (x * int(r))
        
    print(result)
        
    