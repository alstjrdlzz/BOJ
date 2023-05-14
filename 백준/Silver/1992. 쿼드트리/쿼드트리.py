n = int(input())
image = []
for _ in range(n):
		image.append(input())

answer = ""
def compress(x, y, n):
    global answer
    for i in range(x, x+n):
        for j in range(y, y+n):
            if image[i][j] != image[x][y]:
                answer+='('
                compress(x, y, n//2)
                compress(x, y+n//2, n//2)
                compress(x+n//2, y, n//2)
                compress(x+n//2, y+n//2, n//2)
                answer+=')'
                return
    answer+=(str(image[x][y]))
    
compress(0, 0, n)
print(answer)