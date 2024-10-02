import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

tab = []
ans = 0
for i in range(K):
    # 해당 전기용품이 이미 멀티탭에 꽂혀있으면 continue
    if lst[i] in tab:
        continue
        
    # 멀티탭에 빈 자리가 있으면 해당 전기용품을 꽂고 continue
    if len(tab) < N:
        tab.append(lst[i])
        continue
        
    # 뽑을 전기용품 찾기
    ids = []
    for j in range(len(tab)):
        try:
            idx = lst[i:].index(tab[j])
        except:
            idx = 101
        ids.append(idx)
        
    tab[ids.index(max(ids))] = lst[i]
    ans += 1
    
print(ans)