import sys
input = sys.stdin.readline


def solution(S, start, end):
    answer = 0
    while (start <= end):
        mid = (start + end) // 2
        cur = S[0]
        cnt = 1
        for i in range(1, n):
            if S[i] - cur >= mid:
                cur = S[i]
                cnt += 1
                
        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


n, c = map(int, input().split())
X = [int(input()) for _ in range(n)]
        
X.sort()
print(solution(X, 1, X[-1] - X[0]))