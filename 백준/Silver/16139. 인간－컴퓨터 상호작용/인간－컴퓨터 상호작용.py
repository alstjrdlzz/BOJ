from string import ascii_lowercase
from collections import defaultdict

s = input()
q = int(input())

# prefix_sum
prefix_sum = defaultdict(list)
for alpha in ascii_lowercase:
    prefix_sum[alpha].append(0)
    alpha_cnt = 0
    for i in range(len(s)):
        if s[i] == alpha:
            alpha_cnt += 1
        prefix_sum[alpha].append(alpha_cnt)
					
for _ in range(q):
    alpha, l, r = input().split()
    print(prefix_sum[alpha][int(r)+1] - prefix_sum[alpha][int(l)])