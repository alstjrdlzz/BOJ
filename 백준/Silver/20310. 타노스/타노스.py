import sys
input = sys.stdin.readline


S = input().strip()

trg0 = S.count("0") // 2
trg1 = S.count("1") // 2

ans = ""
cnt0, cnt1 = 0, 0
for ch in S:
    if ch == "0":
        if cnt0 < trg0:
            ans += ch
            cnt0 += 1
    else:
        if cnt1 < trg1:
            cnt1 += 1
        else:
            ans += ch
print(ans)