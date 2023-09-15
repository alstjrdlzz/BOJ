from itertools import combinations
import sys
input = sys.stdin.readline


def find_sub(S):
    res = []
    for i in range(0, len(S) + 1):
        for subsum in list(map(sum, combinations(S, i))):
            if subsum <= c:
                res.append(subsum)
    return res


def solution(S, cur):
    if cur > c:
        return 0
    
    start = 0
    end = len(S) - 1
    
    while start <= end:
        mid = (start + end) // 2
        target = cur + S[mid]
        
        if target <= c:
            start = mid + 1
        else:
            end = mid - 1
            
    return start


n, c = map(int, input().split())
S = list(map(int, input().split()))

A = S[:n // 2]
B = S[n // 2:]

sub_A = find_sub(A)
sub_B = find_sub(B)

sub_A.sort()

cnt = 0
for cur in sub_B:
    cnt += solution(sub_A, cur)

print(cnt)