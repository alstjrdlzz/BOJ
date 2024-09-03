import sys
input = sys.stdin.readline
import heapq

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]

lst.sort() # 시작시간이 빠른 순으로 정렬

h = []
heapq.heappush(h, lst[0][1])

for i in range(1, N):
    if lst[i][0] < h[0]:             # T_top <= S_i --> 같이 들을 수 있음
        heapq.heappush(h, lst[i][1])
    else:                            # 새로운 강의실에 배정
        heapq.heappop(h)
        heapq.heappush(h, lst[i][1])
        
print(len(h))