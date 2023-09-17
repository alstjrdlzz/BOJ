import sys
input = sys.stdin.readline


def cal_total_len(mid):
    l = 0
    for tree in trees:
        if tree >= mid:
            l += (tree - mid)
    return l


def solution(start, end):
    answer = 0
    while (start <= end):
        mid = (start + end) // 2
        
        l = cal_total_len(mid)
        
        if l >= m:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(1, max(trees)))
