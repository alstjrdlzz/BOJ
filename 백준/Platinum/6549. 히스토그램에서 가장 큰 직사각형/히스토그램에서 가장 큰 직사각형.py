def sol(left, right):
    if left == right:
        return h[left]
    
    mid = (left + right) // 2
    
    ans = max(sol(left, mid), sol(mid + 1, right))
    
    # 양쪽 부분 문제에 걸쳐있는 경우
    lo, hi = mid, mid + 1
    height = min(h[lo], h[hi])
    ans = max(ans, 2 * height) # 너비가 2인 직사각형부터 시작해서 너비가 n이 될 때까지 체크
    while left < lo or hi < right:
        # 항상 높이가 더 높은 쪽으로 확장
        if hi < right and (lo == left or h[lo - 1] < h[hi + 1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])    
        # 확장한 후 사각형의 넓이
        ans = max(ans, (hi - lo + 1) * height)    
    return ans


while True:
    n, *h = list(map(int, input().split()))
    if n == 0:
        break
    print(sol(0, n - 1))