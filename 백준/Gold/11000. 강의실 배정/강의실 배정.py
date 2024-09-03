import sys
input = sys.stdin.readline
import heapq

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

lst.sort() # 시작시간이 빠른 순으로 정렬

h = []
heapq.heappush(h, lst[0][1])

for i in range(1, N):
    if lst[i][0] < h[0]:         # 강의 시작시간이 빠르면 강의실 추가
        heapq.heappush(h, lst[i][1])
    else:                           # 강의 시작시간이 늦으면 기존 강의실에서 강의
        heapq.heappop(h)
        heapq.heappush(h, lst[i][1])
        
print(len(h))