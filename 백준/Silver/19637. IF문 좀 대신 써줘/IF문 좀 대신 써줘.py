import sys
input = sys.stdin.readline


def solution(power):
    start = 0
    end = n - 1
    answer = 0
    while (start <= end):
        mid = (start + end) // 2
        
        if thresholds[mid] >= power:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
    
    
n, m = map(int, input().split())

names = []
thresholds = []
for _ in range(n):
    data = input().split()
    names.append(data[0])
    thresholds.append(int(data[1]))
    
powers = []
for _ in range(m):
    powers.append(int(input()))

for p in powers:
    idx = solution(p)
    print(names[idx])
