import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dic = {}
for _ in range(N):
    nid, g, s, b = map(int, input().split())
    dic[nid] = (g, s, b)
    
kg, ks, kb = dic[K]    
cnt = 0
for cid in range(1, N + 1):
    if cid == K:
        continue
        
    cg, cs, cb = dic[cid]
    if cg > kg:
        cnt += 1
        break
    elif (cg == kg) and (cs > ks):
        cnt += 1
        break
    elif (cs == ks) and (cb > kb):
        cnt += 1
        break

print(cnt + 1)