import sys
input = sys.stdin.readline


N, X = map(int, input().split())
lst = list(map(int, input().split())) 
    
max_sum = sum(lst[:X])
sum_value = max_sum
cnt = 1
for i in range(N - X):
    sum_value -= lst[i]
    sum_value += lst[i + X]
    
    if sum_value > max_sum:
        max_sum = sum_value
        cnt = 1
    elif sum_value == max_sum:
        cnt += 1
        
if max_sum == 0:
    print("SAD")
else:
    print(f"{max_sum} {cnt}")