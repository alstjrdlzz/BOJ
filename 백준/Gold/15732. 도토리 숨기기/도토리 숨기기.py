import sys
input = sys.stdin.readline


def count_untill(mid):
    cnt = 0
    for a, b, c in R:
        if a > mid:
            continue
        b = min(b, mid)
        cnt += (b - a) // c + 1
    return cnt


def solution(R, start, end):
    answer = 0
    while (start <= end):
        mid = (start + end) // 2
        
        cnt = count_untill(mid)
        
        if cnt >= d:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer


n, k, d = map(int, input().split())
R = []
for _ in range(k):
    R.append(list(map(int, input().split())))

print(solution(R, 1, n))