import sys
input = sys.stdin.readline

def sol(st, ch, trg):
    cnt = 0
    i = 0
    while cnt < trg:
        if st[i] == ch:
            st = st[:i] + st[i + 1:]
            cnt += 1
        i += 1
    
    return st


S = input().strip()

cnt0, cnt1 = 0, 0
for ch in S:
    if ch == "0":
        cnt0 += 1
    else:
        cnt1 += 1

S = sol(S, "1", cnt1//2)
S = sol(S[::-1], "0", cnt0//2)

print(S[::-1])