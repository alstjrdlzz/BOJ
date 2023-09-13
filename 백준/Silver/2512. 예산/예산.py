import sys
input = sys.stdin.readline


def solution(S, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        total = 0
        for x in S:
            total += min(x, mid)
       
        if total <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


n = int(input())
S = list(map(int, input().split()))
m = int(input())

print(solution(S, 0, max(S)))