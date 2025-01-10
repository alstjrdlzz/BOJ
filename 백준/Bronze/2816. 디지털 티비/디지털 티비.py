import sys
input = sys.stdin.readline

N = int(input())
lst = [input().rstrip() for _  in range(N)]

ans = ""
kbs1_idx = lst.index("KBS1")
lst.insert(0, lst.pop(kbs1_idx))
ans += ("1" * kbs1_idx + "4" * kbs1_idx)

kbs2_idx = lst.index("KBS2")
ans += ("1" * kbs2_idx + "4" * (kbs2_idx - 1))
print(ans)