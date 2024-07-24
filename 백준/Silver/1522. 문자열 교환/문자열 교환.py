import sys
input = sys.stdin.readline

st = input().rstrip()

n = len(st)

ans = 1001
for s in range(n):
    e = s + st.count("a")
    
    if e > n:
        window = st[s:n] + st[:e - n]
    else:
        window = st[s:e]
        
    ans = min(ans, window.count("b"))
    
print(ans)