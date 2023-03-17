x = {}
for i in range(9):
    x[i+1] = int(input())
    
sorted_x = sorted(x.items(), key=lambda x: x[1])

print(sorted_x[8][1])
print(sorted_x[8][0])