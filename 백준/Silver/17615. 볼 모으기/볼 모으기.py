import sys
input = sys.stdin.readline

N = int(input())
st = input().rstrip()

def move(c, st):
    cut = st.lstrip(c)
    return cut.count(c)

print(min(
move("R", st),
move("R", st[::-1]),
move("B", st),
move("B", st[::-1])))