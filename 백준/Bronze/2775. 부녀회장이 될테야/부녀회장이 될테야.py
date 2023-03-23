t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    
    d = [[0] * (n) for _ in range(k+1)]
    d[0] = [i+1 for i in range(n)]
    
    for i in range(k):
        for j in range(n):
            d[i+1][j] = sum(d[i][:j+1])

    print(d[k][n-1])