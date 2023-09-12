import sys
input = sys.stdin.readline


def solution(start, end):
    while start <= end:
        mid = (start + end) // 2
        
        result = 0
        for tree in trees:
            if tree >= mid:
                result += (tree - mid)
                
        if result >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end
        
n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(1, max(trees)))