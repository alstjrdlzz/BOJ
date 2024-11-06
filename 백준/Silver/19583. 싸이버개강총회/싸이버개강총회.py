import sys
input = sys.stdin.readline

def hhmm_to_m(st):
    return int(st[:2]) * 60 + int(st[3:])

S, E, Q = input().split()
S = hhmm_to_m(S)
E = hhmm_to_m(E)
Q = hhmm_to_m(Q)

sset = set()
ans = 0
while 1:
    try:
        t, n = input().split()
        t = hhmm_to_m(t)
        
        if t <= S:
            sset.add(n)  
        elif n in sset and (E <= t <= Q):
            sset.remove(n)
            ans += 1
    except:
        break
        
print(ans)