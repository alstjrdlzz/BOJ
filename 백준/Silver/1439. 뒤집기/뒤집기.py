import sys
input = sys.stdin.readline


st = input().strip()

cnt = 0
old = ""
for ch in st:
    if ch != old:
        cnt += 1
        old = ch
        
print(cnt // 2)      