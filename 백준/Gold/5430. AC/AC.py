import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    P = input().rstrip()
    N = int(input())
    st = input().rstrip()
    
    if not st[1:-1]:
        q = deque([])
    else:
        q = deque(list(map(int, st[1:-1].split(","))))
    
    flag = 0
    cnt = 0
    for c in P:
        if c == "R":
            cnt += 1
        elif c == "D":
            if not q:
                flag = 1
                break
            elif cnt % 2 == 0:
                q.popleft()
            elif cnt % 2 == 1:
                q.pop()
                
    if flag:
        print("error")
    else:
        if cnt % 2 == 0:
            print("["+",".join(list(map(str, list(q))))+"]")
        else:
            print("["+",".join(list(map(str, list(q)[::-1])))+"]")