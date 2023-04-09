k, n = map(int, input().split())

data = []
for _ in range(k):
    data.append(int(input()))
    
    
# 이분탐색
start, end = 1, max(data)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for x in data:
        cnt += x // mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)