import sys
input = sys.stdin.readline


a, b = map(int, input().split())
s_a = set(list(map(int, input().split())))
s_b = set(list(map(int, input().split())))

print(len(((s_a - s_b) | (s_b - s_a))))