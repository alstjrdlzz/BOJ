import sys
from heapq import heappop, heappush


n = int(sys.stdin.readline().rstrip())
heap1 = []
heap2 = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heappush(heap1, x)
    elif x < 0:
        heappush(heap2, -x)
    else: # x == 0
        if not heap1 and not heap2:
            print(0)
        elif heap1 and not heap2:
            print(heappop(heap1))
        elif not heap1 and heap2:
            print(-heappop(heap2))
        else: # heap1 and heap2
            temp1 = heappop(heap1)
            temp2 = heappop(heap2)
            if temp1 == temp2:
                print(-temp2)
                heappush(heap1, temp1)
            elif temp1 > temp2:
                print(-temp2)
                heappush(heap1, temp1)
            else: # temp1 < temp2
                print(temp1)
                heappush(heap2, temp2)