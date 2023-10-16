import sys
input = sys.stdin.readline


def get_xy(k):
    return k // 2 + 1, (k - 1) // 2 + 1


def get_ans1(k, x, y):
    dm, dn = m - k , n - k
    if (k % 2 == 1) and (dm > 0):
        return 2 * (k - 1) + 1
    elif (k % 2 == 0) and (dm > 0):
        return 2 * (k - 1) + 1
    else:
        return 2 * (k - 1)
    

def get_ans2(k, x, y):
    dm, dn = m - k , n - k
    if (k % 2 == 1) and (dn > 0):
        return (x, y + dn)
    elif (k % 2 == 1) and (dm > 0):
        return (x + dm, y)
    else:
        return (x, y)
    

m, n = map(int, input().split())

k = min(m, n)
x, y = get_xy(k)
ans1 = get_ans1(k, x, y)
ans2 = get_ans2(k, x, y)

print(f"{ans1}")
print(f"{ans2[0]} {ans2[1]}")