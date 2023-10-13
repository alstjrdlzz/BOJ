import sys
input = sys.stdin.readline


def get_stack(i):
    stack = []
    if i % 2 == 1:
        # 하 i번
        for _ in range(i):
            stack.append((1, 0))
        # 우 i번
        for _ in range(i):
            stack.append((0, 1))
        # 상 1번
        stack.append((-1, 0))
    else:
        # 상 i번
        for _ in range(i):
            stack.append((-1, 0))
        # 좌 i번
        for _ in range(i):
            stack.append((0, -1))
        # 하 1번
        stack.append((1, 0))
    return stack
   

# 입력
n = int(input())
m = int(input())

# 표 초기화
table = [[0] * n for _ in range(n)]

# 좌표 초기화
x = n // 2
y = (n - 1) // 2
table[x][y] = 1

# 표 채우기
ans = []
for i in range(1, n):
    start = i ** 2 + 1
    end = (i + 1) ** 2
    stack = get_stack(i)
    for num in range(start, end + 1):
        dx, dy = stack.pop()
        x += dx
        y += dy
        table[x][y] = num
        if num == m:
            ans.append(x + 1)
            ans.append(y + 1)
# 출력
for row in table:
    print(*row)

if m == 1:
    ans = [n // 2 + 1, (n - 1) // 2 + 1]
    
print(*ans)