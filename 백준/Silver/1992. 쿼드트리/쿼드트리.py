import sys
input = sys.stdin.readline

def check(n, si, sj):
    c = img[si][sj]
    for i in range(si, si + n):
        for j in range(sj, sj + n):
            if img[i][j] != c:
                return False
    return True


def compress(n, si, sj):
    global ans
    
    if n == 1:
        ans += img[si][sj]
        return
    
    if check(n, si, sj):
        ans += img[si][sj]
        return
    
    p1 = (si, sj)
    p2 = (si, sj + n // 2)
    p3 = (si + n // 2, sj)
    p4 = (si + n // 2, sj + n // 2)
    
    half = n // 2
    
    ans += "("
    for si, sj in (p1, p2, p3, p4):
        compress(half, si, sj)
    ans += ")"
    

N = int(input())
img = [list(input().rstrip()) for _ in range(N)]

ans = ""
compress(N, 0, 0)
print(ans)  