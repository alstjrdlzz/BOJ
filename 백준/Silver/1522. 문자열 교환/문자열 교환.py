import sys
input = sys.stdin.readline

st = input().rstrip()
n = len(st)
window_size = st.count("a")
st += st[:n]

ans = 1001
for s in range(n):
    window = st[s:s+window_size]  
    ans = min(ans, window.count("b"))
    
print(ans)