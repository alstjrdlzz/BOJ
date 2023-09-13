import sys
input = sys.stdin.readline


def compute_k_hat(x):
    k_hat = 0
    for i in range(1, n + 1):
        k_hat += min(x // i, n)
    return k_hat


n = int(input())
k = int(input())

def solution(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        
        k_hat = compute_k_hat(mid)
        
        if k_hat >= k:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer

print(solution(1, n ** 2))
