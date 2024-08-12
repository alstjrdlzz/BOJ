import sys
input = sys.stdin.readline

st = input().rstrip()

ans = 0
idx = 0
while 1:
    ans += 1
    for ch in str(ans):
        if st[idx] == ch:
            idx += 1
            if idx >= len(st):
                print(ans)
                break
    else:
        continue
    break