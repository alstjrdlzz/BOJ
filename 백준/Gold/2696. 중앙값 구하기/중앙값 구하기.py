import heapq
import sys
input = sys.stdin.readline


def solution(S):
    small = []
    big = []
    median = S[0]
    medians = [median]
    for i in range(1, len(S)):
        x = S[i]
        if x <= median:
            heapq.heappush(small, -x)
        else:
            heapq.heappush(big, x)
        
        if i % 2 == 0:
            if len(small) < len(big):
                heapq.heappush(small, -median)
                median = heapq.heappop(big)
            elif len(small) > len(big):
                heapq.heappush(big, median)
                median = -heapq.heappop(small)
            medians.append(median)
    return medians
         
    
t = int(input())
for _ in range(t):
    m = int(input())
    
    if m % 10 == 0:
        num_lines = m // 10
    else:
        num_lines = m // 10 + 1
        
    S = []
    for _ in range(num_lines):
        S.extend(list(map(int, input().split())))
    
    medians = solution(S)
    
    print(len(medians))
    
    cnt = 0
    for median in medians:
        print(median, end=" ")
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()