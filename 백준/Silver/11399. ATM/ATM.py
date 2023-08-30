import sys
input = sys.stdin.readline


n = int(input())
data = list(map(int, input().split()))

data.sort()

answer = 0
for i in range(n):
    answer += data[i] * (n - i)
    
print(answer)