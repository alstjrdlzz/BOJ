import sys
input = sys.stdin.readline

N = int(input())
lst = [input().rstrip() for _  in range(N)]

ans = ""
KBS1_idx = lst.index("KBS1")
lst.insert(0, lst.pop(KBS1_idx))
ans += ("1" * KBS1_idx + "4" * KBS1_idx)

KBS2_idx = lst.index("KBS2")
ans += ("1" * KBS2_idx + "4" * (KBS2_idx - 1))
print(ans)